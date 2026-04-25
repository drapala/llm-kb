---
title: "Attention Dilution in LLM Context Provision"
sources:
  - path: raw/papers/kumar-2026-swe-prbench-ai-code-review.md
    type: paper
    quality: primary
    stance: challenging
    challenging_type: implication
  - path: raw/papers/wang-2025-sgcr-specification-grounded-review.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-23
updated: 2026-04-23
tags: [llm, context-window, attention, code-review, prompt-engineering, context-provision]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: synthesis
reads: 0
retrievals_correct: 0
retrievals_gap: 0
freshness_status: current
quarantine: false
quarantine_promoted: 2026-04-23
quarantine_criteria_met:
  auto_promote: true
  gates_passed: [1, 2, 4]
  gate3_skipped: staleness
  newest_source_yyyymm: "2026-03"
  challenge_verdict: PUBLICÁVEL
  challenge_log: outputs/logs/sessions/2026-04-23/challenge-attention-dilution-llm-context.md
  prior_work_found: 5
  claims_survived: 1
  claims_weakened: 2
  claims_invalidated: 0
topics: [llm-context, attention-mechanism, code-review, prompt-design, context-selection]
depends_on:
  - raw/papers/kumar-2026-swe-prbench-ai-code-review.md
synthesis_sources:
  - raw/papers/kumar-2026-swe-prbench-ai-code-review.md
  - raw/papers/wang-2025-sgcr-specification-grounded-review.md
---

## Resumo

Attention dilution é o fenômeno pelo qual LLMs degradam em tasks específicas quando mais contexto é adicionado ao prompt — mesmo contexto estruturado e relevante. No dataset de SWE-PRBench (Kumar 2026, 350 PRs, pesquisador independente), todos os 8 modelos frontier testados degradaram monotonicamente ao passar de diff-only para full context em code review — incluindo quando o contexto continha AST, import graphs e execution context. O mecanismo hipotético é colapso de detecção de issues contextuais (Type2), não de issues locais (Type1). Resultado necessita replicação em escala maior.

## Conteúdo

### Evidência empírica — SWE-PRBench (Kumar 2026)

**Setup:** 350 PRs com ground truth humano anotado. 3 configurações frozen de contexto:

| Config | Conteúdo | Resultado |
|--------|----------|-----------|
| config_A | Diff only | **Melhor** performance |
| config_B | Diff + file content | Pior que A |
| config_C | Full context (exec context, behaviour mapping, test signatures, AST, import graphs) | **Pior** de todos |

**Todos os 8 modelos frontier degradam A → B → C monotonicamente.**

A degradação ocorre mesmo quando o contexto de config_C é enriquecido com estruturas semânticas como:
- AST-extracted function context
- Import graph resolution
- Execution context
- Behaviour mapping
- Test signatures

### Mecanismo: colapso de Type2_Contextual issues

Dois tipos de issues em code review:
- **Type1_Direct** — detectáveis apenas do diff (bugs locais, estilo, sintaxe)
- **Type2_Contextual** — requerem compreensão de contexto mais amplo (impacto arquitetural, integração, comportamento esperado)

O colapso ocorre especificamente em Type2_Contextual ao adicionar contexto (config_B). O mecanismo hipotético: atenção do modelo se dilui pelo contexto extenso e perde o sinal das partes críticas do diff.

### Prompt estruturado vs. contexto completo

**Achado central de SWE-PRBench:**

> Um prompt de 2.000 tokens (diff + summary estruturado) **supera** um prompt de 2.500 tokens com full context enriquecido (no setup de Kumar 2026).

Implicação sugerida: estrutura e seleção do contexto importam mais do que volume de contexto. Caveat: o comparativo não controla independentemente a qualidade de estruturação do prompt mais longo — um full context de 2.5K igualmente bem estruturado pode ter performance diferente.

### Estratégias de mitigação documentadas

**SGCR — Divide and Conquer (Wang et al. 2025):**
Quando spec set é muito longa, divide em chunks e processa em paralelo — cada chunk recebe atenção completa. Síntese final integra os resultados parciais. Resultado: 42% adoption rate vs. 22% baseline.

**RovoDev — RAG para contexto mínimo (Tantithamthavorn 2026):**
Em vez de injetar contexto completo do codebase, usa semantic search para recuperar apenas o contexto relevante para aquele diff específico. Resultado: PR cycle -30.8%.

**BitsAI-CR — Two-stage filtering (Sun 2025):**
Não resolve attention dilution diretamente, mas mitiga consequências: filtra comentários de baixa qualidade antes de expor ao developer.

