#!/usr/bin/env bash
# watch-check.sh — Verifica tópicos de watch e escreve inbox se houver material novo.
#
# Lógica:
#   1. Lê outputs/state/watch-topics.yaml
#   2. Para cada tópico ativo e com check due (conforme frequência):
#      - Invoca `claude -p` com prompt de check (usa WebSearch nativo)
#      - Claude compara resultados com baseline salvo
#      - Se material novo: escreve outputs/inbox/watch-<slug>-YYYY-MM-DD.md
#   3. Atualiza last_check no watch-topics.yaml
#
# Uso: bash scripts/watch-check.sh [<slug>]
#   <slug>: verifica apenas esse tópico (ignora frequência / last_check)
#   sem argumento: verifica todos os tópicos com check due
#
# Dependências:
#   - claude CLI no PATH (Claude Code)
#   - python3 + pyyaml (.venv/bin/python3 preferido)
#   - yq (para atualizar yaml)

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WATCH_TOPICS="${PROJECT_ROOT}/outputs/state/watch-topics.yaml"
INBOX="${PROJECT_ROOT}/outputs/inbox"
WATCH_DIR="${PROJECT_ROOT}/outputs/watch"
TODAY=$(date +%Y-%m-%d)
TARGET_SLUG="${1:-}"

PYTHON="${PROJECT_ROOT}/.venv/bin/python3"
[[ -x "$PYTHON" ]] || PYTHON="python3"

[[ -f "$WATCH_TOPICS" ]] || { echo "❌ watch-topics.yaml não encontrado" >&2; exit 1; }

command -v claude >/dev/null 2>&1 || {
  echo "❌ claude CLI não encontrado no PATH. Instale Claude Code." >&2
  exit 1
}

mkdir -p "$INBOX" "$WATCH_DIR"

# --- 1. Selecionar tópicos a verificar ---
TOPICS_JSON=$("$PYTHON" - "$WATCH_TOPICS" "$TODAY" "$TARGET_SLUG" <<'PYEOF'
import yaml, json, sys
from datetime import date, timedelta

topics_file = sys.argv[1]
today = date.fromisoformat(sys.argv[2])
target_slug = sys.argv[3] if len(sys.argv) > 3 else ""

with open(topics_file) as f:
    data = yaml.safe_load(f)

topics = data.get('topics', []) or []
to_check = []

for t in topics:
    if not t.get('active', True):
        continue
    slug = t.get('slug', '')

    # Se slug específico fornecido, só processa ele
    if target_slug and slug != target_slug:
        continue

    # Verificar se check é due (ignorar se slug específico)
    if not target_slug:
        last = t.get('last_check')
        freq = t.get('frequency', 'weekly')
        if last:
            last_date = date.fromisoformat(str(last))
            delta = timedelta(days=7 if freq == 'weekly' else 30)
            if today - last_date < delta:
                continue  # ainda não está na hora

    to_check.append({
        'slug': slug,
        'topic': t.get('topic', slug),
        'queries': t.get('queries', [t.get('query', slug)]),
        'baseline': t.get('baseline', f'outputs/watch/{slug}-baseline.md'),
        'frequency': t.get('frequency', 'weekly'),
    })

print(json.dumps(to_check, ensure_ascii=False))
PYEOF
)

COUNT=$("$PYTHON" -c "import json,sys; print(len(json.loads(sys.argv[1])))" "$TOPICS_JSON")

if [[ "$COUNT" -eq 0 ]]; then
  echo "✅ Nenhum tópico com check due em ${TODAY}."
  exit 0
fi

echo "🔍 ${COUNT} tópico(s) para verificar em ${TODAY}"

# --- 2. Para cada tópico, invocar claude check ---
"$PYTHON" - "$TOPICS_JSON" "$PROJECT_ROOT" "$TODAY" <<'PYEOF'
import json, sys, subprocess, os
from pathlib import Path

topics = json.loads(sys.argv[1])
root = Path(sys.argv[2])
today = sys.argv[3]

