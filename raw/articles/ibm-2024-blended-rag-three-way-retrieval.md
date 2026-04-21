# Blended RAG — Three-Way Retrieval (IBM Research, 2024)

**Origem:** IBM Research  
**URL:** infiniflow.org/blog/best-hybrid-search-solution (análise comparativa)  
**Publicado:** 2024  
**Type:** STUB — relatório técnico; sem arxiv

---

## Hipótese Central

Three-way retrieval (BM25 full-text + dense vector + sparse vector/SPLADE) supera todas as combinações de dois fatores em nDCG. ColBERT como reranker in-database amplifica o ganho sem custo de latência de reranker externo.

---

## Evidências

- IBM Research comparou sistematicamente: BM25, dense, BM25+dense, dense+sparse, BM25+dense+sparse
- **Three-way retrieval é a combinação ótima** em nDCG
- ColBERT reranker in-database é mais eficiente que rerankers externos (sem round-trip)
- Top-K expandido (top-1000) antes do reranking maximiza recall sem custo de latência visível ao usuário
- SPLADE (sparse learned vocabulary) complementa BM25 para jargão técnico

---

## Por que Three-Way?

Cada retriever cobre um caso diferente:

| Retriever | Cobre bem |
|-----------|-----------|
| BM25 (keyword) | Queries exatas: CNPJ, número de processo, valor exato |
| Dense vector | Queries semânticas: "contrato de manutenção predial" sem termo exato |
| SPLADE (sparse) | Jargão técnico: siglas, termos normativos (pregão, dispensa, CATMAT) |

---

## Limitações / Falsificadores

- Complexidade operacional de três índices simultâneos é significativa (manutenção, sincronização, storage)
- SPLADE é treinado em inglês — sparse vectors para jargão técnico PT-BR de licitações podem não funcionar bem
- Avaliado em datasets genéricos — performance em corpus de DOs não documentada

---

## Applicabilidade Zelox

**ALTA como arquitetura alvo de longo prazo.**

Para o contexto de DO:
- BM25: CNPJ, número de contrato, número de processo
- Dense: objeto do contrato, modalidade (por semântica, não só keyword)
- SPLADE/sparse: vocabulário normativo BR (pregão eletrônico, dispensa de licitação, CATMAT, SICAF)

O CrossEncoderReranker já em uso no METAXON equivale ao ColBERT in-database — isso valida a arquitetura existente como correta.

**Risco:** SPLADE para PT-BR de licitações é o componente mais incerto. Alternativa: treinar sparse model em corpus PNCP em vez de usar SPLADE pré-treinado em inglês.

---

## Conexões

- Confirma: hybrid-search.md (BM25 + dense como base)
- Complementa: DAT Dynamic Alpha Tuning (pesos dinâmicos entre os três retrievers)
- Relaciona com: CrossEncoderReranker do METAXON (equivalente ao ColBERT in-database)
