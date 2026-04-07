---
arxiv: 2510.05174
title: "Emergent Coordination in Multi-Agent Language Models"
authors: [Christoph Riedl]
year: 2025
revised: 2026-03-15
type: paper
quality: primary
---

## Abstract

Framework information-teórico para testar — de forma puramente data-driven — se sistemas multi-agente LLM mostram sinais de organização de ordem superior via partial information decomposition de mutual information com time delay.

## Key Claims

- Sistemas multi-agente LLM podem transitar de agregados para coletivos coordenados via design de prompt estratégico
- Padrões de interação em grupos LLM espelham princípios estabelecidos de collective intelligence humana
- Performance eficaz requer alinhamento em objetivos E especialização complementar de papéis

## Methodology

- PID (Partial Information Decomposition) medindo temporal synergy e cross-agent synergy
- Guessing game sem comunicação direta
- 3 intervenções randomizadas: controle, persona assignment, persona + "think about other agents"
- Múltiplos entropy estimators para robustez

## Findings

- Controle: temporal synergy sem coordenação
- Persona assignment: diferenciação estável por identidade
- Persona + "think about others": diferenciação + complementaridade goal-directed
- Resultados mantidos em diferentes emergence measures e baselines

## Limitations

- Experimento único: guessing game
- Feedback de nível grupal mínimo
- Não testa domínios além do jogo simples
