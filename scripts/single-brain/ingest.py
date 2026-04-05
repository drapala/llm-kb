#!/usr/bin/env python3
"""
Single Brain — Phase 1 ingest pipeline.

Reads wiki/concepts/*.md → chunks with MarkdownNodeParser →
embeds with nomic-embed-text (Ollama) → stores in LanceDB.

Usage:
    python scripts/single-brain/ingest.py              # ingest all
    python scripts/single-brain/ingest.py --dry-run    # preview only
    python scripts/single-brain/ingest.py --file wiki/concepts/agent-memory-architectures.md
"""

import argparse
import hashlib
from datetime import date
from pathlib import Path

import lancedb
import ollama
import yaml
from llama_index.core import Document
from llama_index.core.node_parser import MarkdownNodeParser

# ── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent.parent
WIKI_DIR = ROOT / "wiki" / "concepts"
DB_PATH = ROOT / "outputs" / "single-brain" / "db"

# ── Config ───────────────────────────────────────────────────────────────────
EMBED_MODEL = "nomic-embed-text"
EMBED_DIMS = 768
TABLE_NAME = "fragments"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML frontmatter from markdown body."""
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


def determine_network(fm: dict) -> str:
    """Map frontmatter to Hindsight network namespace."""
    if fm.get("quarantine"):
        return "opinion"  # speculative — not yet validated
    if fm.get("provenance") == "emergence":
        return "opinion"  # emerged but promoted
    return "observation"  # compiled, promoted knowledge


def fragment_id(source_path: str, chunk_index: int) -> str:
    key = f"{source_path}::{chunk_index}"
    return hashlib.sha256(key.encode()).hexdigest()[:16]


def embed(text: str) -> list[float]:
    response = ollama.embeddings(model=EMBED_MODEL, prompt=text)
    return response["embedding"]


def ingest_file(path: Path, table, dry_run: bool = False) -> int:
    text = path.read_text()
    fm, body = parse_frontmatter(text)

    if not body.strip():
        print(f"  skip {path.name} — empty body")
        return 0

    network = determine_network(fm)
    title = fm.get("title", path.stem)
    created = str(fm.get("created", date.today()))

    doc = Document(text=body, metadata={"source": str(path.relative_to(ROOT))})
    nodes = MarkdownNodeParser().get_nodes_from_documents([doc])

    if dry_run:
        print(f"  {path.name} → {len(nodes)} chunks [{network}]")
        return len(nodes)

    rows = []
    for i, node in enumerate(nodes):
        content = node.get_content()
        if len(content.strip()) < 20:
            continue
        rows.append(
            {
                "id": fragment_id(str(path.relative_to(ROOT)), i),
                "content": content,
                "vector": embed(content),
                "network": network,
                "source": str(path.relative_to(ROOT)),
                "title": title,
                "created": created,
                "agent": "ingest-script-v1",
            }
        )

    if rows:
        # Delete existing fragments from this source (update = delete + reinsert)
        try:
            table.delete(f"source = '{path.relative_to(ROOT)}'")
        except Exception:
            pass
        table.add(rows)

    print(f"  {path.name} → {len(rows)} chunks [{network}]")
    return len(rows)


def get_or_create_table(db):
    import pyarrow as pa

    schema = pa.schema(
        [
            pa.field("id", pa.string()),
            pa.field("content", pa.string()),
            pa.field("vector", pa.list_(pa.float32(), EMBED_DIMS)),
            pa.field("network", pa.string()),
            pa.field("source", pa.string()),
            pa.field("title", pa.string()),
            pa.field("created", pa.string()),
            pa.field("agent", pa.string()),
        ]
    )

    if TABLE_NAME in db.table_names():
        return db.open_table(TABLE_NAME)
    return db.create_table(TABLE_NAME, schema=schema)


def hub_order(paths: list[Path]) -> list[Path]:
    """Sort by in-degree from _registry.md (hubs first)."""
    registry = ROOT / "wiki" / "_registry.md"
    if not registry.exists():
        return paths

    text = registry.read_text()

    def count_refs(p: Path) -> int:
        return text.count(p.stem)

    return sorted(paths, key=count_refs, reverse=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--file", type=Path)
    args = parser.parse_args()

    db = lancedb.connect(str(DB_PATH))
    table = None if args.dry_run else get_or_create_table(db)

    if args.file:
        paths = [args.file]
    else:
        paths = hub_order(list(WIKI_DIR.glob("*.md")))

    total_chunks = 0
    print(f"{'DRY RUN — ' if args.dry_run else ''}Ingesting {len(paths)} articles...")

    for path in paths:
        total_chunks += ingest_file(path, table, dry_run=args.dry_run)

    print(f"\n✓ {len(paths)} articles → {total_chunks} chunks stored in {DB_PATH}")


if __name__ == "__main__":
    main()
