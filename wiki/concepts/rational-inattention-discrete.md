---
title: "Rational Inattention to Discrete Choices (Matějka & McKay 2011)"
sources:
  - path: raw/papers/matejka-mckay-2011-rational-inattention-discrete-choices.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [information-theory, decision-theory, rational-inattention, discrete-choice, logit, bounded-rationality, lateral]
source_quality: high
interpretation_confidence: high
resolved_patches: []
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-12
quarantine: false
provenance: source
---

## Resumo

Matějka & McKay (2011): quando um agente racionalmente inattentive escolhe entre N alternativas discretas com informação custosa, a estratégia ótima segue exatamente o multinomial logit: `P_i = e^{q_i/λ} / Σ_j e^{q_j/λ}`, onde λ é o custo unitário de informação. Estende Sims (2003) do domínio Gaussiano contínuo para escolhas discretas. Resultado analiticamente tratável — o caso contínuo exige métodos numéricos fora do Gaussiano; o discreto tem solução fechada.

## Conteúdo

### O modelo

DM escolhe entre N opções. Valor da opção i: q_i (incerto, distribuição conjunta g(q⃗)). Custo de processar informação quantificado por mutual information I(q⃗; i), controlado pela distribuição condicional que o DM escolhe.

**Problema de otimização** (eq. 2-4):

```
max   Σᵢ Pᵢ⁰ ∫ qᵢ f(q⃗|i) dq⃗ − λκ
s.t.  I(q⃗; i) ≤ κ               [restrição de capacidade]
      Σᵢ Pᵢ⁰ f(q⃗|i) = g(q⃗)     [consistência bayesiana]
      Σᵢ Pᵢ⁰ = 1, Pᵢ⁰ ∈ [0,1]
```

λ = Lagrange multiplier da restrição de capacidade (se κ exógeno) OU shadow price da atenção (se λ exógeno, κ escolha do agente).

### Resultado principal (Theorem 1 + Theorem 3)

**Solução geral** (Theorem 1): probabilidade de escolher i dado q⃗:

```
P_i(q⃗) = [Pᵢ⁰ · e^{q_i/λ}] / [Σⱼ Pⱼ⁰ · e^{q_j/λ}]
```

onde Pᵢ⁰ = probabilidade *a priori* de selecionar i (antes de processar informação).

**Caso simétrico** (Theorem 3): quando as N opções são *ex ante* simétricas (prior g(q⃗) é simétrico nas permutações dos índices), Pᵢ⁰ = 1/N para todo i, e a equação simplifica para:

```
P_i(q⃗) = e^{q_i/λ} / Σⱼ e^{q_j/λ}
```

**que é exatamente o multinomial logit.**

O parâmetro λ é: não uma escolha ad hoc de temperatura, mas o **custo marginal de um bit de informação**. Isso dá a interpretação: λ grande = informação cara = agente mais ruidoso. λ → 0 = informação gratuita = agente perfeitamente atento.

### Limites do λ

| λ | Comportamento | Análogo |
|---|---------------|---------|
| λ → 0 | P_best → 1 (seleciona melhor com certeza) | Agente perfeitamente atento |
| λ → ∞ | P_i → 1/N (escolha uniforme, ignora tudo) | Inattention total |
| λ finito | Logit probabilístico ponderado por priors | Inattention parcial ótima |

### Prior assimétrico e IIA

Com prior assimétrico, a solução geral incorpora Pᵢ⁰ como peso adicional: opções com alta probabilidade *a priori* têm vantagem mesmo após processar informação.

**Resultado sobre IIA** (§3.1, §5.2): o modelo viola IIA (independência de alternativas irrelevantes) quando o prior é assimétrico — porque adicionar opções muda os Pᵢ⁰. No caso simétrico, IIA se mantém (os Pᵢ⁰ = 1/N são invariantes).

**Opções duplicadas** (Proposition 4, §5.2): o DM racionalmente inattentive trata duplicatas como uma única opção — resolve o famoso paradoxo dos ônibus de Debreu. O multinomial logit padrão falha neste caso; o modelo de rational inattention não.

### Conexão com Sims (2003)

Sims (2003): caso Gaussiano contínuo, solução: Var(Y|X) = Var(X)/e^{2C}. Matějka & McKay: caso discreto, solução: logit. Ambos são instâncias do mesmo framework de rational inattention (minimização de custo de mutual information). O discreto é mais tratável analiticamente.

