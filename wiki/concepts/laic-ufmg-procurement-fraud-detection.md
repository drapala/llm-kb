---
title: "LAIC/UFMG — Detecção de Fraude em Licitações Públicas Brasileiras"
sources:
  - path: raw/papers/brandao-pappa-2024-plus-pipeline.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/costa-pappa-2023-audit-trails-fraud.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/oliveira-pappa-2023-brasnam-ranking.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/pereira-2022-redes-complexas-licitacao.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/silva-pappa-2024-overpricing-iqr.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/braz-pappa-2024-small-companies-fraud.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/costa-pappa-2022-brasnam-alertas-fraude.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/oliveira-pappa-2022-webmedia-inconsistencies.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/mendes-pappa-2023-doacoes-eleitorais-licitacoes.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/gomide-pappa-2023-mineracao-despesas-municipais.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/brandao-pappa-2023-preprocessing-classification-licitacoes.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/dutra-pappa-2025-fraud-alerts-health.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/brum-pappa-2024-unsupervised-grouping-procurement.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/silva-pappa-2024-govbert-br.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/silva-pappa-2024-domain-adapted-lms-sbbd.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/costa-pappa-2024-sicom-sbbd.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/morais-2024-fraud-prediction-random-forest.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/schmitz-2025-gmm-semisupervised-licitacoes.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-12
updated: 2026-04-12
tags: [procurement-fraud, brazil, licitacao, network-analysis, IQR, audit-trails, UFMG, LAIC, bid-rigging, overpricing, small-companies, NLP, BERT, GMM, semi-supervised, electoral-donations]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
status: promoted
promoted_date: 2026-04-12
freshness_status: impacted
synthesis_sources:
  - raw/papers/brandao-pappa-2024-plus-pipeline.md
  - raw/papers/costa-pappa-2023-audit-trails-fraud.md
  - raw/papers/oliveira-pappa-2023-brasnam-ranking.md
  - raw/papers/pereira-2022-redes-complexas-licitacao.md
  - raw/papers/silva-pappa-2024-overpricing-iqr.md
  - raw/papers/braz-pappa-2024-small-companies-fraud.md
  - raw/papers/costa-pappa-2022-brasnam-alertas-fraude.md
  - raw/papers/oliveira-pappa-2022-webmedia-inconsistencies.md
  - raw/papers/mendes-pappa-2023-doacoes-eleitorais-licitacoes.md
  - raw/papers/gomide-pappa-2023-mineracao-despesas-municipais.md
  - raw/papers/brandao-pappa-2023-preprocessing-classification-licitacoes.md
  - raw/papers/dutra-pappa-2025-fraud-alerts-health.md
  - raw/papers/brum-pappa-2024-unsupervised-grouping-procurement.md
  - raw/papers/silva-pappa-2024-govbert-br.md
  - raw/papers/silva-pappa-2024-domain-adapted-lms-sbbd.md
  - raw/papers/costa-pappa-2024-sicom-sbbd.md
  - raw/papers/morais-2024-fraud-prediction-random-forest.md
  - raw/papers/schmitz-2025-gmm-semisupervised-licitacoes.md
---

## Resumo
O grupo LAIC/UFMG (Pappa, Lacerda, Brandão et al.) publicou 15+ papers (2022–2025) sobre detecção de fraude em licitações públicas brasileiras usando ML, análise de redes, NLP e estatística. Cobrem cinco domínios: (1) pipeline de extração e ranking via audit trails, (2) redes de co-participação de empresas com medidas de centralidade, (3) detecção de sobrepreço via IQR, (4) stack NLP para classificação e agrupamento de documentos governamentais (GovBERT-BR, DAPT, clustering de itens), (5) sinais complementares (doações eleitorais × licitações, despesas municipais peer-comparison, inconsistências CNAE × objeto). Um paper adicional (WCGE 2022, grupo diferente) validou empiricamente centralidade de grafo com dados de investigação real (Operação Licitante Fantasma, precisão >71%). Dois papers externos (UFU/USP Random Forest; UFSC GMM semi-supervisionado) oferecem abordagens alternativas fora do cluster LAIC.

## Conteúdo

### Programa de Pesquisa LAIC — Visão Geral

