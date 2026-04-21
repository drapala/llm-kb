# AMBIG-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering

**arXiv:** 2502.13069  
**Authors:** Sanidhya Vijayvargiya, Xuhui Zhou, Akhila Yerukola, Maarten Sap, Graham Neubig (Carnegie Mellon University)  
**Published:** 2025-02 (accepted ICLR 2026)  
**Categories:** cs.AI, cs.SE, cs.CL

## Abstract

AI agents are increasingly deployed to automate tasks based on underspecified user instructions. Making unwarranted assumptions about missing information, and failing to ask clarifying questions, leads to suboptimal outcomes, safety risks from tool misuse, and wasted computational resources.

This paper studies LLM agents' ability to handle underspecified instructions in interactive code generation. Evaluates proprietary and open-weight models across three steps: (a) detecting underspecificity, (b) asking targeted clarification questions, (c) leveraging interaction to improve performance.

**AMBIG-SWE:** an underspecified variant of SWE-Bench Verified designed to evaluate agent behavior under ambiguity and interaction.

## Key Findings

### Detection failure
Models **struggle to distinguish between well-specified and underspecified instructions**.  
- Claude Sonnet 4 achieves 89% accuracy in distinguishing underspecified vs. well-specified
- Claude Sonnet 3.5 achieves 84%
- Most other models perform significantly worse

### Interactivity boost
When models interact for underspecified inputs, they obtain vital missing information:  
**+74% over non-interactive settings** (when model actually asks questions vs. assumes)

### Non-interactive default
LLMs default to non-interactive behavior without explicit encouragement.  
Even with encouragement, models struggle to consistently detect when interaction is needed.

### Cascading failure
Underspecification in complex agentic tasks can involve multiple interdependent gaps that arise dynamically. Agents may take many steps before recognizing missing information — by which point the trajectory is already compromised.

## Experimental Design

- Base: SWE-Bench Verified (real GitHub issues)
- AMBIG-SWE: information systematically removed from original issues
- Agent scaffold: OpenHands with Claude Sonnet 4.5
- Three evaluation conditions: fully specified (baseline), underspecified + no interaction, underspecified + interaction enabled

## Implications

1. **Pre-execution validation is empirically valuable:** the +74% result is measured on real SWE tasks — not synthetic benchmarks
2. **Detection is the hard problem:** generating questions given ambiguity is easier than detecting ambiguity exists
3. **Pipeline design implication:** a validation gate before planning that detects underspecificity and triggers clarification prevents compounded downstream failures
4. **Automation tension:** fully autonomous pipelines that suppress interaction sacrifice performance on ambiguous tickets

## Relation to KB

- DIRECTLY SUPPORTS gap "ticket-pre-validation-agentic-planning" — empirical evidence that detection + clarification before execution yields large performance gains
- REFINES agentic-coding-failure-taxonomy: Phase 1 (Understanding) failures have a measurable fix (interactive clarification before planning)
- REFINES uncertainty-aware-workflow-denoising: ambiguity detection → clarification is one instantiation of the Sensing→Regulating→Correcting loop at the ticket-input level
