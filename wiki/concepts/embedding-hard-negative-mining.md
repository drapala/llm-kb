---
title: "Hard Negative Mining para Embedding Models"
sources:
  - path: raw/papers/moreira-2024-nv-retriever-hard-negative-mining.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-14
updated: 2026-04-14
tags: [embedding, retrieval, fine-tuning, contrastive-learning, hard-negatives, rag, zelox]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
---

## Resumo

NV-Retriever (NVIDIA, 2024) introduz positive-aware hard-negative mining: usa o relevance score do positivo como âncora para remover false negatives antes do treinamento contrastivo de embeddings. NV-Retriever-v1 atingiu MTEB Retrieval 60.9 (#1 em Jul 2024). Resultado principal: false negatives em hard-negative selection degradam modelos; filtragem por positive score remove o problema com ganho consistente.

## Conteúdo

### O Problema: Hard Negatives com False Negatives

Treinamento contrastivo de embedding models:
- **Positivo:** (query, doc_relevante) — par correto
- **Negative aleatório:** doc irrelevante — fácil demais; pouco gradiente de aprendizado
- **Hard negative:** doc semanticamente similar mas irrelevante — força discriminação; alto gradiente

O problema: em corpora com muitos documentos similares, **hard negatives às vezes são genuinamente relevantes** (false negatives). Incluí-los como negativos faz o modelo aprender a se afastar de documentos relevantes.

### Solução: Positive-Aware Mining

NV-Retriever usa o score de relevância do positivo como âncora:

```
aceitar_como_negative(cand) IF score(query, cand) << score(query, positive)
```

Um candidato só vira negative se seu score é significativamente menor que o do positivo confirmado. Isso remove false negatives antes do treinamento.

**Família de métodos:** diferentes formas de calcular o threshold (absoluto, relativo, percentual) — paper faz ablation study em todas.

### Resultados

- NV-Retriever-v1: **MTEB Retrieval (BEIR) = 60.9** — 1º lugar quando publicado (Jul 2024)
- Positive-aware mining supera standard hard-negative mining em todas as configurações testadas
- Funciona com diferentes teacher models e base models
- Treinamento mais rápido (menos iterações necessárias com negatives de qualidade)

### Contexto de Mercado (2024)

MTEB Retrieval é o benchmark padrão para embedding models de retrieval. 60.9 no BEIR (inglês) era state-of-the-art em julho 2024 — desde então outros modelos superaram, mas a metodologia de mining permanece relevante.

## Interpretação

(⚠️ nossa interpretação) Para fine-tuning de embeddings em corpus de DOs, o false negative problem é **agudo**: dois extratos de contrato similares (mesmo objeto, empresas diferentes) podem ambos ser relevantes para a mesma query ("contratos de manutenção predial"). Se um é positivo e o outro vira negative, o modelo aprende errado.

(⚠️ nossa interpretação) Positive-aware mining requer um teacher model para scoring — overhead de inference antes do treinamento. Para corpus de DOs, pode-se usar BM25 como teacher de primeira iteração (cheap, sem GPU) e refinar com dense model.

(⚠️ nossa interpretação) Esta técnica é mais relevante para Zelox V2 (fine-tuning de embeddings em corpus PNCP) do que para MVP. No MVP, embedder pré-treinado (jina-v3 ou RoBERTaLexPT) sem fine-tuning provavelmente é suficiente.

## Verificação Adversarial

**Claim mais fraco:** "positive-aware mining causa treinamento mais rápido" — depende do overhead de scoring dos candidatos, que o paper não quantifica separadamente.

**O que o paper NÃO diz:**
1. Não testa em línguas além do inglês
2. Não testa em domínios legais/administrativos
3. Não compara com other deduplication strategies (e.g., SimCSE, E5)

**Prior work:** o paper cita E5, GTE, Gecko — família de embedding models que NV-Retriever supera.

## Conexões

- validates: [[blended-rag-three-way-retrieval]] — embedding quality é prerequisito para dense tier funcionar; hard-negative mining melhora o embedding base
- complementa: [[legal-bert-pt-models]] — metodologia de fine-tuning para LegalBert-pt/RoBERTaLexPT em corpus DO

## Fontes

- [NV-Retriever 2024 (NVIDIA)](../../raw/papers/moreira-2024-nv-retriever-hard-negative-mining.md) — positive-aware mining, false negative removal, MTEB 60.9

## Quality Gate

- [x] Wikilinks tipados: 2 relações tipadas
- [x] Instance→class: MTEB 60.9 qualificado como "NV-Retriever-v1, BEIR benchmark, inglês, Jul 2024"
- [x] Meta-KB separado: sim — referências Zelox em Interpretação
- [x] Resumo calibrado: sim
