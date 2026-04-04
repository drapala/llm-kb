---
title: "Rational Inattention (Sims 2003)"
sources:
  - path: raw/papers/sims-rational-inattention.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [information-theory, bounded-rationality, economics, channel-capacity, decision-theory, lateral]
source_quality: high
interpretation_confidence: medium
quarantine: false
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: source
---

## Resumo

Sims (2003): agentes têm capacidade limitada de processamento de informação, formalizada como restrição de Shannon channel capacity C sobre o canal entre observações e ações. Para Gaussian X, a constraint resulta em Var(Y|X) = Var(X)/e^{2C} — comportamento idêntico a signal-extraction, mas com predições diferentes quando a distribuição de X muda. Aplicações: price stickiness em macroeconomia, atenção seletiva em mercados financeiros.

## Conteúdo

### Motivação

Sims (2003) enquadra a rational inattention como alternativa ao modelo de "sticky prices" de Keynes: ao invés de postular rigidez de preços como exógena, deriva-a da capacidade limitada de agentes de processar informação. O mecanismo é aplicável a qualquer situação onde agentes devem tomar decisões com base em observações ruidosas (Sims 2003, Introduction).

Objetivo: substituir o "information delay" (informação disponível só com atraso) por um modelo de capacidade de canal — mais fundamental, sem dependência dos detalhes de como a informação é processada.

### Formalismo

**Constraint de informação** (Sims 2003, §III, eq. 5-6):

Agente observa X através de canal com capacidade C. A ação Y pode depender de X apenas via um canal cuja mutual information não excede C:

I(X; Y) ≤ C

onde C é medido em bits/observação.

**Problema de otimização** (Sims 2003, eq. 3-6):

```
min E[(Y − X)²]
q(y|x)
s.t.   I(X; Y) ≤ C
```

onde q(y|x) é a distribuição condicional de ação dado observação.

**Solução para X Gaussiano** (Sims 2003, §III):

Quando X ~ N(0, σ²), a distribuição ótima q(y|x) é Gaussiana com:
- Y | X ~ N(αX, σ²ₑ) para algum α
- Var(Y|X) = σ²/e^{2C}
- A ação Y age como se X fosse observado com ruído Gaussiano i.i.d.

O resultado *parece* um signal-extraction outcome, mas as predições diferem quando a distribuição de X muda (ver abaixo).

### Predições distintas das rational expectations

**Rational expectations**: se Var(X) dobra, o agente observa X com a mesma precisão absoluta (o "noise" é fixo externamente).

**Rational inattention**: se Var(X) dobra mantendo C constante, Var(Y|X) dobra proporcionalmente — o agente automaticamente ajusta sua atenção para a magnitude dos sinais relevantes.

Esta diferença é a base empírica do modelo: a resposta de agentes a mudanças na distribuição de shocks difere das predições de rational expectations com information delays (Sims 2003, §III).

### Aplicações econômicas (Sims 2003, §IV–V)

**Dynamic optimization com information constraints**:
- Agente controla estado Sₜ, observa Xₜ através de canal com capacidade C
- Solução: Y*ₜ aproxima "slow" adjustment — ação responde gradualmente às mudanças
- Este gradual adjustment assemelha-se a price stickiness sem postulá-la

**Price stickiness endógena**:
- Produtores têm capacidade limitada para processar informações de mercado
- Com C pequeno, preços respondem pouco a choques de demanda no curto prazo
- Implicação para política monetária: mudanças de regra não produzem jumps imediatos

**Observação empírica**: Sims (2003) cita convergência com evidências macroeconométricas sobre sluggish price adjustment — compatível com sticky-price predictions mas com microfundamentos diferentes.

### Limitações do modelo (Sims 2003, §VI e notas)

1. **Coding delay ignorado**: optimal coding geralmente introduz delay; Sims assume coded signal disponível no mesmo período t — justificado por declínio exponencial do gap com code length
2. **Capacidade como scalar**: C é um único número; sistemas reais têm capacidade diferenciada por tipo de informação
3. **Gaussiano como caso focal**: solução explícita apenas para distribuições Gaussianas; não-Gaussiano requer numerical methods

## Interpretação

### Rational inattention como instância de rate distortion

⚠️ Interpretação nossa — o mapeamento formal não está em Sims nesta forma.

