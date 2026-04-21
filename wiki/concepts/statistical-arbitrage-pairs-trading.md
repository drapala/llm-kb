---
title: "Statistical Arbitrage and Pairs Trading"
sources:
  - path: raw/papers/2305.06961.pdf
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/2403.12180.pdf
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/2407.16103.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-12
updated: 2026-04-12
tags: [trading, statistical-arbitrage, pairs-trading, mean-reversion, reinforcement-learning, cryptocurrency]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - raw/papers/2305.06961.pdf
  - raw/papers/2403.12180.pdf
  - raw/papers/2407.16103.pdf
topics: [statistical-arbitrage, pairs-trading, mean-reversion, reinforcement-learning, cryptocurrency-trading]
freshness_status: current
depends_on: []
reads: 3
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-12
---

## Resumo

Arbitragem estatística (stat-arb) explora desvios temporários de preço entre ativos similares usando métodos quantitativos. Pairs trading é a forma mais comum: identifica dois ativos co-moventes, constrói um spread, e opera quando o spread desvia do equilíbrio de longo prazo. Três papers cobrem abordagens distintas: copulas para modelar dependência (Tadi & Witzany 2023), aprendizado por reforço com tempo empírico de reversão (Ning & Lee 2024), e RL com escalonamento dinâmico de quantidade (Yang & Malik 2024).

## Conteúdo

### Estrutura geral do pairs trading

Pairs trading opera em dois períodos:
- **Formação:** identifica pares com co-movimento histórico. Métodos: distância (SSD — sum of squared deviations), cointegração, correlação, cópulas.
- **Trading:** monitora o spread e abre/fecha posições quando o spread desvia além de um limiar.

A posição padrão: long no ativo subprecificado, short no sobrevalorizado. A posição se fecha quando os preços convergem. A estratégia é essencialmente market-neutral — os lucros derivam da convergência relativa, não do movimento absoluto de mercado (Gatev et al. 2006).

### Abordagens de seleção de pares

**Abordagem por distância:** usa o SSD (sum of squared distances) entre séries de preços normalizados para selecionar os pares mais similares durante o período de formação. Simples e transparente, adequada para aplicações em larga escala.

**Abordagem por cointegração:** identifica equilíbrio de longo prazo entre séries não-estacionárias. O teste Engle-Granger (1987) é o método linear padrão: regressão linear seguida de teste ADF nos resíduos. Mercados cripto exibem frequentemente não-linearidades; nesses casos, o teste Kapetanios-Shin-Shell (KSS) para raiz unitária não-linear é mais robusto (Tadi & Witzany 2023).

**Abordagem por cópulas:** modela a estrutura de dependência entre ativos sem assumir distribuição gaussiana. Captura assimetria e caudas pesadas. O índice de mispricing é definido via probabilidade condicional da cópula: `h^{1|2} = P(U1 ≤ u1 | U2 = u2)`. Quando h se afasta de 0.5, os ativos estão fora de equilíbrio. O método CMI (cumulative mispricing index) agrega desvios ao longo do tempo (Tadi & Witzany 2023). Liew e Wu (2013) mostraram que a abordagem por cópulas generaliza os métodos de distância e cointegração como casos especiais.

### Spread e limiar de entrada/saída

O spread normalizado (z-score) é a métrica padrão de trading:
```
Z = (s - s̄) / σ_s
```
Posição abre quando Z ultrapassa o limiar de abertura (Open Threshold — OT); fecha quando retorna ao limiar de fechamento (Close Threshold — CT). Gatev et al. (2006) adotaram 2σ como OT e cruzamento de preço como CT. Em mercados mais voláteis como cripto, limiares mais amplos são necessários.

### Reinforcement Learning em pairs trading

RL substitui regras fixas de limiar por políticas adaptativas que otimizam decisões de trading ao longo do tempo como um MDP (Markov Decision Process). Os elementos do MDP:
- **Estado:** vetor de observações recentes do spread (direção e magnitude das variações de preço)
- **Ação:** {-1, 0, +1} — vender, manter, comprar
- **Recompensa:** P&L menos custos de transação

**Empirical Mean Reversion Time (EMRT):** métrica introduzida por Ning & Lee (2024) para selecionar coeficientes de portfólio sem assumir modelo OU. EMRT é o tempo médio entre extremos locais e cruzamentos da média — um análogo empírico do parâmetro μ do processo OU, mensurável sem calibração paramétrica. Para spreads OU simulados, EMRT cai monotonicamente com μ (ex: EMRT=98.79 para μ=2.0, EMRT=31.15 para μ=20.0).

**Escalonamento dinâmico de quantidade (Yang & Malik 2024):** extensão do RL que otimiza não apenas *quando* operar, mas *quanto* investir. O espaço de ação é contínuo A ∈ [-1, 1], representando percentual do portfólio. O observation space inclui {Posição, Spread, Zona}. Quatro algoritmos RL foram testados (DQN, SAC, A2C, PPO). Usando dados BTC-GBP e BTC-EUR em intervalos de 1 minuto (n=263,520), o método RL-based atingiu retornos anualizados de 9.94% a 31.53% vs. 8.33% para o método tradicional não-RL.

