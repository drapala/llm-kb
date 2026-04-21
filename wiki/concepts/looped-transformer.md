---
title: "Looped Transformer (Recurrent-Depth)"
sources:
  - path: raw/papers/geiping-2025-recurrent-depth-huginn.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/kohli-2026-loop-think-generalize.pdf
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/wang-2024-grokked-transformers-implicit-reasoners.pdf
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/lu-2025-latent-cot-huginn.pdf
    type: paper
    quality: primary
    stance: challenging
    challenging_type: content
  - path: raw/papers/gao-2025-universal-reasoning-model.pdf
    type: paper
    quality: primary
    stance: confirming
  - path: https://loopformer.github.io/
    type: article
    quality: secondary
    stance: neutral
created: 2026-04-16
updated: 2026-04-16
tags: [architecture, transformer, latent-reasoning, recurrent-depth, inference-time-compute]
source_quality: high
interpretation_confidence: high
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
  re_challenge_trigger: "Lu 2025 ingerido, claim 3 reformulado com evidência primária"
  challenge_claims_survived: 3
  challenge_claims_total: 3
  challenge_log: outputs/logs/sessions/2026-04-17/re-challenge-looped-transformer-21-42.md
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: synthesis
synthesis_sources:
  - raw/papers/kohli-2026-loop-think-generalize.pdf
  - raw/papers/wang-2024-grokked-transformers-implicit-reasoners.pdf
topics: [transformer-architecture, weight-sharing, iterative-refinement, parametric-memory]
depends_on:
  - raw/papers/kohli-2026-loop-think-generalize.pdf
  - raw/papers/wang-2024-grokked-transformers-implicit-reasoners.pdf
---

## Resumo
Looped Transformer reutiliza o mesmo bloco de camadas L por R iterações no forward pass,
produzindo profundidade efetiva D = L×R sem inflar parâmetros. Kohli et al. (2026) mostram
que essa recorrência habilita generalização sistemática e extrapolação de profundidade no
raciocínio implícito — capacidades em que transformers vanilla falham.

## Conteúdo

### Arquitetura
Decoder-only GPT-2 style com L camadas compartilhadas aplicadas R vezes:
`h^(r+1) = f_θ(h^(r); m)` para `r = 0,...,R-1`. Embedding e LM head com pesos atados.
Zero-initialization dos `c_proj` matrices (saídas de attention e FFN inicializadas em zero)
garante que cada bloco recorrente é identity mapping *no momento inicial* do treino — o
Jacobiano input-output começa próximo à identidade, o que Kohli 2026 reporta como crítico
para estabilização sob unrolling longo. (⚠️ nossa nota: a heurística ajuda a evitar
explosão inicial mas não garante estabilidade global; LayerNorm, softmax attention e
dinâmica de treino modulam o comportamento em runs longos.)

Predecessores: Universal Transformer (Dehghani 2019) com weight-sharing explicitamente
motivado por iterative refinement + adaptive computation time (ACT) — precursor direto
da ideia de raciocínio latente recurrente. ALBERT (Lan 2020) compartilha pesos entre
camadas mas com motivação primária de parameter-efficiency. Escala LLM: **Huginn
(Geiping et al. 2025, 3.5B, 800B tokens, AMD Frontier)** é a primeira instância
pretreinada em escala — ver [[huginn-3.5b-recurrent-depth]] para arquitetura
prelude/recurrent/coda, log-normal Poisson sampling de r, truncated backprop k=8 e
sandwich normalization. Ouro (Zhu 2025) é a outra instância em escala.

**Lu et al. (2025, COLM Workshop) — evidência empírica contra latent CoT em Huginn:**
- Probing via logit lens + coda lens sobre 2+4r+2 blocos unrolled (r=16 iterações).
- **Rank trajectory** de tokens intermediate e final: não há separação temporal que
  caracterizaria CoT latente. Ambos caem em rank rapidamente nas primeiras iterations.
- **Descontinuidades entre blocos**: R₁-R₃ decodam via logit lens (100% dos top-5 tokens
  são numeric prefixes); R₄ requer coda lens (logit lens produz tokens não-numéricos).
  Interpretabilidade depende da lens escolhida — não é "smooth refinement".
- **GSM8K**: Huginn w/o CoT a 32 recurrent steps = 4.93% (plateau). Huginn *com* CoT
  explícito = 24.87% (5× maior). Scaling latente não bate reasoning externalizado.
- Implicação: arquitetura treinada em escala, **mas latent reasoning demonstrado não**.
  Ganhos de recurrence são marginais em tarefa aritmética real.

