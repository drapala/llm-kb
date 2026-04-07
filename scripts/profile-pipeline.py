#!/usr/bin/env python3
"""
Pipeline profiler — mede cada etapa do /auto pipeline.

Foco: ingest.py (etapas mensuráveis sem LLM calls externas completas).
Para LLM calls (stance-classify, cross-model-challenge), faz 1 call real e extrapola.

Usage:
    python scripts/profile-pipeline.py [--sample N]  # N artigos (default: 5)
"""

import argparse
import time
import asyncio
import sys
import hashlib
import statistics
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

stages: dict[str, float] = {}
details: dict[str, list] = {}


async def timed(name: str, fn, *args):
    start = time.perf_counter()
    if asyncio.iscoroutinefunction(fn):
        result = await fn(*args)
    else:
        result = fn(*args)
    elapsed = time.perf_counter() - start
    stages[name] = stages.get(name, 0) + elapsed
    details.setdefault(name, []).append(elapsed)
    return result


# ── Import pipeline internals ─────────────────────────────────────────────────


def load_pipeline():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "ingest", ROOT / "scripts" / "single-brain" / "ingest.py"
    )
    mod = (
        importlib.util.load_from_spec(spec)
        if hasattr(importlib.util, "load_from_spec")
        else None
    )
    # fallback: direct import
    sys.path.insert(0, str(ROOT / "scripts" / "single-brain"))
    import ingest as ing

    return ing


# ── Stage functions ───────────────────────────────────────────────────────────


def stage_read_file(path: Path) -> str:
    return path.read_text()


def stage_parse_frontmatter(ing, text: str):
    return ing.parse_frontmatter(text)


def stage_chunk_document(ing, body: str):
    return ing.chunk_document(body)


def stage_embed_single(ing, content: str, title: str, section: str):
    return ing.embed(content, title=title, section=section)


def stage_lancedb_write(table, rows: list):
    if rows and table:
        source = rows[0]["source"]
        try:
            table.delete(f"source = '{source}'")
        except Exception:
            pass
        table.add(rows)


def stage_lancedb_connect():
    import lancedb

    db_path = ROOT / "outputs" / "single-brain" / "db"
    db = lancedb.connect(str(db_path))
    if "fragments" in db.table_names():
        return db.open_table("fragments")
    return None


def stage_yaml_read():
    import yaml

    path = ROOT / "outputs" / "state" / "kb-state.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


# ── Main profiler ─────────────────────────────────────────────────────────────


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sample", type=int, default=5, help="Número de artigos para amostrar"
    )
    parser.add_argument(
        "--embed-sample", type=int, default=10, help="Chunks para amostrar no embed"
    )
    args = parser.parse_args()

    print(f"\n{'=' * 60}")
    print("LLM-KB Pipeline Profiler")
    print(f"Sample: {args.sample} artigos, {args.embed_sample} chunks para embed")
    print(f"{'=' * 60}\n")

    ing = load_pipeline()

    # ── Etapa 0: kb-state.yaml read ───────────────────────────────────────────
    print("[0] kb-state.yaml read...")
    await timed("0_yaml_read", stage_yaml_read)

    # ── Etapa 1: LanceDB connect ──────────────────────────────────────────────
    print("[1] LanceDB connect...")
    table = await timed("1_lancedb_connect", stage_lancedb_connect)

    # ── Etapa 2-5: por arquivo ────────────────────────────────────────────────
    wiki_dir = ROOT / "wiki" / "concepts"
    paths = list(wiki_dir.glob("*.md"))[: args.sample]
    print(f"\n[2-5] Processando {len(paths)} artigos...\n")

    total_chunks = 0
    embed_times = []

    for path in paths:
        print(f"  {path.name}")

        # Etapa 2: file read
        text = await timed("2_file_read", stage_read_file, path)

        # Etapa 3: parse frontmatter
        fm, body = await timed(
            "3_parse_frontmatter", stage_parse_frontmatter, ing, text
        )
        if not body.strip():
            continue

        # Etapa 4: chunking (MarkdownNodeParser + SentenceSplitter + merge)
        chunks = await timed("4_chunk_document", stage_chunk_document, ing, body)
        total_chunks += len(chunks)
        title = fm.get("title", path.stem)

        # Etapa 5: embed (sample de chunks por artigo)
        sample_chunks = chunks[: args.embed_sample]
        rows = []
        for i, (section, content) in enumerate(sample_chunks):
            t0 = time.perf_counter()
            vec = await timed(
                "5_embed_per_chunk", stage_embed_single, ing, content, title, section
            )
            embed_times.append(time.perf_counter() - t0)
            rows.append(
                {
                    "id": hashlib.sha256(f"{path}::{i}".encode()).hexdigest()[:16],
                    "content": content,
                    "section": section,
                    "vector": vec,
                    "network": "observation",
                    "source": str(path.relative_to(ROOT)),
                    "title": title,
                    "created": str(fm.get("created", "2026-04-06")),
                    "agent": "profiler",
                }
            )

        # Etapa 6: LanceDB write (skip write in profiler — just time the call)
        # await timed("6_lancedb_write", stage_lancedb_write, table, rows)
        # (comentado para não sujar o DB com dados de profiling)

    # ── Relatório ─────────────────────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    print("RESULTADOS DO PROFILING")
    print(f"{'=' * 60}")

    sampled_chunks = len(embed_times)
    avg_embed = statistics.mean(embed_times) if embed_times else 0
    p95_embed = sorted(embed_times)[int(len(embed_times) * 0.95)] if embed_times else 0

    print(f"\n{'Etapa':<35} {'Total (s)':>10} {'Tipo':>10}")
    print("-" * 58)

    report = [
        ("0_yaml_read", "I/O (disco)"),
        ("1_lancedb_connect", "I/O (disco)"),
        ("2_file_read", "I/O (disco)"),
        ("3_parse_frontmatter", "CPU"),
        ("4_chunk_document", "CPU"),
        ("5_embed_per_chunk", "I/O (Ollama)"),
    ]

    for key, tipo in report:
        total = stages.get(key, 0)
        print(f"  {key:<33} {total:>10.3f}s {tipo:>10}")

    print(f"\n{'─' * 58}")
    print(f"  Artigos amostrados:     {len(paths)}")
    print(f"  Chunks totais:          {total_chunks}")
    print(f"  Chunks embedados:       {sampled_chunks}")
    print(f"  Embed médio/chunk:      {avg_embed:.3f}s")
    print(f"  Embed p95/chunk:        {p95_embed:.3f}s")

    # Extrapolação para todo o corpus
    all_articles = list(wiki_dir.glob("*.md"))
    n_all = len(all_articles)
    avg_chunks_per_article = total_chunks / max(len(paths), 1)
    total_chunks_full = n_all * avg_chunks_per_article
    embed_full_sequential = total_chunks_full * avg_embed

    print(f"\n{'=' * 60}")
    print("EXTRAPOLAÇÃO PARA CORPUS COMPLETO")
    print(f"{'=' * 60}")
    print(f"  Artigos totais:         {n_all}")
    print(f"  Chunks estimados:       {total_chunks_full:.0f}")
    print(
        f"  Embed sequencial:       {embed_full_sequential:.1f}s  ({embed_full_sequential / 60:.1f} min)"
    )
    print("\n  NOTA: LLM calls (stance-classify, cross-model-challenge)")
    print("        NÃO estão neste profiling — são I/O bound por API.")
    print("        Cada call GPT/Gemini com reasoning ≈ 30-90s.")
    print("        Cada stance-classify (Haiku) ≈ 2-4s.")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    asyncio.run(main())
