# Session Start Hook

## Quando ativa
No início de TODA sessão no llm-kb, antes de qualquer outra ação.

## O que faz

### Check 1 — Quarentena
```bash
grep -r "quarantine: true" wiki/concepts/ wiki/patterns/
```

Para cada artigo em quarentena:
- Tempo: quarantine_created vs hoje → passou 24h?
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

### Check 6 — kb-state

Leia `outputs/state/kb-state.yaml`.

Se `last_updated` é nulo ou tem mais de 7 dias:
  "⚠️ kb-state pode estar desatualizado (última atualização: [data ou 'nunca'])"

Reporte apenas o que tem ação:

- Se `ingest_count_since_last_lint >= 5`:
  "📊 /lint-epistemic recomendado ([N] ingestões)"

- Se `promoted_since_last_emerge` não vazio:
  "🔍 /emerge recomendado — promovidos desde último /emerge: [lista]"

- Se `sessions_since_last_dream >= 5`:
  "💭 /dream recomendado ([N] sessões)"

- Se `emerge_top_pairs` não vazio:
  "🔗 Pares pendentes de /ask: [lista resumida]"

Se todos os campos estão em zero/vazio: silêncio — não reporta nada sobre kb-state.

## Formato
Conciso. Apenas checks com itens aparecem.
Se nada: "✅ KB em bom estado."

## O que NÃO faz
- Não executa ações
- Não commita
- Não modifica artigos
- Não modifica kb-state.yaml
- Apenas informa e sugere