### Estratégias de parada
- **Fixed iteration**: R constante por instância.
- **Dynamic iteration**: R ~ clip(Poisson(λ), R_min, R_max) amostrado por batch.
- **Adaptive halting** (Kohli 2026, §6): combina KL-divergence + entropia da distribuição
  de output. Kohli argumenta que critério KL-only (Geiping 2025) halta prematuramente em
  raciocínio implícito — entropia alta sinaliza incerteza mesmo quando distribuição
  estabilizou.

### Capacidade provada (setup sintético)
Kohli 2026 treina em grafo de conhecimento (|E|=200, |R|=10) com fatos atômicos 1-hop e
inferidos k-hop (k ∈ [2,40]):
- **Generalização sistemática (2-hop OOD)**: R=1 (vanilla) falha completamente; R=2 já
  atinge acurácia não-trivial; R=4 converge em 2k épocas vs R=2 em 7k.
- **Extrapolação de profundidade** (neste setup sintético Kohli): modelo com R=4 treinado
  até 12-hop extrapola para 22-hop ao escalar iterações em inference-time. Sem recorrência
  (R=1) ou com R baixo (R<4), scaling inference-time não ajuda. (⚠️ números específicos
  dependem de curriculum, tokenizer dedicado e grafo sintético — transferência para
  linguagem natural não é provada.)
- **Profundidade aprendível**: R=7 e R=8 ambos atingem 16-hop training — mais iterações
  não traduzem automaticamente em learnable depth maior. Dynamic iteration > fixed.

### Universal Reasoning Model (Gao et al. 2025, URM)
Revival UT aplicado a ARC-AGI. Insight: gains de UT **não vêm de arquitetura elaborada**
(HRM/TRM), mas do recurrent inductive bias + nonlinearidade:

- **ARC-AGI 1**: URM 53.8% pass@1 (SOTA) vs TRM 40.0% vs HRM 34.4%
- **ARC-AGI 2**: URM 16.0% pass@1 vs TRM 4.6% vs HRM 5.4% (~3× HRM)
- **Sudoku**: URM 77.6% vs TRM 66.8% vs HRM 63.9%

Contribuições arquiteturais de URM:
- **ConvSwiGLU**: depthwise 1D convolution (kernel=2) sobre saída do SwiGLU gating —
  injeta interação local no canal sem aumentar complexidade sequencial.
- **Truncated Backpropagation Through Loops (TBPTL)**: dos M loops, só os últimos (M-N)
  recebem gradiente; primeiros N são forward-only. Mitiga noise accumulation em long
  unrolling. Ablação (Table 1): sem TBPTL, ARC-AGI 1 cai de 53.8% → 40.0% pass@1.

**Validação-chave (Table 2):** param-efficiency do UT supera profundidade vanilla.
Com 4× params, UT atinge 40.0% pass@1 ARC-AGI 1 vs vanilla 32× params = 23.75%. Converter
FLOPs em recurrent depth > adicionar parâmetros independentes para reasoning tasks.

### LoopFormer (Jeddi et al. 2025)
Extensão que treina em trajetórias de comprimento variável com shortcut-consistency loss,
alinhando caminhos curtos ao resultado do caminho completo. Cada iteração recebe tempo
interno t e step size Δt. Habilita budget-conditioned inference: usuário escolhe R no
test-time sem retrain. Outperforma vanilla, fixed-depth looped, e early-exit baselines.

## Interpretação

(⚠️ nossa interpretação) Looped Transformer é um ponto de equivalência entre três
arquiteturas vistas como separadas:
- **Recorrência explícita** (RNN) — compartilha pesos no tempo.
- **Profundidade fixa** (deep transformer) — compartilha arquitetura entre camadas, pesos
  distintos.
- **Looped** — compartilha ambos, mas ainda feedforward no sentido causal.

(⚠️ design analogy) A separação "knowledge tied to specific layers" (Kohli §1) é o
análogo neural do gap entre [[raptor-vs-flat-retrieval]]: fatos armazenados shallow não
são acessíveis em deeper hops quando camadas não compartilham memória. Recorrência força
compartilhamento — equivalente a "re-anchor" em [[graph-anchored-iterative-retrieval]],
mas no espaço latente em vez de no corpus externo.

(⚠️ nossa interpretação) Compute adaptativo real. Diferente de "thinking tokens" como no
Claude extended thinking — que gasta tokens textualmente — looped transformer faz
compute adaptativo puramente latente. Isso tem implicação de segurança: raciocínio não é
auditável por leitura de CoT. Complementa, não substitui, CoT explícito.

## Aplicação à KB

