---
title: "Weak Supervisor Analysis: Quality Gate vs Compiler"
date: 2026-04-04
query: "O compilador é mais forte que raw/? O quality gate é weak supervisor de strong model?"
confidence: alta (dimensão analysis), baixa (weak-to-strong L0)
---

# Weak Supervisor Analysis

## The Compiler Is Not Stronger OR Weaker — It Has Different Variety

| Dimension | Compiler (Claude Opus 4.6) | raw/ sources |
|-----------|---------------------------|-------------|
| Breadth | Enormous (trained on internet) | Narrow (64 sources, ~5 domains) |
| Depth per domain | Shallow-to-medium | Deep (specialist per topic) |
| Reasoning/synthesis | Strong | Zero (static text) |
| Factual specificity | Weak (hallucinations documented) | Strong (paper says what it says) |
| Self-assessment | Near random on hard tasks | N/A |

Not "strong vs weak." Different varieties (Ashby).

## What's Actually Happening: Gate Compliance ≠ Quality

The Quality Gate (4 checks) has V(gate) << V(compiler output).

The compiler satisfies the 4 checks AND is UNCONSTRAINED in everything the gate doesn't cover. This is worse than weak-to-strong imitation:
- W2S: student imitates specific teacher errors → localized errors
- Gate compliance: compiler satisfies checks, errors in all unchecked dimensions → distributed errors

**Gate covers:** wikilink typing, number qualification, meta-KB separation, resumo calibration.
**Gate does NOT cover:** argument quality, logical consistency, nuance preservation, style diversity, factual accuracy of non-numeric claims.

**The gap between what the gate checks and what the compiler produces IS where the errors live.**

## Ashby Diagnosis

V(gate) << V(compiler). Most compiler output dimensions pass unregulated. Error floor in unchecked dimensions.

## Fix (Not More Checks)

1. External feedback of DIFFERENT variety (spot-check by different model/human)
2. Gate as FLOOR not CEILING — "passed 4 checks = minimum. Is it EXCELLENT?"
3. Missing check: "Is this article better than what compiler would produce WITHOUT the gate?"
