---
title: "RAPTOR vs. Flat 3-Layer Retrieval"
sources:
  - path: raw/papers/raptor-recursive-abstractive-retrieval.md
    type: paper
    quality: primary
  - path: raw/papers/long-context-vs-rag-evaluation.md
    type: paper
    quality: primary
  - path: raw/articles/claude-code-internals-harness-engineering.md
    type: article
    quality: primary
  - path: raw/papers/chunking-strategies-rag-comparison.md
    type: paper
    quality: primary
created: 2026-04-03
updated: 2026-04-03
tags: [retrieval, comparison, architecture]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: emergence
emergence_trigger:
  pair: [retrieval-augmented-generation, context-management]
  ask_session: null
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-03
quarantine: true
quarantine_created: 2026-04-04
quarantine_reason: "retrofit — speculative synthesis"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: true
  review_frio: false
  adversarial_or_scout_or_prediction: false
---

## Resumo

RAPTOR (tree-organized retrieval) and the flat 3-layer pattern used in this KB solve the same problem — multi-level abstraction for retrieval — through opposite approaches. RAPTOR automates tree construction via statistical clustering; the KB uses LLM-guided concept extraction. Comparison reveals what already works, what's missing, and what can be borrowed without adding infrastructure.

## Conteúdo

### Structural Comparison

| Dimension | RAPTOR | 3-Layer Flat KB |
|-----------|--------|-----------------|
| Construction | Automatic: chunk → GMM clustering → LLM summarize → re-embed → repeat | LLM-guided: /ingest identifies concepts → writes articles → updates _index |
| Structure | Tree with N levels (depth varies per document) | Exactly 3 fixed levels: _index → concepts/ → raw/ |
| Retrieval | Collapsed tree: cosine similarity across all levels | Sequential escalation: Layer 1 → 2 → 3 |
| Clustering | Soft (GMM): a chunk can belong to multiple clusters | Hard: 1 source maps to max 3 concepts, each concept is 1 article |
| Compression | 0.28 ratio per level (72% compression) | Variable: _index ~150 chars/article, articles ~500-1500 words |
| Infrastructure | SBERT embeddings + GMM + LLM summarization pipeline | Zero — just .md files and an LLM |

### Structural Parallels with RAPTOR (⚠️ analogies, not validation)

**1. _index.md resembles a RAPTOR root node.** RAPTOR's summary nodes contribute 23-57% of useful retrieved content. Our _index with ~150 char pointers serves a similar function (fast orientation), but the mechanism differs: RAPTOR uses embedding-based retrieval across all levels simultaneously; we use sequential LLM reading. The parallel is functional, not mechanical.

**2. Layer 1→2→3 escalation loosely parallels collapsed tree.** RAPTOR's collapsed tree selects nodes from any level by cosine similarity. Our /ask escalates sequentially (index → articles → raw/). Structurally different despite the analogy.

