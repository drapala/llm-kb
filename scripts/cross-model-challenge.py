#!/usr/bin/env python3
"""
cross-model-challenge.py — Oracle externo para validação de pares emergentes.

Resolve o Pilar 1 do autoresearch-reliability-triad: requer unanimidade entre
GPT-5.4 Thinking (OpenAI) e Gemini 3.1 Pro Preview (Google) para validar
uma conexão como estrutural (genuína) vs. superficial (analogia enganosa).

Design epistêmico:
- Thinking models para multi-hop reasoning, não apenas pattern matching
- Unanimidade obrigatória: ambos GENUINE para passar (threshold >= 7 cada)
- Claim isolado: judges recebem apenas mecanismos abstratos + claim, sem
  títulos de artigos nem contexto da KB — evita anchoring (ver curse-of-knowledge)
- Training data overlap mitigation: dar o mesmo contexto do wiki voltaria
  ao bias que o oracle deve prevenir

Uso:
  echo '{"pair": {...}}' | python3 scripts/cross-model-challenge.py
  python3 scripts/cross-model-challenge.py --file /tmp/pair.json
  python3 scripts/cross-model-challenge.py --mode openai --file /tmp/pair.json
  python3 scripts/cross-model-challenge.py --mode gemini --file /tmp/pair.json

Input JSON (stdin ou --file):
{
  "mechanism_a": "...",            # X causa Y via Z (sem título, sem resumo do artigo)
  "mechanism_b": "...",            # análogo em domínio diferente
  "proposed_connection": "...",    # o claim estrutural isolado
  "connection_type": "ANÁLOGO-A | INSTANCIA | EMERGE-DE",
  "pearl_level": "L1 | L2 | L3"
}

Compatibilidade retroativa: se "article_a"/"article_b" presentes, extrai
apenas o campo "mechanism" de cada um.

Output JSON (stdout) — modo unanimous:
{
  "verdict": "GENUINE | SUPERFICIAL | SPLIT",
  "unanimous": true|false,
  "openai": { "score": 1-10, "verdict": "...", "reasoning": "...", ... },
  "gemini":  { "score": 1-10, "verdict": "...", "reasoning": "...", ... }
}

Output JSON (stdout) — modo single:
{
  "score": 1-10,
  "verdict": "GENUINE | SUPERFICIAL",
  "reasoning": "...",
  "model_used": "gpt-5.4 | gemini-3.1-pro-preview",
  "confidence": "high | medium | low"
}

Exit codes:
  0 — GENUINE (unanimous) ou GENUINE (single)
  1 — erro de API ou configuração
  2 — input inválido
  3 — SUPERFICIAL ou SPLIT

Dependências: openai>=1.0, google-genai>=1.0
  uv pip install openai google-genai
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
SYSTEM_PROMPT = """You are an epistemologist evaluating structural isomorphisms between
causal mechanisms from different domains.

You receive only abstract mechanism descriptions and a proposed structural claim.
You have NO access to the source articles, knowledge base, or any named context.
This isolation is intentional — you are the external oracle, evaluating the claim
in a vacuum to prevent anchoring to source material."""


def build_user_prompt(pair: dict) -> str:
    return f"""Evaluate whether this proposed structural claim represents a genuine
causal isomorphism or a superficial analogy.

MECHANISM A (domain 1):
{pair["mechanism_a"]}

MECHANISM B (domain 2):
{pair["mechanism_b"]}

PROPOSED STRUCTURAL CLAIM:
{pair["proposed_connection"]}
Connection type: {pair["connection_type"]}
Pearl causal level claimed: {pair["pearl_level"]}

Evaluate:
1. Do mechanisms A and B share the same causal skeleton (same variables, same
   dependency structure, same feedback loops) in structurally independent domains?
   Or are they connected only by surface similarity / shared metaphor?
2. Would domain experts in BOTH fields recognize this as a non-trivial insight
   that neither domain alone would generate?
3. Is the Pearl level ({pair["pearl_level"]}) appropriate? L2 requires intervention
   structure; L3 requires counterfactual. L1 (correlation) does not qualify as
   structural isomorphism.

