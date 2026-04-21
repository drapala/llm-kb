---
title: "Depth Extrapolation and Overthinking in Recurrent Transformers"
sources:
  - path: raw/papers/kohli-2026-loop-think-generalize.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-16
updated: 2026-04-16
tags: [inference-time-compute, test-time-scaling, adaptive-halting, overthinking]
source_quality: medium
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
  challenge_run: 2026-04-16
  challenge_log: outputs/logs/sessions/2026-04-16/challenge-depth-extrapolation-recurrent-19-59.md
  previous_gate3: "claims_weakened=5, invalidated=2 — reclassificados como staleness false-negatives após detector"
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: source
topics: [inference-time-compute, overthinking, adaptive-halting, depth-extrapolation]
depends_on:
  - raw/papers/kohli-2026-loop-think-generalize.pdf
---

## Resumo
Looped transformers generalizam para profundidades de raciocínio (k-hop) muito maiores que
as vistas em training, simplesmente aumentando iterações em inference-time. Isso é depth
extrapolation. Mas há limite: overthinking — iterações excessivas *degradam* predição.
Kohli et al. (2026) caracterizam ambos fenômenos e propõem halting combinando KL + entropia.

## Conteúdo

### Depth extrapolation: scaling inference-time (Kohli 2026, §6.3)
Modelo treinado com R iterations em inputs k-hop (k ≤ 12) consegue resolver k-hop maior
ao rodar mais iterations em inference. Condições:

- **R_train > 4** emergiu como pré-requisito *neste setup*: modelos Kohli com R=1,2,3 não
  se beneficiam de mais iterations em inference. (⚠️ limite específico ao grafo sintético
  k-hop de Kohli; transferência para outras tarefas não é provada.)
- **Dynamic recurrence** (R ~ Poisson durante training) > fixed iteration para extrapolação.
  Dynamic R com max=8 alcança 22-hop em inference; fixed R=8 atinge 19-hop na mesma data.
- Curriculum em hop depth *neste setup*: modelo treina em 2-hop até 95%, depois 3-hop, etc.
  Sem curriculum, Kohli reporta que modelo colapsa em shortcuts via permutation constraint
  (Apêndice B). Necessidade universal de curriculum não é demonstrada.

### Overthinking (Kohli 2026, §6 + Bansal 2022)
Inference iterations > ~15 *degradam* OOD accuracy mesmo em modelos que funcionam bem com
6-12 iterations. Análise via logit margin (diferença entre logit da resposta correta e
do competidor mais forte):

- Margin sobe rapidamente nas primeiras iterações, atinge pico, depois declina.
- Pico ocorre antes para inputs simples (2-hop) que complexos (30-hop).
- Dynamic-recurrence training tem decay de margin *mais lento* que fixed-recurrence —
  mais robusto a overthinking mas não imune.
- Técnicas prévias contra overthinking (input injection, gated halting; Bansal 2022,
  Geiping 2025) *não resolvem* no setup de implicit reasoning.

### Adaptive halting: KL + entropia (Kohli 2026, §6)
Critério de Geiping 2025: parar quando KL(p_t || p_{t-1}) < ε_KL. Kohli mostra que isso
halta prematuramente em implicit reasoning — output distribution estabiliza antes do
modelo ter confiança.

Proposta Kohli: halt quando:
```
KL(p_t || p_{t-1}) < ε_KL  AND  H(p_t) < H_thresh
```
com ε_KL=0.01 e H_thresh=3.00. Em setup dynamic-R max=22, método alcança 15 iterations
médias em 37-hop (vs 5 iterations para KL-only — undershoot) e mantém accuracy.

### O que limita a extrapolação
- **Learnable recursion depth** é função de R_train. R=7 e R=8 ambos aprendem até 16-hop
  (Kohli Figure 5) — aumentar R não escala linearmente.
- **Overthinking cap**: iterations > 2× (R_train_max) tipicamente degradam.
- Saunshi et al. (2025) com Pile 250B mostram tradeoff explícito entre reasoning capacity
  e perplexity/fact recall — modelo looped sacrifica knowledge recall por reasoning depth.

