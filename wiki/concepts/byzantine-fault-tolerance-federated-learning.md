---
title: "Byzantine Fault Tolerance em Federated Learning via Consistency Scoring"
sources:
  - path: raw/papers/byzantine-fault-tolerance-federated-learning.md
    type: paper
    quality: secondary
    stance: confirming
created: 2026-04-07
updated: 2026-04-07
tags: [federated-learning, byzantine-fault-tolerance, security, distributed-systems, multi-agent]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
quarantine: true
quarantine_reason: "Fonte secundária (síntese paramétrica + PDF real, 6 páginas, KAIST/Hansung). Claims numéricos verificados via texto completo. Aguarda challenge protocol."
---

## Resumo

Lee, Gong & Kang (KAIST/Hansung, 2024/2025) propõem um plugin modular que embute Byzantine Fault Tolerance em métodos de Federated Learning existentes sem modificar seu núcleo. O mecanismo central: gerar amostras virtuais N(0,I), extrair feature vectors dos desvios de cada update local em relação ao modelo global, computar pairwise cosine similarity, e filtrar os M updates com menor score médio. Resultados no task de blood cell classification: FedAvg com plugin mantém >89.6% de acurácia sob 30% de targeted attacks (vs. 19.5% sem plugin).

## Conteúdo

### Problema

Federated Learning é vulnerável a Byzantine attacks de edge devices comprometidos (targeted model poisoning e untargeted model poisoning). FL métodos heterogeneity-aware (FedProx, FedDyn, FedRS, FedSAM, FedSpeed) caem para ~20% de acurácia quando 30% dos dispositivos são comprometidos.

### Mecanismo: virtual data-driven consistency scoring

3 etapas no servidor central após receber updates locais:

1. **Deviation analysis**: Δwᵢ = wᵢ^ge − wge (desvio de cada update em relação ao modelo global)

2. **Feature mapping**: Para cada par (wᵢ, wⱼ) e N amostras virtuais vₙ ~ N(0,I), extrair feature vectors via g₁:L₋₁ (todas as camadas exceto classificador final):
   - Fᵢ = {fᵢ¹, ..., fᵢᴺ} = g₁:L₋₁(vₙ; Δwᵢ)

3. **Similarity-based rejection**: Cosine similarity pairwise média sobre N amostras:
   - sᵢ,ⱼ = (1/N) Σ cos(fᵢⁿ, fⱼⁿ)
   - s̄ₖ = média das similaridades de k com todos os outros
   - S = {k | π(s̄ₖ) > M} — excluir os M updates com menor score

### Resultados empíricos

Dataset: blood cell classification, ResNet-18, K=10 edge devices, distribuição non-IID:

| Cenário | FedAvg vanilla | FedAvg + plugin |
|---|---|---|
| Targeted (p=0.3) | 19.47% | >89.6% |
| Untargeted (p=0.3) | ~17-19% | 65-70% |

- Untargeted attacks são mais difíceis: mesmo com plugin, acurácia cai para 65-70% vs. 85-90% em targeted.
- Efetividade do plugin aumenta com maior homogeneidade de dados (log α alto).
- Quando log α < 0 (alta heterogeneidade), mesmo o plugin luta para superar 30% sob untargeted attacks.

### Comparação com baselines Byzantine-resilient

Krum, TrimmedMean e Fang (métodos Byzantine-resilient existentes) superam FL heterogeneity-aware sem plugin, mas o plugin-FedAvg é competitivo com eles enquanto mantém os benefícios do método original.

### Propriedade de composabilidade

O plugin é aplicável sobre qualquer método FL sem alterar o núcleo do protocolo: FedAvg, FedProx, FedDyn, FedRS, FedSAM, FedSpeed — todos testados com ganhos consistentes.

### Aplicação original: healthcare

O paper foi desenvolvido no contexto de FL para diagnóstico médico (HIPAA, privacy), onde Byzantine attacks têm implicações de segurança de pacientes. Mas o mecanismo é genérico — não depende de propriedades do domínio médico.

## Interpretação

(⚠️ nossa interpretação) O plugin resolve o gap "Byzantine" identificado no [[metaxon-federation-protocol]], especificamente na Camada 4 (Byzantine resilience). A abordagem via consistency scoring é compatível com a premissa de soberania local: o servidor central não acessa os dados dos nós — apenas compara comportamentos em amostras virtuais.

(⚠️ nossa interpretação) A limitação com alta heterogeneidade (log α < 0) é relevante para o caso de federação epistêmica: KBs de domínios muito distantes podem ter "feature vectors" tão distintos que consistency scoring subestima updates legítimos. Requer threshold adaptativo por cluster de domínio.

(⚠️ nossa interpretação) A distinção targeted vs. untargeted attack tem análogo epistêmico: um agente que sistematicamente injeta claims falsos sobre um tópico específico (targeted) é mais detectável via consistency do que ruído aleatório (untargeted) — o que sugere que o sinal algedônico da KB seria mais eficaz contra ataques targeted.

## Conexões

- [[metaxon-federation-protocol]] — resolve gap Byzantine/Sybil identificado no artigo; Camada 4 implementável com este mecanismo
- [[multi-agent-memory-consistency]] — update-time ordering problem compartilha estrutura com Byzantine filtering
- [[collaborative-memory-access-control]] — provenance imutável por fragmento complementa o consistency scoring
- [[self-organizing-agents-stigmergy]] — ambos tratam coordenação distribuída sem controle central; BFT é pré-requisito para self-organization confiável

## Fontes

- [Lee, Gong & Kang 2024](../../raw/papers/byzantine-fault-tolerance-federated-learning.md) — plugin BFT; consistency scoring; resultados blood cell classification; Algorithm 1
