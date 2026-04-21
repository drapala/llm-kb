#!/usr/bin/env bash
# bradford-watch.sh — Monitora Zone3/Zone2 ratio e notifica quando itens
# com trigger_condition: bradford_open podem ser ingeridos.
#
# Lógica:
#   - Lê slow_cycle.lint.alerts em kb-state.yaml
#   - Se não há alerta bradford_coverage com value >= 0.8 → Bradford ABERTO
#   - Lista itens bradford_blocked: true em ingest_queue_priority
#   - Escreve outputs/inbox/bradford-unblocked-YYYY-MM-DD.md se houver itens
#
# Uso: bash scripts/bradford-watch.sh [--notify-only]
#   --notify-only: imprime no stdout mas não salva arquivo

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
KB_STATE="${PROJECT_ROOT}/outputs/state/kb-state.yaml"
INBOX="${PROJECT_ROOT}/outputs/inbox"
TODAY=$(date +%Y-%m-%d)

# Prefer venv python (has pyyaml)
PYTHON="${PROJECT_ROOT}/.venv/bin/python3"
[[ -x "$PYTHON" ]] || PYTHON="python3"

NOTIFY_ONLY=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --notify-only) NOTIFY_ONLY=true; shift ;;
    *) shift ;;
  esac
done

[[ -f "$KB_STATE" ]] || { echo "❌ kb-state.yaml não encontrado" >&2; exit 1; }

# --- 1. Checar Bradford status via lint alerts ---
BRADFORD_STATUS=$("$PYTHON" - "$KB_STATE" <<'PYEOF'
import yaml, sys

with open(sys.argv[1]) as f:
    state = yaml.safe_load(f)

alerts = (state.get('slow_cycle', {})
               .get('lint', {})
               .get('alerts', []) or [])

for a in (alerts or []):
    if isinstance(a, dict) and a.get('type') == 'bradford_coverage':
        val = float(a.get('value', 0))
        print(f"PAUSA:{val}" if val >= 0.8 else f"OPEN:{val}")
        sys.exit(0)

print('OPEN_NO_DATA')
PYEOF
)

STATUS_TYPE="${BRADFORD_STATUS%%:*}"
STATUS_VALUE="${BRADFORD_STATUS#*:}"

if [[ "$STATUS_TYPE" == "PAUSA" ]]; then
  echo "📊 Bradford Zone3/Zone2 = ${STATUS_VALUE} → PAUSA. Nenhum item desbloqueado."
  exit 0
fi

# --- 2. Bradford ABERTO — listar itens bloqueados ---
BLOCKED_JSON=$("$PYTHON" - "$KB_STATE" <<'PYEOF'
import yaml, json, sys

with open(sys.argv[1]) as f:
    state = yaml.safe_load(f)

queue = state.get('ingest_queue_priority', []) or []
blocked = [i for i in queue if isinstance(i, dict) and i.get('bradford_blocked') is True]
print(json.dumps(blocked, ensure_ascii=False))
PYEOF
)

BLOCKED_COUNT=$("$PYTHON" -c "import json,sys; print(len(json.loads(sys.argv[1])))" "$BLOCKED_JSON")

if [[ "$BLOCKED_COUNT" -eq 0 ]]; then
  echo "✅ Bradford ${STATUS_TYPE} (${STATUS_VALUE}) — nenhum item bradford_blocked na fila."
  exit 0
fi

echo "🟢 Bradford ABERTO (${STATUS_VALUE}) — ${BLOCKED_COUNT} item(s) prontos para ingestão"

# --- 3. Gerar notificação ---
NOTIFICATION=$("$PYTHON" - "$BLOCKED_JSON" "$STATUS_VALUE" "$TODAY" <<'PYEOF'
import json, sys

items = json.loads(sys.argv[1])
ratio = sys.argv[2]
today = sys.argv[3]

lines = [
    f"# Bradford Desbloqueado — {today}",
    "",
    f"Zone3/Zone2 = {ratio} → aberto para ingestão Zone 3.",
    f"**{len(items)} item(s) com `trigger_condition: bradford_open`:**",
    "",
]

for i, item in enumerate(items, 1):
    lines.append(f"## {i}. {item.get('slug', 'sem-slug')}")
    lines.append(f"- **Artigo afetado:** {item.get('article', '?')}")
    lines.append(f"- **Impacto:** {item.get('impact', '?')}")
    lines.append(f"- **Claim:** {item.get('claim', '?')}")
    if item.get('url'):
        lines.append(f"- **URL:** {item['url']}")
    lines.append(f"- **Adicionado:** {item.get('added_on', '?')} por {item.get('added_by', '?')}")
    lines.append("")

lines += [
    "---",
    "Para ingerir: `/ingest <URL>` para cada item.",
    "Após ingerir, remova `bradford_blocked: true` do item em kb-state.yaml.",
]
print('\n'.join(lines))
PYEOF
)

echo "$NOTIFICATION"

if [[ "$NOTIFY_ONLY" == "false" ]]; then
  mkdir -p "$INBOX"
  OUTFILE="${INBOX}/bradford-unblocked-${TODAY}.md"
  printf '%s\n' "$NOTIFICATION" > "$OUTFILE"
  echo ""
  echo "📝 Notificação salva em: $OUTFILE"
fi
