# SUMMARY_EXECUTABLE — Sprint Planning Pack

**Date**: 2026-04-19  
**Source**: synthesis of `01`..`12` + `SUMMARY.md`  
**Goal**: convert insights into executable sprint backlog with measurable outcomes.

---

## 1) Scope for next 2 sprints

This plan executes the highest-ROI subset without committing to high-risk platform bets (multi-tenant/moat) yet.

### Included now (Top ROI)
1. Prompt 07: `parallel_attempts: N` (best-of-N)
2. Prompt 02: `oracle_sampling_policy` + multi-family default
3. Prompt 33: Plan Structural Gate (new)
4. Prompt 34: Stage Classification Gate (new)
5. Prompt 11: continuant/occurrent split for antipattern feedback
6. Prompt 15: compaction hierarchy + adaptive budget + pre-commit reflexion
7. Prompt 12: strict symbolic->neural->symbolic flow
8. Prompt 06: `marginal_oracle_lift`, `llm_call_ratio`, registry health metrics
9. Prompt 20: fixture provenance + config invalidation hooks
10. Prompt 41: ontology alignment spike (not full migration)

### Deferred
- Prompt 32 (inner-agent tree search)
- Prompt 37/38 (multi-tenant moat track)
- Prompt 40 (screening AC menu) until AC gaming baseline is measured

---

## 2) Baseline metrics (must capture before coding)

Run one frozen baseline over current main:
- `approve_rate`
- `cost_per_ac`
- `false_approve_rate`
- `llm_call_ratio`
- `review_reopen_rate`
- `replan_due_to_context_loss`

Store in: `eval_results/<run-id>/summary.md` and copy key values into sprint notes.

---

## 3) Sprint backlog

## Sprint 1 (safety + cost controls)

| ID | Task | Est. | Dependencies | DoD | Primary metric |
|---|---|---:|---|---|---|
| S1-01 | Prompt 07 best-of-N (`parallel_attempts=3`) | 1.5d | none | Feature-flagged run path + tests for selection logic | `approve_rate`, `tokens_total` |
| S1-02 | Prompt 02 oracle mixed policy | 1.5d | none | Deterministic red-zone + stochastic sample + config docs | `cost_per_ac`, `false_approve_rate` |
| S1-03 | Prompt 12 symbolic-first reorder | 1d | none | LLM reviewer called only on inconclusive symbolic result | `llm_reviewer_call_rate` |
| S1-04 | Prompt 06 telemetry additions | 1d | S1-01,S1-02,S1-03 | Metrics emitted + regression tests for parser/summary | `marginal_oracle_lift`, `llm_call_ratio` |
| S1-05 | Prompt 33 Plan Structural Gate (MVP) | 2.5d | none | AC ownership + circularity + scope bounds + deps checks | `revise_after_stage1` |

## Sprint 2 (quality loops + ontology groundwork)

| ID | Task | Est. | Dependencies | DoD | Primary metric |
|---|---|---:|---|---|---|
| S2-01 | Prompt 34 Stage Classification Gate | 2d | S1-04 | Trivial stages route to deterministic checks only | `llm_call_ratio` |
| S2-02 | Prompt 15 compaction hierarchy + adaptive budget | 3d | S1-04 | 12-level policy + uncertainty budget deltas + tests | `replan_due_to_context_loss` |
| S2-03 | Prompt 11 antipattern continuant/occurrent split | 3d | S1-04 | `antipattern_matches` persisted with usefulness outcome | `retrieval_useful_rate` |
| S2-04 | Prompt 20 provenance + config invalidation | 2d | S1-04 | Fixture provenance tracked, invalidation trigger wired | `regressions_after_promote` |
| S2-05 | Prompt 41 ontology alignment spike | 2d | S2-03 | `pipeline_core.py` draft + migration ADR + POC tests | `schema_validation_failures` |

---

## 4) Measured vs Projected policy

Use this tag in PR descriptions and reports:

- `Measured`: observed directly in pipeline runs.
- `Measured (external)`: from literature; not yet validated in pipeline.
- `Projected`: hypothesis/estimate pending validation.

No projected claim should be merged without an experiment definition and a target metric.

---

## 5) Experiment matrix (quick)

| Hypothesis | Experiment | Success threshold |
|---|---|---|
| Mixed oracle policy cuts cost safely | A/B `oracle_full` vs `oracle_mixed` | `cost_per_ac -25%`, `false_approve_rate` non-inferior |
| Best-of-N improves outcomes | `N=1` vs `N=3` | `approve_rate +5pp`, `tokens_total <=2.5x` |
| Symbolic-first gate 12 saves calls | before/after call-rate comparison | `llm_reviewer_call_rate -60%` |
| Stage classification reduces LLM dependence | trivial-route enabled vs disabled | `llm_call_ratio -30%` with stable quality |
| Compaction adaptive avoids context loss | static vs adaptive budget | `replan_due_to_context_loss -30%` |

---

## 6) Risks and controls

| Risk | Control |
|---|---|
| Cost optimization harms quality | Non-inferiority guard on `false_approve_rate` |
| New gates over-block | Start in observe mode, then enforce |
| Metrics drift by suite composition | Freeze baseline suite per sprint |
| Ontology migration churn | Do spike + dual-write before full cutover |

---

## 7) Exit criteria for this plan

Plan succeeds when:
1. At least 7 of 10 tasks complete with tests.
2. `approve_rate` non-inferior and `cost_per_ac` down by >=20%.
3. `llm_call_ratio` down by >=25%.
4. No increase in security escape / false approve incidents.

