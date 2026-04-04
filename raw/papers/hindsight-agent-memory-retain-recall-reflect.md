---
source: https://arxiv.org/abs/2512.12818
authors: Chris Latimer, Nicoló Boschi, Andrew Neeser, Chris Bartholomew, Gaurav Srivastava, Xuan Wang, Naren Ramakrishnan
date: 2025-12-14
type: paper
arxiv: "2512.12818"
stance: challenging
---

# Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects

## Abstract

Memory framework with 4 logical networks (world facts, experiences, entity summaries, beliefs) and 3 operations (retain, recall, reflect). Temporal and entity-aware processing. With 20B open-source model: 83.6% on LongMemEval vs 39% baseline. Larger variants reach 91.4%, matching GPT-4o full-context.

## 4 Logical Networks (Epistemic Separation)

| Network | What it stores | Epistemic status |
|---------|---------------|-----------------|
| World (𝒲) | Objective facts about environment | Facts |
| Experience (ℬ) | Agent's own activities (first person) | Biographical |
| Opinion (𝒪) | Subjective judgments with confidence c∈[0,1] + timestamps | Beliefs (evolving) |
| Observation (𝒮) | Preference-neutral entity summaries from multiple facts | Synthesis |

Key design: **epistemic clarity** — developers can distinguish what agent knows vs believes.

## 3 Core Operations

### Retain
- Extracts narrative facts with temporal ranges (τₛ, τₑ)
- Entity resolution + linking
- 4 graph link types: temporal, semantic, entity, causal
- Updates opinions via reinforcement when new evidence arrives

### Recall (multi-strategy retrieval)
- Semantic: vector similarity (cosine)
- Keyword: BM25
- Graph: spreading activation across entity/causal links
- Temporal: date-range matching with decay-weighted proximity
- Combined via RRF, reranked with cross-encoder, filtered to token budget

### Reflect
- Loads behavioral profile: Skepticism, Literalism, Empathy (1-5 scale) + bias strength (0-1)
- Generates responses shaped by disposition parameters
- Forms and reinforces opinions with confidence tracking

## Results

### LongMemEval
| System | Model | Overall |
|--------|-------|---------|
| Full-context | OSS-20B | 39.0% |
| Zep | GPT-4o | 71.2% |
| **Hindsight** | **OSS-20B** | **83.6%** |
| **Hindsight** | **OSS-120B** | **89.0%** |
| **Hindsight** | **Gemini-3** | **91.4%** |

+44.6% over full-context baseline with same 20B model.

### LoCoMo
| System | Accuracy |
|--------|----------|
| Mem0 | 75.78% |
| Zep | ~77% |
| **Hindsight (20B)** | **85.67%** |
| **Hindsight (120B)** | **89.61%** |

## Direct Challenge to RWKG

Hindsight's 4-network architecture with epistemic separation is MORE structured than our proposed Reflexion-Weighted KG. Critically:
- **Opinion Network** with confidence scores that update via reinforcement = what RWKG proposes (edge weights modified by experience) but actually implemented
- **Causal links** in the graph = the "Bridge Nodes" concept from Synapse, but with explicit causal typing
- "Structured memory organization matters more than raw model capacity" — validates our architectural approach but with a more sophisticated implementation than RWKG proposes

The key difference: Hindsight separates facts from beliefs STRUCTURALLY (4 networks), not via inline markers (our ⚠️ convention). Their approach is stronger.
