---
title: "Deep Learning Statistical Arbitrage"
sources:
  - path: raw/papers/2106.04028-deep-learning-stat-arb.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-12
updated: 2026-04-12
tags: [deep-learning, statistical-arbitrage, factor-model, convolutional-transformer, asset-pricing, quantitative-finance]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
topics: [deep-learning, statistical-arbitrage, factor-models, convolutional-transformer, asset-pricing]
freshness_status: current
depends_on: []
reads: 2
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-12
---

## Resumo

Guijarro-Ordonez, Pelger e Zanotti (Stanford, 2022 — publicado na Management Science) propõem um framework unificador para arbitragem estatística decomposto em três problemas: (1) geração de portfólios de arbitragem como resíduos de modelos de asset pricing, (2) extração de sinais de série temporal via convolutional transformer, e (3) alocação ótima de trading baseada nos sinais. Aplicado às 550 maiores ações US (1998-2016), o modelo atinge Sharpe ratio out-of-sample superior a 4 e retorno médio anual de 20%, superando todos os benchmarks paramétricos.

## Conteúdo

### Framework unificador (três componentes)

O paper propõe que toda estratégia de arbitragem estatística pode ser decomposta em:

**Componente 1 — Portfólios de arbitragem:**
Ativos similares (mesma exposição ao risco sistemático) devem ter o mesmo preço fundamental. Resíduos de um modelo de fator de asset pricing capturam desvios temporários desse preço justo. Formalmente:
```
R_{n,t} = β_{n,t-1}^⊤ F_t + ε_{n,t}
```
onde F ∈ ℝ^{T×K} são K fatores sistemáticos, β são as loadings, e ε é o resíduo — o portfólio de arbitragem. Portfólios de resíduos são fracamente correlacionados cross-sectionalmente e próximos de estacionários, o que os torna adequados para modelagem pura de série temporal.

O paper testa múltiplas especificações de fatores: Fama-French 5 fatores, PCA local, IPCA (Instrumented PCA de Kelly et al. 2019 — loadings como funções de 46 características de firmas). IPCA com 5 fatores condicionais gera Sharpe out-of-sample de 4.2, versus 3.2 para PCA simples. A escolha do modelo de fatores tem efeito **marginal** na performance — o componente de extração de sinal é mais determinante.

**Componente 2 — Extração de sinal por convolutional transformer:**
Um filtro data-driven baseado em redes convolucionais combinadas com transformers extrai padrões de série temporal nos resíduos. Diferentemente de modelos paramétricos (OU, Fourier), não prescreve a estrutura do sinal — aprende diretamente a função ótima de extração para o objetivo de trading.

Redes convolucionais capturam padrões locais nos dados; o transformer combina esses padrões em dependências globais de série temporal. O modelo é interpretável via "dependency factors" — padrões de trend e reversão que dominam o sinal. O convolutional transformer dobra a performance relativa a um modelo deep learning idêntico sem o filtro convolucional — evidência de que modelagem de série temporal é o componente crítico.

**Componente 3 — Alocação ótima de trading:**
Redes neurais mapeiam sinais de arbitragem em alocações ótimas, generalizando regras de limiar fixas. O objetivo é maximizar Sharpe ratio (ou retorno esperado com penalidade de risco) sujeito a restrições de turnover, leverage e proporção de shorts. Usar objetivo de trading (vs. objetivo de predição) é crítico: a literatura mostra que otimizar para predição não é equivalente a otimizar para retorno (Bryzgalova et al. 2019, Chen et al. 2022).

### Resultados empíricos principais

Dataset: ~550 ações US mais líquidas, retornos diários, 1998-2016. Janela rolling out-of-sample.

- **Sharpe ratio out-of-sample > 4** (anualized) com o modelo completo
- **Retorno médio anual de 20%** out-of-sample, respeitando restrições de short-selling
- Performance 4x melhor que modelos paramétricos, 2x melhor que deep learning sem convolutional transformer
- Estratégia é ortogonal a fatores de mercado, momentum e reversal — não é risk premium disfarçado
- Robusta à escolha de tuning parameters e ao período de estimação
- Sinais de arbitragem persistem no curto prazo: ~metade do Sharpe persiste em horizonte de 1 semana; arbitrageurs corrigem a maioria do mispricing em ~1 mês

