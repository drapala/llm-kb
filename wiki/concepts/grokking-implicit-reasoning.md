---
title: "Grokking of Implicit Reasoning"
sources:
  - path: raw/papers/wang-2024-grokked-transformers-implicit-reasoners.pdf
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/kohli-2026-loop-think-generalize.pdf
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/lin-2025-implicit-reasoning-shortcuts.pdf
    type: paper
    quality: primary
    stance: challenging
    challenging_type: implication
created: 2026-04-16
updated: 2026-04-16
tags: [training-dynamics, mechanistic-interpretability, generalization, grokking]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
quarantine: false
quarantine_promoted: 2026-04-17
quarantine_criteria_met:
  auto_promote: true
  gates_passed: [1, 2, 4]
  gate3_skipped: staleness
  newest_source_yyyymm: "2026-01"
  oracle_cutoff_yyyymm: "2025-10"
  challenge_verdict: PUBLICÁVEL
  challenge_run_initial: 2026-04-16
  re_challenge_run: 2026-04-17
  re_challenge_trigger: "Lin 2025 ingerido, claim 3 com caveat shortcut learning integrado"
  challenge_claims_survived: 3
  challenge_claims_total: 3
  challenge_log: outputs/logs/sessions/2026-04-17/re-challenge-grokking-21-42.md
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: source
topics: [training-dynamics, parametric-memory, circuit-formation, compositional-generalization]
depends_on:
  - raw/papers/wang-2024-grokked-transformers-implicit-reasoners.pdf
  - raw/papers/kohli-2026-loop-think-generalize.pdf
---

## Resumo
Grokking é generalização emergindo muito depois de overfitting no training set. Wang et al.
(NeurIPS 2024) mostram que transformers aprendem raciocínio implícito via grokking — mas
apenas em tarefas de comparação, não de composição. Kohli et al. (2026) estendem o
resultado: recurrent-depth transformers *sim* grokkam composição sistemática, em três
estágios mecanisticamente distintos.

## Conteúdo

### Grokking como dinâmica (Wang 2024)
Transformer treinado em grafo de fatos atômicos (h, r, t) com conjunto de fatos inferidos
2-hop (axiomas → teoremas). Training accuracy satura em ~14k steps (99% ID e inferred);
ID generalization continua subindo por ~50× mais steps. OOD generalization nunca emerge
para composição. Fenômeno é reprodutível em composição e comparação.

**Fator crítico: distribuição, não tamanho.** Ratio φ = |train_inferred| / |atomic|
controla velocidade de grokking. **Mantendo φ constante**, variar o tamanho absoluto
(|E|=2k, 5k, 10k) não afeta gap train-test nem systematicity (Wang 2024, Fig 2b).
Correção a hipóteses anteriores sobre "critical data size" (Liu 2022, Nanda 2023): ambos
fatores existem, mas na decomposição controlada de Wang, é a *distribuição* (ratio φ) que
carrega o signal, não o tamanho absoluto.

### Mecanismo: circuit formation (Wang 2024, §3.3)
Via logit lens + causal tracing em checkpoints:

- Antes de grokking: `C_mem` domina. Associa (h, r1, r2) → t diretamente, ignorando bridge.
- Durante grokking: forma-se `C_gen` composto de:
  - Layers 0-4: recuperam fato 1-hop (h, r1, b), armazenam bridge b em S[5, r1].
  - Layers 5-8: recuperam fato 2-hop (b, r2, t) a partir de S[5, r1] e S[5, r2].
- Weight decay + implicit bias do optimizer favorecem `C_gen` por ser mais *eficiente*
  (armazena menos fatos: apenas atomics, vs `C_mem` que armazena atomic+inferred).

**Limitação estrutural OOD:** no circuito `C_gen` que Wang 2024 identifica, atomic facts
só são armazenados em upper layers quando aparecem como 2º hop durante training. Fatos
`atomic_OOD` nunca são usados como 2º hop, logo não são armazenados nas upper layers.
Sem um mecanismo de cross-layer memory sharing (memory augmentation ou recorrência
explícita), o transformer vanilla treinado desta forma não consegue recuperá-los em OOD
composição. (⚠️ não é proibição arquitetônica universal — é consequência do circuito
aprendido sob este setup.)

### Caveat: shortcut learning (Lin et al. 2025, ACL Findings)
Lin 2025 treina GPT-2 do zero em dataset sintético de adição/subtração modular, variando
se premisas aparecem em ordem fixa vs shuffled:

- **Premise order fixo**: modelo atinge 99% OOD em 6-step, 90% em 7-step via raciocínio
  implícito. Activation patching confirma propagação diagonal step-by-step no residual
  stream (layers 0-2 → intermediários → layers 8-10).
- **Premise order shuffled**: accuracy cai drasticamente — forward 5-step = 43%,
  6-step = 23%. Modelo falha em aprender stepwise reasoning internal sem ancoragem
  sequencial no prompt.
- **Variable as Subtrahend Plight**: quando variáveis aparecem como subtraendos
  (ex: `b = 16-5-v+22`), accuracy colapsa a near-zero. Mecanismo: modelo aprende atalho
  via commutatividade da adição (chaining numérico); subtração com variável quebra o
  atalho. Lin confirma em SotA LLMs, não apenas GPT-2.
- Implicação: o que Wang 2024 chama "C_gen generalizing circuit" pode ser **shortcut
  pattern matching** com estrutura sequencial favorável, não composição sistemática
  verdadeira. Kohli 2026 mitiga parcialmente via permutation constraint (Apêndice B),
  mas transferência para linguagem natural com premises shuffled permanece aberta.

