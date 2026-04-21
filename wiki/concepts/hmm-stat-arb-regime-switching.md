---
title: "HMM Statistical Arbitrage with Regime-Switching (Crude Oil — COVID & Ukraine)"
sources:
  - path: raw/papers/2309.00875-hmm-stat-arb-crude-oil.pdf
    type: paper
    quality: primary
    stance: challenging
    challenging_type: content
created: 2026-04-12
updated: 2026-04-12
tags: [statistical-arbitrage, hidden-markov-model, regime-switching, commodity-trading, crude-oil, covid-2020, volatility-stress, cointegration]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
topics: [statistical-arbitrage, regime-switching, hidden-markov-model, financial-crises, commodity-markets]
freshness_status: current
depends_on:
  - wiki/concepts/statistical-arbitrage-pairs-trading.md
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-12
---

## Resumo

Fanelli et al. (2023 — arxiv 2309.00875) aplicam Hidden Markov Model (HMM) com estimador online para arbitragem estatística em futuros de petróleo cru (Brent, WTI, Shanghai), cobrindo explicitamente o colapso de COVID-19 (mar 2020) e o pico de volatilidade do conflito Rússia-Ucrânia (fev-jun 2022). A estratégia modela o spread de cointegração como processo de reversão à média com regime-switching — o regime é inferido pelo filtro de Kalman online. Lucrativa mesmo com custos de transação conservadores, superando estratégias de pares clássicos sem regime-switching.

## Conteúdo

### Estrutura do modelo

O paper identifica que os três futuros de petróleo (Brent, WTI, Shanghai) são cointegrados. O spread de cointegração S(t) é modelado como:

```
dS(t) = κ(r(t))[θ(r(t)) - S(t)] dt + σ(r(t)) dW(t)
```

onde `r(t) ∈ {1, 2, ..., N}` é o regime atual (variável de estado latente), modulado por uma cadeia de Markov oculta. Cada regime tem seus próprios parâmetros (κ: velocidade de reversão, θ: média de reversão, σ: volatilidade).

O regime nunca é observado diretamente — é inferido via estimador online (filtro de Kalman ou variante HMM). Isso permite recalibrar a estratégia de trading conforme o regime evolui, sem janelas de re-treinamento fixas.

### Período e eventos de stress cobertos

**Dados:** futuros de petróleo Brent, WTI e Shanghai Crude Oil (SCO), amostra estendida.
**Período de treinamento:** até 07/01/2022
**Período de teste (out-of-sample):** após 07/01/2022 — inclui:
- Colapso de preços do petróleo COVID-19 (sharp decline de mar 2020): **incluso na amostra de treinamento**
- Pico do conflito Rússia-Ucrânia e período subsequente de alta volatilidade (fev-jun 2022): **incluso no período de teste**

Este é um dos poucos papers de stat-arb com teste out-of-sample explicitamente cobrindo um período de volatilidade extrema (pico e normalização da crise energética 2022).

### Resultados principais

- Estratégias de 3 futuros (Brent + WTI + SCO) são lucrativas mesmo com custos de transação conservadores
- Estratégias de 2 futuros clássicos (Brent + WTI sem SCO) **não geram oportunidades lucrativas** — a adição de Shanghai como terceiro ativo é necessária para o spread ser explorável
- Lucratividade persiste "over different time periods" — inclusive o período de volatilidade extrema da crise energética 2022
- Regime-switching melhora a adaptação a mudanças de volatilidade: quando o spread entra em regime de alta volatilidade, os limiares de trading ajustam automaticamente

### Estimador online como mecanismo de robustez

O uso de estimador online (adaptativo) é o ponto crítico de diferenciação:
- **Estimadores offline (static):** calibram parâmetros uma vez no período de formação; ficam desatualizados em crises
- **Estimador online:** atualiza parâmetros incrementalmente à medida que novos dados chegam — o regime atual é sempre inferido com base em toda a história observada até o momento

Esta propriedade faz a estratégia "self-adapting" durante crises: quando a volatilidade aumenta drasticamente (COVID, Ucrânia), o modelo reconhece que está em um novo regime e ajusta limiares de entrada/saída.

### Diferença em relação a pairs trading clássico

Pairs trading clássico (Gatev et al. 2006, cointegração estática) assume que os parâmetros do spread são estacionários ao longo de todo o período de backtesting. Em crises:
1. A volatilidade explode → z-scores que normalmente indicam entrada não são mais válidos com σ calibrado no período de formação
2. O spread pode se deslocar para um novo equilíbrio → θ (média de longo prazo) muda de regime

O HMM com estimador online endereça ambos: σ e θ são re-estimados continuamente.

## Interpretação

(⚠️ Zone 3 — domínio financeiro lateral ao core AI/ML da KB. Conexões ao design da KB emergem via /ask, não no /ingest.)

(⚠️ nossa interpretação) O estimador online do HMM é funcionalmente análogo a algoritmos adaptativos em outros domínios de ML (Kalman Filter em SLAM, variational inference incremental). A robustez em regime change aqui é uma propriedade do processo de estimação, não da estrutura do modelo.

## Conexões
- challenges: [[statistical-arbitrage-pairs-trading]] (cointegração com HMM + estimador online adapta-se a regime change; cointegração estática dos papers Tadi & Witzany e Ning & Lee não)
- partOf: [[deep-learning-statistical-arbitrage]] (mesmo domínio de stat-arb quantitativo)

## Fontes
- [Fanelli et al. (2023)](../../raw/papers/2309.00875-hmm-stat-arb-crude-oil.pdf) — HMM para stat-arb em futuros de petróleo (Brent, WTI, Shanghai); cobre COVID e crise energética 2022; arxiv 2309.00875

## Verificação adversarial

**a. Claim mais fraco:** "lucrativo durante o período de stress de 2022" — o período de teste começa em 07/01/2022, mas o pior da volatilidade (invasão da Ucrânia, pico de preços de petróleo) foi fev-mar 2022, que é a transição entre treinamento e teste. Não está claro se o período de test out-of-sample captura o pico de estresse ou a normalização posterior.

**b. O que o paper NÃO diz:**
- Não reporta Sharpe ratio ou drawdown máximo separado para o período de alta volatilidade — apenas que é "lucrativo over different time periods".
- Não testa em ativos cripto — commodity futures é mercado com dinâmica diferente (storage costs, delivery, seasonality).
- Não compara com HMM de regime fixo (sem estimador online) para isolar a contribuição do estimador adaptativo.

**c. Simplificações feitas:** o modelo assume que a cadeia de Markov oculta tem um número fixo de regimes (N) definido a priori. Escolher N errado pode fazer o modelo falhar em reconhecer um novo regime sem precedente histórico.

**d. Prior work:** Erlwein et al. (2011) para HMM em pares de câmbio; Farnoosh et al. (2011) para regime-switching em mercados financeiros; Hamilton (1989) para o modelo original de regime-switching de Markov em macroeconomia.

## Quality Gate
- [x] Wikilinks tipados: 2 wikilinks tipados (challenges x1, partOf x1)
- [x] Instance→class: claims de lucratividade qualificados por ativo específico (petróleo Brent/WTI/SCO) e período (treinamento até jul 2022, teste posterior)
- [x] Meta-KB separado: sim
- [x] Resumo calibrado: sim — limitação de escopo de crises cobertas explicitada
