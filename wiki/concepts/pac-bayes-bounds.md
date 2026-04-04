---
title: "PAC-Bayes Bounds (Alquier 2024)"
sources:
  - path: raw/papers/alquier-pac-bayes-bounds.md
    type: paper
    quality: secondary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [machine-learning, generalization, ensemble, bayesian, statistical-learning, pac-bayes]
source_quality: medium
interpretation_confidence: high
quarantine: false
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: source
---

## Resumo

PAC-Bayes bounds (Shawe-Taylor & Williamson 1997; McAllester 1998; textbook treatment: Alquier 2024) fornecem limites de generalização para preditores agregados/aleatorizados. Core theorem: com probabilidade ≥ 1−δ, o risco verdadeiro E_{θ~ρ}[R(θ)] ≤ risco empírico + √(KL(ρ||π)/n). O prior π é livre (pode ser escolhido antes dos dados); o posterior ρ é o preditore a ser avaliado. KL(ρ||π) é o custo de complexidade. Aplicação a ensembles: PAC-Bayes bounds on neural networks têm sido non-vacuous pela primeira vez (Dziugaite & Roy 2017).

## Conteúdo

### Contexto: PAC bounds clássicos

**PAC (Probably Approximately Correct)**: dados S = {(xᵢ,yᵢ)}ⁿ i.i.d., queremos controlar o generalization gap R(θ) − r(θ), onde:
- R(θ) = risco verdadeiro: E_{(x,y)}[l(θ,(x,y))]
- r(θ) = risco empírico: (1/n)∑ l(θ,(xᵢ,yᵢ))

**PAC bound básico** (Proposition 1.1, Alquier 2024): Para θ fixo e δ ∈ (0,1):

P(R(θ) > r(θ) + √(log(1/δ)/(2n))) ≥ 1 − δ

**Problema**: para espaço de hipóteses Θ infinito, o union bound não funciona. PAC-Bayes resolve isso via prior/posterior.

### Core Theorem: PAC-Bayes Bound (Theorem 2.1, Alquier 2024)

**Setup**:
- π ∈ P(Θ): prior sobre hipóteses (escolhido **antes** de ver os dados)
- ρ ∈ P(Θ): posterior (qualquer distribuição, pode depender dos dados)
- l: perda bounded em [0, C]

**Theorem 2.1** (Alquier 2024, §2.1):

Para qualquer λ > 0, qualquer δ ∈ (0,1), com probabilidade ≥ 1−δ sobre S:

```
∀ρ ∈ P(Θ):  E_{θ~ρ}[R(θ)] ≤ E_{θ~ρ}[r(θ)] + λC²/8n + KL(ρ||π)/λ + log(1/δ)/λ
```

**Otimizando λ** = √(8n·KL(ρ||π)/C²):

```
E_{θ~ρ}[R(θ)] ≤ E_{θ~ρ}[r(θ)] + C√(KL(ρ||π)/(2n)) + log(1/δ)·C/(√(8nKL(ρ||π)))
```

**Termos do bound**:
1. **E_{θ~ρ}[r(θ)]**: risco empírico do ensemble com pesos ρ
2. **KL(ρ||π)/λ**: penalidade de complexidade — quanto o posterior se afasta do prior
3. **log(1/δ)/λ**: penalidade de confiança

### O prior e o posterior

**Prior π**: pode ser qualquer distribuição sobre Θ, escolhida a priori. Escolhas comuns:
- Gaussiano isotrópico N(0, σ²I) sobre parâmetros de rede neural
- Distribuição uniforme sobre conjunto finito de hipóteses

**Posterior ρ**: pode ser data-dependent. O bound vale para *todos* os ρ simultaneamente (quantificador ∀ρ), não just para ρ fixo.

**Gibbs measure ótima** (Lemma 2.2, Donsker & Varadhan 1976, via Alquier):

O ρ que maximiza E_{θ~ρ}[h(θ)] − KL(ρ||π) é o Gibbs measure:

πₕ(θ) ∝ π(θ) · eʰ⁽θ⁾

Para aprendizado com h(θ) = −λ·l(θ, S): πₕ(θ) ∝ π(θ) · e^{−λ·l(θ,S)} — exponential weighting dos preditores pela sua performance.

### PAC-Bayes em redes neurais (Dziugaite & Roy 2017, citado em Alquier)

**Problema histórico**: PAC bounds clássicos em redes neurais eram vacuous (bound ≥ 1 em classificação binária) porque Θ é muito grande.

**Resultado** (Dziugaite & Roy 2017): Com prior π = N(w₀, σ²I) onde w₀ são os pesos antes do treino e ρ = N(ŵ, s²I) onde ŵ são os pesos treinados:

KL(ρ||π) = ||ŵ−w₀||²/(2σ²) + ... ≈ norma dos ajustes de treino

