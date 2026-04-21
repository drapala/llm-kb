---
title: "AgentOps — MAS Failure Management via Historical Trace Retrieval"
sources:
  - path: raw/papers/eager-2026-failure-management-multiagent.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-18
updated: 2026-04-18
tags: [agents, failure-modes, agentops, multi-agent, retrieval, contrastive-learning]
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
  newest_source_yyyymm: "2026-12"
  challenge_verdict: PUBLICÁVEL
topics: [failure-modes, agentic-coding, agentops, trace-retrieval, contrastive-learning]
depends_on: []
---

## Resumo

Zhang et al. (2026) propõem EAGER — framework de gerenciamento de falhas para Multi-Agent Systems (MAS) baseado em representação de traces de raciocínio. O achado empírico central: **em MAS específicos/fixos, tipos de falha são concentrados e recorrentes**, não arbitrários — o que viabiliza reuso de padrões históricos. Standard embeddings (BGE-M3) falham em capturar similaridade de traces de raciocínio (NDCG@10=14.5%), exigindo encoder especializado. EAGER detecta falhas step-by-step com F1 63–86% e latência ~4.9s/step.

## Conteúdo

### Achado Empírico: Concentração de Falhas em MAS Fixos

Análise de 3 MAS open-source revela distribuições altamente distintas e concentradas:

| Tipo de Falha | AutoGen-Code | RCLAgent | SWE-Agent |
|---|---|---|---|
| Incorrect Code | 48.28% | 0% | 46.15% |
| Decomposition Error | 34.48% | 0% | 0% |
| Critical Trace Miss | 0% | 52.63% | 0% |
| Metrics Query Error | 0% | 42.11% | 0% |
| Editing Error | 0% | 0% | 25.64% |
| Localization Error | 0% | 0% | 28.21% |
| Round Limitation | 17.24% | 5.26% | 0% |

**Consequência:** As 2 categorias principais cobrem 82.76% (AutoGen-Code), 94.74% (RCLAgent), e 74.36% (SWE-Agent) das falhas. Reuso de padrões históricos é viável porque o espaço de falhas é pequeno e estável.

### Standard Embeddings Falham em Reasoning Traces

Experimento de retrieval com 45 traces de raciocínio (9 questões × 5 runs):

| Modelo | Recall@10 | NDCG@10 | MRR@10 |
|---|---|---|---|
| Qwen3-0.6B-Embedding | 13.3% | 8.7% | 6.2% |
| BGE-M3-Embedding | 22.2% | 14.5% | 10.8% |

Ambos os modelos falham em capturar similaridade estrutural entre traces semanticamente equivalentes. Exigem encoder especializado para semântica intra-agente e inter-agente.

### EAGER: Framework de 4 Componentes

**1. Failure Knowledge Base (dual granularity)**
- *Fine-grained*: erros específicos no raciocínio de um agente individual (onde hallucinations/inconsistências ocorrem)
- *Coarse-grained*: trace completo reconhecido como errado sem identificar agente específico

**2. Step-Wise Detection**
- Após cada agente completar raciocínio: compara embedding com fine-grained knowledge
- Após todos os agentes: compara trace completo com coarse-grained knowledge
- Latência: 4.57–5.23s por step (vs. per-trace LLM reasoning: significativamente maior)

**3. Reflexive Mitigation (2 níveis)**
- *Model-centric reflection*: agente específico identificado → refine raciocínio daquele agente
- *Orchestration-centric reflection*: trace completo defeituoso → re-avalia coordenação inter-agente

**4. Expert Inspect + Agent RCA** (pós-falha confirmada)
- Enriquece Failure Knowledge Base com novos padrões
- Loop contínuo de aprendizado a partir de falhas confirmadas pelo usuário

### Reasoning-Scoped Contrastive Learning

Treinamento sem labels de falha (unsupervised) via variação de questões:

`L_total = λ₁·L_intra + λ₂·L_inter + λ₃·L_rank`

- **L_intra**: proximidade entre embeddings do mesmo agente em questões similares
- **L_inter**: alinhamento entre agentes para preservar semântica de coordenação
- **L_rank**: consistência entre trace parcial e completo (habilita detecção step-wise)

### Resultados de Avaliação

| Métrica | AutoGen-Code | RCLAgent | SWE-Agent |
|---|---|---|---|
| Anomaly Detection F1 | 73.57% | 86.18% | 79.95% |
| Failure Diagnosis F1 | 63.23% | 78.76% | 69.51% |
| Detection Latency | 5.23s | 4.57s | 4.91s |

Melhoria de task performance (RCLAgent):
- Recall@10: 68.14% → 70.03% (+1.89%)
- MRR: 46.13% → 48.65% (+2.52%)

## Verificação adversarial

**Claim mais fraco:** "failures within a fixed MAS are often limited and recurring" — baseado em apenas 3 MAS com datasets pequenos (29 casos AutoGen-Code, 19 RCLAgent, 39 SWE-Agent aproximado). Generalização para MAS de produção não verificada.

**O que o paper NÃO diz:**
1. Não compara EAGER com simples retry (quanto do ganho é pela detecção precoce vs. reflexive mitigation)?
2. Não demonstra que o encoder treinado generaliza para MAS não vistos durante treino
3. Não mede custo total (step-wise detection + reflexive mitigation) vs. baseline sem EAGER

**Simplificações feitas:** EAGER é avaliado em MAS pequenos e específicos (RCLAgent, SWE-Agent). Em MAS gerais (como AutoGPT, general agents), os autores admitem que "failure types are unpredictable and highly variable" — EAGER seria ineficaz.

**Prior work citado:** TRAIL, MAST (falhas em MAS gerais); AgenTracer, AEGIS, RAFFLES (failure diagnosis); Who&When (atribuição de falhas).

## Interpretação

(⚠️ nossa interpretação) A concentração de falhas em MAS fixos é análoga à distribuição de Pareto em sistemas de produção: poucos tipos de erro respondem pela maioria dos casos. Isso tem implicação direta para design de retry loops: em vez de retry genérico, sistemas com histórico de operação deveriam derivar estratégias de recovery das top-K categorias específicas ao sistema.

(⚠️ nossa interpretação) A falha dos embeddings padrão em traces de raciocínio (BGE-M3 NDCG@10=14.5%) é provavelmente subestimada neste experimento small-scale. Sugere que retrieval de experiências passadas em agentes de coding (ERL) pode estar operando com qualidade de retrieval muito abaixo do reportado — se usar embeddings genéricos.

## Conexões

- validates: [[agentic-coding-failure-taxonomy]] ON "EAGER confirma empiricamente que falhas em MAS fixos são concentradas e recorrentes — o que justifica o routing por tipo de falha que Liu 2025 propõe"
- refines: [[self-improving-agents]] ON "reflexive mitigation distingue model-centric de orchestration-centric reflection — refinamento da taxonomia de self-improvement por nível (agente vs. sistema)"
- validates: [[agent-memory-architectures]] ON "fine-grained vs. coarse-grained failure knowledge é instância de episodic memory (evento específico) vs. semantic memory (padrão geral)"

## Fontes

- [Zhang et al. 2026 — EAGER](../../raw/papers/eager-2026-failure-management-multiagent.md) — framework completo + avaliação empírica em 3 MAS

## Quality Gate

- [x] Wikilinks tipados: 3 (validates×2, refines)
- [x] Instance→class: claims qualificados com dataset size e benchmark específicos
- [x] Meta-KB separado: nenhuma referência a /ask ou /ingest no Conteúdo
- [x] Resumo calibrado: limitações documentadas (3 MAS pequenos, generalização não verificada)
