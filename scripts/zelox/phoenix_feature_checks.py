#!/usr/bin/env python3
"""
Targeted phoenix feature checks for bid_engine.db.

Checks requested:
1. repetition of wins in the same organ
2. concentration by organ/buyer
3. whether win-rate can be measured with current schema
4. whether "created post-sanction" should be a mandatory feature
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--output", required=True)
    return parser.parse_args()


def row_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def q(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> list[dict]:
    return conn.execute(sql, params).fetchall()


def one(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> dict:
    row = conn.execute(sql, params).fetchone()
    return row or {}


def build_temp_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        DROP TABLE IF EXISTS temp_sanctioned_pj;
        DROP TABLE IF EXISTS temp_shared_successors;
        DROP TABLE IF EXISTS temp_successor_flags;
        DROP TABLE IF EXISTS temp_post_contracts;

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
         AND ss2.cnpj != ss1.cnpj
        WHERE ss1.cnpj_cpf IS NOT NULL
          AND ss1.cnpj_cpf != '';

        CREATE INDEX temp_idx_successor_cnpj
            ON temp_shared_successors(successor_cnpj);

        CREATE TEMP TABLE temp_successor_flags AS
        SELECT
            ts.sanctioned_cnpj,
            ts.sanction_date,
            ts.successor_cnpj,
            rfb.data_inicio_atividade,
            CASE
                WHEN rfb.data_inicio_atividade IS NOT NULL
                 AND rfb.data_inicio_atividade > ts.sanction_date
                THEN 1 ELSE 0
            END AS created_post_sanction
        FROM temp_shared_successors ts
        LEFT JOIN suppliers_rfb rfb
          ON rfb.cnpj = ts.successor_cnpj;

        CREATE INDEX temp_idx_successor_flags_successor
            ON temp_successor_flags(successor_cnpj);
        CREATE INDEX temp_idx_successor_flags_created
            ON temp_successor_flags(created_post_sanction);

        CREATE TEMP TABLE temp_post_contracts AS
        SELECT
            sf.sanctioned_cnpj,
            sf.sanction_date,
            sf.successor_cnpj AS supplier_cnpj,
            sf.created_post_sanction,
            ce.organ_cnpj,
            ce.id AS contract_id,
            ce.data_assinatura,
            ce.categoria_processo_nome,
            ce.modality_code,
            ce.contracts_per_compra
        FROM temp_successor_flags sf
        JOIN contracts_enriched ce
          ON ce.supplier_cnpj = sf.successor_cnpj
        WHERE ce.data_assinatura IS NOT NULL
          AND ce.data_assinatura >= sf.sanction_date;

        CREATE INDEX temp_idx_post_contracts_created
            ON temp_post_contracts(created_post_sanction);
        CREATE INDEX temp_idx_post_contracts_supplier
            ON temp_post_contracts(supplier_cnpj);
        CREATE INDEX temp_idx_post_contracts_organ
            ON temp_post_contracts(organ_cnpj);
        """
    )


def get_temporal_filter_stats(conn: sqlite3.Connection) -> dict:
    return {
        "successor_candidates": one(
            conn,
            """
            SELECT
                COUNT(DISTINCT successor_cnpj) AS all_successors,
                COUNT(DISTINCT CASE WHEN created_post_sanction = 1 THEN successor_cnpj END) AS genuine_successors,
                COUNT(DISTINCT CASE WHEN created_post_sanction = 0 THEN successor_cnpj END) AS preexisting_successors
            FROM temp_successor_flags
            """,
        ),
        "contracts_post_sanction": q(
            conn,
            """
            SELECT
                created_post_sanction,
                COUNT(*) AS contracts,
                COUNT(DISTINCT supplier_cnpj) AS suppliers
            FROM temp_post_contracts
            GROUP BY 1
            ORDER BY 1
            """,
        ),
    }