### Resultados empíricos (backtesting)

- **Tadi & Witzany (2023) — cripto:** cópulas com dados horários Binance (20 criptomoedas, 2021-2023, 104 ciclos de 1 mês). Estratégia com cópulas outperforma buy-and-hold tanto em retorno absoluto quanto em retorno ajustado a risco.
- **Ning & Lee (2024) — ações US:** S&P 500, 10 pares representativos. RL com EMRT supera métodos paramétricos (OU clássico) e deep learning sem RL.
- **Yang & Malik (2024) — cripto:** BTC-GBP e BTC-EUR, ~70 bilhões USD/dia de volume. RL com escalonamento dinâmico supera pair trading tradicional em retorno anualizado e redução de risco.

## Interpretação

(⚠️ Zone 3 — domínio financeiro lateral ao core AI/ML da KB. Conexões ao design da KB emergem via /ask, não no /ingest.)

## Conexões
- partOf: [[copula-dependency-modeling]]
- derivedFrom: [[deep-learning-statistical-arbitrage]]
- partOf: [[cryptocurrency-perpetual-futures-funding-rate]]

> [!patch]
> id: patch-2026-04-12-002
> status: pending
> trigger: ingest/robust-stat-arb-dnn-regime,ingest/hmm-stat-arb-regime-switching,ingest/market-neutral-pairs-crypto-bull-bear
> impact_type: scope_expansion
> materiality: high
> affected_claims: ["não demonstram que as estratégias são robustas a regimes de baixa volatilidade ou colapso de correlação entre pares", "nenhum dos três verifica se os pares permanecem cointegrados fora do período de formação"]
> summary: Três novos papers endereçam diretamente os gaps de robustez identificados na verificação adversarial: (1) 2203.03179 demonstra DNN lucrativa sem cointegração e em crises; (2) 2309.00875 demonstra HMM com estimador online lucrativo durante COVID e crise energética 2022; (3) 2405.15461 fornece o breakdown bull/bear ausente em Tadi & Witzany e Yang & Malik RL.
> action: Adicionar subseção "Robustez em regime change" em Conteúdo com referências cruzadas para os 3 novos artigos. Atualizar a verificação adversarial: o claim "b. O que os papers NÃO dizem" sobre robustez a crises agora tem cobertura parcial via 2309.00875 (HMM + COVID/Ucrânia) e 2405.15461 (bull/bear 2021-2023 desagregado).
> sources:
>   - wiki/concepts/robust-stat-arb-dnn-regime.md
>   - wiki/concepts/hmm-stat-arb-regime-switching.md
>   - wiki/concepts/market-neutral-pairs-crypto-bull-bear.md
> created_at: 2026-04-12

## Fontes
- [Tadi & Witzany (2023)](../../raw/papers/2305.06961.pdf) — cópulas para pairs trading em cripto; outperforma buy-and-hold
- [Ning & Lee (2024)](../../raw/papers/2403.12180.pdf) — RL model-free com EMRT; supera métodos paramétricos no S&P 500
- [Yang & Malik (2024)](../../raw/papers/2407.16103.pdf) — RL com escalonamento dinâmico de quantidade em BTC

## Verificação adversarial

**a. Claim mais fraco:** "RL supera métodos tradicionais em pairs trading" — os três papers usam datasets diferentes (um S&P 500, dois cripto), períodos curtos, e condições de backtesting controladas. Generalização para outros períodos ou regimes de mercado não está demonstrada.

**b. O que os papers NÃO dizem:**
- Não demonstram que as estratégias são robustas a regimes de baixa volatilidade ou colapso de correlação entre pares.
- Yang & Malik (2024) não comparam com estratégias de momentum ou factor models estabelecidos.
- Nenhum dos três verifica se os pares permanecem cointegrados fora do período de formação — apenas assumem estabilidade.

**c. Simplificações feitas:** os resultados de backtesting não incorporam impacto de mercado (slippage em mercados ilíquidos), shorting costs, ou restrições de capital. Os retornos reportados são brutos ou com custos simplificados.

**d. Prior work:** todos os três citam extensamente Gatev et al. (2006) como baseline canônico. Tadi & Witzany citam Liew & Wu (2013) para cópulas em pairs trading. Ning & Lee citam Kim & Kim (2019) como baseline RL. Tradição estabelecida de pelo menos 20 anos na literatura.

## Quality Gate
- [x] Wikilinks tipados: 3 wikilinks tipados (partOf x2, derivedFrom x1)
- [x] Instance→class: retornos anualizados qualificados por paper/dataset específico
- [x] Meta-KB separado: nenhuma referência a comandos KB
- [x] Resumo calibrado: sim — sem overclaiming de generalização
