#!/usr/bin/env python3
"""
build-claim-indexes.py — Gera claim indexes para todos os artigos promovidos.

Lê cada artigo em wiki/concepts/, extrai claims da seção ## Conteúdo e
## Interpretação, e salva em outputs/index/promoted-claims/{slug}.yaml.

Uso:
    python scripts/build-claim-indexes.py                  # todos sem index
    python scripts/build-claim-indexes.py --all            # força regeneração
    python scripts/build-claim-indexes.py --slug <slug>    # artigo específico
    python scripts/build-claim-indexes.py --dry-run        # mostra sem salvar
"""

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
HEALTH_FILE = REPO_ROOT / "outputs/state/article-health.yaml"
CLAIMS_DIR = REPO_ROOT / "outputs/index/promoted-claims"
WIKI_DIR = REPO_ROOT / "wiki/concepts"

# Load .env (same pattern as cross-model-challenge.py)
_env_file = REPO_ROOT / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))

EXTRACT_PROMPT = """\
Você é um extrator de claims epistêmicos de artigos de knowledge base.

Dado o artigo abaixo, extraia as claims principais como uma lista YAML.

Regras:
- Cada claim deve ser 1 frase que pode ser verdadeira ou falsa (não processo, não instrução)
- Claims de ## Conteúdo têm support_level igual ao source_quality do artigo
- Claims de ## Interpretação têm support_level "low" e tag "interpretação"
- Inclua números/dados específicos na claim se disponíveis
- Máximo 12 claims por artigo (priorize as mais falsificáveis)
- Tags devem ser palavras-chave do domínio (2-5 por claim)
- Sources: lista de caminhos raw/ citados na frase (ou wiki/ para sínteses)

Responda APENAS com YAML válido neste formato (sem markdown fences, sem texto extra):

claims:
  - claim_id: c001
    text: "..."
    support_level: high|medium|low
    sources: [raw/papers/..., ...]
    tags: [tag1, tag2]

ARTIGO:
{article_content}
"""


def load_health() -> dict:
    with open(HEALTH_FILE) as f:
        return yaml.safe_load(f)


def load_article(slug: str) -> str | None:
    path = WIKI_DIR / f"{slug}.md"
    if not path.exists():
        return None
    return path.read_text()


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown."""
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def extract_claims(
    slug: str, content: str, topics: list[str], dry_run: bool
) -> dict | None:
    """Call OpenAI to extract claims from article content."""
    try:
        import openai
    except ImportError:
        print(" ERRO: openai não instalado. Run: uv pip install openai")
        return None

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(" ERRO: OPENAI_API_KEY não definida")
        return None

    client = openai.OpenAI(api_key=api_key)

    # Strip frontmatter for the prompt
    body = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)

    print("  → Extraindo claims via API...", end="", flush=True)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": EXTRACT_PROMPT.format(article_content=body[:6000]),
                }
            ],
        )
        raw = response.choices[0].message.content.strip()
    except Exception as e:
        print(f" ERRO: {e}")
        return None

    # Parse YAML response
    try:
        parsed = yaml.safe_load(raw)
        if not isinstance(parsed, dict) or "claims" not in parsed:
            print(" ERRO: resposta inesperada do modelo")
            return None
    except yaml.YAMLError as e:
        print(f" ERRO YAML: {e}")
        print(f"  Raw: {raw[:200]}")
        return None

    fm = parse_frontmatter(content)
    promoted_at = fm.get("updated", str(date.today()))

    result = {
        "article_slug": slug,
        "promoted_at": str(promoted_at),
        "topics": topics,
        "claims": parsed["claims"],
    }

    print(f" {len(parsed['claims'])} claims extraídas")
    return result


def save_index(slug: str, data: dict) -> None:
    out_path = CLAIMS_DIR / f"{slug}.yaml"
    # Build YAML manually to preserve comment-friendly format
    lines = [
        f"article_slug: {data['article_slug']}",
        f"promoted_at: {data['promoted_at']}",
        f"topics: {yaml.dump(data['topics'], default_flow_style=True).strip()}",
        "",
        "claims:",
    ]
    for claim in data["claims"]:
        lines.append(f"  - claim_id: {claim.get('claim_id', 'c???')}")
        lines.append(
            f"    text: {yaml.dump(claim.get('text', ''), default_style='"').strip()}"
        )
        lines.append(f"    support_level: {claim.get('support_level', 'medium')}")
        sources = claim.get("sources", [])
        lines.append(
            f"    sources: {yaml.dump(sources, default_flow_style=True).strip()}"
        )
        tags = claim.get("tags", [])
        lines.append(f"    tags: {yaml.dump(tags, default_flow_style=True).strip()}")
        if "note" in claim:
            lines.append(
                f"    note: {yaml.dump(claim['note'], default_style='"').strip()}"
            )
        lines.append("")

    out_path.write_text("\n".join(lines))
    print(f"  → Salvo: {out_path.relative_to(REPO_ROOT)}")


def main():
    parser = argparse.ArgumentParser(
        description="Gera claim indexes para artigos promovidos"
    )
    parser.add_argument(
        "--all", action="store_true", help="Regenera todos (inclusive existentes)"
    )
    parser.add_argument("--slug", help="Processa apenas este slug")
    parser.add_argument("--dry-run", action="store_true", help="Mostra sem salvar")
    args = parser.parse_args()

    health = load_health()
    articles = health.get("articles", [])

    # Filter target articles
    if args.slug:
        articles = [a for a in articles if a["article_slug"] == args.slug]
        if not articles:
            print(f"Slug não encontrado: {args.slug}")
            sys.exit(1)

    existing = {p.stem for p in CLAIMS_DIR.glob("*.yaml") if p.stem != "_schema"}

    processed = 0
    skipped = 0
    errors = 0

    for article in articles:
        slug = article["article_slug"]
        topics = article.get("topics", [])

        if not args.all and slug in existing:
            skipped += 1
            continue

        print(f"\n[{slug}]")
        content = load_article(slug)
        if content is None:
            print(f"  WARN: arquivo não encontrado — wiki/concepts/{slug}.md")
            errors += 1
            continue

        data = extract_claims(slug, content, topics, args.dry_run)
        if data is None:
            errors += 1
            continue

        if not args.dry_run:
            save_index(slug, data)
        else:
            print(f"  DRY RUN — {len(data['claims'])} claims (não salvo)")

        processed += 1

    print(f"\n{'=' * 50}")
    print(
        f"Processados: {processed} | Pulados (já existem): {skipped} | Erros: {errors}"
    )
    if args.dry_run and processed > 0:
        print("(dry-run: nenhum arquivo foi salvo)")


if __name__ == "__main__":
    main()