def get_same_organ_repetition(conn: sqlite3.Connection) -> list[dict]:
    return q(
        conn,
        """
        WITH organ_counts AS (
            SELECT
                created_post_sanction,
                supplier_cnpj,
                organ_cnpj,
                COUNT(*) AS wins_same_organ
            FROM temp_post_contracts
            GROUP BY 1, 2, 3
        ),
        rollup AS (
            SELECT
                created_post_sanction,
                supplier_cnpj,
                SUM(wins_same_organ) AS total_contracts,
                MAX(wins_same_organ) AS max_same_organ,
                CAST(MAX(wins_same_organ) AS REAL) / SUM(wins_same_organ) AS top1_share,
                COUNT(*) AS organs_used
            FROM organ_counts
            GROUP BY 1, 2
        )
        SELECT
            created_post_sanction,
            COUNT(*) AS suppliers,
            ROUND(AVG(total_contracts), 3) AS avg_contracts_per_supplier,
            ROUND(AVG(max_same_organ), 3) AS avg_max_same_organ,
            ROUND(AVG(top1_share), 3) AS avg_top1_share,
            ROUND(AVG(organs_used), 3) AS avg_organs_used,
            SUM(CASE WHEN max_same_organ >= 2 THEN 1 ELSE 0 END) AS suppliers_with_repeat_same_organ,
            SUM(CASE WHEN max_same_organ >= 5 THEN 1 ELSE 0 END) AS suppliers_with_5plus_same_organ
        FROM rollup
        GROUP BY 1
        ORDER BY 1
        """,
    )


def get_top_organs(conn: sqlite3.Connection) -> list[dict]:
    return q(
        conn,
        """
        SELECT
            created_post_sanction,
            organ_cnpj,
            COUNT(*) AS contracts,
            COUNT(DISTINCT supplier_cnpj) AS suppliers
        FROM temp_post_contracts
        GROUP BY 1, 2
        ORDER BY created_post_sanction DESC, contracts DESC
        LIMIT 20
        """
    )


def get_organ_concentration(conn: sqlite3.Connection) -> list[dict]:
    return q(
        conn,
        """
        WITH organ_counts AS (
            SELECT
                created_post_sanction,
                supplier_cnpj,
                organ_cnpj,
                COUNT(*) AS wins_same_organ
            FROM temp_post_contracts
            GROUP BY 1, 2, 3
        ),
        shares AS (
            SELECT
                created_post_sanction,
                supplier_cnpj,
                organ_cnpj,
                wins_same_organ,
                CAST(wins_same_organ AS REAL) /
                    SUM(wins_same_organ) OVER (PARTITION BY created_post_sanction, supplier_cnpj) AS organ_share
            FROM organ_counts
        ),
        supplier_rollup AS (
            SELECT
                created_post_sanction,
                supplier_cnpj,
                MAX(organ_share) AS top1_share,
                SUM(organ_share * organ_share) AS hhi,
                SUM(CASE WHEN organ_share >= 0.8 THEN 1 ELSE 0 END) AS organs_above_80pct
            FROM shares
            GROUP BY 1, 2
        )
        SELECT
            created_post_sanction,
            COUNT(*) AS suppliers,
            ROUND(AVG(top1_share), 3) AS avg_top1_share,
            ROUND(AVG(hhi), 3) AS avg_hhi,
            SUM(CASE WHEN top1_share >= 0.5 THEN 1 ELSE 0 END) AS suppliers_top1_ge_50pct,
            SUM(CASE WHEN top1_share >= 0.8 THEN 1 ELSE 0 END) AS suppliers_top1_ge_80pct,
            SUM(CASE WHEN organs_above_80pct >= 1 THEN 1 ELSE 0 END) AS suppliers_single_organ_dominant
        FROM supplier_rollup
        GROUP BY 1
        ORDER BY 1
        """,
    )


