---
title: "Rate Distortion Theory (Cover & Thomas Ch. 13)"
sources:
  - path: raw/papers/cover-thomas-elements-information-theory.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [information-theory, rate-distortion, compression, lossy-coding, foundational]
source_quality: high
interpretation_confidence: high
quarantine: false
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
---

## Resumo

Rate distortion theory (Shannon 1959; textbook treatment: Cover & Thomas 1991 Ch.13) establishes the fundamental limit of lossy source coding: R(D) = min I(X;X̂) over all encoders achieving expected distortion ≤ D. For a Gaussian source with squared error: R(D) = ½ log(σ²/D). For Bernoulli(½): R(D) = 1 − H(D). The rate distortion theorem proves these bounds are achievable and tight. Foundation for the Information Bottleneck (Tishby) and for the CEO problem (multi-terminal generalization).

## Conteúdo

### O problema de rate distortion

Dado um source X i.i.d. ~p(x) e uma distortion measure d(x,x̂):
- **Rate R**: bits per symbol necessários para descrever X
- **Distortion D**: expected reconstruction error Ed(X, X̂)
- **Tradeoff**: mais bits → menos distortion; menos bits → mais distortion

O problema básico: encontrar o mínimo R tal que distortion D é alcançável.

### Definições formais

**Distortion measure**: d: 𝒳 × 𝒳̂ → ℝ⁺

Exemplos comuns (Cover & Thomas 1991, §13.2):
- **Hamming**: d(x, x̂) = 0 se x = x̂, 1 caso contrário → probability of error
- **Squared error**: d(x, x̂) = (x − x̂)² → mais comum para fontes contínuas

**Rate distortion function** (definição operacional):

R(D) = inf{R : (R,D) é alcançável}

onde (R,D) alcançável significa: existem (2^nR, n) codes com lim_{n→∞} E[d(X^n, X̂^n)] ≤ D.

**Information rate distortion function** (definição matemática):

R^I(D) = min_{p(x̂|x): Σ p(x)p(x̂|x)d(x,x̂)≤D} I(X; X̂)

### Teorema principal (Theorem 13.2.1)

**Cover & Thomas (1991), Ch.13:**

> Para fonte i.i.d. X com distribuição p(x) e bounded distortion function d(x, x̂), o rate distortion function operacional é igual ao information rate distortion function:
>
> R(D) = R^I(D) = min_{p(x̂|x): E[d]≤D} I(X; X̂)

Este é o mínimo atingível — não há código que use menos bits e ainda atinja distortion D.

### Exemplos canônicos

**Fonte Bernoulli(p) com Hamming distortion** (Theorem 13.3.1):

R(D) = H(p) − H(D),   para 0 ≤ D ≤ min{p, 1−p}
R(D) = 0,              para D > min{p, 1−p}

Caso especial Bernoulli(½): R(D) = 1 − H(D). Para D = 0 (lossless): R = 1 bit = H(X). Para D = ½ (random guess): R = 0 bits.

**Fonte Gaussiana N(0, σ²) com squared error** (Theorem 13.3.3):

R(D) = ½ log(σ²/D),   para 0 ≤ D ≤ σ²
R(D) = 0,              para D > σ²

Interpretação: para atingir distortion D, precisamos de ½ log(σ²/D) bits por amostra.

**Multi-dimensional Gaussian** (§13.3.3): Reverse water-filling — alocar bits às dimensões com maior variância, zerar as dimensões com variância < D.

### Prova: estrutura (§13.4–13.5)

**Converse** (lower bound): Para qualquer código com distortion ≤ D,

nR ≥ H(X̂^n) − H(X̂^n|X^n) ≥ Σ I(Xi; X̂i) ≥ n R^I(D)

Por chain rule e convexidade de I(X;X̂).

**Achievability** (upper bound): Codebook aleatório de 2^{n(R^I(D)+ε)} codewords i.i.d. ~q(x̂) (output distribution). Encoder: encontra codeword x̂^n jointly typical com x^n. Pelo AEP: para n suficientemente grande, com alta probabilidade existe codeword jointly typical, e a distortion é ≤ D + ε.

### Propriedades de R(D)

1. R(D) é convexa e monótona decrescente em D
2. R(0) = H(X) (lossless = standard entropy)
3. R(D) = 0 para D ≥ D_max = min_{x̂} Σ p(x)d(x,x̂)
4. R(D) é contínua em D

### Computo: algoritmo de Blahut-Arimoto (§13.8)

Para calcular R^I(D) numericamente:

