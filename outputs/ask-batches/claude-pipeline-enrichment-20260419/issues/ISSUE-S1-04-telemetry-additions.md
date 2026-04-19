# S1-04 — Prompt 06 Telemetry Additions

## Context
Need metrics to validate cost/quality hypotheses and policy decisions.

## Scope
- Emit and persist:
  - `marginal_oracle_lift`
  - `llm_call_ratio`
  - related summary fields used in sprint evaluation.
- Add parser/summary regression tests.

## Out of Scope
- OTel exporter integration.
- Dashboard UI.

## DoD
- Metrics available in eval summary artifacts.
- Backward-compatible output format.
- Tests cover parser + aggregation paths.

## Primary Metrics
- `marginal_oracle_lift`
- `llm_call_ratio`

## Dependencies
- S1-01, S1-02, S1-03

## Estimate
- 1d

