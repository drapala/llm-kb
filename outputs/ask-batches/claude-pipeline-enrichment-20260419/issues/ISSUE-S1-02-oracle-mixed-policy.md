# S1-02 — Prompt 02 Oracle Mixed Policy

## Context
Reduce oracle cost while preserving safety by combining deterministic and sampled audits.

## Scope
- Implement `oracle_sampling_policy`:
  - deterministic on red-zone stages,
  - stochastic sampling for non-red-zone stages.
- Default `oracle_models` to multi-family set.
- Add config docs and examples.

## Out of Scope
- PRM training.
- Auto-policy tuning by reinforcement.

## DoD
- Policy config supported end-to-end.
- Red-zone always audited.
- Sampling reproducible with seeded randomness in tests.

## Primary Metrics
- `cost_per_ac`
- `false_approve_rate`

## Dependencies
- None

## Estimate
- 1.5d

