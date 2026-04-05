# Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead

**Authors:** Zhongming Yu, Naicheng Yu, Hejia Zhang, Wentao Ni, Mingrui Yin, Jiaying Yang, Yujie Zhao, Jishen Zhao  
**arXiv:** 2603.10062  
**Submitted:** March 9, 2026; revised March 30, 2026  
**Type:** Position paper (no empirical experiments)

---

## Abstract

Reframes multi-agent memory management as a computer architecture challenge. Proposes a three-layer memory hierarchy (I/O, cache, memory) and identifies two critical protocol gaps: cache coordination among agents and access management for organized memory. Argues that multi-agent memory consistency is the most significant unresolved problem in the field — and has not been formally defined.

---

## Three-Layer Memory Hierarchy

Mirrors computer architecture hierarchy:

| Layer | Contents | Analogy |
|-------|----------|---------|
| I/O | Interfaces that ingest/emit information (audio, text, images, network calls) | Peripheral I/O |
| Cache | Fast, limited-capacity memory for immediate reasoning: compressed context, recent tool calls, short-term latent storage (KV caches, embeddings) | CPU cache |
| Memory | Large-capacity, slower memory optimized for retrieval and persistence: full dialogue history, vector DBs, graph DBs, document stores | RAM/disk |

Key framing: "performance is an end-to-end data movement problem — relevant information stuck in the wrong tier degrades reasoning accuracy."

---

## Shared vs. Distributed Memory Paradigms

**Shared Memory:** All agents access a unified pool (vector stores, document DBs).
- Advantage: knowledge reuse
- Drawback: requires coherence support; without coordination, agents overwrite, read stale data, or depend on inconsistent versions

**Distributed Memory:** Agents maintain local memory with selective synchronization.
- Advantage: isolation and scalability
- Drawback: requires explicit synchronization; state divergence without careful management

**Observed reality:** Most systems occupy "a middle ground: local working memory with selectively shared artifacts."

---

## Two Critical Protocol Gaps

### Gap 1: Cache Sharing Protocol

Recent work explores KV cache sharing between LLMs (Liu et al. DroidSpeak; Fu et al. Cache-to-cache; Ye et al. KVComm) but lacks "a principled protocol for sharing cached artifacts across agents." Goal: enable one agent's cached results to be transformed and reused by another — analogous to multiprocessor cache transfers.

### Gap 2: Memory Access Protocol

Existing frameworks (MemGPT, A-mem, Mem0, MemorAG) propose memory maintenance strategies but "standard access protocol (permissions, scope, granularity) remains under-specified."

Unresolved questions:
- Read/write permissions per agent
- Access units: document, chunk, record, or trace segment?
- Scope boundaries across agents

---

## Memory Consistency — The Central Problem

In hardware: memory consistency models specify the order in which operations from one processor become visible to others.

### Single-Agent Consistency

Updates must propagate causally across working, episodic, and semantic stores. Prior work acknowledges "need for temporally coherent retrieval" but doesn't formalize ordering guarantees.

### Multi-Agent Consistency

Decomposes into two requirements:

1. **Update-time visibility and ordering:** When agent writes become observable to others and in what order concurrent writes are observed — "directly analogous to the ordering contracts of hardware consistency models."

2. **Read-time conflict resolution:** How agents reconcile conflicting or stale artifacts from concurrent revisions.

Why harder than hardware:
- Memory artifacts are semantically heterogeneous (evidence, tool traces, plans)
- Inter-agent dependencies are implicit rather than declared
- Conflicts are often semantic and coupled to environment state

**Critical finding:** "Multi-agent memory consistency has not been formally defined, and no framework exists to detect or classify consistency violations in practice."

---

## Context Complexity Drivers (Motivation)

Four forces justify the architectural framing:

1. **Long-context reasoning** — RULER benchmarks: multi-hop tracing over simple retrieval
2. **Multimodality** — MMMU, VideoMME: joint reasoning across modalities
3. **Structured data** — Spider, BIRD: agents operate on executable traces
4. **Environment state** — SWE-bench, OSWorld: long-horizon state tracking

Conclusion: "Context is no longer a static prompt; it is a dynamic memory system with bandwidth, caching, and coherence constraints."

---

## Recommendations (Position Paper)

- Build explicit hierarchies rather than monolithic "one memory" designs
- Develop cache-sharing protocols analogous to hardware multiprocessor standards
- Formalize access control: permissions, scope, granularity
- Define consistency models for multi-agent scenarios with formal verification
- Move from ad-hoc to principled protocols

---

## Key Citations

- Sorin et al. — memory consistency models (hardware precedent)
- MemGPT, A-mem, Mem0, MemorAG — existing agent memory frameworks
- Liu/Fu/Ye et al. — KV cache sharing across LLMs
- MetaGPT, AutoGen, LangGraph — multi-agent systems
- RULER, MMMU, VideoMME, Spider, BIRD, SWE-bench, OSWorld — benchmarks
