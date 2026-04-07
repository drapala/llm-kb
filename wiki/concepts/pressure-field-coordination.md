---
title: "Pressure-Field Coordination in Multi-Agent Systems"
sources:
  - path: raw/papers/pressure-field-coordination-rodriguez-2026.md
    type: paper
    quality: primary
    stance: challenging
    challenging_type: implication
created: 2026-04-06
updated: 2026-04-06
tags: [multi-agent, coordination, emergence, stigmergy, orchestration]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: source
quarantine: true
quarantine_created: 2026-04-06
quarantine_reason: "Gate 3∥challenge — 3 invalidated + 3 weakened"
quarantine_promoted: null
quarantine_criteria_met:
  gates_passed: [1, 2]
  gates_failed: [3]
  gate3_run: 2026-04-06
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  gate3_claims_challenged: 8
  gate3_claims_survived: 2
  gate3_claims_weakened: 3
  gate3_claims_invalidated: 3
---

## Resumo

Rodriguez (2026) propõe coordenação implícita via pressure gradients como alternativa à orquestração hierárquica explícita em sistemas LLM multi-agente. Agentes trabalham sobre artefato compartilhado guiados por gradientes de qualidade com temporal decay. Em scheduling tasks com 1-4 agentes: 48.5% solve rate vs. 1.5% (hierarchical) e 12.6% (conversation-based). Resultado provocativo mas domínio restrito (scheduling, até 4 agentes).

## Conteúdo

### O mecanismo

Em vez de um orquestrador explícito que distribui e coordena tarefas, cada agente lê um **artefato compartilhado** (o problema em progresso) e um **campo de pressão** derivado de quality signals mensuráveis — regiões do problema com alta pressão indicam onde a intervenção é mais necessária.

O **temporal decay** melhora significativamente o desempenho (+10pp; sem decay: 38.5% vs. 48.5%) ao redistribuir pressão para áreas não trabalhadas. O artigo interpreta isso como prevenção de convergência prematura, mas a ablação mostra que o sistema sem decay ainda supera todos os baselines (38.5% vs. 12.6%); "essencial" seria forte demais.

O sistema é formalizado como otimização sobre pressure landscape com garantias de convergência provadas (condições teóricas não testadas empiricamente além do benchmark).

### Resultados (scheduling tasks, 1.350 trials)

| Abordagem | Solve Rate |
|-----------|------------|
| Pressure-field | **48.5%** |
| Conversation-based | 12.6% |
| Hierarchical control | 1.5% |
| Sequential/random | 0.4% |

- Problemas fáceis: 86.7% solve rate
- Sem temporal decay: -10 pp (38.5%)
- Escala de 1 a 4 agentes testada; comportamento além de 4 não documentado

### O que pressure-field não é

- Não é orquestração: nenhum agente decide quem faz o quê
- Não é orquestração explícita: nenhum agente central decide quem faz o quê
- Não é multi-agent debate (sem rounds de leitura cruzada explícita)
- É coordenação via ambiente compartilhado — estruturalmente análogo à stigmergy (Grassé 1959), não idêntico; stigmergy não exige pheromones persistentes nem ausência de decay
- O mecanismo de quality-signal como campo é específico a este paper; não há tradição anterior documentada com exatamente este design

### Comparação com paradigmas existentes

| Paradigma | Locus de coordenação | Perf. em scheduling |
|-----------|---------------------|---------------------|
| Hierarchical orchestration | Coordenador explícito | 1.5% (solve rate neste benchmark) |
| Pressure-field | Campo de qualidade compartilhado | Baixo — sem coordenador |
| Multiagent debate | Leitura cruzada explícita de respostas | Médio |
| Stigmergic | Marcação do ambiente persistente | Baixo |

## Verificação adversarial

**Claim mais fraco:** generalização além de scheduling tasks. O domínio é incomumente bem-estruturado para pressure gradients: qualidade de scheduling é mensurável (conflitos resolvidos, restrições satisfeitas). Domínios com quality signals ambíguos (raciocínio aberto, pesquisa) podem não ter campo de pressão computável.

**O que o paper NÃO diz:**
- Não testa além de 4 agentes — comportamento com N grande é desconhecido
- Não compara com task decomposition (dividir problema antes)
- Não analisa falhas: quando o campo de pressão diverge

**Simplificações:**
- "Hierarchical control" com 1.5% pode ser implementação fraca de coordenação explícita — não representativa de state-of-art em orchestration
- Garantias de convergência teóricas ≠ garantias em produção

**Prior work:** Rodriguez cita multi-agent systems e optimization literature, mas sem benchmarks em tarefas além de scheduling. Trabalhos de stigmergic coordination (Grassé 1959) e swarm intelligence são precursores não citados.

## Interpretação

(⚠️ nossa interpretação) A diferença de performance entre pressure-field (48.5%) e hierarchical control (1.5%) em scheduling é provocativa, mas a interpretação correta é: **coordenação explícita adiciona overhead que prejudica tarefas paralelizáveis com quality signal claro**. Isso não implica que orchestration seja inferior em geral — implica que o tipo de tarefa determina a estratégia de coordenação correta.

(⚠️ nossa interpretação) O mecanismo é estruturalmente análogo à coordenação stigmergic de Grassé (1959): agentes modificam o ambiente, o ambiente guia o próximo agente. A diferença: pressure fields são computados de quality signals em vez de traces físicos.

(⚠️ nossa interpretação) A implicação para VSM: pressure-field coordination poderia ser implementação de S2 (coordenação) sem S3 (controle explícito) — S2 implícito via campo de pressão, sem coordinator agent. Mas isso pressupõe que quality signals são computáveis, o que VSM não assume.

## Aplicação à KB

(⚠️ nossa interpretação) Implicação para Prometheus: tarefas como /ingest paralelo com múltiplos papers poderiam usar pressure-field em vez de scheduling manual — mas requer quality signal mensurável por artefato (o que "qualidade de ingest" significa?).

## Quality Gate

- [x] Wikilinks tipados: 3 relações (contradicts, analogoTo, related)
- [x] Instance→class: números qualificados com domínio (scheduling, 1-4 agentes)
- [x] Meta-KB: referência a Prometheus em ## Aplicação à KB
- [x] Resumo calibrado: "resultado provocativo mas domínio restrito"

## Conexões

- contradicts: [[multi-agent-orchestration]] ON "hierarchical coordinator mode — 1.5% vs 48.5% em scheduling (domínio específico)"
- analogoTo: [[stigmergic-coordination]] ON "coordenação via ambiente compartilhado; sem coordenador explícito"
- related: [[viable-system-model-beer]] ON "pressure-field como S2 implícito — coordenação sem coordinator agent"
- related: [[requisite-variety]] ON "pressure gradient = mecanismo de variety attenuation distribuído"

## Fontes

- [Pressure Fields Rodriguez 2026](../../raw/papers/pressure-field-coordination-rodriguez-2026.md) — mecanismo, benchmarks scheduling 1-4 agentes, comparações, temporal decay

> ⚠️ QUARENTENA: Gate 3∥challenge — 3 claims invalidated + 3 weakened. Correções aplicadas, mas revisão humana necessária antes de citar como fonte:
> 1. "overhead" removido da comparação — 1.5% é solve rate, não medida de overhead
> 2. Caracterização de stigmergy corrigida — stigmergy não exige pheromones persistentes
> 3. Temporal decay qualificado como "benéfico (+10pp)" em vez de "essencial"