for t in topics:
    slug = t['slug']
    topic = t['topic']
    queries = t['queries']
    baseline_path = root / t['baseline']
    inbox_file = root / 'outputs' / 'inbox' / f"watch-{slug}-{today}.md"

    print(f"\n{'='*60}")
    print(f"🔍 Checking: {slug}")
    print(f"   Topic: {topic}")

    # Ler baseline se existir
    baseline_content = ""
    if baseline_path.exists():
        baseline_content = baseline_path.read_text()[:3000]  # primeiros 3000 chars
        print(f"   Baseline: {baseline_path.name} ({len(baseline_content)} chars lidos)")
    else:
        print(f"   ⚠️  Baseline não encontrado — check gerará baseline inicial")

    # Montar prompt para claude
    queries_text = "\n".join(f"- {q}" for q in queries)
    baseline_section = f"""
## Baseline existente (resumo)
```
{baseline_content}
```
""" if baseline_content else "## Baseline: não existe ainda — este será o primeiro check."

    prompt = f"""You are running an automated watch check for the METAXON knowledge base.

## Watch Topic
Slug: {slug}
Topic: {topic}

## Search Queries to Execute
{queries_text}

## Task
1. Run WebSearch for each query above (2-3 searches total)
2. If WebSearch returns fewer than 3 relevant results or results are mostly snippets without useful content,
   fall back to tavily_search (mcp__tavily__tavily_search) for richer content extraction
3. Compare results against the baseline below
4. Identify genuinely NEW material (new papers, new rulings, new datasets, new benchmarks)
5. Ignore: blog posts without data, republished content, social media, obvious duplicates

{baseline_section}

## Output Rules
- If NEW material found: output a markdown report starting with exactly "# WATCH ALERT"
- If NO new material: output exactly one line: "NO_NEW_MATERIAL"
- WATCH ALERT format:
  # WATCH ALERT — {slug} — {today}
  **Topic:** {topic}
  **New findings:**
  [list each new item with: title, URL, date if known, 1-2 sentence relevance]
  **Recommended action:** /ingest <url> | monitor | skip
  **Queries used:** [list]

Be conservative: only report material that a researcher would consider genuinely new and relevant.
Do NOT report duplicates of what's in the baseline."""

    # Invocar claude --print com o prompt
    try:
        result = subprocess.run(
            ['claude', '--print', '--allowedTools', 'WebSearch,mcp__tavily__tavily_search'],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=str(root)
        )
        output = result.stdout.strip()

        if result.returncode != 0:
            print(f"   ❌ claude falhou (exit {result.returncode}): {result.stderr[:200]}")
            continue

        if output == "NO_NEW_MATERIAL" or not output.startswith("# WATCH ALERT"):
            print(f"   ✓ Sem material novo")
        else:
            inbox_file.write_text(output + "\n")
            print(f"   🆕 Material novo encontrado!")
            print(f"   📝 Escrito em: {inbox_file.name}")
            # Contar itens novos (aprox)
            new_count = output.count("\n- ") + output.count("\n### ")
            print(f"   ~{new_count} item(s) novo(s)")

    except subprocess.TimeoutExpired:
        print(f"   ⏱️ Timeout (120s) — tópico {slug} ignorado nesta rodada")
    except Exception as e:
        print(f"   ❌ Erro: {e}")
PYEOF

# --- 3. Atualizar last_check no watch-topics.yaml ---
"$PYTHON" - "$WATCH_TOPICS" "$TODAY" "$TOPICS_JSON" <<'PYEOF'
import yaml, sys, json
from pathlib import Path

topics_file = Path(sys.argv[1])
today = sys.argv[2]
checked_slugs = {t['slug'] for t in json.loads(sys.argv[3])}

with open(topics_file) as f:
    data = yaml.safe_load(f)

for t in data.get('topics', []):
    if t.get('slug') in checked_slugs:
        t['last_check'] = today

# Reescrever preservando estrutura (sem yaml.dump que destrói comentários)
# Usar yq para update seguro
import subprocess
for slug in checked_slugs:
    subprocess.run(
        ['yq', '-i', f'.topics[] |= if .slug == "{slug}" then .last_check = "{today}" else . end',
         str(topics_file)],
        check=False  # não crítico
    )

print(f"\n✅ last_check atualizado para: {', '.join(checked_slugs)}")
PYEOF

echo ""
echo "🏁 Watch check concluído — ${TODAY}"
echo "   Inbox: ${INBOX}/"
echo "   Arquivos watch-*.md serão detectados na próxima sessão METAXON."
