#!/usr/bin/env bash
# pdf-to-raw.sh — Converte PDFs com texto em raw/ para .txt.md e remove o PDF original
#
# PDFs escaneados (sem texto selecionável) são PULADOS e preservados como PDF —
# OCR introduz ruído que pode propagar para o wiki. Escaneados ficam no raw/ como PDF.
#
# Uso:
#   ./scripts/pdf-to-raw.sh              # processa todos os PDFs em raw/
#   ./scripts/pdf-to-raw.sh raw/papers/foo.pdf   # processa um PDF específico
#   ./scripts/pdf-to-raw.sh --dry-run    # mostra o que faria sem executar
#
# Resultado: raw/papers/foo.pdf → raw/papers/foo.pdf.txt.md + PDF removido
#
# Dependência: pdftotext (poppler) — brew install poppler

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DRY_RUN=false
SPECIFIC_FILE=""

# PDFs escaneados têm < 100 chars de texto por página em média
SCANNED_THRESHOLD=100

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    *.pdf) SPECIFIC_FILE="$arg" ;;
  esac
done

is_scanned() {
  local pdf="$1"
  local pages
  pages=$(pdfinfo "$pdf" 2>/dev/null | grep "^Pages:" | awk '{print $2}')
  [ -z "$pages" ] || [ "$pages" -eq 0 ] && return 0

  local chars
  chars=$(pdftotext "$pdf" - 2>/dev/null | wc -c)
  local threshold=$((pages * SCANNED_THRESHOLD))
  [ "$chars" -lt "$threshold" ]
}

convert_pdf() {
  local pdf="$1"
  local out="${pdf%.pdf}.pdf.txt.md"
  local base
  base=$(basename "$pdf")
  local size
  size=$(du -sh "$pdf" | cut -f1)
  local pages
  pages=$(pdfinfo "$pdf" 2>/dev/null | grep "^Pages:" | awk '{print $2}' || echo "?")
  local date
  date=$(date +%Y-%m-%d)

  if is_scanned "$pdf"; then
    echo "  PULADO (escaneado): $base ($size, ${pages}p) — PDF preservado"
    return
  fi

  if [ "$DRY_RUN" = true ]; then
    echo "  CONVERTE: $base ($size, ${pages}p) → $(basename "$out") [PDF removido]"
    return
  fi

  echo "  Convertendo: $base ($size, ${pages}p)..."

  {
    printf "# %s — Texto extraído de PDF\n\n" "$base"
    printf "**Metadados da conversão:**\n"
    printf "- Arquivo original: \`%s\`\n" "$base"
    printf "- Tamanho original: %s\n" "$size"
    printf "- Páginas: %s\n" "$pages"
    printf "- Convertido em: %s\n" "$date"
    printf "- Ferramenta: pdftotext (poppler)\n\n"
    printf "---\n\n"
    pdftotext "$pdf" - 2>/dev/null
  } > "$out"

  local out_size
  out_size=$(du -sh "$out" | cut -f1)
  rm "$pdf"
  echo "    ✓ $(basename "$out") ($out_size) — PDF removido"
}

if [ -n "$SPECIFIC_FILE" ]; then
  if [ ! -f "$SPECIFIC_FILE" ]; then
    echo "Arquivo não encontrado: $SPECIFIC_FILE" >&2
    exit 1
  fi
  convert_pdf "$SPECIFIC_FILE"
else
  converted=0
  skipped=0
  while IFS= read -r -d '' pdf; do
    convert_pdf "$pdf"
    # conta baseado no output — simplificado: verifica se .txt.md foi criado
    out="${pdf%.pdf}.pdf.txt.md"
    if [ -f "$out" ]; then
      converted=$((converted + 1))
    else
      skipped=$((skipped + 1))
    fi
  done < <(find "$PROJECT_ROOT/raw" -name "*.pdf" -print0)

  total=$((converted + skipped))
  if [ "$total" -eq 0 ]; then
    echo "Nenhum PDF encontrado em raw/"
  else
    echo ""
    echo "Total: $converted convertido(s), $skipped pulado(s) (escaneado)."
  fi
fi