**3. Summarization-based outperforms chunk-based in multi-hop QA benchmarks.** RAPTOR outperforms chunk-based retrievers (38.5% vs 20-22% — from the LC vs RAG paper, not RAPTOR's own benchmarks). Our /ingest groups by concept, which is a different mechanism than RAPTOR's GMM clustering. Both produce multi-level abstractions but through fundamentally different methods. Note: the LC vs RAG paper concludes "neither approach universally dominates" — this heading should not be read as universal superiority.

### Exploitable Gaps (No Infrastructure Required)

**Gap 1: Soft clustering via bidirectional backlinks.**

RAPTOR uses soft clustering: a chunk can belong to multiple clusters. Our /ingest already allows a source to feed multiple articles (max 3 concepts), but the reverse is weak — articles reference sources, but don't systematically reference other articles covering the same sub-concept.

**Improvement:** If two articles cite the same raw/ source, they should have bidirectional wikilinks. This simulates soft clustering via backlinks. In Obsidian, the graph view renders these clusters visually.

**Gap 2: Explicit compression targets per level.**

RAPTOR measures 0.28 ratio (72% compression) per level. We have no compression target. _index.md has ~150 chars/article, but wiki articles vary from 500 to 2000+ words without a target.

**Improvement:** The article template already requires a 2-3 sentence summary. A /review heuristic should enforce that summaries actually function as "intermediate nodes" — if a summary is weak or generic, /review rewrites it. This improves Layer 1 → Layer 2 transition without structural changes.

**Gap 3: Adaptive depth (3 fixed levels → sub-indices).**

RAPTOR generates N levels based on document depth. Our KB has exactly 3 fixed levels. The _index.md comment says "~200 entries" as migration trigger, but this number conflates two different limits:

1. **Token capacity limit (~200 articles):** At ~150 chars/article, 200 articles ≈ 30K chars ≈ 7.5K tokens. This fits in context, so ~200 is not a hard limit but an orientation budget.

2. **(⚠️ speculative extrapolation) Selection accuracy limit:** [[self-improving-agents|ERL]] shows random heuristic inclusion degrades after 40-60 items on Gaia2 agent tasks. We extrapolate this to _index.md selection, but the domain transfer is NOT validated — _index.md entries (~150 chars, homogeneous) differ from ERL heuristics (multi-sentence, with trigger conditions). The actual threshold for _index.md could be higher (200+ if pointers are well-written) or lower (20 if pointers are vague). The number "50-80" gives false precision. The observable signal (Layer 1 misses relevant articles) is more reliable than a speculative threshold.

**Observable degradation signal:** /ask should track when Layer 1 selection misses relevant articles (detectable when Layer 2 reading reveals that a non-selected article would have been more relevant, or when the user corrects an answer). A pattern of misses indicates _index.md has exceeded the LLM's reliable selection capacity.

**Improvement (Fase 2):** Group articles into thematic sub-indices: `_index-agents.md`, `_index-retrieval.md`. Each sub-index is a RAPTOR mid-level node. The main _index.md points to sub-indices instead of individual articles. This creates a 2-step selection: first select the right sub-index (from ~5-10 sub-indices), then select articles within it (from ~20-40). Both steps stay well within the ERL-validated selection window. This is "Option A" from the blueprint's _index migration plan, now with theoretical justification from both RAPTOR (mid-level node contribution 23-57%) and ERL (selection degrades at 40-60 items).

### Challenging Evidence: Concept-Based May Not Be Optimal (Chunking Benchmarks)

Multiple 2024-2025 benchmarks challenge our assumption that concept-based segmentation is sufficient:

- **NVIDIA study**: page-level chunking won at 0.648 accuracy — preserving author's original structure beats re-segmentation for well-structured documents
- **Chroma research**: up to 9% recall variation across chunking methods — non-trivial
- **Proposition chunking** (atomic facts) outperforms concept-level for factoid queries
- **Optimal strategy depends on query type**: factoid queries need 256-512 tokens, analytical queries need 1024+

Our /ingest uses concept-level articles (~500-1500 words) — potentially suboptimal for factoid /ask queries where finer granularity would help. For synthesis queries, concept-level is likely correct.

No single strategy dominates. The practical implication: our concept-based approach may be leaving retrieval quality on the table for certain query types, but switching to chunk-based would hurt synthesis queries. A hybrid (concept articles + atomic fact index) may be the optimal Fase 2 design.

### What NOT to Import

- **GMM clustering**: We use LLM-guided concept extraction; RAPTOR uses statistical GMM clustering on embeddings. Whether one is "more precise" for knowledge bases is untested — no source compares them. We chose concept extraction for pragmatic reasons (no embedding infrastructure), not because it's proven superior.
- **Embeddings for Layer 1 retrieval**: at ~9 articles, reading _index.md whole is more efficient than any embedding pipeline. At ~200 articles, [[hybrid-search|QMD]] solves this better than DIY embeddings.

## Níveis epistêmicos

### Descrição (verificado nas fontes)
- RAPTOR: 0.28 compression, 23-57% non-leaf contribution, 4% hallucination (RAPTOR paper)
- RAPTOR 38.5% vs chunk-based 20-22% (from LC vs RAG paper, NOT RAPTOR's own benchmarks)
- NVIDIA: page-level chunking won at 0.648 accuracy (chunking benchmarks)
- 9% recall variation across chunking methods (Chroma research)
- ERL: random selection degrades at 40-60 items (ERL paper, on Gaia2 agent tasks)

### Interpretação (inferido, não declarado pelos autores)
- "_index.md is a RAPTOR root node" — structural analogy, not validated
- "Layer 1→2→3 escalation ≈ collapsed tree" — structurally different (sequential vs simultaneous), analogy only
- "Concept-based > chunk-based" — RAPTOR uses summarization, not concept extraction. Different mechanisms.

### Especulação (proposto pela KB, sem evidência empírica)
- Sub-indices as RAPTOR mid-level nodes — proposed architecture, untested
- "50-80 articles" as real degradation threshold — extrapolated from ERL's agent task benchmark, NOT validated for wiki _index.md selection
- "Two-step selection stays within ERL-validated window" — combining ERL + RAPTOR to justify sub-indices is novel reasoning without empirical backing
- "QMD solves this better than DIY embeddings at ~200 articles" — unsupported claim

### Gaps não resolvidos
- No direct comparison of concept-based vs chunk-based vs surprise-based segmentation for KB retrieval
- The 50-80 article threshold is theoretically derived, not empirically observed

## Conexões

- [[retrieval-augmented-generation]] — RAPTOR is the top-performing RAG retriever (38.5% vs 20-22% chunk-based)
- [[kb-architecture-patterns]] — validates Pattern 4 (Bandwidth-Aware Retrieval) with academic evidence
- [[context-management]] — the 3-layer escalation pattern originates from Claude Code's compaction hierarchy
- [[hybrid-search]] — QMD is the practical alternative to RAPTOR for Fase 2-3 scaling

## Fontes

- [RAPTOR Paper](../../raw/papers/raptor-recursive-abstractive-retrieval.md) — tree construction, 0.28 compression, 23-57% non-leaf contribution, 4% hallucination rate
- [LC vs RAG Paper](../../raw/papers/long-context-vs-rag-evaluation.md) — RAPTOR 38.5% vs chunk-based 20-22%, confirms summarization-based retrieval superiority
- [Claude Code Internals](../../raw/articles/claude-code-internals-harness-engineering.md) — the 3-layer bandwidth-aware pattern that our /ask implements
- [Chunking Benchmarks](../../raw/papers/chunking-strategies-rag-comparison.md) — (challenging) page-level won NVIDIA benchmark, 9% recall variation, proposition chunking beats concept for factoid queries