def get_win_rate_proxy(conn: sqlite3.Connection) -> dict:
    participation_cte = """
        WITH supplier_item_participation AS (
            SELECT
                sf.created_post_sanction,
                pir.ni_fornecedor AS supplier_cnpj,
                pir.notice_id,
                pir.item_number,
                MAX(CASE WHEN COALESCE(pir.valor_total_homologado, 0) > 0 THEN 1 ELSE 0 END) AS won_item
            FROM pncp_item_results pir
            JOIN (
                SELECT DISTINCT successor_cnpj, created_post_sanction
                FROM temp_successor_flags
            ) sf
              ON sf.successor_cnpj = pir.ni_fornecedor
            WHERE pir.notice_id IS NOT NULL
              AND pir.item_number IS NOT NULL
            GROUP BY 1, 2, 3, 4
        ),
    """
    participation_summary = q(
        conn,
        participation_cte
        + """
        supplier_rollup AS (
            SELECT
                created_post_sanction,
                supplier_cnpj,
                COUNT(*) AS participations,
                SUM(won_item) AS wins,
                CAST(SUM(won_item) AS REAL) / COUNT(*) AS win_rate
            FROM supplier_item_participation
            GROUP BY 1, 2
        )
        SELECT
            created_post_sanction,
            COUNT(*) AS suppliers,
            SUM(participations) AS participations,
            SUM(wins) AS wins,
            ROUND(CAST(SUM(wins) AS REAL) / SUM(participations), 4) AS pooled_win_rate,
            ROUND(AVG(win_rate), 4) AS avg_supplier_win_rate,
            ROUND(AVG(participations), 2) AS avg_participations_per_supplier
        FROM supplier_rollup
        GROUP BY 1
        ORDER BY 1
        """,
    )
    item_signal_quality = one(
        conn,
        participation_cte
        + """
        item_rollup AS (
            SELECT
                notice_id,
                item_number,
                COUNT(*) AS bidders,
                SUM(won_item) AS winners
            FROM supplier_item_participation
            GROUP BY 1, 2
        )
        SELECT
            COUNT(*) AS total_notice_items,
            SUM(CASE WHEN bidders > 1 THEN 1 ELSE 0 END) AS competitive_items,
            SUM(CASE WHEN winners = 1 THEN 1 ELSE 0 END) AS items_with_single_winner,
            SUM(CASE WHEN winners > 1 THEN 1 ELSE 0 END) AS items_with_multiple_winners,
            SUM(CASE WHEN winners = 0 THEN 1 ELSE 0 END) AS items_with_zero_winner_flag
        FROM item_rollup
        """,
    )
    return {
        "method": "Distinct supplier participation per notice_id/item_number; win proxy = any row with valor_total_homologado > 0 for that supplier-item.",
        "participation_summary": participation_summary,
        "item_signal_quality": item_signal_quality,
    }


def get_win_rate_feasibility(conn: sqlite3.Connection) -> dict:
    item_results = one(
        conn,
        """
        WITH x AS (
            SELECT notice_id, item_number, COUNT(*) AS rows_per_item
            FROM pncp_item_results
            GROUP BY 1, 2
        )
        SELECT
            COUNT(*) AS total_notice_items,
            SUM(CASE WHEN rows_per_item > 1 THEN 1 ELSE 0 END) AS items_with_multiple_rows,
            MAX(rows_per_item) AS max_rows_per_item
        FROM x
        """
    )
    procurement_results = one(
        conn,
        """
        WITH x AS (
            SELECT notice_id, numero_item, COUNT(*) AS rows_per_item
            FROM procurement_results
            GROUP BY 1, 2
        )
        SELECT
            COUNT(*) AS total_notice_items,
            SUM(CASE WHEN rows_per_item > 1 THEN 1 ELSE 0 END) AS items_with_multiple_rows,
            MAX(rows_per_item) AS max_rows_per_item
        FROM x
        """
    )
    feasible = (
        (item_results.get("items_with_multiple_rows") or 0) > 0
        or (procurement_results.get("items_with_multiple_rows") or 0) > 0
    )
    return {
        "feasible_with_current_schema": feasible,
        "pncp_item_results": item_results,
        "procurement_results": procurement_results,
        "interpretation": (
            "Current schema appears winner-only per notice item; true win rate requires losers/bidders table."
            if not feasible
            else "Multiple rows per item exist; winner-rate analysis may be feasible."
        ),
    }


def main() -> int:
    args = parse_args()
    conn = sqlite3.connect(args.db)
    conn.row_factory = row_factory
    conn.execute("PRAGMA temp_store = MEMORY")
    conn.execute("PRAGMA mmap_size = 268435456")
    conn.execute("PRAGMA cache_size = -200000")
    build_temp_tables(conn)

    payload = {
        "meta": {"db": args.db},
        "temporal_filter": get_temporal_filter_stats(conn),
        "same_organ_repetition": get_same_organ_repetition(conn),
        "organ_concentration": get_organ_concentration(conn),
        "top_organs": get_top_organs(conn),
        "win_rate_feasibility": get_win_rate_feasibility(conn),
        "win_rate_proxy": get_win_rate_proxy(conn),
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {output}")
    print(json.dumps(payload["temporal_filter"]["successor_candidates"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