## Interpretação

(⚠️ nossa interpretação) Depth extrapolation é a primeira demonstração limpa de "compute
adaptativo real" em transformer. Modelo decide quantos FLOPs gastar sem tokenizar CoT.
Diferente do paradigma "think harder = generate more tokens" do extended thinking
tradicional.

(⚠️ design analogy) Halting combinado (KL + entropia) ecoa princípio de
[[epistemic-kb-benchmark-protocol]]: convergência de distribuição ≠ confiança epistêmica.
KB precisa de dois sinais: corpus convergiu (novas buscas retornam mesmos docs) AND
entropy de resposta caiu (respostas convergem semanticamente). Usar só um é análogo ao
bug de Geiping.

(⚠️ especulação) Overthinking como fenômeno pode ter análogo em retrieval iterativo.
[[graph-anchored-iterative-retrieval]] hops além de ~5-6 podem degradar precisão —
testagem em corpus próprio pendente.

## Aplicação à KB

Para `/ask`: se o pipeline Layer 0→1→2→3 é visto como recurrent-depth externa, a
prescrição Kohli se aplica:
1. Halt precisa de 2 sinais (corpus estabiliza AND resposta estabiliza), não 1.
2. Escalar hops além do treinado (≈3 layers) pode degradar — testar antes de expandir.
3. Dynamic (variar número de hops por query) > fixed em robustez.

## Verificação adversarial

**Claim mais fraco:** "22-hop generalization" — demonstrado em grafo sintético com tokens
dedicados por entidade/relação, out-degree fixo, permutation constraint. Linguagem natural
com tokenização subword, distractors, e surface-form variation provavelmente reduz
drasticamente a profundidade efetiva aprendível.

**O que o paper NÃO diz:**
1. Não testa se modelos com R>8 podem extrapolar além de 24-hop. Limite superior
   desconhecido.
2. Overthinking pode ser artefato de zero-initialization — default init (Kohli Apêndice E)
   mostra comportamento mais caótico.
3. Não compara compute adaptativo latente vs CoT explícito em paridade de FLOPs.

**Simplificações feitas:** Artigo trata "learnable recursion depth" como propriedade
determinística do R_train; na prática depende de seed, learning rate, curriculum, como
Apêndices F e G indicam variabilidade.

**Prior work citado:** Bansal 2022 (end-to-end algorithm synthesis, overthinking),
Geiping 2025 (Huginn, KL halting), Fan 2025 (length generalization via looped),
Zhu 2025 (Ouro).

## Conexões
- partOf: [[looped-transformer]] — extrapolation é propriedade emergente da arquitetura
  looped; precisa R_train > 4
- depende-de: [[grokking-implicit-reasoning]] — extrapolation requer Stage 3 de grokking
  prévio; sem systematic circuit, inference-time scaling não ajuda

## Fontes
- [Kohli et al. 2026 — Loop, Think, & Generalize](../../raw/papers/kohli-2026-loop-think-generalize.pdf) — fonte primária única: §6 depth extrapolation + adaptive halting + overthinking analysis

## Quality Gate
- [x] Wikilinks tipados: 2 substituições (partOf)
- [x] Instance→class: 22-hop, 15 iter médias, ε_KL=0.01, H_thresh=3.00 — todos qualificados ao setup Kohli sintético
- [x] Meta-KB separado: referência a `/ask`, `epistemic-kb-benchmark-protocol`, `graph-anchored-iterative-retrieval` em ## Interpretação e ## Aplicação à KB
- [x] Resumo calibrado: mantém dois claims — extrapolation funciona + overthinking existe

> ✓ PROMOVIDO 2026-04-17: Gate 3 skipped por staleness (Kohli 2026-01 posterior ao cutoff 2025-10 dos oracles). /challenge com web search retornou PUBLICÁVEL (3/3 claims SÓLIDO, prior work CONFIRMS). Ver `outputs/logs/sessions/2026-04-16/challenge-depth-extrapolation-recurrent-19-59.md`.
