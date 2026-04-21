---
title: "SMTA + Burn-After-Use — Secure Multi-Tenant Architecture para LLM Empresarial"
sources:
  - path: raw/papers/zhang-2026-smta-burn-after-use-enterprise-llm.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-20
updated: 2026-04-20
tags: [multi-tenancy, enterprise-llm, data-leakage, burn-after-use, context-ownership, scout-e39]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
quarantine: true
freshness_status: current
depends_on:
  - raw/papers/zhang-2026-smta-burn-after-use-enterprise-llm.md
topics: [multi-tenancy, enterprise-llm-isolation, context-ownership, ephemeral-context, leakage-metrics]
---

## Resumo
Zhang et al. (arXiv:2601.06627, 2026) propõem Secure Multi-Tenant Architecture (SMTA) + Burn-After-Use (BAU) para LLMs empresariais. SMTA isola instâncias por departamento com context-ownership boundaries; BAU enforça contextos conversacionais efêmeros destruídos após uso. Em 127 iterações experimentais, SMTA alcança 92% de defense success rate contra 55 ataques infrastructure-level; BAU atinge 76,75% contra 72 cenários de leakage pós-sessão, medido por 4 métricas formais (LRPR, RRPR, IFER, BTPR).

## Conteúdo

### Motivação e gap identificado
Salvaguardas institucionais tradicionais (access control + encryption) mitigam acesso não-autorizado mas **falham em abordar persistência contextual** — retenção de informação sensível em conversational memory. Gap: cross-session e cross-user inference via contexto remanescente.

### SMTA: arquitetura
- Isolamento de instâncias LLM entre departamentos.
- Context-ownership boundaries rigorosos.
- Infraestrutura internamente deployada (não cloud compartilhada).
- 55 infrastructure-level attack tests, incluindo vector-database credential compromise e shared logging pipeline exposure.

### BAU: mecanismo
- Contextos conversacionais efêmeros.
- Destruição automática após uso.
- Previne cross-session e cross-user inference.
- Avaliado sob failure scenarios realísticos.

### Métricas empíricas formais (Appendix B)
Quatro métricas quantitativas sobre 72 iterações:
- **LRPR** (Local Residual Persistence Rate) — persistência no cliente.
- **RRPR** (Remote Residual Persistence Rate) — persistência em servidores remotos.
- **IFER** (Image Frame Exposure Rate) — fração de interação LLM visível ao usuário que persiste em frames/imagens.
- **BTPR** (Burn Timer Persistence Rate) — falhas no timer de destruição.

### Resultados
- **SMTA**: 92% defense success rate em 55 infrastructure-level attacks.
  - Residual risks apontados: credential misconfiguration + observability pipelines.
- **BAU**: 76,75% success rate médio em 72 iterações contra post-session leakage.
  - Cobre client, server, application, infrastructure, cache layers.
- Total: 127 iterações experimentais.

## Interpretação

(⚠️ nossa interpretação) **"Context ownership" como primitivo arquitetural.** SMTA codifica uma tese específica: isolamento multi-tenant não é propriedade de infra (rede, VM) mas de **ownership de contexto** — quem detém a narrativa conversacional. Isto está próximo do Pattern 4 em [[kb-architecture-patterns]]: "fat skills" com contexto próprio. Generaliza para: tenant isolation requer boundaries na camada semântica, não só de infraestrutura.

(⚠️ design analogy) **Métricas LRPR/RRPR/IFER/BTPR são templates reutilizáveis para medir leakage em KBs.** Cada métrica responde a "onde o contexto vaza quando deveria ser efêmero?". Traduz-se para LLM-KB: se promovemos shared-layer e depois revogamos um tenant, qual é nossa LRPR/RRPR equivalente? Paper dá um vocabulário formal para leakage metrics.

(⚠️ nossa interpretação) **92% defense rate revela limite estrutural.** Os 8% de falhas vêm predominantemente de **credential misconfiguration + observability pipelines** — superfícies que isolamento semântico não cobre. Lição: mesmo com context-ownership perfeito, logging/observability infraestruturais permanecem como side-channel. Reforça argumento de que cross-tenant learning "defensável" requer cobertura em múltiplas camadas simultâneas.

(⚠️ especulativo) **Threshold de "strong isolation" = 92%.** Paper trata 92% como forte evidência de isolation. Isto implica que 8% residual é aceitável empresarialmente. Para NDA/IP cross-tenant learning em setores regulados (financeiro, saúde), 92% pode ser insuficiente — threshold deve ser contextual, não universal.

## Conexões
- complementa: [[safekv-selective-kv-cache-isolation]] — SMTA trata macro-arquitetura; SafeKV trata cache-level
- emerge-para: [[feddca-cross-client-domain-coverage]] — trade-off entre isolation e cross-client learning
- instancia: [[kb-architecture-patterns]] — Pattern 4 com context-ownership explícito

## Fontes
- [Zhang et al. 2026 — SMTA + Burn-After-Use](../../raw/papers/zhang-2026-smta-burn-after-use-enterprise-llm.md) — arXiv:2601.06627. 127 iterações, 92% SMTA, 76,75% BAU, 4 métricas formais LRPR/RRPR/IFER/BTPR.
