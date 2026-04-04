---
title: "Prospect Theory (Kahneman & Tversky 1979)"
sources:
  - path: raw/papers/kahneman-tversky-1979-prospect-theory.md
    type: paper
    quality: primary
    stance: challenging
created: 2026-04-04
updated: 2026-04-04
tags: [behavioral-economics, decision-theory, loss-aversion, value-function, utility-theory]
source_quality: high
interpretation_confidence: high
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-04
quarantine: false
provenance: source
---

## Resumo

Kahneman & Tversky (1979): teoria alternativa à utilidade esperada. Valor atribuído a ganhos e perdas (não a ativos finais); pesos de decisão substituem probabilidades. Função valor: côncava para ganhos, convexa para perdas, mais íngreme para perdas (loss aversion). Pesos de decisão: superpeso de probabilidades baixas, subpeso de altas. ~80k citações — paper mais citado de Econometrica.

## Conteúdo

### Por que utility theory falha descritivamente

4 classes de problemas demonstram violações sistemáticas da utilidade esperada:

**1. Certainty Effect:** Pessoas preferem um ganho certo a um provável maior esperado. Exemplo clássico:
- 80% chance de ganhar $4000 vs. certeza de $3000 → maioria escolhe certeza ($3000)
- Mas 20% chance de $4000 vs. 25% chance de $3000 → maioria escolhe $4000
- Inconsistente: ambas as escolhas envolvem proporções idênticas (multiplicadas por 0.25)

**2. Reflection Effect:** Abaixo do ponto de referência, as preferências se revertem:
- Perdas certas preferidas a perdas prováveis maiores (risk seeking in losses)
- Espelha exatamente o padrão de ganhos mas com sinal oposto

**3. Isolation Effect (Framing):** Quando um problema é decomposto, as pessoas descartam componentes comuns e focam no diferencial — levando a escolhas inconsistentes com representações equivalentes.

**4. Overweighting de probabilidades baixas:** Seguro e loteria têm apelo por razões simétricas: pequenas probabilidades de grande perda (seguro) e de grande ganho (loteria) são superweighted.

### A teoria formal

**Fase 1 — Editing:** O decisor formata a decisão: determina o ponto de referência, simplifica, cancela componentes comuns.

**Fase 2 — Evaluation:**

Valor de uma perspectiva (x₁, p₁; x₂, p₂):

**V = π(p₁)v(x₁) + π(p₂)v(x₂)**

Onde:
- v(x): **função valor** sobre ganhos/perdas em relação ao ponto de referência
- π(p): **pesos de decisão** (≠ probabilidades)

**Função Valor v(x):**
- Definida sobre ganhos e perdas (não riqueza absoluta)
- Côncava para ganhos: v(x) ~ xᵅ com α < 1
- Convexa para perdas: v(-x) ~ -λ(-x)ᵝ com β < 1
- Mais íngreme para perdas: λ > 1 (**loss aversion**)
- v(0) = 0; ponto de referência = status quo ou aspiration level

**Pesos de decisão π(p):**
- π(0) = 0, π(1) = 1
- Subaditividade: π(p) + π(1-p) < 1
- Superpeso de probabilidades pequenas: π(p) > p para p pequeno
- Subcerteza: π(p) < p para p moderado/alto
- NÃO são probabilidades — não somam a 1 em geral

### Loss aversion

Loss aversion é a assimetria fundamental: perdas doem mais do que ganhos equivalentes satisfazem. Estimativa de Kahneman & Tversky: λ ≈ 2 (perdas pesam ~2x ganhos de mesmo valor). Consequências:

- **Status quo bias:** Qualquer mudança é vista como potencial perda — inércia racional
- **Endowment effect (Thaler):** Posse de um objeto aumenta seu valor porque vender = perda
- **Equity premium puzzle:** Investidores exigem retorno muito alto em ações vs. bonds

### Diferença de utilidade esperada

| Dimensão | Utilidade Esperada | Prospect Theory |
|---|---|---|
| Avaliação sobre | Riqueza final | Ganhos/perdas relativas ao ref. |
| Pesos | Probabilidades | Pesos de decisão π(p) |
| Função de valor | Côncava global | Côncava ganhos, convexa perdas |
| Aspecto central | Consistência normativa | Descrição do comportamento real |

## Verificação adversarial

**Claim mais fraco:** Os parâmetros específicos (λ ≈ 2, α, β) foram estimados em experimentos de laboratório com pequenos ganhos hipotéticos — podem não escalar para decisões de alto stakes ou domínios não-monetários.

**O que o paper NÃO diz:** Não modela como o ponto de referência é determinado (lacuna central da teoria); não trata de prospectos com mais de 2 outcomes de forma completa; a fase de "editing" não é formalizada.

**Simplificações:** Cumulative Prospect Theory (Tversky & Kahneman 1992) corrige violações de dominância estocástica do modelo original — o paper de 1979 é tecnicamente supersedido por CPT, mas permanece a formulação-referência.

**Prior work:** Markowitz (1952) propôs função valor com ponto de referência; Edwards (1954) introduziu weighted utilities. K&T sistematizaram e testaram empiricamente de forma mais rigorosa.

## Conexões

- derivedFrom: [[heuristics-and-biases]] — Prospect Theory é a formalização matemática dos padrões de escolha descritos em K&T (1974); loss aversion implica que "framing" (isolation effect) gera escolhas inconsistentes
- complementsAt: [[fast-frugal-heuristics]] ON "ecological rationality" — Gigerenzer critica PT por assumir que desvios de EU theory são "erros"; PT responde com dados empíricos robustos
- contradicts: [[judgment-aggregation]] ON "individual rationality baseline" — PT mostra que mesmo a racionalidade individual é mais fraca do que Arrow assume; o problema de agregação de List & Pettit se agrava

## Fontes

- [Kahneman & Tversky — Prospect Theory](../../raw/papers/kahneman-tversky-1979-prospect-theory.md) — certainty effect, reflection effect, isolation effect, função valor, pesos de decisão, Econometrica 1979

## Níveis epistêmicos

### Descrição (verificado)
- 4 classes de violações da EU theory com experimentos específicos
- Função valor v(x): côncava ganhos, convexa perdas, assimétrica (loss aversion)
- Pesos de decisão π(p): super-peso de baixas probabilidades, sub-peso de altas

### Interpretação (nossa)
- Relação com Gigerenzer como complementar/crítico
- CPT (1992) como sucessor — não discutido no paper original

## Quality Gate
- [x] Wikilinks tipados: 3 (derivedFrom, complementsAt, contradicts)
- [x] Instance→class: λ ≈ 2 qualificado como estimativa de experimentos de laboratório
- [x] Meta-KB separado: sem referências a esta KB
- [x] Resumo calibrado: menção a ~80k citações como contexto de impacto, não como validação
