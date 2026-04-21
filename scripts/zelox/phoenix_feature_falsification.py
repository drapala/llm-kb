#!/usr/bin/env python3
"""
Build a falseable, empirical feature report for phoenix-style procurement signals.

Outputs:
1. JSON payload with supplier-level metrics and feature-test summaries
2. Markdown report with tested features and a broader feature catalog
"""

from __future__ import annotations

import argparse
import json
import math
import sqlite3
import statistics
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FeatureSpec:
    key: str
    tested_now: bool
    sql_formula: str
    threshold: str
    rationale: str
    falsifiable_hypothesis: str


FEATURE_SPECS = [
    FeatureSpec(
        key="same_socio_sanction_count",
        tested_now=True,
        sql_formula="COUNT(DISTINCT sanctioned_cnpj) OVER successor_cnpj",
        threshold=">= 2",
        rationale="Um mesmo CPF absorvendo mais de uma firma sancionada eleva precision e explicabilidade juridica.",
        falsifiable_hypothesis="Genuine phoenix com contratos pos-sancao exibem maior multiplicidade de firmas sancionadas ligadas ao mesmo socio do que sucessores preexistentes.",
    ),
    FeatureSpec(
        key="sanction_scope_score",
        tested_now=True,
        sql_formula="SUM(weight_categoria_sancao * weight_esfera_orgao) OVER linked sanctions",
        threshold=">= 4",
        rationale="A rede ligada a sancoes mais graves e mais amplas tende a ser juridicamente mais acionavel.",
        falsifiable_hypothesis="Successores com score alto deveriam concentrar maior incidencia de sinais fase 1 ou fase 2 do que successores com score baixo.",
    ),
    FeatureSpec(
        key="post_sanction_ramp_speed",
        tested_now=True,
        sql_formula="contracts_30d, contracts_90d, contracts_180d, value_30d, value_90d, value_180d",
        threshold="contracts_90d >= 5 OR value_90d >= 100000",
        rationale="Reentrada rapida com volume anormal e um bom proxy operacional de evasao.",
        falsifiable_hypothesis="Genuine phoenix rampam mais rapido nos primeiros 90 dias apos a sancao do que sucessores preexistentes com contratos pos-sancao.",
    ),
    FeatureSpec(
        key="activation_lag_post_sanction",
        tested_now=True,
        sql_formula="julianday(first_post_contract_date) - julianday(anchor_sanction_date)",
        threshold="<= 30 dias",
        rationale="Atraso curto entre sancao da empresa-mae e primeira contratacao do sucessor e um sinal temporal forte de evasao operacional.",
        falsifiable_hypothesis="Genuine phoenix entram em contratacao logo apos a data-ancora de sancao, mais rapidamente do que sucessores preexistentes.",
    ),
    FeatureSpec(
        key="new_buyer_ratio",
        tested_now=True,
        sql_formula="COUNT(DISTINCT post_organs NOT IN mother_organs) / COUNT(DISTINCT post_organs)",
        threshold=">= 0.8",
        rationale="Explica evasao por credencialismo: o novo CNPJ entra em orgaos onde o historico da mae nao pesa.",
        falsifiable_hypothesis="Genuine phoenix ganham em orgaos novos, fora do historico pre-sancao da rede-mae, com razao mediana acima de 0.8.",
    ),
    FeatureSpec(
        key="extreme_additive_tail",
        tested_now=True,
        sql_formula="COUNT(delta_pct > 50), COUNT(delta_pct > 100), MAX(delta_valor)",
        threshold=">= 1 contrato com delta_pct > 50",
        rationale="Fase 2 parece rara, mas maximalista quando aparece; a cauda e mais informativa que o limiar de 25%.",
        falsifiable_hypothesis="Empresas phoenix com sinal fase 1 forte acumulam maior incidencia de aditivos extremos ao longo do tempo.",
    ),
    FeatureSpec(
        key="stealth_to_extraction_gap",
        tested_now=True,
        sql_formula="julianday(first_extreme_additive) - julianday(first_post_sanction_contract)",
        threshold="<= 365 dias",
        rationale="Se o gap temporal se repetir, a camada phoenix pode antecipar fase 2.",
        falsifiable_hypothesis="Empresas com stealth re-entry que chegam a extracao extrema o fazem dentro de uma janela temporal relativamente curta e repetivel.",
    ),
    FeatureSpec(
        key="small_contract_burst",
        tested_now=False,
        sql_formula="contracts_90d + median_ticket_90d + median_duration_90d",
        threshold="contracts_90d >= 5 AND median_duration_90d <= 30",
        rationale="Rajada de contratos pequenos e curtos parece ser a assinatura operacional da fase 1.",
        falsifiable_hypothesis="Genuine phoenix deveriam apresentar burst inicial mais intenso de contratos pequenos/curtos do que grupos de controle.",
    ),
    FeatureSpec(
        key="organ_dependency_after_entry",
        tested_now=False,
        sql_formula="MAX(orgao_share), HHI(orgao_share)",
        threshold="top1_share >= 0.5",
        rationale="Separa credencialismo difuso de captura localizada em poucos compradores.",
        falsifiable_hypothesis="Phoenix com fase 2 deveriam concentrar mais fortemente em um ou dois compradores apos a reentrada.",
    ),
    FeatureSpec(
        key="category_shift_from_mother",
        tested_now=True,
        sql_formula="1 - jaccard(post_categories_phoenix, pre_categories_mother)",
        threshold="<= 0.5 shift",
        rationale="Continuidade de categoria reforca continuidade operacional; shift extremo sinaliza possivel falso positivo societario.",
        falsifiable_hypothesis="Genuine phoenix tendem a permanecer perto do mix de categorias da firma-mae, mais do que sucessores preexistentes.",
    ),
    FeatureSpec(
        key="qsa_change_near_sanction",
        tested_now=True,
        sql_formula="MIN(ABS(julianday(data_entrada_sociedade) - julianday(anchor_sanction_date))) <= 90",
        threshold="TRUE",
        rationale="Cronologia societaria perto da sancao e uma das features mais explicaveis juridicamente.",
        falsifiable_hypothesis="Genuine phoenix exibem mudanca de QSA mais proxima da data de sancao do que sucessores preexistentes.",
    ),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--json-output", required=True)
    parser.add_argument("--md-output", required=True)
    return parser.parse_args()


def row_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def run_sql(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> list[dict]:
    return conn.execute(sql, params).fetchall()


def build_temp_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        DROP TABLE IF EXISTS temp_sanctioned_pj;
        DROP TABLE IF EXISTS temp_shared_successors;
        DROP TABLE IF EXISTS temp_supplier_anchor;
        DROP TABLE IF EXISTS temp_post_contracts;
        DROP TABLE IF EXISTS temp_mother_pre_contracts;
        DROP TABLE IF EXISTS temp_mother_organs;
        DROP TABLE IF EXISTS temp_post_organs;
        DROP TABLE IF EXISTS temp_sanction_scope;

        CREATE TEMP TABLE temp_sanctioned_pj AS
        SELECT
            cpf_cnpj_norm AS sanctioned_cnpj,
            MIN(substr(data_inicio, 7, 4) || '-' || substr(data_inicio, 4, 2) || '-' || substr(data_inicio, 1, 2)) AS sanction_date
        FROM ceis_sanctions
        WHERE LENGTH(cpf_cnpj_norm) = 14
          AND data_inicio LIKE '__/__/____'
        GROUP BY 1;

        CREATE INDEX temp_idx_sanctioned_cnpj
            ON temp_sanctioned_pj(sanctioned_cnpj);

        CREATE TEMP TABLE temp_shared_successors AS
        SELECT DISTINCT
            s.sanctioned_cnpj,
            s.sanction_date,
            ss2.cnpj AS successor_cnpj
        FROM temp_sanctioned_pj s
        JOIN supplier_socios ss1
          ON ss1.cnpj = s.sanctioned_cnpj
        JOIN supplier_socios ss2
          ON ss2.cnpj_cpf = ss1.cnpj_cpf
         AND ss2.cnpj <> ss1.cnpj
        WHERE ss1.cnpj_cpf IS NOT NULL
          AND ss1.cnpj_cpf <> '';

        CREATE INDEX temp_idx_shared_successors_successor
            ON temp_shared_successors(successor_cnpj);
        CREATE INDEX temp_idx_shared_successors_sanctioned
            ON temp_shared_successors(sanctioned_cnpj);

        CREATE TEMP TABLE temp_supplier_anchor AS
        SELECT
            ts.successor_cnpj,
            MIN(ts.sanction_date) AS anchor_sanction_date,
            COUNT(DISTINCT ts.sanctioned_cnpj) AS same_socio_sanction_count,
            rfb.data_inicio_atividade,
            CASE
                WHEN rfb.data_inicio_atividade IS NOT NULL
                 AND rfb.data_inicio_atividade > MIN(ts.sanction_date)
                THEN 1 ELSE 0
            END AS created_post_sanction
        FROM temp_shared_successors ts
        LEFT JOIN suppliers_rfb rfb
          ON rfb.cnpj = ts.successor_cnpj
        GROUP BY ts.successor_cnpj;

        CREATE INDEX temp_idx_supplier_anchor_successor
            ON temp_supplier_anchor(successor_cnpj);
        CREATE INDEX temp_idx_supplier_anchor_created
            ON temp_supplier_anchor(created_post_sanction);

        CREATE TEMP TABLE temp_sanction_scope AS
        SELECT
            ts.successor_cnpj,
            ROUND(SUM(
                (CASE
                    WHEN lower(COALESCE(cs.categoria_sancao, '')) LIKE '%inid%' THEN 4
                    WHEN lower(COALESCE(cs.categoria_sancao, '')) LIKE '%imped%' THEN 3
                    WHEN lower(COALESCE(cs.categoria_sancao, '')) LIKE '%suspens%' THEN 2
                    ELSE 1
                END) *
                (CASE
                    WHEN lower(COALESCE(cs.esfera_orgao, '')) LIKE '%federal%' THEN 3
                    WHEN lower(COALESCE(cs.esfera_orgao, '')) LIKE '%estadual%' THEN 2
                    WHEN lower(COALESCE(cs.esfera_orgao, '')) LIKE '%municipal%' THEN 1
                    ELSE 1
                END)
            ), 2) AS sanction_scope_score
        FROM temp_shared_successors ts
        JOIN ceis_sanctions cs
          ON cs.cpf_cnpj_norm = ts.sanctioned_cnpj
        GROUP BY 1;

        CREATE INDEX temp_idx_sanction_scope_successor
            ON temp_sanction_scope(successor_cnpj);

        CREATE TEMP TABLE temp_post_contracts AS
        SELECT
            sa.successor_cnpj,
            sa.created_post_sanction,
            sa.anchor_sanction_date,
            ce.id AS contract_id,
            ce.organ_cnpj,
            ce.data_assinatura,
            COALESCE(ce.valor_global, ce.valor_inicial, 0) AS contract_value,
            ce.delta_pct,
            ce.delta_valor,
            ce.categoria_processo_nome
        FROM temp_supplier_anchor sa
        JOIN contracts_enriched ce
          ON ce.supplier_cnpj = sa.successor_cnpj
        WHERE ce.data_assinatura IS NOT NULL
          AND ce.data_assinatura >= sa.anchor_sanction_date;

        CREATE INDEX temp_idx_post_contracts_successor
            ON temp_post_contracts(successor_cnpj);
        CREATE INDEX temp_idx_post_contracts_created
            ON temp_post_contracts(created_post_sanction);

        CREATE TEMP TABLE temp_mother_pre_contracts AS
        SELECT
            sa.successor_cnpj,
            ts.sanctioned_cnpj,
            ce.id AS contract_id,
            ce.organ_cnpj,
            ce.categoria_processo_nome,
            ce.data_assinatura
        FROM temp_supplier_anchor sa
        JOIN temp_shared_successors ts
          ON ts.successor_cnpj = sa.successor_cnpj
        JOIN contracts_enriched ce
          ON ce.supplier_cnpj = ts.sanctioned_cnpj
        WHERE ce.data_assinatura IS NOT NULL
          AND ce.data_assinatura < sa.anchor_sanction_date;

        CREATE INDEX temp_idx_mother_pre_successor
            ON temp_mother_pre_contracts(successor_cnpj);

        CREATE TEMP TABLE temp_mother_organs AS
        SELECT DISTINCT successor_cnpj, organ_cnpj
        FROM temp_mother_pre_contracts;

        CREATE INDEX temp_idx_mother_organs_successor
            ON temp_mother_organs(successor_cnpj);

        CREATE TEMP TABLE temp_post_organs AS
        SELECT DISTINCT successor_cnpj, organ_cnpj
        FROM temp_post_contracts;

        CREATE INDEX temp_idx_post_organs_successor
            ON temp_post_organs(successor_cnpj);
        """
    )


def normalize_value(value: float | int | None) -> float | None:
    if value is None:
        return None
    return float(value)


def summarize_numeric(values: list[float]) -> dict:
    clean = [float(v) for v in values if v is not None and not math.isnan(float(v))]
    if not clean:
        return {"n": 0, "median": None, "mean": None, "p75": None}
    return {
        "n": len(clean),
        "median": round(statistics.median(clean), 4),
        "mean": round(sum(clean) / len(clean), 4),
        "p75": round(statistics.quantiles(clean, n=4, method="inclusive")[2], 4),
    }


def summarize_bool(values: list[int | bool]) -> dict:
    clean = [1 if v else 0 for v in values if v is not None]
    if not clean:
        return {"n": 0, "rate": None, "count_true": 0}
    count_true = sum(clean)
    return {
        "n": len(clean),
        "count_true": count_true,
        "rate": round(count_true / len(clean), 4),
    }


def classify_support(direction_ok: bool, difference: float | None, min_gap: float) -> str:
    if difference is None:
        return "inconclusive"
    if direction_ok and abs(difference) >= min_gap:
        return "supported"
    if not direction_ok and abs(difference) >= min_gap:
        return "refuted"
    return "weak"


def load_supplier_metrics(conn: sqlite3.Connection) -> list[dict]:
    rows = run_sql(
        conn,
        """
        WITH post_rollup AS (
            SELECT
                successor_cnpj,
                COUNT(*) AS post_contracts_total,
                MIN(data_assinatura) AS first_post_contract_date,
                SUM(CASE WHEN julianday(data_assinatura) <= julianday(anchor_sanction_date) + 30 THEN 1 ELSE 0 END) AS contracts_30d,
                SUM(CASE WHEN julianday(data_assinatura) <= julianday(anchor_sanction_date) + 90 THEN 1 ELSE 0 END) AS contracts_90d,
                SUM(CASE WHEN julianday(data_assinatura) <= julianday(anchor_sanction_date) + 180 THEN 1 ELSE 0 END) AS contracts_180d,
                ROUND(SUM(CASE WHEN julianday(data_assinatura) <= julianday(anchor_sanction_date) + 30 THEN contract_value ELSE 0 END), 2) AS value_30d,
                ROUND(SUM(CASE WHEN julianday(data_assinatura) <= julianday(anchor_sanction_date) + 90 THEN contract_value ELSE 0 END), 2) AS value_90d,
                ROUND(SUM(CASE WHEN julianday(data_assinatura) <= julianday(anchor_sanction_date) + 180 THEN contract_value ELSE 0 END), 2) AS value_180d,
                COUNT(DISTINCT organ_cnpj) AS post_organs,
                COUNT(DISTINCT CASE WHEN julianday(data_assinatura) <= julianday(anchor_sanction_date) + 90 THEN organ_cnpj END) AS buyer_burst_90d
            FROM temp_post_contracts
            GROUP BY 1
        ),
        buyer_overlap AS (
            SELECT
                sa.successor_cnpj,
                COUNT(DISTINCT po.organ_cnpj) AS post_organs,
                COUNT(DISTINCT CASE WHEN mo.organ_cnpj IS NULL THEN po.organ_cnpj END) AS new_organs
            FROM temp_supplier_anchor sa
            LEFT JOIN temp_post_organs po
              ON po.successor_cnpj = sa.successor_cnpj
            LEFT JOIN temp_mother_organs mo
              ON mo.successor_cnpj = sa.successor_cnpj
             AND mo.organ_cnpj = po.organ_cnpj
            GROUP BY 1
        ),
        additive_tail AS (
            SELECT
                successor_cnpj,
                SUM(CASE WHEN COALESCE(delta_pct, 0) > 50 THEN 1 ELSE 0 END) AS extreme_additive_gt50_count,
                SUM(CASE WHEN COALESCE(delta_pct, 0) > 100 THEN 1 ELSE 0 END) AS extreme_additive_gt100_count,
                MAX(COALESCE(delta_valor, 0)) AS max_delta_valor,
                MAX(CASE WHEN COALESCE(delta_pct, 0) > 50 THEN 1 ELSE 0 END) AS any_extreme_additive,
                MIN(data_assinatura) AS first_post_contract_date,
                MIN(CASE WHEN COALESCE(delta_pct, 0) > 50 THEN data_assinatura END) AS first_extreme_additive_date
            FROM temp_post_contracts
            GROUP BY 1
        ),
        category_shift AS (
            WITH mother_cat AS (
                SELECT DISTINCT successor_cnpj, categoria_processo_nome
                FROM temp_mother_pre_contracts
                WHERE categoria_processo_nome IS NOT NULL
            ),
            post_cat AS (
                SELECT DISTINCT successor_cnpj, categoria_processo_nome
                FROM temp_post_contracts
                WHERE categoria_processo_nome IS NOT NULL
            ),
            mother_count AS (
                SELECT successor_cnpj, COUNT(*) AS mother_categories
                FROM mother_cat
                GROUP BY 1
            ),
            post_count AS (
                SELECT successor_cnpj, COUNT(*) AS post_categories
                FROM post_cat
                GROUP BY 1
            ),
            overlap AS (
                SELECT m.successor_cnpj, COUNT(*) AS overlap_categories
                FROM mother_cat m
                JOIN post_cat p
                  ON p.successor_cnpj = m.successor_cnpj
                 AND p.categoria_processo_nome = m.categoria_processo_nome
                GROUP BY 1
            )
            SELECT
                sa.successor_cnpj,
                mc.mother_categories,
                pc.post_categories,
                COALESCE(ov.overlap_categories, 0) AS overlap_categories,
                CASE
                    WHEN COALESCE(mc.mother_categories, 0) + COALESCE(pc.post_categories, 0) - COALESCE(ov.overlap_categories, 0) = 0 THEN NULL
                    ELSE ROUND(
                        1.0 - (
                            CAST(COALESCE(ov.overlap_categories, 0) AS REAL) /
                            (COALESCE(mc.mother_categories, 0) + COALESCE(pc.post_categories, 0) - COALESCE(ov.overlap_categories, 0))
                        ),
                        4
                    )
                END AS category_shift_from_mother
            FROM temp_supplier_anchor sa
            LEFT JOIN mother_count mc
              ON mc.successor_cnpj = sa.successor_cnpj
            LEFT JOIN post_count pc
              ON pc.successor_cnpj = sa.successor_cnpj
            LEFT JOIN overlap ov
              ON ov.successor_cnpj = sa.successor_cnpj
        ),
        qsa_shift AS (
            SELECT
                sa.successor_cnpj,
                MIN(ABS(CAST(julianday(ss.data_entrada_sociedade) - julianday(sa.anchor_sanction_date) AS INTEGER))) AS min_abs_days_to_qsa_change,
                MAX(CASE
                    WHEN ABS(CAST(julianday(ss.data_entrada_sociedade) - julianday(sa.anchor_sanction_date) AS INTEGER)) <= 90
                    THEN 1 ELSE 0
                END) AS qsa_change_near_sanction
            FROM temp_supplier_anchor sa
            LEFT JOIN supplier_socios ss
              ON ss.cnpj = sa.successor_cnpj
             AND ss.data_entrada_sociedade IS NOT NULL
             AND ss.data_entrada_sociedade <> ''
            GROUP BY 1
        )
        SELECT
            sa.successor_cnpj,
            sa.created_post_sanction,
            sa.anchor_sanction_date,
            sa.data_inicio_atividade,
            sa.same_socio_sanction_count,
            COALESCE(ssc.sanction_scope_score, 0) AS sanction_scope_score,
            pr.post_contracts_total,
            pr.first_post_contract_date,
            pr.contracts_30d,
            pr.contracts_90d,
            pr.contracts_180d,
            pr.value_30d,
            pr.value_90d,
            pr.value_180d,
            pr.buyer_burst_90d,
            at.extreme_additive_gt50_count,
            at.extreme_additive_gt100_count,
            at.max_delta_valor,
            COALESCE(at.any_extreme_additive, 0) AS any_extreme_additive,
            CASE
                WHEN at.first_extreme_additive_date IS NULL THEN NULL
                ELSE CAST(julianday(at.first_extreme_additive_date) - julianday(at.first_post_contract_date) AS INTEGER)
            END AS stealth_to_extraction_gap_days,
            CASE
                WHEN sa.data_inicio_atividade IS NULL OR pr.first_post_contract_date IS NULL THEN NULL
                ELSE ROUND((julianday(pr.first_post_contract_date) - julianday(sa.data_inicio_atividade)) / 365.25, 4)
            END AS activation_lag_years,
            CASE
                WHEN pr.first_post_contract_date IS NULL THEN NULL
                ELSE CAST(julianday(pr.first_post_contract_date) - julianday(sa.anchor_sanction_date) AS INTEGER)
            END AS post_sanction_activation_gap_days,
            CASE
                WHEN sa.data_inicio_atividade IS NOT NULL
                 AND pr.first_post_contract_date IS NOT NULL
                 AND ((julianday(pr.first_post_contract_date) - julianday(sa.data_inicio_atividade)) / 365.25) >= 3.0
                 AND ABS(CAST(julianday(pr.first_post_contract_date) - julianday(sa.anchor_sanction_date) AS INTEGER)) <= 30
                THEN 1 ELSE 0
            END AS dormant_activation_flag,
            bo.post_organs,
            bo.new_organs,
            CASE
                WHEN COALESCE(bo.post_organs, 0) = 0 THEN NULL
                ELSE ROUND(CAST(bo.new_organs AS REAL) / bo.post_organs, 4)
            END AS new_buyer_ratio,
            cs.mother_categories,
            cs.post_categories,
            cs.overlap_categories,
            cs.category_shift_from_mother,
            qs.min_abs_days_to_qsa_change,
            COALESCE(qs.qsa_change_near_sanction, 0) AS qsa_change_near_sanction
        FROM temp_supplier_anchor sa
        LEFT JOIN temp_sanction_scope ssc
          ON ssc.successor_cnpj = sa.successor_cnpj
        LEFT JOIN post_rollup pr
          ON pr.successor_cnpj = sa.successor_cnpj
        LEFT JOIN additive_tail at
          ON at.successor_cnpj = sa.successor_cnpj
        LEFT JOIN buyer_overlap bo
          ON bo.successor_cnpj = sa.successor_cnpj
        LEFT JOIN category_shift cs
          ON cs.successor_cnpj = sa.successor_cnpj
        LEFT JOIN qsa_shift qs
          ON qs.successor_cnpj = sa.successor_cnpj
        WHERE COALESCE(pr.post_contracts_total, 0) > 0
        ORDER BY sa.created_post_sanction DESC, pr.post_contracts_total DESC
        """,
    )
    return rows


def split_groups(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    genuine = [row for row in rows if row["created_post_sanction"] == 1]
    preexisting = [row for row in rows if row["created_post_sanction"] == 0]
    return genuine, preexisting


def build_test_summary(
    key: str,
    metric: str,
    genuine_rows: list[dict],
    pre_rows: list[dict],
    *,
    threshold: float | None = None,
    higher_is_expected: bool = True,
    bool_metric: bool = False,
    threshold_mode: str = "gte",
    min_gap_override: float | None = None,
) -> dict:
    genuine_values = [row.get(metric) for row in genuine_rows]
    pre_values = [row.get(metric) for row in pre_rows]
    if bool_metric:
        genuine_summary = summarize_bool(genuine_values)
        pre_summary = summarize_bool(pre_values)
        difference = None
        if genuine_summary["rate"] is not None and pre_summary["rate"] is not None:
            difference = round(genuine_summary["rate"] - pre_summary["rate"], 4)
        direction_ok = difference is not None and ((difference > 0) if higher_is_expected else (difference < 0))
        support = classify_support(direction_ok, difference, 0.05)
    else:
        genuine_summary = summarize_numeric([normalize_value(v) for v in genuine_values if v is not None])
        pre_summary = summarize_numeric([normalize_value(v) for v in pre_values if v is not None])
        difference = None
        if genuine_summary["median"] is not None and pre_summary["median"] is not None:
            difference = round(genuine_summary["median"] - pre_summary["median"], 4)
        direction_ok = difference is not None and ((difference > 0) if higher_is_expected else (difference < 0))
        min_gap = min_gap_override if min_gap_override is not None else (0.1 if (metric.endswith("_ratio") or "shift" in metric) else 1.0)
        support = classify_support(direction_ok, difference, min_gap)

    threshold_rates = None
    if threshold is not None:
        if bool_metric:
            threshold_rates = {
                "genuine": genuine_summary["rate"],
                "preexisting": pre_summary["rate"],
            }
        else:
            if threshold_mode == "lte":
                g_rate = summarize_bool([1 if (v is not None and float(v) <= threshold) else 0 for v in genuine_values if v is not None])
                p_rate = summarize_bool([1 if (v is not None and float(v) <= threshold) else 0 for v in pre_values if v is not None])
            else:
                g_rate = summarize_bool([1 if (v is not None and float(v) >= threshold) else 0 for v in genuine_values if v is not None])
                p_rate = summarize_bool([1 if (v is not None and float(v) >= threshold) else 0 for v in pre_values if v is not None])
            threshold_rates = {
                "threshold": threshold,
                "mode": threshold_mode,
                "genuine_rate": g_rate["rate"],
                "preexisting_rate": p_rate["rate"],
            }

    return {
        "feature": key,
        "metric": metric,
        "genuine": genuine_summary,
        "preexisting": pre_summary,
        "difference_genuine_minus_preexisting": difference,
        "support": support,
        "threshold_comparison": threshold_rates,
    }


def build_threshold_outcome_summary(
    feature: str,
    rows: list[dict],
    *,
    feature_metric: str,
    threshold: float,
    outcome_metric: str,
    threshold_mode: str = "gte",
) -> dict:
    def is_selected(value: object) -> bool:
        if value is None:
            return False
        if threshold_mode == "lte":
            return float(value) <= threshold
        return float(value) >= threshold

    selected = [row for row in rows if is_selected(row.get(feature_metric))]
    unselected = [row for row in rows if row.get(feature_metric) is not None and not is_selected(row.get(feature_metric))]
    selected_outcome = summarize_bool([row.get(outcome_metric) for row in selected])
    unselected_outcome = summarize_bool([row.get(outcome_metric) for row in unselected])
    difference = None
    if selected_outcome["rate"] is not None and unselected_outcome["rate"] is not None:
        difference = round(selected_outcome["rate"] - unselected_outcome["rate"], 4)
    direction_ok = difference is not None and difference > 0
    support = classify_support(direction_ok, difference, 0.05)
    return {
        "feature": feature,
        "feature_metric": feature_metric,
        "outcome_metric": outcome_metric,
        "threshold": threshold,
        "mode": threshold_mode,
        "selected": selected_outcome,
        "unselected": unselected_outcome,
        "difference_selected_minus_unselected": difference,
        "support": support,
    }


def build_payload(db_path: str, supplier_rows: list[dict]) -> dict:
    genuine_rows, pre_rows = split_groups(supplier_rows)
    tests = {
        "sanction_scope_score": build_test_summary(
            "sanction_scope_score",
            "sanction_scope_score",
            genuine_rows,
            pre_rows,
            threshold=4,
            higher_is_expected=True,
        ),
        "same_socio_sanction_count": build_test_summary(
            "same_socio_sanction_count",
            "same_socio_sanction_count",
            genuine_rows,
            pre_rows,
            threshold=2,
            higher_is_expected=True,
        ),
        "post_sanction_ramp_speed_contracts_90d": build_test_summary(
            "post_sanction_ramp_speed",
            "contracts_90d",
            genuine_rows,
            pre_rows,
            threshold=5,
            higher_is_expected=True,
        ),
        "post_sanction_ramp_speed_value_90d": build_test_summary(
            "post_sanction_ramp_speed",
            "value_90d",
            genuine_rows,
            pre_rows,
            threshold=100000,
            higher_is_expected=True,
        ),
        "activation_lag_post_sanction": build_test_summary(
            "activation_lag_post_sanction",
            "post_sanction_activation_gap_days",
            genuine_rows,
            pre_rows,
            threshold=30,
            higher_is_expected=False,
            threshold_mode="lte",
        ),
        "new_buyer_ratio": build_test_summary(
            "new_buyer_ratio",
            "new_buyer_ratio",
            genuine_rows,
            pre_rows,
            threshold=0.8,
            higher_is_expected=True,
        ),
        "extreme_additive_tail_any": build_test_summary(
            "extreme_additive_tail",
            "any_extreme_additive",
            genuine_rows,
            pre_rows,
            higher_is_expected=True,
            bool_metric=True,
        ),
        "extreme_additive_tail_count_gt50": build_test_summary(
            "extreme_additive_tail",
            "extreme_additive_gt50_count",
            genuine_rows,
            pre_rows,
            threshold=1,
            higher_is_expected=True,
        ),
        "extreme_additive_tail_count_gt100": build_test_summary(
            "extreme_additive_tail",
            "extreme_additive_gt100_count",
            genuine_rows,
            pre_rows,
            threshold=1,
            higher_is_expected=True,
        ),
        "max_delta_valor": build_test_summary(
            "extreme_additive_tail",
            "max_delta_valor",
            genuine_rows,
            pre_rows,
            threshold=100000,
            higher_is_expected=True,
        ),
        "stealth_to_extraction_gap_days": build_test_summary(
            "stealth_to_extraction_gap",
            "stealth_to_extraction_gap_days",
            genuine_rows,
            pre_rows,
            threshold=365,
            higher_is_expected=False,
            threshold_mode="lte",
        ),
        "category_shift_from_mother": build_test_summary(
            "category_shift_from_mother",
            "category_shift_from_mother",
            genuine_rows,
            pre_rows,
            threshold=0.5,
            higher_is_expected=False,
            threshold_mode="lte",
            min_gap_override=0.1,
        ),
        "qsa_change_near_sanction": build_test_summary(
            "qsa_change_near_sanction",
            "qsa_change_near_sanction",
            genuine_rows,
            pre_rows,
            higher_is_expected=True,
            bool_metric=True,
        ),
        "min_abs_days_to_qsa_change": build_test_summary(
            "qsa_change_near_sanction",
            "min_abs_days_to_qsa_change",
            genuine_rows,
            pre_rows,
            threshold=90,
            higher_is_expected=False,
            threshold_mode="lte",
        ),
    }
    association_tests = {
        "sanction_scope_score_to_extreme_additive": build_threshold_outcome_summary(
            "sanction_scope_score",
            supplier_rows,
            feature_metric="sanction_scope_score",
            threshold=4,
            outcome_metric="any_extreme_additive",
        ),
        "same_socio_sanction_count_to_extreme_additive": build_threshold_outcome_summary(
            "same_socio_sanction_count",
            supplier_rows,
            feature_metric="same_socio_sanction_count",
            threshold=2,
            outcome_metric="any_extreme_additive",
        ),
    }
    return {
        "meta": {
            "db": db_path,
            "supplier_rows_with_post_contracts": len(supplier_rows),
            "genuine_suppliers_with_post_contracts": len(genuine_rows),
            "preexisting_suppliers_with_post_contracts": len(pre_rows),
        },
        "feature_catalog": [spec.__dict__ for spec in FEATURE_SPECS],
        "supplier_metrics_preview": supplier_rows[:50],
        "tested_features": tests,
        "association_tests": association_tests,
    }


def render_test_line(name: str, test: dict) -> str:
    g = test["genuine"]
    p = test["preexisting"]
    if "rate" in g and g["rate"] is not None:
        return (
            f"- `{name}`: genuine {g['rate']:.2%} vs preexisting {p['rate']:.2%}; "
            f"support = **{test['support']}**."
        )
    return (
        f"- `{name}`: median genuine {g['median']} vs preexisting {p['median']}; "
        f"support = **{test['support']}**."
    )


def build_markdown(payload: dict) -> str:
    meta = payload["meta"]
    tests = payload["tested_features"]
    catalog = payload["feature_catalog"]

    lines = [
        "# Phoenix Feature Falsification Report",
        "",
        "Base: `bid_engine.db` com definicao operacional de successor por CPF compartilhado em `supplier_socios`, sancao em `ceis_sanctions`, data de criacao em `suppliers_rfb`, e contratos em `contracts_enriched`.",
        "",
        "## Dataset",
        "",
        f"- suppliers com contratos pos-sancao: `{meta['supplier_rows_with_post_contracts']}`",
        f"- genuine (`created_post_sanction = 1`): `{meta['genuine_suppliers_with_post_contracts']}`",
        f"- preexisting (`created_post_sanction = 0`): `{meta['preexisting_suppliers_with_post_contracts']}`",
        "",
        "## Tested Now",
        "",
        render_test_line("sanction_scope_score", tests["sanction_scope_score"]),
        render_test_line("same_socio_sanction_count", tests["same_socio_sanction_count"]),
        render_test_line("post_sanction_ramp_speed / contracts_90d", tests["post_sanction_ramp_speed_contracts_90d"]),
        render_test_line("post_sanction_ramp_speed / value_90d", tests["post_sanction_ramp_speed_value_90d"]),
        render_test_line("activation_lag_post_sanction", tests["activation_lag_post_sanction"]),
        render_test_line("new_buyer_ratio", tests["new_buyer_ratio"]),
        render_test_line("extreme_additive_tail / any", tests["extreme_additive_tail_any"]),
        render_test_line("extreme_additive_tail / gt50 count", tests["extreme_additive_tail_count_gt50"]),
        render_test_line("extreme_additive_tail / gt100 count", tests["extreme_additive_tail_count_gt100"]),
        render_test_line("max_delta_valor", tests["max_delta_valor"]),
        render_test_line("stealth_to_extraction_gap_days", tests["stealth_to_extraction_gap_days"]),
        render_test_line("category_shift_from_mother", tests["category_shift_from_mother"]),
        render_test_line("qsa_change_near_sanction", tests["qsa_change_near_sanction"]),
        render_test_line("min_abs_days_to_qsa_change", tests["min_abs_days_to_qsa_change"]),
        "",
        "Leitura curta:",
        "",
        "- `sanction_scope_score` entra para testar se gravidade/abrangencia da rede sancionada separa melhor os genuinos ou a fase 2.",
        "- `same_socio_sanction_count` melhora precision, mas fraco como feature isolada: a mediana empata, embora a taxa `>=2` seja maior em genuine.",
        "- `post_sanction_ramp_speed` foi refutado contra este controle: genuine nao aceleram mais rapido que os preexisting.",
        "- `activation_lag_post_sanction` testa diretamente a entrada rapida apos a sancao, sem misturar isso com a data de fundacao do CNPJ.",
        "- `new_buyer_ratio` confirma a tese substantiva de orgaos novos, mas quase todo mundo no universo de sucessores tambem fica alto; sozinho, separa pouco.",
        "- `extreme_additive_tail` e `stealth_to_extraction_gap` testam explicitamente a fase 2 como comportamento raro, mas mensuravel.",
        "- `category_shift_from_mother` testa continuidade operacional via semelhanca de categoria entre mae e sucessora.",
        "- `qsa_change_near_sanction` funciona melhor como distancia temporal minima do que como flag binaria de `<=90 dias`.",
        "",
        "## Association Tests",
        "",
        f"- `sanction_scope_score >= 4 -> any_extreme_additive`: support = **{payload['association_tests']['sanction_scope_score_to_extreme_additive']['support']}**.",
        f"- `same_socio_sanction_count >= 2 -> any_extreme_additive`: support = **{payload['association_tests']['same_socio_sanction_count_to_extreme_additive']['support']}**.",
        "",
        "## Feature Table",
        "",
        "| Feature | Tested now | SQL formula | Threshold inicial | Hipotese falseable |",
        "|---|---|---|---|---|",
    ]

    for spec in catalog:
        lines.append(
            f"| `{spec['key']}` | {'yes' if spec['tested_now'] else 'no'} | `{spec['sql_formula']}` | `{spec['threshold']}` | {spec['falsifiable_hypothesis']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretacao operacional",
            "",
            "- `supported` significa que a direcao prevista apareceu nos dados, com gap material entre genuine e preexisting.",
            "- `weak` significa que a direcao apareceu, mas o gap foi pequeno demais para ser uma feature principal sem combinacao com outras.",
            "- `refuted` significa que a direcao esperada nao apareceu; a feature pode continuar util para score, mas nao como eixo central.",
            "- `inconclusive` significa cobertura ou gap insuficiente.",
            "",
            "## Leituras",
            "",
            "- `same_socio_sanction_count >= 2` e uma boa feature de precision se a multiplicidade realmente separar genuine de preexisting.",
            "- `post_sanction_ramp_speed` serve para capturar reentrada operacional rapida; se so o grupo genuine disparar, vira feature forte.",
            "- `new_buyer_ratio >= 0.8` testa diretamente a tese de credencialismo em orgaos novos.",
            "- `qsa_change_near_sanction` e a camada mais juridicamente explicavel; se aparecer com forca, entra no laudo.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    conn = sqlite3.connect(args.db)
    conn.row_factory = row_factory
    conn.execute("PRAGMA temp_store = MEMORY")
    conn.execute("PRAGMA mmap_size = 268435456")
    conn.execute("PRAGMA cache_size = -200000")

    build_temp_tables(conn)
    supplier_rows = load_supplier_metrics(conn)
    payload = build_payload(args.db, supplier_rows)

    json_path = Path(args.json_output)
    md_path = Path(args.md_output)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(build_markdown(payload))

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
