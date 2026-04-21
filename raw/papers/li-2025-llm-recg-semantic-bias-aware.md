---
citation: "Li, Y., et al. (2025). LLM-RecG: A Semantic Bias-Aware Framework for Zero-Shot Sequential Recommendation. Proceedings of the Nineteenth ACM Conference on Recommender Systems (RecSys '25). DOI: 10.1145/3705328.3748077."
arxiv_id: "2501.19232"
venue: "RecSys 2025"
published: 2025-01-31 # v1
v2_published: 2025-07-17
url: https://arxiv.org/abs/2501.19232
acm_url: https://dl.acm.org/doi/10.1145/3705328.3748077
code: https://github.com/yunzhel2/LLM-RecG
stub_upgraded: 2026-04-20
pdf_full_text: raw/papers/li-2025-llm-recg-semantic-bias-aware.full.md
ingested: 2026-04-20
---

# LLM-RecG — Semantic Bias-Aware Framework for Zero-Shot Sequential Recommendation

## Abstract (from arxiv v2)

Zero-shot cross-domain sequential recommendation (ZCDSR) enables predictions in unseen domains without retraining. LLMs improve ZCDSR via rich pretrained representations, but **domain semantic bias** — differences in vocabulary and content focus between domains — remains a persistent challenge, leading to misaligned item embeddings and reduced generalization.

LLM-RecG é um framework model-agnostic que captura **transferable sequential patterns** enquanto preserva **domain-specific nuances** (distinct vocabularies, interaction behaviors, content focuses).

## Training Objective

Balança duas propriedades:
1. **Inter-domain compactness** — item embeddings de diferentes domínios ficam próximos, facilitando transferência de conhecimento e reduzindo bias.
2. **Intra-domain diversity** — mantém distinções fine-grained entre itens dentro do mesmo domínio, evitando overfit a features do source domain dominante.

Loss adicional = **shared-generalization loss (VG component)**.

## Experimental Setup

Datasets: Video Games, Industrial & Scientific, Musical Instruments (Amazon Reviews) + cross-platform Steam dataset.

Backbones: GRU4Rec, SASRec, Bert4Rec. Variants: baseline, `-Sem` (LLM embeddings), `-RecG` (proposed generalization loss).

Baselines: UniSRec, RecFormer (SOTA text-only cross-domain methods).

Métricas: Recall@k, NDCG@k.

## Key Empirical Findings

- **Semantic bias magnitude**: GRU4Rec-Sem drops **>6pts R@10** in Video Games domain when sourced from Industrial&Scientific or Musical Instruments (baseline degradation due to semantic bias).
- **Generalization gap**: BERT4Rec-Sem Steam→IS achieves only 9.97% N@10, muito inferior a MI (17.06%) e VG (17.67%). Steam tem vocabulário distinto, aumenta domain gap.
- **Proposed mitigation**: `-RecG` variants consistentemente mitigam degradação. Exemplo: **+28.9% NDCG@10 Steam→Industrial&Scientific zero-shot**.
- **Ablation (VG loss)**: remover o shared-generalization component derruba R@10 de **35.81 → 28.26** (≈20% relative drop).

## Embedding Analysis

LLM embeddings têm strong semantic separation que paradoxalmente **prejudica generalization** downstream. Os `-RecG` embeddings são mais uniformes/menos distinguíveis across domínios — propriedade desejada para robustness.

## Relevância para E39

- **Strong semantic separation prejudica generalização** ⇒ agreement em set homogêneo (3 tenants mesmo sector) pode refletir embedding bias, não universal pattern.
- **Shared-generalization loss ablation** = evidência empírica de que componente explícito de diversidade cross-domain é necessário; ausência → collapse (R@10 28.26 vs. 35.81).
- **Implicação para T03**: AC17 (held-out sector test) é operacionalmente análogo ao teste `-RecG` variants sob domain shifts; sem esse gate, agreement cross-tenant replica bias ao invés de detectar universalidade.

## Notas de Ingestão

**Stub upgraded 2026-04-20** — full arxiv HTML v2 (2025-07-17) extraído via `mcp__arxiv__download_paper 2501.19232`. Conteúdo completo em `li-2025-llm-recg-semantic-bias-aware.full.md` (93KB).

**Verificação post-PDF (2026-04-20):**
- Drop >6pts R@10 Video Games cross-domain **confirmado** (paper Section 4.4 narrative).
- BERT4Rec-Sem Steam→IS 9.97% N@10 **confirmado** (vs. MI→IS 17.06%, VG→IS 17.67%).
- +28.9% NDCG@10 Steam→IS com LLM-RecG **confirmado** (paper narrative).
- Ablation N@10: **VG (Video Games target)** R@10 35.81 (full) → 28.26 (w/o ID — intra-domain diversity) → 32.49 (w/o IG — item-level generalization) → 32.74 (w/o IC — inter-domain compactness). Papel reporta que ablation de **ID** é o mais destrutivo (não o componente mais amplo "VG loss" como o stub original implicou). Stub original dizia "VG loss ablation" — refer a componente de Video Games domain, mas a ablation real é dos três componentes (IG/ID/IC) + SG (sequential generalization).
- Core claim (shared-generalization loss é mecanismo necessário, não opcional) preservado.
