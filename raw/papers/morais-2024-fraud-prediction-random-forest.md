# Previsão de Fraude em Licitações no Brasil

**Autores:** Vinícius Morais, Daniel Vitor Tartari Garruti, Pablo Rogers, Flavio Barboza (UFU/FAGEN — Universidade Federal de Uberlândia)
**Publicação:** Cadernos de Finanças Públicas, Vol. 24, No. 03, 2024 (Tesouro Nacional / STN)
**URL:** https://publicacoes.tesouro.gov.br/index.php/cadernos/article/view/256
**Grupo:** UFU/FAGEN — grupo diferente do LAIC/UFMG
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract da publicação do Tesouro Nacional.

---

## Tese Central

Random Forest aplicado a dados de licitações eletrônicas de 2022 para prever **incidência de multas em empresas** (proxy de fraude). F1 Score médio de 78.5% mensal e 80% anual, com Recall de 90%.

## Metodologia

- Modelo: Random Forest
- Dados: licitações eletrônicas de 2022
- Variável-alvo: multas aplicadas a empresas (proxy de irregularidade/fraude)
- Avaliação: F1 Score mensal e anual + Recall

## Resultados

- F1 Score médio mensal: 78.5%
- F1 Score anual: 80%
- Recall: 90% (mensal e anual)
- Melhor mês: janeiro (Recall = 1.00, F1 = 0.96)
- Pior mês: novembro (Recall = 0.47, F1 = 0.54) — **variação sazonal significativa**

## Limitações

- Proxy de fraude via multas é impreciso: nem toda multa indica fraude; muitas fraudes não resultam em multa
- Dados de apenas 1 ano (2022)
- Variação sazonal extrema (janeiro F1=0.96 vs novembro F1=0.54) — modelo instável

## Relevância para Zelox

**Mais relevante como baseline de comparação do que como metodologia a adaptar:**
- Recall de 90% é alto mas proxy (multas) é fraco — não equivale a fraude confirmada
- A variação sazonal é um achado importante: sazonalidade como feature no risk_score de Zelox (ex: período pré-eleição, fim de mandato)
- Publicado no Tesouro Nacional = benchmark com credibilidade governamental, mesmo sendo grupo externo ao LAIC

## Contexto bibliométrico

Fora do cluster UFMG. Cadernos de Finanças Públicas é periódico do STN, revisado por pares, voltado para aplicações em finanças públicas brasileiras. Metodologia mais simples (RF) que os papers UFMG, mas com dado de ground truth (multas = decisão governamental).
