# Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents

**arXiv:** 2603.26233  
**Authors:** Nicholas Edwards, Sebastian Schuster (University of Vienna)  
**Published:** 2026-03-27  
**Categories:** cs.CL, cs.SE

## Abstract

LLM agents deployed in open-ended domains like software engineering frequently encounter underspecified instructions that lack crucial context. While human developers naturally resolve underspecification by asking clarifying questions, current agents are largely optimized for autonomous execution.

This paper systematically evaluates clarification-seeking abilities on an underspecified variant of SWE-bench Verified. Proposes an uncertainty-aware multi-agent scaffold that explicitly **decouples underspecification detection from code execution**.

## Key Results

**Multi-agent scaffold (OpenHands + Claude Sonnet 4.5):**  
- Task resolve rate: **69.40%** (underspecified input, with clarification)
- vs. single-agent baseline: **61.20%** (underspecified, no clarification)
- vs. fully specified baseline: ~71% (theoretical upper bound)

**Calibrated uncertainty:**
- The multi-agent system conserves queries on simple tasks
- Proactively seeks information on complex tasks
- Avoids the failure mode of asking unnecessary questions on unambiguous tickets

## Architecture: Decoupled Detection + Execution

The key design insight: **separation of underspecification detection from code execution** into distinct agents with distinct objectives.

```
[Ticket] → [Underspecification Detector] → (ambiguous?) → [Clarification Agent] → [Execution Agent]
                                          → (clear?) ─────────────────────────→ [Execution Agent]
```

- Detection agent: focused solely on "is this underspecified?" — does not execute code
- Clarification agent: generates targeted questions when detection triggers
- Execution agent: runs with full context after clarification

This separation prevents the execution agent from making unwarranted assumptions mid-trajectory.

## Finding: Detection is harder than asking

Once the agent correctly identifies underspecification, asking useful questions is relatively tractable. The bottleneck is **detection** — knowing that you don't know enough.

Uncertainty-aware scaffolding (explicit calibration on when to ask) significantly improves detection compared to prompting a single agent to "ask if unsure."

## Relation to KB

- PRIMARY source for "ticket-pre-validation-agentic-planning" concept
- Architectural pattern: decoupled detection + clarification as pre-planning gate
- EXTENDS AMBIG-SWE (vijayvargiya-2026): both confirm +7-8pp from clarification; this paper adds architectural prescription (separate agents)
- REFINES agentic-coding-failure-taxonomy: Phase 1 (Understanding) failure prevention via architectural separation
- VALIDATES uncertainty-aware-workflow-denoising: explicit uncertainty measurement before execution reduces downstream failures (DenoiseFlow shows same at plan level; this paper shows it at ticket-input level)