O grupo construiu um programa incremental:
1. **2022:** Sinais base — audit trails como rede social (BraSNAM); inconsistências CNAE × objeto (WebMedia)
2. **2023:** Ranqueamento com 19 trilhas (BraSNAM); doações eleitorais × licitações (SBBD); despesas municipais peer-comparison (SBBD); pré-processamento de documentos (SBBD); versão journal audit trails (iSys)
3. **2024:** Pipeline completo PLUS (ACM DGOV); sobrepreço IQR (JIS); pequenas empresas geoespacial (JIS); GovBERT-BR (BRACIS); avaliação DAPT (SBBD); agrupamento não-supervisionado de itens (LREC-COLING); SICOM data science (SBBD Estendido)
4. **2025:** Audit trails em saúde pública (iSys)

A maioria dos papers usa dados públicos sem ground truth CGU/TCU sistematizado. Exceção: Pereira 2022 valida com dados da Operação Licitante Fantasma (investigação policial real = ground truth externo, mas com viés de seleção — só empresas já investigadas).

### Sinais de Fraude Identificados

**1. Co-bidding patterns (audit trails):**
- Empresas que sistematicamente participam juntas nos mesmos processos
- Comportamento consistente com bid-rigging: exclusividade de vencedor dentro do grupo
- Modelagem via social network analysis dos históricos de participação

**2. Centralidade em grafos de co-participação (Pereira 2022, WCGE):**
- Nós = empresas, arestas = co-participação em licitações
- Betweenness, Eigenvector, PageRank, Weighted Degree como features
- Validado com Operação Licitante Fantasma: precisão >71%, acurácia 68% — caveats: classe desbalanceada não reportada (fraude é rara; 68% acurácia pode ser trivial dependendo do baseline), amostra retrospectiva de uma única operação
- Empresas fraudulentas tendem a ter centralidade local elevada (degree, weighted degree) na sua rede de co-participação — caveats: betweenness global pode ser baixo (evitam exposição); resultado específico ao contexto de cartel local, não regra geral

**3. Sobrepreço por IQR (Silva 2024):**
- Item padronizado → comparação com distribuição de preços do mesmo item
- Anomalia: preço fora de [Q1 - 1.5×IQR, Q3 + 1.5×IQR]
- Mais robusto a outliers que z-score padrão

**4. 19 trilhas de auditagem (Oliveira BraSNAM 2023):**
- Feature set mais completo documentado pelo grupo
- Modeladas como rede social para ranqueamento integrado
- Detalhes das 19 trilhas não disponíveis sem PDF completo

**5. Padrões geoespaciais em pequenas empresas (Braz 2024):**
- Clusters geográficos de pequenas empresas com alertas de irregularidade
- Comunidades via Fast Unfolding (Blondel 2008)
- Dimensão complementar: onde estão concentradas as irregularidades

**6. Inconsistências CNAE × objeto da licitação (Oliveira WebMedia 2022):**
- Compatibilidade entre item licitado e código CNAE do licitante como sinal de fraude
- Classificação hierárquica: Válido / Duvidoso / Inválido por licitante
- Dado público: CNAE disponível na Receita Federal

**7. Doações eleitorais × faturamento via licitações (Mendes/Pappa SBBD 2023):**
- Sócios de empresas que doam para candidatos eleitos têm aumento de receita de contratos públicos
- Proxy de captura política — sinal ortogonal a bid-rigging e sobrepreço
- Contexto: pós-proibição de doações corporativas diretas (2018); doações de pessoa física como contorno

**8. Peer-comparison de despesas municipais (Gomide/Pappa SBBD 2023):**
- Clustering de municípios por população e microrregião
- Despesas fora do range do cluster de pares = anomalia
- Abordagem complementar: foca em quem compra (municípios) vs. quem vende (empresas)

### Stack NLP do LAIC

O grupo desenvolveu infraestrutura NLP especializada para processamento de documentos governamentais:
- **GovBERT-BR** (Silva/Pappa BRACIS 2024): BERT pré-treinado para português governamental (legal + administrativo). Supera BERTimbau genérico em classificação de documentos públicos.
- **DAPT avaliação** (Silva/Pappa SBBD 2024): factores determinantes do DAPT — dataset alvo > composição linguística > tamanho. BERTimbau + LaBSE com DAPT superam modelos genéricos.
- **Agrupamento não-supervisionado de itens** (Brum/Pappa LREC-COLING 2024): para clustering de itens, embeddings supervisionados não superam métodos não-supervisionados; conhecimento de domínio é o fator crítico. Dataset: 2M+ itens.
- **Pré-processamento e classificação** (Brandão/Pappa SBBD 2023): avaliação sistemática de estratégias de pré-processamento para classificação de documentos de licitação.

