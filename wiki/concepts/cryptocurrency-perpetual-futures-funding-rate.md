---
title: "Cryptocurrency Perpetual Futures and Funding Rate Arbitrage"
sources:
  - path: raw/papers/mdpi-funding-rate-two-tiered-2025.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-12
updated: 2026-04-12
tags: [cryptocurrency, perpetual-futures, funding-rate, arbitrage, market-microstructure, CEX, DEX]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
topics: [cryptocurrency, perpetual-futures, funding-rate, market-microstructure, arbitrage, CEX-DEX]
freshness_status: current
depends_on: []
reads: 2
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-12
---

## Resumo

Futuros perpétuos são contratos derivativos sem data de expiração que dominam os mercados de derivativos cripto (~93% do volume de futuros). O mecanismo de funding rate — pagamentos periódicos entre posições long e short — ancora o preço perpétuo ao spot. Zhivkov (2026) documenta estrutura de dois níveis nos mercados de funding rate: exchanges centralizadas (CEX) dominam a descoberta de preço, com fluxo de informação em sentido único CEX→DEX. Apesar de spreads de funding rate economicamente significativos (≥20 bps) existirem em 17% das observações, apenas 40% das oportunidades de topo geram retorno positivo após custos e reversões de spread.

## Conteúdo

### Mecanismo de futuros perpétuos

Futuros perpétuos não têm data de expiração e não convergem naturalmente para o spot via expiração. A ancoragem ao preço spot é mantida via **funding rate**: periodicamente (tipicamente a cada 1h, 4h ou 8h), posições long pagam posições short (ou vice-versa) com base no desvio entre o preço perpétuo e o spot. Quando o perpétuo está acima do spot, longs pagam shorts (desincentivando compras); abaixo do spot, shorts pagam longs.

### Dataset e escopo do estudo (Zhivkov 2026)

- 35.7 milhões de observações de granularidade 1 minuto
- 26 exchanges (11 CEX, 15 DEX) ao longo de 8 dias consecutivos (8-15 Novembro 2025)
- 749 símbolos de criptomoedas
- 11 CEX: BINANCE, BYBIT, OKX, KUCOIN, MEXC, GATEIO, BITGET, BINGX, PHEMEX, CRYPTOCOM, HTX
- 15 DEX: HYPERLIQUID, DRIFT, PARADOX, KUMA, VEST, BLUEFIN, PACIFICA, LIGHTER, EXTENDED, EDGEX, HIBACHI, ETHEREAL, VARIATIONAL, ASTER, WOOFI

### Estrutura de dois níveis: CEX vs. DEX

**Achados sobre descoberta de preço (Granger causality):**
- CEX exibem 61% maior integração de mercado que DEX
- Todo fluxo de informação significativo é CEX→DEX, sem causalidade reversa
- CEX operam com order books centralizados e custódia centralizada; DEX usam AMM (Automated Market Maker) com liquidação on-chain

**Mecanismos estruturais que explicam a diferença:**
- CEX: order books tradicionais, latência baixa, maior liquidez (OI)
- DEX: liquidação permissionless on-chain, restrições de latência por blockchains (Solana, Arbitrum, Optimism têm custos de gas < $0.01/trade)

### Oportunidades de arbitragem de funding rate

**Definição de spread:** diferença entre funding rate máxima e mínima entre exchanges para o mesmo símbolo, normalizada para intervalo de 8h:
```
Spread_{s,t} = max_{e ∈ E_s} r_{e,s,t} - min_{e ∈ E_s} r_{e,s,t}
```

**Threshold de significância econômica:** ≥20 bps (equivalente a ~219% APY), muito acima dos custos de transação típicos de 4-8 bps.

**Estratégia delta-neutral:** posição long na exchange com menor funding rate + posição short na exchange com maior funding rate, valor nocional igual N. Lucro por período = N × Spread/10,000. A estratégia é market-neutral quanto ao preço do ativo.

