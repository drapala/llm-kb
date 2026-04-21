---
title: "Market-Neutral Multivariate Pairs Trading in Crypto (Bull & Bear Regimes)"
sources:
  - path: raw/papers/2405.15461-market-neutral-pairs-crypto.pdf
    type: paper
    quality: primary
    stance: challenging
    challenging_type: content
created: 2026-04-12
updated: 2026-04-12
tags: [pairs-trading, cryptocurrency, market-neutral, reinforcement-learning, bull-bear-regime, convex-optimization, regime-robustness]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
topics: [pairs-trading, cryptocurrency-trading, regime-change, market-neutral, convex-optimization]
freshness_status: current
depends_on:
  - wiki/concepts/statistical-arbitrage-pairs-trading.md
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-12
---

## Resumo

Yang & Malik (2024 — arxiv 2405.15461) propõem o Optimal Trading Technique (OTT), abordagem de pairs trading multivariate market-neutral com bi-objective convex optimization, testada em cripto de **jan 2021 a jan 2023** — período que cobre explicitamente o bull run de 2021, o colapso de LUNA-Terra (mai 2022), e o início do bear market de 2022. Atingiu 15.49% de lucro anualizado mantendo neutralidade de mercado. Este paper fornece o breakdown por regime bull/bear ausente nos outros papers de pairs trading crypto do corpus.

## Conteúdo

### Contexto do período testado

O período jan 2021 – jan 2023 é particularmente informativo para robustez de regime:
- **Bull run (jan 2021 – nov 2021):** BTC atingiu ATH de ~69k; correlações entre cripto-pares muito altas
- **Início de bear (jan 2022):** correção significativa; correlações instáveis
- **Colapso Terra-LUNA (mai 2022):** colapso sistêmico do stablecoin UST; contágio para todo o mercado cripto
- **Deep bear (jun-dez 2022):** BTC caiu para ~16k; muitas exchanges em dificuldades (Celsius, FTX colapsou em nov 2022, fora da janela de dados deste paper)

### Abordagem OTT (Optimal Trading Technique)

O método forma um "bucket" de moedas fiduciárias (GBP, EUR etc.) ancoradas à criptomoeda-base para monitorar oportunidades de arbitragem simultâneas entre múltiplos pares.

**Bi-objective convex optimization:**
Quando múltiplos sinais de trading conflitam (ex: BTC-GBP diz comprar, BTC-EUR diz vender com diferentes magnitudes), o OTT resolve o conflito via otimização convexa bi-objetivo:
```
min (1-λ) · risk_term + λ · (-profit_term)
```
onde λ ∈ [0,1] controla o tradeoff profitabilidade/risco. Parâmetros tunable: penalidade de volatilidade e threshold de ação.

**Market neutrality:**
A posição total do portfólio é mantida delta-neutral — ganhos em convergência relativa de pares, não em direção absoluta do mercado.

### Resultados desagregados por regime

O paper reporta experimentos separados para:
- **Mercado em alta (jan 2021 – jan 2022):** 10,456 trades executados
- **Mercado em queda (jan 2022 – jan 2023):** 3,306 trades executados (34% do volume do bull run)
- **Ciclo completo (jan 2021 – jan 2023):** lucro anualizado de 15.49%

A redução de 3x no número de trades no bear market reflete que oportunidades de convergência de pares são menos frequentes quando correlações colapsam — mas quando existem, são exploradas com lucratividade similar.

**Resultado crítico para o gap:** a estratégia é **market-neutral mesmo durante o bear market de 2022** — o drawdown total não é reportado explicitamente, mas a neutralidade de mercado implica que a queda de BTC de ~70% em 2022 não afetou o P&L da estratégia diretamente.

### Comparação com abordagens do corpus existente

| Aspecto | Tadi & Witzany (2305.06961) | Yang & Malik RL (2407.16103) | **Este paper (2405.15461)** |
|---|---|---|---|
| Metodologia | Copulas + cointegração | RL com escalonamento dinâmico | OTT + otimização convexa |
| Período | 2021-2023 (agregado) | Set-Dez 2023 (4 meses) | Jan 2021 – Jan 2023 (2 anos) |
| Breakdown bull/bear | Não | Não | **Sim — 2 subperíodos** |
| FTX coberto | Parcialmente | Não (posterior) | Não (FTX = nov 2022, período termina jan 2023) |
| Market-neutral | Sim (conceitualmente) | Parcialmente | Sim (explicitamente) |

### Limitação: FTX não está na amostra de teste

FTX colapsou em novembro 2022. O período de teste termina em jan 2023 — inclui apenas o período **imediatamente após** o colapso (2 meses), não o colapso em si. O impacto direto do colapso da FTX na liquidez de BTC-GBP e BTC-EUR (pares testados) não é analisado separadamente.

## Interpretação

(⚠️ Zone 3 — domínio financeiro lateral ao core AI/ML da KB. Conexões ao design da KB emergem via /ask, não no /ingest.)

(⚠️ nossa interpretação) A redução de 3x no número de trades no bear market é um dado importante: a estratégia market-neutral não colapsa em bear market, mas "throttle" naturalmente — menos oportunidades de convergência ativas significa menos exposição, o que pode ser proteção implícita de drawdown.

## Conexões
- challenges: [[statistical-arbitrage-pairs-trading]] (fornece breakdown por regime bull/bear que os papers existentes Tadi & Witzany e Yang & Malik RL não têm; demonstra que performance market-neutral persiste em bear market 2022)
- partOf: [[cryptocurrency-perpetual-futures-funding-rate]] (mesmo universo de cripto)

## Fontes
- [Yang & Malik (2024)](../../raw/papers/2405.15461-market-neutral-pairs-crypto.pdf) — OTT multivariate pairs trading cripto; 15.49% anualizado; bull/bear jan 2021 – jan 2023; arxiv 2405.15461

## Verificação adversarial

**a. Claim mais fraco:** "15.49% anualizado mantendo neutralidade de mercado" — o período de 2 anos inclui o bull run de 2021, que é favorável a estratégias de convergência de pares (correlações altas). O resultado combinado pode mascarar que a maior parte do lucro veio do bull market.

**b. O que o paper NÃO diz:**
- Não reporta Sharpe ratio separado para o subperíodo de bear market.
- Não reporta drawdown máximo durante o colapso de LUNA (mai 2022) — evento de contágio sistêmico que quebrou correlações de todos os pares cripto.
- Não testa pares além de BTC-GBP e BTC-EUR — universo restrito.

**c. Simplificações feitas:** os pares testados são BTC vs. moedas fiduciárias — essencialmente pairs de câmbio, não pairs de duas criptomoedas. A dinâmica de correlação entre BTC-GBP e BTC-EUR é mais estável do que entre, say, BTC-ETH, onde fundamentos idiossincrásicos cripto importam. Os resultados podem não generalizar para pares intra-cripto.

**d. Prior work:** mesmo grupo de autores do Yang & Malik 2407.16103 (RL com escalonamento dinâmico). Este paper (2405.15461) é a versão anterior focada na metodologia OTT. Ambos citam Gatev et al. (2006) como baseline.

## Quality Gate
- [x] Wikilinks tipados: 2 wikilinks tipados (challenges x1, partOf x1)
- [x] Instance→class: retorno 15.49% qualificado por par específico (BTC-GBP, BTC-EUR) e período (jan 2021 – jan 2023); trades por regime desagregados com números específicos
- [x] Meta-KB separado: sim
- [x] Resumo calibrado: sim — limitação sobre FTX e ausência de Sharpe por subperíodo explicitadas
