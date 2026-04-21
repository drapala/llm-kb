---
title: "Retrofitting Recurrence — Convertendo Modelos Pretrained em Depth-Recurrent (McLeish 2025)"
sources:
  - path: raw/papers/mcleish-2025-retrofitted-recurrence.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-19
updated: 2026-04-19
tags: [recurrent-depth, model-surgery, continued-pretraining, post-training, latent-reasoning]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
topics: [recurrent-depth, model-surgery, continued-pretraining, post-training, training-efficiency]
depends_on:
  - raw/papers/mcleish-2025-retrofitted-recurrence.md
  - raw/papers/geiping-2025-recurrent-depth-huginn.md
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
---

## Resumo
McLeish et al. (2025-11, arXiv:2511.07384, mesmo grupo do Huginn) demonstram que modelos
fixed-depth pretrained (TinyLlama, OLMo-2, Llama-3.2-1B) podem ser convertidos em
depth-recurrent transformers via continued pretraining + curriculum de recurrence,
**eliminando a necessidade de pretrain RDT from-scratch**. Init de Llama supera init
aleatória em ~950B tokens equivalentes — viabiliza adoção prática sem repetir o custo
do Huginn.

## Conteúdo

### Problema atacado
[[huginn-3.5b-recurrent-depth]] (Geiping 2025) provou que RDT escala mas exigiu pretrain
from-scratch em 800B tokens com r̄=32 — custo proibitivo para reaproveitamento. McLeish
ataca a eficiência de treino, focando em **knowledge transfer** de checkpoints existentes.

### Procedimento de model surgery
Mantém triplet `(l_P, l_R, l_C)` de Geiping. Da pretrained network com L camadas:
- **Prelude**: pega as primeiras layers (camadas iniciais embedding-like)
- **Recurrent block**: layers do meio (intermediárias intercambiáveis)
- **Coda**: últimas layers (decision-like)

Ex: Llama com 22 layers em config (4, 8, 4) → seleciona [0-3], [10-17], [18-21]. Layers
descartadas (4-9) são removidas. Funciona melhor que ShortGPT pruning method (Men 2024).

Modelos testados:
- TinyLlama-1.1B (3T tokens, scratch) → recurrent (4,8,4) ou (6,10,6)
- OLMo-2-0425-1B
- Llama-3.2-1B (distilled de 3.1-8B/70B em 9T tokens)

### Diferenças de arquitetura vs Geiping
- **2 normalizações por decoder block** (vs 4 sandwich de Geiping) + remove dual-use de
  final layernorm
- Grouped-query attention (Ainslie 2023)
- Context length 1024 em treino
- Sem weight-tie entre embedding/unembedding (Geiping faz tied)

Mantém de Geiping: random s_0 ~ N(0, σ²), Poisson-Lognormal sampling de r com média 32,
truncated backprop k=8, scalable initialization de Takase 2023.

### Resultados-chave

**1. Pretrained init >> random init.** Treinando (2,4,2) Llama-init vs random sobre 120B
tokens FineWeb-Edu: Llama-init alcança loss menor consistentemente; em Hellaswag, modelo
pretrained-init já leverages recurrence em step 1000, enquanto random-init permanece em
random accuracy para todos r ∈ [1,2,4,8,16,32]. Extrapolação log-linear das loss curves:
**~950B tokens** para curvas se cruzarem (provavelmente subestimativa).

**2. Curriculum de recurrence.** Linearmente aumenta mean da Poisson-Lognormal de 1 → 32
ao longo do treino. Reduz FLOPs por step nas fases iniciais (forward dominante porque
backprop é truncado em k=8). Resultado: melhora loss vs FLOPs spent. "Gradual stacking"
analogue para depth-recurrent.

**3. Recurrent post-training > non-recurrent post-training para math.** Convertendo
TinyLlama/OLMo/Llama via Common Crawl math data: melhor GSM8K e MATH que post-training
the original non-recurrent model com mesmo compute budget. Confirma que depth-recurrence
**captura algo que extra training tokens em fixed-depth não captura**.

