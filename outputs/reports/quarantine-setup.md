---
title: "Quarantine Protocol Setup Report"
date: 2026-04-04
---

# Quarantine Protocol Setup

## 1. SCHEMA

- wiki/meta/process-log.md atualizado ✓ (quarantine protocol, 3 criteria, frontmatter schema)
- .claude/commands/promote.md criado ✓ (5-step verification)
- .claude/commands/ingest.md atualizado ✓ (step 13: quarantine check)
- .claude/hooks/session-start.md criado ✓ (4 checks: quarantine, inbox, utility, propagation)
- .claude/commands/ask.md atualizado ✓ (leader impartiality check — Janis prescription)

## 2. ARTIGOS EM QUARENTENA (após retrofit)

| Artigo | Razão | Tempo | Review frio | Critério 3 |
|--------|-------|-------|-------------|-----------|
| reflexion-weighted-knowledge-graphs | confidence:low + 23 speculations | ✅ (>24h) | ❌ | ❌ |
| immune-inspired-credit-assignment | confidence:low | ✅ (>24h) | ❌ | ❌ |
| autonomous-kb-failure-modes | 22 speculations | ✅ (>24h) | ❌ | ❌ |
| raptor-vs-flat-retrieval | 14 speculations | ✅ (>24h) | ❌ | ❌ |
| causal-reasoning-pearl | 12 speculations | ✅ (>24h) | ❌ | ❌ |

**5 artigos em quarentena.** Todos já passaram critério 1 (tempo). Precisam de review frio (critério 2) e challenge/scout/prediction (critério 3).

## 3. ARTIGOS LIBERADOS

18 artigos com quarantine: false (padrão — nunca precisaram):
- llm-knowledge-base, kb-architecture-patterns, retrieval-augmented-generation, context-management, memory-consolidation, multi-agent-orchestration, autonomous-research-agents, hybrid-search, agent-memory-architectures, self-improving-agents, llm-as-judge, tension-resolution, curation-anti-bias, question-taxonomy, formal-ontology-for-kbs, obsidian-agent-workflow, fast-frugal-heuristics, groupthink-and-cascades

## 4. CRITÉRIO MAIS DIFÍCIL DE SATISFAZER

**Critério 3 (adversarial/scout/prediction)** será o mais raramente satisfeito.

Razão: /challenge requer leitura profunda + web search (~15 min/artigo). /scout requer web search + triagem (~15 min). Predição falsificável requer pensamento de design experimental. Todos custam significativamente mais que critério 1 (esperar) e critério 2 (rodar /review).

**Isso é bug ou feature?** Feature — critério 3 é o que garante que a promoção não é rubber-stamp. Se fosse fácil, não preveniria groupthink. O custo é o ponto.

## 5. EDGE CASES NÃO COBERTOS

1. **Artigo que melhora com novas fontes:** Se artigo X começa com confidence:low mas depois um paper que confirma X é ingerido, X deveria sair de quarentena? O protocolo atual não re-avalia automaticamente — precisa de /promote manual. Fix: adicionar ao /ingest: "se nova fonte confirma artigo em quarentena, atualizar quarantine_criteria_met."

2. **Artigo em quarentena que é linkado indiretamente:** Artigo A (quarentena) é linkado por B (livre). C linka B. C herda claims de A via B sem saber que A está em quarentena. O protocolo bloqueia links DIRETOS a artigos em quarentena, mas não previne propagação INDIRETA. Fix: session-start poderia verificar se artigos livres linkam artigos em quarentena.

3. **Todos os artigos de síntese em quarentena simultânea:** Com 5/23 artigos quarentinados, o grafo de conceitos perde 22% dos nodes. Se /ask precisa de um artigo em quarentena, deve lê-lo com caveat ou ignorá-lo? Atual: não especificado. Fix: /ask deve ler artigos em quarentena com flag explícito: "⚠️ artigo em quarentena — claims especulativos."
