---
title: "SafeKV — Selective KV-Cache Sharing e Reuse Diversity Ratio"
sources:
  - path: raw/papers/chu-2025-safekv-selective-kv-cache-sharing.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-20
updated: 2026-04-20
tags: [multi-tenancy, llm-serving, kv-cache, side-channel, isolation, privacy, rdr, scout-e39]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
quarantine: true
freshness_status: current
depends_on:
  - raw/papers/chu-2025-safekv-selective-kv-cache-sharing.md
topics: [multi-tenancy, kv-cache-isolation, cross-tenant-leakage, rdr-metric, llm-serving]
---

## Resumo
SafeKV (Chu et al., arXiv:2508.08438, 2025) é um co-design runtime para multi-tenant LLM inference que substitui isolamento total de KV-cache por isolamento seletivo guiado por sensibilidade. Introduz o **Reuse Diversity Ratio (RDR)**, métrica de runtime que detecta e limita leakage residual em caches compartilhados. Comparado a isolamento completo, reduz overhead de TTFT em até 40,58% e aumenta throughput em até 2,66×, preservando privacidade sob modelo de ameaça cross-tenant.

## Conteúdo

### Problema (cross-tenant via shared KV-cache)
Compartilhamento global de KV-cache acelera LLM inference por reutilizar prefixos entre requests. Mas introduz **side-channel temporal visível via API**: cache hits são mais rápidos que misses, permitindo que adversários infiram inputs sensíveis de outros tenants observando latências. Defesas anteriores ([[optileak-prompt-reconstruction]] demonstra viabilidade: 12,48× redução de requests/token para reconstrução).

### Três contribuições técnicas do SafeKV
1. **Three-tier asynchronous detection pipeline** — desacopla classificação de privacidade da inferência, suportando workloads de streaming sem bloquear TTFT.
2. **Radix-tree-based memory manager** — gerenciador de memória unificado com compressão de caminho (path compression) e sensitivity-aware eviction para isolamento seletivo escalável.
3. **RDR-guided runtime safeguard** — Reuse Diversity Ratio monitora e limita reutilização concentrada que poderia indicar exfiltração; detecta leakage residual em tempo real.

### Resultados empíricos
- TTFT overhead: até 40,58% menor que full isolation.
- Throughput: até 2,66× maior que full isolation.
- Avaliado em LLM backends de produção (detalhes de modelo específico no paper).
- Threat model: adversário cross-tenant observando latência via API pública.

### Posicionamento no espectro de defesas
- **Sledgehammer (full isolation)**: desabilita APC/cache sharing, perde 40%+ de throughput.
- **SafeKV (selective)**: mantém reuse para tráfego benigno, isola apenas blocos sensíveis.
- **Vulnerável (global sharing)**: exposto a ataques como OptiLeak.

## Interpretação

(⚠️ nossa interpretação) **RDR como métrica generalizável de tenant diversity.** A Reuse Diversity Ratio mede quantos tenants distintos contribuem para reutilização de um bloco específico. Baixa diversidade em bloco sensível = sinal de exfiltração concentrada. Este é um análogo operacional do [[bradford-law-scattering]] — concentração anômala em poucos consumidores indica anomalia. Pode informar métrica equivalente para shared-layer promotion em KBs multi-tenant.

(⚠️ design analogy) **Isolamento seletivo > isolamento total em sistemas multi-tenant.** O paper valida empiricamente uma tese arquitetural: a questão não é "isolar ou compartilhar" mas "quais fragmentos isolar, sob quais critérios de sensibilidade, com qual custo de performance". Aplicável a [[kb-architecture-patterns]] Pattern 4 e a decisões sobre shared-layer em multi-tenant AI platforms.

(⚠️ nossa interpretação) **Threat model implica que "multi-tenant compartilhado == cross-tenant attack surface".** Mesmo sem intenção maliciosa, compartilhamento de representação cria superfície de inferência. Reforça argumento do E39 ticket sobre limiar defensável de cross-tenant learning.

## Conexões
- instancia: [[kb-architecture-patterns]] — pattern de isolation tiers
- complementa: [[optileak-prompt-reconstruction]] — attack counterpart
- emerge-para: [[feddca-cross-client-domain-coverage]] — diversidade como métrica de saúde

## Fontes
- [Chu et al. 2025 — SafeKV](../../raw/papers/chu-2025-safekv-selective-kv-cache-sharing.md) — arXiv:2508.08438. Three-tier detection + radix-tree + RDR. 40,58% TTFT reduction, 2,66× throughput.
