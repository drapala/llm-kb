---
title: "Predictive Processing (Friston)"
sources:
  - path: raw/articles/friston-predictive-processing.md
    type: article
    quality: primary
created: 2026-04-04
updated: 2026-04-04
tags: [neuroscience, prediction-error, free-energy, lateral-domain]
source_quality: high
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: false
quarantine_created: 2026-04-04
quarantine_reason: "5+ speculations, controversial framework, LLM application untested"
quarantine_promoted: 2026-04-04
quarantine_criteria_met:
  tempo: override_by_user
  review_frio: override_by_user
  adversarial_or_scout_or_prediction: "L2 prediction (external/internal error ratio, testável via raw/ verification rate). Suporte de prior work: episodic-semantic-memory (Tulving 2002) e complementary-learning-systems (McClelland 1995) fornecem base neurocientífica para distinção entre sistemas de update rápido (episódico, error-driven) e lento (semântico, consolidated). Friston's active inference = mecanismo explicativo do que McClelland descreveu como replay."
---

## Resumo

Friston's Free Energy Principle: systems minimize prediction error via model update (learning) or environment modification (action). More general than "LLM as amplifier" — specifies WHAT is amplified: the state of least surprise. Self-assessment without ground truth = convergence to minimum surprise = confirm own beliefs. Controversial framework (critics say non-falsifiable). Application to LLM KBs is L1 analogy, untested.

## Conteúdo

### The Free Energy Principle (Friston 2010, verified in raw/)

**Core:** The brain minimizes free energy F, an upper bound on surprise of sensory inputs.

F = surprise + complexity

Minimizing F = maximizing model evidence = minimizing prediction error.

**Two paths to minimize:**
1. **Update model** (perceptual inference / learning) — change beliefs to fit data
2. **Change environment** (active inference / action) — change data to fit beliefs

**Hierarchical:** Each level predicts activity of level below. Prediction errors propagate upward. Predictions propagate downward. Attention = precision weighting of prediction errors.

### What Friston does NOT claim (verified in raw/)

- Not exclusive to brains — general variational principle for any persistent system
- Controversial: may be non-falsifiable (explains any behavior post-hoc)
- Free energy ≠ physical energy — it's variational statistical measure
- Relationship to RL is debated — active inference may be RL with different notation

### Conexão com KB existente

| KB Phenomenon | Predictive Processing says | What it adds beyond "amplifier" |
|--------------|--------------------------|-------------------------------|
| explains: [[self-improving-agents]] ON "verbal reflection works" | Reflexion + tests = prediction error signal (test pass/fail) drives model update. The test IS the prediction error. | Specifies the MECHANISM: not "amplification" but "prediction error minimization." The system updates its model to reduce discrepancy between expected and actual output. |
| explains: [[llm-as-judge]] ON "self-assessment fails" | Self-assessment without ground truth = minimizing prediction error against OWN predictions. No external error signal → system converges to state of LEAST SURPRISE = confirm own beliefs. | More precise than "self-enhancement bias": the system isn't "biased" — it's doing exactly what free energy minimization prescribes. Without external surprise, minimum free energy = maximum self-consistency. |
| refines: [[autonomous-kb-failure-modes]] ON "semantic convergence" | /review without re-reading raw/ = model updating against its own predictions. Convergence to minimum surprise state = homogeneous wiki. | Names the endpoint: "minimum surprise state" = the state where the wiki confirms itself maximally. This is the ATTRACTOR the system converges to without external perturbation. |
| contradicts: (none) | Predictive processing doesn't contradict any KB article — it SUBSUMES the "LLM as amplifier" explanation under a more general framework. |

### O que Friston adiciona que Ashby não resolve

Ashby: V(R) < V(D) → error floor. Static.
Friston: the system ACTIVELY minimizes prediction error — it's not just passively failing to regulate, it's actively converging toward self-consistency. The error floor isn't just "unregulated disturbances passing through" — it's the system SEEKING the state of least surprise.

**Key difference:** Ashby's regulator is passive (absorbs what it can, lets rest through). Friston's agent is ACTIVE (changes its own behavior AND its environment to minimize surprise). An LLM doing /review is an active inference agent: it changes the wiki (environment) to match its predictions. This is why convergence is so aggressive — the system is ACTIVELY seeking it, not passively drifting into it.