## Interpretação

### Logit como microfundamento de attention

⚠️ Nossa interpretação — não está explicitamente em Matějka & McKay nesta forma.

Antes de Matějka & McKay, o logit era justificado por: (a) Random Utility Model (ruído exógeno), ou (b) Choice Axiom de Luce. O paper oferece terceira justificação: o logit emerge da **solução ótima de um agente que escolhe como alocar atenção escassa entre opções**. Não é ruído — é incerteza residual ótima dada capacidade limitada.

Implicação: λ não é um parâmetro de ajuste sem interpretação — é mensurável em princípio (custo marginal de atenção). Isso tem implicações empíricas: se λ muda com os stakes (apostas maiores → mais atenção → λ menor), o modelo faz previsões diferentes da versão padrão do logit.

### Relação com Take-the-Best (Gigerenzer)

⚠️ Nossa interpretação — não cita Gigerenzer.

A solução ótima de Matějka & McKay é o logit, não o Take-the-Best. Mas as duas convergem em um regime específico: quando os valores das opções diferem muito (`|q_best - q_second| >> λ`), o logit concentra probabilidade ≈ 1 na melhor opção — comportamento que Take-the-Best replica usando apenas o cue mais válido.

Portanto: **Take-the-Best não é a solução geral de rational inattention para escolhas discretas — é uma aproximação válida quando o ambiente tem dominância clara de uma opção.** Gigerenzer's ecological rationality identifica os ambientes onde essa aproximação é boa.

## Verificação adversarial

**Claim mais fraco:** O Theorem 3 requer que as opções sejam *ex ante* simétricas — condição forte. Em muitos problemas reais, o prior é assimétrico e a solução geral (com Pᵢ⁰) é mais difícil de calcular.

**O que o paper NÃO diz:**
- Não deriva Take-the-Best como caso especial — a solução é sempre logit
- Não modela capacidade de atenção diferenciada por tipo de informação (C é escalar)
- Não conecta ao resultado de Gigerenzer — ausência notável dado o overlap conceitual

**Simplificações:** Working paper (2011) — versão publicada (AER 2015) tem extensões não cobertas aqui.

**Prior work:** Sims (1998, 2003) — rational inattention Gaussiana. Luce (1959) — axiomática do logit. McFadden (1974) — random utility model para logit. Este paper é a primeira derivação do logit via rational inattention com restrição de fluxo de informação explícita.

## Quality Gate
- [x] Wikilinks tipados: instancia/extends
- [x] Instance→class: Theorem 3 especifica ex ante symmetric — não é afirmação geral
- [x] Meta-KB separado: implicações para retrieval em ## Interpretação
- [x] Resumo calibrado: menciona que é working paper e que AER 2015 tem extensões

## Níveis epistêmicos

### Descrição (verificado)
- Theorem 1: solução geral com prior assimétrico (eq. 10) — do paper
- Theorem 3: solução simétrica = multinomial logit — do paper
- λ = shadow price de atenção — do paper (§2)
- Duplicatas tratadas como opção única — Proposition 4 + Corollary 5 do paper
- λ → 0: perfeita atenção; λ → ∞: inattention total — do paper

### Interpretação (nossa)
- Logit como terceiro microfundamento (além de RUM e Luce) — nossa síntese
- Relação com Take-the-Best: aproximação boa quando dominância clara — nossa interpretação

## Conexões

- extends: [[rational-inattention]] ON "caso Gaussiano contínuo de Sims → caso discreto com solução logit fechada"
- validates: [[binding-attention-regime]] ON "formaliza rational inattention discreta; esclarece que solução ótima é logit, não Take-the-Best"
- derivedFrom: [[information-theory-shannon]] ON "mutual information I(X;Y) como métrica de custo de atenção"
- relaciona: [[fast-frugal-heuristics]] ON "⚠️ Take-the-Best ≈ logit quando dominância clara (|q_best - q_second| >> λ); não é equivalência geral"

## Fontes

- [Matějka & McKay (2011) — Rational Inattention to Discrete Choices](../../raw/papers/matejka-mckay-2011-rational-inattention-discrete-choices.pdf) — Theorem 1 (solução geral), Theorem 3 (logit simétrico), λ como custo de atenção, paradoxo de Debreu resolvido. CERGE-EI WP 442, publicado AER 2015.
