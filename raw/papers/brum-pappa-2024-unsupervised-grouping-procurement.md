# Unsupervised Grouping of Public Procurement Similar Items: Which Text Representation Should I Use?

**Autores:** Pedro P. V. Brum, Mariana O. Silva, Gabriel P. Oliveira, Lucas G. L. Costa, Anisio Lacerda, Gisele Pappa (UFMG)
**Publicação:** Proceedings of the Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), Torino, pp. 17176–17185
**URL:** https://aclanthology.org/2024.lrec-main.1492/
**Grupo:** LAIC — UFMG
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract da ACL Anthology.

---

## Tese Central

Para agrupamento não-supervisionado de itens de compras públicas, representações sofisticadas **supervisionadas** oferecem pouca vantagem sobre métodos não-supervisionados. O **conhecimento contextual de domínio** é o fator mais importante para melhoria da representação.

## Problema

Itens de compras públicas não são padronizados — mesma descrição aparece em dezenas de formas. Para estabelecer preços de referência, é necessário agrupar itens similares. O paper testa sistematicamente qual representação textual funciona melhor.

## Metodologia

- Framework para limpeza, extração e representação textual
- 8 representações distintas de sentenças testadas
- Dataset: >2 milhões de itens de compras públicas
- Tarefa: clustering não-supervisionado de itens similares

## Resultados

- Métodos supervisionados sofisticados para vetorização oferecem pouca vantagem em tarefas não-supervisionadas
- Conhecimento contextual de domínio específico é crucial para melhoria de representação
- (métricas quantitativas completas não disponíveis no abstract)

## Relevância para Zelox

**Alta relevância técnica para o problema de agrupamento de itens:**
- Valida a estratégia "Words" de Silva/Pappa 2024 de um ângulo diferente (NLP)
- Resultado contra-intuitivo: embeddings supervisionados ≠ melhor clustering → implicação para feature engineering do Zelox
- O pipeline de normalização de descrições (Zelox faz grouping por tipo de objeto) pode se beneficiar do framework de 8 representações
- Dataset de 2M itens sugere escala de dados disponível no SICOM/PNCP compatível com abordagens de clustering

## Conexão com outros papers do grupo

Complementa diretamente Silva/Pappa 2024 (overpricing IQR): aquele paper usa a estratégia "Words" para normalização; este paper avalia sistematicamente qual representação é mais eficaz para o mesmo problema.
