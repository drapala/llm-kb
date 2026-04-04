# /draft-post

Gera rascunho de post a partir de artigo com `provenance: emergence` que foi promovido da quarentena.
Condição de ativação: artigo tem `quarantine: false` E `provenance: emergence`.

## Uso

```
/draft-post [artigo]
```

Exemplo:
```
/draft-post reflexion-weighted-knowledge-graphs
```

## Passo 1 — Verifica elegibilidade

Lê `wiki/concepts/[artigo].md`. Verifica:
- `quarantine: false` → se ainda em quarentena, aborta: "Artigo ainda em quarentena. Promova primeiro."
- `provenance: emergence` → se não for emergence, aborta: "Artigo não é emergido. /draft-post aplica-se apenas a artigos com provenance: emergence."
- `emergence_trigger` preenchido → se ausente, aborta: "emergence_trigger não encontrado. Rode /synthesize antes."

## Passo 2 — Check anti-paramétrico

**Esta é a etapa mais importante.** Determina se o insight é original ou está no training data do modelo.

Pergunta a si mesmo:
> "Se eu mandasse a seguinte pergunta a um LLM genérico sem acesso a esta KB, ele chegaria nesta conexão?"

A pergunta de teste é: o conceito emergido, formulado em linguagem neutra sem revelar os dois artigos de origem.

Critérios de classificação:

**Paramétrico** (insight já existe no training data):
- A conexão entre os domínios é conhecida na literatura acadêmica
- Um LLM genérico formularia a mesma conexão com linguagem similar
- A contribuição da KB é apenas ter compilado — não ter descoberto

**Original** (insight emergiu da KB):
- A conexão específica não é encontrável numa busca simples
- Requer ter lido os dois artigos e seu contexto nesta KB
- O nível Pearl é L2 ou L3 (não apenas associação)

Se **paramétrico**:
- Salva em `outputs/inbox/parametric-insights.md`:
  ```
  ## [artigo] — YYYY-MM-DD
  Classificação: paramétrico
  Razão: [por que o insight já existe no training data]
  Valor de publicar: baixo (compilação, não descoberta)
  Alternativa: usar como contexto em post sobre [tema maior]
  ```
- Não gera rascunho de post.
- Documenta e encerra.

Se **original**: continua para Passo 3.

## Passo 3 — Lê insumos

1. Lê o artigo emergido completo
2. Lê os dois artigos de `emergence_trigger.pair`
3. Lê o log de /ask em `emergence_trigger.ask_session` (grep pelos 50 tokens centrais se arquivo grande)
4. Verifica `pearl_level` e `connection_type` no `emergence_trigger`

## Passo 4 — Gera rascunho

Salva em `outputs/drafts/[artigo]-post.md`:

```markdown
---
artigo_origem: wiki/concepts/[artigo].md
provenance: emergence
pearl_level: [L1/L2/L3]
status: rascunho
criado: YYYY-MM-DD
publicar: false
---

# [Título sugerido]
[Título que comunica o insight sem jargão interno da KB]

## O insight
[O conceito emergido em 2-3 parágrafos — o que a KB descobriu]

## Como chegamos aqui
[O processo: dois artigos que não se citavam, o /ask que conectou, o que a combinação revelou]
[Transparência epistêmica: não é dedução — é descoberta emergente]

## Por que não é óbvio
[Evidência de originalidade: por que a conexão não aparece na literatura padrão]
[O que você precisava ter lido para chegar aqui]

## Predição falsificável
[Se o insight for correto, o que deveria ser observável?]
[Formulado como claim testável, não como afirmação]

## Limitações
[O que esta conexão não explica]
[Onde o isomorfismo quebra]

---
*Insight emergido de KB pessoal via /ask cross-domain.
Artigos de origem: [[artigo-A]] × [[artigo-B]].*
```

## Passo 5 — Nota final

Após salvar o rascunho, imprime:

```
Rascunho salvo em outputs/drafts/[artigo]-post.md

Check anti-paramétrico: ORIGINAL
Pearl level: [nível]

Antes de publicar:
- [ ] Leia o rascunho frio (sessão diferente desta)
- [ ] Verifique se a predição falsificável sobrevive a um /challenge
- [ ] Confirme que a conexão não aparece em busca simples
```

## Notas

- NUNCA publica automaticamente — apenas gera rascunho
- A decisão de publicar é sempre humana
- O check anti-paramétrico é o passo mais valioso — sem ele, você publica compilação como descoberta
- Posts com `pearl_level: L3` têm prioridade de publicação — contrafactuais são os mais raros

---

## Pipeline — kb-state.yaml

### Lê (início)
- `promote.promoted_since_last_draft_scan` — artigos promovidos desde o último draft scan: filtre por `provenance: emergence` para identificar elegíveis
- `corpus.quarantined_list` — verificação de elegibilidade (artigo deve estar fora da lista)

### Escreve (final)
```yaml
updated: YYYY-MM-DD
promote:
  promoted_since_last_draft_scan: []  # reset após processar todos elegíveis
```

Se insight classificado como paramétrico:
```yaml
# Nenhuma escrita adicional — apenas gera entrada em outputs/inbox/parametric-insights.md
```

Se rascunho gerado:
```yaml
# Nenhuma escrita adicional em kb-state — rascunho em outputs/drafts/[artigo]-post.md
# O operador decide o que fazer com o rascunho
```

### Gatilhos — verifique ao final

| Condição | Gatilho |
|----------|---------|
| Rascunho gerado com `pearl_level: L2` | `💡 Rascunho pronto. Leia frio em outra sessão antes de publicar.` |
| Insight classificado como paramétrico | `💡 Insight paramétrico arquivado. Considere usá-lo como contexto em post sobre tema maior, não como descoberta.` |
| `promoted_since_last_draft_scan` ainda tem artigos elegíveis não processados | `💡 Mais artigos elegíveis para /draft-post: [lista restante].` |
