---
reads: 1
last_read: 2026-04-13
retrievals_correct: 1
title: "Summary-Augmented Chunking (SAC)"
sources:
  - path: raw/papers/reuter-2025-summary-augmented-chunking-legal-rag.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-13
updated: 2026-04-13
tags: [rag, chunking, legal, retrieval, zelox]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
---

## Resumo

Summary-Augmented Chunking (SAC) resolve o Document-Level Retrieval Mismatch (DRM) em RAG legal: ao prepend de um resumo de ~150 chars do documento-pai a cada chunk, o retriever distingue documentos estruturalmente similares. Em corpora de NDAs, DRM supera 95% no baseline padrão; SAC reduz o mismatch à metade. Surpreendentemente, resumo genérico supera resumo guiado por especialistas legais.

## Conteúdo

### Document-Level Retrieval Mismatch (DRM)

DRM é a proporção de chunks top-k recuperados que não se originam do documento contendo o texto ground-truth. Em documentos legais com linguagem boilerplate padronizada (NDAs, políticas de privacidade), o retriever confunde documentos por alta similaridade léxica/semântica.

Resultado empírico (ContractNLI, 362 NDAs): DRM > 95% no pipeline RAG padrão — o retriever quase sempre retorna chunk do documento errado.

Por que DRM importa em contexto legal: profissionais legais exigem raciocínio documento-fiel. Mesmo resposta factualmente correta por coincidência é inválida se não rastreável ao documento específico.

### Metodologia SAC

1. **Sumarização:** LLM gera resumo de ~150 caracteres por documento ("impressão digital")
2. **Chunking:** recursive character splitting (chunk size 500 chars, sem overlap)
3. **Augmentação:** resumo prepended a cada chunk derivado do documento
4. **Indexação:** chunks augmentados embarcados e indexados

Custo adicional: uma chamada de LLM por documento. Integra em pipelines RAG existentes sem mudança arquitetural.

Modelo de sumarização: gpt-4o-mini. Embedder: `thenlper/gte-large`. Banco vetorial: FAISS.

### Resultados no LegalBench-RAG

| Dataset | DRM Baseline | DRM SAC | Precisão SAC |
|---------|-------------|---------|-------------|
| ContractNLI (NDAs) | >95% | ~47% | 97% |
| CUAD | melhora | sim | — |
| MAUD | melhora | sim | — |
| PrivacyQA | melhora | sim | — |

SAC reduz DRM à metade em toda gama de hiperparâmetros. SAC genérico (150 chars) supera SAC expert-guided em retrieval de texto.

### Achado Contraintuitivo: Genérico > Especializado

Resumo guiado por especialistas legais (focado em variáveis diferenciadoras: partes, prazo, lei aplicável para NDAs) não supera o prompt genérico.

Hipóteses: (1) resumo genérico cobre maior variedade de queries; (2) linguagem densa especializada comprime mal em vetor de embedding de tamanho fixo.

### Limitações

- Testado exclusivamente em inglês e documentos common-law
- DRM residual significativo mesmo após SAC
- Avaliação cobre apenas etapa de recuperação, não geração end-to-end
- Corpora contratuais, não administrativos

## Interpretação

(⚠️ nossa interpretação) Para o Zelox, o análogo de DRM existe em DOs com atos boilerplate idênticos exceto por CNPJ e valor. SAC resolve: prepend do resumo do ato distingue "Contrato 001/2025 com Empresa X" de "Contrato 002/2025 com Empresa Y".

(⚠️ nossa interpretação) O achado "genérico supera especializado" sugere cautela ao tentar criar prompts muito específicos para entidades de licitação. Um prompt genérico pode ser mais robusto à diversidade de queries do Zelox.

(⚠️ nossa interpretação) Verificação adversarial: SAC não substitui segmentação por ato — só melhora a indexação após segmentação. Um corpus de atos não-segmentados (DO inteiro como chunk) não é resolvido por SAC.

## Conexões

- validates: [[retrieval-augmented-generation]] — SAC como intervenção pré-retrieval em corpora legais
- complementa: [[hybrid-search]] — BM25 por CNPJ + SAC para desambiguação semântica entre atos similares
- contradicts: [[late-chunking-contextual-embeddings]] — Late Chunking é alternativa sem LLM adicional; cada método cobre caso diferente

## Fontes

- [Reuter et al. 2025](../../raw/papers/reuter-2025-summary-augmented-chunking-legal-rag.md) — definição de DRM, metodologia SAC, experimentos LegalBench-RAG, ContractNLI >95% DRM
