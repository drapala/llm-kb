---
arxiv: 2601.08129
title: "Emergent Coordination in Multi-Agent Systems via Pressure Fields and Temporal Decay"
authors: [Roland Rodriguez]
year: 2026
type: paper
quality: primary
---

## Abstract

Propõe alternativa à orquestração hierárquica explícita em sistemas LLM multi-agente. Agentes trabalham sobre artefato compartilhado guiados por pressure gradients derivados de quality signals mensuráveis, com temporal decay prevenindo convergência prematura. Formalizado como otimização sobre pressure landscape com garantias de convergência provadas.

## Key Claims

1. Implicit coordination via shared pressure gradients supera controle hierárquico explícito
2. Constraint-driven emergence é fundação mais simples e eficaz que padrões de orquestração tradicionais
3. Temporal decay é essencial para a eficácia do mecanismo

## Methodology

- Meeting room scheduling tasks; 1.350 trials
- 1 a 4 agentes
- Baselines: conversation-based, hierarchical, sequential, random

## Results

| Abordagem | Solve Rate |
|-----------|------------|
| Pressure-field coordination | **48.5%** |
| Conversation-based | 12.6% |
| Hierarchical control | 1.5% |
| Sequential/random | 0.4% |

- Easy problems: 86.7% solve rate
- Desabilitar temporal decay: -10 pp
- p < 0.001 para todas as comparações

## Limitations

- Escalabilidade além de 4 agentes não testada
- Domínio restrito: scheduling tasks
- Garantias de convergência: condições teóricas não testadas empiricamente além do benchmark
