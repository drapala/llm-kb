---
title: "FedDCA — Cross-Client Domain Coverage como Driver Empírico de FedDIT"
sources:
  - path: raw/papers/wang-2024-feddca-cross-client-domain-coverage.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-20
updated: 2026-04-20
tags: [federated-learning, llm-tuning, cross-client, domain-coverage, diversity, privacy, scout-e39]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
quarantine: true
freshness_status: current
depends_on:
  - raw/papers/wang-2024-feddca-cross-client-domain-coverage.md
topics: [federated-instruction-tuning, cross-client-coverage, tenant-diversity, llm-domain-adaptation]
---

## Resumo
Wang et al. (arXiv:2409.20135, 2024) estabelecem empiricamente que **cross-client domain coverage — não data heterogeneity — é o fator pivotal** em federated domain-specific instruction tuning (FedDIT) de LLMs. FedDCA maximiza coverage via diversity-oriented client center selection + retrieval-based augmentation, atingindo ganhos de até 29,19% em performance e 4,82%–21,36% em domain coverage sobre 11 baselines, preservando privacidade.

## Conteúdo

### Framing: FedDIT e o paradoxo da heterogeneidade
Federated Domain-Specific Instruction Tuning (FedDIT) treina LLMs em dados privados distribuídos por clientes/tenants. Literatura prévia tratava data heterogeneity como problema central. Wang et al. desafiam empiricamente essa premissa.

### Claim empírico central
Em experimentos cross-domain, **cross-client domain coverage (diversidade de domínios representados no conjunto agregado de clientes) é o driver pivotal de performance**, não heterogeneidade intrínseca dos dados. Isto é, o problema não é "clientes têm distribuições diferentes" mas "o conjunto de clientes cobre o espectro de domínios que o modelo precisa aprender".

### Algoritmo FedDCA
Dois módulos principais:
1. **Diversity-oriented client center selection** — seleciona centros de cluster que maximizam cobertura de domínios no espaço agregado.
2. **Retrieval-based augmentation** — constrói instruction sets cross-client diversos e não-redundantes via retrieval dirigido.

### Resultados empíricos
- Superioridade sobre 11 baselines em múltiplos domínios.
- Performance gain: até **29,19%** (baseline-dependente).
- Domain coverage improvement: **4,82% a 21,36%**.
- Mantém eficácia em data selection, held-out settings onde dados públicos task-specific são escassos, e sob diferentes graus de heterogeneidade.
- Privacy risks classificados como "manageable" (paper não detalha threat model formal aqui).

### Escopo validado
- Domínios: múltiplos (detalhes no paper; típico FedDIT: médico, financeiro, legal, técnico).
- Número de clientes: variável nos experimentos.
- Comparação contra: 11 baselines de federated instruction tuning e domain generalization.

## Interpretação

(⚠️ nossa interpretação) **Empirical support para "tenant diversity" como métrica de saúde em multi-tenant AI platforms.** O achado de Wang et al. valida parcialmente a intuição do E39 ticket: se cross-client domain coverage é o driver, então 3 tenants do mesmo setor produzem coverage inferior a 3 tenants de setores distintos, mesmo com volume de dados equivalente. Dá base empírica ao argumento "3 tenants ≠ universal; tenant diversity importa mais que tenant count".

(⚠️ design analogy) **Métrica candidata para Tenant Diversity Index.** O threshold de 4,82%–21,36% em coverage improvement sugere que efeito é significativo mas não dominante. Para KB multi-tenant, traduz-se em: promover shared-layer requer demonstrar que tenants contribuintes cobrem diversidade suficiente de domínios — não basta contar tenants. Entropia de Shannon sobre distribuição de domínios é proxy razoável, mas precisa calibração empírica (⚠️ especulativo — paper não propõe threshold específico).

(⚠️ nossa interpretação) **Heterogeneity ≠ diversity.** Distinção sutil: heterogeneity (clientes têm distribuições internas diferentes) é frequentemente resolvível por agregação; diversity (conjunto de clientes cobre espectro relevante) é irredutível — se o conjunto não cobre, aggregate learning não descobre o que falta. Esta distinção é fundamental para argumentar contra cross-tenant learning prematuro.

## Conexões
- emerge-de: [[safekv-selective-kv-cache-isolation]] — ambos tratam cross-tenant como eixo operacional
- complementa: [[kb-architecture-patterns]] — informa shared-layer promotion protocol
- instancia: [[requisite-variety]] — V(shared layer) ≥ V(domain) só se coverage é alto

## Fontes
- [Wang et al. 2024 — FedDCA](../../raw/papers/wang-2024-feddca-cross-client-domain-coverage.md) — arXiv:2409.20135. Cross-client domain coverage é pivotal; +29,19% performance; +4,82–21,36% coverage; 11 baselines.
