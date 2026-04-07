---
arxiv: 2604.00555
title: "Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents"
authors: [Thanh Luong Tuan]
year: 2026
type: paper
quality: primary
---

## Abstract

Aborda desafios de adoção enterprise de LLMs: alucinação, domain drift, compliance regulatória. Apresenta plataforma neurossimbólica Foundation AgenticOS (FAOS) com ontologia em 3 camadas (Role, Domain, Interaction) para ancorar raciocínio do agente em semântica formal.

## Key Claims

1. Asymmetric neurosymbolic coupling: conhecimento ontológico simbólico constrainge inputs do agente; mecanismos de output propostos
2. **Inverse parametric knowledge effect**: o valor de ontological grounding aumenta onde a cobertura do dado de treino do LLM é mais fraca
3. Melhorias significativas vs. agentes não-ancorados

## Methodology

- 600 runs controlados
- 5 domínios: FinTech, Insurance, Healthcare, + 2 domínios localizados para vietnamita
- Ontology-constrained tool discovery via SQL-pushdown scoring
- Métricas: Metric Accuracy, Regulatory Compliance, Role Consistency

## Results

| Métrica | Melhoria | p-value |
|---------|----------|---------|
| Metric Accuracy | +W=.460 | p < .001 |
| Regulatory Compliance | +W=.318 | p = .003 |
| Role Consistency | +W=.614 | p < .001 |

- Maiores ganhos: domínios localizados vietnamitas (menor cobertura paramétrica)
- Produção: 21 domínios industriais, 650+ agentes

## Limitations

- 5 domínios testados (3 inglês + 2 vietnamita)
- Sem seção explícita de limitações
- Single author; sem peer review documentado