### Abordagens Externas ao LAIC

**Random Forest com proxy de multas (Morais/UFU 2024):**
- F1 Score médio 80% anual, Recall 90%
- Limitação: multas como proxy de fraude é impreciso
- Variação sazonal extrema (F1: 0.96 em janeiro → 0.54 em novembro)

**GMM semi-supervisionado (Schmitz/UFSC 2025):**
- Endereça o problema fundamental: escassez de dados rotulados
- Semi-supervisão: poucos casos confirmados como âncoras + grande volume de dados não rotulados
- Alternativa ao z-score heurístico (heurística → modelo aprendido)

### PLUS Pipeline — Arquitetura de Pesquisa/Protótipo

O paper mais maduro (Brandão 2024, ACM) descreve pipeline semi-automatizado:
```
[Documentos de licitação heterogêneos]
  → [Classifier de documentos — 4 meta-classes]
  → [Clustering de itens por similaridade textual]
  → [Reference Price Database]
  → [Detecção de anomalia de preço]
  → [Alertas para auditores]
```

Problema central endereçado: heterogeneidade de formatos de documentos públicos brasileiros.

### Comparação com Sinais Zelox

| Sinal Zelox | Análogo LAIC | Diferença |
|---|---|---|
| `rede_empresas_score` (CNPJ sobrepostos) | Centralidade de grafo (Pereira 2022) | LAIC usa co-participação + centralidade; Zelox usa overlap de CNPJ/sócio |
| `z_score_aditivo_por_tipo` | (sem análogo LAIC) | LAIC não cobre aditivos contratuais. O IQR de Silva 2024 é aplicado a **preços unitários de itens** na fase de licitação — objeto e fase distintos (delta_pct de aditivos × execução contratual). A lógica estatística é análoga; os objetos de medição não são. Possível adaptação: dois tiers de threshold (overpricing + anomalia) em vez de z-score único |
| `compliance_rule` threshold | 19 audit trails (Oliveira 2023) | LAIC tem feature set maior; Zelox tem base teórica mais forte (Lei 14.133) |
| (ausente) | Padrão geoespacial (Braz 2024) | Município como feature contextual não está no Zelox V1.1 |
| (ausente) | Inconsistência CNAE × objeto (Oliveira WebMedia 2022) | Sinal implementável via Receita Federal API; ortogonal aos 4 sinais atuais |
| (ausente) | Doações eleitorais × licitações (Mendes SBBD 2023) | Sinal de captura política; dados TSE públicos e cruzáveis com CNPJ |
| (ausente) | Peer-comparison municipal (Gomide SBBD 2023) | Contextualização do risk_score por porte de município |

## Verificação adversarial

**Claims mais fracos:** (1) todos os papers são STUBs — métricas quantitativas não disponíveis em abstracts; (2) precisão >71% (Pereira 2022) é de grupo diferente, validado com uma única operação policial — ground truth com viés de seleção; (3) "19 trilhas de auditagem" sem detalhamento das trilhas — não é possível comparar diretamente com features do Zelox.

**O que os papers não dizem:** (1) nenhum compara diretamente seus sinais contra o Zelox ou sistemas similares; (2) ground truth em todos os casos é fraco — nenhum usa decisões confirmadas do CGU/TCU sistematicamente; (3) generalização além de Minas Gerais (LAIC) e além de uma operação (Pereira 2022) não avaliada.

**Prior work:** LAIC cita Decarolis implicitamente via bid-rigging patterns, mas não referencia explicitamente a literatura econométrica de procurement fraud (Ferraz & Finan, Zamboni & Litschig).

## Quality Gate
- [x] Wikilinks tipados: sem wikilinks — artigo novo no cluster B2G
- [x] Instance→class: precisão >71% atribuída a Pereira 2022, Operação Licitante Fantasma; "19 trilhas" atribuídas a Oliveira BraSNAM 2023
- [x] Meta-KB separado: comparação Zelox na seção de conteúdo é factual (features vs features); sem referências ao processo do KB
- [x] Resumo calibrado: source_quality medium (STUBs); nota sobre paper 4 ser de grupo diferente

