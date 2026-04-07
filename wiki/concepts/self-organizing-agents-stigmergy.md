---
title: "Self-Organizing LLM Agents and the Endogeneity Paradox"
sources:
  - path: raw/papers/self-organizing-agents-stigmergy.md
    type: paper
    quality: secondary
    stance: confirming
created: 2026-04-07
updated: 2026-04-07
tags: [multi-agent, self-organization, stigmergy, coordination, emergence]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
quarantine: true
quarantine_reason: "Fonte secundária (síntese paramétrica + PDF real). Claims numéricos verificados via texto completo do paper. Aguarda challenge protocol."
---

## Resumo

Paper de Victoria Dochkina (MIPT, 2026) apresenta experimento computacional de 25.000 tarefas comparando arquiteturas de coordenação em sistemas multi-agente LLM. Descoberta central — o "endogeneity paradox": nem controle máximo externo nem autonomia máxima produz resultados ótimos; um protocolo híbrido (Sequential) com ordenação fixa mas seleção autônoma de papéis supera coordenação centralizada em 14% (p<0.001) e protocolos totalmente autônomos em 44% (Cohen's d=1.86, p<0.0001).

## Conteúdo

### Setup experimental

- 25.000+ task runs, 20.810 configurações únicas
- 8 modelos LLM (Claude Sonnet 4.6, GPT-5.4, GPT-4o, GPT-4.1-mini, Gemini-3-flash, GigaChat 2 Max, DeepSeek v3.2, GLM-5)
- 4 a 256 agentes por sistema
- 8 protocolos de coordenação (do Coordinator centralizado ao Shared totalmente autônomo)
- 4 níveis de complexidade de tarefa (L1–L4)

### Endogeneity paradox

O protocolo Sequential — onde a ordenação dos agentes é fixa mas a seleção de papéis é autônoma — supera:
- Coordinator (centralizado): +14% (p<0.001)
- Shared (totalmente autônomo): +44% (Cohen's d=1.86, p<0.0001)

Interpretação dos autores: a scaffolding mínima (ordenação fixa) desbloqueia o potencial do modelo sem impor restrições desnecessárias ao conteúdo da coordenação.

### Capability threshold

Abaixo de um limiar de capacidade do modelo, a auto-organização reverte: estrutura rígida supera autonomia. A auto-organização efetiva exige simultaneamente um modelo capaz E o protocolo certo.

### Emergent phenomena

Com agentes suficientemente capazes:
- **Dynamic role invention**: 5.006 papéis únicos gerados a partir de apenas 8 agentes (RSI → 0)
- **Voluntary self-abstention**: agentes voluntariamente se abstêm de tarefas fora de sua competência
- **Spontaneous hierarchy formation**: hierarquias rasas emergem sem serem pré-programadas

### Sub-linear scaling

O sistema escala sub-linearmente de 4 a 256 agentes sem degradação de qualidade (p=0.61).

### "Universal actor" capability

LLMs podem "mudar especialização instantaneamente, processar contexto organizacional completo, e contribuir com custo marginal zero quando ociosos" — propriedades fundamentalmente distintas de trabalhadores humanos que tornam papéis fixos desnecessariamente restritivos.

### Replicação cross-modelo

Open-source models (DeepSeek v3.2, GLM-5) atingem 95% da qualidade a 24x menor custo que modelos closed-source.

### Three-ring constitutional framework

Os autores propõem um framework constitucional de três anéis para governar organizações multi-agente autônomas (detalhes não expandidos no texto completo disponível).

## Interpretação

(⚠️ nossa interpretação) O endogeneity paradox tem implicação direta para o design do Metaxon Federation Protocol: a Layer de coordenação não deve impor papéis fixos, mas pode oferecer scaffolding estrutural mínimo (e.g., ordenação de precedência). Soberania local dos nós (seleção autônoma de papéis) é confirmada como superior a centralização.

(⚠️ nossa interpretação) A lógica do "capability threshold" mapeia para o critério de promoção da KB: artigos em quarentena não participam de /emerge até validação — analogamente, agentes abaixo do threshold não se auto-organizam de forma útil.

(⚠️ nossa interpretação) Os 5.006 papéis únicos de 8 agentes é evidência empírica de que coordenação estigmérgica via ambiente compartilhado (não via papéis pré-atribuídos) é prática e produtiva — sustenta diretamente o artigo [[stigmergic-coordination]].

## Conexões

- [[stigmergic-coordination]] — paper confirma com dados experimentais o mecanismo de coordenação estigmérgica descrito por Grassé
- [[metaxon-federation-protocol]] — endogeneity paradox confirma soberania local; scaffolding mínima > controle centralizado
- [[multi-agent-orchestration]] — contrasta diretamente com frameworks exógenos (ChatDev, MetaGPT, AutoGen)
- [[self-improving-agents]] — complementar: este paper trata coordenação horizontal; DGM trata melhoria vertical
- [[complexity-emergence]] — emergência espontânea de hierarquias e papéis = exemplo de edge-of-chaos behavior
- [[vsm-autonomous-threshold-design]] — capability threshold ressoa com threshold-triggered S5

## Fontes

- [Dochkina 2026](../../raw/papers/self-organizing-agents-stigmergy.md) — experimento de 25k tarefas; endogeneity paradox; dynamic role invention; sub-linear scaling
