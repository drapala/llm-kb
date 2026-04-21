#!/usr/bin/env python3
"""
Phoenix / dormant-activation risk score v1.

Target:
- evasion_vehicle_flag = created_post_sanction OR dormant_activation_flag

Architecture:
- score_evasao_v1: prospective structural/activation score calibrated with balanced ridge logistic regression
- score_extracao_v1: observed monitoring score for phase-2 extraction, derived from extreme additive tail
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


FEATURE_SPECS = [
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
        "rationale": "mudanca de QSA mais proxima da data ancora de sancao eleva risco",
    },
    {
        "name": "activation_lag_years",
        "source": "activation_lag_years",
        "transform": "log1p",
        "rationale": "entidade muito antiga ativada tardiamente e plausivel veiculo dormente",
    },
    {
        "name": "sanction_activation_proximity_score",
        "source": "post_sanction_activation_gap_days",
        "transform": "neg_abs_log1p",
        "rationale": "ativacao proxima da sancao da rede aumenta suspeita de evasao",
    },
    {
        "name": "buyer_burst_90d",
        "source": "buyer_burst_90d",
        "transform": "log1p",
        "rationale": "entrada rapida em varios orgaos apos ativacao reforca credencialismo operacional",
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


def build_matrix(rows: list[dict]) -> tuple[list[str], np.ndarray, np.ndarray]:
    ids = [row["successor_cnpj"] for row in rows]
    y = np.array(
        [
            1.0 if (row["created_post_sanction"] == 1 or row["dormant_activation_flag"] == 1) else 0.0
            for row in rows
        ],
        dtype=float,
    )
    cols = []
    for spec in FEATURE_SPECS:
        cols.append(
            np.array(
                [transform_value(spec["transform"], row.get(spec["source"])) for row in rows],
                dtype=float,
            )
        )
    X = np.column_stack(cols)
    return ids, X, y


def impute_and_scale_fit(X: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    means = np.nanmean(X, axis=0)
    X_imp = np.where(np.isnan(X), means, X)
    stds = X_imp.std(axis=0)
    stds = np.where(stds == 0, 1.0, stds)
    return (X_imp - means) / stds, means, stds


def sigmoid(z: np.ndarray) -> np.ndarray:
    z = np.clip(z, -30.0, 30.0)
    return 1.0 / (1.0 + np.exp(-z))


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
        train_idx = all_idx[mask]
        folds.append((train_idx, val_idx))
    return folds


def cross_validate(X: np.ndarray, y: np.ndarray, lambdas: list[float]) -> dict:
    results = []
    for reg_lambda in lambdas:
        fold_metrics = []
        for train_idx, val_idx in stratified_kfold(y):
            X_train_raw, X_val_raw = X[train_idx], X[val_idx]
            y_train, y_val = y[train_idx], y[val_idx]
            X_train, means, stds = impute_and_scale_fit(X_train_raw)
            X_val = np.where(np.isnan(X_val_raw), means, X_val_raw)
            X_val = (X_val - means) / stds
            beta = fit_ridge_logistic(X_train, y_train, balanced_weights(y_train), reg_lambda)
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


def build_extraction_score(row: dict) -> int:
    if (row.get("extreme_additive_gt50_count") or 0) > 0:
        return 1
    if (row.get("extreme_additive_gt100_count") or 0) > 0:
        return 1
    if (row.get("any_extreme_additive") or 0) == 1:
        return 1
    return 0


def compute_ranking(rows: list[dict], X: np.ndarray, ids: list[str], model: dict) -> list[dict]:
    means = model["means"]
    stds = model["stds"]
    beta = model["beta"]
    X_imp = np.where(np.isnan(X), means, X)
    X_scaled = (X_imp - means) / stds
    probs = predict_proba(beta, X_scaled)
    intercept = float(beta[0])
    coef = beta[1:]

    ranking = []
    for idx, row in enumerate(rows):
        z = X_scaled[idx]
        contributions = {
            spec["name"]: round(float(coef[j] * z[j]), 6)
            for j, spec in enumerate(FEATURE_SPECS)
        }
        ranking.append(
            {
                "successor_cnpj": ids[idx],
                "score_evasao_v1": round(float(probs[idx]), 6),
                "score_extracao_v1": build_extraction_score(row),
                "raw_logit": round(float(intercept + np.dot(coef, z)), 6),
                "evasion_vehicle_flag": int(
                    1 if (row["created_post_sanction"] == 1 or row["dormant_activation_flag"] == 1) else 0
                ),
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
                "feature_contributions": contributions,
            }
        )
    ranking.sort(key=lambda r: r["score_evasao_v1"], reverse=True)
    for i, row in enumerate(ranking, start=1):
        row["rank"] = i
    return ranking


def build_payload(db_path: str, rows: list[dict], cv: dict, model: dict, ranking: list[dict]) -> dict:
    beta = model["beta"]
    weights = []
    for i, spec in enumerate(FEATURE_SPECS, start=1):
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
    positives = [row for row in ranking if row["evasion_vehicle_flag"] == 1]
    dormant_positives = [row for row in ranking if row["dormant_activation_flag"] == 1]
    return {
        "meta": {
            "db": db_path,
            "n_suppliers": len(rows),
            "n_positive_evasion_vehicle": len(positives),
            "n_positive_created_post_sanction": sum(row["created_post_sanction"] for row in ranking),
            "n_positive_dormant_activation": len(dormant_positives),
            "target": "evasion_vehicle_flag = created_post_sanction OR dormant_activation_flag",
            "method": "balanced ridge logistic regression with 5-fold stratified CV and lambda selected by lowest mean log loss",
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
    selected = payload["cross_validation"]["selected"]
    model = payload["final_model"]
    top = payload["top_50"][:20]
    lines = [
        "# Phoenix Risk Score v1",
        "",
        "Arquitetura: `score_evasao_v1` para detectar veiculo de evasao (novo ou dormente) e `score_extracao_v1` para monitorar fase 2.",
        "",
        "## Calibration",
        "",
        f"- target: `{meta['target']}`",
        f"- suppliers: `{meta['n_suppliers']}`",
        f"- positivos alvo ampliado: `{meta['n_positive_evasion_vehicle']}`",
        f"- positivos `created_post_sanction`: `{meta['n_positive_created_post_sanction']}`",
        f"- positivos `dormant_activation_flag`: `{meta['n_positive_dormant_activation']}`",
        f"- lambda selecionado: `{selected['lambda']}`",
        f"- CV mean log loss: `{selected['mean_log_loss']}`",
        f"- CV mean Brier: `{selected['mean_brier']}`",
        f"- CV mean AUC: `{selected['mean_auc']}`",
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
            "`score_evasao_v1 = sigmoid(intercept + sum(weight_i * z_i))`, com `z_i = (feature_transformada - center_i) / scale_i`.",
            "",
            "## Ranking",
            "",
            "| Rank | CNPJ | Evasao | Extracao | Dormant | New | Contracts |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in top:
        lines.append(
            f"| {row['rank']} | `{row['successor_cnpj']}` | {row['score_evasao_v1']:.4f} | {row['score_extracao_v1']} | {row['dormant_activation_flag']} | {row['created_post_sanction']} | {row['post_contracts_total']} |"
        )
    return "\n".join(lines) + "\n"


def render_laudo_template(payload: dict) -> str:
    top = payload["top_50"][0]
    return f"""# Laudo de Analise de Risco — Veiculo de Evasao e Extracao
