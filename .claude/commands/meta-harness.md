# /meta-harness

Analisa logs de sessão e propõe ou aplica patches mínimos nos comandos da KB.

## Contexto

Esta KB é mantida via comandos em `.claude/commands/`. Logs de sessão em `outputs/logs/sessions/` registram feedback, invalidações Gate 3, SPLITs e quarentenas. Eventos de atrito operacional ficam em `raw/meta/ops/friction-*.md`.

## Pipeline

### STEP 1 — SCAN

**1A — Session logs**

Leia todos os arquivos em `outputs/logs/sessions/` (glob: `outputs/logs/sessions/**/*.md`).

Para cada log de sessão, extraia:
- Eventos de feedback (correções de comportamento da KB, problemas de pipeline)
- Invalidações Gate 3 (fontes rejeitadas com motivo)
- Eventos SPLIT (discordâncias do oracle ainda abertas)
- Eventos de quarentena (artigos quarentenados, motivos)

Monte lista A: `session_date`, `event_type`, `description`, `affected_command`.

**1B — Friction files**

Leia todos os arquivos em `raw/meta/ops/friction-*.md`.

Para cada friction file, extraia:
- `type` (friction | workaround | wish)
- `surface` (ingest | ask | promote | emerge | quarantine | kb-state | other)
- `severity` (low | medium | high)
- `tags` (lista)
- Descrição do evento (corpo do arquivo)

Monte lista B: `date`, `friction_type`, `surface`, `severity`, `tags`, `description`.

**Mapeamento surface → command:**
```
ingest      → .claude/commands/ingest.md
ask         → .claude/commands/ask.md
promote     → .claude/commands/promote.md + auto-promote.md
emerge      → .claude/commands/emerge.md
quarantine  → .claude/commands/challenge.md + auto-promote.md
kb-state    → outputs/state/kb-state.yaml (estrutura) ou dream.md (visibilidade)
other       → avaliar pela descrição
```

**Severity → severity_score para PATTERN:**
```
high   → 3
medium → 2
low    → 1
```

### STEP 2 — PATTERN

**2A — Padrões de session logs** (lista A)

Agrupe por `(event_type + affected_command + similaridade de descrição)`.

```
weight = (session_count × 2) + severity_score
severity: crítico=3, recorrente=2, pontual=1
```

Padrão confirmado se `weight ≥ 6` (requer 3+ sessões).

**2B — Padrões de friction** (lista B)

Agrupe por `(surface + tags_overlap ≥ 2)`.

```
weight = (friction_count × 2) + sum(severity_scores)
```

Padrão confirmado se `weight ≥ 4` (threshold menor — friction é sinal mais direto que log).

Um único evento `high` já vale weight=3; dois eventos `medium` no mesmo surface valem weight=6.

**2C — Cross-signal:** se um padrão de friction confirma um padrão de log no mesmo surface/command → eleva weight do padrão de log em +2.

### STEP 3 — PATCH

Para cada padrão confirmado:
- Identifique o arquivo em `.claude/commands/` responsável
- Leia o arquivo
- Gere patch mínimo como bloco `[!patch]`
- Calcule elegibilidade para auto-apply:

**AUTO-APPLY** somente se TODOS verdadeiros:
- ✓ patch é aditivo (adiciona instrução, não remove texto existente)
- ✓ patch não altera gates existentes
- ✓ patch não afeta `epistemic_status` de artigos já promovidos
- ✓ padrão apareceu em 5+ sessões distintas
- ✓ nenhum SPLIT aberto sobre o domínio do patch

**ESCALAR** se QUALQUER verdadeiro:
- ✗ patch remove ou modifica instrução existente
- ✗ patch afeta gate de promoção
- ✗ patch contradiz artigo L1 existente
- ✗ padrão tem SPLIT aberto
- ✗ elegibilidade é ambígua

### STEP 4 — APPLY

- **Auto-apply:** aplica direto no arquivo com Edit.
- **Escalação:** escreve patch proposto só no output — NÃO edita nenhum arquivo.

### STEP 5 — OUTPUT

Escreva relatório em `outputs/meta-harness/YYYY-MM-DD.md` (data de hoje).
Crie `outputs/meta-harness/` se não existir.

```markdown
---
date: YYYY-MM-DD
sessions_scanned: N
friction_files_scanned: N
patterns_found: N
patches_applied: N
patches_escalated: N
---

## Padrões de Session Logs
[cada: descrição, weight, sessões de evidência, comando afetado]

## Padrões de Friction
[cada: surface, tags recorrentes, weight, N eventos, descrição do padrão]
[se cross-signal com log pattern: nota de correlação]

## Patches aplicados automaticamente
[cada: diff, justificativa, checklist de elegibilidade]

## Patches aguardando aprovação humana
[cada: bloco de patch proposto, motivo da escalação, urgência]
[indicar origem: session_log | friction | cross-signal]

## Próxima execução recomendada
[data + trigger note]
```

## Invariantes — NUNCA viola

- NUNCA aplica patch que afeta `/promote` ou gates de promoção
- NUNCA aplica patch sem 5+ sessões de evidência
- NUNCA remove instrução existente automaticamente
- SEMPRE gera log auditável de cada decisão
- SEMPRE escala quando incerto — padrão é escalar, não aplicar

Se menos de 3 sessões estiverem logadas, escreve relatório indicando dados insuficientes e encerra. Não inventa padrões.
