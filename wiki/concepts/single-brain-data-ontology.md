---
title: "Single Brain Data Ontology"
sources:
  - path: raw/papers/hindsight-agent-memory-retain-recall-reflect.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-05
updated: 2026-04-05
tags: [world-model, agent-architecture, data-ontology, multi-agent, single-brain]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
provenance: emergence
emergence_trigger:
  pair: [agent-memory-architectures, stigmergic-coordination]
  ask_session: outputs/logs/sessions/2026-04-05/ask-12-34.md
  connection_type: ANÁLOGO-A
  pearl_level: L2
emerged_on: 2026-04-05
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-05
quarantine: true
quarantine_created: 2026-04-05
quarantine_reason: "artigo emergido — requer 24h + review frio + evidência adversarial ou predição"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: "L2 predição: implementação com 4 camadas epistêmicas reduz conflitos entre agentes vs. flat DB"
---

## Resumo

Um world model com múltiplos agentes especializados precisa separar epistemicamente os dados que ingere. Hindsight (2025) formalizou 4 redes epistêmicas (World, Experience, Opinion, Observation) com 83.6% de accuracy no LongMemEval. (⚠️ nossa interpretação) Aplicado ao Single Brain: cada rede mapeia para um tipo de dado com regime de atualização e confiança distintos — misturar os tipos é a causa raiz de conflitos entre agentes concorrentes.

## Conteúdo

### As 4 redes de Hindsight (verificado em raw/)

Hindsight (2025) organiza memória de agentes em 4 redes lógicas com separação epistêmica explícita:

| Network | Stores | Epistemic status | Update trigger |
|---------|--------|-----------------|----------------|
| World (𝒲) | Objective environment facts | Facts — não evoluem por opinião | Nova observação externa |
| Experience (ℬ) | Agent's own activities (first person) | Biographical — log imutável | Cada ação do agente |
| Opinion (𝒪) | Subjective judgments, confidence c∈[0,1] | Beliefs — atualizam por evidência | Novo dado confirma/refuta |
| Observation (𝒮) | Preference-neutral entity summaries | Synthesis — derivado dos outros | Consolidação periódica |

**Resultado empírico:** 83.6% LongMemEval com modelo 20B (vs. 39% baseline, vs. 71.2% Zep com GPT-4o). A separação epistêmica, não o modelo maior, explica o ganho.

**Operações:** Retain (extract + entity resolution + 4 tipos de link) → Recall (semantic + BM25 + graph + temporal via RRF) → Reflect (resposta parametrizada pela disposição epistêmica da rede consultada).

### Mapeamento ao Single Brain (⚠️ nossa interpretação)

Contexto: Single Brain = world model pessoal unificado para múltiplos agentes especializados (Zelox, KB, carreira, trabalho).

| Hindsight Network | Single Brain equivalent | Exemplos concretos |
|-------------------|------------------------|--------------------|
| World (𝒲) | Fatos externos verificáveis | Contratos PNCP, artigos wiki promovidos, dados de mercado |
| Experience (ℬ) | Log de ações dos agentes | "Agente Zelox gerou risk score X para contrato Y em data Z" |
| Opinion (𝒪) | Outputs com confiança | Risk scores, hipóteses emergidas, predições L2 |
| Observation (𝒮) | Sínteses compiladas | World model compilado, relatórios, artigos wiki em quarentena |

**Por que a separação importa para múltiplos agentes:**

Sem separação, agente A escreve opinião no mesmo espaço que agente B lê como fato. Isso é o **authority bias cascade** de [[autonomous-kb-failure-modes]] em nível de DB: um agente especulativo contamina as leituras de todos os outros. A separação epistêmica é o mecanismo arquitetural que previne a cascade sem requerer coordenação central.

### Regimes de atualização por rede

| Network | Update regime | Quem pode escrever | Conflito resolve como |
|---------|---------------|--------------------|-----------------------|
| World (𝒲) | Append-only + expiry (bi-temporal) | Somente fontes externas verificadas | Bi-temporal: ambas versões coexistem com validity window |
| Experience (ℬ) | Append-only, imutável | Somente o próprio agente | Não conflita — log pessoal |
| Opinion (𝒪) | Update com confidence decay | Qualquer agente, com provenance | Confidence-weighted merge |
| Observation (𝒮) | Rebuild periódico | Processo de consolidação | Re-derivado das outras redes |

**Conexão com [[complementary-learning-systems]]:** World + Experience = hipocampo (ingest rápido, esparso). Observation = neocórtex (consolidação lenta). Opinion = zona de transição onde hipocampo alimenta o neocórtex via replay.

### Predição L2

"Implementar o Single Brain com 4 camadas epistêmicas separadas (vs. flat vector DB) reduzirá conflitos entre agentes especializados em >50% nas primeiras 4 semanas de operação concorrente."

- Dados necessários: log de conflitos (quando agente A sobrescreve output de agente B) em dois regimes
- Falsificador: se conflitos não reduzem com separação, o problema não é ontológico mas de protocolo de comunicação
- Impacto se refutado: o problema está nos protocolos A2A, não na ontologia de dados

## Interpretação

A aplicação de Hindsight ao Single Brain é nossa analogia — Hindsight foi validado em cenários de memória conversacional de agente único, não em world models multi-agente contínuos. A extensão é plausível mas não testada nesse regime.

O claim mais especulativo: que separação epistêmica reduz conflitos entre agentes. Hindsight mede accuracy em QA, não taxa de conflito entre agentes concorrentes. São métricas relacionadas mas não idênticas.

## Gaps que este artigo não resolve

1. **Como fazer ingest contínuo nas 4 redes** — Hindsight não cobre pipelines de streaming
2. **Protocolo quando Opinion de dois agentes conflitam** — confidence-weighted merge é nossa sugestão, não de Hindsight
3. **Escala da rede World com 300M+ vetores** — Hindsight testou em conversas, não em corpora documentais

## Conexões

- [[agent-memory-architectures]] — Hindsight é Pattern 5; Zep/Graphiti (bi-temporal) resolve regime de atualização da rede World
- [[autonomous-kb-failure-modes]] — separação epistêmica é o mecanismo arquitetural que previne authority bias cascade
- [[complementary-learning-systems]] — World+Experience = hipocampo; Observation = neocórtex
- [[stigmergic-coordination]] — agentes comunicam via estado (world model), não diretamente; separação de redes = differentiated pheromones
- [[multi-agent-orchestration]] — coordinator mode assume shared filesystem; 4 redes definem o que cada agente pode ler/escrever

## Fontes

- [Hindsight](../../raw/papers/hindsight-agent-memory-retain-recall-reflect.md) — 4 epistemic networks, retain/recall/reflect ops, 83.6% LongMemEval com 20B model
