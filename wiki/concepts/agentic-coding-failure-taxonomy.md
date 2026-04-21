---
title: "Agentic Coding Failure Taxonomy"
sources:
  - path: raw/papers/liu-2025-failures-automated-issue-solving.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-18
updated: 2026-04-18
tags: [agents, failure-modes, coding-agents, retry, swe-bench, taxonomy]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
reads: 1
last_read: 2026-04-18
retrievals_correct: 1
provenance: source
freshness_status: current
quarantine: false
quarantine_promoted: 2026-04-18
quarantine_criteria_met:
  auto_promote: true
  gates_passed: [1, 2, 3, 4]
  gate3_skipped: staleness
  newest_source_yyyymm: "2025-12"
  challenge_verdict: PUBLICÁVEL
topics: [failure-modes, agentic-coding, retry-routing, cognitive-deadlock, expert-executor]
depends_on: []
---

## Resumo

Liu et al. (2025) analisaram 150 falhas manuais em 3 ferramentas SOTA no SWE-Bench-Verified e desenvolveram uma taxonomia de **3 fases, 9 categorias, 25 subcategorias** para falhas em agentes de código. O achado principal: pipeline vs. agentic tools têm fingerprints de falha distintos. Arquiteturas agênticas falham predominantemente em Phase 2 (deadlocks cognitivos e raciocínio falho), não em entendimento do problema. Um framework Expert-Executor resolve **22.2% de issues previamente intratáveis**.

## Conteúdo

### Taxonomia de Falhas: 3 Fases

**Phase 1 — Issue Understanding**
- Misidentifying root cause
- Incomplete reproduction of reported behavior
- Incorrect scope inference

**Phase 2 — Solution Planning**
- Flawed reasoning about fix strategy
- Cognitive deadlock (agent loops without progress)
- Scope underestimation (fix too narrow)

**Phase 3 — Implementation**
- Incorrect code change (variable type errors, logic errors)
- Editing errors (wrong file, wrong location)
- Localization errors (incorrect blame attribution)

### Fingerprints por Arquitetura

Ferramentas pipeline-based vs. agentic mostram **distribuições de falha distintas**:

| Arquitetura | Fase dominante de falha |
|---|---|
| Pipeline-based | Phase 1 — Issue Understanding |
| Agentic | Phase 2 — Flawed reasoning + Cognitive deadlock |

Citação direta: "The majority of agentic failures stem from flawed reasoning and cognitive deadlocks."

### Routing por Tipo de Falha

As 25 subcategorias permitem roteamento preciso de recuperação:

| Tipo de falha | Estratégia de recuperação |
|---|---|
| Cognitive deadlock | Interrupção externa + nova estratégia (não retry simples) |
| Type errors | Análise estática pode pré-detectar (abordagem PAGENT) |
| Scope underestimation | Expansão de plano obrigatória antes de retry |
| Localization error | Retrieval augmentation necessária, não retry de código |

### Framework Expert-Executor

Arquitetura de 2 agentes:
- **Expert agent**: apenas texto, sem execução de código. Analisa o issue, despacha tarefas, revisa implementações, fornece supervisão estratégica
- **Executor agent**: acesso completo ao repositório, executa mudanças de código

**Pré-condição crítica**: "The directing relationship requires a genuine capability gap — structure without substance is pure overhead."

**Resultado**: +22.2% de resolução em issues previamente intratáveis (issues que nenhum dos 7 agentes top resolveu individualmente).

### Números-Chave

- 150 instâncias de falha analisadas manualmente
- 769 patches falhos de 7 agentes LLM top (estudo companion PAGENT)
- 3 ferramentas SOTA avaliadas: cobrindo arquiteturas pipeline + agentic
- 22.2% dos issues "intratáveis" resolvidos pelo Expert-Executor

## Verificação adversarial

**Claim mais fraco**: "+22.2% de issues intratáveis resolvidos" — depende da definição de intratável (issues que NENHUM dos 7 agentes resolveu). O conjunto pode ser pequeno e de alta variância.

**O que o paper NÃO diz**:
1. Não fornece dados precisos sobre a distribuição por subcategoria (apenas exemplos)
2. Não avalia se o Expert-Executor é superior a retentar com o mesmo agente + mais tokens
3. Não testa se a taxonomia é exaustiva ou se há tipos raros não capturados em 150 instâncias

**Simplificações feitas**: O resumo trata "pipeline vs. agentic" como binário — o paper avalia 3 ferramentas específicas, não arquiteturas em geral.

**Prior work citado**: PAGENT (companion study), SWE-Bench-Verified como benchmark padrão.

## Interpretação

(⚠️ nossa interpretação) A taxonomia de 3 fases é análoga a um funil de diagnóstico: falha de compreensão (Phase 1) invalida tudo downstream; falha de planejamento (Phase 2) desperdiça execução correta; falha de implementação (Phase 3) é a mais cirurgicamente corrigível. O roteamento por tipo implica que retry homogêneo é sempre subótimo — a estratégia de recuperação deve depender da fase de falha, não apenas do outcome binário.

(⚠️ nossa interpretação) O pré-requisito do Expert-Executor — "genuine capability gap" — sugere que a arquitetura só funciona quando Expert tem modelo de capacidade superior ao Executor. Em cenários onde ambos usam o mesmo modelo base, a estrutura pode ser overhead puro, conforme o paper alerta explicitamente.

## Conexões

- refines: [[self-improving-agents]] ON "Reflexion (retry verbal) é estratégia genérica; esta taxonomia especifica qual fase de falha se beneficia de Reflexion (Phase 3) vs. exige nova estratégia (Phase 2 deadlock)"
- instancia: [[multi-agent-orchestration]] ON "Expert-Executor é instância do padrão coordinator/worker com gap de capacidade explícito como pré-condição"
- validates: [[llm-as-judge]] ON "instabilidade de juízes LLM: Phase 2 (flawed reasoning) é precisamente a fase onde LLM-as-judge é menos confiável por auto-avaliação"

## Fontes

- [Liu et al. 2025 — Failures in Automated Issue Solving](../../raw/papers/liu-2025-failures-automated-issue-solving.md) — taxonomia 3 fases + Expert-Executor framework

## Quality Gate

- [x] Wikilinks tipados: 3 (refines, instancia, validates)
- [x] Instance→class: claims quantitativos qualificados ("up to 22.2%", benchmark específico SWE-Bench-Verified)
- [x] Meta-KB separado: nenhuma referência a /ask ou /ingest no Conteúdo
- [x] Resumo calibrado: mantido — limitações documentadas em Verificação adversarial

> [!patch]
> id: patch-2026-04-19-001
> status: pending
> trigger: ingest/ticket-pre-validation-agentic-planning
> impact_type: scope_expansion
> materiality: high
> affected_claims: [Phase 1 Understanding failures]
> summary: AMBIG-SWE + Ask or Assume fornecem evidência empírica direta para Phase 1: +74% resolve rate em SWE-bench Verified com detecção de underspecification pré-execução. Taxonomy descreve Phase 1 como categoria mas sem intervenção documentada.
> action: Adicionar subseção "Intervenção em Phase 1" referenciando ticket-pre-validation-agentic-planning; qualificar claim sobre Phase 1 failures com dados de AMBIG-SWE/Ask-or-Assume.
> sources:
>   - wiki/concepts/ticket-pre-validation-agentic-planning.md
> created_at: 2026-04-19
