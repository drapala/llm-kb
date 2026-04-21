---
title: "Participation Gap — Generalization em Federated Learning"
sources:
  - path: raw/papers/yuan-2022-participation-gap-federated-learning.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-20
updated: 2026-04-20
tags: [multi-tenancy, e39, federated-learning, generalization, held-out, participation-gap, scout-e39]
source_quality: high
interpretation_confidence: medium
resolved_patches:
  - date: 2026-04-20
    original: "4. Diversity sweep em vez de single-point evaluation."
    replacement: "Community Suggestions (paper Section 6) lista 3 itens: (1) three-way split para disentangle gaps; (2) preferir natural/semantic partitioning over label-based LDA; (3) report distributions (percentis, variance), não apenas médias. 'Diversity sweep' era paráfrase do stub — paper Section 5.2 é 'Effect of client diversity' via Dirichlet concentration, não sweep de número de clientes held-out."
    source: "Post-PDF verification; paper Section 6 Community Suggestions."
  - date: 2026-04-20
    original: "Held-out ≥20% dos clientes — participation test set separado"
    replacement: "20% é default operacional dos experimentos do paper (Section 3.1), não recomendação normativa explícita. Paper não fixa percentual mínimo — apenas recomenda que unparticipating test set seja distinto do participating validation split."
    source: "Post-PDF verification; paper Section 3.1."
provenance: source
quarantine: true
quarantine_created: 2026-04-20
quarantine_reason: "Ingerido via Deep Research Gap E39 (Gaps 1+4) — aguarda challenge"
freshness_status: current
depends_on:
  - raw/papers/yuan-2022-participation-gap-federated-learning.md
topics: [federated-learning, participation-gap, held-out-clients, diversity-sweep, generalization-framework]
---

## Resumo

Yuan et al. 2022 (ICLR, arXiv:2110.14216) formalizam que generalização em federated learning exige separar **out-of-sample gap** (performance em dados unseen dentro de clientes participantes) de **participation gap** (performance em distribuições de clientes unseen). Literatura prévia conflating ambos superestima generalização. Paper propõe three-way split para disentangle os gaps e demonstra que synthetic datasets (LDA-partitioned) produzem participation gap artificialmente pequeno. 20% held-out é default operacional nos experimentos; Community Suggestions (Section 6) listam 3 recomendações: three-way split, preferir natural/semantic partitioning, reportar distribution of metrics (não apenas médias).

## Conteúdo

### Dois tipos de gap
1. **Out-of-sample gap**: client participou do training, dado avaliado é unseen intra-client. Mede generalização clássica.
2. **Participation gap**: cliente **não participou** do training. Mede se modelo generaliza a **distribuições cliente unseen**.

Os dois gaps são ortogonais: baixo out-of-sample pode coexistir com alto participation gap. Conflating-os (i.e., avaliar apenas intra-participating clients) inflaciona conclusões sobre robustness.

### Evidência empírica
- **Natural datasets** (Stack Overflow, Shakespeare) apresentam participation gap substancial e distinto do out-of-sample gap.
- **Synthetic datasets** (CIFAR particionado via LDA) apresentam participation gap **artificialmente pequeno**, porque estratégia sintética preserva estrutura latente comum.
- Implicação: literatura que avalia FL principalmente em synthetic datasets superestima generalization.

### Recomendações Experimentais (Community Suggestions — Section 6)

Três itens formais do paper:
1. **Three-way split para disentangle out-of-sample vs participation gaps** — training participants held-out + unparticipating clients (Section 3.1).
2. **Preferir naturally-partitioned ou semantically-partitioned datasets** — evitar label-based LDA partitioning que produz participation gap artificialmente zero.
3. **Reportar distribution of metrics across clients** (percentis, variance), não apenas médias — diferenças entre distributions têm fairness implications.

Método auxiliar (paper-contributed, não listado como recomendação formal):
- **Semantic synthesis strategy** (Section 4.3): procedimento para gerar synthetic datasets com participation gap realista quando naturally-partitioned data ausente; paper partitiona CIFAR-10 em 300 clients e CIFAR-100 em 100 clients via semantic partitioning.
- **Section 5.2 "Effect of client diversity"**: varia concentração Dirichlet mantendo training data size fixo — mede efeito direto de heterogeneity em generalization gaps.

**Nota sobre held-out 20%**: valor default nos experimentos do paper (Section 3.1), **não** recomendação normativa explícita de produção.

## Interpretação

(⚠️ design analogy) **Participation gap é o analog formal do "held-out-sector test" (AC17).** Out-of-sample gap = rule funciona em novos tickets dentro dos N tenants que concordaram = baixo valor de generalização. Participation gap = rule funciona em tenant que não contribuiu (held-out sector) = evidência de padrão universal vs. agreement-set artifact. Sem medir participation gap, promotion replica o mesmo erro que Yuan et al. identificam na literatura FL clássica.

(⚠️ design analogy) **20% held-out recommendation operacionalmente traduzível.** Para E39 T03: se agreement set tem 5 tenants, held-out-tenant obrigatório é equivalente. Para 3 tenants (limite inferior AC1), held-out 1 tenant dedicado de sector distinto é mínimo; 0 held-out = participation gap indeterminado.

(⚠️ nossa interpretação) **Diversity sweep vs. single-point justifica AC13 Shannon + AC15 coverage combinados.** Yuan recomenda curva, não ponto. Shannon (AC13) + coverage-embedding (AC15) operam como duas dimensões complementares de sweep — AC13 é discreta (rotulagem setorial), AC15 é contínua (embedding proximity). Ambos passarem ≈ diversity sweep passando em múltiplos pontos. Single-point evaluation (apenas Shannon, apenas coverage, apenas held-out) é insuficiente.

(⚠️ nossa interpretação) **Limitação da analogia.** FL é federated training (parameter gradients) e T03 é federated KB promotion (symbolic rules). Transferência por estrutura (variáveis latentes cross-client, held-out distribution unseen) mas não por mecanismo (gradient descent vs. agreement voting). Yuan **não** fornece threshold production-grade para nosso problema — fornece **métrica conceitual** (participation gap) e **recomendação metodológica** (20% held-out + diversity sweep). Thresholds empíricos em T03 permanecem governance choices, não literature-derived.

## Conexões
- complementa: [[feddca-cross-client-domain-coverage]] — Wang 2024 opera em domain coverage; Yuan 2022 opera em client-distribution generalization; framework complementar.
- emerge-de: [[uni-ctr-multidomain-seesaw]], [[llm-recg-semantic-bias-shared-layer]] — ambos evidenciam que testes in-set infla generalization; participation gap é formalização disso.
- instancia: [[requisite-variety]] — held-out test é modo operacional de medir se regulator tem variedade ≥ ambiente.

## Fontes
- [Yuan et al. 2022 — Participation Gap FL](../../raw/papers/yuan-2022-participation-gap-federated-learning.md) — ICLR 2022, arXiv:2110.14216. Out-of-sample gap vs. participation gap; 20% held-out clients; diversity sweep; natural vs. synthetic datasets.