Para redes com flat loss landscape, KL é pequeno → bounds não-vacuous pela primeira vez.

**Implicação**: PAC-Bayes captura a intuição de que "flat minima generalizam melhor" com garantias formais.

### Ensemble interpretation

**Aggregated predictor**: ŷ = E_{θ~ρ}[f(x;θ)] — média de preditores com pesos ρ.

**Randomized predictor**: θ ~ ρ, ŷ = f(x;θ) — amostrar um preditor.

PAC-Bayes bounds mostram: se ρ não se afasta muito do prior π (KL pequeno), o ensemble generaliza bem. O KL é o "preço" de especialização nos dados.

## Interpretação

### PAC-Bayes como foundation para ensembles de compiladores

⚠️ Interpretação nossa — não está em Alquier.

Em um KB com múltiplos LLMs como compiladores:
- θ = parâmetros de um compilador (ou identidade de um compilador específico)
- π = prior sobre compiladores antes de ver as fontes
- ρ = pesos aprendidos sobre compiladores após processar as fontes
- R(θ) = distortion do compilador θ em conteúdo não visto
- KL(ρ||π) = quanto o ensemble final divergiu do prior (especialização)

**Predição PAC-Bayes**: a taxa de generalization gap do ensemble é √(KL(ρ||π)/n) onde n = número de fontes. Isso fornece a foundation teórica para o tradeoff entre especialização (baixo risco empírico) e generalização (baixo KL).

### Relação com Partial Information Decomposition (PID)

⚠️ Interpretação nossa.

PID (Wibral) diagnóstica unique/shared/synergistic de compiladores. PAC-Bayes determina os pesos ρ ótimos para minimizar o bound. Juntos: PID diz *quanta* informação cada compilador contribui unicamente; PAC-Bayes determina *quanto peso* dar a cada compilador no ensemble final mantendo boa generalização.

## Verificação adversarial

**Claim mais fraco:** Bounds de PAC-Bayes são muitas vezes não-tight (loose) na prática — o bound de Dziugaite & Roy (2017) foi non-vacuous mas ainda conservativo (bound de 30-40% para erro de teste de 5%). A aplicabilidade depende da escolha de π.

**O que o monograph NÃO diz:**
- Não diz que PAC-Bayes é o único ou melhor método de regularização para ensembles
- Não resolve o problema de computar o posterior ótimo eficientemente para redes grandes
- Não conecta explicitamente PAC-Bayes a arquiteturas específicas de multi-agent KB

**Simplificações:** O bound assume perdas i.i.d. — fontes de uma KB não são i.i.d. (Bradford zones, correlações entre sources). A extensão para dados dependentes existe mas é mais complexa (Catoni 2007, van Erven e.a.).

**Prior work:** Shawe-Taylor & Williamson (1997), McAllester (1998) — bounds originais. Alquier (2024) é a introdução tutorial, não o paper de resultados novos.

## Quality Gate
- [x] Wikilinks tipados: `complementsAt: [[partial-information-decomposition]] ON "PID diagnostics + PAC-Bayes weights = ensemble design framework"`; `derivedFrom: [[information-theory-shannon]] ON "KL divergence como medida de complexidade"`
- [x] Instance→class: Theorem 2.1 é para perdas bounded em [0,C]; bound para Dziugaite & Roy é para redes neurais específicas — não generalizado
- [x] Meta-KB separado: aplicação a ensembles de compiladores em ## Interpretação com ⚠️
- [x] Resumo calibrado: "non-vacuous pela primeira vez" qualificado para Dziugaite & Roy 2017

## Níveis epistêmicos

### Descrição (verificado)
- Theorem 2.1 — no monograph de Alquier
- Gibbs measure como posterior ótimo — Lemma 2.2 no monograph
- PAC-Bayes em redes neurais (Dziugaite & Roy) — citado no monograph
- Prior/posterior interpretation — no monograph

### Interpretação (nossa aplicação)
- PAC-Bayes para ensembles de compiladores LLM — nossa interpretação
- Relação PID + PAC-Bayes para design de ensembles — nossa síntese

### Especulação
- (nenhuma)

## Conexões

- derivedFrom: [[information-theory-shannon]] ON "KL(ρ||π) generaliza entropia relativa de Shannon como complexidade de modelo"
- complementsAt: [[partial-information-decomposition]] ON "PID diagnostica informação única/compartilhada; PAC-Bayes pesa compiladores para minimizar generalization gap (⚠️ nossa síntese)"

## Fontes

- [Alquier (2024) — User-friendly Introduction to PAC-Bayes Bounds](../../raw/papers/alquier-pac-bayes-bounds.md) — Theorem 2.1, Gibbs measure, PAC-Bayes em redes neurais, ensemble interpretation
