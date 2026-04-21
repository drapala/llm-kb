---
title: "Huginn-3.5B (Geiping 2025) — Foundational Recurrent-Depth Pretrained Model"
sources:
  - path: raw/papers/geiping-2025-recurrent-depth-huginn.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/lu-2025-latent-cot-huginn.pdf
    type: paper
    quality: primary
    stance: challenging
    challenging_type: content
created: 2026-04-19
updated: 2026-04-19
tags: [architecture, recurrent-depth, latent-reasoning, inference-time-compute, pretraining]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
topics: [recurrent-depth, transformer-architecture, inference-time-compute, latent-reasoning, pretraining]
depends_on:
  - raw/papers/geiping-2025-recurrent-depth-huginn.md
  - raw/papers/lu-2025-latent-cot-huginn.pdf
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
---

## Resumo
Huginn-3.5B (Geiping et al. 2025, arXiv:2502.05171) é o primeiro modelo recurrent-depth
treinado em escala (3.5B params, 800B tokens, AMD Frontier). Demonstra empiricamente que
loop depth em inferência pode equivaler computacionalmente a ~50B params, validando
test-time compute scaling como terceiro eixo (além de tokens-out e parâmetros).

## Conteúdo

### Arquitetura macro: Prelude → Recurrent Block → Coda
Decoder-only transformer organizado em três grupos funcionais:
- **Prelude P** (l_P=2 layers): embedding de tokens em espaço latente
- **Recurrent block R** (l_R=4 layers): bloco central iterado r vezes
- **Coda C** (l_C=2 layers): un-embedding + prediction head

Forward pass para r iterações:
- `e = P(x)` — embedding fixo
- `s_0 ~ N(0, σ²·I)` — estado latente inicial **aleatório** (path independence)
- `s_i = R(e, s_{i-1})` para i ∈ {1,...,r} — recorrência com **re-injeção de e em cada
  passo**
- `p = C(s_r)` — vocab prob

Forma compacta: triplet `(l_P, l_R, l_C) = (2, 4, 2)`. Modelo final tem apenas **8
camadas "reais"**, mas com r=32 unfolds para profundidade efetiva 2 + 4·32 + 2 = **132
camadas**.

### Decisões de design não-óbvias

**Re-injeção de e a cada step** (não só em s_0): se e fosse fornecido só na inicialização,
R não poderia ser operador monótono dependente dos dados — análogo direto a gradient
descent que precisa do dado y a cada iteração para convergir.

**Random s_0** (não zero, não embedding): garante **path independence** (Anil 2022) —
o estado estável não depende da inicialização específica.

**Concatenação ao invés de soma** no adapter A: `R(e, s) = adapter([e; s])`. Em pequena
escala soma e concatenação funcionam igual; em escala, concatenação vence.

**Sandwich normalization** (4 RMSNorms por layer):
```
x̂_l = n_2(x_{l-1} + Attn(n_1(x_{l-1})))
x_l = n_4(x̂_l + MLP(n_3(x̂_l)))
```
Necessário para estabilizar recorrência em escala — pre/post-norm padrão falham.

**Não usa step embedding R_i(·)**: variantes diffusion-style (Peebles & Xie 2023) com
core dependente do passo i quebram path independence e impedem extrapolação.

### Training objective: log-normal Poisson sampling de r

Otimiza `E_{x∈X} E_{r∼Λ} L(m_θ(x, r), x')` onde Λ é log-normal Poisson com média r̄+1
e variância σ²=½. Distribuição samplea principalmente valores menores que r̄ mas tem
**heavy tail** com iterações ocasionalmente muito altas — força o modelo a generalizar
para r não vistos.

**Truncated backprop através das últimas k=8 iterações**: gradiente atravessa apenas
as 8 últimas iterações da recorrência. Mantém compute/memória de backward independente
de r, permitindo Λ heavy-tailed sem custo proibitivo. Análogo a TBPTT em RNNs, mas
recurrent in depth not time. Prelude ainda recebe gradiente em todo step (e é
re-injetado).

### Treinamento em escala
- 3.5B parâmetros: 1.5B prelude+coda + 1.5B core recurrent + 0.5B embeddings
- Hidden h=5280, 55 heads × 96, MLP inner 17920
- r̄=32 (média de iterações em treino)
- 800B tokens, AMD Frontier cluster
- Tokenizer BPE 65536 treinado sobre instruction-data split
- Mistura de pretraining heavily skewed para code + math reasoning
- Initialization de Takase 2024: σ²_h = 2/(5h), out-projection σ² = 1/(5hl) com
  l = l_P + r̄·l_R + l_C

### Resultados em escala
Performance escala monotonicamente com r até equivalente a ~50B params em benchmarks de
raciocínio. Comportamentos emergentes em latente: visualizações em §7 mostram trajetórias
"orbitando" para tarefas numéricas — indício de que computação iterativa em vetor
high-dim explora múltiplas direções simultaneamente, não apenas refinement linear.

### Releases públicas
- Modelo: `huggingface.co/tomg-group-umd/huginn-0125`
- Code + data: `github.com/seal-rg/recurrent-pretraining`
- Checkpoints intermediários disponíveis

