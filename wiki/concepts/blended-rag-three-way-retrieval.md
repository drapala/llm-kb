---
reads: 1
last_read: 2026-04-13
retrievals_correct: 1
title: "Blended RAG — Three-Way Retrieval"
sources:
  - path: raw/articles/ibm-2024-blended-rag-three-way-retrieval.md
    type: article
    quality: secondary
    stance: confirming
created: 2026-04-13
updated: 2026-04-13
tags: [rag, hybrid-search, retrieval, bm25, splade, colbert, zelox]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
---

## Resumo

Three-way retrieval (BM25 + dense vector + SPLADE sparse) supera todas as combinações de dois fatores em nDCG segundo IBM Research (2024). Cada retriever cobre um caso de query distinto. ColBERT como reranker in-database é mais eficiente que rerankers externos. Top-K expandido (top-1000) antes do reranking maximiza recall sem custo de latência visível.

## Conteúdo

### Os Três Retrievers e seus Casos

| Retriever | Melhor para |
|-----------|-------------|
| BM25 (keyword) | Queries exatas: CNPJ, número de processo, valor exato |
| Dense vector | Queries semânticas: "contrato de manutenção predial" sem termo exato |
| SPLADE (sparse learned) | Jargão técnico: siglas, termos normativos |

SPLADE aprende vocabulário esparso alinhado com o domínio, complementando BM25 para termos técnicos que BM25 perde por frequência baixa no corpus.

### Hierarquia de Desempenho (nDCG)

BM25 + dense + sparse > BM25 + dense > BM25 > dense isolado

ColBERT in-database elimina round-trip de reranker externo, mantendo latência baixa mesmo com top-1000 candidatos.

### Limitações da Fonte

- Relatório técnico IBM/infiniflow, sem arxiv formal
- Avaliado em datasets genéricos — desempenho em corpus de DOs não documentado
- SPLADE treinado em inglês — sparse vectors para PT-BR de licitações podem não funcionar bem
- Complexidade operacional: três índices simultâneos (manutenção, sincronização, storage)

## Interpretação

(⚠️ nossa interpretação) Para Zelox — aplicação direta dos três retrievers:
- BM25: CNPJ, número de contrato, número de processo (correspondência exata)
- Dense: objeto do contrato por semântica ("pavimentação" ↔ "obras de calçamento")
- SPLADE: vocabulário normativo PT-BR (pregão eletrônico, dispensa de licitação, CATMAT, SICAF)

(⚠️ nossa interpretação) Risco principal: SPLADE pré-treinado em inglês provavelmente não captura bem o vocabulário normativo BR. Alternativa: treinar sparse model em corpus PNCP antes de adotar SPLADE.

(⚠️ nossa interpretação) O CrossEncoderReranker do METAXON equivale funcionalmente ao ColBERT in-database — validação indireta da arquitetura existente.

(⚠️ nossa interpretação) Verificação adversarial: this paper não compara contra late chunking ou SAC — o ganho do three-way retrieval pode ser parcialmente sobreposto com melhorias de chunking. Baseline experimental separado necessário.

## Conexões

- validates: [[hybrid-search]] — three-way retrieval estende modelo BM25 + dense do QMD com sparse (SPLADE)
- complementa: [[summary-augmented-chunking]] — SAC resolve DRM; three-way retrieval maximiza recall em corpus diverso
- derivedFrom: [[legal-bert-pt-models]] — modelo de embedding PT-BR adequado é prerequisito para tier dense

## Fontes

- [IBM Research 2024](../../raw/articles/ibm-2024-blended-rag-three-way-retrieval.md) — three-way retrieval superior, ColBERT in-database, top-1000 antes do reranking
