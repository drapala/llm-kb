---
title: "Semantic Chunking — Custo vs. Benefício"
sources:
  - path: raw/papers/qu-2024-semantic-chunking-computational-cost.md
    type: paper
    quality: primary
    stance: challenging
    challenging_type: content
  - path: raw/articles/nvidia-2024-chunking-benchmark-rag.md
    type: article
    quality: secondary
    stance: confirming
created: 2026-04-13
updated: 2026-04-13
tags: [chunking, rag, retrieval, evaluation]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - wiki/concepts/retrieval-augmented-generation.md
---

## Resumo

Semantic chunking (dividir documentos em segmentos semanticamente coerentes) NÃO justifica custo computacional adicional vs fixed-size chunking em avaliação sistemática (NAACL 2025). Benefícios são altamente dependentes de contexto, inconsistentes e frequentemente mascarados pela qualidade dos embeddings. Fixed-size chunking com overlap é a escolha mais eficiente para aplicações práticas de RAG.

## Conteúdo

### Estratégias Avaliadas (Qu et al. 2024)

**Fixed-size chunking:** divide sequencialmente em N sentenças com overlap entre chunks consecutivos.

**Breakpoint-based semantic chunking:** insere breakpoint onde distância semântica entre sentenças consecutivas excede limiar. Decisão local (apenas 2 sentenças por vez).

**Clustering-based semantic chunking:** agrupa sentenças por algoritmo de clustering (single-linkage, DBSCAN) com distância combinada:

```
d(a, b) = λ · d_pos(a, b) + (1-λ) · d_cos(a, b)
```

### Resultados em Recuperação de Documentos (F1@5)

| Dataset tipo | Fixed-size win | Semantic win |
|-------------|---------------|-------------|
| Documentos stitched (artificiais) | — | Breakpoint ganha em 4/6 |
| Documentos originais (reais) | Ganha em 3/4 | — |

Em datasets reais (HotpotQA, MSMARCO, ConditionalQA, Qasper), fixed-size supera semantic chunkers.

Recuperação de evidências: fixed-size ganhou em 3/5 datasets; diferenças mínimas (< 1 pp).

Geração de respostas (BERTScore): diferenças praticamente nulas em todos os datasets.

### Por que semantic chunking não supera?

- Quando embeddings são fortes, diferenças entre estratégias de chunking tornam-se menos relevantes
- Vantagem do semantic só aparece em documentos com diversidade artificial de tópicos (stitched = concatenação aleatória)
- Documentos reais têm tópicos menos diversificados — a condição para semantic chunking ajudar raramente se verifica

### NVIDIA Benchmark (2024): Query-Type → Chunk Size

Page-level chunking maximiza acurácia (0.648) para documentos paginados.

| Tipo de query | Chunk size ótimo |
|---------------|-----------------|
| Factoid (entidade exata) | 256-512 tokens |
| Analytical (cross-section) | 1024+ tokens |

Semantic chunking melhora recall em até 9% mas com custo 10× maior.

### Adversarial Check

O que os papers NÃO dizem:
- Qu et al. testam principalmente corpora genéricos (BEIR), não domínios legais/administrativos
- Documentos de DO com vocabulário compartilhado entre seções podem ser exatamente o caso onde semantic chunking é mais problemático (confirmado empiricamente por UnB/PPGI 2021)
- Fixed-size pode produzir DRM alto em corpora boilerplate — problema documentado por SAC (Reuter 2025)

## Interpretação

(⚠️ nossa interpretação) Para o Zelox: fixed-size é suficiente como estratégia de chunking dentro de um ato já segmentado. O problema difícil é a segmentação por ato (boundary detection), não o chunking interno. Semantic chunking para atos completos seria custo sem benefício verificado.

(⚠️ nossa interpretação) A hierarquia correta para Zelox é: (1) boundary detection por ato (problema hard, sequence labeling), (2) fixed-size chunking dentro do ato (simples), (3) SAC para desambiguação entre atos similares.

## Conexões

- contradicts: [[summary-augmented-chunking]] — SAC mostra que problema de desambiguação cross-document não é resolvido por chunking, mas por context injection
- contradicts: [[retrieval-augmented-generation]] — questiona suposições sobre semantic chunking como melhoria universal
- derivedFrom: [[diario-oficial-segmentation-strategies]] — implicação para pipeline de ingestão de DOs

## Fontes

- [Qu et al. 2024 (NAACL 2025)](../../raw/papers/qu-2024-semantic-chunking-computational-cost.md) — avaliação sistemática em 10 datasets, 3 estratégias, 3 tarefas proxy; resultado: fixed-size superior ou equivalente em datasets reais
- [NVIDIA Chunking Benchmark 2024](../../raw/articles/nvidia-2024-chunking-benchmark-rag.md) — page-level accuracy 0.648, query-type → chunk size mapping, semantic 9% recall mas 10× custo
