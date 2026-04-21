# Heterogeneous Graph Neural Networks for Fraud Detection and Explanation in Supply Chain Finance

**Autores:** Bin Wu, Kuo-Ming Chao, Yinsheng Li  
**Publicação:** Information Systems (Elsevier), Vol. 121, Março 2024  
**DOI:** 10.1016/j.is.2023.102335  
**URL:** https://www.sciencedirect.com/science/article/abs/pii/S0306437923001710  
**Ano:** 2024  
**Tipo:** paper / primary  
**Status:** STUB — full text não acessível; conteúdo baseado em abstract e metadados.

---

## Tese Central

**MultiFraud:** framework de detecção de fraude em supply chain finance usando GNNs heterogêneas com aprendizado multitarefa e explicabilidade. O problema central: fraudes em financiamento de cadeia de suprimentos envolvem múltiplos tomadores simultaneamente usando "truques sofisticados" — análise de entidades isoladas é insuficiente. MultiFraud modela o grafo completo de relacionamentos.

## Arquitetura

**Estrutura do grafo:**
- **Nós:** múltiplas entidades da supply chain — empresas, tomadores, fornecedores
- **Arestas:** relações heterogêneas — transações financeiras, relacionamentos comerciais, ownership

**Mecanismo heterogêneo:**
- Grafos separados por domínio (multi-view) para preservar semântica de cada tipo de relação
- GNNs heterogêneas aplicadas a cada view
- Mecanismo de atenção para compartilhamento de embeddings entre entidades

**Multi-task learning:**
- Treinamento simultâneo de detecção em múltiplas entidades
- Componente de explicabilidade: pesos de features e arestas por decisão

## Resultados

- Avaliado em 5 datasets
- Supera métodos state-of-the-art (métricas específicas não divulgadas no abstract)
- Fornece "explicações abrangentes em múltiplos grafos heterogêneos"

## Requisitos de Dados

- Dados de transações de múltiplos stakeholders da supply chain
- **Ground truth obrigatório:** labels indicando tomadores fraudulentos vs. legítimos
- Múltiplas views das mesmas entidades para validação cross-domain

## Limitações

- Ground truth necessário — não funciona sem labels supervisionados
- Métricas de performance não divulgadas no abstract
- Escalabilidade e complexidade computacional não discutidas
- Dataset público não disponibilizado
