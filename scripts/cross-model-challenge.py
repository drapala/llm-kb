#!/usr/bin/env python3
"""
cross-model-challenge.py — Oracle externo para validação de pares emergentes.

Resolve o Pilar 1 do autoresearch-reliability-triad: usa modelo independente
(GPT-4o ou Gemini) para avaliar se uma conexão entre dois artigos da KB é
estrutural (genuína) ou superficial (analogia enganosa).

Uso:
  echo '{"pair": {...}}' | python3 scripts/cross-model-challenge.py
  python3 scripts/cross-model-challenge.py --file /tmp/pair.json
  python3 scripts/cross-model-challenge.py --mode gemini --file /tmp/pair.json

Input JSON (stdin ou --file):
{
  "article_a": {
    "title": "...",
    "summary": "...",       # 2-3 frases do artigo
    "mechanism": "..."      # X causa Y via Z
  },
  "article_b": {
    "title": "...",
    "summary": "...",
    "mechanism": "..."
  },
  "proposed_connection": "...",   # descrição da conexão proposta
  "connection_type": "ANÁLOGO-A | INSTANCIA | EMERGE-DE",
  "pearl_level": "L1 | L2 | L3"
}

Output JSON (stdout):
{
  "score": 1-10,
  "verdict": "GENUINE | SUPERFICIAL",
  "reasoning": "...",
  "model_used": "gpt-4o | gemini-1.5-pro",
  "confidence": "high | medium | low"
}

Exit codes:
  0 — sucesso
  1 — erro de API ou configuração
  2 — input inválido

Dependências: openai>=1.0, google-generativeai>=0.5
  uv pip install openai google-generativeai python-dotenv
"""

import argparse
import json
import os
import sys
from pathlib import Path

# ── Carrega .env se presente ────────────────────────────────────────────────
env_file = Path(__file__).parent.parent / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")

# ── Prompt ────────────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are an epistemologist evaluating whether a proposed conceptual
connection between two knowledge-base articles represents a genuine structural isomorphism
or a superficial analogy.

You have NO access to the knowledge base itself. Your evaluation is based solely on the
article summaries and the proposed connection provided. This independence is intentional —
you are the external oracle."""


def build_user_prompt(pair: dict) -> str:
    a = pair["article_a"]
    b = pair["article_b"]
    return f"""Evaluate this proposed connection between two articles:

ARTICLE A: {a["title"]}
Summary: {a["summary"]}
Core mechanism: {a["mechanism"]}

ARTICLE B: {b["title"]}
Summary: {b["summary"]}
Core mechanism: {b["mechanism"]}

PROPOSED CONNECTION: {pair["proposed_connection"]}
Connection type: {pair["connection_type"]}
Pearl causal level claimed: {pair["pearl_level"]}

Evaluate:
1. Are the mechanisms structurally isomorphic (same causal structure in different domains)?
   Or are they connected only by surface-level similarity?
2. Would domain experts in BOTH fields recognize this as a non-trivial insight?
3. Is the Pearl level ({pair["pearl_level"]}) appropriate given the evidence?

Respond ONLY with valid JSON:
{{
  "score": <integer 1-10>,
  "verdict": "<GENUINE or SUPERFICIAL>",
  "reasoning": "<2-3 sentences explaining why>",
  "confidence": "<high|medium|low>",
  "pearl_level_appropriate": <true|false>,
  "main_concern": "<null or one-line concern if verdict is SUPERFICIAL>"
}}

GENUINE = score >= 7 (structural isomorphism, non-trivial)
SUPERFICIAL = score < 7 (surface similarity, metaphor, or obvious)"""


# ── Backends ──────────────────────────────────────────────────────────────────
def call_openai(pair: dict) -> dict:
    try:
        from openai import OpenAI
    except ImportError:
        print(
            "ERROR: openai not installed. Run: uv pip install openai", file=sys.stderr
        )
        sys.exit(1)

    if not OPENAI_KEY:
        print("ERROR: OPENAI_API_KEY not set in environment or .env", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(api_key=OPENAI_KEY)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(pair)},
        ],
        temperature=0.2,
        response_format={"type": "json_object"},
    )
    result = json.loads(response.choices[0].message.content)
    result["model_used"] = "gpt-4o"
    return result


def call_gemini(pair: dict) -> dict:
    try:
        import google.generativeai as genai
    except ImportError:
        print(
            "ERROR: google-generativeai not installed. Run: uv pip install google-generativeai",
            file=sys.stderr,
        )
        sys.exit(1)

    if not GEMINI_KEY:
        print("ERROR: GEMINI_API_KEY not set in environment or .env", file=sys.stderr)
        sys.exit(1)

    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel(
        "gemini-1.5-pro",
        system_instruction=SYSTEM_PROMPT,
        generation_config={
            "temperature": 0.2,
            "response_mime_type": "application/json",
        },
    )
    response = model.generate_content(build_user_prompt(pair))
    result = json.loads(response.text)
    result["model_used"] = "gemini-1.5-pro"
    return result


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="JSON file with pair data (default: stdin)")
    parser.add_argument(
        "--mode",
        choices=["openai", "gemini", "auto"],
        default="auto",
        help="Which model to use (auto = openai if key present, else gemini)",
    )
    args = parser.parse_args()

    # Lê input
    if args.file:
        data = json.loads(Path(args.file).read_text())
    else:
        data = json.loads(sys.stdin.read())

    if "pair" in data:
        pair = data["pair"]
    else:
        pair = data  # aceita o objeto direto também

    required = [
        "article_a",
        "article_b",
        "proposed_connection",
        "connection_type",
        "pearl_level",
    ]
    missing = [f for f in required if f not in pair]
    if missing:
        print(f"ERROR: missing fields: {missing}", file=sys.stderr)
        sys.exit(2)

    # Escolhe modelo
    mode = args.mode
    if mode == "auto":
        mode = "openai" if OPENAI_KEY else "gemini"

    if mode == "openai":
        result = call_openai(pair)
    else:
        result = call_gemini(pair)

    print(json.dumps(result, ensure_ascii=False, indent=2))

    # Exit code reflete veredicto (útil em shell scripts)
    sys.exit(0 if result.get("verdict") == "GENUINE" else 3)


if __name__ == "__main__":
    main()
