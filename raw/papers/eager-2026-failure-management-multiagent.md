# EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation

**arXiv:** 2603.21522  
**Authors:** Lingzhe Zhang, Tong Jia, Mingyu Wang, Weijie Hong, Chiming Duan, Minghua He, Rongqian Wang, Xi Peng, Meiling Wang, Gong Zhang, Renhai Chen, Ying Li (Peking University + Huawei)  
**Published:** 2026-03-23  
**Categories:** cs.SE

## Abstract

LLM-based Multi-Agent Systems (MASs) are increasingly complex and autonomous, making failure management critical. Existing approaches rely on per-trace reasoning (slow) and neglect historical failure patterns (inaccurate). EAGER addresses both: it uses unsupervised reasoning-scoped contrastive learning to encode intra-agent reasoning + inter-agent coordination, enabling real-time step-wise failure detection, diagnosis, and reflexive mitigation guided by historical failure knowledge.

## Key Empirical Finding: Failure Concentration in Fixed MAS

Failures within a specific/fixed MAS are **limited and recurring** rather than arbitrary — enabling historical pattern reuse.

### Failure Type Distribution Across 3 MAS

| Failure Type | AutoGen-Code | RCLAgent | SWE-Agent |
|---|---|---|---|
| Decomposition Error | 34.48% | 0% | 0% |
| Incorrect Code | 48.28% | 0% | 46.15% |
| Round Limitation | 17.24% | 5.26% | 0% |
| Critical Trace Miss | 0% | 52.63% | 0% |
| Metrics Query Error | 0% | 42.11% | 0% |
| Editing Error | 0% | 0% | 25.64% |
| Localization Error | 0% | 0% | 28.21% |

**Insight:** Each MAS has a completely distinct failure fingerprint. AutoGen-Code fails at code generation; SWE-Agent fails at file editing and localization; RCLAgent fails at information extraction.

### Standard Embeddings Fail for Reasoning Traces

Standard embedding models cannot retrieve semantically similar reasoning traces:

| Model | Recall@10 | NDCG@10 | MRR@10 |
|---|---|---|---|
| Qwen3-0.6B-Embedding | 13.3% | 8.7% | 6.2% |
| BGE-M3-Embedding | 22.2% | 14.5% | 10.8% |

Both models fail — reasoning traces require specialized representation, not general NLP embeddings.

## EAGER Framework

### Components

**1. Failure Knowledge Base**
- *Fine-grained knowledge*: specific reasoning errors at agent level (where hallucinations/inconsistencies occur)
- *Coarse-grained knowledge*: entire trace deemed erroneous without pinpointing specific agent

**2. Step-Wise Detection**
- After each agent completes reasoning: compare embedding to fine-grained knowledge
- After all agents complete: compare full trace embedding to coarse-grained knowledge
- Triggers reflexive mitigation if similarity detected

**3. Reflexive Mitigation**
- *Model-centric reflection*: when specific agent failure identified — refine that agent's reasoning
- *Orchestration-centric reflection*: when full trace deemed faulty — re-evaluate inter-agent coordination globally

**4. Expert Inspect + Agent RCA** (post-failure)
- Triggered when user reports final output incorrect
- Updates both fine-grained and coarse-grained failure knowledge for future detection

### Reasoning-Scoped Contrastive Learning

Training loss = λ₁·L_intra + λ₂·L_inter + λ₃·L_rank

- **L_intra**: intra-scope contrastive — proximity between same agent's reasoning on similar questions
- **L_inter**: inter-scope contrastive — alignment across agents to preserve coordination semantics
- **L_rank**: prefix-to-full ranking — consistency between partial and complete traces

Training data: unsupervised (no failure labels) — constructed via question variation.

## Results

### Anomaly Detection and Failure Diagnosis (F1-Score)

| Task | AutoGen-Code | RCLAgent | SWE-Agent |
|---|---|---|---|
| Anomaly Detection | 73.57% | 86.18% | 79.95% |
| Failure Diagnosis | 63.23% | 78.76% | 69.51% |
| Detection Latency | 5.23s | 4.57s | 4.91s |

### Task Performance Improvement (RCLAgent + EAGER)

| Metric | R@1 | R@3 | R@5 | R@10 | MRR |
|---|---|---|---|---|---|
| RCLAgent | 28.47% | 62.37% | 64.41% | 68.14% | 46.13% |
| RCLAgent + EAGER | 30.19% | 65.82% | 68.56% | 70.03% | 48.65% |

## Key Implications

1. **Failure type is MAS-specific, not universal** — generic failure handling is suboptimal; route by system type first
2. **Historical failure patterns are reusable** — KNN retrieval over past traces outperforms LLM re-reasoning each time
3. **Step-wise detection is faster** — avoids analyzing full trace; can catch failures mid-execution
4. **Reflexive mitigation reduces retry cost** — self-reflection before reset; matches Reflexion pattern
5. **General embeddings insufficient** — purpose-built reasoning-trace encoder required for effective retrieval

## Relations to KB

- Confirms [[self-improving-agents]] Reflexion pattern: reflexive mitigation = verbal reflection before retry
- Confirms [[llm-as-judge]] instability on hard tasks: "LLMs are inherently unstable — same failure may be analyzed correctly sometimes and incorrectly sometimes"
- Extends [[multi-agent-orchestration]]: introduces step-wise detection as operational pattern for MAS reliability

## Fontes
- [EAGER arXiv 2603.21522](../../raw/papers/eager-2026-failure-management-multiagent.md) — paper completo
