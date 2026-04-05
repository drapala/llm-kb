"""
Shared logic: DB connection, embed, hybrid search, ingest trigger.
Imported by both FastAPI (api/main.py) and MCP server (mcp_server.py).
"""

from __future__ import annotations

import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

import lancedb
import ollama
from langdetect import LangDetectException
from langdetect import detect as _langdetect

ROOT = Path(__file__).parent.parent
DB_PATH = ROOT / "outputs" / "single-brain" / "db"
EMBED_MODEL = "paraphrase-multilingual"
TABLE_NAME = "fragments"

# Hybrid search weights — baseline (PT query vs PT corpus)
W_VECTOR = 0.6
W_BM25 = 0.4
# Cross-language weights — BM25 degrades on EN→PT lexical mismatch
W_VECTOR_CROSSLANG = 0.9
W_BM25_CROSSLANG = 0.1
RRF_K = 60

KB_LANG = "pt"


# ── Language detection ────────────────────────────────────────────────────────


def query_lang(text: str) -> str:
    try:
        return _langdetect(text)
    except LangDetectException:
        return "en"


# ── DB ────────────────────────────────────────────────────────────────────────


@lru_cache(maxsize=1)
def get_table():
    db = lancedb.connect(str(DB_PATH))
    t = db.open_table(TABLE_NAME)
    try:
        t.create_fts_index("content", replace=False)
    except Exception:
        pass
    return t


# ── Embedding ─────────────────────────────────────────────────────────────────


def _strip_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"^\|.*\|$", "", text, flags=re.M)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"[*_`~]{1,3}", "", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def embed(text: str, title: str = "", section: str = "") -> list[float]:
    """
    Embed with contextual prefix prepended: "title | section\\n\\ncontent".
    Strips markdown, then progressively truncates for paraphrase-multilingual (128-token ctx).
    """
    prefix = f"{title} | {section}" if section else title
    full = f"{prefix}\n\n{text}" if prefix else text
    clean = _strip_markdown(full)
    words = clean.split()
    for limit in [40, 30, 20, 10]:
        prompt = " ".join(words[:limit]) if len(words) > limit else clean
        try:
            return ollama.embeddings(model=EMBED_MODEL, prompt=prompt)["embedding"]
        except Exception:
            continue
    raise RuntimeError(f"embed failed at 10 words: {repr(clean[:80])}")


# ── Search ────────────────────────────────────────────────────────────────────

_SELECT = ["id", "content", "section", "title", "source", "network", "created"]


def _rrf_merge(
    vector_rows: list[dict],
    bm25_rows: list[dict],
    limit: int,
    w_vector: float = W_VECTOR,
    w_bm25: float = W_BM25,
) -> list[dict]:
    scores: dict[str, float] = {}
    by_id: dict[str, dict] = {}
    for rank, row in enumerate(vector_rows):
        rid = row["id"]
        scores[rid] = scores.get(rid, 0) + w_vector / (RRF_K + rank + 1)
        by_id[rid] = row
    for rank, row in enumerate(bm25_rows):
        rid = row["id"]
        scores[rid] = scores.get(rid, 0) + w_bm25 / (RRF_K + rank + 1)
        by_id.setdefault(rid, row)
    merged = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [{**by_id[rid], "score": round(s, 6)} for rid, s in merged[:limit]]


def search(
    query: str,
    network: str | None = None,
    limit: int = 10,
    mode: str = "hybrid",
) -> list[dict]:
    table = get_table()
    fetch = limit * 3

    def _where(q):
        return q.where(f"network = '{network}'") if network else q

    def _fmt(rows: list[dict], score_key: str = "_distance") -> list[dict]:
        return [
            {
                "id": r["id"],
                "title": r["title"],
                "section": r.get("section", ""),
                "source": r["source"],
                "network": r["network"],
                "created": r["created"],
                "score": float(r.get(score_key, 0)),
                "content": r["content"][:500],
            }
            for r in rows
        ]

    if mode == "vector":
        rows = _where(
            table.search(embed(query)).limit(limit).select([*_SELECT, "_distance"])
        ).to_list()
        return _fmt(rows)

    if mode == "bm25":
        rows = _where(
            table.search(query, query_type="fts").limit(limit).select(_SELECT)
        ).to_list()
        return _fmt(rows, score_key="_score")

    # hybrid — language-adaptive RRF
    lang = query_lang(query)
    w_vec = W_VECTOR_CROSSLANG if lang != KB_LANG else W_VECTOR
    w_bm = W_BM25_CROSSLANG if lang != KB_LANG else W_BM25

    vec_rows = _fmt(
        _where(
            table.search(embed(query)).limit(fetch).select([*_SELECT, "_distance"])
        ).to_list()
    )
    try:
        bm25_rows = _fmt(
            _where(
                table.search(query, query_type="fts").limit(fetch).select(_SELECT)
            ).to_list(),
            score_key="_score",
        )
    except Exception:
        bm25_rows = []

    return _rrf_merge(vec_rows, bm25_rows, limit, w_vector=w_vec, w_bm25=w_bm)


# ── Ingest ────────────────────────────────────────────────────────────────────


def run_ingest(file: str | None = None, rebuild: bool = False) -> dict:
    script = ROOT / "scripts" / "single-brain" / "ingest.py"
    cmd = [sys.executable, str(script)]
    if rebuild:
        cmd.append("--rebuild")
    if file:
        cmd += ["--file", str((ROOT / file).resolve())]

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
    get_table.cache_clear()

    return {
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip() if result.returncode != 0 else None,
    }


# ── Stats ─────────────────────────────────────────────────────────────────────


def stats() -> dict:
    table = get_table()
    df = table.to_pandas()
    df["tokens"] = df["content"].str.split().str.len()
    return {
        "total_chunks": len(df),
        "by_network": df["network"].value_counts().to_dict(),
        "unique_articles": df["source"].nunique(),
        "chunk_tokens": {
            "mean": float(round(df["tokens"].mean(), 1)),
            "median": float(round(df["tokens"].median(), 1)),
            "min": int(df["tokens"].min()),
            "max": int(df["tokens"].max()),
            "pct_under_50": float(round((df["tokens"] < 50).mean() * 100, 1)),
            "heading_only": int(df["content"].str.match(r"^#{1,4} .{0,80}$").sum()),
        },
    }
