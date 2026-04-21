---
title: "Copula Dependency Modeling"
sources:
  - path: raw/papers/2305.06961.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-12
updated: 2026-04-12
tags: [statistics, copula, dependency-modeling, pairs-trading, financial-econometrics]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
topics: [copula, dependency-modeling, statistical-arbitrage, financial-econometrics]
freshness_status: current
depends_on: []
reads: 2
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-12
---

## Resumo

Cópulas são funções matemáticas que modelam a estrutura de dependência entre variáveis aleatórias separadamente das suas distribuições marginais. No contexto de trading, permitem capturar assimetria e caudas pesadas na relação entre dois ativos — propriedades ausentes nos modelos baseados em correlação linear ou cointegração gaussiana.

## Conteúdo

### Definição formal

Pelo Teorema de Sklar, qualquer distribuição conjunta F(x₁, x₂) pode ser decomposta em:
```
F(x₁, x₂) = C(F₁(x₁), F₂(x₂))
```
onde F₁ e F₂ são as distribuições marginais e C é a cópula — a função que captura exclusivamente a estrutura de dependência. As variáveis transformadas U₁ = F₁(x₁) e U₂ = F₂(x₂) seguem distribuição uniforme U[0,1].

### Famílias de cópulas relevantes para trading

As principais famílias usadas em pairs trading (Tadi & Witzany 2023):
- **Gaussian copula:** dependência simétrica, sem caudas pesadas. Baseline comum.
- **Student-t copula:** dependência simétrica com caudas pesadas. Rad, Low & Faff (2016) mostraram que é mais adequada para modelar dependência no mercado de ações US.
- **Clayton copula:** dependência assimétrica — mais forte na cauda inferior (co-crashes).
- **Gumbel copula:** dependência assimétrica — mais forte na cauda superior (co-booms).
- **Frank copula:** dependência simétrica, adequada para dados com correlação moderada.

### Mispricing index (MI) em trading

A cópula gera sinais de trading via probabilidade condicional. Para dois ativos com log-returns transformados U₁ e U₂:
```
h^{1|2} = P(U₁ ≤ u₁ | U₂ = u₂) = ∂C(u₁, u₂) / ∂u₂
h^{2|1} = P(U₂ ≤ u₂ | U₁ = u₁) = ∂C(u₁, u₂) / ∂u₁
```
Valores de h próximos a 0 ou 1 indicam desvio da relação esperada entre os ativos. O **Cumulative Mispricing Index (CMI)** agrega esses desvios ao longo do tempo:
```
CMI^{1|2}_t = CMI^{1|2}_{t-1} + (h^{1|2}_t - 0.5)
```
CMI positivo indica que o ativo 1 está sobrevalorizado relativo ao ativo 2; negativo indica subvalorização. Esta abordagem é chamada "value-based" (Xie & Wu 2013) em contraste com o método "return-based" que usa apenas o valor de h do período anterior.

### Vantagens sobre distância e cointegração

Xie & Wu (2013) demonstraram que os métodos de distância e cointegração são casos especiais da abordagem por cópula sob certas condições. Adicionalmente:
- Não assume linearidade na associação entre ativos
- Captura assimetria na dependência (crashes vs. booms podem ter comportamentos diferentes)
- Mais robusto a distribuições não-gaussianas — relevante em cripto, que exibe fat tails e regime-switching

Desvantagem: CMI pode não exibir comportamento mean-reverting em todos os cenários, o que pode afetar a geração de sinais de trading (Tadi & Witzany 2023).

### Estimação de cópulas

Parâmetros são estimados por máxima verossimilhança. O Kendall's Tau (τ) é a medida de correlação de rank usada para estimar os parâmetros da cópula, sendo mais robusta que a correlação de Pearson para dados financeiros com caudas pesadas.

### Resultado empírico (Tadi & Witzany 2023)

Aplicado a 20 criptomoedas no Binance (dados horários, 2021-2023, 104 ciclos de 1 mês com 3 semanas de formação e 1 semana de trading). A estratégia baseada em cópulas outperformou a estratégia buy-and-hold tanto em retorno absoluto quanto em retorno ajustado a risco (Sharpe). Os autores testaram diferentes famílias de cópulas e múltiplos triggers de abertura de posição.

## Interpretação

(⚠️ Zone 3 — domínio financeiro lateral ao core AI/ML da KB. Conexões ao design da KB emergem via /ask, não no /ingest.)

## Conexões
- partOf: [[statistical-arbitrage-pairs-trading]]
- emerge-para: [[epistemic-dependency-copula]] ON "Teorema de Sklar como separação marginal/dependência epistêmica; CMI como proxy de staleness de pares co-ativados"

## Fontes
- [Tadi & Witzany (2023)](../../raw/papers/2305.06961.pdf) — estratégia de pairs trading com cópulas para cripto; backtesting em Binance 2021-2023

## Verificação adversarial

**a. Claim mais fraco:** "cópulas são superiores a cointegração para cripto" — Tadi & Witzany aplicam ao mercado cripto num período específico (2021-2023, que inclui período de alta volatilidade). O resultado pode não generalizar para mercados mais eficientes ou períodos de baixa volatilidade.

**b. O que o paper NÃO diz:**
- Não compara diretamente contra cointegração não-linear (KSS) com os mesmos dados.
- Não avalia performance em regime de mercado em queda prolongada (bear market 2022 é incluído, mas sem análise separada por regime).
- Não quantifica robustez da seleção de família de cópula — qual família específica foi dominante.

**c. Simplificações feitas:** ciclos de 1 mês com 3 semanas de formação assumem estabilidade da estrutura de dependência dentro do ciclo. Em mercados cripto com choques de liquidez, isso pode falhar.

**d. Prior work:** literatura de cópulas em finance remonta a Embrechts et al. (1999). Em pairs trading, Ferreira (2008), Liew & Wu (2013), Xie & Wu (2013), e Stander, Marais & Botha (2013) estabeleceram o método. Este paper estende para cripto.

## Quality Gate
- [x] Wikilinks tipados: 1 wikilink tipado (partOf)
- [x] Instance→class: resultado empírico qualificado por dataset e período específico
- [x] Meta-KB separado: sim
- [x] Resumo calibrado: sim
