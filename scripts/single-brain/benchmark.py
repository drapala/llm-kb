#!/usr/bin/env python3
"""
Single Brain — Recall@1 benchmark.

Usage:
    python scripts/single-brain/benchmark.py
    python scripts/single-brain/benchmark.py --rerank
    python scripts/single-brain/benchmark.py --compare   # baseline vs rerank side-by-side
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

from api.core import search  # noqa: E402

# ── Benchmark suite ───────────────────────────────────────────────────────────
# Each entry: (query, expected_slug)
# Queries are tuned to point unambiguously at the expected article.
SUITE = [
    ("hybrid search BM25 vector RRF fusion retrieval", "hybrid-search"),
    ("lancedb embedded vector database lance format", "lancedb-embedded-vector-db"),
    (
        "autonomous knowledge base failure modes drift silent",
        "autonomous-kb-failure-modes",
    ),
    (
        "multi-agent orchestration coordinator subagent workflow",
        "multi-agent-orchestration",
    ),
    (
        "reflexion verbal reinforcement learning self-improving agents",
        "self-improving-agents",
    ),
    (
        "fast frugal heuristics gigerenzer bias variance small sample",
        "fast-frugal-heuristics",
    ),
    (
        "retrieval augmented generation RAG long context evaluation",
        "retrieval-augmented-generation",
    ),
    # single-brain-data-ontology: Hindsight 4 namespaces, not Tulving episodic memory
    (
        "hindsight 4 networks epistemic observation opinion world model",
        "single-brain-data-ontology",
    ),
    # corruption-audits-brazil: Ferraz & Finan 2008 CGU audit → reelection, not 2011 term limits
    (
        "CGU random audits mayors reelection brazil corrupt politicians",
        "corruption-audits-brazil",
    ),
    (
        "McClelland 1995 catastrophic interference hippocampus neocortex consolidation",
        "complementary-learning-systems",
    ),
]


def run(rerank: bool = False) -> tuple[int, list[tuple[bool, str, str]]]:
    hits = 0
    rows = []
    for query, expected_slug in SUITE:
        results = search(query, limit=1, rerank=rerank)
        top = results[0] if results else None
        got_slug = top["source"].split("/")[-1].replace(".md", "") if top else "NONE"
        ok = expected_slug in got_slug or got_slug in expected_slug
        hits += ok
        rows.append((ok, got_slug, expected_slug, query))
    return hits, rows


def print_results(label: str, hits: int, rows: list):
    print(f"\n{'─' * 60}")
    print(f"  {label}  —  Recall@1: {hits}/{len(SUITE)}")
    print(f"{'─' * 60}")
    for ok, got, exp, query in rows:
        status = "✓" if ok else "✗"
        print(f"  {status} {got:<40} ← {query[:50]}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rerank", action="store_true", help="Use cross-encoder reranker"
    )
    parser.add_argument(
        "--compare", action="store_true", help="Run both modes side-by-side"
    )
    args = parser.parse_args()

    if args.compare:
        hits_base, rows_base = run(rerank=False)
        hits_re, rows_re = run(rerank=True)
        print_results("baseline (hybrid RRF)", hits_base, rows_base)
        print_results("+ cross-encoder rerank", hits_re, rows_re)
        delta = hits_re - hits_base
        sign = "+" if delta >= 0 else ""
        print(f"\n  Delta: {sign}{delta}")
    else:
        hits, rows = run(rerank=args.rerank)
        label = "hybrid + rerank" if args.rerank else "hybrid (baseline)"
        print_results(label, hits, rows)


if __name__ == "__main__":
    main()
