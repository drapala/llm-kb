"""
Phoenix Feature v1 Candidates — Falsification Test
Tests 4 new hypotheses against genuine (created_post_sanction=1, n~30)
vs preexisting (created_post_sanction=0, n~1241) with post-sanction contracts.

Features:
1. company_name_similarity   — Jaccard token overlap (phoenix name vs mother names)
2. cnae_overlap_with_mother  — phoenix shares CNAE principal with debarred mother
3. multi_sister_sanction_burst — sanctions in CPF cluster within 180-day window
4. first_contract_to_second_organ_days — days to diversify to 2nd distinct organ
"""

import sqlite3
import json
import argparse
import re
from datetime import datetime, timedelta
from statistics import median, mean

DB_DEFAULT = "/Users/drapala/projects/bid-engine/bid_engine.db"
JSON_DEFAULT = "/Users/drapala/projects/llm-kb/outputs/reports/pncp-queries/phoenix-feature-v1-candidates.json"
MD_DEFAULT = "/Users/drapala/projects/llm-kb/outputs/reports/pncp-queries/phoenix-feature-v1-candidates.md"


def tokenize(name: str) -> set:
    """Lowercase word tokens, strip common suffixes."""
    if not name:
        return set()
    name = name.upper()
    # Remove legal suffixes
    for suffix in [
        "LTDA",
        "S/A",
        "SA",
        "EIRELI",
        "ME",
        "EPP",
        "COMERCIO",
        "COMERCIAL",
        "SERVICOS",
        "INDUSTRIA",
        "E",
        "DE",
        "DA",
        "DO",
    ]:
        name = re.sub(rf"\b{suffix}\b", "", name)
    tokens = set(t for t in re.split(r"\W+", name) if len(t) >= 3)
    return tokens


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def parse_date(s):
    if not s:
        return None
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d")
    except Exception:
        return None


def build_universe(con):
    """
    Returns list of dicts: {phoenix_cnpj, debarred_cnpj, data_sancao, created_post_sanction}
    Same definition as phoenix_feature_falsification.py.
    """
    rows = con.execute("""
        SELECT DISTINCT
            ss2.cnpj        AS phoenix_cnpj,
            cs.cpf_cnpj_norm AS debarred_cnpj,
            cs.data_inicio  AS data_sancao
        FROM supplier_socios ss1
        JOIN ceis_sanctions cs
            ON ss1.cnpj = cs.cpf_cnpj_norm
        JOIN supplier_socios ss2
            ON ss2.cnpj_cpf = ss1.cnpj_cpf
           AND ss2.cnpj != ss1.cnpj
        JOIN contracts_enriched ce
            ON ce.supplier_cnpj = ss2.cnpj
           AND ce.data_assinatura > cs.data_inicio
        WHERE ss1.cnpj_cpf IS NOT NULL
    """).fetchall()

    universe = []
    seen = set()
    for r in rows:
        key = (r["phoenix_cnpj"], r["debarred_cnpj"])
        if key in seen:
            continue
        seen.add(key)

        rfb = con.execute(
            "SELECT data_inicio_atividade FROM suppliers_rfb WHERE cnpj = ?",
            (r["phoenix_cnpj"],),
        ).fetchone()
        data_inicio = rfb["data_inicio_atividade"] if rfb else None
        data_sancao = r["data_sancao"]

        created_post = 0
        if data_inicio and data_sancao:
            created_post = 1 if data_inicio > data_sancao else 0

        universe.append(
            {
                "phoenix_cnpj": r["phoenix_cnpj"],
                "debarred_cnpj": r["debarred_cnpj"],
                "data_sancao": data_sancao,
                "created_post_sanction": created_post,
            }
        )

    return universe


