# /auto

Executa a fila `next_actions` do kb-state.yaml sem esperar confirmação humana.
Delega decisões epistêmicas ao oracle externo (cross-model-challenge.py) em vez de ao operador.

## Pré-condições

```bash
# Verifica que o oracle externo está disponível
python3 scripts/cross-model-challenge.py --help
```

Se falhar: instale dependências com `uv pip install openai google-generativeai python-dotenv`
e configure `.env` com as chaves (ver `.env.example`).

## Passo 1 — Lê fila

Lê `outputs/state/kb-state.yaml`:
- `next_actions` — fila de ações em ordem de prioridade
- `readiness_signal` — estado do domínio (bloqueia /ingest se `can_ingest: false`)

Exibe:
```
/auto iniciando — N ações na fila
readiness: [status do readiness_signal]
```

## Passo 2 — Executa cada ação

Para cada item em `next_actions` (em ordem de `priority`), verifica `blocked_by`:

- Se `blocked_by` não nulo: pula e registra como "bloqueado — [razão]"
- Se `blocked_by` nulo: executa conforme tipo de ação abaixo

### Ações automáticas (executa sem pausa)

**`/promote [artigo]`**
Verifica os 3 critérios mecanicamente:
1. `quarantine_created` vs hoje → >= 24h?
2. Existe `outputs/logs/sessions/review-[artigo]-*.md` com data diferente?
3. Artigo tem `## Verificação adversarial` com L2+ OU existe `challenge-[artigo]-*.md`?
Se todos satisfeitos → promove (atualiza frontmatter, remove aviso, escreve log).
Se algum falha → registra "critério N não satisfeito" e passa para próxima ação.

**`/challenge [artigo]`**
Executa /challenge completo (lê artigo, avalia claims, web search de prior work).
Atualiza kb-state.yaml e next_actions com resultado.

**`/ingest [fonte]`**
Executa /ingest da fonte indicada no `why` ou `ingest_queue_priority`.
Requer que `readiness_signal.can_ingest == true`.

**`/lint-epistemic`**
Executa lint completo. Atualiza `readiness_signal`.

**`/dream`**
Executa consolidação de memória.

### Ações com oracle externo (executa + valida com cross-model)

**`/emerge`**
1. Executa /emerge normalmente (Passos 1-5 do comando)
2. Para cada par candidato gerado, chama o oracle externo:

```bash
python3 scripts/cross-model-challenge.py --mode auto << 'EOF'
{
  "article_a": {"title": "...", "summary": "...", "mechanism": "..."},
  "article_b": {"title": "...", "summary": "...", "mechanism": "..."},
  "proposed_connection": "...",
  "connection_type": "ANÁLOGO-A",
  "pearl_level": "L2"
}
EOF
```

3. Par entra em `emerge_top_pairs` apenas se oracle retorna `score >= 7` (GENUINE)
4. Pares com score < 7 são registrados em `outputs/reports/emerge-rejected-YYYY-MM-DD.md`
   com o reasoning do oracle — útil para entender o que a KB tende a confundir

### Ações que /auto NÃO executa

- `/ask` — requer pergunta específica do operador
- `/dream` em contexto > 70% — avisa e para
- `/retro` — requer acumulação de friction events (>= 10)
- `/propose` — requer padrão identificado pelo /retro

## Passo 3 — Log e atualização

Após executar todas as ações da fila:

1. Remove ações concluídas de `next_actions`
2. Registra ações bloqueadas com razão
3. Salva log em `outputs/logs/sessions/YYYY-MM-DD/auto-HH-MM.md`:

```markdown
---
date: YYYY-MM-DD
actions_executed: N
actions_blocked: N
oracle_calls: N
oracle_genuine: N
oracle_superficial: N
---

## Executadas
- /promote autoresearch-reliability-triad — ✅ promovido
- /challenge autonomous-kb-failure-modes — PUBLICÁVEL (2/3 claims sobreviveram)

## Bloqueadas
- /emerge — bloqueado por: autonomous-kb-failure-modes ainda em quarentena

## Oracle externo (cross-model)
[resultados de cada chamada ao cross-model-challenge.py]
```

4. Atualiza `last_updated` em kb-state.yaml

## Passo 4 — Relatório terminal

```
/auto completo — YYYY-MM-DD HH:MM

Executadas: N ações
  - [lista]
Bloqueadas: N ações
  - [lista com razão]
Oracle: N chamadas — N genuínas, N superficiais

Próximas ações restantes: N
  1. [action] — [why]
```

## Frequência recomendada

- Início de cada sessão de trabalho real (não de manutenção da KB)
- Antes de qualquer /ask ou /prioritize
- Automaticamente quando `next_actions` tem >= 3 itens com `blocked_by: null`
