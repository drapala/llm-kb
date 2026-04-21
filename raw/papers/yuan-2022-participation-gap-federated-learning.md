---
citation: "Yuan, H., Morningstar, W., Ning, L., Singhal, K. (2022). What Do We Mean by Generalization in Federated Learning? International Conference on Learning Representations (ICLR 2022)."
arxiv_id: "2110.14216"
venue: "ICLR 2022"
published: 2021-10-27 # v1
v2_published: 2022-03-16
url: https://arxiv.org/abs/2110.14216
pdf_path: raw/papers/yuan-2022-participation-gap-federated-learning.pdf
stub_upgraded: 2026-04-20
ingested: 2026-04-20
---

# What Do We Mean by Generalization in Federated Learning?

## Abstract (from arxiv v2 / ICLR 2022)

Generalization em federated learning (FL) precisa separar **dois tipos de gap de performance**:
1. **Out-of-sample gap** — performance em dados unseen dentro dos clientes participantes (generalização intra-client).
2. **Participation gap** — performance em distribuições de clientes unseen (clientes que não participaram do treinamento).

Paper argumenta que literatura prévia conflating os dois inflaciona conclusões sobre generalização. Autores propõem:
- Framework para **disentangle** os dois gaps.
- Observam diferenças sistemáticas entre **natural federated datasets** (ex: Stack Overflow, Shakespeare) e **synthetic federated datasets** (ex: LDA-partitioned CIFAR).
- **Recommendation experimental**: held-out 20% dos clientes como **participation test set** — não basta held-out data dentro dos clientes participantes.
- **Semantic synthesis strategy**: método para criar datasets sintéticos realistas quando dados naturally-partitioned não estão disponíveis.

## Key Empirical Findings

- Em natural datasets (Stack Overflow, Shakespeare), participation gap é substancial e distinto do out-of-sample gap.
- Em synthetic datasets (LDA-partitioned), participation gap é frequentemente artificialmente pequeno → literatura superestima generalization quando avalia apenas em synthetic.
- Proposed **diversity sweep**: variar número de clientes held-out e observar curva; shape da curva diagnostica se modelo generaliza a distribuições novas.

## Recommendations para Design Experimental

Paper Section 6 "Community Suggestions" lista exatamente três itens:

1. **Three-way split para disentangle out-of-sample vs participation gaps** — usar o split proposto em Section 3.1 (training clients held-out data + unparticipating clients).
2. **Preferir naturally-partitioned ou semantically-partitioned datasets** para simulações realistas (vs. label-based LDA partitioning que artificialmente zera participation gap).
3. **Reportar distribution of metrics (percentis, variance) across clients** em vez de apenas média — diferenças entre distribuições têm implicações de fairness.

**Held-out 20%** é valor usado nos experimentos do paper (Section 3.1 default setup), **não** recomendação normativa explícita — o paper cita 20% como valor operacional nos experimentos, não como minimum produção.

**"Diversity sweep"** é paráfrase do stub original; paper Section 5.2 chama-se "Effect of client diversity" e varia concentração (Dirichlet alpha) mantendo training data fixo — não varia número de clientes held-out.

## Relevância para E39

**Gap 1 (threshold calibrado)**: Yuan et al. é a fonte mais próxima de uma literatura que propõe métrica operacional de generalização cross-tenant. Não fornecem **threshold production-grade** para Shannon entropy ou coverage-embedding em KB, mas fornecem:
- **Participation gap** como conceito formal análogo a "shared-layer pattern surviving held-out sector".
- **20% held-out recommendation** operacionalmente traduzível para AC17 (held-out-sector mandatory).
- **Diversity sweep** como método de calibração (não threshold single).

**Gap 4 (promotion protocols)**: o framework de separar out-of-sample gap (intra-tenant) de participation gap (cross-tenant) mapeia diretamente no problema T03: 3 tenants concordando em um padrão = evidência intra-cohort; sobreviver a held-out tenant = evidência de participation-invariance. Sem o segundo, promoção replica out-of-sample gap.

**Limitação**: FL é federated training, não federated KB promotion. Analogia transfere por estrutura (variáveis cross-client latent) mas não por mecanismo (gradientes vs. rules). Transferência por analogia, não evidência direta.

## Notas de Ingestão

**Stub upgraded 2026-04-20** — PDF completo baixado via WebFetch de `https://arxiv.org/pdf/2110.14216`, armazenado em `raw/papers/yuan-2022-participation-gap-federated-learning.pdf` (6.1MB). Extração `pdftotext -layout` → 1431 linhas. ICLR 2022, v2 (2022-03-16).

**Verificação post-PDF (2026-04-20):**
- Two-gap framework (out-of-sample vs participation gap) **confirmado** — Definitions 2.2-2.5 no paper.
- Six tasks demonstrando significant participation gaps **confirmado** (Figure 1: EMNIST-10, EMNIST-62, CIFAR-10, CIFAR-100, Shakespeare, StackOverflow).
- LDA label-based partitioning zera participation gap artificialmente **confirmado** (Section 4.2, Figures 4-5).
- Semantic synthesis strategy **confirmado** (Section 4.3; CIFAR-10 para 300 clients, CIFAR-100 para 100 clients).
- **Correção**: Stub original dizia "Diversity sweep" como método; paper Section 5.2 é "Effect of client diversity" via Dirichlet concentration, não sweep de número de clientes held-out. Stub update acima reflete isso.
- **Correção**: 20% held-out é default dos experimentos, não recomendação explícita de produção. Community Suggestions (Section 6) têm 3 itens, não 4 como stub original listava.