def feature_name_similarity(con, universe):
    """Jaccard token overlap between phoenix name and all debarred-company names in its cluster."""
    results = {}
    for row in universe:
        pcnpj = row["phoenix_cnpj"]
        if pcnpj in results:
            continue

        # Phoenix name
        rfb_p = con.execute(
            "SELECT nome_empresarial FROM suppliers_rfb WHERE cnpj = ?", (pcnpj,)
        ).fetchone()
        p_name = rfb_p["nome_empresarial"] if rfb_p else ""
        p_tokens = tokenize(p_name)

        # All debarred CNPJs in cluster (same CPF network)
        cpfs = [
            r["cnpj_cpf"]
            for r in con.execute(
                "SELECT cnpj_cpf FROM supplier_socios WHERE cnpj = ? AND cnpj_cpf IS NOT NULL",
                (pcnpj,),
            ).fetchall()
        ]

        if not cpfs:
            results[pcnpj] = 0.0
            continue

        ph = ",".join("?" * len(cpfs))
        debarred_cnpjs = [
            r["cnpj"]
            for r in con.execute(
                f"SELECT DISTINCT cnpj FROM supplier_socios WHERE cnpj_cpf IN ({ph}) AND cnpj != ?",
                (*cpfs, pcnpj),
            ).fetchall()
        ]

        max_sim = 0.0
        for dcnpj in debarred_cnpjs:
            rfb_d = con.execute(
                "SELECT nome_empresarial FROM suppliers_rfb WHERE cnpj = ?", (dcnpj,)
            ).fetchone()
            if rfb_d and rfb_d["nome_empresarial"]:
                sim = jaccard(p_tokens, tokenize(rfb_d["nome_empresarial"]))
                if sim > max_sim:
                    max_sim = sim

        results[pcnpj] = max_sim

    return results


def feature_cnae_overlap(con, universe):
    """1 if phoenix shares CNAE principal with any debarred company in cluster, else 0."""
    results = {}
    for row in universe:
        pcnpj = row["phoenix_cnpj"]
        if pcnpj in results:
            continue

        rfb_p = con.execute(
            "SELECT cnae_fiscal_principal FROM suppliers_rfb WHERE cnpj = ?", (pcnpj,)
        ).fetchone()
        p_cnae = rfb_p["cnae_fiscal_principal"] if rfb_p else None

        if not p_cnae:
            results[pcnpj] = 0
            continue

        cpfs = [
            r["cnpj_cpf"]
            for r in con.execute(
                "SELECT cnpj_cpf FROM supplier_socios WHERE cnpj = ? AND cnpj_cpf IS NOT NULL",
                (pcnpj,),
            ).fetchall()
        ]

        if not cpfs:
            results[pcnpj] = 0
            continue

        ph = ",".join("?" * len(cpfs))
        debarred_cnpjs = [
            r["cnpj"]
            for r in con.execute(
                f"SELECT DISTINCT cnpj FROM supplier_socios WHERE cnpj_cpf IN ({ph}) AND cnpj != ?",
                (*cpfs, pcnpj),
            ).fetchall()
        ]

        # Check CEIS membership and CNAE
        overlap = 0
        for dcnpj in debarred_cnpjs:
            in_ceis = con.execute(
                "SELECT 1 FROM ceis_sanctions WHERE cpf_cnpj_norm = ? LIMIT 1", (dcnpj,)
            ).fetchone()
            if not in_ceis:
                continue
            rfb_d = con.execute(
                "SELECT cnae_fiscal_principal FROM suppliers_rfb WHERE cnpj = ?",
                (dcnpj,),
            ).fetchone()
            if rfb_d and rfb_d["cnae_fiscal_principal"]:
                # 4-digit CNAE group match (divisão)
                p4 = str(p_cnae)[:4]
                d4 = str(rfb_d["cnae_fiscal_principal"])[:4]
                if p4 == d4:
                    overlap = 1
                    break

        results[pcnpj] = overlap

    return results


def feature_sanction_burst(con, universe):
    """Number of distinct CEIS sanctions across CPF cluster within any 180-day window."""
    results = {}
    for row in universe:
        pcnpj = row["phoenix_cnpj"]
        if pcnpj in results:
            continue

        cpfs = [
            r["cnpj_cpf"]
            for r in con.execute(
                "SELECT cnpj_cpf FROM supplier_socios WHERE cnpj = ? AND cnpj_cpf IS NOT NULL",
                (pcnpj,),
            ).fetchall()
        ]

        if not cpfs:
            results[pcnpj] = 0
            continue

        ph = ",".join("?" * len(cpfs))
        all_cnpjs_in_cluster = [
            r["cnpj"]
            for r in con.execute(
                f"SELECT DISTINCT cnpj FROM supplier_socios WHERE cnpj_cpf IN ({ph})",
                tuple(cpfs),
            ).fetchall()
        ]

        if not all_cnpjs_in_cluster:
            results[pcnpj] = 0
            continue

        ph2 = ",".join("?" * len(all_cnpjs_in_cluster))
        sanctions = con.execute(
            f"SELECT data_inicio FROM ceis_sanctions WHERE cpf_cnpj_norm IN ({ph2}) AND data_inicio IS NOT NULL",
            tuple(all_cnpjs_in_cluster),
        ).fetchall()

        dates = sorted(
            [
                parse_date(r["data_inicio"])
                for r in sanctions
                if parse_date(r["data_inicio"])
            ]
        )

        if not dates:
            results[pcnpj] = 0
            continue

        # Sliding window: max sanctions in any 180-day span
        max_burst = 0
        window = timedelta(days=180)
        for i, d in enumerate(dates):
            count = sum(1 for dd in dates if d <= dd <= d + window)
            if count > max_burst:
                max_burst = count

        results[pcnpj] = max_burst

    return results


