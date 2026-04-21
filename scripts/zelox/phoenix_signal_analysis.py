#!/usr/bin/env python3
"""
Exploratory phoenix-signal analysis over bid_engine.db.

Focus:
- compare post-debarment phoenix contracts vs baseline contracts
- measure more than delta_pct:
  * award vs estimate discount
  * category/modality mix
  * contract duration and plurianuality
  * organ concentration
  * lag from sanction to first observed contract
  * first vs later post-debarment contracts

Current phoenix heuristic:
- start from CEIS sanctions for PJs
- find sanctioned firms in supplier_socios
- link to other firms sharing a partner identifier (`cnpj_cpf`) or PJ partner CNPJ
- keep successor contracts signed after sanction date

The heuristic is permissive and can produce false positives.
"""

from __future__ import annotations

import argparse
import json
import math
import sqlite3
from collections import Counter
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--sample-sanctioned",
        type=int,
        default=0,
        help="Optional limit of sanctioned firms for faster iteration; 0 = all",
    )
    parser.add_argument(
        "--min-post-contracts",
        type=int,
        default=1,
        help="Minimum post-debarment contracts per successor firm",
    )
    parser.add_argument(
        "--baseline-limit",
        type=int,
        default=50000,
        help="Max non-phoenix baseline contracts to materialize; 0 = skip baseline",
    )
    return parser.parse_args()