### Implicação para design de sistemas de code review

A abordagem intuitiva — "mais contexto = review mais informado" — está empiricamente desafiada com evidência crescente para o domínio de code review com contexto de codebase (AST, import graphs, execution context). A literatura geral de long-context (Liu et al. 2024, TACL; arXiv:2510.05381) confirma o padrão fora de code review; para outras tasks como QA, contexto adicional pode ainda ajudar. O design sugerido para code review é:

1. **Selecionar** contexto mínimo relevante (RAG, não dump)
2. **Estruturar** o contexto explicitamente antes de passar ao LLM
3. Usar topologia/blast-radius como **filtro de routing** (o que revisar), não como **contexto injetado** (o que passar ao LLM)
4. Se necessário passar specs longas: fragmentar em chunks paralelos

## Interpretação

(⚠️ nossa interpretação) Este achado tem implicação direta para pipelines de code review que usam topologia de codebase (pagerank, reverse edges, communities) como contexto rico para subagents de review. Se esse contexto é injetado verbatim, attention dilution pode degradar exatamente a detecção de issues contextuais — o tipo mais difícil de capturar. A solução não é abandonar o grafo, mas usá-lo como roteador: o grafo decide *quais camadas rodar* e *o que priorizar*, mas o LLM recebe apenas o contexto comprimido e estruturado.

(⚠️ nossa interpretação) O resultado de Kumar 2026 é de um pesquisador independente com dataset pequeno (350 PRs) — precisa de replicação em escala. Mas é consistente com o que SGCR resolveu empiricamente: o chunk-based approach resolve exatamente a attention dilution que Kumar documenta.

## Conexões

- derivedFrom: [[llm-automated-code-review]] — contexto do problema onde attention dilution aparece
- partOf: [[specification-grounded-review]] — SGCR resolve attention dilution via chunk processing
- implica-em: [[agentic-codebase-enforcement-patterns]] — blast-radius como roteador, não contexto injetado no LLM
- emerge-para: [[ib-optimal-context-selection-review]] ON "colapso de I(X̃;Y) quando |X| excede capacidade efetiva"
- emerge-para: [[rational-inattention-llm-context-failure]] ON "degradação monotônica análoga a canal de Sims saturado"
- emerge-para: [[vsm-blast-radius-routing-calibration]] ON "injeção de fingerprint topológico causa attention dilution em S4"

## Fontes

- [Kumar 2026 SWE-PRBench](../../raw/papers/kumar-2026-swe-prbench-ai-code-review.md) — 350 PRs, 8 modelos, degradação A→B→C, Type2_Contextual collapse
- [Wang 2025 SGCR](../../raw/papers/wang-2025-sgcr-specification-grounded-review.md) — chunk-based processing como solução, 42% adoption

## Verificação adversarial

**Claim mais fraco:** "Todos os 8 modelos degradam monotonicamente." — Dataset de 350 PRs é pequeno; a degradação pode ser específica do domínio dos repos selecionados.

**O que os papers NÃO dizem:**
- Kumar 2026 não testa prompts estruturados vs. dump (apenas diferentes volumes de contexto) — não comprova diretamente que estruturação resolve o problema
- SGCR não testa com contexto de codebase — resolve attention dilution para specs, não para grafo de código

**Simplificações feitas:** "attention dilution" é terminologia do próprio paper de Kumar — não é um mecanismo formalmente verificado, é uma hipótese explicativa para o padrão observado.

**Prior work verificado:** Liu et al. "Lost in the Middle" (TACL 2024, arXiv:2307.03172) — CONFIRMA degradação por posição de contexto relevante. "Context Length Alone Hurts" (arXiv:2510.05381, 2025) — CONFIRMA que length per se degrada, mesmo sem distractors. "Long-Context LLMs Meet RAG" (ICLR 2025, arXiv:2410.05983) — CONFIRMA degradação com mais passagens em RAG. "Long Context vs. RAG" (arXiv:2501.01880) — TENSÃO: LC outperforms RAG em QA benchmarks, o que limita a generalização do claim 3. "Benchmarking LLM-based Code Review" (arXiv:2509.01494) — REFINA — em fila para ingestão.

## Quality Gate

- [x] Wikilinks tipados: 3 relações (derivedFrom, partOf x2)
- [x] Instance→class: claims com fonte e caveat de tamanho de dataset
- [x] Meta-KB separado: sem referências a comandos internos
- [x] Resumo calibrado: inclui "documentou que" (factual) e limitações de replicação na interpretação