Iteração alternada:
1. q(x̂) → p*(x̂|x) via Lagrange: p*(x̂|x) ∝ q(x̂) exp(−λ d(x,x̂))
2. p*(x̂|x) → q(x̂) via marginalização: q(x̂) = Σ_x p(x) p*(x̂|x)

Converge para o mínimo global de I(X;X̂) sujeito a E[d] ≤ D (Cover & Thomas 1991, §13.8).

## Interpretação

### Rate distortion como framework unificador

⚠️ Interpretação nossa — não está explicitamente em Cover & Thomas nesta forma.

R(D) formaliza o tradeoff fundamental compression/fidelity. Duas conexões diretas:

1. **Information Bottleneck (Tishby 2000)**: o objetivo L = I(X̃;X) − βI(X̃;Y) é um problema de rate distortion com rate = I(X̃;X) e distortion = −I(X̃;Y). O β é o multiplicador de Lagrange λ da restrição de distortion. Tishby generalizou R(D) de distortion arbitrária para "relevância" como distortion.

2. **CEO Problem (Berger 1996)**: generalização de R(D) para múltiplos observadores. L agentes observam versões ruidosas X₁,...,X_L de uma fonte θ, codificam a taxas R₁,...,R_L, e um centro (CEO) reconstrói θ com distortion D. Rate distortion theory é o caso L=1. Ver raw/papers/courtade-ceo-problem.md.

### Lemma "joint é melhor que individual"

Cover & Thomas (1991, §13.1): "É mais simples descrever um elefante e um frango com uma descrição do que descrevê-los separadamente." Para X₁, X₂ independentes com distortion D:

R(X₁,X₂; D₁,D₂) ≤ R(X₁; D₁) + R(X₂; D₂)

O vetor de fontes pode ser descrito mais eficientemente do que a soma das descrições individuais. Isso motiva o Slepian-Wolf theorem (Ch14).

## Verificação adversarial

**Claim mais fraco:** A prova de achievability usa codebooks aleatórios — existência probabilística, não construção explícita. Para aplicações práticas, implementações eficientes (Huffman, arithmetic coding) existem apenas para casos especiais.

**O que o textbook NÃO diz:**
- Não cobre taxas variáveis ou codebooks adaptativos (fixed-block-length assumption)
- Não trata CEO problem (Post-1991; Berger 1996)
- Não discute implementações computacionalmente eficientes além de Blahut-Arimoto

**Simplificações:** A prova assume fonte i.i.d. — fontes com memória requerem extensão (entropia rate H(X∞) no lugar de H(X)).

**Prior work:** Shannon (1959) — "Coding theorems for a discrete source with a fidelity criterion" — é o paper original de rate distortion. Cover & Thomas é o tratamento textbook padrão.

## Quality Gate
- [x] Wikilinks tipados: `derivedFrom: [[information-theory-shannon]]` (R^I baseado em I(X;X̂)); `complementsAt: [[information-bottleneck]] ON R(D) ↔ IB Lagrangian`; `prerequisiteOf: [[network-information-theory]] ON Slepian-Wolf`
- [x] Instance→class: exemplos Bernoulli e Gaussiano apresentados com tipo de fonte e distortion explícitos; não generalizados para todos os casos
- [x] Meta-KB separado: conexões com CEO problem e Information Bottleneck em ## Interpretação
- [x] Resumo calibrado: sem oversell; caveats de implementação presentes

## Níveis epistêmicos

### Descrição (verificado)
- R(D) = min I(X;X̂) sujeito a E[d] ≤ D — definição formal do textbook
- Theorem 13.2.1 (R operacional = R^I) — prova no textbook
- Exemplos Bernoulli e Gaussiano — derivados no textbook
- Algoritmo Blahut-Arimoto — descrito no textbook

### Interpretação (nossa aplicação)
- R(D) como framework unificador de IB e CEO problem — não está nestes termos em Cover & Thomas

### Especulação
- (nenhuma)

## Conexões

- derivedFrom: [[information-theory-shannon]] — I(X;X̂) como base matemática; R(D) generaliza Shannon channel coding
- complementsAt: [[information-bottleneck]] ON "IB Lagrangian = R(D) com relevância como distortion" — ⚠️ nossa interpretação
- prerequisiteOf: [[network-information-theory]] ON "Slepian-Wolf e Wyner-Ziv são extensões de R(D) para múltiplas fontes"
- prerequisiteOf: [[team-decision-theory]] ON "CEO problem formaliza rate-distortion para L agentes paralelos"

## Fontes

- [Cover & Thomas — Elements of Information Theory, Ch. 13](../../raw/papers/cover-thomas-elements-information-theory.md) — R(D) definição, Theorem 13.2.1, exemplos Bernoulli/Gaussiano, algoritmo Blahut-Arimoto