**Resultados empíricos:**
- 17% das observações apresentam spread ≥ 20 bps (oportunidades economicamente significativas)
- Apenas 40% das oportunidades de topo geram retorno positivo após custos e reversões de spread
- Saídas forçadas (spread → negativo) ocorrem em 95% das oportunidades, limitando a lucratividade
- Simulações delta-neutral com position sizing de $10,000/lado: mercados líquidos (OI rank < 50) têm custo de $60/round-trip; mercados ilíquidos (OI rank ≥ 50) custam $220/round-trip

### Custos de transação em detalhes

Para exchanges na amostra (novembro 2025):
- Taker fees: 0.01%-0.05%, estimados conservadoramente em 0.05%
- Slippage: 0.1% para pares líquidos (OI rank < 50), 0.5% para ilíquidos
- Gas costs DEX: negligíveis em blockchains low-cost (< $0.01/trade)

### Persistência e reversão de spreads

Spreads de funding rate exibem persistência (autocorrelação positiva), mas reversões súbitas são comuns — exchanges invertem suas posições relativas de funding rate. O protocolo de saída forçada (fechar posição imediatamente quando spread < 0 bps) é conservador mas necessário: 95% das oportunidades enfrentam saída forçada antes da convergência natural.

Half-life de spreads: calculado como ln(2)/λ, onde λ é estimado de regressões de decaimento exponencial. Spreads com half-life curto são menos exploráveis — se o spread reverte rapidamente, as oportunidades se fecham antes de gerar retorno suficiente para cobrir custos.

### Limitações da arbitragem na prática

O paper documenta que "substantial price fragmentation coexisting with market efficiency" é possível porque:
1. Custos de transação criam zonas de não-arbitragem
2. Riscos de execução, liquidez, margem e timing impedem a eliminação completa de mispricing
3. Fluxos de capital segmentados entre CEX e DEX criam fricções estruturais

## Interpretação

(⚠️ Zone 3 — domínio financeiro lateral ao core AI/ML da KB. Conexões ao design da KB emergem via /ask, não no /ingest.)

## Conexões
- partOf: [[statistical-arbitrage-pairs-trading]]

## Fontes
- [Zhivkov (2026)](../../raw/papers/mdpi-funding-rate-two-tiered-2025.pdf) — estrutura dois níveis em mercados de funding rate cripto; 35.7M observações, 26 exchanges

## Verificação adversarial

**a. Claim mais fraco:** "apenas CEX→DEX, sem causalidade reversa" — baseado em apenas 8 dias de dados (8-15 Nov 2025). Período muito curto para estabelecer estrutura causal estável; resultados de Granger causality são sensíveis à janela temporal e à escolha de lags.

**b. O que o paper NÃO diz:**
- Não demonstra que a estrutura de dois níveis é estável ao longo do tempo — 8 dias pode ser atípico.
- Não verifica se os resultados se mantêm em períodos de alta volatilidade extrema (flash crashes, liquidações em cascata).
- Não avalia impacto de regulações ou mudanças estruturais nas DEX (novos protocolos AMM, migração de liquidez).

**c. Simplificações feitas:** a estratégia delta-neutral assume execução simultânea nas duas exchanges — em prática, latência entre CEX e DEX pode criar slippage adicional. O paper reconhece esse timing risk mas não o quantifica separadamente.

**d. Prior work:** Bhambhwani et al. (2019) sobre pricing de cripto; literatura de microestrutura de mercado aplicada a cripto é relativamente recente (2018+). O paper é pioneiro na comparação sistemática CEX vs. DEX para funding rates.

## Quality Gate
- [x] Wikilinks tipados: 1 wikilink tipado (partOf)
- [x] Instance→class: todos os números qualificados com fonte, dataset e período
- [x] Meta-KB separado: sim
- [x] Resumo calibrado: sim — caveats explícitos sobre 8 dias de dados
