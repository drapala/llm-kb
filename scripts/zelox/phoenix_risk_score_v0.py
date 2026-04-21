#!/usr/bin/env python3
"""
Calibrate and score a Phoenix Risk Score v0 using explicit statistical weights.

Method:
- candidate features chosen ex ante from tested, non-leaky structural/behavioral features
- log / sign transforms to stabilize skew and align higher = riskier
- stratified K-fold cross-validation
- balanced-class ridge logistic regression
- select lambda by lowest mean log loss
- fit final model on full dataset and generate ranking
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sqlite3
from pathlib import Path

import numpy as np

from phoenix_feature_falsification import build_temp_tables, load_supplier_metrics, row_factory


CANDIDATE_FEATURES = [
    {
        "name": "sanction_scope_score",
        "source": "sanction_scope_score",
        "transform": "log1p",
        "rationale": "gravidade e abrangencia da rede sancionada",
    },
    {
        "name": "same_socio_multi_flag",
        "source": "same_socio_sanction_count",
        "transform": "ge2_flag",
        "rationale": "multiplicidade de firmas sancionadas ligadas ao mesmo socio (threshold empiricamente apoiado)",
    },
    {
        "name": "qsa_proximity_score",
        "source": "min_abs_days_to_qsa_change",
        "transform": "neg_log1p",
        "rationale": "mudanca de QSA mais proxima da sancao = maior risco",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--json-output", required=True)
    parser.add_argument("--md-output", required=True)
    parser.add_argument("--csv-output", required=True)
    return parser.parse_args()


def apply_transform(name: str, value: float | int | None) -> float:
    if value is None:
        return math.nan
    x = float(value)
    if name == "log1p":
        return math.log1p(max(x, 0.0))
    if name == "ge2_flag":
        return 1.0 if x >= 2.0 else 0.0
    if name == "neg_log1p":
        return -math.log1p(max(x, 0.0))
    return x


def build_matrix(rows: list[dict]) -> tuple[list[str], np.ndarray, np.ndarray]:
    ids = [row["successor_cnpj"] for row in rows]
    y = np.array([row["created_post_sanction"] for row in rows], dtype=float)
    cols = []
    for spec in CANDIDATE_FEATURES:
        col = np.array([apply_transform(spec["transform"], row.get(spec["source"])) for row in rows], dtype=float)
        cols.append(col)
    X = np.column_stack(cols)
    return ids, X, y


def impute_and_standardize_fit(X: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    means = np.nanmean(X, axis=0)
    X_imputed = np.where(np.isnan(X), means, X)
    stds = X_imputed.std(axis=0)
    stds = np.where(stds == 0, 1.0, stds)
    X_scaled = (X_imputed - means) / stds
    return X_scaled, means, stds


def sigmoid(z: np.ndarray) -> np.ndarray:
    z = np.clip(z, -30, 30)
    return 1.0 / (1.0 + np.exp(-z))


def fit_ridge_logistic(
    X: np.ndarray,
    y: np.ndarray,
    sample_weight: np.ndarray,
    reg_lambda: float,
    max_iter: int = 100,
    tol: float = 1e-6,
) -> np.ndarray:
    n, p = X.shape
    X1 = np.column_stack([np.ones(n), X])
    beta = np.zeros(p + 1, dtype=float)
    ridge = np.eye(p + 1, dtype=float)
    ridge[0, 0] = 0.0

    for _ in range(max_iter):
        logits = X1 @ beta
        probs = sigmoid(logits)
        W = sample_weight * probs * (1.0 - probs)
        grad = X1.T @ (sample_weight * (probs - y)) + reg_lambda * (ridge @ beta)
        hess = X1.T @ (W[:, None] * X1) + reg_lambda * ridge + 1e-6 * np.eye(p + 1)
        step = np.linalg.solve(hess, grad)
        beta_next = beta - step
        if np.max(np.abs(step)) < tol:
            beta = beta_next
            break
        beta = beta_next
    return beta


def predict_proba(beta: np.ndarray, X: np.ndarray) -> np.ndarray:
    X1 = np.column_stack([np.ones(len(X)), X])
    return sigmoid(X1 @ beta)


def balanced_weights(y: np.ndarray) -> np.ndarray:
    pos = max(float((y == 1).sum()), 1.0)
    neg = max(float((y == 0).sum()), 1.0)
    n = len(y)
    w_pos = n / (2.0 * pos)
    w_neg = n / (2.0 * neg)
    return np.where(y == 1, w_pos, w_neg)


def log_loss(y: np.ndarray, p: np.ndarray) -> float:
    p = np.clip(p, 1e-8, 1 - 1e-8)
    return float(-(y * np.log(p) + (1 - y) * np.log(1 - p)).mean())


def brier_score(y: np.ndarray, p: np.ndarray) -> float:
    return float(np.mean((p - y) ** 2))


def roc_auc(y: np.ndarray, p: np.ndarray) -> float:
    order = np.argsort(p)
    ranks = np.empty_like(order, dtype=float)
    ranks[order] = np.arange(1, len(p) + 1, dtype=float)
    pos = y == 1
    n_pos = pos.sum()
    n_neg = (~pos).sum()
    if n_pos == 0 or n_neg == 0:
        return math.nan
    sum_ranks_pos = ranks[pos].sum()
    return float((sum_ranks_pos - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg))


def stratified_kfold(y: np.ndarray, k: int = 5, seed: int = 42) -> list[tuple[np.ndarray, np.ndarray]]:
    rng = np.random.default_rng(seed)
    pos_idx = np.where(y == 1)[0]
    neg_idx = np.where(y == 0)[0]
    rng.shuffle(pos_idx)
    rng.shuffle(neg_idx)
    pos_folds = np.array_split(pos_idx, k)
    neg_folds = np.array_split(neg_idx, k)
    folds = []
    all_idx = np.arange(len(y))
    for i in range(k):
        val_idx = np.concatenate([pos_folds[i], neg_folds[i]])
        train_mask = np.ones(len(y), dtype=bool)
        train_mask[val_idx] = False
        train_idx = all_idx[train_mask]
        folds.append((train_idx, val_idx))
    return folds


def cross_validate(X: np.ndarray, y: np.ndarray, lambdas: list[float]) -> dict:
    folds = stratified_kfold(y, k=5, seed=42)
    results = []
    for reg_lambda in lambdas:
        fold_metrics = []
        for train_idx, val_idx in folds:
            X_train_raw, X_val_raw = X[train_idx], X[val_idx]
            y_train, y_val = y[train_idx], y[val_idx]
            X_train, means, stds = impute_and_standardize_fit(X_train_raw)
            X_val = np.where(np.isnan(X_val_raw), means, X_val_raw)
            X_val = (X_val - means) / stds
            weights = balanced_weights(y_train)
            beta = fit_ridge_logistic(X_train, y_train, weights, reg_lambda)
            probs = predict_proba(beta, X_val)
            fold_metrics.append(
                {
                    "log_loss": log_loss(y_val, probs),
                    "brier": brier_score(y_val, probs),
                    "auc": roc_auc(y_val, probs),
                }
            )
        results.append(
            {
                "lambda": reg_lambda,
                "mean_log_loss": round(float(np.mean([m["log_loss"] for m in fold_metrics])), 6),
                "mean_brier": round(float(np.mean([m["brier"] for m in fold_metrics])), 6),
                "mean_auc": round(float(np.nanmean([m["auc"] for m in fold_metrics])), 6),
                "folds": fold_metrics,
            }
        )
    best = min(results, key=lambda x: (x["mean_log_loss"], -x["mean_auc"]))
    return {"grid": results, "selected": best}


def fit_final_model(X: np.ndarray, y: np.ndarray, reg_lambda: float) -> dict:
    X_scaled, means, stds = impute_and_standardize_fit(X)
    weights = balanced_weights(y)
    beta = fit_ridge_logistic(X_scaled, y, weights, reg_lambda)
    probs = predict_proba(beta, X_scaled)
    return {
        "beta": beta,
        "means": means,
        "stds": stds,
        "probs": probs,
        "train_log_loss": log_loss(y, probs),
        "train_brier": brier_score(y, probs),
        "train_auc": roc_auc(y, probs),
    }


def compute_ranking(rows: list[dict], X: np.ndarray, ids: list[str], model: dict) -> list[dict]:
    means = model["means"]
    stds = model["stds"]
    beta = model["beta"]
    X_imputed = np.where(np.isnan(X), means, X)
    X_scaled = (X_imputed - means) / stds
    probs = predict_proba(beta, X_scaled)
    intercept = float(beta[0])
    coef = beta[1:]

    ranked = []
    for idx, row in enumerate(rows):
        z = X_scaled[idx]
        contributions = {spec["name"]: round(float(coef[j] * z[j]), 6) for j, spec in enumerate(CANDIDATE_FEATURES)}
        ranked.append(
            {
                "successor_cnpj": ids[idx],
                "score_evasao_v0": round(float(probs[idx]), 6),
                "raw_logit": round(float(intercept + np.dot(coef, z)), 6),
                "created_post_sanction": int(row["created_post_sanction"]),
                "any_extreme_additive": int(row["any_extreme_additive"]),
                "score_extracao_v0": int(row["any_extreme_additive"]),
                "extreme_additive_gt50_count": row["extreme_additive_gt50_count"],
                "extreme_additive_gt100_count": row["extreme_additive_gt100_count"],
                "max_delta_valor": row["max_delta_valor"],
                "sanction_scope_score": row["sanction_scope_score"],
                "same_socio_sanction_count": row["same_socio_sanction_count"],
                "min_abs_days_to_qsa_change": row["min_abs_days_to_qsa_change"],
                "post_contracts_total": row["post_contracts_total"],
                "feature_contributions": contributions,
            }
        )
    ranked.sort(key=lambda x: x["score_evasao_v0"], reverse=True)
    for i, item in enumerate(ranked, start=1):
        item["rank"] = i
    return ranked


def build_payload(db_path: str, rows: list[dict], ids: list[str], cv: dict, model: dict, ranking: list[dict]) -> dict:
    beta = model["beta"]
    weights = []
    for i, spec in enumerate(CANDIDATE_FEATURES, start=1):
        weights.append(
            {
                "feature": spec["name"],
                "source": spec["source"],
                "transform": spec["transform"],
                "rationale": spec["rationale"],
                "weight_zspace": round(float(beta[i]), 6),
                "center_full_sample": round(float(model["means"][i - 1]), 6),
                "scale_full_sample": round(float(model["stds"][i - 1]), 6),
            }
        )
    return {
        "meta": {
            "db": db_path,
            "n_suppliers": len(rows),
            "n_positive_created_post_sanction": int(sum(row["created_post_sanction"] for row in rows)),
            "target": "created_post_sanction",
            "method": "balanced ridge logistic regression with 5-fold stratified CV and lambda selected by lowest mean log loss",
            "architecture": {
                "score_evasao_v0": "prospective detection score calibrated on structural signals",
                "score_extracao_v0": "monitoring flag derived from observed extreme additive tail"
            },
        },
        "cross_validation": cv,
        "final_model": {
            "intercept": round(float(beta[0]), 6),
            "train_log_loss": round(float(model["train_log_loss"]), 6),
            "train_brier": round(float(model["train_brier"]), 6),
            "train_auc": round(float(model["train_auc"]), 6),
            "weights": weights,
        },
        "top_50": ranking[:50],
        "ranking_size": len(ranking),
    }


def render_markdown(payload: dict) -> str:
    meta = payload["meta"]
    cv = payload["cross_validation"]["selected"]
    model = payload["final_model"]
    top = payload["top_50"][:20]

    lines = [
        "# Phoenix Risk Score v0",
        "",
        "Arquitetura: dois scores separados.",
        "",
        "- `score_evasao_v0`: regressao logistica ridge com classes balanceadas, 5-fold stratified CV e escolha de `lambda` por menor `log loss` medio fora da amostra.",
        "- `score_extracao_v0`: monitor de fase 2 baseado no `extreme_additive_tail` ja observado; nao entra na calibracao prospectiva.",
        "",
        "## Calibration",
        "",
        f"- alvo: `{meta['target']}`",
        f"- amostra: `{meta['n_suppliers']}` suppliers, com `{meta['n_positive_created_post_sanction']}` positivos",
        f"- lambda selecionado: `{cv['lambda']}`",
        f"- CV mean log loss: `{cv['mean_log_loss']}`",
        f"- CV mean Brier: `{cv['mean_brier']}`",
        f"- CV mean AUC: `{cv['mean_auc']}`",
        "",
        "## Weights",
        "",
        f"- intercept: `{model['intercept']}`",
    ]

    for weight in model["weights"]:
        lines.append(
            f"- `{weight['feature']}` ({weight['transform']} de `{weight['source']}`): weight = `{weight['weight_zspace']}`; center = `{weight['center_full_sample']}`; scale = `{weight['scale_full_sample']}`."
        )

    lines.extend(
        [
            "",
            "Formula operacional:",
            "",
            "`score_evasao_v0 = sigmoid(intercept + sum(weight_i * z_i))`, onde `z_i = (feature_transformada - center_i) / scale_i`.",
            "",
            "## Ranking",
            "",
            "| Rank | CNPJ | Evasao | Extracao | Genuine | Contracts |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )

    for row in top:
        lines.append(
            f"| {row['rank']} | `{row['successor_cnpj']}` | {row['score_evasao_v0']:.4f} | {row['score_extracao_v0']} | {row['created_post_sanction']} | {row['post_contracts_total']} |"
        )

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `category_shift_from_mother` ficou fora do v0 principal. O resultado atual sugere usar a feature invertida em uma proxima iteracao, se a amostra confirmar.",
            "- `score_evasao_v0` foi calibrado para `created_post_sanction`, nao para `any_extreme_additive`.",
            "- Features outcome-leaky para fase 2 ficaram fora da calibracao principal.",
            "- `score_extracao_v0` e um monitor observado de escalacao, nao um modelo prospectivo.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_csv(ranking: list[dict], path: Path) -> None:
    fieldnames = [
        "rank",
        "successor_cnpj",
        "score_evasao_v0",
        "score_extracao_v0",
        "raw_logit",
        "created_post_sanction",
        "any_extreme_additive",
        "extreme_additive_gt50_count",
        "extreme_additive_gt100_count",
        "max_delta_valor",
        "sanction_scope_score",
        "same_socio_sanction_count",
        "min_abs_days_to_qsa_change",
        "post_contracts_total",
    ]
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in ranking:
            writer.writerow({key: row[key] for key in fieldnames})


def main() -> int:
    args = parse_args()
    conn = sqlite3.connect(args.db)
    conn.row_factory = row_factory
    conn.execute("PRAGMA temp_store = MEMORY")
    conn.execute("PRAGMA mmap_size = 268435456")
    conn.execute("PRAGMA cache_size = -200000")

    build_temp_tables(conn)
    rows = load_supplier_metrics(conn)
    ids, X, y = build_matrix(rows)
    lambdas = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0]
    cv = cross_validate(X, y, lambdas)
    model = fit_final_model(X, y, cv["selected"]["lambda"])
    ranking = compute_ranking(rows, X, ids, model)
    payload = build_payload(args.db, rows, ids, cv, model, ranking)

    json_path = Path(args.json_output)
    md_path = Path(args.md_output)
    csv_path = Path(args.csv_output)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(payload))
    write_csv(ranking, csv_path)

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Wrote {csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