### Padrões identificados pelo modelo

O modelo é assimétrico: reage mais rapidamente a movimentos de queda do que de alta.
- "Dependency factors" para movimentos de queda: focam nos últimos 10 dias
- "Dependency factors" para movimentos de alta: focam nos últimos 20 dias em janela de 30 dias

Isso sugere que o modelo captura asymmetric mean reversion — quedas revertem mais rápido que altas (comportamento consistente com literatura de overreaction/underreaction).

### Implicação sobre eficiência de mercado

O paper estima que há substancial quantidade de short-term arbitrage remanescente nos mercados financeiros. A lucratividade é ortogonal a movimentos de mercado e fatores de risco convencionais. A inferência dos autores é que arbitrageurs recebem compensação significativa pela "lei do preço único" — mas eles não afirmam que os mercados são ineficientes em sentido forte; apenas que frições práticas preservam oportunidades de stat-arb.

## Interpretação

(⚠️ Zone 3 — domínio financeiro lateral ao core AI/ML da KB. Conexões ao design da KB emergem via /ask, não no /ingest.)

## Conexões
- derivedFrom: [[statistical-arbitrage-pairs-trading]]

> [!patch]
> id: patch-2026-04-12-001
> status: pending
> trigger: ingest/robust-stat-arb-dnn-regime
> impact_type: claim_refinement
> materiality: high
> affected_claims: ["Sharpe > 4 out-of-sample", "robustez à escolha de tuning parameters e período de estimação"]
> summary: Neufeld, Sester & Yin (2203.03179) demonstram que DNN stat-arb é lucrativa mesmo durante crises financeiras e quando cointegração colapsa. O claim de robustez do Guijarro-Ordonez (1998-2016) não testa essas condições. O paper 2203.03179 estende o escopo de robustez para além de tuning parameters — para robustez a regime change e colapso de modelo.
> action: Adicionar subseção "Limitação de robustez em regime change" em Conteúdo, citando 2203.03179 como extensão que endereça essa limitação. Mover claim de robustez para ## Interpretação com qualificação: "robusto a tuning parameters no período 1998-2016, mas robustez a regime change requer metodologia de ambiguidade de modelo (ver robust-stat-arb-dnn-regime)"
> sources:
>   - wiki/concepts/robust-stat-arb-dnn-regime.md
> created_at: 2026-04-12

## Fontes
- [Guijarro-Ordonez, Pelger & Zanotti (2022)](../../raw/papers/2106.04028-deep-learning-stat-arb.pdf) — framework unificador para stat-arb com deep learning; S&P 550, 1998-2016, Management Science

## Verificação adversarial

**a. Claim mais fraco:** "Sharpe > 4 out-of-sample" — o período 1998-2016 inclui a crise de 2008 e o período pós-crise de alta volatilidade, que pode ser favorável a estratégias de mean reversion. Sharpe de 4 é extraordinariamente alto; estratégias reais enfrentam capacidade limitada (market impact quando escaladas) e regime changes (ex: compressão de spreads com HFT).

**b. O que o paper NÃO diz:**
- Não avalia se a estratégia continua lucrativa em mercados de alta frequência dominados por HFT (pós-2016).
- Não estima a capacidade máxima da estratégia — quanto capital pode ser deployado antes de degradar performance.
- Não testa robustez a mudanças regulatórias (restrições de short-selling em crises).

**c. Simplificações feitas:** custos de transação são modelados de forma simplificada. Impacto de mercado (market impact) em escalas de capital institucionais é ignorado — crítico para uma estratégia que opera 550 ações diariamente.

**d. Prior work:** Gatev et al. (2006) para distance method; Vidyamurthy (2004) para cointegração; Rad et al. (2016) para cópulas. Na interseção ML + stat-arb: Kim & Kim (2019) para RL, Mulvey et al. (2020) para ML paramétrico. Este paper é o mais abrangente em escopo e escala empírica da literatura ML-stat-arb até 2022.

## Quality Gate
- [x] Wikilinks tipados: 1 wikilink tipado (derivedFrom)
- [x] Instance→class: Sharpe ratio qualificado por dataset, período e condições específicas
- [x] Meta-KB separado: sim
- [x] Resumo calibrado: sim — paper publicado em Management Science, alta qualidade, mas caveats sobre período e escalabilidade explicitados
