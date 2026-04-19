# S1-03 — Prompt 12 Symbolic-First Reorder

## Context
Gate 12 should be tool-first: symbolic checks first, LLM reviewer only for inconclusive cases.

## Scope
- Reorder flow to `symbolic -> optional neural -> symbolic decision`.
- Add structured reviewer output: `{verdict, rule, quote}`.
- Add observe-mode counters for call-rate and block reasons.

## Out of Scope
- New injection detectors outside current gate scope.

## DoD
- LLM reviewer not called for clear symbolic pass/fail.
- Structured payload persisted for auditability.
- Regression tests for all decision branches.

## Primary Metrics
- `llm_reviewer_call_rate`

## Dependencies
- None

## Estimate
- 1d