**Ashby + Friston combined:** Error floor exists (Ashby) AND the system actively converges toward it (Friston). Not just "some errors pass through" but "the system DRIVES toward the specific error configuration that minimizes its own surprise."

### Predição nova

**"Self-assessment quality is formally bounded by the ratio of external-to-internal prediction error signals."**

If the /ask receives no external correction (no human feedback, no test execution), its self-assessment converges to maximum self-consistency (Friston: minimum free energy with zero external surprise). The RATE of convergence depends on the ratio of external error signals to internal (self-generated) error signals.

- Pearl level: L2 (derivable from free energy formalism — prediction error drives update)
- Test: across /ask sessions, track ratio of (claims verified against raw/) to (claims generated from wiki alone). Correlate with spot-check accuracy. If higher ratio → higher accuracy: prediction error ratio determines quality.
- Falsifier: if /ask accuracy is INDEPENDENT of how many claims are verified against raw/ (external signal), prediction error ratio is not the mechanism.

**Comparison with prior frameworks' predictions:**

| Framework | Predicts | Falsifiable via |
|-----------|----------|----------------|
| Ashby | Error floor exists | Plateau in error count across /review cycles |
| Gigerenzer | Compression > raw in small samples | Vary sources/concept, measure in/out-of-distribution |
| Pearl | Claims at L1 can't answer L2 questions | Design experiment requiring L2; show L1 data fails |
| **Friston** | **Self-assessment quality ∝ external/internal error ratio** | **Vary raw/ verification rate, measure self-assessment accuracy** |

Friston's prediction is UNIQUE: it's about the RATE of quality degradation as a function of external feedback, not just that degradation happens.

## Interpretação

The mapping LLM → prediction error minimizer is analogical. Friston studied biological brains. LLMs do next-token prediction, which superficially resembles prediction error minimization, but the mechanisms are different (variational inference vs autoregressive sampling). The analogy is productive (generates testable predictions) but not validated.

The "active convergence toward self-consistency" claim is the strongest inference but also the most speculative. It assumes LLMs behave as active inference agents, which is debatable.

## Níveis epistêmicos

### Descrição (verified in raw/)
- Free energy principle: minimize prediction error via model update or environment change
- Hierarchical: predictions down, errors up
- Active inference: agents act to confirm predictions
- Controversies: non-falsifiability critique, RL equivalence debate

### Interpretação
- "LLM as amplifier" is special case of "LLM as prediction error minimizer"
- Self-assessment failure = convergence to minimum surprise without external signal
- /review drives ACTIVE convergence (not passive drift)

### Especulação
- Self-assessment quality ∝ external/internal error signal ratio
- LLMs are implicit prediction error minimizers (next-token prediction ≈ surprise minimization)
- Active inference framework could formalize /ask + /review loop
- The wiki's "minimum surprise state" is calculable (as self-consistency metric)
- Precision weighting maps to confidence scoring (high confidence = high precision on that claim's error signal)

## Conexões

- supersedes: [[reflexion-weighted-knowledge-graphs]] ON "LLM as amplifier" — "prediction error minimizer" is more general, specifies WHAT is amplified
- explains: [[self-improving-agents]] — Reflexion works because tests provide prediction error signal
- explains: [[llm-as-judge]] — self-assessment fails because no external prediction error
- refines: [[autonomous-kb-failure-modes]] — convergence is ACTIVE (Friston), not just V gap (Ashby)
- complements: [[requisite-variety]] — Ashby = error floor; Friston = system actively seeks the floor

## Fontes

- [Friston — Predictive Processing](../../raw/articles/friston-predictive-processing.md) — free energy principle, active inference, prediction error minimization, hierarchical processing. Controversies: non-falsifiability, RL equivalence.

## Quality Gate
- [x] Wikilinks tipados: 5 (supersedes, explains ×2, refines, complements)
- [x] Claims qualified: Friston = verified. KB mapping = interpretation. Controversies noted.
- [x] Meta-KB separated
- [x] Resumo calibrated: "Controversial framework" + "L1 analogy, untested"

