---
title: "Taxa de Retirada Segura no Brasil (TSR)"
sources:
  - path: raw/papers/perlin-pereira-2023-taxa-retirada-sustentavel-brasil.md
    type: paper
    quality: primary
    stance: neutral
  - path: raw/data/aa40-tsr-brasil-2025-2026.md
    type: dataset
    quality: secondary
    stance: neutral
created: 2026-04-13
updated: 2026-04-13
tags: [finanças-pessoais, aposentadoria, brasil, TSR, selic, ibovespa, IPCA, FIRE, planejamento-financeiro]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - raw/papers/perlin-pereira-2023-taxa-retirada-sustentavel-brasil.md
  - raw/data/aa40-tsr-brasil-2025-2026.md
topics: [safe-withdrawal-rate, retirement-planning, brazil, portfolio-management]
freshness_status: current
depends_on: []
reads: 0
---

## Resumo

Estudos adaptando a regra dos 4% ao Brasil encontram TSR históricas entre 7,3% e 9,3% dependendo da alocação, significativamente acima dos 4% americanos — reflexo dos juros reais historicamente elevados no país. Porém, com apenas um ciclo histórico de 30 anos (Plano Real) e condições de juros provavelmente não-repetíveis, as análises de Monte Carlo convergem para 3,7–4,5% a 95% de sucesso.

## Conteúdo

### Contexto brasileiro

O Brasil apresenta características estruturalmente distintas dos EUA para planejamento de aposentadoria:

- **Juros reais elevados**: Selic historicamente muito acima da inflação. De 1995 a 2024, Selic média = 10,8% a.a. com IPCA médio = 4,83% — juro real de ~5,7% a.a.
- **Tesouro IPCA+**: ativo único no mundo que oferece rendimento real garantido pelo governo. Permite manter poder de compra sem exposição a renda variável.
- **Ibovespa volátil**: maior volatilidade e menor histórico longo que o S&P 500. -10,36% a.a. em USD real no período 1995–2024 (em BRL nominal, positivo; em termos reais ajustados por câmbio, adverso).
- **Histórico curto**: Plano Real iniciado em 1994. Apenas ~30 anos de dados estáveis (vs. 109 anos dos EUA no estudo de Pfau).

### Perlin & Pereira (2023) — paper acadêmico FGV

Primeira adaptação acadêmica do modelo Trinity ao Brasil publicada em revista revisada por pares (Revista Brasileira de Finanças, FGV, v.21 n.3).

Metodologia: Trinity adaptado com Asset Liability Management (ALM) + programação estocástica para contornar limitações de histórico curto.

**Resultado principal: taxa de retirada de 5% é sustentável e relativamente segura** para carteiras com predominância em renda fixa.

Portfólios com maior alocação em renda fixa são favorecidos no contexto brasileiro — consistente com Meng & Pfau (2011) para mercados emergentes em geral.

### AA40 — Cálculo histórico 1995–2025

A comunidade FIRE brasileira AA40 publicou o primeiro cálculo sistemático da TSR com dados completos do Plano Real (30 anos).

**TSR SafeMax por alocação (pior período histórico = 1995–2024):**

| Alocação | TSR SafeMax | PWR (capital preservado) |
|----------|-------------|--------------------------|
| 100% Ibovespa | 7,29% | — |
| 50% Ibov / 50% Selic | **8,48%** | **6,93%** |
| 100% Selic/CDI | 9,34% | — |

**Monte Carlo a 95% de probabilidade de sucesso:** 3,69% – 4,5%

**Interpretação dos dados:** a TSR histórica alta (8,48%) reflete juros reais excepcionais do período inicial do Plano Real (1995–2003), quando a Selic chegou a 45% a.a. com IPCA de ~10%. Esse regime provavelmente não se repete.

### Por que a renda fixa domina no Brasil

Ao contrário dos EUA onde bonds de governo rendem próximo da inflação (juro real ~1-2%), no Brasil o Tesouro Selic e o Tesouro IPCA+ oferecem juro real de 5-7% a.a. historicamente. Isso inverte a lógica de que aposentados precisam de renda variável para bater a inflação — a renda fixa local já faz isso.

Implicação: um portfólio 100% Selic/CDI no Brasil tem TSR SafeMax superior (9,34%) ao portfólio 100% Ibovespa (7,29%), o oposto do que se encontra nos EUA.

### Limitações críticas

1. **Um único ciclo**: 30 anos é insuficiente para robustez estatística. Pfau usou 109 anos para 17 países.
2. **Regime irrepetível**: juros reais de dois dígitos dos anos 1990 são anomalia histórica. Selic de 2% (2020–2021) e tendência de queda secular reduzem TSR esperada.
3. **Risco-país não capturado**: defaults, confiscos (Plano Collor 1990 está fora do período de análise), instabilidade fiscal.
4. **Plano Collor**: se o período de análise iniciasse em 1990 (incluindo o confisco de poupança), os resultados seriam dramaticamente diferentes.
5. **IR não incorporado**: tributação sobre fundos e renda fixa reduz retorno real efetivo.
6. **Diversificação geográfica ausente**: análise cobre apenas ativos domésticos.

### Recomendação prática (síntese das fontes)

- A regra dos 4% americana é **conservadoramente segura** para o Brasil (abaixo do SafeMax histórico de 8,48%)
- **Não usar a TSR histórica alta** (8,48% ou 9,34%) no planejamento — dado de um ciclo sem validade estatística
- Monte Carlo a 95% → 3,7–4,5% é o range mais defensável
- Diversificação geográfica (ativos em USD/EUR) é recomendada para mitigar risco-país
- Tesouro IPCA+ é o ativo de menor risco real disponível no Brasil para o horizonte de aposentadoria

## Interpretação

## Conexões

- [[safe-withdrawal-rate]] — metodologia original (Bengen, Pfau internacional)

## Fontes

- [Perlin & Pereira (2023)](../../raw/papers/perlin-pereira-2023-taxa-retirada-sustentavel-brasil.md) — modelo Trinity adaptado ao Brasil, 5% sustentável para renda fixa
- [AA40 TSR Brasil (2025–2026)](../../raw/data/aa40-tsr-brasil-2025-2026.md) — cálculo histórico 30 anos, TSR 8,48%, Monte Carlo 3,7–4,5%
