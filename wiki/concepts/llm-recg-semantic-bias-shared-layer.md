---
title: "LLM-RecG — Semantic Bias em Shared-Layer Multi-Domain"
sources:
  - path: raw/papers/li-2025-llm-recg-semantic-bias-aware.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-20
updated: 2026-04-20
tags: [multi-tenancy, e39, semantic-bias, shared-layer, zero-shot, sequential-recommendation, scout-e39]
source_quality: high
interpretation_confidence: medium
resolved_patches:
  - date: 2026-04-20
    original: "Ablation do VG (shared-generalization) component: remover componente derruba R@10 de 35.81 → 28.26 (~21% relative drop)."
    replacement: "VG é o domínio de avaliação (Video Games), não um componente da loss. Ablation real é dos 4 componentes (IG/ID/IC/SG). Remover ID (Intra-domain Diversity) é o mais destrutivo: R@10 35.81→28.26 em VG (source IS). Claim direcional preservado: ablation de UM componente (ID) derruba R@10 ~21%, evidência de que decoupling mechanism é binário, não gradient."
    source: "Post-PDF verification; paper Table 5 e Section 4.3."
provenance: source
quarantine: true
quarantine_created: 2026-04-20
quarantine_reason: "Ingerido via Deep Research Gap E39 (Gap 2 sectoral bias) — aguarda challenge"
freshness_status: current
depends_on:
  - raw/papers/li-2025-llm-recg-semantic-bias-aware.md
topics: [semantic-bias, zero-shot-generalization, shared-generalization-loss, cross-domain-recommendation]
---

## Resumo

Li et al. 2025 (RecSys '25, arXiv:2501.19232) demonstram que **strong semantic separation em LLM embeddings paradoxalmente prejudica generalização cross-domain**. Domain semantic bias — vocabulário e foco de conteúdo divergentes — produz misalignment de item embeddings e collapse zero-shot. LLM-RecG adiciona shared-generalization loss com 4 componentes (IG/ID/IC/SG: item-level generalization, intra-domain diversity, inter-domain compactness, sequential-level generalization), com +28.9% NDCG@10 Steam→Industrial&Scientific e ablation de **Intra-domain Diversity** (ID) como mais destrutiva — R@10 35.81→28.26 no domínio VG (pior que Sem-baseline).

## Conteúdo

### Domain Semantic Bias — definição
Diferenças em vocabulário, content focus e interaction behavior entre domínios criam **misaligned item embeddings**. LLMs com strong semantic separation preservam essa bias, reduzindo generalização quando source domain ≠ target domain.

Observação contraintuitiva: **melhores embeddings (mais separáveis) nem sempre são melhores para transfer**. Strong separation é útil dentro de domínio mas prejudicial cross-domain.

### Training Objective (Shared-Generalization Loss)
Balanceia:
- **Inter-domain compactness** — item embeddings aproximam-se across domínios (favorece transfer).
- **Intra-domain diversity** — preserva distinções fine-grained dentro de domínio (evita collapse em source-domain dominante features).

### Setup Experimental
Datasets: Amazon Reviews (Video Games, Industrial&Scientific, Musical Instruments) + Steam cross-platform.
Backbones: GRU4Rec, SASRec, Bert4Rec. Variants: baseline | `-Sem` (LLM embeddings) | `-RecG` (proposta).
Baselines: UniSRec, RecFormer.
Métricas: Recall@k, NDCG@k.

### Findings Empíricos Centrais

1. **Semantic bias magnitude (GRU4Rec-Sem)**: drop **>6pts R@10** in Video Games quando source domain é Industrial&Scientific ou Musical Instruments. Baseline strong em source mas frágil cross-domain.

2. **Steam effect (BERT4Rec-Sem)**: Steam→Industrial&Scientific atinge apenas 9.97% NDCG@10, muito abaixo de Musical Instruments→IS (17.06%) ou Video Games→IS (17.67%). Vocabulário Steam mais distinto ⇒ bias amplificado.

3. **LLM-RecG uplift**: +28.9% NDCG@10 Steam→Industrial&Scientific zero-shot vs. `-Sem` baseline.

4. **Ablation dos 4 componentes** (Table 5, BERT4Rec trained on IS, evaluated on VG and MI):
   - Full LLM-RecG: R@10 35.81 (VG), 30.10 (MI).
   - w/o IG (item-level generalization): 32.49 / 26.49.
   - **w/o ID (intra-domain diversity) — mais destrutivo**: 28.26 / 20.93 (pior que o `-Sem` baseline 31.84/24.82).
   - w/o IC (inter-domain compactness): 32.74 / 27.35.
   - w/o SG (sequential-level generalization): 33.17 / 28.63.
   
   Ablation de ID sozinho derruba R@10 de 35.81→28.26 (~21% relative drop) — evidência de que preservar fine-grained distinctions dentro de domínio é mais crítico que alignment cross-domain.

### Embedding Analysis
LLM-RecG embeddings são **mais uniformes / menos distinguíveis** across domínios. Contraintuitivo mas benéfico para robustness — "blurred" em termos de discriminação domain-wise, mais generalizáveis em transfer.

## Interpretação

(⚠️ design analogy) **Agreement em set semanticamente homogêneo ≠ universalidade.** Se 3 tenants da claude-pipeline têm semantic signatures similares (e.g., todos SaaS B2B engineering orgs), agreement em uma rule reflete bias compartilhado no vocabulário/interaction pattern — não universal structural pattern. Evidência direta do mecanismo: `-Sem` baseline excelente em-domain mas frágil cross-domain.

(⚠️ design analogy) **Shared-generalization loss analogy para KB promotion.** Sem mecanismo explícito que force **inter-domain compactness** (rule é semanticamente próxima across tenants distintos) + **intra-domain diversity** (variantes do padrão em tenants distintos capturadas), shared-layer promotion replica source-domain bias. AC17 (held-out sector) é aproximação operacional: se rule sobrevive em tenant de sector não-contribuinte, propriedade inter-domain compactness é evidenciada; se falha, rule é sector-specific mesmo sob agreement aparente.

(⚠️ nossa interpretação) **Ablation VG-loss é argumento contra soft promotion.** O fato de remover UM componente derrubar R@10 ~21% mostra que mecanismo de desacoplamento não é gradiente suave — é binário. Tradução para E39: **soft gates (weighted vote de N tenants) são insuficientes; hard gates (held-out sector passou/falhou) são o análogo correto**.

## Conexões
- complementa: [[uni-ctr-multidomain-seesaw]] — Fu 2025 em CTR multi-domain; mesmo mecanismo.
- confirma: [[feddca-cross-client-domain-coverage]] — coverage > heterogeneity; mesma conclusão via federated instruction tuning.
- instancia: [[autonomous-kb-failure-modes]] FM1 — semantic convergence evitável só com mecanismo explícito de diversidade cross-domain.

## Fontes
- [Li et al. 2025 — LLM-RecG](../../raw/papers/li-2025-llm-recg-semantic-bias-aware.md) — RecSys '25, arXiv:2501.19232. Semantic bias documentado; +28.9% uplift; VG ablation R@10 35.81→28.26.