## Conexões
- procurement-manipulation-signals partOf laic-ufmg-procurement-fraud-detection (LAIC confirma empiricamente sinais de bid-rigging de Decarolis com dados brasileiros)

## Fontes

**Cluster LAIC/UFMG — Pipeline principal:**
- [Brandão & Pappa 2024](../../raw/papers/brandao-pappa-2024-plus-pipeline.md) — PLUS pipeline, meta-classifier, reference price DB (ACM DGOV, STUB)
- [Costa & Pappa 2023](../../raw/papers/costa-pappa-2023-audit-trails-fraud.md) — audit trails, co-bidding, cartel detection (iSys, STUB)
- [Costa & Pappa 2022](../../raw/papers/costa-pappa-2022-brasnam-alertas-fraude.md) — versão conferência de audit trails via redes sociais (BraSNAM 2022, STUB)
- [Oliveira & Pappa 2023](../../raw/papers/oliveira-pappa-2023-brasnam-ranking.md) — 19 audit trails, ranking via grafo social (BraSNAM 2023, STUB)
- [Oliveira & Pappa 2022](../../raw/papers/oliveira-pappa-2022-webmedia-inconsistencies.md) — inconsistências CNAE × objeto, Válido/Duvidoso/Inválido (WebMedia 2022, STUB)
- [Silva & Pappa 2024](../../raw/papers/silva-pappa-2024-overpricing-iqr.md) — sobrepreço via IQR, padronização textual, R²=95% vs ANP (JIS 2024, FULL)
- [Braz & Pappa 2024](../../raw/papers/braz-pappa-2024-small-companies-fraud.md) — pequenas empresas, geoespacial, Fast Unfolding (JIS 2024, STUB)
- [Mendes & Pappa 2023](../../raw/papers/mendes-pappa-2023-doacoes-eleitorais-licitacoes.md) — doações eleitorais × faturamento via licitações, eleições MG 2020 (SBBD 2023, STUB)
- [Gomide & Pappa 2023](../../raw/papers/gomide-pappa-2023-mineracao-despesas-municipais.md) — despesas municipais peer-comparison, clustering por microrregião (SBBD 2023, STUB)
- [Dutra & Pappa 2025](../../raw/papers/dutra-pappa-2025-fraud-alerts-health.md) — audit trails em saúde pública, ranqueamento comportamental (iSys 2025, STUB)

**Cluster LAIC/UFMG — Stack NLP:**
- [Silva & Pappa 2024 GovBERT](../../raw/papers/silva-pappa-2024-govbert-br.md) — GovBERT-BR, BERT especializado para português governamental (BRACIS 2024, STUB)
- [Silva & Pappa 2024 DAPT](../../raw/papers/silva-pappa-2024-domain-adapted-lms-sbbd.md) — avaliação DAPT para classificação governamental (SBBD 2024, STUB)
- [Brum & Pappa 2024](../../raw/papers/brum-pappa-2024-unsupervised-grouping-procurement.md) — 8 representações textuais para clustering de itens, 2M+ itens (LREC-COLING 2024, STUB)
- [Brandão & Pappa 2023](../../raw/papers/brandao-pappa-2023-preprocessing-classification-licitacoes.md) — pré-processamento e representação para classificação de documentos de licitação (SBBD 2023, STUB)
- [Costa & Pappa 2024 SICOM](../../raw/papers/costa-pappa-2024-sicom-sbbd.md) — ciência de dados sobre base SICOM, colaboração governamental (SBBD Estendido 2024, STUB)

**Grupo diferente — validação externa:**
- [Pereira et al. 2022](../../raw/papers/pereira-2022-redes-complexas-licitacao.md) — centralidade em grafo, precisão >71%, Operação Licitante Fantasma (WCGE 2022, STUB) ⚠️ grupo diferente de Pappa
- [Morais/UFU 2024](../../raw/papers/morais-2024-fraud-prediction-random-forest.md) — Random Forest, F1=80%, variação sazonal, proxy multas (Cadernos Finanças Públicas 2024, STUB) ⚠️ grupo UFU/FAGEN
- [Schmitz/UFSC 2025](../../raw/papers/schmitz-2025-gmm-semisupervised-licitacoes.md) — GMM semi-supervisionado, escassez de labels, dissertação (UFSC 2025, STUB) ⚠️ grupo UFSC
