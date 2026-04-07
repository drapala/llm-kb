# /meta-harness

Analisa logs de sessão e propõe ou aplica patches mínimos nos comandos da KB.

## Contexto

Esta KB é mantida via comandos em `.claude/commands/`. Logs de sessão em `outputs/logs/sessions/` registram feedback, invalidações Gate 3, SPLITs e quarentenas por sessão.

## Pipeline

### STEP 1 — SCAN

Leia todos os arquivos em `outputs/logs/sessions/` (glob: `outputs/logs/sessions/**/*.md`).

Para cada log de sessão, extraia:
- Eventos de feedback (correções de comportamento da KB, problemas de pipeline)
- Invalidações Gate 3 (fontes rejeitadas com motivo)
- Eventos SPLIT (discordâncias do oracle ainda abertas)
- Eventos de quarentena (artigos quarentenados, motivos)

Monte lista: `session_date`, `event_type`, `description`, `affected_command`.

### STEP 2 — PATTERN

Agrupe eventos por `(event_type + affected_command + similaridade de descrição)`.

Para cada grupo:
```
weight = (session_count × 2) + severity_score
severity: crítico=3, recorrente=2, pontual=1
```

Padrão **confirmado** se `weight ≥ 6` (requer 3+ sessões distintas).

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
patterns_found: N
patches_applied: N
patches_escalated: N
---

## Padrões identificados
[cada: descrição, weight, sessões de evidência, comando afetado]

## Patches aplicados automaticamente
[cada: diff, justificativa, checklist de elegibilidade]

## Patches aguardando aprovação humana
[cada: bloco de patch proposto, motivo da escalação, urgência]

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
