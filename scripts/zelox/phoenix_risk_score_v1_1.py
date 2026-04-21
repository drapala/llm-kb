#!/usr/bin/env python3
"""
Phoenix Risk Score v1.1

Hierarchical architecture:
1. structural model -> score_evasao_structural
2. dormant-activation model -> score_dormant_activation
3. combiner model on submodel logits -> score_evasao_v1_1
4. score_extracao_v1_1 remains observed phase-2 monitor
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


STRUCTURAL_FEATURES = [
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
        "rationale": "multiplicidade de firmas sancionadas ligadas ao mesmo socio",
    },
    {
        "name": "qsa_proximity_score",
        "source": "min_abs_days_to_qsa_change",
        "transform": "neg_log1p",
        "rationale": "mudanca de QSA mais proxima da sancao",
    },
]

DORMANT_FEATURES = [
    {
        "name": "activation_lag_years",
        "source": "activation_lag_years",
        "transform": "log1p",
        "rationale": "entidade antiga ativada tardiamente",
    },
    {
        "name": "sanction_activation_proximity_score",
        "source": "post_sanction_activation_gap_days",
        "transform": "neg_abs_log1p",
        "rationale": "ativacao proxima da janela da sancao",
    },
    {
        "name": "buyer_burst_90d",
        "source": "buyer_burst_90d",
        "transform": "log1p",
        "rationale": "explosao de compradores logo apos ativacao",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--json-output", required=True)
    parser.add_argument("--md-output", required=True)
    parser.add_argument("--csv-output", required=True)
    parser.add_argument("--laudo-template-output", required=True)
    return parser.parse_args()


def transform_value(kind: str, value: float | int | None) -> float:
    if value is None:
        return math.nan
    x = float(value)
    if kind == "log1p":
        return math.log1p(max(x, 0.0))
    if kind == "ge2_flag":
        return 1.0 if x >= 2.0 else 0.0
    if kind == "neg_log1p":
        return -math.log1p(max(x, 0.0))
    if kind == "neg_abs_log1p":
        return -math.log1p(abs(x))
    return x


def build_feature_matrix(rows: list[dict], specs: list[dict]) -> np.ndarray:
    cols = []
    for spec in specs:
        col = np.array(
            [transform_value(spec["transform"], row.get(spec["source"])) for row in rows],
            dtype=float,
        )
        cols.append(col)
    return np.column_stack(cols)


def impute_and_scale_fit(X: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    means = np.nanmean(X, axis=0)
    X_imp = np.where(np.isnan(X), means, X)
    stds = X_imp.std(axis=0)
    stds = np.where(stds == 0, 1.0, stds)
    return (X_imp - means) / stds, means, stds


def impute_and_scale_apply(X: np.ndarray, means: np.ndarray, stds: np.ndarray) -> np.ndarray:
    X_imp = np.where(np.isnan(X), means, X)
    return (X_imp - means) / stds


def sigmoid(z: np.ndarray) -> np.ndarray:
    z = np.clip(z, -30.0, 30.0)
    return 1.0 / (1.0 + np.exp(-z))


def logit(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-8, 1 - 1e-8)
    return np.log(p / (1 - p))


def balanced_weights(y: np.ndarray) -> np.ndarray:
    pos = max(float((y == 1).sum()), 1.0)
    neg = max(float((y == 0).sum()), 1.0)
    n = len(y)
    return np.where(y == 1, n / (2.0 * pos), n / (2.0 * neg))


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
        probs = sigmoid(X1 @ beta)
        w = sample_weight * probs * (1.0 - probs)
        grad = X1.T @ (sample_weight * (probs - y)) + reg_lambda * (ridge @ beta)
        hess = X1.T @ (w[:, None] * X1) + reg_lambda * ridge + 1e-6 * np.eye(p + 1)
        step = np.linalg.solve(hess, grad)
        beta_next = beta - step
        if np.max(np.abs(step)) < tol:
            beta = beta_next
            break
        beta = beta_next
    return beta


def predict_proba(beta: np.ndarray, X: np.ndarray) -> np.ndarray:
    return sigmoid(np.column_stack([np.ones(len(X)), X]) @ beta)


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
    return float((ranks[pos].sum() - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg))


def stratified_kfold(y: np.ndarray, k: int = 5, seed: int = 42) -> list[tuple[np.ndarray, np.ndarray]]:
    rng = np.random.default_rng(seed)
    pos_idx = np.where(y == 1)[0]
    neg_idx = np.where(y == 0)[0]
    rng.shuffle(pos_idx)
    rng.shuffle(neg_idx)
    pos_folds = np.array_split(pos_idx, k)
    neg_folds = np.array_split(neg_idx, k)
    all_idx = np.arange(len(y))
    folds = []
    for i in range(k):
        val_idx = np.concatenate([pos_folds[i], neg_folds[i]])
        mask = np.ones(len(y), dtype=bool)
        mask[val_idx] = False
        folds.append((all_idx[mask], val_idx))
    return folds


def cross_validate_single(X: np.ndarray, y: np.ndarray, lambdas: list[float]) -> dict:
    results = []
    for reg_lambda in lambdas:
        metrics = []
        for train_idx, val_idx in stratified_kfold(y):
            X_train_raw, X_val_raw = X[train_idx], X[val_idx]
            y_train, y_val = y[train_idx], y[val_idx]
            X_train, means, stds = impute_and_scale_fit(X_train_raw)
            X_val = impute_and_scale_apply(X_val_raw, means, stds)
            beta = fit_ridge_logistic(X_train, y_train, balanced_weights(y_train), reg_lambda)
            probs = predict_proba(beta, X_val)
            metrics.append(
                {
                    "log_loss": log_loss(y_val, probs),
                    "brier": brier_score(y_val, probs),
                    "auc": roc_auc(y_val, probs),
                }
            )
        results.append(
            {
                "lambda": reg_lambda,
                "mean_log_loss": round(float(np.mean([m["log_loss"] for m in metrics])), 6),
                "mean_brier": round(float(np.mean([m["brier"] for m in metrics])), 6),
                "mean_auc": round(float(np.nanmean([m["auc"] for m in metrics])), 6),
                "folds": metrics,
            }
        )
    selected = min(results, key=lambda item: (item["mean_log_loss"], -item["mean_auc"]))
    return {"grid": results, "selected": selected}


def fit_final_single(X: np.ndarray, y: np.ndarray, reg_lambda: float) -> dict:
    X_scaled, means, stds = impute_and_scale_fit(X)
    beta = fit_ridge_logistic(X_scaled, y, balanced_weights(y), reg_lambda)
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


def calibrate_submodel(rows: list[dict], specs: list[dict], target_name: str, lambdas: list[float]) -> dict:
    X = build_feature_matrix(rows, specs)
    y = np.array([float(row[target_name]) for row in rows], dtype=float)
    cv = cross_validate_single(X, y, lambdas)
    model = fit_final_single(X, y, cv["selected"]["lambda"])
    return {"X": X, "y": y, "cv": cv, "model": model, "specs": specs, "target": target_name}


def calibrate_combiner(structural_probs: np.ndarray, dormant_probs: np.ndarray, y: np.ndarray, lambdas: list[float]) -> dict:
    X = np.column_stack([logit(structural_probs), logit(dormant_probs)])
    cv = cross_validate_single(X, y, lambdas)
    model = fit_final_single(X, y, cv["selected"]["lambda"])
    return {"X": X, "y": y, "cv": cv, "model": model}


def build_extraction_score(row: dict) -> int:
    return 1 if (row.get("any_extreme_additive") or 0) == 1 else 0


def compute_ranking(
    rows: list[dict],
    structural: dict,
    dormant: dict,
    combiner: dict,
) -> list[dict]:
    struct_X = impute_and_scale_apply(structural["X"], structural["model"]["means"], structural["model"]["stds"])
    dorm_X = impute_and_scale_apply(dormant["X"], dormant["model"]["means"], dormant["model"]["stds"])
    struct_probs = predict_proba(structural["model"]["beta"], struct_X)
    dorm_probs = predict_proba(dormant["model"]["beta"], dorm_X)
    comb_X_raw = np.column_stack([logit(struct_probs), logit(dorm_probs)])
    comb_X = impute_and_scale_apply(comb_X_raw, combiner["model"]["means"], combiner["model"]["stds"])
    comb_probs = predict_proba(combiner["model"]["beta"], comb_X)

    ranking = []
    for i, row in enumerate(rows):
        ranking.append(
            {
                "successor_cnpj": row["successor_cnpj"],
                "score_evasao_structural": round(float(struct_probs[i]), 6),
                "score_dormant_activation": round(float(dorm_probs[i]), 6),
                "score_evasao_v1_1": round(float(comb_probs[i]), 6),
                "score_extracao_v1_1": build_extraction_score(row),
                "evasion_vehicle_flag": int(row["created_post_sanction"] == 1 or row["dormant_activation_flag"] == 1),
                "created_post_sanction": int(row["created_post_sanction"]),
                "dormant_activation_flag": int(row["dormant_activation_flag"]),
                "sanction_scope_score": row["sanction_scope_score"],
                "same_socio_sanction_count": row["same_socio_sanction_count"],
                "min_abs_days_to_qsa_change": row["min_abs_days_to_qsa_change"],
                "activation_lag_years": row["activation_lag_years"],
                "post_sanction_activation_gap_days": row["post_sanction_activation_gap_days"],
                "buyer_burst_90d": row["buyer_burst_90d"],
                "post_contracts_total": row["post_contracts_total"],
                "extreme_additive_gt50_count": row["extreme_additive_gt50_count"],
                "extreme_additive_gt100_count": row["extreme_additive_gt100_count"],
                "max_delta_valor": row["max_delta_valor"],
            }
        )
    ranking.sort(key=lambda r: r["score_evasao_v1_1"], reverse=True)
    for idx, row in enumerate(ranking, start=1):
        row["rank"] = idx
    return ranking


def weights_payload(specs: list[dict], model: dict) -> list[dict]:
    beta = model["beta"]
    payload = []
    for i, spec in enumerate(specs, start=1):
        payload.append(
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
    return payload


def build_payload(db_path: str, rows: list[dict], structural: dict, dormant: dict, combiner: dict, ranking: list[dict]) -> dict:
    target = np.array([1.0 if (r["created_post_sanction"] == 1 or r["dormant_activation_flag"] == 1) else 0.0 for r in rows], dtype=float)
    return {
        "meta": {
            "db": db_path,
            "n_suppliers": len(rows),
            "n_positive_created_post_sanction": int(sum(r["created_post_sanction"] for r in rows)),
            "n_positive_dormant_activation": int(sum(r["dormant_activation_flag"] for r in rows)),
            "n_positive_evasion_vehicle": int(target.sum()),
            "architecture": "hierarchical: structural model + dormant model + combiner",
        },
        "structural_model": {
            "target": "created_post_sanction",
            "cv": structural["cv"],
            "train_log_loss": round(float(structural["model"]["train_log_loss"]), 6),
            "train_brier": round(float(structural["model"]["train_brier"]), 6),
            "train_auc": round(float(structural["model"]["train_auc"]), 6),
            "intercept": round(float(structural["model"]["beta"][0]), 6),
            "weights": weights_payload(structural["specs"], structural["model"]),
        },
        "dormant_model": {
            "target": "dormant_activation_flag",
            "cv": dormant["cv"],
            "train_log_loss": round(float(dormant["model"]["train_log_loss"]), 6),
            "train_brier": round(float(dormant["model"]["train_brier"]), 6),
            "train_auc": round(float(dormant["model"]["train_auc"]), 6),
            "intercept": round(float(dormant["model"]["beta"][0]), 6),
            "weights": weights_payload(dormant["specs"], dormant["model"]),
        },
        "combiner_model": {
            "target": "evasion_vehicle_flag",
            "cv": combiner["cv"],
            "train_log_loss": round(float(combiner["model"]["train_log_loss"]), 6),
            "train_brier": round(float(combiner["model"]["train_brier"]), 6),
            "train_auc": round(float(combiner["model"]["train_auc"]), 6),
            "intercept": round(float(combiner["model"]["beta"][0]), 6),
            "weights": [
                {"feature": "logit(score_evasao_structural)", "weight_zspace": round(float(combiner["model"]["beta"][1]), 6)},
                {"feature": "logit(score_dormant_activation)", "weight_zspace": round(float(combiner["model"]["beta"][2]), 6)},
            ],
        },
        "top_50": ranking[:50],
        "ranking_size": len(ranking),
    }


def render_markdown(payload: dict) -> str:
    meta = payload["meta"]
    s = payload["structural_model"]
    d = payload["dormant_model"]
    c = payload["combiner_model"]
    top = payload["top_50"][:20]
    lines = [
        "# Phoenix Risk Score v1.1",
        "",
        "Arquitetura hierarquica: `score_evasao_structural` + `score_dormant_activation` -> meta-modelo `score_evasao_v1_1`.",
        "",
        "## Dataset",
        "",
        f"- suppliers: `{meta['n_suppliers']}`",
        f"- created_post_sanction: `{meta['n_positive_created_post_sanction']}`",
        f"- dormant_activation_flag: `{meta['n_positive_dormant_activation']}`",
        f"- evasion_vehicle_flag: `{meta['n_positive_evasion_vehicle']}`",
        "",
        "## Structural Model",
        "",
        f"- target: `{s['target']}`",
        f"- lambda: `{s['cv']['selected']['lambda']}`",
        f"- CV AUC: `{s['cv']['selected']['mean_auc']}`",
        "",
        "## Dormant Model",
        "",
        f"- target: `{d['target']}`",
        f"- lambda: `{d['cv']['selected']['lambda']}`",
        f"- CV AUC: `{d['cv']['selected']['mean_auc']}`",
        "",
        "## Combiner",
        "",
        f"- target: `{c['target']}`",
        f"- lambda: `{c['cv']['selected']['lambda']}`",
        f"- CV AUC: `{c['cv']['selected']['mean_auc']}`",
        "",
        "## Ranking",
        "",
        "| Rank | CNPJ | Final | Structural | Dormant | Extracao | DormantFlag | NewFlag |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in top:
        lines.append(
            f"| {row['rank']} | `{row['successor_cnpj']}` | {row['score_evasao_v1_1']:.4f} | {row['score_evasao_structural']:.4f} | {row['score_dormant_activation']:.4f} | {row['score_extracao_v1_1']} | {row['dormant_activation_flag']} | {row['created_post_sanction']} |"
        )
    return "\n".join(lines) + "\n"


def render_laudo_template(payload: dict) -> str:
    top = payload["top_50"][0]
    return f"""# Laudo de Analise de Risco — Veiculo de Evasao e Extracao
