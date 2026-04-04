---
title: "Ontology Retrofit Report"
date: 2026-04-04
---

# Ontology Retrofit Report

## 1. PROBLEMAS ENCONTRADOS

| Tipo | Severidade | Frequência | Artigos |
|------|-----------|-----------|---------|
| Untyped wikilinks | MEDIUM (systemic) | 19/19 (100%) | ALL |
| Instance→class escalation | MEDIUM | 16/19 (84%) | Most |
| Meta-KB leakage into Conteúdo | MEDIUM | 14/19 (74%) | Most |
| Continuant/occurrent conflation | LOW | 12/19 (63%) | Domain-inherited |
| Direction ambiguity | MEDIUM | 10/19 (53%) | ~half |
| Resumo drops caveats | MEDIUM-HIGH | 8/19 (42%) | Hub articles |
| 16.1% without Qwen2 qualifier | MEDIUM | 5/19 (26%) | Downstream of self-improving-agents |

**Cross-batch findings:**
- 8 bidirectional relation pairs with type disagreement
- 4 missing reciprocal dependencies
- 3 severity inconsistencies across batches
- 5 blind spots (transitivity, symmetry, quality/disposition, cross-level inventory, none escaped)

**Total: 0 CRITICAL individual, 7 MEDIUM systemic, 19/19 articles affected by at least 1 pattern.**

## 2. ARTIGOS MAIS AFETADOS

### 1. kb-architecture-patterns
- Hub with 10+ inbound links — errors propagate to entire KB
- Pattern 4 is a Role misclassified at same level as Patterns 1-3
- Resumo was overconfident ("validates" language → now "our taxonomy, not measured")
- Scale thresholds extrapolated without qualification

### 2. llm-knowledge-base
- Root definitional article — sets tone for all meta-KB claims
- Entity/process conflation in Resumo
- "Independently converged" was factually wrong (Kepano cites Karpathy)
- Now includes risk documentation (Model Collapse, Wikipedia risks)

### 3. self-improving-agents
- Primary vector for 16.1% propagation to 4+ downstream articles
- Meta-KB claims in Conteúdo ("our pipeline", "our patch system")
- ERL validation presented as field-wide when it's Gaia2-specific

## 3. CORREÇÕES APLICADAS

| Article | What changed | Why |
|---------|-------------|-----|
| kb-architecture-patterns | Resumo rewritten: "our taxonomy", Pattern 4 = role, thresholds = extrapolated | Hub — errors cascade to 10+ articles |
| llm-knowledge-base | Resumo rewritten: not independent, risks documented, anecdotal evidence qualified | Root article — sets meta-KB tone |
| _index.md | 3 pointers calibrated (llm-kb, kb-patterns, raptor-vs-flat, self-improving) | Layer 1 entry points must reflect caveats |

## 4. MODELO CRIADO

wiki/meta/ontology.md contains:
- **7 primitivos** (continuant, occurrent, quality, disposition, role + from BFO/DOLCE)
- **7 relation types** (partOf, contradicts, derivedFrom, validates, supersedes, instanceOf, complementsAt) with formal properties (symmetry, transitivity, asymmetry)
- **3-level abstraction hierarchy** (META / DOMÍNIO / INSTÂNCIA) with mixing rules
- **7-item consistency checklist** for new articles
- **7 questions enabled** by typed relations
- **3 prohibited questions** (malformed ontologically)

## 5. PENDENTE (MÉDIO e BAIXO para próxima sessão)

### MEDIUM — for next /review
- Type all 114+ wikilinks across 19 articles (Phase 1: conventions in descriptions)
- Move meta-KB claims from Conteúdo to Interpretação in 14 articles
- Add Qwen2 qualifier to 16.1% in remaining 4 articles (beyond llm-as-judge)
- Validate all bidirectional relations for symmetry consistency
- Add Quality Gate section to existing articles

### LOW — can wait
- Continuant/occurrent distinction in article structure (domain convention, low impact)
- Cross-level link inventory
- Transitivity validation of partOf chains

## 6. INSIGHT INESPERADO

**A KB não tem ontologia de seus próprios processos.**

Os 19 artigos descrevem ENTIDADES (memory architectures, retrieval patterns, bias types). Nenhum artigo descreve os PROCESSOS da KB como objetos de primeira classe: o que um /ingest run produz como output, quais artigos um /ask session leu, se a resposta foi correta, quanto tempo levou.

Em BFO: todos os nossos artigos são sobre continuants. Os occurrents (processes) são documentados em commands (.claude/commands/*.md) mas não no wiki — não são objetos do knowledge graph. Isso significa:
- Não sabemos quais artigos foram USADOS por /ask (sem log de retrieval)
- Não sabemos quais artigos foram MODIFICADOS por /review (sem changelog per-article)
- Não sabemos se respostas do /ask foram CORRETAS (sem feedback loop)

O RWKG concept (Reflexion-weighted graph) depende de saber "qual edge causou falha" — mas sem logging de occurrents, não temos os dados pra isso. A ontologia revela que o pre-requisito do RWKG não é edge weight modification — é LOGGING DE PROCESSOS. Antes de modificar o grafo baseado em experiência, precisamos REGISTRAR a experiência.

Isso muda a prioridade: em vez de typed wikilinks (que melhoram a estrutura do grafo), o upgrade mais valioso é logging de /ask sessions (que gera os dados pra qualquer learning-from-experience mechanism).