## CNPJ [PREENCHER]

**Data de geracao:** [PREENCHER]  
**Metodologia:** PNCP + CEIS/CGU + QSA/Receita Federal + Phoenix Risk Score v1  
**Finalidade:** Subsidio para representacao ao TCU / MPF  
**Classificacao:** Preliminar — analise automatizada, requer verificacao documental  
**Score de evasao (v1):** [PREENCHER]  
**Score de extracao (v1):** [PREENCHER]  
**Rank no universo analisado:** [PREENCHER]

---

## 1. Identificacao do Objeto

- Razao social: [PREENCHER]
- CNPJ: [PREENCHER]
- Socio(s)-chave: [PREENCHER]
- Data de fundacao / inicio de atividade: [PREENCHER]
- Sede: [PREENCHER]
- Primeiro contrato PNCP: [PREENCHER]
- Periodo analisado: [PREENCHER]

## 2. Rede Societaria e Vinculos CEIS

- CNPJs sancionados ligados ao mesmo CPF/QSA: [PREENCHER]
- Escopo das sancoes: [federal/estadual/municipal]
- `sanction_scope_score`: [PREENCHER]
- `same_socio_sanction_count`: [PREENCHER]

## 3. Tipologia de Veiculo de Evasao

- `created_post_sanction`: [0/1]
- `dormant_activation_flag`: [0/1]
- `activation_lag_years`: [PREENCHER]
- `post_sanction_activation_gap_days`: [PREENCHER]
- `buyer_burst_90d`: [PREENCHER]
- `min_abs_days_to_qsa_change`: [PREENCHER]

Interpretacao:
- Se `created_post_sanction = 1`: phoenix classico.
- Se `dormant_activation_flag = 1`: ativacao de entidade dormente.

## 4. Perfil de Contratacao

- Contratos totais: [PREENCHER]
- Valor total: [PREENCHER]
- Orgaos distintos: [PREENCHER]
- Burst inicial de compradores (90 dias): [PREENCHER]

## 5. Sinais de Extracao

- `score_extracao_v1`: [PREENCHER]
- contratos com `delta_pct > 50`: [PREENCHER]
- contratos com `delta_pct > 100`: [PREENCHER]
- maior `delta_valor`: [PREENCHER]

## 6. Conclusao Preliminar

Estrutura sugerida:
1. Descrever a tipologia (`phoenix classico` ou `entidade dormente`).
2. Enquadrar a rede sancionada e a cronologia societaria.
3. Destacar sinais de extracao, se presentes.
4. Apontar recomendacoes documentais para confirmacao.

---

**Exemplo de topo atual do ranking v1:** `{top['successor_cnpj']}` com `score_evasao_v1 = {top['score_evasao_v1']:.4f}` e `score_extracao_v1 = {top['score_extracao_v1']}`.
"""


def write_csv(ranking: list[dict], path: Path) -> None:
    fields = [
        "rank",
        "successor_cnpj",
        "score_evasao_v1",
        "score_extracao_v1",
        "raw_logit",
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
    ids, X, y = build_matrix(rows)
    lambdas = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0]
    cv = cross_validate(X, y, lambdas)
    model = fit_final_model(X, y, cv["selected"]["lambda"])
    ranking = compute_ranking(rows, X, ids, model)
    payload = build_payload(args.db, rows, cv, model, ranking)

    json_path = Path(args.json_output)
    md_path = Path(args.md_output)
    csv_path = Path(args.csv_output)
    laudo_path = Path(args.laudo_template_output)
    for path in [json_path, md_path, csv_path, laudo_path]:
        path.parent.mkdir(parents=True, exist_ok=True)

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(payload))
    csv_path.write_text("")
    write_csv(ranking, csv_path)
    laudo_path.write_text(render_laudo_template(payload))

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {laudo_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
