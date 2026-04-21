#!/usr/bin/env python3
"""
Fetch PNCP public contract records for a supplier CNPJ and generate a compact
aditivo-oriented report.

Data flow validated on 2026-04-08:
1. Public search: /api/search?tipos_documento=contrato&q=<cnpj>&pagina=N
2. Contract detail: /api/pncp/v1/orgaos/{orgao_cnpj}/contratos/{ano}/{sequencial}
3. Optional terms: /api/pncp/v1/orgaos/{orgao_cnpj}/contratos/{ano}/{sequencial}/termos

The search API is noisy: it returns documents matching the query, not only
supplier-side matches. This script fetches each contract detail and keeps only
records where detail.niFornecedor == supplier_cnpj.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path
from statistics import median

BASE_URL = "https://pncp.gov.br"
SEARCH_URL = f"{BASE_URL}/api/search"
DETAIL_URL = BASE_URL + "/api/pncp/v1/orgaos/{orgao_cnpj}/contratos/{ano}/{sequencial}"
TERMS_URL = (
    BASE_URL
    + "/api/pncp/v1/orgaos/{orgao_cnpj}/contratos/{ano}/{sequencial}/termos?pagina=1"
)
DEFAULT_OUTPUT_DIR = Path("outputs/reports/pncp-queries")
USER_AGENT = "metaxon-zelox-validator/0.1"


def only_digits(value: str) -> str:
    return re.sub(r"\D+", "", value or "")


def get_json(url: str) -> dict | list | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status == 204:
                return None
            body = resp.read()
            if not body:
                return None
            return json.loads(body)
    except urllib.error.HTTPError as exc:
        if exc.code == 204:
            return None
        raise


@dataclass
class ContractRecord:
    supplier_cnpj: str
    supplier_name: str
    orgao_cnpj: str
    orgao_nome: str
    numero_controle_pncp: str
    item_url: str
    ano_contrato: int
    sequencial_contrato: int
    numero_contrato: str
    tipo_contrato: str
    modalidade: str
    categoria_processo: str
    objeto_contrato: str
    data_assinatura: str | None
    data_inicio_vigencia: str | None
    data_fim_vigencia: str | None
    valor_inicial: float | None
    valor_global: float | None
    valor_acumulado: float | None
    aditivo_absoluto: float | None
    aditivo_ratio: float | None
    termos_count: int
    # Aditivo realizado via soma de valorAcrescido nos /termos (fonte mais confiável
    # para Serviços e Compras, onde valor_global pode refletir teto pré-autorizado).
    aditivo_termos_absoluto: float | None
    aditivo_termos_ratio: float | None
    query_group: str
    zscore_grupo: float | None = None


def fetch_search_page(query: str, page: int) -> dict:
    params = {
        "tipos_documento": "contrato",
        "q": query,
        "pagina": page,
    }
    url = f"{SEARCH_URL}?{urllib.parse.urlencode(params)}"
    payload = get_json(url)
    if not isinstance(payload, dict):
        raise RuntimeError(f"unexpected search payload for {url}")
    return payload


def fetch_contract_detail(item_url: str) -> dict:
    parts = item_url.strip("/").split("/")
    if len(parts) != 4 or parts[0] != "contratos":
        raise ValueError(f"unexpected item_url format: {item_url}")
    _, orgao_cnpj, ano, sequencial = parts
    url = DETAIL_URL.format(
        orgao_cnpj=orgao_cnpj,
        ano=ano,
        sequencial=sequencial,
    )
    payload = get_json(url)
    if not isinstance(payload, dict):
        raise RuntimeError(f"unexpected detail payload for {url}")
    return payload


def fetch_terms(item_url: str) -> tuple[int, float | None]:
    """Retorna (count, aditivo_realizado) via /termos.

    aditivo_realizado = soma de valorAcrescido dos termos do tipo 'Termo Aditivo'.
    Retorna None se o endpoint não expõe valorAcrescido (pseudo-schema ou 204).
    Termos de prorrogação, rescisão etc. têm valorAcrescido=0 ou None — incluídos
    na contagem mas não inflam o aditivo_realizado.
    """
    parts = item_url.strip("/").split("/")
    _, orgao_cnpj, ano, sequencial = parts
    url = TERMS_URL.format(
        orgao_cnpj=orgao_cnpj,
        ano=ano,
        sequencial=sequencial,
    )
    payload = get_json(url)
    if payload is None:
        return 0, None
    items: list[dict] = []
    if isinstance(payload, list):
        items = [t for t in payload if isinstance(t, dict)]
    elif isinstance(payload, dict):
        raw = payload.get("data") or payload.get("items") or payload.get("content")
        if isinstance(raw, list):
            items = [t for t in raw if isinstance(t, dict)]

    count = len(items)
    # valorAcrescido presente e numérico → podemos calcular aditivo realizado
    has_valor = any("valorAcrescido" in t for t in items)
    if not has_valor:
        return count, None

    soma = sum(
        (t.get("valorAcrescido") or 0.0)
        for t in items
        if t.get("tipoTermoContratoNome") == "Termo Aditivo"
    )
    return count, soma if soma != 0.0 else None


def fetch_terms_count(item_url: str) -> int:
    """Compat wrapper — retorna apenas o count."""
    count, _ = fetch_terms(item_url)
    return count


def to_float(value: object) -> float | None:
    if value in (None, ""):
        return None
    return float(value)


def contract_group(search_item: dict, detail: dict) -> str:
    parts = [
        search_item.get("modalidade_licitacao_nome") or "sem-modalidade",
        detail.get("categoriaProcesso", {}).get("nome") or "sem-categoria",
        detail.get("tipoContrato", {}).get("nome") or "sem-tipo",
    ]
    return " | ".join(parts)


def normalize_record(
    supplier_cnpj: str,
    search_item: dict,
    detail: dict,
    terms_count: int,
    aditivo_termos: float | None = None,
) -> ContractRecord:
    valor_inicial = to_float(detail.get("valorInicial"))
    valor_global = to_float(detail.get("valorGlobal"))
    valor_acumulado = to_float(detail.get("valorAcumulado"))
    aditivo_absoluto = None
    aditivo_ratio = None
    if valor_inicial not in (None, 0.0) and valor_global is not None:
        aditivo_absoluto = valor_global - valor_inicial
        aditivo_ratio = aditivo_absoluto / valor_inicial

    # Aditivo via /termos: mais confiável para Serviços/Compras onde valor_global
    # pode ser teto pré-autorizado. Para Obras, converge com aditivo_ratio.
    aditivo_termos_absoluto = aditivo_termos
    aditivo_termos_ratio = None
    if aditivo_termos is not None and valor_inicial not in (None, 0.0):
        aditivo_termos_ratio = aditivo_termos / valor_inicial  # type: ignore[operator]

    return ContractRecord(
        supplier_cnpj=supplier_cnpj,
        supplier_name=detail.get("nomeRazaoSocialFornecedor") or "",
        orgao_cnpj=detail.get("orgaoEntidade", {}).get("cnpj") or "",
        orgao_nome=detail.get("orgaoEntidade", {}).get("razaoSocial") or "",
        numero_controle_pncp=detail.get("numeroControlePNCP") or "",
        item_url=search_item.get("item_url") or "",
        ano_contrato=int(detail.get("anoContrato") or 0),
        sequencial_contrato=int(detail.get("sequencialContrato") or 0),
        numero_contrato=str(detail.get("numeroContratoEmpenho") or ""),
        tipo_contrato=detail.get("tipoContrato", {}).get("nome") or "",
        modalidade=search_item.get("modalidade_licitacao_nome") or "",
        categoria_processo=detail.get("categoriaProcesso", {}).get("nome") or "",
        objeto_contrato=detail.get("objetoContrato") or "",
        data_assinatura=detail.get("dataAssinatura"),
        data_inicio_vigencia=detail.get("dataVigenciaInicio"),
        data_fim_vigencia=detail.get("dataVigenciaFim"),
        valor_inicial=valor_inicial,
        valor_global=valor_global,
        valor_acumulado=valor_acumulado,
        aditivo_absoluto=aditivo_absoluto,
        aditivo_ratio=aditivo_ratio,
        aditivo_termos_absoluto=aditivo_termos_absoluto,
        aditivo_termos_ratio=aditivo_termos_ratio,
        termos_count=terms_count,
        query_group=contract_group(search_item, detail),
    )


# Empenhos acumulam pagamentos iterativos — não aditivos contratuais.
# Excluídos da distribuição de referência do z-score.
_ZSCORE_ELIGIBLE_TIPOS = frozenset({"Contrato (termo inicial)"})

# Todas as categorias são elegíveis quando temos aditivo_termos_ratio (via /termos).
# Sem termos, restringimos a categorias onde valor_global - valor_inicial é confiável:
# Obras e Serviços de Engenharia. Serviços e Compras usam valor_global como teto
# pré-autorizado — não como aditivo realizado — e ficam fora sem /termos.
_ZSCORE_CATEGORIAS_SEM_TERMOS = frozenset({"Obras", "Serviços de Engenharia"})


def _effective_ratio(record: ContractRecord) -> float | None:
    """Retorna o ratio de aditivo mais confiável disponível.

    Prioridade:
    1. aditivo_termos_ratio — soma de valorAcrescido dos /termos (campo direto da API)
    2. aditivo_ratio — valor_global - valor_inicial (confiável só para Obras/Eng.)
    """
    if record.aditivo_termos_ratio is not None and record.aditivo_termos_ratio > 0:
        return record.aditivo_termos_ratio
    if (
        record.categoria_processo in _ZSCORE_CATEGORIAS_SEM_TERMOS
        and record.aditivo_ratio is not None
        and record.aditivo_ratio > 0
    ):
        return record.aditivo_ratio
    return None


def _is_zscore_eligible(record: ContractRecord) -> bool:
    """True se o contrato deve entrar na distribuição de referência do z-score."""
    return (
        record.tipo_contrato in _ZSCORE_ELIGIBLE_TIPOS
        and _effective_ratio(record) is not None
    )


def enrich_zscores(records: list[ContractRecord]) -> None:
    # Usa o ratio mais confiável disponível para cada contrato.
    by_group: dict[str, list[float]] = {}
    for record in records:
        ratio = _effective_ratio(record)
        if ratio is None or record.tipo_contrato not in _ZSCORE_ELIGIBLE_TIPOS:
            continue
        by_group.setdefault(record.query_group, []).append(ratio)

    stats_map: dict[str, tuple[float, float]] = {}
    for group, values in by_group.items():
        if len(values) < 2:
            continue
        mean = sum(values) / len(values)
        variance = sum((v - mean) ** 2 for v in values) / len(values)
        stddev = math.sqrt(variance)
        stats_map[group] = (mean, stddev)

    for record in records:
        ratio = _effective_ratio(record)
        if ratio is None or record.tipo_contrato not in _ZSCORE_ELIGIBLE_TIPOS:
            continue
        mean_std = stats_map.get(record.query_group)
        if not mean_std:
            continue
        mean, stddev = mean_std
        if stddev == 0:
            record.zscore_grupo = 0.0
        else:
            record.zscore_grupo = (ratio - mean) / stddev


def collect_supplier_contracts(
    supplier_cnpj: str,
    max_pages: int,
    sleep_ms: int,
) -> tuple[list[ContractRecord], dict]:
    search_hits = 0
    kept = 0
    pages = 0
    records: list[ContractRecord] = []
    seen_controls: set[str] = set()

    for page in range(1, max_pages + 1):
        payload = fetch_search_page(supplier_cnpj, page)
        pages += 1
        items = payload.get("items") or []
        if not items:
            break

        for item in items:
            search_hits += 1
            detail = fetch_contract_detail(item["item_url"])
            if only_digits(detail.get("niFornecedor") or "") != supplier_cnpj:
                continue
            control = detail.get("numeroControlePNCP") or item.get(
                "numero_controle_pncp"
            )
            if control in seen_controls:
                continue
            seen_controls.add(control)
            terms_count, aditivo_termos = fetch_terms(item["item_url"])
            records.append(
                normalize_record(
                    supplier_cnpj, item, detail, terms_count, aditivo_termos
                )
            )
            kept += 1
            if sleep_ms:
                time.sleep(sleep_ms / 1000)

        if len(items) < 10:
            break

    enrich_zscores(records)
    meta = {
        "supplier_cnpj": supplier_cnpj,
        "search_hits": search_hits,
        "kept_contracts": kept,
        "pages_fetched": pages,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "search_api": SEARCH_URL,
        "detail_endpoint_pattern": DETAIL_URL,
        "terms_endpoint_pattern": TERMS_URL,
    }
    return records, meta


def pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:.2f}%"


def brl(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def summarize(records: list[ContractRecord]) -> dict:
    with_ratio = [r for r in records if r.aditivo_ratio is not None]
    flagged_20 = [r for r in with_ratio if (r.aditivo_ratio or 0) >= 0.20]
    flagged_23 = [r for r in with_ratio if (r.aditivo_ratio or 0) >= 0.23]
    flagged_25 = [r for r in with_ratio if (r.aditivo_ratio or 0) >= 0.25]

    ratios = [r.aditivo_ratio for r in with_ratio if r.aditivo_ratio is not None]
    top = sorted(
        with_ratio,
        key=lambda r: (r.aditivo_ratio or float("-inf"), r.valor_global or 0),
        reverse=True,
    )[:10]
    return {
        "contracts_with_ratio": len(with_ratio),
        "flagged_20": len(flagged_20),
        "flagged_23": len(flagged_23),
        "flagged_25": len(flagged_25),
        "median_ratio": median(ratios) if ratios else None,
        "max_ratio": max(ratios) if ratios else None,
        "top_contracts": top,
    }


def markdown_report(meta: dict, records: list[ContractRecord]) -> str:
    summary = summarize(records)
    supplier_name = records[0].supplier_name if records else ""
    lines = [
        f"# PNCP Supplier Contract Scan — {meta['supplier_cnpj']}",
        "",
        f"- Fornecedor: {supplier_name or 'não resolvido'}",
        f"- CNPJ: `{meta['supplier_cnpj']}`",
        f"- Gerado em: {meta['generated_at']}",
        f"- Hits brutos no search: {meta['search_hits']}",
        f"- Contratos mantidos após filtro por `niFornecedor`: {meta['kept_contracts']}",
        f"- Páginas consultadas: {meta['pages_fetched']}",
        "",
        "## Resumo",
        "",
        f"- Contratos com `valorInicial` e `valorGlobal` comparáveis: {summary['contracts_with_ratio']}",
        f"- `aditivo_ratio >= 20%`: {summary['flagged_20']}",
        f"- `aditivo_ratio >= 23%`: {summary['flagged_23']}",
        f"- `aditivo_ratio >= 25%`: {summary['flagged_25']}",
        f"- Mediana do `aditivo_ratio`: {pct(summary['median_ratio'])}",
        f"- Máximo `aditivo_ratio`: {pct(summary['max_ratio'])}",
        "",
        "## Método",
        "",
        "- Busca inicial: `GET /api/search?tipos_documento=contrato&q=<cnpj>&pagina=N`",
        "- Resolução do detalhe por contrato: `GET /api/pncp/v1/orgaos/{orgao_cnpj}/contratos/{ano}/{sequencial}`",
        "- Filtro de precisão: mantém apenas contratos onde `detail.niFornecedor == supplier_cnpj`",
        "- Sinal principal: `aditivo_ratio = (valorGlobal - valorInicial) / valorInicial`",
        "- Sinal termos: `aditivo_termos_ratio = Σ valorAcrescido (Termo Aditivo) / valorInicial` — fonte mais confiável para Serviços/Compras",
        "- Sinal contextualizado: `zscore_grupo` usa `aditivo_termos_ratio` quando disponível, fallback para `aditivo_ratio` (Obras/Eng.)",
        "- Agrupamento z-score: `modalidade | categoria_processo | tipo_contrato`",
        "",
        "## Top contratos por aditivo",
        "",
        "| Controle PNCP | Objeto | Modalidade | Inicial | Global | Ratio (global) | Ratio (termos) | Z-score | Termos |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for record in summary["top_contracts"]:
        objeto = record.objeto_contrato.replace("\n", " ").strip()[:80]
        zscore = "n/a" if record.zscore_grupo is None else f"{record.zscore_grupo:.2f}"
        ratio_t = (
            pct(record.aditivo_termos_ratio)
            if record.aditivo_termos_ratio is not None
            else "—"
        )
        lines.append(
            "| {control} | {objeto} | {modalidade} | {inicial} | {global_} | {ratio} | {ratio_t} | {zscore} | {termos} |".format(
                control=record.numero_controle_pncp,
                objeto=objeto or "-",
                modalidade=record.modalidade or "-",
                inicial=brl(record.valor_inicial),
                global_=brl(record.valor_global),
                ratio=pct(record.aditivo_ratio),
                ratio_t=ratio_t,
                zscore=zscore,
                termos=record.termos_count,
            )
        )

    lines.extend(
        [
            "",
            "## Limitações",
            "",
            "- O `api/search` é textual e pode perder contratos se o fornecedor não aparecer indexado de forma consistente.",
            "- `termos_count = 0` não prova ausência de aditivo; em vários casos o próprio registro já representa um termo publicado.",
            "- `aditivo_termos_ratio` depende de valorAcrescido preenchido pelo órgão — campos None são tratados como 0.",
            "- O agrupamento do `zscore_grupo` é operacional, não jurídico. Serve para triagem, não para laudo final.",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supplier-cnpj", required=True, help="CNPJ do fornecedor")
    parser.add_argument(
        "--max-pages", type=int, default=5, help="Páginas do search a varrer"
    )
    parser.add_argument(
        "--sleep-ms",
        type=int,
        default=0,
        help="Delay entre requests de detalhe/termos",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Diretório para outputs json/md",
    )
    parser.add_argument(
        "--slug",
        default="supplier-scan",
        help="Prefixo de arquivo para os relatórios",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    supplier_cnpj = only_digits(args.supplier_cnpj)
    if len(supplier_cnpj) != 14:
        print("supplier-cnpj deve ter 14 dígitos", file=sys.stderr)
        return 2

    records, meta = collect_supplier_contracts(
        supplier_cnpj=supplier_cnpj,
        max_pages=args.max_pages,
        sleep_ms=args.sleep_ms,
    )
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    stem = f"{args.slug}-{supplier_cnpj}"
    json_path = output_dir / f"{stem}.json"
    md_path = output_dir / f"{stem}.md"
    payload = {"meta": meta, "records": [asdict(record) for record in records]}
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(markdown_report(meta, records), encoding="utf-8")

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Contracts kept: {len(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