A constraint I(X; Y) ≤ C com minimização de E[(Y-X)²] é equivalente ao problema de rate distortion (Cover & Thomas, Ch.13) com:
- Fonte = X
- Representação = Y (ação)
- Distortion = squared error
- Rate = capacidade de canal C

A solução Var(Y|X) = Var(X)/e^{2C} é exatamente R(D) Gaussiano invertido: D = σ²/e^{2C}.

Portanto, rational inattention é rate distortion theory aplicada à cognição econômica — o agente opera no tradeoff R(D) ótimo entre atenção (bits) e precision (distortion) de suas ações.

### Conexão com CEO problem

⚠️ Interpretação nossa.

O CEO problem (Courtade 2014) generaliza rational inattention para L agentes paralelos observando a mesma fonte X. Se cada agente tem capacity Cᵢ:
- Rational inattention = CEO problem com L=1
- A rate region do CEO problem define quais combinações (C₁,...,C_L) são suficientes para alcançar distortion D coletivamente

### Conexão com V(LLM) como capacidade de canal

⚠️ Interpretação especulativa nossa.

Sims formaliza V(R) em termos de Shannon channel capacity C. A Predição D de Ashby (error floor mensurável via V gap) torna-se operacionalizável: o error floor de cada compilador LLM = Var(X)/e^{2C_LLM} — mas C_LLM não é medida diretamente. A analogia é sugestiva, não mensurável sem empirismo adicional.

## Conexões

- instancia: [[fast-frugal-heuristics]] ON "⚠️ regime onde heurísticas frugais ganham = regime onde constraint I(X;Y)≤C é binding; ecological rationality ≈ optimal attention allocation (nossa interpretação, L1)"
- emerge-para: [[binding-attention-regime]] ON "binding regime como conceito unificador entre Sims e Gigerenzer"

## Verificação adversarial

**Claim mais fraco:** A derivação da price stickiness endógena depende de C pequeno — se C é alto (agente muito atento), o modelo colapsa para rational expectations. Sims não estima C empiricamente; a calibração é qualitativa.

**O que o paper NÃO diz:**
- Não diz que agentes *devem* ter capacidade C específica — C é parâmetro exógeno
- Não resolve o caso não-Gaussiano analiticamente
- Não testa empiricamente contra alternativas (behavioral economics, sticky information)

**Simplificações:** O modelo usa capacity constraint escalar; sistemas reais provavelmente têm múltiplos canais com capacidades diferentes para tipos distintos de informação.

**Prior work:** Shannon (1948) — fundamentos de channel capacity. Sims aplicação original a macroeconomia; Woodford (2009), Maćkowiak & Wiederholt (2009) — extensões no mesmo espírito.

## Quality Gate
- [x] Wikilinks tipados: `derivedFrom: [[information-theory-shannon]]`; `derivedFrom: [[rate-distortion-theory]] ON I(X;Y)≤C = rate distortion Gaussiano`; `complementsAt: [[ceo-problem]] ON L=1 special case`
- [x] Instance→class: Var(Y|X) = σ²/e^{2C} é resultado para X Gaussiano, não para distribuições gerais; qualificado no texto
- [x] Meta-KB separado: interpretação V(LLM) como capacidade em ## Interpretação com ⚠️
- [x] Resumo calibrado: "predições diferentes" qualificado — só diferentes quando distribuição de X muda

## Níveis epistêmicos

### Descrição (verificado)
- Constraint I(X;Y) ≤ C — formal model do paper
- Solução Gaussiana Var(Y|X) = σ²/e^{2C} — derivada no paper
- Price stickiness endógena — argumentada no paper
- Diferenças de predição vs rational expectations — demonstradas no paper

### Interpretação (nossa aplicação)
- Rational inattention = rate distortion aplicada à cognição econômica
- Conexão com CEO problem como L=1 special case

### Especulação
- V(LLM) operacionalizável via C_LLM — sugestivo, não mensurável sem dados

## Conexões

- derivedFrom: [[information-theory-shannon]] — I(X;Y) ≤ C usa mutual information de Shannon
- derivedFrom: [[rate-distortion-theory]] ON "rational inattention = rate distortion com distortion = squared error e rate = C"
- complementsAt: [[ceo-problem]] ON "CEO problem = rational inattention com L agentes paralelos (⚠️ nossa interpretação)"

## Fontes

- [Sims (2003) — Implications of Rational Inattention](../../raw/papers/sims-rational-inattention.md) — I(X;Y)≤C constraint, Gaussian solution, price stickiness derivation, macroeconomic applications
