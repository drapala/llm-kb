# PLUS: A Semi-automated Pipeline for Fraud Detection in Public Bids

**Autores:** Michele A. Brandão, Arthur P. G. Reis, Bárbara M. A. Mendes, Clara A. Bacha de Almeida et al. (UFMG/IFMG)
**Publicação:** Digital Government: Research and Practice (ACM), 2024
**DOI:** 10.1145/3616396
**Grupo:** LAIC — Laboratório de Aprendizado, Inteligência e Conhecimento, UFMG
**Tipo:** paper / primary
**Status:** STUB — full text não acessível integralmente; conteúdo baseado em abstract e web search.

---

## Tese Central

Pipeline semi-automatizado para detecção de fraudes em licitações públicas brasileiras. Automatiza extração e análise de documentos licitários heterogêneos, reduzindo trabalho manual de especialistas.

## Metodologia

**Módulo 1 — Classificação de documentos:**
- Meta-classifier heurístico baseado em keywords
- Categoriza documentos de licitação em 4 meta-classes
- Lida com heterogeneidade de formatos (atas de registro de preço)

**Módulo 2 — Construção de Reference Price Database:**
- Clustering de itens licitados por similaridade textual
- Algoritmo de variação de preços para detectar anomalias de superfaturamento
- Saída: base de preços de referência para comparação

## Dados

Documentos de licitações públicas brasileiras — atas de registro de preço. Origem específica (PNCP/Comprasnet) não especificada.

## Resultados

Pipeline reduz significativamente o tempo de busca por irregularidades. Prototipagem validou viabilidade em dados reais.

## Limitações

- Dependência de qualidade e padronização dos documentos
- Keywords precisam de refinamento contínuo
- Métricas quantitativas não reportadas no abstract
