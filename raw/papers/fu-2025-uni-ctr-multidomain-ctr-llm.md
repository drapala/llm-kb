---
citation: "Fu, Z., Li, X., Wu, C., Wang, Y., Dong, K., Zhao, X., Zhao, M., Guo, H., Tang, R. (2025). A Unified Framework for Multi-Domain CTR Prediction via Large Language Models. ACM Transactions on Information Systems. DOI: 10.1145/3698878."
arxiv_id: "2312.10743"
venue: "ACM Transactions on Information Systems (TOIS)"
published: 2024-09-26 # v4 (latest)
acm_published: 2025
url: https://arxiv.org/abs/2312.10743
acm_url: https://dl.acm.org/doi/10.1145/3698878
code: https://github.com/Applied-Machine-Learning-Lab/Uni-CTR
stub_upgraded: 2026-04-20
pdf_full_text: raw/papers/fu-2025-uni-ctr-multidomain-ctr-llm.full.md
ingested: 2026-04-20
---

# Uni-CTR — A Unified Framework for Multi-Domain CTR Prediction via LLMs

## Abstract (from arxiv v4)

Multi-Domain Click-Through Rate (MDCTR) prediction crucial for online recommendation. Current MDCTR models face two main limitations: (1) varying data sparsity between domains causes models to be dominated by specific domains, producing the **seesaw phenomenon** — performance improvements in one domain come at the cost of others; (2) scalability is limited when new domains appear.

Uni-CTR leverages an LLM to extract **layer-wise semantic representations** that capture domain commonalities, mitigating the seesaw phenomenon, and incorporates a **pluggable domain-specific network (DSN)** via ladder networks on top of different transformer layers, ensuring scalability.

## Architecture

Three modules:
1. **Prompt template** — consolidates domain, user and product features into natural-language sequences.
2. **LLM backbone** — generates contextualized semantic representations across transformer layers.
3. **Domain-specific networks (DSN)** — ladder networks on top of intermediate LLM layers; each DSN is pluggable per domain.

Key design: **masked loss strategy**. Gradients for a given sample update (i) its corresponding DSN only, not all DSN, and (ii) the LLM backbone and general network. This decouples DSNs and alleviates the seesaw problem because common and distinct features are modeled separately.

## Empirical Results

Three public datasets: Fashion, Musical Instruments, Gift Cards (Amazon categories). Backbone: Sheared-LLaMA 1.3B, 24 transformer layers; 4 ladder layers per DSN.

**Absolute AUC (Table III):**
- Uni-CTR: 0.7523 (Fashion) / 0.7569 (Musical Instruments) / 0.7246 (Gift Cards).
- All baselines (PNN, DCN, DeepFM, xDeepFM, DIEN, AutoInt, FiBiNET, IntTower, Shared Bottom, MMOE, PLE, STAR, SAR-Net, DFFM) had AUC in [0.5907, 0.7031] range across the three domains.
- Best baseline per domain: xDeepFM 0.7031 (Fashion), DCN 0.6893 (Musical), PLE 0.6375 (Gift Cards).

**Relative Improvement (RelaImpr metric — convention in CTR literature):**
RelaImpr(A,B) = (AUC_A − 0.5)/(AUC_B − 0.5) − 1. Uni-CTR over best baseline per domain (paper narrative V-B):
- Fashion: **24.22%** (vs. xDeepFM).
- Musical Instruments: **35.71%** (vs. DCN).
- Gift Cards: **63.35%** (vs. PLE).
- Paper emphasizes Gift Cards gain (63.35%) is largest due to data sparsity — LLM world knowledge compensates seesaw.

**Zero-shot (unseen domain: All Beauty):** Uni-CTR outperforms traditional multi-domain models by "exceeding 6% points" AUC (paper V-C); single-domain models degrade to ~0.51 AUC zero-shot.

**LLM Scaling (V-D):** Scale-up from TinyBERT (14M) → BERT (110M) → DeBERTa-V3-Large (340M) → Sheared-LLaMA (1.3B) shows monotonic improvement. BERT-backbone Uni-CTR already surpasses all non-LLM multi-domain baselines.

**Scalability (V-E, Table IV):** DSN pluggability tested by scaling to Digital Music (new domain) without retraining shared backbone.

**Industrial scenario (VI-A, Table VII):** Two production domains, one month of user behavior logs.
- Uni-CTR: AUC 0.7387 (Domain 0) / 0.6881 (Domain 1).
- Best multi-domain baseline in Domain 1: PLE 0.6706.
- Uni-CTR **relative improvement over PLE in Domain 1: 10.26%** — RelaImpr calculation verified: (0.6881−0.5)/(0.6706−0.5)−1 = 0.1026.
- Paper note: multi-domain models already outperform single-domain on industrial scale (unlike Amazon public datasets) because commonality modeling becomes critical at scale.

**Inference latency:** With Sheared-LLaMA backbone exported to ONNX + FP16 via TensorRT on V100, batch=32 seq_len=256 → 80ms batch latency, ~2ms/sample. AUC loss from quantization < 0.01. Acceptable for rank-stage industrial serving.

## Relevância para E39 / Multi-tenancy

Core findings applicable to multi-tenant knowledge base promotion:
- **Seesaw phenomenon** é evidência empírica de que shared-layer entre N domínios degrada sub-conjuntos quando diversidade semântica cresce sem mecanismo explícito de desacoplamento.
- O uso de **ladder networks + masked loss** sugere que "promover rule para shared" sem mecanismo de desacoplamento por tenant reproduz seesaw — recomendar apenas promoção de padrões structural (não idiomatic) é alinhado.
- Held-out sector test (AC17) é operacionalmente equivalente à forma como Uni-CTR testa domain novel (+6pts zero-shot).

## Notas de Ingestão

**Stub upgraded 2026-04-20** — full arxiv HTML (v4, 2024-09-26) extraído via `mcp__arxiv__download_paper 2312.10743`. Conteúdo completo em `fu-2025-uni-ctr-multidomain-ctr-llm.full.md` (149KB).

**Verificação post-PDF (2026-04-20):**
- Números absolutos do stub original (AUC 0.7523/0.7569/0.7246, +6pts zero-shot, +10.26% industrial) **confirmados**.
- Adicionadas métricas RelaImpr (24.22/35.71/63.35%) para contexto completo — o challenge anterior provavelmente interpretou absolute AUCs como improvements; ambas coexistem e são não-contraditórias.
- Backbone específico: Sheared-LLaMA 1.3B (não genérico "LLM"); 4 ladder layers por DSN; 3 perceptron tower layers {512, 256, 128}.