def feature_organ_diversification(con, universe):
    """Days from first post-sanction contract to contract with second distinct organ.
    None if only 1 organ ever used."""
    results = {}
    for row in universe:
        pcnpj = row["phoenix_cnpj"]
        data_sancao = row["data_sancao"]
        if pcnpj in results:
            continue

        contracts = con.execute(
            """
            SELECT organ_cnpj, data_assinatura
            FROM contracts_enriched
            WHERE supplier_cnpj = ? AND data_assinatura > ?
            ORDER BY data_assinatura
        """,
            (pcnpj, data_sancao or "1900-01-01"),
        ).fetchall()

        if not contracts:
            results[pcnpj] = None
            continue

        first_date = parse_date(contracts[0]["data_assinatura"])
        first_organ = contracts[0]["organ_cnpj"]

        second_organ_date = None
        for c in contracts[1:]:
            if c["organ_cnpj"] != first_organ:
                second_organ_date = parse_date(c["data_assinatura"])
                break

        if second_organ_date is None or first_date is None:
            results[pcnpj] = None
        else:
            results[pcnpj] = (second_organ_date - first_date).days

    return results


def compare_groups(
    genuine_vals, preexisting_vals, feature_name, higher_is_riskier=True
):
    """Compare two lists, return summary dict."""
    g = [v for v in genuine_vals if v is not None]
    p = [v for v in preexisting_vals if v is not None]

    if not g or not p:
        return {
            "feature": feature_name,
            "support": "inconclusive",
            "note": "insufficient data",
        }

    g_med = median(g)
    p_med = median(p)
    g_mean = mean(g)
    p_mean = mean(p)

    if higher_is_riskier:
        direction_ok = g_med >= p_med
    else:
        direction_ok = g_med <= p_med

    gap = abs(g_med - p_med)
    gap_pct = (gap / max(abs(p_med), 1e-9)) * 100

    if direction_ok and gap_pct >= 20:
        support = "supported"
    elif direction_ok and gap_pct >= 5:
        support = "weak"
    elif not direction_ok:
        support = "refuted"
    else:
        support = "weak"

    return {
        "feature": feature_name,
        "support": support,
        "genuine_median": round(g_med, 4),
        "preexisting_median": round(p_med, 4),
        "genuine_mean": round(g_mean, 4),
        "preexisting_mean": round(p_mean, 4),
        "gap_pct": round(gap_pct, 1),
        "n_genuine": len(g),
        "n_preexisting": len(p),
        "direction_as_predicted": direction_ok,
    }


def compare_binary(genuine_vals, preexisting_vals, feature_name):
    g = [v for v in genuine_vals if v is not None]
    p = [v for v in preexisting_vals if v is not None]
    g_rate = sum(g) / len(g) if g else 0
    p_rate = sum(p) / len(p) if p else 0

    direction_ok = g_rate >= p_rate
    gap_pct = abs(g_rate - p_rate) * 100

    if direction_ok and gap_pct >= 10:
        support = "supported"
    elif direction_ok and gap_pct >= 3:
        support = "weak"
    elif not direction_ok:
        support = "refuted"
    else:
        support = "weak"

    return {
        "feature": feature_name,
        "support": support,
        "genuine_rate": round(g_rate, 4),
        "preexisting_rate": round(p_rate, 4),
        "gap_pct": round(gap_pct, 1),
        "n_genuine": len(g),
        "n_preexisting": len(p),
        "direction_as_predicted": direction_ok,
    }


