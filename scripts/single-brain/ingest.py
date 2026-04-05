#!/usr/bin/env python3
"""
Single Brain — Phase 1 ingest pipeline.

Pipeline:
  1. MarkdownNodeParser — split on headings, preserve section hierarchy
  2. SentenceSplitter   — cap chunks > MAX_CHUNK_WORDS (soft ceiling)
  3. merge_small_chunks — eliminate tiny/heading-only fragments
  4. contextual_prefix  — prepend "title | section" to embed input only
  5. embed              — paraphrase-multilingual via Ollama (128-token ctx)
  6. store              — LanceDB fragments table

Usage:
    python scripts/single-brain/ingest.py              # ingest all
    python scripts/single-brain/ingest.py --dry-run    # preview only
    python scripts/single-brain/ingest.py --file wiki/concepts/foo.md
"""

import argparse
import hashlib
import re
from datetime import date
from pathlib import Path

import lancedb
import ollama
import yaml
from llama_index.core import Document
from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent.parent
WIKI_DIR = ROOT / "wiki" / "concepts"
DB_PATH = ROOT / "outputs" / "single-brain" / "db"

# ── Config ────────────────────────────────────────────────────────────────────
EMBED_MODEL = "paraphrase-multilingual"
EMBED_DIMS = 768
TABLE_NAME = "fragments"
MIN_CHUNK_WORDS = 50  # merge chunks smaller than this into previous
MAX_CHUNK_WORDS = 300  # SentenceSplitter kicks in above this


# ── Text helpers ──────────────────────────────────────────────────────────────


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


def extract_section(text: str) -> str:
    """Return the leading heading of a markdown chunk, stripped of # markers."""
    m = re.match(r"^#{1,4}\s+(.+)", text.strip())
    return m.group(1).strip() if m else ""