**4. Healing period.** Como remove layers no surgery, modelo perde basic LM performance
inicialmente. Healing period (continued pretraining em distribution-similar data antes de
math-specific) recupera language modeling antes de refinar reasoning.

### Cost accounting
FLOPs para recurrent: `(6N₁ + 2N₂)·D` onde N₁ = params com gradients (depende de k
truncado) e N₂ = params no forward sem gradient. Não é o `6ND` de Kaplan 2020.

## Interpretação

(⚠️ nossa interpretação) McLeish é o **passo de adoção** que faltava. Antes desse paper,
RDT exigia: comprar 800B tokens de compute ou viver com modelos toy. Agora: pegue
qualquer Llama-class model com pesos públicos, faça continued pretraining com curriculum
+ math data, e tem RDT funcional em ordem de grandeza menos compute. **Bar de entrada
caiu drasticamente.**

(⚠️ design analogy) O padrão "convert existing → enhanced via continued pretraining" é
estruturalmente análogo a outros enhancements pós-pretrain: instruction tuning,
RLHF, long-context extension (mencionado no paper como benchmark conceitual). Sugere
que **depth-recurrence pode virar mais um stage padrão no pipeline de treino LLM**, não
um paradigma alternativo competidor.

(⚠️ qualificador importante) Modelos testados são todos ≤1.1B. Não há evidência
empírica de que retrofit funciona em escala 7B+ ou 70B+. Concurrent work de
Koishekenov et al. 2025 (citado mas não comparado em FLOPs) tenta similar com OLMo mas
sem input injection e sem ganhos em escalonar test-time recurrence.

## Conexões
- supersedes (parcialmente): [[huginn-3.5b-recurrent-depth]] — viabiliza RDT sem pretrain
  from-scratch; mesmo grupo, mesma família arquitetural
- derivedFrom: Bae et al. 2024 — prior work em conversion via low-rank adapters; McLeish
  remove necessidade de adapters/distillation
- complementa: [[looped-transformer]] — adiciona caminho de adoção para a família
- complementa: ShortGPT (Men 2024) — pruning method comparado, McLeish vence

## Verificação adversarial

**Claim mais fraco:** "950B tokens para parity entre pretrained-init e random-init".
Extrapolação log-linear admitidamente subestimativa; curvas não são log-linear no fim
dos dados; comparação assume mesma trajetória. É evidência heurística, não rigorosa.

**O que o paper NÃO diz:**
1. Não testa retrofit em modelos > 1.1B params. Toda família Llama-class menor.
2. Não compara com extended thinking / o3-style scaling em mesma tarefa.
3. Não prova que conversion preserva instruction-following ou alignment de modelos
   distilled como Llama-3.2-1B.
4. Healing period em "minimal distribution shift" data é vago — paper não especifica
   métrica de "minimal".

**Simplificações feitas:** O paper tem extensa discussão sobre layer selection ablations
(Appendix Figs 12-14) que omiti — basicamente "early/later beats middle".

**Prior work citado:** Geiping 2025 (foundational), Bae et al. 2024 (prior conversion
attempt com adapters), Lan 2019 (ALBERT), Dehghani 2018 (Universal Transformer),
Csordás 2024, Saunshi 2025, Zeng 2025 (recurrent transformer studies), Schwarzschild
2021 (deep thinking), Bansal 2022, Hu 2022 (LoRA), Koishekenov 2025 (concurrent OLMo
conversion), Wang 2025 (HRM).

## Fontes
- [McLeish et al. 2025 — Teaching Pretrained LMs to Think Deeper with Retrofitted Recurrence](../../raw/papers/mcleish-2025-retrofitted-recurrence.md) — método, 3 modelos convertidos, curriculum de recurrence, healing period

## Quality Gate
- [x] Wikilinks tipados: 4 substituições (supersedes, derivedFrom, complementa×2)
- [x] Instance→class: claims numéricos qualificados (TinyLlama 3T, Llama 9T distilled, FineWeb-Edu 120B, ~950B parity tokens marcado como subestimativa)
- [x] Meta-KB separado: nenhuma referência a /ask/comandos
- [x] Resumo calibrado: "viabiliza adoção prática" não promete frontier-scale
