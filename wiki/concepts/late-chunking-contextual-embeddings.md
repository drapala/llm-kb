---
title: "Late Chunking — Embeddings Contextuais"
sources:
  - path: raw/papers/gunther-2024-late-chunking-contextual-embeddings.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-13
updated: 2026-04-13
tags: [chunking, embedding, retrieval, rag, jina]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
---

## Resumo

Late Chunking (Jina AI, 2024) aplica chunking *depois* do transformer, não antes: o documento inteiro é processado no transformer primeiro, depois mean pooling é aplicado por chunk. Isso preserva contexto cross-chunk nos embeddings sem custo de LLM adicional. Melhoria média de 3.5% em nDCG@10 vs naive chunking em benchmarks BeIR. Chunking melhora retrieval em +24% vs sem chunking, mesmo com modelos de 8K context.

## Conteúdo

### O Problema: Perda de Contexto no Naive Chunking

Em naive chunking, cada chunk é processado isoladamente. Pronomes e referências que dependem de contexto anterior têm embeddings semanticamente desconectados do antecedente.

Evidência (query "Berlin"): naive chunking — chunks sem "Berlin" têm cosine similarity 0.71-0.75; late chunking — mesmos chunks têm similarity 0.82-0.85 porque os token embeddings já capturaram o referente.

### Algoritmo Late Chunking

1. Tokeniza o documento inteiro
2. Processa todos os tokens no transformer → embeddings de token contextualizados
3. Aplica mean pooling por chunk (usando boundary cues do algoritmo de chunking escolhido)

O chunking (fixed-size, sentence, semantic) determina *onde* fazer pooling, não é aplicado antes da transformação.

**Long Late Chunking:** para documentos maiores que a janela do modelo, processa em macro-chunks com overlap ω. Supera truncação simples.

**Span Pooling (fine-tuning):** variante supervisionada com InfoNCE loss — melhoria adicional consistente mas pequena.

### Resultados (nDCG@10, médias BeIR 4 datasets)

| Estratégia | Naive AVG | Late AVG | Ganho |
|-----------|-----------|----------|-------|
| Fixed-size (256 tok) | 52.2% | 54.0% | +3.46% |
| Sentence boundaries (5 sent) | 52.4% | 54.3% | +3.63% |
| Semantic sentence | 52.4% | 53.8% | +2.70% |

Ganho é consistente através de modelos (jina-v2, jina-v3, nomic) e estratégias de chunking.

### Chunking vs. Sem Chunking (Appendix)

| Dataset | Sem chunking (8192 tok) | Chunking 512 tok |
|---------|------------------------|-----------------|
| NarrativeQA | 32.73 | 47.63 (+45%) |
| 2WikiMultiHopQA | 70.32 | 86.30 (+23%) |
| QMSum | 36.81 | 48.34 (+31%) |

Melhoria média: +24.47%. Chunking é benéfico mesmo quando documentos cabem na janela do modelo.

### Comparação com SAC (Anthropic Contextual Retrieval)

Experimento qualitativo: late chunking e contextual retrieval (prepend de contexto gerado por LLM) ambos identificam o chunk relevante com alta similarity. Naive chunking falha. Late chunking **não requer LLM adicional** — vantagem operacional.

### Limitações

- Não ajuda em "needle in haystack" tasks (contexto do documento é irrelevante para o chunk)
- Chunks grandes em reading comprehension: naive pode superar late em casos específicos
- Dados de fine-tuning (span pooling) restritos a Wikipedia

## Interpretação

(⚠️ nossa interpretação) Para o Zelox: late chunking é preferível a SAC quando o custo de LLM por ato é proibitivo (corpus grande, ingestão contínua). Trade-off: late chunking requer modelo de contexto longo (jina-embeddings-v3 = 8K context), SAC requer LLM call mas funciona com qualquer embedder.

(⚠️ nossa interpretação) Verificação adversarial: late chunking não resolve DRM (Document-Level Retrieval Mismatch) descrito por Reuter 2025 — o problema de confundir *documentos* distintos com vocabulário boilerplate similar. Late chunking melhora *intra-document* context; SAC melhora *inter-document* disambiguation. São complementares, não substitutos.

(⚠️ nossa interpretação) Overlap entre chunks: evidência do paper (Appendix A.2) mostra que overlap não melhora desempenho — simplificação válida para Zelox: usar zero overlap.

## Conexões

- contradicts: [[summary-augmented-chunking]] — SAC resolve DRM via context injection; late chunking resolve loss de contexto intra-documento — complementares, não substitutos
- validates: [[retrieval-augmented-generation]] — chunking +24% vs sem chunking mesmo com 8K context window
- complementa: [[hierarchical-chunking-rag]] — late chunking é flat; HiChunk adiciona hierarquia multi-nível

## Fontes

- [Günther et al. 2024](../../raw/papers/gunther-2024-late-chunking-contextual-embeddings.md) — algoritmo, BeIR benchmark +3.5% nDCG@10, long late chunking, span pooling, comparação vs SAC
