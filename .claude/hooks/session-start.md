# Session Start Hook

## Quando ativa
No início de TODA sessão no llm-kb, antes de qualquer outra ação.

## O que faz

### Check 0 — Painel de decisão (SEMPRE primeiro)

Leia `outputs/state/kb-state.yaml`.

**`next_actions`** — exibe se não vazio:
```
📋 Próximas ações:
  1. [action] — [why]  [🚫 bloqueado por: X]
  2. ...
```

**`readiness_signal`** — exibe sempre:
```
🟢 Pode ingerir — [stance_status]
🟡 Ingestão com cuidado — [warning]
🔴 Consolide antes de ingerir — [warning]
```
Regra: 🟢 se `can_ingest: true` e sem warning. 🟡 se `can_ingest: true` com warning. 🔴 se `can_ingest: false`.

Se `next_actions` vazio e `readiness_signal` verde: "✅ Sem ações pendentes. KB em bom estado."

---

### Check 1 — Quarentena

```bash
grep -r "quarantine: true" wiki/concepts/ wiki/patterns/
```

Para cada artigo em quarentena:
- Tempo: `quarantine_created` vs hoje → passou 24h?
- Review frio: existe log com data diferente?
- Critério 3: challenge, scout, ou predição?

Output:
- Se pronto: "📋 [artigo] pronto para /promote — todos os critérios satisfeitos"
- Se pendente: "⏳ [artigo] em quarentena — pendente: [critérios]"

### Check 2 — Inbox

```bash
ls outputs/inbox/
```
Se não vazio: "📥 Inbox tem [N] items pendentes"

### Check 3 — Utility flags

Para artigos com `reads >= 5`:
- `utility_score = retrievals_correct / reads`
- Se < 0.3: "⚠️ [artigo] utility baixo ([score]) — /review?"
- Se reads = 0 e last_read: null: "👻 [artigo] nunca lido — remoção ou ponteiro?"

### Check 4 — Propagação indireta de quarentena

Para cada artigo em quarentena:
  Busca artigos LIVRES que o linkam via wikilink.
  Se encontra: "⚠️ [artigo-livre] linka [artigo-quarentena] — claims especulativos podem propagar indiretamente"

### Check 5 — Propagation review

Se `outputs/inbox/propagation-review.md` não vazio:
"🔗 [N] artigos precisam de propagation review"

### Check 6 — kb-state (contadores)

Reporte apenas o que tem ação:

- Se `ingest_count_since_last_lint >= 5`:
  "📊 /lint-epistemic recomendado ([N] ingestões)"

- Se `emerge_queue` tem >= 3 itens:
  "🔍 /emerge recomendado — [N] artigos na fila"

- Se `sessions_since_last_dream >= 5`:
  "💭 /dream recomendado ([N] sessões)"

- Se `emerge_top_pairs` não vazio:
  "🔗 Pares pendentes de /ask: [lista resumida]"

- Se `last_updated` tem mais de 7 dias:
  "⚠️ kb-state pode estar desatualizado (última atualização: [data])"

Se `next_actions` tem itens com `blocked_by: null`:
  "▶ /auto disponível — executa [N] ações automaticamente sem confirmação"

## Formato
Conciso. Check 0 sempre aparece. Checks 1-6 apenas se têm itens.

## O que NÃO faz
- Não executa ações
- Não commita
- Não modifica artigos
- Não modifica kb-state.yaml
- Apenas informa e sugere