## CNPJ [PREENCHER]

**Metodologia:** PNCP + CEIS/CGU + QSA/Receita Federal + Phoenix Risk Score v1.1  
**Score estrutural:** [PREENCHER]  
**Score dormant activation:** [PREENCHER]  
**Score evasao final (v1.1):** [PREENCHER]  
**Score extracao:** [PREENCHER]

## Tipologia

- `created_post_sanction`: [0/1]
- `dormant_activation_flag`: [0/1]
- `activation_lag_years`: [PREENCHER]
- `post_sanction_activation_gap_days`: [PREENCHER]
- `buyer_burst_90d`: [PREENCHER]

## Rede sancionada

- `sanction_scope_score`: [PREENCHER]
- `same_socio_sanction_count`: [PREENCHER]
- `min_abs_days_to_qsa_change`: [PREENCHER]

## Contratacao e extracao

- contratos totais: [PREENCHER]
- `score_extracao_v1_1`: [PREENCHER]
- contratos `delta_pct > 50`: [PREENCHER]
- contratos `delta_pct > 100`: [PREENCHER]
- maior `delta_valor`: [PREENCHER]

**Exemplo topo do ranking v1.1:** `{top['successor_cnpj']}` com `score_evasao_v1_1 = {top['score_evasao_v1_1']:.4f}`.
"""


def write_csv(ranking: list[dict], path: Path) -> None:
    fields = [
        "rank",
        "successor_cnpj",
        "score_evasao_v1_1",
        "score_evasao_structural",
        "score_dormant_activation",
        "score_extracao_v1_1",
        "evasion_vehicle_flag",
        "created_post_sanction",
        "dormant_activation_flag",
        "sanction_scope_score",
        "same_socio_sanction_count",
        "min_abs_days_to_qsa_change",
        "activation_lag_years",
        "post_sanction_activation_gap_days",
        "buyer_burst_90d",
        "post_contracts_total",
        "extreme_additive_gt50_count",
        "extreme_additive_gt100_count",
        "max_delta_valor",
    ]
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in ranking:
            writer.writerow({field: row[field] for field in fields})


def main() -> int:
    args = parse_args()
    conn = sqlite3.connect(args.db)
    conn.row_factory = row_factory
    conn.execute("PRAGMA temp_store = MEMORY")
    conn.execute("PRAGMA mmap_size = 268435456")
    conn.execute("PRAGMA cache_size = -200000")

    build_temp_tables(conn)
    rows = load_supplier_metrics(conn)
    lambdas = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0]

    structural_rows = [row for row in rows if row["created_post_sanction"] in (0, 1)]
    dormant_rows = [row for row in rows if row["dormant_activation_flag"] in (0, 1)]

    structural = calibrate_submodel(structural_rows, STRUCTURAL_FEATURES, "created_post_sanction", lambdas)
    dormant = calibrate_submodel(dormant_rows, DORMANT_FEATURES, "dormant_activation_flag", lambdas)

    # align submodel scores on full ranking population
    struct_X_full = build_feature_matrix(rows, STRUCTURAL_FEATURES)
    struct_scaled = impute_and_scale_apply(struct_X_full, structural["model"]["means"], structural["model"]["stds"])
    struct_probs_full = predict_proba(structural["model"]["beta"], struct_scaled)

    dorm_X_full = build_feature_matrix(rows, DORMANT_FEATURES)
    dorm_scaled = impute_and_scale_apply(dorm_X_full, dormant["model"]["means"], dormant["model"]["stds"])
    dorm_probs_full = predict_proba(dormant["model"]["beta"], dorm_scaled)

    y_comb = np.array([1.0 if (r["created_post_sanction"] == 1 or r["dormant_activation_flag"] == 1) else 0.0 for r in rows], dtype=float)
    combiner = calibrate_combiner(struct_probs_full, dorm_probs_full, y_comb, lambdas)

    # store full matrices in submodels for ranking
    structural["X"] = struct_X_full
    dormant["X"] = dorm_X_full

    ranking = compute_ranking(rows, structural, dormant, combiner)
    payload = build_payload(args.db, rows, structural, dormant, combiner, ranking)

    json_path = Path(args.json_output)
    md_path = Path(args.md_output)
    csv_path = Path(args.csv_output)
    laudo_path = Path(args.laudo_template_output)
    for path in [json_path, md_path, csv_path, laudo_path]:
        path.parent.mkdir(parents=True, exist_ok=True)

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(payload))
    write_csv(ranking, csv_path)
    laudo_path.write_text(render_laudo_template(payload))

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {laudo_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
