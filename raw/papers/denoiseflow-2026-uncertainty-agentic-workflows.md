# DenoiseFlow: Uncertainty-Aware Denoising for Reliable LLM Agentic Workflows

**arXiv:** 2603.00532  
**Authors:** Yandong Yan, Junwei Peng, Shijie Li, Chenxi Li, Yifei Shang, Can Deng, Ruiting Dai, Yongqiang Zhao, Jiaqi Zhu, Yu Huang (Peking University + collaborators)  
**Published:** 2026-02-28  
**Venue:** KDD 2026  
**Categories:** cs.AI

## Abstract

Long-horizon agentic workflows suffer from **accumulated semantic ambiguity**: minor interpretation errors in natural-language instructions compound silently across steps. Existing approaches use static exploration budgets, reactive error recovery, or single-path execution — none adapt at runtime to uncertainty signals. DenoiseFlow formalizes multi-step reasoning as a Noisy MDP and introduces closed-loop progressive denoising through three stages: Sensing (uncertainty estimation), Regulating (adaptive branching), and Correcting (influence-based root-cause localization). Self-calibration requires no ground-truth labels.

## Core Concept: Accumulated Semantic Ambiguity

The central failure mode in long-horizon agentic tasks:
- Minor interpretation errors in natural-language instructions propagate silently
- Each step amplifies prior ambiguity → error cascade
- "Logical soft errors": covert deviations that degrade quality without triggering crashes
- Reactive approaches (Self-Refine, code exceptions) only catch failures post-hoc — too late

## DenoiseFlow Framework (3 Stages)

**Stage 1 — Sensing (Uncertainty Estimation)**
- Monte Carlo sampling (N=5, temperature=0.7) to generate diverse interpretations
- Semantic clustering (all-MiniLM-L6-v2, τ_sim=0.85) to estimate ambiguity
- Outputs per-step uncertainty score

**Stage 2 — Regulating (Adaptive Computation)**
- Routes based on estimated risk:
  - Low uncertainty → fast single-path execution
  - High uncertainty → parallel branch exploration (max K=7 branches)
- Online self-calibration adjusts decision boundaries using verifier feedback (no labels needed)

**Stage 3 — Correcting (Targeted Recovery)**
- Influence-based root-cause localization: identifies which step caused the failure
- Targeted refinement (max R=2 retries) at the identified root cause
- Not full retry from scratch — surgical correction

## Results: 6 Benchmarks

All methods use GPT-4o-mini backbone:

| Task | Benchmark | DenoiseFlow | JudgeFlow (2nd) | AFlow |
|---|---|---|---|---|
| Math | GSM8K | best | JudgeFlow +0.9% | — |
| Math | MATH | best | +2.9% over JudgeFlow | +8.6% over AFlow |
| Code | MBPP | 84.9% | best | — |
| Code | HumanEval | 93.9% | best | — |
| QA | HotpotQA | best | — | — |
| QA | DROP | best | — | — |
| **Average** | | **83.3%** | JudgeFlow 82.0% | AFlow 78.1% |

**Cost reduction: 40–56% through adaptive branching** (vs. fixed exploration budget)

## Key Design Principles

1. **Proactive vs. reactive**: Sense uncertainty before execution fails, not after
2. **Adaptive computation allocation**: Spend more on uncertain steps, less on confident ones
3. **Surgical correction**: Root-cause localization enables targeted fix, not full retry
4. **Self-calibration**: No ground-truth labels required — uses verifier feedback (code pass/fail, etc.)

## Ablation Insights

- All 3 stages necessary: removing any stage degrades performance
- Branching most valuable on complex tasks (MATH) where multiple solution paths exist
- Code tasks benefit most from external verifier signal (binary pass/fail is unambiguous)
- Online calibration critical for robustness across domains

## Comparisons in Context

- vs. Reflexion: DenoiseFlow is proactive (sensing before failure); Reflexion is reactive (after failure)
- vs. AFlow/DSPy: Those optimize static graphs offline; DenoiseFlow adapts at runtime
- vs. Self-Refine: Full retry vs. targeted root-cause correction

## Implications for KB

- **Extends [[self-improving-agents]]**: proactive sensing + adaptive branching = improved retry discipline
- **Extends [[autonomous-emergence-pipeline-risks]]**: influence-based root-cause localization addresses compound error cascade
- **Contrasts with [[multi-agent-orchestration]]**: static orchestration vs. closed-loop Noisy MDP regulation
- Adaptive branching as mechanism to balance exploration/exploitation dynamically — connects to rational inattention (⚠️ nossa interpretação)

## Fontes
- [DenoiseFlow arXiv 2603.00532](../../raw/papers/denoiseflow-2026-uncertainty-agentic-workflows.md) — paper completo
