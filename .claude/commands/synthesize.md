# /synthesize

Cria artigo wiki com `provenance: emergence` a partir de dois artigos existentes + log de /ask que confirmou a conexão.

## Uso

```
/synthesize [artigo-A] [artigo-B] [ask-session-log]
```

Exemplo:
```
/synthesize requisite-variety complementary-learning-systems outputs/logs/sessions/2026-04-04/ask-14h32.md
```

## Passo 1 — Lê insumos

1. Lê `wiki/concepts/[artigo-A].md`
2. Lê `wiki/concepts/[artigo-B].md`
3. Lê o log de /ask fornecido (ou o mais recente em `outputs/logs/sessions/` se não especificado)
4. Identifica no log: qual pergunta foi feita, qual conexão emergiu, qual foi o nível Pearl da conexão

## Passo 2 — Define nome e escopo do artigo emergido

Nome do artigo: kebab-case descritivo do conceito emergido (não concatenação dos dois nomes).
Escopo: apenas o conceito que não estava em nenhuma das duas fontes individuais.

Se o conceito emergido já existe em algum artigo atual (verificar `_index.md`), não criar — adicionar à seção `## Conexões` dos dois artigos originais.

## Passo 3 — Cria artigo com template de emergence

```markdown
---
title: "[Nome do Conceito Emergido]"
sources:
  - path: wiki/concepts/[artigo-A].md
    type: synthesis
    quality: primary
  - path: wiki/concepts/[artigo-B].md
    type: synthesis
    quality: primary
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
source_quality: medium
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: true
quarantine_created: YYYY-MM-DD
quarantine_reason: "Artigo emergido de /ask cross-domain — aguarda confirmação adversarial e review frio"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
provenance: emergence
emergence_trigger:
  pair: [[artigo-A], [artigo-B]]
  ask_session: [path do log]
  connection_type: ANÁLOGO-A | INSTANCIA | EMERGE-DE
  pearl_level: L1 | L2 | L3
emerged_on: YYYY-MM-DD
---

## Resumo

[2-3 frases descrevendo o conceito emergido — o que não estava em nenhuma fonte individual]

## Conteúdo

### O que [artigo-A] contribui

[mecanismo de A relevante para a conexão]

### O que [artigo-B] contribui

[mecanismo de B relevante para a conexão]

### O que emerge da combinação

[conceito que nenhum dos dois articula individualmente]
[marcar como ⚠️ interpretação do compilador]

## Especulação

- [claims que dependem de validação futura]

## Verificação adversarial

**Pergunta falsificável:** [a pergunta gerada no /emerge ou no /ask]
**Evidência que confirmaria:** [o que precisaria ser verdade]
**Evidência que refutaria:** [o que indicaria que a conexão é ilusória]

## Conexões

- emerge-de: [[artigo-A]] ON "[mecanismo A]"
- emerge-de: [[artigo-B]] ON "[mecanismo B]"

## Fontes

- [[artigo-A]] — [contribuição específica para esta síntese]
- [[artigo-B]] — [contribuição específica para esta síntese]
- [Log /ask](../../[path do log]) — sessão que descobriu a conexão

> ⚠️ QUARENTENA: artigo emergido de /ask cross-domain. Critérios pendentes: tempo (24h), review frio, adversarial.
```

## Passo 4 — Atualiza artigos originais

Nos dois artigos originais (`artigo-A.md` e `artigo-B.md`), adiciona na seção `## Conexões`:

```
- emerge-para: [[novo-artigo]] ON "[mecanismo da conexão descoberta]"
```

## Passo 5 — Atualiza _index.md e _registry.md

Adiciona linha em `_index.md`:
```
- [Nome do Conceito](concepts/novo-artigo.md) — ⚠️ EMERGIDO. [2-3 frases do Resumo]
```

Adiciona linha em `_registry.md`:
```
| wiki/concepts/novo-artigo.md | YYYY-MM-DD | synthesis | primary | neutral | [artigo-A],[artigo-B] | processed |
```

## Notas

- Todo artigo criado via /synthesize começa em quarentena — sem exceção
- `interpretation_confidence: low` por padrão — síntese cross-domain tem mais risco de over-synthesis
- O log de /ask é a única evidência de que a conexão foi confirmada por análise — não por intuição do compilador

---

## Pipeline — kb-state.yaml

### Lê (início)
- `synthesize.pending_from_ask` — se não vazio, use o par registrado (evita duplicação se /ask já registrou a conexão)
- `slow_cycle.emerge.top_pairs` — para verificar se o par veio de uma recomendação de /emerge (ajuda a preencher `emergence_trigger` automaticamente)

### Escreve (final)
```yaml
updated: YYYY-MM-DD
corpus:
  total_articles: +1
  quarantined_articles: +1
  quarantined_list:
    - [novo-artigo]  # append
  provenance_breakdown:
    emergence: +1
synthesize:
  pending_from_ask: []  # remove o par processado
```

### Gatilhos — verifique ao final

| Condição | Gatilho |
|----------|---------|
| Sempre após criação | `💡 Artigo [nome] criado em quarentena. Próximos passos: (1) aguarde 24h, (2) /review em sessão diferente, (3) /challenge ou formule predição falsificável.` |
| Par veio de `emerge_top_pairs` | `💡 /emerge — pare processado. Outros pares em emerge_top_pairs disponíveis para próximo /ask.` |
