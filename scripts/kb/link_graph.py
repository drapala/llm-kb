#!/usr/bin/env python3
"""
Build a queryable link graph from wiki article wikilinks and typed connections.

Outputs:
  outputs/state/link-graph.json — full graph with untyped and typed edges

Also patches article-health.yaml: updates depends_on[] for each promoted article
  with auto-discovered wiki/ links (raw/ deps stay as-is, only wiki/ entries
  are replaced; promoted articles that aren't in article-health.yaml are skipped).

Usage:
  python scripts/kb/link_graph.py           # build + patch article-health.yaml
  python scripts/kb/link_graph.py --dry-run # show changes without writing
  python scripts/kb/link_graph.py --graph-only  # build graph, skip health patch
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent.parent
WIKI_DIR = ROOT / "wiki" / "concepts"
GRAPH_OUT = ROOT / "outputs" / "state" / "link-graph.json"
HEALTH_PATH = ROOT / "outputs" / "state" / "article-health.yaml"

# Regex: [[slug]] or [[slug|label]]
RE_WIKILINK = re.compile(r"\[\[([^\]|#]+?)(?:\|[^\]]+)?\]\]")

# Typed connection line: "- TYPE: [[slug]] ON ..." or "- TYPE: [[slug]] —..."
# TYPE is one of the known relation labels used in ## Conexões sections
KNOWN_RELATIONS = {
    "derivedFrom",
    "complementsAt",
    "relaciona",
    "extends",
    "challenges",
    "instanciates",
    "analogTo",
    "contradicts",
    "supports",
    "isPartOf",
    "refines",
}

RE_TYPED_CONN = re.compile(
    r"[-*]\s+(" + "|".join(re.escape(r) for r in KNOWN_RELATIONS) + r")"
    r"(?:At|):\s+\[\[([^\]|#]+?)(?:\|[^\]]+)?\]\]"
    r"(?:\s+ON\s+[\"'](.+?)[\"'])?",
    re.IGNORECASE,
)

# Plain list link in Conexões: "- [[slug]] — ..."
RE_PLAIN_CONN = re.compile(r"[-*]\s+\[\[([^\]|#]+?)(?:\|[^\]]+)?\]\]")


def slug_from_path(path: Path) -> str:
    return path.stem


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, parts[2].strip()


def extract_conexoes_section(body: str) -> str:
    """Return the body of the ## Conexões section, or empty string."""
    m = re.search(r"##\s+Conex[oõ]es\s*\n(.*?)(?=\n##|\Z)", body, re.S | re.I)
    return m.group(1) if m else ""


def parse_article(path: Path) -> dict:
    """
    Returns:
    {
      slug: str,
      title: str,
      topics: list[str],
      provenance: str,
      quarantine: bool,
      promoted: bool,
      raw_deps: list[str],          # raw/ paths from sources frontmatter
      links: list[str],             # all [[slug]] refs in body (untyped)
      typed_links: list[dict],      # [{target, relation, label}] from Conexões
    }
    """
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    slug = slug_from_path(path)

    # raw/ deps from sources frontmatter
    raw_deps = []
    for src in fm.get("sources", []):
        p = src.get("path", "") if isinstance(src, dict) else str(src)
        if p.startswith("raw/"):
            raw_deps.append(p)

    # all wikilinks in body (untyped)
    links = list({m.group(1).strip() for m in RE_WIKILINK.finditer(body)})

    # typed connections from ## Conexões section
    conexoes_text = extract_conexoes_section(body)
    typed_links = []
    seen_typed = set()
    for m in RE_TYPED_CONN.finditer(conexoes_text):
        relation = m.group(1).lower()
        target = m.group(2).strip()
        label = m.group(3) or ""
        key = (relation, target)
        if key not in seen_typed:
            seen_typed.add(key)
            typed_links.append({"target": target, "relation": relation, "label": label})

    # plain [[slug]] in Conexões not already captured as typed
    typed_targets = {tl["target"] for tl in typed_links}
    for m in RE_PLAIN_CONN.finditer(conexoes_text):
        target = m.group(1).strip()
        if target not in typed_targets:
            typed_links.append({"target": target, "relation": "relaciona", "label": ""})
            typed_targets.add(target)

    return {
        "slug": slug,
        "title": fm.get("title", slug),
        "topics": fm.get("tags", []),
        "provenance": fm.get("provenance", "source"),
        "quarantine": bool(fm.get("quarantine")),
        "raw_deps": raw_deps,
        "links": links,
        "typed_links": typed_links,
    }


