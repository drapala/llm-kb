#!/usr/bin/env python3
"""
Consolidated Phoenix Risk Score v1.

Rules:
1. Hard filter `n_socios <= 20` before ranking.
2. Keep structural score formula unchanged from v0:
   - sanction_scope_score
   - same_socio_multi_flag
   - qsa_proximity_score
3. Add dormant_entity as an out-of-score flag:
   - created_post_sanction = 0
   - first_post_contract_date within 90 days of anchor_sanction_date
4. Generate filtered ranking and a top-20 laudo bundle.
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
        "rationale": "multiplicidade de firmas sancionadas ligadas ao mesmo socio",
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
    parser.add_argument("--top20-output", required=True)
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


def fetch_auxiliary_maps(conn: sqlite3.Connection) -> tuple[dict[str, int], dict[str, str]]:
    socios = {
        row["cnpj"]: row["n_socios"]
        for row in conn.execute(
            """
            SELECT cnpj, COUNT(*) AS n_socios
            FROM supplier_socios
            GROUP BY 1
            """
        ).fetchall()
    }
    names = {
        row["cnpj"]: row["nome_empresarial"] or row["nome_fantasia"] or ""
        for row in conn.execute(
            """
            SELECT cnpj, nome_empresarial, nome_fantasia
            FROM suppliers_rfb
            """
        ).fetchall()
    }
    return socios, names


def enrich_and_filter_rows(conn: sqlite3.Connection, rows: list[dict]) -> list[dict]:
    socios_map, names_map = fetch_auxiliary_maps(conn)
    enriched = []
    for row in rows:
        n_socios = socios_map.get(row["successor_cnpj"], 0)
        first_gap = row.get("post_sanction_activation_gap_days")
        dormant_entity = (
            row["created_post_sanction"] == 0
            and first_gap is not None
            and abs(int(first_gap)) <= 90
        )
        row = dict(row)
        row["n_socios"] = int(n_socios)
        row["supplier_name"] = names_map.get(row["successor_cnpj"], "")
        row["dormant_entity"] = 1 if dormant_entity else 0
        if row["n_socios"] <= 20:
            enriched.append(row)
    return enriched


def build_matrix(rows: list[dict]) -> tuple[list[str], np.ndarray, np.ndarray]:
    ids = [row["successor_cnpj"] for row in rows]
    y = np.array([row["created_post_sanction"] for row in rows], dtype=float)
    cols = []
    for spec in CANDIDATE_FEATURES:
        cols.append(
            np.array([apply_transform(spec["transform"], row.get(spec["source"])) for row in rows], dtype=float)
        )
    return ids, np.column_stack(cols), y


def impute_and_scale_fit(X: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    means = np.nanmean(X, axis=0)
    X_imp = np.where(np.isnan(X), means, X)
    stds = X_imp.std(axis=0)
    stds = np.where(stds == 0, 1.0, stds)
    return (X_imp - means) / stds, means, stds


def sigmoid(z: np.ndarray) -> np.ndarray:
    z = np.clip(z, -30.0, 30.0)
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


def balanced_weights(y: np.ndarray) -> np.ndarray:
    pos = max(float((y == 1).sum()), 1.0)
    neg = max(float((y == 0).sum()), 1.0)
    n = len(y)
    return np.where(y == 1, n / (2.0 * pos), n / (2.0 * neg))


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


def cross_validate(X: np.ndarray, y: np.ndarray, lambdas: list[float]) -> dict:
    results = []
    for reg_lambda in lambdas:
        metrics = []
        for train_idx, val_idx in stratified_kfold(y):
            X_train_raw, X_val_raw = X[train_idx], X[val_idx]
            y_train, y_val = y[train_idx], y[val_idx]
            X_train, means, stds = impute_and_scale_fit(X_train_raw)
            X_val = np.where(np.isnan(X_val_raw), means, X_val_raw)
            X_val = (X_val - means) / stds
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


def fit_final_model(X: np.ndarray, y: np.ndarray, reg_lambda: float) -> dict:
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


def compute_ranking(rows: list[dict], X: np.ndarray, ids: list[str], model: dict) -> list[dict]:
    X_imp = np.where(np.isnan(X), model["means"], X)
    X_scaled = (X_imp - model["means"]) / model["stds"]
    probs = predict_proba(model["beta"], X_scaled)
    coef = model["beta"][1:]
    intercept = float(model["beta"][0])
    ranking = []
    for i, row in enumerate(rows):
        z = X_scaled[i]
        ranking.append(
            {
                "successor_cnpj": ids[i],
                "supplier_name": row["supplier_name"],
                "score_evasao_v1": round(float(probs[i]), 6),
                "score_extracao_v1": int(row["any_extreme_additive"]),
                "raw_logit": round(float(intercept + np.dot(coef, z)), 6),
                "created_post_sanction": int(row["created_post_sanction"]),
                "dormant_entity": int(row["dormant_entity"]),
                "n_socios": int(row["n_socios"]),
                "sanction_scope_score": row["sanction_scope_score"],
                "same_socio_sanction_count": row["same_socio_sanction_count"],
                "min_abs_days_to_qsa_change": row["min_abs_days_to_qsa_change"],
                "anchor_sanction_date": row["anchor_sanction_date"],
                "first_post_contract_date": row["first_post_contract_date"],
                "post_sanction_activation_gap_days": row["post_sanction_activation_gap_days"],
                "post_contracts_total": row["post_contracts_total"],
                "extreme_additive_gt50_count": row["extreme_additive_gt50_count"],
                "extreme_additive_gt100_count": row["extreme_additive_gt100_count"],
                "max_delta_valor": row["max_delta_valor"],
                "feature_contributions": {
                    spec["name"]: round(float(coef[j] * z[j]), 6)
                    for j, spec in enumerate(CANDIDATE_FEATURES)
                },
            }
        )
    ranking.sort(key=lambda r: r["score_evasao_v1"], reverse=True)
    for idx, row in enumerate(ranking, start=1):
        row["rank"] = idx
    return ranking


def build_payload(db_path: str, filtered_rows: list[dict], cv: dict, model: dict, ranking: list[dict]) -> dict:
    return {
        "meta": {
            "db": db_path,
            "n_suppliers_after_filter": len(filtered_rows),
            "n_positive_created_post_sanction": int(sum(r["created_post_sanction"] for r in filtered_rows)),
            "n_dormant_entity": int(sum(r["dormant_entity"] for r in filtered_rows)),
            "filter": "n_socios <= 20",
            "dormant_flag_rule": "created_post_sanction = 0 AND abs(post_sanction_activation_gap_days) <= 90",
            "score_formula": "sanction_scope_score + same_socio_multi_flag + qsa_proximity",
        },
        "cross_validation": cv,
        "final_model": {
            "intercept": round(float(model["beta"][0]), 6),
            "train_log_loss": round(float(model["train_log_loss"]), 6),
            "train_brier": round(float(model["train_brier"]), 6),
            "train_auc": round(float(model["train_auc"]), 6),
            "weights": [
                {
                    "feature": spec["name"],
                    "source": spec["source"],
                    "transform": spec["transform"],
                    "rationale": spec["rationale"],
                    "weight_zspace": round(float(model["beta"][i]), 6),
                    "center_full_sample": round(float(model["means"][i - 1]), 6),
                    "scale_full_sample": round(float(model["stds"][i - 1]), 6),
                }
                for i, spec in enumerate(CANDIDATE_FEATURES, start=1)
            ],
        },
        "top_20": ranking[:20],
        "ranking_size": len(ranking),
    }


def render_summary(payload: dict) -> str:
    meta = payload["meta"]
    selected = payload["cross_validation"]["selected"]
    model = payload["final_model"]
    lines = [
        "# Phoenix Risk Score v1 (Consolidated)",
        "",
        "Consolidacao operacional:",
        "",
        "- filtro duro `n_socios <= 20` antes do ranking",
        "- `dormant_entity` fora do score",
        "- score estrutural identico ao v0 em features",
        "",
        "## Calibration",
        "",
        f"- suppliers apos filtro: `{meta['n_suppliers_after_filter']}`",
        f"- positivos `created_post_sanction`: `{meta['n_positive_created_post_sanction']}`",
        f"- `dormant_entity`: `{meta['n_dormant_entity']}`",
        f"- lambda selecionado: `{selected['lambda']}`",
        f"- CV mean AUC: `{selected['mean_auc']}`",
        f"- CV mean log loss: `{selected['mean_log_loss']}`",
        "",
        "## Weights",
        "",
        f"- intercept: `{model['intercept']}`",
    ]
    for weight in model["weights"]:
        lines.append(
            f"- `{weight['feature']}` ({weight['transform']} de `{weight['source']}`): weight = `{weight['weight_zspace']}`."
        )
    lines.extend(
        [
            "",
            "## Top 20",
            "",
            "| Rank | CNPJ | Nome | Score evasao | Extracao | Dormant | Socios |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in payload["top_20"]:
        name = row["supplier_name"][:50]
        lines.append(
            f"| {row['rank']} | `{row['successor_cnpj']}` | {name} | {row['score_evasao_v1']:.4f} | {row['score_extracao_v1']} | {row['dormant_entity']} | {row['n_socios']} |"
        )
    return "\n".join(lines) + "\n"


def render_top20_laudos(payload: dict) -> str:
    sections = [
        "# Top 20 — Laudos Automáticos Preliminares",
        "",
        "Filtro aplicado: `n_socios <= 20`.",
        "",
    ]
    for row in payload["top_20"]:
        sections.extend(
            [
                f"## Rank {row['rank']} — {row['supplier_name'] or '[sem nome]'}",
                f"**CNPJ:** `{row['successor_cnpj']}`  ",
                f"**Score evasao (v1):** `{row['score_evasao_v1']:.4f}`  ",
                f"**Score extracao:** `{row['score_extracao_v1']}`  ",
                f"**Created post-sanction:** `{row['created_post_sanction']}`  ",
                f"**Dormant entity:** `{row['dormant_entity']}`  ",
                f"**N socios:** `{row['n_socios']}`",
                "",
                "**Sinais principais**",
                f"- `sanction_scope_score`: `{row['sanction_scope_score']}`",
                f"- `same_socio_sanction_count`: `{row['same_socio_sanction_count']}`",
                f"- `min_abs_days_to_qsa_change`: `{row['min_abs_days_to_qsa_change']}`",
                f"- `anchor_sanction_date`: `{row['anchor_sanction_date']}`",
                f"- `first_post_contract_date`: `{row['first_post_contract_date']}`",
                f"- `post_sanction_activation_gap_days`: `{row['post_sanction_activation_gap_days']}`",
                f"- `post_contracts_total`: `{row['post_contracts_total']}`",
                "",
                "**Extracao observada**",
                f"- `extreme_additive_gt50_count`: `{row['extreme_additive_gt50_count']}`",
                f"- `extreme_additive_gt100_count`: `{row['extreme_additive_gt100_count']}`",
                f"- `max_delta_valor`: `{row['max_delta_valor']}`",
                "",
                "**Leitura preliminar**",
                "- caso de alta prioridade para revisao documental se score alto e rede sancionada relevante;",
                (
                    "- `dormant_entity = 1` sugere veiculo preexistente ativado na janela da sancao."
                    if row["dormant_entity"] == 1
                    else "- sem sinal de `dormant_entity` pela regra automatizada atual."
                ),
                (
                    "- `score_extracao = 1` indica sinais de fase 2 ja observados."
                    if row["score_extracao_v1"] == 1
                    else "- sem sinal observado de fase 2 no monitor de extracao."
                ),
                "",
            ]
        )
    return "\n".join(sections) + "\n"


def write_csv(ranking: list[dict], path: Path) -> None:
    fields = [
        "rank",
        "successor_cnpj",
        "supplier_name",
        "score_evasao_v1",
        "score_extracao_v1",
        "created_post_sanction",
        "dormant_entity",
        "n_socios",
        "sanction_scope_score",
        "same_socio_sanction_count",
        "min_abs_days_to_qsa_change",
        "anchor_sanction_date",
        "first_post_contract_date",
        "post_sanction_activation_gap_days",
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
    filtered_rows = enrich_and_filter_rows(conn, rows)
    ids, X, y = build_matrix(filtered_rows)
    lambdas = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0]
    cv = cross_validate(X, y, lambdas)
    model = fit_final_model(X, y, cv["selected"]["lambda"])
    ranking = compute_ranking(filtered_rows, X, ids, model)
    payload = build_payload(args.db, filtered_rows, cv, model, ranking)

    json_path = Path(args.json_output)
    md_path = Path(args.md_output)
    csv_path = Path(args.csv_output)
    top20_path = Path(args.top20_output)
    for path in [json_path, md_path, csv_path, top20_path]:
        path.parent.mkdir(parents=True, exist_ok=True)

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_summary(payload))
    csv_path.write_text("")
    write_csv(ranking, csv_path)
    top20_path.write_text(render_top20_laudos(payload))

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {top20_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
