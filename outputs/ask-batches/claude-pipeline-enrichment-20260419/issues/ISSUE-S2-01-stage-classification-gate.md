# S2-01 — Prompt 34 Stage Classification Gate

## Context
Route trivial stages to deterministic checks to reduce LLM dependence.

## Scope
- Add stage classifier: `trivial | medium | complex`.
- Route `trivial` stages through tool-first path.
- Add override controls and audit trail.

## Out of Scope
- Full determinism-first refactor across all modules.

## DoD
- Classification decision visible in logs/artifacts.
- Trivial route works end-to-end with fallback safety.
- Tests for classification + routing.

## Primary Metrics
- `llm_call_ratio`

## Dependencies
- S1-04

## Estimate
- 2d

