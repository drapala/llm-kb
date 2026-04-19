# S2-02 — Prompt 15 Compaction Hierarchy + Adaptive Budget

## Context
Prevent context-loss failures under long runs while keeping token usage controlled.

## Scope
- Implement 12-level preservation hierarchy.
- Add adaptive budget deltas based on uncertainty signals.
- Add pre-commit reflexion hook and tests.

## Out of Scope
- Full C_LLM measurement study.

## DoD
- Hierarchy rules encoded and tested.
- Adaptive budget behavior deterministic under fixed inputs.
- Context-loss regressions reduced in fixture runs.

## Primary Metrics
- `replan_due_to_context_loss`

## Dependencies
- S1-04

## Estimate
- 3d