## Interpretação

(⚠️ nossa interpretação) Huginn é o "GPT-2 moment" para recurrent-depth: prova que o
paradigma escala empiricamente além de small-scale toy tasks. Antes de Huginn, RDT era
literatura de "deep thinking" (Schwarzschild 2021/2023, Bansal 2022) restrita a tarefas
algorítmicas controladas. Geiping 2025 demonstra que a arquitetura **pretreina** com
dados de linguagem natural sem demonstrações especializadas.

(⚠️ design analogy) A separação prelude/recurrent/coda é estruturalmente análoga ao
padrão **encoder/processor/decoder** de Neural Algorithmic Reasoning (Veličković):
embedding fixo → loop iterativo de raciocínio → projeção para output space. Mesmo padrão
em [[looped-transformer]] (Kohli 2026 GPT-2 style) e em URM (Gao 2025 ARC-AGI).

(⚠️ qualificador importante) Lu et al. 2025 (já no wiki) é challenging direto deste
paper: probing de Huginn mostra que **scaling de recurrence em GSM8K é marginal**
(4.93% w/o CoT vs 24.87% com CoT externo). Latent reasoning demonstrável **não** se
materializa em aritmética real — apenas em tarefas onde latente é o único canal. Huginn
prova viabilidade arquitetural; não prova que latent reasoning vence CoT verbal em
tarefas naturais.

## Conexões
- instanceOf: [[looped-transformer]] — Huginn é a primeira instância pretreinada em
  escala da família recurrent-depth
- contradicts: claim implícito "scaling latent recurrence supera CoT" — refutado por
  [[looped-transformer]] §Lu 2025
- supersededBy: [[mcleish-2025-retrofitted-recurrence]] (parcialmente) — McLeish mostra
  que retrofit de modelos pretrained não-recorrentes é mais eficiente que pretrain
  from-scratch como Huginn
- supersededBy: [[parcae-lti-stable-looped]] (parcialmente, em estabilidade) — Parcae
  prova formalmente que sandwich norm de Geiping é workaround; ρ(Ā)<1 via diagonal
  negativa é solução teórica
- complementa: [[depth-extrapolation-recurrent]] — Huginn demonstra extrapolation
  empírica em escala; Kohli formaliza fenômeno em setup controlado

## Verificação adversarial

**Claim mais fraco:** "compute equivalente a 50B params". Métrica é benchmark-dependent
(reasoning tasks específicos) e não controla por arquitetura/training-data do baseline
50B. Comparação não é apples-to-apples — qualquer claim de "X params equivalente" sem
controlar tokens vistos, dataset, e benchmark mix é fraco.

**O que o paper NÃO diz:**
1. Não prova que Huginn vence GPT-3.5/Claude/Gemini em qualquer benchmark — apenas que
   escala internamente com r.
2. Não compara contra modelos com extended thinking (o3, DeepSeek R1) head-to-head em
   reasoning benchmarks reais.
3. Não resolve overthinking — paper §5 reporta que após r grande, performance estabiliza
   ou degrada (consistente com Kohli 2026).
4. Path independence é teórica (Anil 2022) mas não medida diretamente em escala — só
   inferida do fato de que modelo extrapola.

**Simplificações feitas neste artigo:** O paper tem extensos detalhes sobre dataset
mixture (Appendix C), AMD Frontier infra (Section 4), e adaptive halting strategies
(KL-divergence baseado) que omiti. Halting é coberto em [[looped-transformer]] §Estratégias.

**Prior work citado:** Universal Transformer (Dehghani 2019), ALBERT (Lan 2020), deep
thinking (Schwarzschild 2021/2023, Bansal 2022), Anil 2022 (path independence), Bauschke
2011 (monotone operators), Levine 2021 e Merrill 2022 (depth limits de transformers
fixos), Kaplan 2020 (scaling laws), Skean/Sun 2024 (analysis de layer roles).

## Fontes
- [Geiping et al. 2025 — Scaling up Test-Time Compute with Latent Reasoning](../../raw/papers/geiping-2025-recurrent-depth-huginn.md) — paper foundational; arquitetura Prelude/Recurrent/Coda; 3.5B params; 800B tokens; r̄=32; truncated backprop k=8; AMD Frontier
- [Lu et al. 2025 — Latent CoT? Decoding the Depth-Recurrent Transformer](../../raw/papers/lu-2025-latent-cot-huginn.pdf) — challenging direto: GSM8K probing mostra ganhos latentes marginais

## Quality Gate
- [x] Wikilinks tipados: 4 substituições (instanceOf, contradicts, supersededBy, complementa)
- [x] Instance→class: claims numéricos qualificados (3.5B/800B/AMD Frontier; r̄=32; equiv "50B" marcado como benchmark-dependent)
- [x] Meta-KB separado: nenhuma referência a /ask ou comandos da KB no ## Conteúdo
- [x] Resumo calibrado: 50B equivalence apresentada como "computacionalmente" não "performance-wise"