A KB não implementa raciocínio paramétrico — opera por retrieval sobre wiki/ e raw/.
Mas o framework Kohli ilumina uma questão: `/ask` é loop externo equivalente a uma
iteração recurrent-depth? Cada hop de [[graph-anchored-iterative-retrieval]] seria um R.
Se sim, `/ask` sofreria de overthinking análogo após ~15 iterations.

## Verificação adversarial

**Claim mais fraco:** "looped transformer habilita depth extrapolation". Só testado em
tarefa sintética com knowledge graph estruturado e tokens dedicados por entidade/relação.
Transferência para linguagem natural com tokenizer subword e distractor tokens não é
demonstrada no paper (Appendix A explícito: "we do not claim complete and immediate
transfer of positive results to LLMs trained with recurrent-depth at scale").

**O que o paper NÃO diz:**
1. Não prova que modelos frontier são looped transformers. Huginn/Ouro existem mas não
   são Claude/GPT/Gemini.
2. Não compara com CoT explícito head-to-head em tarefas reais.
3. Não resolve overthinking — apenas documenta.

**Simplificações feitas:** Artigo lista "zero-initialization" como detalhe, mas paper
§4 dedica seção explicando que é *crítico* — sem isso, recurrent-depth colapsa.

**Prior work citado:** Universal Transformer (Dehghani 2019), ALBERT (Lan 2020),
Deep Equilibrium Networks (Agarwala 2022), Yang et al. 2024a (algorithm learning),
Fan et al. 2025 (length generalization), Saunshi et al. 2025 (scaling com Pile).

## Conexões
- instancia: [[grokking-implicit-reasoning]] — grokking é a dinâmica de treino sob a qual
  systematic generalization emerge em looped transformer
- derivedFrom: [[depth-extrapolation-recurrent]] — extrapolation é capacidade derivada da
  arquitetura looped
- complementa: [[coconut-continuous-latent-reasoning]] — paradigma alternativo para
  raciocínio latente (continuous-thought vs recurrent-depth); diferentes tradeoffs de
  mecanismo, ambos resolvem token bottleneck
- complementa: [[graph-anchored-iterative-retrieval]] — ambos fazem iterative refinement
  (⚠️ design analogy: um no corpus externo, outro no estado latente). Tipo ANÁLOGO-A
  proposto em `outputs/inbox/ontology-proposals.md`.
- complementa: [[raptor-vs-flat-retrieval]] — problema estrutural de "knowledge tied to
  layer/level" (⚠️ design analogy)

## Fontes
- [Geiping et al. 2025 — Scaling up Test-Time Compute with Latent Reasoning](../../raw/papers/geiping-2025-recurrent-depth-huginn.md) — foundational: arquitetura prelude/recurrent/coda; primeiro pretrain em escala (Huginn-3.5B). Detalhes em [[huginn-3.5b-recurrent-depth]]
- [Kohli et al. 2026 — Loop, Think, & Generalize](../../raw/papers/kohli-2026-loop-think-generalize.pdf) — paper central: arquitetura, generalização sistemática, extrapolação, overthinking
- [Wang et al. 2024 — Grokked Transformers](../../raw/papers/wang-2024-grokked-transformers-implicit-reasoners.pdf) — circuit mechanistic, motivação para recurrence
- [Lu et al. 2025 — Latent CoT? Decoding Huginn](../../raw/papers/lu-2025-latent-cot-huginn.pdf) — evidência empírica contra latent CoT em Huginn-3.5B (GSM8K w/o CoT 4.93% vs CoT 24.87%)
- [Gao et al. 2025 — Universal Reasoning Model](../../raw/papers/gao-2025-universal-reasoning-model.pdf) — ARC-AGI 53.8%/16.0% SOTA via ConvSwiGLU + TBPTL; valida recurrent inductive bias
- LoopFormer (Jeddi et al. 2025, loopformer.github.io) — elastic-depth via shortcut modulation

## Quality Gate
- [x] Wikilinks tipados: 4 substituições (instancia, derivedFrom, complementa×2)
- [x] Instance→class: claims numéricos qualificados (R=4 converge em 2k épocas, setup sintético |E|=200)
- [x] Meta-KB separado: 3 referências a `/ask`, `graph-anchored-iterative-retrieval`, `raptor-vs-flat-retrieval` movidas para ## Interpretação e ## Aplicação à KB
- [x] Resumo calibrado: mantido — 3 claims factuais do paper sem extrapolar

> ✓ PROMOVIDO 2026-04-17: Lu 2025 ingerido como stance:challenging; claim 3 sobre Huginn reformulado com números primários (GSM8K w/o CoT 4.93% vs CoT 24.87%). Gate 3 skipped por staleness; re-challenge PUBLICÁVEL 3/3.
