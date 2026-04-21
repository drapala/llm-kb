---
title: "Uni-CTR — Seesaw Phenomenon em Multi-Domain LLM"
sources:
  - path: raw/papers/fu-2025-uni-ctr-multidomain-ctr-llm.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-20
updated: 2026-04-20
tags: [multi-tenancy, e39, seesaw-phenomenon, shared-layer, multi-domain, ctr-prediction, scout-e39]
source_quality: high
interpretation_confidence: medium
resolved_patches:
  - date: 2026-04-20
    original: "AUC reported at 0.7523 / 0.7569 / 0.7246 across three domains (seesaw asymmetry visible)."
    replacement: "Added RelaImpr context: absolute AUCs coexist with RelaImpr values 24.22%/35.71%/63.35% over best baseline per domain. Challenge earlier interpretation resolved — both number sets are correct and report distinct metrics."
    source: "Post-PDF verification; paper Section V-B Table III and narrative."
provenance: source
quarantine: true
quarantine_created: 2026-04-20
quarantine_reason: "Ingerido via Deep Research Gap E39 (Gap 2 sectoral bias) — aguarda challenge"
freshness_status: current
depends_on:
  - raw/papers/fu-2025-uni-ctr-multidomain-ctr-llm.md
topics: [multi-domain-ctr, shared-layer-promotion, seesaw-phenomenon, ladder-networks, masked-loss]
---

## Resumo

Fu et al. 2025 (ACM TOIS, arXiv:2312.10743) documentam empiricamente o **seesaw phenomenon** em multi-domain CTR prediction: shared-layer dominado por domínios com mais dados degrada performance em domínios minoritários. Uni-CTR usa LLM backbone + **ladder networks** por domínio + **masked loss** para desacoplar gradientes, atingindo +6pts AUC zero-shot e +10.26% em deploy industrial.

## Conteúdo

### Seesaw Phenomenon — definição
Quando arquitetura multi-domain compartilha representação entre N domínios, training é dominado por domínios com mais dados. Ganho em um domínio implica perda em outros (zero-sum característico). Paper reporta **AUC absolutos** 0.7523 / 0.7569 / 0.7246 em Fashion / Musical Instruments / Gift Cards — spread de ~3pts inter-domain mesmo com modelo SOTA, atribuído ao seesaw.

**Métrica RelaImpr (relative improvement over best baseline per domain)**, convenção em CTR literature definida como RelaImpr(A,B) = (AUC_A − 0.5)/(AUC_B − 0.5) − 1:
- Fashion: **24.22%** vs. xDeepFM (best baseline).
- Musical Instruments: **35.71%** vs. DCN.
- Gift Cards: **63.35%** vs. PLE (domínio com menor data → maior relative gain via LLM world knowledge).

Os dois sets de números coexistem: absolute AUCs mostram seesaw asymmetry; RelaImpr mostra que Uni-CTR's advantage é **maior justamente no domínio data-sparse** (Gift Cards), evidenciando que LLM backbone carrega world knowledge que compensa sparsity.

### Arquitetura Uni-CTR
Três módulos:
1. Prompt template: domain + user + product features → natural language sequence.
2. LLM backbone: gera layer-wise semantic representations.
3. Domain-Specific Networks (DSN) pluggáveis: ladder networks sobre diferentes transformer layers do LLM.

### Masked loss — mecanismo de desacoplamento
Gradiente de cada sample atualiza:
(i) apenas o DSN correspondente ao seu domínio (não todos os DSN);
(ii) LLM backbone + general network.

Efeitos:
- Common features são aprendidos via LLM + general network (compartilhado).
- Distinct features são capturados por DSN do próprio domínio (isolado).
- Seesaw reduzido porque "compartilhar" e "isolar" são decisões orthogonais por feature type.

### Resultados empíricos
- 3 public datasets (Amazon Fashion/Music/Gift Cards, Table III): Uni-CTR supera STAR, PLE, SAR-Net, DFFM e todos single-domain baselines.
- **Zero-shot (V-C)** em domain novel (All Beauty): +~6pts AUC vs. best multi-domain baseline; single-domain models degradam a ~0.51 AUC.
- **LLM Scaling (V-D)**: monotonic gains de TinyBERT 14M → Sheared-LLaMA 1.3B. BERT 110M já surpassing todos non-LLM baselines.
- **Industrial deploy (VI-A, Table VII)**: 2 production domains (Domain 0/1), 1 mês user logs. Uni-CTR AUC 0.7387/0.6881; PLE (best baseline) 0.7019/0.6706. **RelaImpr Uni-CTR vs PLE em Domain 1 = 10.26%** (verificado: (0.6881−0.5)/(0.6706−0.5)−1 = 0.1026). Paper note: multi-domain models superam single-domain por margem grande em industrial (ao contrário de Amazon), porque modeling commonality é crítico em escala.
- **Inference latency (VI-B)**: Sheared-LLaMA + ONNX + FP16 via TensorRT → 2ms/sample (V100). AUC loss pós-quantização < 0.01. Acceptable para rank-stage serving.
- **Scalability (V-E)**: DSNs são pluggáveis — Digital Music como new domain adiciona-se sem retreinar shared backbone.

## Interpretação

(⚠️ design analogy) **Seesaw é predição operacional para E39 shared-layer promotion.** Se N tenants compartilham rules via shared-layer sem mecanismo de desacoplamento análogo a masked loss, tenant com mais rules domina shared → rules promovidas refletem estrutura de tenant majoritário. 3 tenants concordando ≠ padrão universal se 1 dos 3 domina o corpus contribuinte.

(⚠️ design analogy) **Ladder networks sugerem arquitetura de shared/private layers.** Tradução para KB multi-tenant: shared-layer deveria armazenar padrões **structural** (análogos a common features via masked loss), tenant-private layers mantêm idiomatic (análogos a DSN-specific). Isto é consistente com AC14 já existente em V2.E39.T03 (abstraction_level=structural-only em shared).

(⚠️ nossa interpretação) **Validação de AC17 proposed.** Zero-shot +6pts em Uni-CTR mostra que held-out-domain test detecta generalização real vs. inflated in-domain metrics. Para E39: held-out-sector test é o equivalente operacional — sem ele, agreement cross-tenant não distingue universal pattern de seesaw artifact.

## Conexões
- emerge-de: [[feddca-cross-client-domain-coverage]] — ambos instanciam "diversity > agreement count" em multi-entity settings.
- complementa: [[llm-recg-semantic-bias-shared-layer]] — Li 2025 opera em recommendation; Fu 2025 em CTR; mecanismo compartilhado.
- instancia: [[requisite-variety]] — V(shared layer) < V(N domains) produz seesaw quando mecanismo de desacoplamento ausente.

## Fontes
- [Fu et al. 2025 — Uni-CTR](../../raw/papers/fu-2025-uni-ctr-multidomain-ctr-llm.md) — ACM TOIS, arXiv:2312.10743. Seesaw phenomenon; ladder + masked loss; +6pts zero-shot; +10.26% industrial.
