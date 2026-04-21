#!/usr/bin/env python3
"""
Build a first-pass phoenix candidate table from local CEIS/QSA/contracts files.

This is intentionally local-file driven. The repo does not contain CEIS/QSA/RAIS
datasets, so the purpose here is to make the experiment executable as soon as
those files exist, without inventing a fake online integration.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import date
from datetime import datetime
from pathlib import Path


def load_rows(path: Path) -> list[dict]:
    if path.suffix.lower() == ".json":
        payload = json.loads(path.read_text())
        if isinstance(payload, dict):
            for key in ("records", "items", "data"):
                value = payload.get(key)
                if isinstance(value, list):
                    return value
        if isinstance(payload, list):
            return payload
        raise ValueError(f"unsupported json payload in {path}")
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8") as fh:
            return list(csv.DictReader(fh))
    raise ValueError(f"unsupported file type: {path}")


def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"):
        try:
            return datetime.strptime(value[: len(fmt)], fmt).date()
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def build_ceis_index(rows: list[dict], cnpj_key: str, date_key: str) -> dict[str, date]:
    result: dict[str, date] = {}
    for row in rows:
        cnpj = "".join(ch for ch in str(row.get(cnpj_key, "")) if ch.isdigit())
        if not cnpj:
            continue
        sanction_date = parse_date(str(row.get(date_key, "")))
        if sanction_date is None:
            continue
        result[cnpj] = sanction_date
    return result


def build_qsa_index(rows: list[dict], company_key: str, partner_key: str) -> dict[str, set[str]]:
    company_to_partners: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        company = "".join(ch for ch in str(row.get(company_key, "")) if ch.isdigit())
        partner = "".join(ch for ch in str(row.get(partner_key, "")) if ch.isdigit())
        if company and partner:
            company_to_partners[company].add(partner)
    return company_to_partners


def build_contract_index(
    rows: list[dict],
    supplier_key: str,
    control_key: str,
    published_key: str,
) -> dict[str, list[dict]]:
    by_supplier: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        supplier = "".join(ch for ch in str(row.get(supplier_key, "")) if ch.isdigit())
        if not supplier:
            continue
        by_supplier[supplier].append(
            {
                "numero_controle_pncp": row.get(control_key, ""),
                "data_publicacao_pncp": row.get(published_key, ""),
            }
        )
    return by_supplier


def detect_candidates(
    ceis_index: dict[str, date],
    qsa_index: dict[str, set[str]],
    contract_index: dict[str, list[dict]],
) -> list[dict]:
    partner_to_companies: dict[str, set[str]] = defaultdict(set)
    for company, partners in qsa_index.items():
        for partner in partners:
            partner_to_companies[partner].add(company)

    candidates: list[dict] = []
    for blocked_cnpj, blocked_on in ceis_index.items():
        partners = qsa_index.get(blocked_cnpj, set())
        seen_successors: set[str] = set()
        for partner in partners:
            for successor in partner_to_companies.get(partner, set()):
                if successor == blocked_cnpj or successor in seen_successors:
                    continue
                seen_successors.add(successor)
                contracts = contract_index.get(successor, [])
                post_block_contracts = [
                    c
                    for c in contracts
                    if (dt := parse_date(str(c.get("data_publicacao_pncp")))) and dt >= blocked_on
                ]
                if not post_block_contracts:
                    continue
                candidates.append(
                    {
                        "blocked_cnpj": blocked_cnpj,
                        "successor_cnpj": successor,
                        "blocked_on": blocked_on.isoformat(),
                        "shared_partner_count": len(partners & qsa_index.get(successor, set())),
                        "post_block_contracts": len(post_block_contracts),
                        "first_post_block_contract": post_block_contracts[0]["numero_controle_pncp"],
                    }
                )
    candidates.sort(
        key=lambda row: (
            row["post_block_contracts"],
            row["shared_partner_count"],
            row["blocked_on"],
        ),
        reverse=True,
    )
    return candidates


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ceis", required=True, help="CSV/JSON com CNPJ sancionado e data")
    parser.add_argument("--qsa", required=True, help="CSV/JSON com empresa_cnpj e socio_cpf")
    parser.add_argument(
        "--contracts",
        required=True,
        help="CSV/JSON com contratos normalizados contendo supplier CNPJ",
    )
    parser.add_argument("--ceis-cnpj-key", default="cnpj")
    parser.add_argument("--ceis-date-key", default="data_sancao")
    parser.add_argument("--qsa-company-key", default="empresa_cnpj")
    parser.add_argument("--qsa-partner-key", default="socio_cpf")
    parser.add_argument("--contracts-supplier-key", default="supplier_cnpj")
    parser.add_argument("--contracts-control-key", default="numero_controle_pncp")
    parser.add_argument("--contracts-date-key", default="data_publicacao_pncp")
    parser.add_argument("--output", required=True, help="Arquivo JSON de saída")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ceis_rows = load_rows(Path(args.ceis))
    qsa_rows = load_rows(Path(args.qsa))
    contract_rows = load_rows(Path(args.contracts))

    ceis_index = build_ceis_index(ceis_rows, args.ceis_cnpj_key, args.ceis_date_key)
    qsa_index = build_qsa_index(qsa_rows, args.qsa_company_key, args.qsa_partner_key)
    contract_index = build_contract_index(
        contract_rows,
        args.contracts_supplier_key,
        args.contracts_control_key,
        args.contracts_date_key,
    )

    candidates = detect_candidates(ceis_index, qsa_index, contract_index)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "meta": {
            "generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "candidates": len(candidates),
            "blocked_companies": len(ceis_index),
        },
        "candidates": candidates,
    }
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {output}")
    print(f"Candidates: {len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
