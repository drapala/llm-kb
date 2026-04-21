---
title: "Parcae — Estabilidade LTI para Looped Transformers (Prairie 2026)"
sources:
  - path: raw/papers/prairie-2026-parcae-stable-looped.md
    type: paper
    quality: primary
    stance: challenging
    challenging_type: content
created: 2026-04-19
updated: 2026-04-19
tags: [recurrent-depth, looped-transformer, stability, control-theory, spectral-norm, scaling-laws]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
topics: [recurrent-depth, looped-transformer, stability, scaling-laws]
depends_on:
  - raw/papers/prairie-2026-parcae-stable-looped.md
  - raw/papers/geiping-2025-recurrent-depth-huginn.md
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
---

## Resumo
Prairie et al. (2026, arXiv:2604.12946, Carnegie Mellon + UCSD) reformulam looped
transformers como sistema dinâmico tempo-variante e mostram que **instabilidade vem de
spectral norms grandes nos parâmetros de injeção**. Parcae é a arquitetura proposta:
constrange ρ(Ā)<1 via parametrização diagonal negativa discretizada. Resultado: 770M
Parcae ≈ 1.3B Transformer no benchmark Core, com 4.3-9.2% menos perplexidade que
Geiping/Huginn em escala equivalente.

## Conteúdo

### Reframe do problema
Looping da forma `h_{t+1} = h_t + Block(h_t, x)` é casteável como sistema dinâmico
não-linear tempo-variante sobre o residual stream. Aproximação linear do bloco resolve
para sistema **linear time-invariant (LTI)** governado por matriz Ā. Teoria clássica
de controle: convergência ↔ ρ(Ā) < 1 (spectral radius). Divergência ↔ residual stream
explode com t.

### Diagnóstico da instabilidade prévia
Para Huginn (Geiping 2025) e arquiteturas similares: parametrizações aprendidas de Ā têm
spectral norm > 1 com frequência → loss spikes + residual explosion em escala. Geiping
mitigou empiricamente combinando Pre-Norm + Post-Norm em sandwich, mas sem garantia
formal. Parcae fornece a garantia.

### Solução: Negative Diagonal Parameterization
Parametriza Ā via discretização de matriz diagonal negativa, garantindo construtivamente
spectral norm < 1. Adicionalmente normaliza a injeção do input. Estabiliza residual
stream `h_t` ao longo de loops sem precisar de schedule cuidadoso de learning rate ou
norm tricks ad-hoc.

### Resultados empíricos

**Validation perplexity** (mesmo dataset Huginn, fixado parameter + data budget):
- Parcae vs RDM (Huginn-style): -6.3% PPL em média
- Parcae vs Transformer fixed-depth matched-param: redução adicional 4.3-9.2%

**Core benchmark** (escala 1.3B):
- Parcae 1.3B vs Transformer 1.3B: +2.99 pontos Core, +1.18 pontos Core-Extended
- **Parcae 770M ≈ Transformer 1.3B em Core** (~half params, mesma qualidade)
- "Relative quality up to 87.5% de Transformer twice the size"

**Test-time scaling**: Parcae escala compute via loops com **decay exponencial saturante
predictível** — primeira lei de escala para test-time looping.

### Scaling laws
Power laws derivadas para training: dado FLOP budget fixo, **looping e dados devem
escalar em tandem**. Não basta empilhar loops sem mais dados — diferente de inference-time
scaling onde loops sozinhos ganham.

### Setup experimental
- Datasets: Huginn-pretraining mix (RDMs) + FineWeb-Edu (Transformer baselines, Karpathy 2024)
- Parcae max loops: 8 em training principal; ablações até 16
- Comparações against Geiping et al. (2025) RDM e standard Transformer matched-param

## Interpretação

(⚠️ nossa interpretação) Parcae é **content-challenging** de Huginn: prova formalmente
que a estabilidade de Geiping era frágil (resolveu na prática via sandwich norm mas sem
garantia teórica) e oferece arquitetura strictly better via control theory. Geiping
reconheceu o problema no próprio paper ("normalization is required to train recurrence
at scale") mas não derivou condição formal. Parcae fecha o loop teórico.

(⚠️ design analogy) ρ(A)<1 é o análogo discreto de "operador contractivo" em
[[fixed-point-iteration]] e em Deep Equilibrium Models (Bai 2019, citado por Geiping).
A família toda RDT é variação do mesmo tema: operadores estáveis sobre estado latente.
Parcae torna explícita a teoria que já estava implícita em todos os predecessores.

(⚠️ qualificador importante) Resultados são em modelos ≤1.3B params com 100B tokens —
escala intermediária. Geiping treinou 3.5B/800B; McLeish converte modelos pretrained.
Parcae não testa retrofit. Família ainda em consolidação prática em escalas frontier.

## Conexões
- contradicts: claim implícito de [[huginn-3.5b-recurrent-depth]] que sandwich
  normalization é solução suficiente para estabilidade — Parcae prova que é
  workaround, não fix
- supersedes (parcialmente): [[huginn-3.5b-recurrent-depth]] em estabilidade — Parcae
  é arquitetonicamente mais limpa para o mesmo problema
- complementa: [[looped-transformer]] — adiciona teoria de controle ao framework geral
- complementa: [[mcleish-2025-retrofitted-recurrence]] — McLeish ataca eficiência de
  treino; Parcae ataca estabilidade arquitetural; ambos são otimizações ortogonais
  sobre Geiping

## Verificação adversarial

**Claim mais fraco:** "770M Parcae ≈ 1.3B Transformer". Métrica é Core benchmark
específico — não SWE-bench, MATH, ou reasoning real. Comparação assume mesmo training
budget e dataset; pode não generalizar para domínios fora do mix avaliado.

**O que o paper NÃO diz:**
1. Não testa Parcae em modelos > 1.3B params (Huginn é 3.5B).
2. Não compara com modelos extended-thinking (o3, R1) em reasoning benchmarks.
3. Não retrofita modelos pretrained (gap que McLeish 2025 cobre para Huginn-style).
4. Aproximação linear assume regime perto do equilíbrio — pode falhar para tarefas que
   genuinamente precisam não-linearidade longa (Parcae §reconhece como limitation).

**Simplificações feitas:** Omiti detalhes de "discretization scheme" da matriz diagonal
negativa (paper §3.3) — relevante para reprodução, não para retrieval conceitual.

**Prior work citado relevante para a KB:** Geiping 2025 (Huginn, baseline RDM), Bai
2019 (Deep Equilibrium Models, prior em operadores convergentes), Karpathy 2024
(FineWeb-Edu Transformer recipe), Schwarzschild 2021 (deep thinking).

## Fontes
- [Prairie et al. 2026 — Parcae: Scaling Laws For Stable Looped Language Models](../../raw/papers/prairie-2026-parcae-stable-looped.md) — LTI reframe; spectral norm constraint via diagonal negativa; 770M ≈ 1.3B Transformer Core; lei de escala test-time looping

## Quality Gate
- [x] Wikilinks tipados: 4 substituições (contradicts, supersedes, complementa×2)
- [x] Instance→class: claims numéricos qualificados (770M Parcae no Core benchmark; -6.3% PPL vs Huginn em parameter+data matched setup)
- [x] Meta-KB separado: nenhuma referência a comandos KB
- [x] Resumo calibrado: "770M ≈ 1.3B" com qualificador "Core benchmark"
