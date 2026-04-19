# S1-05 — Prompt 33 Plan Structural Gate (MVP)

## Context
Reject lemon plans before execution with deterministic structural checks.

## Scope
- Add pre-exec symbolic checks:
  - AC ownership exactly once,
  - circular exit-condition detection,
  - bounded `allowed_files`,
  - dependency/order constraints.
- Produce actionable failure messages.

## Out of Scope
- Planner reputation system.
- LLM-based plan scoring.

## DoD
- Gate runs before first stage execution.
- Clear failure reasons in artifacts/timeline.
- Tests for each structural rule and false-positive controls.

## Primary Metrics
- `revise_after_stage1`

## Dependencies
- None

## Estimate
- 2.5d