def build_graph(articles: list[dict]) -> dict:
    """
    Graph structure:
    {
      "nodes": {slug: {title, topics, provenance, quarantine}},
      "edges": [
        {source, target, type: "untyped"|relation_label, label}
      ],
      "index": {
        # slug → list of slugs that link TO it (in-links)
        "in_links": {slug: [slug, ...]},
        # slug → list of slugs it links to (out-links)
        "out_links": {slug: [slug, ...]},
        # slug → raw_deps
        "raw_deps": {slug: [path, ...]},
      }
    }
    """
    all_slugs = {a["slug"] for a in articles}
    nodes = {}
    edges = []
    in_links: dict[str, list[str]] = {a["slug"]: [] for a in articles}
    out_links: dict[str, list[str]] = {a["slug"]: [] for a in articles}
    raw_deps_index: dict[str, list[str]] = {}

    for art in articles:
        slug = art["slug"]
        nodes[slug] = {
            "title": art["title"],
            "topics": art["topics"],
            "provenance": art["provenance"],
            "quarantine": art["quarantine"],
        }
        raw_deps_index[slug] = art["raw_deps"]

        # untyped edges for wikilinks not already in typed_links
        typed_targets = {tl["target"] for tl in art["typed_links"]}
        for target in art["links"]:
            if target not in typed_targets and target in all_slugs:
                edges.append(
                    {
                        "source": slug,
                        "target": target,
                        "type": "untyped",
                        "label": "",
                    }
                )
                out_links[slug].append(target)
                in_links.setdefault(target, []).append(slug)

        # typed edges
        for tl in art["typed_links"]:
            target = tl["target"]
            if target in all_slugs:
                edges.append(
                    {
                        "source": slug,
                        "target": target,
                        "type": tl["relation"],
                        "label": tl["label"],
                    }
                )
                out_links[slug].append(target)
                in_links.setdefault(target, []).append(slug)

    return {
        "nodes": nodes,
        "edges": edges,
        "index": {
            "in_links": in_links,
            "out_links": out_links,
            "raw_deps": raw_deps_index,
        },
    }


def patch_article_health(
    graph: dict,
    articles: dict[str, dict],
    dry_run: bool = False,
) -> None:
    """
    Update article-health.yaml: for each promoted article, replace wiki/ entries
    in depends_on with auto-discovered out_links + keep raw/ entries as-is.
    """
    if not HEALTH_PATH.exists():
        print("  article-health.yaml not found — skip health patch")
        return

    health_raw = HEALTH_PATH.read_text(encoding="utf-8")
    health = yaml.safe_load(health_raw) or {}
    out_links = graph["index"]["out_links"]
    raw_deps = graph["index"]["raw_deps"]

    changed = 0
    for entry in health.get("articles", []):
        slug = entry.get("article_slug")
        if not slug or slug not in articles:
            continue

        # Preserve existing raw/ deps (manually curated, authoritative)
        existing_raw = [d for d in entry.get("depends_on", []) if d.startswith("raw/")]

        # Auto-derive wiki/ deps from graph out_links
        wiki_deps = sorted({f"wiki/concepts/{t}.md" for t in out_links.get(slug, [])})

        # Also include raw/ from article frontmatter sources
        frontmatter_raw = raw_deps.get(slug, [])
        merged_raw = sorted(set(existing_raw) | set(frontmatter_raw))

        new_depends_on = merged_raw + wiki_deps

        if new_depends_on != entry.get("depends_on", []):
            changed += 1
            if dry_run:
                print(
                    f"  [dry] {slug}: depends_on {len(entry.get('depends_on', []))} → {len(new_depends_on)}"
                )
            else:
                entry["depends_on"] = new_depends_on

    if not dry_run and changed:
        HEALTH_PATH.write_text(
            yaml.dump(
                health, allow_unicode=True, sort_keys=False, default_flow_style=False
            ),
            encoding="utf-8",
        )
        print(f"  article-health.yaml patched: {changed} articles updated")
    elif dry_run:
        print(f"  [dry] {changed} articles would be updated in article-health.yaml")
    else:
        print("  article-health.yaml: no changes needed")


def main():
    parser = argparse.ArgumentParser(description="Build KB link graph")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--graph-only",
        action="store_true",
        help="Build graph only, skip article-health.yaml patch",
    )
    args = parser.parse_args()

    paths = sorted(WIKI_DIR.glob("*.md"))
    print(f"Parsing {len(paths)} wiki articles...")

    articles_list = []
    articles_by_slug: dict[str, dict] = {}
    for path in paths:
        try:
            art = parse_article(path)
            articles_list.append(art)
            articles_by_slug[art["slug"]] = art
        except Exception as e:
            print(f"  warn: {path.name} — {e}")

    graph = build_graph(articles_list)

    node_count = len(graph["nodes"])
    edge_count = len(graph["edges"])
    typed_count = sum(1 for e in graph["edges"] if e["type"] != "untyped")
    print(f"Graph: {node_count} nodes, {edge_count} edges ({typed_count} typed)")

    if not args.dry_run:
        GRAPH_OUT.parent.mkdir(parents=True, exist_ok=True)
        GRAPH_OUT.write_text(json.dumps(graph, ensure_ascii=False, indent=2))
        print(f"Wrote {GRAPH_OUT}")
    else:
        print(f"[dry] would write {GRAPH_OUT}")

    if not args.graph_only:
        patch_article_health(graph, articles_by_slug, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