def row_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def fetch_all(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> list[dict]:
    cur = conn.execute(sql, params)
    rows = cur.fetchall()
    return rows


def fetch_one(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> dict:
    cur = conn.execute(sql, params)
    row = cur.fetchone()
    return row or {}


PHOENIX_BASE_CTE = """
WITH partner_links AS (
    SELECT DISTINCT ss1.cnpj AS sanctioned_cnpj_candidate
    FROM supplier_socios ss1
    JOIN supplier_socios ss2
      ON ss2.cnpj_cpf = ss1.cnpj_cpf
     AND ss2.cnpj != ss1.cnpj
    WHERE ss1.cnpj_cpf IS NOT NULL
      AND ss1.cnpj_cpf != ''
),
sanctioned AS (
    SELECT
        cpf_cnpj_norm AS sanctioned_cnpj,
        MIN(substr(data_inicio, 7, 4) || '-' || substr(data_inicio, 4, 2) || '-' || substr(data_inicio, 1, 2)) AS sanction_date
    FROM ceis_sanctions
    WHERE LENGTH(cpf_cnpj_norm) = 14
      AND data_inicio LIKE '__/__/____'
      AND cpf_cnpj_norm IN (SELECT sanctioned_cnpj_candidate FROM partner_links)
    GROUP BY 1
    {sanction_limit}
),
shared_partner AS (
    SELECT
        s.sanctioned_cnpj,
        s.sanction_date,
        ss1.cnpj AS source_cnpj,
        ss2.cnpj AS successor_cnpj,
        ss1.cnpj_cpf AS shared_partner_id
    FROM sanctioned s
    JOIN supplier_socios ss1
      ON ss1.cnpj = s.sanctioned_cnpj
    JOIN supplier_socios ss2
      ON ss2.cnpj_cpf = ss1.cnpj_cpf
     AND ss2.cnpj != ss1.cnpj
    WHERE ss1.cnpj_cpf IS NOT NULL
      AND ss1.cnpj_cpf != ''
),
post_contracts AS (
    SELECT
        sp.sanctioned_cnpj,
        sp.successor_cnpj,
        sp.sanction_date,
        sp.shared_partner_id,
        ce.id AS contract_id,
        ce.organ_cnpj,
        ce.supplier_cnpj,
        ce.data_assinatura,
        ce.data_vigencia_inicio,
        ce.data_vigencia_fim,
        ce.tipo_contrato_nome,
        ce.categoria_processo_nome,
        ce.modality_code,
        ce.contrato_plurianual,
        ce.from_ata,
        ce.join_confidence,
        ce.awarded_value,
        ce.delta_pct,
        ce.valor_global,
        ce.valor_inicial,
        ce.compra_pncp_id,
        n.estimated_value,
        n.modality,
        ROW_NUMBER() OVER (
            PARTITION BY sp.sanctioned_cnpj, sp.successor_cnpj
            ORDER BY ce.data_assinatura, ce.id
        ) AS contract_order
    FROM shared_partner sp
    JOIN contracts_enriched ce
      ON ce.supplier_cnpj_root = substr(sp.successor_cnpj, 1, 8)
     AND ce.supplier_cnpj = sp.successor_cnpj
    LEFT JOIN notices n
      ON n.pncp_sequence = ce.compra_pncp_id
    WHERE ce.data_assinatura IS NOT NULL
      AND ce.data_assinatura >= sp.sanction_date
),
eligible_successors AS (
    SELECT
        sanctioned_cnpj,
        successor_cnpj
    FROM post_contracts
    GROUP BY 1, 2
    HAVING COUNT(*) >= :min_post_contracts
),
phoenix_post_contracts AS (
    SELECT pc.*
    FROM post_contracts pc
    JOIN eligible_successors es
      ON es.sanctioned_cnpj = pc.sanctioned_cnpj
     AND es.successor_cnpj = pc.successor_cnpj
)
"""


SIGNAL_SELECT = """
SELECT
    contract_id,
    sanctioned_cnpj,
    successor_cnpj AS supplier_cnpj,
    organ_cnpj,
    data_assinatura,
    data_vigencia_inicio,
    data_vigencia_fim,
    categoria_processo_nome,
    tipo_contrato_nome,
    modality,
    modality_code,
    contrato_plurianual,
    from_ata,
    join_confidence,
    awarded_value,
    estimated_value,
    delta_pct,
    valor_global,
    valor_inicial,
    compra_pncp_id,
    contract_order,
    julianday(data_vigencia_fim) - julianday(data_vigencia_inicio) AS duration_days,
    julianday(data_assinatura) - julianday(sanction_date) AS days_after_sanction,
    CASE
        WHEN estimated_value IS NOT NULL AND estimated_value > 0 AND awarded_value IS NOT NULL
        THEN ((awarded_value / estimated_value) - 1.0) * 100.0
    END AS award_vs_estimated_pct,
    CASE
        WHEN valor_inicial IS NOT NULL AND valor_inicial > 0 AND awarded_value IS NOT NULL
        THEN ((valor_inicial / awarded_value) - 1.0) * 100.0
    END AS contract_vs_award_pct
FROM phoenix_post_contracts
"""


BASELINE_SELECT = """
WITH phoenix_suppliers AS (
    {phoenix_base_cte}
    SELECT DISTINCT supplier_cnpj
    FROM phoenix_post_contracts
),
baseline_contracts AS (
    SELECT
        ce.id AS contract_id,
        ce.supplier_cnpj,
        ce.organ_cnpj,
        ce.data_assinatura,
        ce.data_vigencia_inicio,
        ce.data_vigencia_fim,
        ce.categoria_processo_nome,
        ce.tipo_contrato_nome,
        ce.modality_code,
        ce.contrato_plurianual,
        ce.from_ata,
        ce.join_confidence,
        ce.awarded_value,
        ce.delta_pct,
        ce.valor_global,
        ce.valor_inicial,
        ce.compra_pncp_id,
        n.estimated_value,
        n.modality,
        julianday(ce.data_vigencia_fim) - julianday(ce.data_vigencia_inicio) AS duration_days,
        CASE
            WHEN n.estimated_value IS NOT NULL AND n.estimated_value > 0 AND ce.awarded_value IS NOT NULL
            THEN ((ce.awarded_value / n.estimated_value) - 1.0) * 100.0
        END AS award_vs_estimated_pct,
        CASE
            WHEN ce.valor_inicial IS NOT NULL AND ce.valor_inicial > 0 AND ce.awarded_value IS NOT NULL
            THEN ((ce.valor_inicial / ce.awarded_value) - 1.0) * 100.0
        END AS contract_vs_award_pct
    FROM contracts_enriched ce
    LEFT JOIN notices n
      ON n.pncp_sequence = ce.compra_pncp_id
    WHERE ce.supplier_cnpj IS NOT NULL
      AND ce.data_assinatura IS NOT NULL
      AND ce.supplier_cnpj NOT IN (SELECT supplier_cnpj FROM phoenix_suppliers)
      AND ce.awarded_value IS NOT NULL
    LIMIT :baseline_limit
)
SELECT * FROM baseline_contracts
"""


def percentile(values: list[float], p: float) -> float | None:
    if not values:
        return None
    values = sorted(values)
    if len(values) == 1:
        return values[0]
    idx = (len(values) - 1) * p
    lo = math.floor(idx)
    hi = math.ceil(idx)
    if lo == hi:
        return values[lo]
    weight = idx - lo
    return values[lo] * (1 - weight) + values[hi] * weight


def summarize_numeric(rows: list[dict], key: str) -> dict:
    values = [row[key] for row in rows if row.get(key) is not None]
    if not values:
        return {"count": 0}
    return {
        "count": len(values),
        "mean": sum(values) / len(values),
        "median": percentile(values, 0.5),
        "p10": percentile(values, 0.10),
        "p90": percentile(values, 0.90),
        "min": min(values),
        "max": max(values),
    }


def top_share(rows: list[dict], entity_key: str, group_key: str = "supplier_cnpj") -> dict:
    grouped: dict[str, Counter] = {}
    for row in rows:
        g = row.get(group_key)
        e = row.get(entity_key)
        if not g or not e:
            continue
        grouped.setdefault(g, Counter())[e] += 1

    shares: list[float] = []
    for counts in grouped.values():
        total = sum(counts.values())
        if total == 0:
            continue
        shares.append(counts.most_common(1)[0][1] / total)
    return {
        "supplier_count": len(grouped),
        "mean_top1_share": sum(shares) / len(shares) if shares else None,
        "median_top1_share": percentile(shares, 0.5),
    }


def categorical_share(rows: list[dict], key: str, top_n: int = 10) -> list[dict]:
    counter = Counter(row.get(key) or "NULL" for row in rows)
    total = sum(counter.values()) or 1
    return [
        {"value": value, "count": count, "share": count / total}
        for value, count in counter.most_common(top_n)
    ]


def compare_flag(rows: list[dict], key: str, predicate) -> dict:
    values = [row for row in rows if row.get(key) is not None]
    if not values:
        return {"count": 0}
    positives = sum(1 for row in values if predicate(row[key]))
    return {"count": len(values), "positives": positives, "rate": positives / len(values)}


def build_summary(rows: list[dict]) -> dict:
    return {
        "rows": len(rows),
        "unique_suppliers": len({row.get("supplier_cnpj") for row in rows if row.get("supplier_cnpj")}),
        "unique_organs": len({row.get("organ_cnpj") for row in rows if row.get("organ_cnpj")}),
        "delta_pct": summarize_numeric(rows, "delta_pct"),
        "award_vs_estimated_pct": summarize_numeric(rows, "award_vs_estimated_pct"),
        "contract_vs_award_pct": summarize_numeric(rows, "contract_vs_award_pct"),
        "duration_days": summarize_numeric(rows, "duration_days"),
        "days_after_sanction": summarize_numeric(rows, "days_after_sanction"),
        "rate_delta_above_25": compare_flag(rows, "delta_pct", lambda x: x >= 25),
        "rate_delta_below_0": compare_flag(rows, "delta_pct", lambda x: x < 0),
        "rate_award_below_estimate_10": compare_flag(rows, "award_vs_estimated_pct", lambda x: x <= -10),
        "rate_contract_below_award_10": compare_flag(rows, "contract_vs_award_pct", lambda x: x <= -10),
        "rate_plurianual": compare_flag(rows, "contrato_plurianual", lambda x: x == 1),
        "rate_from_ata": compare_flag(rows, "from_ata", lambda x: x == 1),
        "modality_mix": categorical_share(rows, "modality"),
        "category_mix": categorical_share(rows, "categoria_processo_nome"),
        "contract_type_mix": categorical_share(rows, "tipo_contrato_nome"),
        "join_confidence_mix": categorical_share(rows, "join_confidence"),
        "organ_concentration": top_share(rows, "organ_cnpj"),
    }


def main() -> int:
    args = parse_args()
    conn = sqlite3.connect(args.db)
    conn.row_factory = row_factory
    conn.execute("PRAGMA temp_store = MEMORY")
    conn.execute("PRAGMA mmap_size = 268435456")
    conn.execute("PRAGMA cache_size = -200000")

    sanction_limit = ""
    if args.sample_sanctioned > 0:
        sanction_limit = f"LIMIT {args.sample_sanctioned}"

    phoenix_cte = PHOENIX_BASE_CTE.format(sanction_limit=sanction_limit)

    post_rows = fetch_all(conn, phoenix_cte + SIGNAL_SELECT, {"min_post_contracts": args.min_post_contracts})
    first_rows = [row for row in post_rows if row.get("contract_order") == 1]
    later_rows = [row for row in post_rows if (row.get("contract_order") or 0) >= 2]

    baseline_rows: list[dict] = []
    if args.baseline_limit > 0:
        baseline_sql = BASELINE_SELECT.format(phoenix_base_cte=phoenix_cte)
        baseline_rows = fetch_all(
            conn,
            baseline_sql,
            {
                "min_post_contracts": args.min_post_contracts,
                "baseline_limit": args.baseline_limit,
            },
        )

    pair_summary = fetch_one(
        conn,
        phoenix_cte
        + """
        SELECT
            COUNT(DISTINCT sanctioned_cnpj) AS sanctioned_firms,
            COUNT(DISTINCT supplier_cnpj) AS successor_firms,
            COUNT(DISTINCT sanctioned_cnpj || '->' || supplier_cnpj) AS pairs
        FROM phoenix_post_contracts
        """,
        {"min_post_contracts": args.min_post_contracts},
    )

    result = {
        "meta": {
            "db": args.db,
            "sample_sanctioned": args.sample_sanctioned,
            "min_post_contracts": args.min_post_contracts,
            "baseline_limit": args.baseline_limit,
        },
        "pair_summary": pair_summary,
        "post_debarment_all": build_summary(post_rows),
        "post_debarment_first_contract": build_summary(first_rows),
        "post_debarment_later_contracts": build_summary(later_rows),
        "baseline_all_non_phoenix": build_summary(baseline_rows),
        "top_suppliers_by_post_contracts": categorical_share(post_rows, "supplier_cnpj", top_n=15),
        "top_organs_post_debarment": categorical_share(post_rows, "organ_cnpj", top_n=15),
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {output}")
    print(json.dumps(result["pair_summary"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