Respond ONLY with valid JSON (no markdown, no explanation outside JSON):
{{
  "score": <integer 1-10>,
  "verdict": "<GENUINE or SUPERFICIAL>",
  "reasoning": "<2-3 sentences — must specify which structural elements match or diverge>",
  "confidence": "<high|medium|low>",
  "pearl_level_appropriate": <true|false>,
  "main_concern": "<null or one-line concern>"
}}

GENUINE = score >= 7 (tight causal isomorphism, non-trivial, independent domains)
SUPERFICIAL = score < 7 (shared metaphor, loose analogy, or obvious connection)"""


def extract_mechanisms(data: dict) -> dict:
    """Normaliza input: aceita formato legado (article_a/b) ou novo (mechanism_a/b)."""
    if "mechanism_a" in data:
        return data

    pair = data.get("pair", data)

    # Compatibilidade com formato legado
    a = pair.get("article_a", {})
    b = pair.get("article_b", {})
    return {
        "mechanism_a": a.get("mechanism", a.get("summary", "")),
        "mechanism_b": b.get("mechanism", b.get("summary", "")),
        "proposed_connection": pair.get("proposed_connection", ""),
        "connection_type": pair.get("connection_type", ""),
        "pearl_level": pair.get("pearl_level", ""),
    }


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
        model="gpt-5.4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(pair)},
        ],
        reasoning_effort="high",
        response_format={"type": "json_object"},
    )
    result = json.loads(response.choices[0].message.content)
    result["model_used"] = "gpt-5.4"
    return result


def call_gemini(pair: dict) -> dict:
    try:
        from google import genai
        from google.genai import types as genai_types
    except ImportError:
        print(
            "ERROR: google-genai not installed. Run: uv pip install google-genai",
            file=sys.stderr,
        )
        sys.exit(1)

    if not GEMINI_KEY:
        print("ERROR: GEMINI_API_KEY not set in environment or .env", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=GEMINI_KEY)
    response = client.models.generate_content(
        model="gemini-3.1-pro-preview",
        contents=build_user_prompt(pair),
        config=genai_types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            thinking_config=genai_types.ThinkingConfig(thinking_budget=8192),
            response_mime_type="application/json",
        ),
    )
    result = json.loads(response.text)
    result["model_used"] = "gemini-3.1-pro-preview"
    return result


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="JSON file with pair data (default: stdin)")
    parser.add_argument(
        "--mode",
        choices=["openai", "gemini", "unanimous"],
        default="unanimous",
        help="unanimous (default) = both must agree GENUINE; single model otherwise",
    )
    args = parser.parse_args()

    raw = sys.stdin.read() if not args.file else Path(args.file).read_text()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON — {e}", file=sys.stderr)
        sys.exit(2)

    pair = extract_mechanisms(data)

    required = [
        "mechanism_a",
        "mechanism_b",
        "proposed_connection",
        "connection_type",
        "pearl_level",
    ]
    missing = [f for f in required if not pair.get(f)]
    if missing:
        print(f"ERROR: missing or empty fields: {missing}", file=sys.stderr)
        sys.exit(2)

    if args.mode == "openai":
        result = call_openai(pair)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result.get("verdict") == "GENUINE" else 3)

    if args.mode == "gemini":
        result = call_gemini(pair)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result.get("verdict") == "GENUINE" else 3)

    # ── Unanimous mode ────────────────────────────────────────────────────────
    openai_result = call_openai(pair)
    gemini_result = call_gemini(pair)

    unanimous = (
        openai_result.get("verdict") == "GENUINE"
        and gemini_result.get("verdict") == "GENUINE"
    )

    if unanimous:
        final_verdict = "GENUINE"
    elif (
        openai_result.get("verdict") == "SUPERFICIAL"
        and gemini_result.get("verdict") == "SUPERFICIAL"
    ):
        final_verdict = "SUPERFICIAL"
    else:
        final_verdict = "SPLIT"

    output = {
        "verdict": final_verdict,
        "unanimous": unanimous,
        "openai": openai_result,
        "gemini": gemini_result,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    sys.exit(0 if unanimous else 3)


if __name__ == "__main__":
    main()
