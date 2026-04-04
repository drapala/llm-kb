---
title: "Utility Tracker Setup Report"
date: 2026-04-04
---

# Utility Tracker Setup

## 1. FRONTMATTER ADICIONADO

- 19 artigos modificados (todos em wiki/concepts/)
- 19 já tinham frontmatter (campos adicionados dentro do bloco existente)
- 0 criados do zero
- Campos: reads:0, retrievals_correct:0, retrievals_gap:0, last_read:null

## 2. ARQUIVOS CRIADOS/ATUALIZADOS

- .claude/hooks/utility-tracker.md ✓ (3 passos: reads, correct, gap)
- .claude/commands/ask.md atualizado ✓ (utility tracking section)
- .claude/commands/scout.md atualizado ✓ (utility analysis table)

## 3. ESTADO INICIAL DA KB — Top 5 por utility_score estimado após 30 sessões

| # | Artigo | Utility estimado | Justificativa |
|---|--------|-----------------|---------------|
| 1 | agent-memory-architectures | Alto | Hub central (10+ inbound links). Qualquer pergunta sobre memory systems passa por aqui. |
| 2 | retrieval-augmented-generation | Alto | Fundacional — RAG vs LC é a pergunta mais frequente do domínio. 4 fontes primary. |
| 3 | llm-as-judge | Alto | Qualquer pergunta sobre qualidade/bias referencia biases. 5 fontes primary. |
| 4 | question-taxonomy | Alto | Meta-artigo consultado antes de cada /ask via /question. 7 fontes. |
| 5 | kb-architecture-patterns | Médio-alto | Hub mas com interpretation_confidence:medium — pode ser lido mas não gerar retrievals_correct se confidence da sessão for LOW. |

Estimativas baseadas em centralidade do grafo (inbound wikilinks) e frequência de tema em /ask queries observadas nesta sessão.

## 4. DADO QUE ESTE HOOK HABILITA (após 10 sessões /ask)

### Análises possíveis:

1. **Artigos fantasma** — reads:0 após 10 sessões = artigo existe mas nunca é consultado. Problema de _index.md ou conceito irrelevante?

2. **Artigos tóxicos** — reads alto + retrievals_correct baixo = artigo é consultado mas degrada a resposta. Conteúdo ruim ou over-synthesis?

3. **Retrieval blind spots** — retrievals_gap alto = artigo deveria ser lido mas não é encontrado. Ponteiro de _index.md é fraco.

4. **Lakatos degeneracy metric** — se os mesmos 5 artigos são lidos em todas as sessões e os outros 14 nunca são, a KB está degenerando (confirming loop nos mesmos conceitos).

5. **Temporal decay natural** — last_read permite identificar artigos que eram úteis mas pararam de ser consultados. Candidatos a /review ou remoção.

### Análise NÃO possível sem mais dados:

- **Correção das respostas** — utility_tracker infere qualidade via confidence do /ask, que é auto-avaliação (susceptível a self-enhancement bias). Feedback humano ("essa resposta tava errada") é o ground truth que o tracker não captura.
