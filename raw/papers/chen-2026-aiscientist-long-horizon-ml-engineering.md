# Chen et al. (2026) — Toward Autonomous Long-Horizon Engineering for ML Research

**arXiv:** 2604.13018  
**Autores:** Guoxin Chen, Jie Chen, Lei Chen, Jiale Zhao, Fanzhe Meng, Wayne Xin Zhao, Ruihua Song, Cheng Chen, Ji-Rong Wen, Kai Jia  
**Data:** 14 Apr 2026  
**Licença:** CC BY 4.0

## Abstract

Autonomous AI research has advanced rapidly, but long-horizon ML research engineering remains difficult: agents must sustain coherent progress across task comprehension, environment setup, implementation, experimentation, and debugging over hours or days.

We introduce AiScientist, a system for autonomous long-horizon engineering for ML research built on a simple principle: **strong long-horizon performance requires both structured orchestration and durable state continuity**.

AiScientist combines hierarchical orchestration with a permission-scoped **File-as-Bus workspace**: a top-level Orchestrator maintains stage-level control through concise summaries and a workspace map, while specialized agents repeatedly re-ground on durable artifacts such as analyses, plans, code, and experimental evidence rather than relying primarily on conversational handoffs, yielding **thin control over thick state**.

## Main Results

**PaperBench** (from-scratch replication of ML papers):
- AiScientist: **33.73** average score (vs human baseline ~41%)
- Best baseline (IterativeAgent, GLM-5): 22.37 → **+11.15 pts**
- Cost: **$12.20/task** vs $54.90 for IterativeAgent

**MLE-Bench Lite** (competition-style ML optimization, Any Medal%):
- AiScientist: **81.82%** under both Gemini-3-Flash and GLM-5
- Strongest matched baseline (LoongFlow): 77.27% → **+4.55 pts**

**MLE-Bench Lite example:** On "Detecting Insults" task, ran 74 experiment cycles over 23 hours without human intervention, raising validation AUC from 0.903 to 0.982 through 18 best-so-far updates.

## File-as-Bus Ablation

Removing File-as-Bus:
- PaperBench: **−6.41 points**
- MLE-Bench Lite: **−31.82 Any Medal%**

The loss is concentrated in later-round refinement (Silver/Gold/Any Medal), not in establishing initial valid submissions. Interpretation: File-as-Bus enables cumulative progress over multi-round loops, not just task setup.

## Design Principles

### 1. Thin Control over Thick State

```
m_t = M(W_t)                  # workspace map = compact index of artifacts
a_t = π₀(c_t, m_t, G; W_t)   # Orchestrator acts on map + summary, not full workspace
```

- **Thin = control interface**: Orchestrator carries stage-level summaries + workspace map
- **Thick = state**: paper analyses, code, logs, experiment records persist as durable files
- Orchestrator can read specific artifacts on demand, but doesn't carry full workspace in context

### 2. File-as-Bus Coordination

Workspace organized into three role-aligned regions:
- `paper_analysis/` — structured paper understanding, target metrics, ambiguities
- `submission/` — runnable reproduction repository (code, config, setup scripts, reproduce.sh)
- `agent/` — planning artifacts: prioritized_task.md, plan.md, impl_log.md, exp_log.md
- `agent/experiments/` — detailed run outputs

**Permission-scoped:** each Tier-1 specialist has write access only to its region. Shared logs are append-only and iteration-structured.

**Key property:** downstream agents re-enter from current workspace state — they do not inherit conversational context from predecessors. Project state is in files, not in chat history.

### 3. Hierarchical Orchestration (Agent-as-Tool)

- Tier-0 Orchestrator: stage-level planning and delegation
- Tier-1 Specialists: Paper Comprehension, Prioritization, Implementation, Experimentation, Generic Helper
- Tier-2 Subagents: leaf workers for focused subtasks; do not recursively spawn

Agent-as-Tool: each specialist is callable as a tool from the Orchestrator's native action space. Delegation is selective — Orchestrator handles lightweight ops directly, invokes specialist only when expected benefit > coordination cost.

Specialist lifecycle per invocation:
```
(s_t, ΔW_t) = π_j(d_t, m_t; W_t)
c_{t+1} = c_t ⊕ s_t        # Orchestrator's context += concise summary
W_{t+1} = U(W_t, ΔW_t)     # Workspace updated with specialist's artifacts
```

Private context of specialist is **re-initialized at each invocation** — continuity is in workspace, not in context.

### 4. Evidence-Driven Research Loop

Pattern: implement → run → diagnose → patch → re-validate

Not a rigid pipeline. Early emphasis on paper comprehension and prioritization. Dominant loop: implementation ↔ experimentation, driven by artifacts in exp_log.md. Failed executions → targeted fixes via impl_log.md.

## Key Takeaways from Paper

1. "More interaction alone is not enough; additional rounds help only when they build on prior progress." (IterativeAgent adds rounds but still lags AiScientist)
2. "Durable state continuity is a key bottleneck in long-horizon ML research engineering."
3. "File-as-Bus matters more for later-round refinement than for establishing a minimally competitive starting point."
4. "Simpler agent organizations are insufficient; hierarchical orchestration appears to contribute materially alongside durable state continuity."

## Relation to Lu et al. (2024) — AI Scientist

Lu et al. (2024) introduced end-to-end scientific discovery (idea → experiment → paper → review) with cost < $15/paper. Chen et al. (2026) focus on a distinct harder setting: from-scratch paper **replication** and **competition-style optimization**, which requires sustained state continuity across multi-round debugging loops — not one-shot ideation.

Lu 2024: single-pass pipeline, timeout as stopping criterion.  
Chen 2026: iterative multi-round loop, durable state as key mechanism.

## Benchmarks

**PaperBench** (Starace et al., 2025): from-scratch replication of top-tier conference papers in Docker environment. Evaluated on code development, successful execution, result matching. Human baseline: 41% in 48 hours. Best prior agent: ~21%.

**MLE-Bench Lite** (Chan et al., 2025): competition-style ML task optimization. Primary metric: Any Medal%.

## Baselines

PaperBench: BasicAgent, IterativeAgent  
MLE-Bench Lite: AIDE, ML-Master 2.0, LoongFlow  
LLM backbones used: Gemini-3-Flash, GLM-5
