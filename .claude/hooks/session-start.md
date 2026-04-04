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

### Check 5 — Propagação indireta de quarentena
Para cada artigo em quarentena:
  Busca artigos LIVRES que o linkam via wikilink.
  Se encontra: "⚠️ [artigo-livre] linka [artigo-quarentena] — claims especulativos podem propagar indiretamente"

### Check 4 — Propagation review
Se `outputs/inbox/propagation-review.md` não vazio:
"🔗 [N] artigos precisam de propagation review"

## Formato
Conciso. Máximo 10 linhas.
Se nada: "✅ KB em bom estado. Nada pendente."

## O que NÃO faz
- Não executa ações
- Não commita
- Não modifica artigos
- Apenas informa e sugere
