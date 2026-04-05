#!/usr/bin/env python3
"""
Single Brain — Phase 1 query interface.

Semantic search over LanceDB index.

Usage:
    python scripts/single-brain/query.py "como agentes coordenam memória compartilhada"
    python scripts/single-brain/query.py "world model" --network observation --top-k 5
"""

import argparse
import sys
from pathlib import Path

import lancedb
import ollama

ROOT = Path(__file__).parent.parent.parent
DB_PATH = ROOT / "outputs" / "single-brain" / "db"
EMBED_MODEL = "nomic-embed-text"
TABLE_NAME = "fragments"


def search(query: str, network: str | None = None, top_k: int = 5) -> list[dict]:
    db = lancedb.connect(str(DB_PATH))
    if TABLE_NAME not in db.table_names():
        print("Index not found. Run ingest.py first.", file=sys.stderr)
        sys.exit(1)

    table = db.open_table(TABLE_NAME)
    vector = ollama.embeddings(model=EMBED_MODEL, prompt=query)["embedding"]

    results = table.search(vector).limit(top_k * 3)
    if network:
        results = results.where(f"network = '{network}'")
    results = results.limit(top_k).to_list()

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="+")
    parser.add_argument(
        "--network", choices=["world", "experience", "opinion", "observation"]
    )
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    query = " ".join(args.query)
    results = search(query, network=args.network, top_k=args.top_k)

    if args.json:
        import json

        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    print(f"\n🔍 Query: {query}\n")
    for i, r in enumerate(results, 1):
        score = 1 - r.get("_distance", 1)
        print(f"[{i}] {r['title']} ({r['network']}) — score {score:.3f}")
        print(f"    {r['source']}")
        print(f"    {r['content'][:200].strip()}...")
        print()


if __name__ == "__main__":
    main()