def main(db_path, json_out, md_out):
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row

    print("Building universe...")
    universe = build_universe(con)
    genuine = [r for r in universe if r["created_post_sanction"] == 1]
    preexisting = [r for r in universe if r["created_post_sanction"] == 0]
    print(f"  Genuine: {len(genuine)}, Preexisting: {len(preexisting)}")

    print("Computing name_similarity...")
    name_sim = feature_name_similarity(con, universe)

    print("Computing cnae_overlap...")
    cnae_ov = feature_cnae_overlap(con, universe)

    print("Computing sanction_burst...")
    burst = feature_sanction_burst(con, universe)

    print("Computing organ_diversification...")
    organ_div = feature_organ_diversification(con, universe)

    # Collect values per group
    def vals(group, feat_dict):
        return [feat_dict.get(r["phoenix_cnpj"]) for r in group]

    results = []

    r1 = compare_groups(
        vals(genuine, name_sim),
        vals(preexisting, name_sim),
        "company_name_similarity",
        higher_is_riskier=True,
    )
    results.append(r1)

    r2 = compare_binary(
        vals(genuine, cnae_ov), vals(preexisting, cnae_ov), "cnae_overlap_with_mother"
    )
    results.append(r2)

    r3 = compare_groups(
        vals(genuine, burst),
        vals(preexisting, burst),
        "multi_sister_sanction_burst",
        higher_is_riskier=True,
    )
    results.append(r3)

    r4 = compare_groups(
        vals(genuine, organ_div),
        vals(preexisting, organ_div),
        "first_contract_to_second_organ_days",
        higher_is_riskier=False,
    )
    results.append(r4)

    # Spot-check: print per-genuine values for manual inspection
    print("\nPer-genuine spot check:")
    for r in genuine:
        p = r["phoenix_cnpj"]
        print(
            f"  {p} | name_sim={name_sim.get(p, '?'):.3f} "
            f"| cnae={cnae_ov.get(p, '?')} "
            f"| burst={burst.get(p, '?')} "
            f"| div_days={organ_div.get(p, '?')}"
        )

    con.close()

    # Write JSON
    with open(json_out, "w") as f:
        json.dump({"results": results}, f, indent=2, ensure_ascii=False)
    print(f"\nJSON: {json_out}")

    # Write Markdown
    with open(md_out, "w") as f:
        f.write("# Phoenix Feature v1 Candidates — Falsification Report\n\n")
        f.write(
            "Base: `bid_engine.db`. Controle: genuine (`created_post_sanction=1`) vs preexisting.\n\n"
        )
        f.write("## Resultados\n\n")
        f.write(
            "| Feature | Support | Genuine | Preexisting | Gap% | N genuine | N preexisting |\n"
        )
        f.write("|---|---|---|---|---|---|---|\n")
        for r in results:
            if "genuine_rate" in r:
                g_val = f"{r['genuine_rate'] * 100:.1f}%"
                p_val = f"{r['preexisting_rate'] * 100:.1f}%"
            else:
                g_val = str(r.get("genuine_median", "?"))
                p_val = str(r.get("preexisting_median", "?"))
            f.write(
                f"| `{r['feature']}` | **{r['support']}** | {g_val} | {p_val} | {r.get('gap_pct', '?')}% | {r.get('n_genuine', '?')} | {r.get('n_preexisting', '?')} |\n"
            )

        f.write("\n## Hipóteses\n\n")
        hypotheses = {
            "company_name_similarity": "Phoenix com nome similar à empresa-mãe (brazenness) têm maior Jaccard mediano que preexistentes.",
            "cnae_overlap_with_mother": "Phoenix que operam no mesmo setor da mãe (CNAE 4 dígitos) têm taxa de overlap maior em genuine vs preexisting.",
            "multi_sister_sanction_burst": "Genuine phoenix emergem de clusters CPF que acumulam mais sanções em janela de 180 dias.",
            "first_contract_to_second_organ_days": "Genuine phoenix diversificam para segundo órgão mais rapidamente (days menor = stealth mais ativo).",
        }
        for r in results:
            f.write(
                f"- **`{r['feature']}`** (`{r['support']}`): {hypotheses.get(r['feature'], '')}\n"
            )
            if "genuine_median" in r:
                f.write(
                    f"  - Mediana: genuine={r['genuine_median']} vs preexisting={r['preexisting_median']} (gap {r['gap_pct']}%)\n"
                )
            else:
                f.write(
                    f"  - Taxa: genuine={r.get('genuine_rate', '?') * 100:.1f}% vs preexisting={r.get('preexisting_rate', '?') * 100:.1f}% (gap {r['gap_pct']}%)\n"
                )

    print(f"MD: {md_out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=DB_DEFAULT)
    parser.add_argument("--json-output", default=JSON_DEFAULT)
    parser.add_argument("--md-output", default=MD_DEFAULT)
    args = parser.parse_args()
    main(args.db, args.json_output, args.md_output)
