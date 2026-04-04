---
source: https://arxiv.org/abs/2403.08319
authors: Rongwu Xu, Zehan Qi, Zhijiang Guo, Cunxiang Wang, Hongru Wang, Yue Zhang, Wei Xu
date: 2024-03-13
type: paper
arxiv: "2403.08319"
---

# Knowledge Conflicts for LLMs: A Survey

## Abstract

Examines knowledge conflicts: complex challenges when blending contextual and parametric knowledge. Three conflict types: context-memory, inter-context, and intra-memory. Explores causes, LLM behaviors, and solutions.

## Three Conflict Types

### 1. Context-Memory Conflict
External context contradicts model's parametric knowledge.
- Temporal misalignment: model trained on old data, context has new info
- Misinformation pollution: false info in retrieved documents

### 2. Inter-Context Conflict
Multiple external sources contradict each other within same context.
- Conflicting documents with different claims
- Simultaneous presence of updated and obsolete facts

### 3. Intra-Memory Conflict
Internal inconsistencies within model parameters.
- Training corpus bias from contradictory sources
- Decoding strategy randomness
- Knowledge editing side effects
- Even GPT-4 shows 13% inconsistency rate on paraphrased queries

## LLM Behavior Under Conflict

| Behavior | Finding |
|----------|---------|
| Semantic coherence preference | Models favor logically coherent info |
| Confirmation bias | Strong tendency to favor parametric knowledge |
| Context sensitivity | Prioritization varies by setup |
| Susceptibility to misleading prompts | Even strong models are influenced |

## Solutions by Objective

### Faithful to Context
KAFT, TrueTeacher, Context-aware Decoding (CAD), opinion-based prompts

### Discriminating Misinformation
Vigilant prompting, confidence from answer redundancy, fine-tuned discriminators

### Disentangling Sources
Separate context-based vs memory-based answers, three-step conflict detection

### Improving Factuality
COMBO (compatible passage pairing), DoLa (dynamic layer selection), ITI (truthfulness-correlated attention heads)

## Relevance to KB

This is the academic formalization of our tension-resolution framework. Our 3 conflict types map directly:
- **Context-memory** = wiki article contradicts what the LLM "knows" from training → authority bias risk
- **Inter-context** = two wiki articles contradict each other → our tension detection in /review item 9
- **Intra-memory** = LLM generates inconsistent responses to same question phrased differently → reliability of /ask

The survey's finding that GPT-4 has 13% inconsistency rate on paraphrased queries directly validates our circuit breaker design: don't trust a single /ask answer on important claims.