def strip_markdown(text: str) -> str:
    """Remove markdown syntax before embedding — preserves semantics, reduces token count."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # [label](url) → label
    text = re.sub(r"https?://\S+", "", text)  # bare URLs
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)  # images
    text = re.sub(r"^\|.*\|$", "", text, flags=re.M)  # table rows
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.M)  # headings
    text = re.sub(r"[*_`~]{1,3}", "", text)  # bold/italic/code
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)  # wikilinks
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ── Chunking ──────────────────────────────────────────────────────────────────


def merge_small_chunks(chunks: list[str]) -> list[str]:
    """Merge chunks < MIN_CHUNK_WORDS (or heading-only) into the previous chunk."""
    merged: list[str] = []
    for text in chunks:
        is_heading_only = bool(re.match(r"^#{1,4} .{0,80}$", text.strip()))
        if merged and (len(text.split()) < MIN_CHUNK_WORDS or is_heading_only):
            merged[-1] = merged[-1].rstrip() + "\n\n" + text
        else:
            merged.append(text)
    return [t for t in merged if t.strip()]


def split_large_chunks(chunks: list[str]) -> list[str]:
    """Apply SentenceSplitter to chunks that exceed MAX_CHUNK_WORDS."""
    splitter = SentenceSplitter(chunk_size=MAX_CHUNK_WORDS, chunk_overlap=30)
    result = []
    for text in chunks:
        if len(text.split()) <= MAX_CHUNK_WORDS:
            result.append(text)
        else:
            doc = Document(text=text)
            nodes = splitter.get_nodes_from_documents([doc])
            result.extend(n.get_content() for n in nodes if n.get_content().strip())
    return result


def chunk_document(body: str) -> list[tuple[str, str]]:
    """
    Returns list of (section, content) tuples.
    section = heading text leading the chunk (empty string if none).
    """
    doc = Document(text=body)
    nodes = MarkdownNodeParser().get_nodes_from_documents([doc])
    raw = [n.get_content() for n in nodes]
    chunks = merge_small_chunks(raw)
    chunks = split_large_chunks(chunks)

    result = []
    for chunk in chunks:
        section = extract_section(chunk)
        result.append((section, chunk))
    return result


# ── Embedding ─────────────────────────────────────────────────────────────────


def embed(content: str, title: str = "", section: str = "") -> list[float]:
    """
    Embed with contextual prefix (title | section) prepended.
    Strips markdown, then progressively truncates to fit paraphrase-multilingual
    128-token context window.
    """
    prefix = title
    if section:
        prefix = f"{title} | {section}"

    clean = strip_markdown(f"{prefix}\n\n{content}" if prefix else content)
    words = clean.split()

    for limit in [40, 30, 20, 10]:
        prompt = " ".join(words[:limit]) if len(words) > limit else clean
        try:
            return ollama.embeddings(model=EMBED_MODEL, prompt=prompt)["embedding"]
        except Exception:
            continue
    raise RuntimeError(f"embed failed at 10 words: {repr(clean[:80])}")


# ── DB helpers ────────────────────────────────────────────────────────────────


def fragment_id(source_path: str, chunk_index: int) -> str:
    key = f"{source_path}::{chunk_index}"
    return hashlib.sha256(key.encode()).hexdigest()[:16]


def determine_network(fm: dict) -> str:
    if fm.get("quarantine"):
        return "opinion"
    if fm.get("provenance") == "emergence":
        return "opinion"
    return "observation"


def get_or_create_table(db):
    import pyarrow as pa

    schema = pa.schema(
        [
            pa.field("id", pa.string()),
            pa.field("content", pa.string()),
            pa.field("section", pa.string()),
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


# ── Ingest ────────────────────────────────────────────────────────────────────


def ingest_file(path: Path, table, dry_run: bool = False) -> int:
    text = path.read_text()
    fm, body = parse_frontmatter(text)

    if not body.strip():
        print(f"  skip {path.name} — empty body")
        return 0

    network = determine_network(fm)
    title = fm.get("title", path.stem)
    created = str(fm.get("created", date.today()))
    chunks = chunk_document(body)

    if dry_run:
        print(f"  {path.name} → {len(chunks)} chunks [{network}]")
        for sec, c in chunks[:3]:
            prefix = f"[{sec[:30]}] " if sec else ""
            print(f"    {prefix}{len(c.split())}w")
        return len(chunks)

    source = str(path.relative_to(ROOT))
    rows = []
    for i, (section, content) in enumerate(chunks):
        rows.append(
            {
                "id": fragment_id(source, i),
                "content": content,
                "section": section,
                "vector": embed(content, title=title, section=section),
                "network": network,
                "source": source,
                "title": title,
                "created": created,
                "agent": "ingest-v2",
            }
        )

    if rows:
        try:
            table.delete(f"source = '{source}'")
        except Exception:
            pass
        table.add(rows)

    print(f"  {path.name} → {len(rows)} chunks [{network}]")
    return len(rows)


def hub_order(paths: list[Path]) -> list[Path]:
    registry = ROOT / "wiki" / "_registry.md"
    if not registry.exists():
        return paths
    text = registry.read_text()
    return sorted(paths, key=lambda p: text.count(p.stem), reverse=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--file", type=Path)
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Drop and recreate table (needed after schema change)",
    )
    args = parser.parse_args()

    db = lancedb.connect(str(DB_PATH))

    if args.rebuild and not args.dry_run:
        if TABLE_NAME in db.table_names():
            db.drop_table(TABLE_NAME)
            print(f"Dropped table '{TABLE_NAME}'")

    table = None if args.dry_run else get_or_create_table(db)

    paths = (
        [args.file.resolve()] if args.file else hub_order(list(WIKI_DIR.glob("*.md")))
    )

    total = 0
    print(f"{'DRY RUN — ' if args.dry_run else ''}Ingesting {len(paths)} articles...")
    for path in paths:
        total += ingest_file(path, table, dry_run=args.dry_run)

    print(f"\n✓ {len(paths)} articles → {total} chunks in {DB_PATH}")


if __name__ == "__main__":
    main()