### Parallel circuit para comparação
Tarefa de comparação (atributos em valores numéricos, relações {<, =, >}) grokka *com*
systematicity. Circuit é paralelo: lower layers armazenam ambos fatos atômicos sem cópia
em upper layers; upper layers comparam. Mesma região armazena ID e OOD facts — explica
por que OOD funciona aqui.

### Três estágios de grokking recurrent-depth (Kohli 2026, §5)
Modelo R=2 (recurrent-depth) via logit lens através de 10⁴ épocas:

1. **Stage 1 — Memorização**: preve target sem decodificar bridge. Modelo vence treino
   via associação direta.
2. **Stage 2 — ID generalization**: bridge torna-se decodificável a profundidade efetiva
   maior. Target predito corretamente em ID.
3. **Stage 3 — Systematic generalization**: OOD funciona. Modelo internalizou a regra
   composicional, não apenas os pares vistos.

Vanilla transformer (8 layers, iso-FLOP vs recurrent R=2 L=4) *não* atinge Stage 3 —
falha em recuperar bridge em deeper layers para OOD inputs.

### Phase transition abrupta (Kohli 2026, §6.2)
Curriculum training em k-hop. Modelo gasta 1.3M steps para atingir 4-hop, depois generaliza
rapidamente até 19-hop com poucos updates adicionais. Depois do "click", cada hop extra
requer <8k steps vs >8k steps/hop antes. Sugere descoberta de regra composicional
unificada, não acumulação incremental.

## Interpretação

(⚠️ nossa interpretação) Grokking é observação empírica, não teoria preditiva. Não sabemos
*quando* vai grokkar sem treinar até observar. Kohli 2026 Figure 6 mostra curva sigmoide —
mas o inflection point é descoberto post-hoc.

(⚠️ design analogy) Para a KB, grokking sugere: métricas de "acurácia em training
distribution" são insuficientes — [[epistemic-kb-benchmark-protocol]] pode estar medindo
stage 1 ou stage 2 mas não stage 3. OOD generalization só emerge com treino muito além
do ponto de saturação. Implicação para benchmarks curtos: subestimam capacidade latente.

(⚠️ design analogy) Efficiency-based explanation de grokking (Wang §3.3) — `C_gen` vence
`C_mem` porque armazena menos — ecoa princípio de parsimônia epistêmica. Mas a analogia
não pode ser aplicada ao wiki: wiki não tem pressão de eficiência estrutural como
weight decay do optimizer.

## Verificação adversarial

**Claim mais fraco:** "grokking é mecanismo universal de generalização implícita". Wang
2024 só testa em 2-hop composition/comparison com grafo aleatório. Dziri et al. (2023)
mostram que transformers reduzem composição a linearized pattern matching em tarefas mais
complexas — grokking pode não escalar para composições profundas sem recorrência.

**O que o paper NÃO diz:**
1. Wang 2024 não prova que frontier LLMs passam por grokking durante pretraining —
   só prova em setup controlado.
2. Phase transition de Kohli 2026 pode ser artefato de curriculum; sem curriculum (Kohli
   §6, Figure 5), extrapolação é mais limitada.
3. Grokking em comparação não implica grokking em composição — são tarefas estruturalmente
   diferentes (serial vs paralela).

**Simplificações feitas:** Artigo descreve circuit gen vs mem como binário; na prática
são distribuições sobrepostas através de training. A transição é gradual nos primeiros
10% e abrupta no restante.

**Prior work citado:** Power et al. 2022 (grokking original), Liu 2022 (critical data
size), Nanda 2023 (mechanistic grokking), Allen-Zhu & Li 2023 (physics of LM).

## Conexões
- instancia: [[looped-transformer]] — recurrent-depth é a arquitetura onde systematic
  grokking emerge para composição
- derivedFrom: [[depth-extrapolation-recurrent]] — depth extrapolation é consequência do
  Stage 3 de grokking em modelos looped

## Fontes
- [Wang et al. 2024 — Grokked Transformers (NeurIPS'24)](../../raw/papers/wang-2024-grokked-transformers-implicit-reasoners.pdf) — paper primário: circuit analysis, delayed generalization, distribution > size
- [Kohli et al. 2026 — Loop, Think, & Generalize](../../raw/papers/kohli-2026-loop-think-generalize.pdf) — extensão para composição sistemática via recorrência, phase transition
- [Lin et al. 2025 — Implicit Reasoning is Reasoning through Shortcuts (ACL Findings)](../../raw/papers/lin-2025-implicit-reasoning-shortcuts.pdf) — challenging: fixed-pattern grokka; shuffled falha; Variable as Subtrahend Plight em SotA LLMs

## Quality Gate
- [x] Wikilinks tipados: 2 substituições (INSTANCIA, derivedFrom)
- [x] Instance→class: 14k steps, 50× saturação, 1.3M steps → 4-hop, <8k steps/hop após click — todos qualificados com paper/dataset
- [x] Meta-KB separado: referência a `epistemic-kb-benchmark-protocol` em ## Interpretação
- [x] Resumo calibrado: mantém distinção "composição falha / comparação funciona" em vanilla, e estende "composição funciona em recurrent-depth"

> ✓ PROMOVIDO 2026-04-17: Lin 2025 ingerido como stance:challenging/implication; seção "Caveat: shortcut learning" integrada com números primários (99% fixed vs 23% 6-step shuffled; Variable as Subtrahend Plight em SotA). Gate 3 skipped por staleness; re-challenge PUBLICÁVEL 3/3.
