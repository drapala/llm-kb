# Usando Redes Complexas na Identificação de Empresas Fraudulentas em Licitações Públicas

**Autores:** Ane Karoline da Silva Pereira, Yuran Moreira Vita, Gardenya da Silva Felix, João Mateus Freitas Gimaque, Marcos Luan Sousa Damasceno, Bruno César Barreto de Figueirêdo
**Publicação:** WCGE 2022 (Workshop de Computação Aplicada em Governo Eletrônico)
**URL:** https://sol.sbc.org.br/index.php/wcge/article/view/20707
**Nota de proveniência:** ⚠️ Este paper é do WCGE 2022 — autores DIFERENTES do grupo LAIC/Pappa. Identificado durante scout focado em Pappa por similaridade temática. Pode não ser da UFMG.
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract.

---

## Tese Central

Aplicar análise de redes complexas e medidas de centralidade para identificar automaticamente empresas envolvidas em conluios em licitações públicas. Motivação: detecção manual é inviável no volume de dados disponíveis.

## Metodologia

**Construção do grafo:**
- Nós = empresas licitantes
- Arestas = co-participação em licitações (empresas que concorreram nos mesmos processos)

**Medidas de centralidade usadas:**
- Betweenness (BW) — empresas que conectam clusters diferentes
- Eigenvector Centrality (EV) — empresas conectadas a empresas influentes
- PageRank (PR) — importância relativa no grafo
- Weighted Degree (WD) — volume de conexões ponderado

**Modelo NDNS:** Detecção eficiente de nós relevantes em cenários multi-rede

**Validação:** Correlações Pearson/Spearman entre métricas de centralidade e ganhos empresariais em licitações

## Dados

Janeiro 2021 — Junho 2022. Baseado em dados da **Operação Licitante Fantasma** (investigação real).

## Resultados

- Precisão: >71%
- Acurácia: 68%
- Centralidade correlacionada com ganhos em licitações em empresas envolvidas na operação

## Limitações

- Período limitado (18 meses)
- Possível desbalanceamento de classes (fraude é rara vs. legítimo)
- Ground truth: empresas da Operação Licitante Fantasma — viés de seleção

## Relevância para Zelox

Validação empírica de que medidas de centralidade em grafo de co-participação identificam empresas fraudulentas. Diretamente análogo ao `rede_empresas_score` do Zelox. Betweenness e PageRank são candidatos a features adicionais além de contagem simples de CNPJ sobrepostos.
