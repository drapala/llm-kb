# S2-04 — Prompt 20 Provenance + Config Invalidation

## Context
Self-mod safety requires traceable fixture provenance and invalidation when runtime config shifts.

## Scope
- Track fixture provenance (human vs self-generated).
- Add invalidation trigger on critical config changes (model/embedding/version).
- Require canary re-run on invalidation events.

## Out of Scope
- Full longitudinal canary redesign.

## DoD
- Provenance recorded in self-mod artifacts.
- Invalidation events trigger mandatory revalidation path.
- Tests cover invalidation trigger matrix.

## Primary Metrics
- `regressions_after_promote`

## Dependencies
- S1-04

## Estimate
- 2d

