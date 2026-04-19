# S2-03 — Prompt 11 Antipattern Continuant/Occurrent Split

## Context
Current feedback loop is weak without explicit antipattern match events.

## Scope
- Keep registry items as continuants (`antipatterns`).
- Add occurrent store (`antipattern_matches`) with usefulness outcome.
- Wire retrieval feedback loop to match events.

## Out of Scope
- Full ontology migration for all registries.

## DoD
- Match events persisted with stable schema.
- Feedback loop uses match outcomes for decay/prioritization.
- Migration path keeps backward compatibility.

## Primary Metrics
- `retrieval_useful_rate`

## Dependencies
- S1-04

## Estimate
- 3d

