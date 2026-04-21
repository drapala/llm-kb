# An Empirical Study on Failures in Automated Issue Solving

**arXiv:** 2509.13941  
**Authors:** Simiao Liu, Fang Liu, Liehao Li, Xin Tan, Yinghao Zhu, Xiaoli Lian, Li Zhang (Beihang University)  
**Published:** 2025-09-17  
**Categories:** cs.SE, cs.AI, cs.CL

## Abstract

Automated issue solving seeks to autonomously identify and repair defective code snippets across an entire codebase. SWE-Bench has emerged as the most widely adopted benchmark. While LLM-based agentic tools show great promise, they still fail on a substantial portion of tasks. Current evaluations primarily report aggregate issue-solving rates, obscuring causes of success and failure.

To bridge this gap, we analyze three SOTA tools (pipeline-based and agentic architectures) on SWE-Bench-Verified. We conducted systematic manual analysis of 150 failed instances, developing a comprehensive taxonomy of failure modes: **3 primary phases, 9 main categories, 25 fine-grained subcategories**.

We then propose a collaborative Expert-Executor framework: a supervisory Expert agent provides strategic oversight and course-correction for a primary Executor agent. This architecture corrects flawed reasoning and breaks cognitive deadlocks. Experiments show our framework **solves 22.2% of previously intractable issues**.

## Failure Taxonomy

### 3 Primary Phases

**Phase 1 — Issue Understanding**
- Misidentifying root cause
- Incomplete reproduction of reported behavior
- Incorrect scope inference

**Phase 2 — Solution Planning**
- Flawed reasoning about fix strategy
- Cognitive deadlock (agent loops without progress)
- Scope underestimation (fix too narrow)

**Phase 3 — Implementation**
- Incorrect code change (variable type errors, logic errors)
- Editing errors (wrong file, wrong location)
- Localization errors (incorrect blame attribution)

### Key Finding: Distinct Failure Fingerprints by Architecture

Pipeline-based vs. agentic architectures show **different failure distributions**:
- Pipeline: more Phase 1 failures (issue understanding)
- Agentic: more Phase 2 failures (flawed reasoning, cognitive deadlocks)

"The majority of agentic failures stem from flawed reasoning and cognitive deadlocks."

### Failure Distribution (SOTA tools on SWE-Bench-Verified)

The 25 subcategories allow precise routing:
- **Cognitive deadlock** → needs external interruption + new strategy (not retry)
- **Type errors** → static analysis can pre-detect (PAGENT approach)
- **Scope underestimation** → plan expansion required before retry
- **Localization error** → retrieval augmentation needed, not code fix retry

## Expert-Executor Framework

Two-agent collaborative design:
- **Expert agent**: text-only, no code execution. Analyzes issue, dispatches tasks, reviews implementations, provides strategic oversight
- **Executor agent**: full repo access, executes code changes

Key insight: "The directing relationship requires a genuine capability gap — structure without substance is pure overhead."

Results: **+22.2% resolution rate on previously intractable issues** (issues no single agent solved across 7 top tools).

## Key Numbers

- 150 failed instances analyzed manually
- 769 failed patches from 7 top LLM code agents (PAGENT companion study)
- 3 SOTA tools: spanning pipeline + agentic architectures
- 22.2% of "intractable" issues resolved by Expert-Executor

## Implications for Agentic Pipelines

1. **Failure classification before retry is necessary** — different failure types need different recovery strategies
2. **Cognitive deadlock** is the dominant agentic failure — requires state reset + new framing, not simple retry
3. **Expert-Executor separation** works when Expert is genuinely stronger at reasoning than Executor
4. **Phase-aware routing**: Phase 1 failure → re-read issue. Phase 2 failure → new plan. Phase 3 failure → targeted fix.
