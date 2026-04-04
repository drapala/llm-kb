---
source: https://arxiv.org/abs/2501.13956
authors: Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais, Jack Ryan, Daniel Chalef
date: 2025-01-20
type: paper
arxiv: "2501.13956"
stance: challenging
---

# Zep: A Temporal Knowledge Graph Architecture for Agent Memory

## Abstract

Memory service for AI agents using Graphiti, a temporally-aware knowledge graph engine. Synthesizes unstructured conversational + structured business data while maintaining historical relationships. 94.8% on DMR (vs MemGPT 93.4%). Up to 18.5% accuracy improvement on LongMemEval with 90% latency reduction.

## Graphiti Architecture: 3 Hierarchical Subgraphs

1. **Episode Subgraph (𝒢ₑ)**: Raw input as messages/text/JSON — non-lossy data store
2. **Semantic Entity Subgraph (𝒢ₛ)**: Entities extracted + resolved; edges = relationships
3. **Community Subgraph (𝒢c)**: Clusters of strongly connected entities with high-level summaries

## Bi-Temporal Modeling (Key Innovation)

Each fact tracks 4 timestamps:

| Timestamp | Purpose |
|-----------|---------|
| t'_created | When system ingested the fact |
| t'_expired | When system marked fact obsolete |
| t_valid | When fact was actually true |
| t_invalid | When fact stopped being true |

**Edge Invalidation:** When new info contradicts old fact, system invalidates prior edge by setting t_invalid = new edge's t_valid. Complete history preserved.

This is MORE sophisticated than RWKG's proposed "edge weight modification" — Zep doesn't change weights, it maintains temporal validity ranges. Old facts aren't forgotten or downweighted; they're marked as no longer valid WITH the timeline of when they were valid.

## Retrieval

3 components:
- **Search (φ)**: cosine semantic + BM25 full-text + BFS n-hop neighbors
- **Reranking (ρ)**: RRF + MMR + episode-mention frequency + cross-encoder
- **Constructor (χ)**: formats nodes/edges into context with temporal info

## Results

### DMR Benchmark
| System | Accuracy |
|--------|----------|
| MemGPT (gpt-4-turbo) | 93.4% |
| **Zep (gpt-4-turbo)** | **94.8%** |
| **Zep (gpt-4o-mini)** | **98.2%** |

### LongMemEval
| System | Model | Accuracy | Latency | Context |
|--------|-------|----------|---------|---------|
| Full-context | gpt-4o | 60.2% | 28.9s | 115k tokens |
| **Zep** | **gpt-4o** | **71.2%** | **2.58s** | **1.6k tokens** |

+18.5% accuracy, 90% latency reduction, 99% context reduction.

### By Question Type
- Temporal reasoning: +38-48%
- Multi-session: +17-31%
- Single-session preference: +78-184%
- Knowledge update: mixed (-3% to +7%)
- Single-session assistant: negative (-9% to -18%)

## Direct Challenge to RWKG

Zep/Graphiti already implements much of what RWKG proposes:
- **Temporal knowledge graph** with edge invalidation (more principled than "edge weight modification")
- **Hierarchical subgraphs** (episodes → entities → communities) = multi-level abstraction
- **Hybrid retrieval** (semantic + BM25 + graph traversal) = what QMD and Synapse do

Key difference from RWKG: Zep handles contradictions via temporal invalidation (marking old edges as expired), not via weight reduction. This preserves history — you can query "what did the agent believe at time T?" RWKG's weight modification would lose that information.
