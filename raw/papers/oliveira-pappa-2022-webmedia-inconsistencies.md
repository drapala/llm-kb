# Detecting Inconsistencies in Public Bids: An Automated and Data-based Approach

**Autores:** Gabriel P. Oliveira, Arthur P. G. Reis, Felipe A. N. Freitas, Lucas G. L. Costa, Mariana O. Silva, Pedro Brum, Samuel E. L. Oliveira, Michele A. Brandão, Anisio Lacerda, Gisele Pappa (UFMG/IFMG)
**Publicação:** Brazilian Symposium on Multimedia and the Web (WebMedia 2022)
**DOI:** 10.1145/3539637.3558230
**Grupo:** LAIC — UFMG
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract.

---

## Tese Central

Detecção de inconsistências em licitações públicas via análise de compatibilidade entre **itens da licitação** e **códigos CNAE** do licitante. Abordagem hierárquica de decisão classifica licitantes como Válido, Duvidoso ou Inválido.

## Metodologia

- Análise de dados públicos de licitações via Web
- Decisão hierárquica: 3 classes por licitante (Válido / Duvidoso / Inválido)
- Sinal: compatibilidade entre descrição do item licitado e CNAE do licitante
- Combinação de dados cadastrais + extração de descrição dos itens

## Resultados

- Combinação de dados cadastrais + extração de itens ajuda na detecção de fraude
- Reduz o número de licitações que um especialista precisa analisar
- (métricas quantitativas não disponíveis no abstract)

## Relevância para Zelox

**Sinal direto e implementável:**
- A incompatibilidade CNAE × objeto contratado é um sinal de anomalia que o Zelox não tem explicitamente
- Implementável via join CNPJ → CNAE da Receita Federal × tipo de objeto do contrato
- Categorias Válido/Duvidoso/Inválido são análogas ao risk_score do Zelox (low/medium/high)
- Dado público: CNAE disponível na Receita Federal via API

## Conexão com outros papers do grupo

Este paper introduz o sinal CNAE × item que é incorporado no PLUS pipeline (Brandão 2024). Representa a dimensão de "inconsistência de habilitação" do licitante — distinta de sobrepreço (Silva 2024) e co-participação (Costa 2022/2023).
