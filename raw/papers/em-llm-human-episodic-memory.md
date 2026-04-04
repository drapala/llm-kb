---
source: https://arxiv.org/abs/2407.09450
authors: Zafeirios Fountas, Martin A Benfeghoul, Adnan Oomerjee, Fenia Christopoulou, Gerasimos Lampouras, Haitham Bou-Ammar, Jun Wang
date: 2024-07-12
type: paper
arxiv: "2407.09450"
---

# EM-LLM: Human-Inspired Episodic Memory for Infinite Context LLMs

## Abstract

Applies human episodic memory principles to LLMs. Uses Bayesian surprise and graph-theoretic boundary refinement to segment token sequences into coherent events. Retrieval via similarity + temporal contiguity. Handles 10M tokens. Strong correlations between EM-LLM's event segmentation and human-perceived events on LongBench and Infinity-Bench.

## Core Neuroscience Principles Applied

### 1. Bayesian Surprise for Event Boundaries
Prediction error exceeding threshold marks segment boundaries: `-log P(xt|x1,...,xt-1;θ) > T`. Mirrors how human brains mark narrative shifts. T adapts via moving window of surprise statistics.

### 2. Event Segmentation Theory
Continuous experience organized into discrete episodic events with boundaries, not uniform chunks. Reflects human perception of time as bounded episodes.

### 3. Temporal Contiguity Effects
Retrieval implements human free-recall patterns: nearby items in time accessed together. Forward-directed retrieval dominates (asymmetry effect).

## Architecture (3 Components)

- **Local Context** (recent tokens): full softmax attention = working memory
- **Initial Tokens** (128 fixed): attention sinks for stability
- **Evicted Tokens** (bulk): managed via episodic memory with surprise-based segmentation

### Memory Formation
1. Initial boundaries via surprise thresholding
2. Graph-theoretic refinement: optimize intra-event similarity + inter-event separation (modularity/conductance)
3. Complexity: O(kn) where k << n

### Retrieval (2-stage)
- Similarity buffer: k-NN on event representatives
- Contiguity buffer: queue of temporal neighbors of retrieved events

## Human Perception Validation

Analysis on human-annotated podcast transcripts:
- Surprise-based segmentation achieves results "very similar to humans"
- Refinement significantly improves alignment
- Surprise methods identified boundaries closest to human consensus
- Refined methods: 25-35x improvement in intra/inter-similarity ratio over random

"LLM-perceived surprise can indeed serve as a proxy for cognitive signals that drive human event segmentation."

## Results

- Retrieval tasks: up to 40% improvement over InfLLM
- QA tasks: 29.7% average improvement
- RAG comparison: 30.5% improvement on LongBench
- Handles 10M tokens (computationally infeasible for full-context)

## Key Differences from MemGPT/Standard Approaches

1. **Layer-wise retrieval**: each Transformer layer independently retrieves (not single-stage like RAG)
2. **Dynamic segmentation**: surprise-based boundaries adapt to content (not fixed-size chunks)
3. **No fine-tuning required**: works on pre-trained models
4. **Temporal dynamics**: contiguity buffers model human memory biases (standard retrieval = similarity only)

## Relevance to KB

Creates direct tension with our engineering approach to memory segmentation. Our /ingest chunks by "concept" (LLM judgment). EM-LLM chunks by "surprise" (statistical signal aligned with human perception). Question: should /ingest segment sources at points of maximum surprise rather than by concept boundaries? Surprise-based segmentation is validated against human cognition; concept-based segmentation is not.
