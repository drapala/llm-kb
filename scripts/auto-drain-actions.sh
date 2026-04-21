#!/usr/bin/env bash
# auto-drain-actions.sh — PostToolUse hook for Write|Edit on kb-state.yaml
# Detecta novas entradas em next_actions após cada write no kb-state.yaml.
# Se encontrar itens novos (sem blocked_by), emite instrução para Claude executar.
#
# Padrão de output: JSON hookSpecificOutput → vira system-reminder → Claude executa.

set -euo pipefail

INPUT=$(/bin/cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null || true)

# Só dispara para kb-state.yaml
[[ "$FILE_PATH" == *"kb-state.yaml" ]] || exit 0

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
KB_STATE="${PROJECT_ROOT}/outputs/state/kb-state.yaml"
SNAPSHOT="/tmp/metaxon-next-actions-$(basename "$PROJECT_ROOT").txt"

[ -f "$KB_STATE" ] || exit 0

# Lê ações não-bloqueadas atuais
CURRENT=$(yq '.next_actions[] | select(.blocked_by == null) | .action' "$KB_STATE" 2>/dev/null | sort || true)

if [ -z "$CURRENT" ]; then
  echo "$CURRENT" > "$SNAPSHOT" 2>/dev/null || true
  exit 0
fi

# Na primeira execução, salva snapshot e sai (sem diff)
if [ ! -f "$SNAPSHOT" ]; then
  echo "$CURRENT" > "$SNAPSHOT"
  exit 0
fi

PREVIOUS=$(cat "$SNAPSHOT")

# Detecta novas ações (presentes agora, ausentes antes)
NEW_ACTIONS=$(comm -13 <(echo "$PREVIOUS" | sort) <(echo "$CURRENT" | sort) 2>/dev/null || true)

# Atualiza snapshot ANTES de emitir (evita re-trigger em escrita subsequente)
echo "$CURRENT" > "$SNAPSHOT"

[ -z "$NEW_ACTIONS" ] && exit 0

# Formata lista compacta (máx 6 ações)
ACTION_LIST=$(echo "$NEW_ACTIONS" | head -6 | awk '{print NR". "$0}' | tr '\n' ' | ' | sed 's/ | $//')
COUNT=$(echo "$NEW_ACTIONS" | wc -l | tr -d ' ')

cat <<EOF
{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"⚡ AUTO-DRAIN: ${COUNT} nova(s) ação(ões) em next_actions. Execute em sequência usando Skill ou Bash:\n${ACTION_LIST}\n\nUse Skill tool para /challenge, /promote, /lint-epistemic. Não pergunte — execute imediatamente."}}
EOF
