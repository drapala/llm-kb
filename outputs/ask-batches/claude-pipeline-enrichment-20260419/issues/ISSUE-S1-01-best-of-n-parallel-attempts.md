# S1-01 — Prompt 07 Best-of-N (`parallel_attempts=3`)

## Context
Improve stage outcome quality via parallel candidate attempts with deterministic selection.

## Scope
- Add feature-flagged `parallel_attempts` path (default off).
- Run `N=3` candidate attempts in isolated worktrees.
- Add selector strategy (initial: critic/oracle verdict, then test evidence tie-break).
- Add tests for selection determinism and failure fallback.

## Out of Scope
- Tree search / MCTS.
- `N>3` tuning beyond baseline experiment.

## DoD
- Feature flag documented and tested.
- Selection logic covered by unit/integration tests.
- No regression in single-attempt path.

## Primary Metrics
- `approve_rate`
- `tokens_total`

## Dependencies
- None

## Estimate
- 1.5d

