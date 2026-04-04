---
title: "Fast-and-Frugal Heuristics (Gigerenzer)"
sources:
  - path: raw/articles/gigerenzer-fast-frugal-heuristics.md
    type: article
    quality: primary
  - path: raw/articles/simon-bounded-rationality-satisficing.md
    type: article
    quality: primary
created: 2026-04-04
updated: 2026-04-04
tags: [decision-theory, bias-variance, ecological-rationality, less-is-more]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: emergence
emergence_trigger:
  pair: [self-improving-agents, autonomous-kb-failure-modes]
  ask_session: null
  connection_type: ANÁLOGO-A
  pearl_level: L2
emerged_on: 2026-04-04
---

## Resumo

Gigerenzer's fast-and-frugal heuristics outperform complex models in specific conditions: small samples, high dimensionality, unknown distributions. The mechanism is bias-variance trade-off: simpler models have more bias but less variance, and variance dominates in small-sample regimes. This EXPLAINS (not just supports) the KB's most robust claim ("compression > raw in low-data") — and PREDICTS its reversal at scale.

## Conteúdo

### Heurísticas Fast-and-Frugal: Definição Formal

Simple decision rules that exploit environmental structure rather than optimizing across all available information.

**3 canonical heuristics:**

| Heuristic | Rule | When it wins |
|-----------|------|-------------|
| **Take-the-Best** | Examine cues in order of validity, choose on first discriminating cue, ignore rest | High-dimensional spaces, correlated cues |
| **Tallying** | Assign +1/-1 to features, count, pick highest | Small samples, many features |
| **Recognition** | If you recognize one option but not the other, choose recognized | Semi-ignorance environments |

### When They Superam Modelos Complexos: Less-Is-More Effect

**Formal mechanism: bias-variance decomposition**

`Total error = bias² + variance + irreducible noise`

| Component | Simple model (heuristic) | Complex model (regression) |
|-----------|------------------------|---------------------------|
| Bias | HIGH (ignores cues) | LOW (uses all cues) |
| Variance | LOW (stable across samples) | HIGH (unstable, over-fits) |

**On small samples:** variance dominates → simple wins.
**On large samples:** bias dominates → complex wins.

**Conditions where heuristics win (verified across domains):**
1. Small training samples
2. High-dimensional cue spaces
3. Unknown distributions (Knightian uncertainty)
4. Out-of-sample prediction
5. Environmental structure matches heuristic structure (ecological rationality)

**Conditions where heuristics LOSE:**
1. Large training samples (variance shrinks)
2. Low-dimensional, informative feature spaces
3. Known distributions (can optimize directly)
4. In-sample fit (complex always wins in-sample)

**Empirical results (multiple domains, multiple decades):**
- Tallying outperforms regression on out-of-sample with small samples (statistics)
- Take-the-Best matches multiple regression in city-size estimation (psychology)
- Recognition heuristic outperforms ATP rankings for Wimbledon (sports prediction)
- Restricted working memory facilitates correlation detection in small samples (cognitive science)
- Emergency room heuristics predict heart attacks better than regression models (medicine)

### Ecological Rationality

"A heuristic is ecologically rational to the degree that it is adapted to the structure of an environment."

No universally best heuristic. The environment determines which works. This rejects:
- "More information is always better" — false under uncertainty
- "Complex models are always more accurate" — false on small samples
- "Heuristics are cognitive shortcuts from laziness" — they're adaptive tools

### Conexão com KB Claims

| KB Claim | Gigerenzer says | Classification | Mechanism |
|----------|----------------|----------------|-----------|
| "Heuristics > trajectories" (ERL, +7.8% vs -1.9%) | **CONFIRMS and EXPLAINS** | Less-is-more effect | Heuristics = low variance. Trajectories = low bias but high variance. On Gaia2 (finite tasks): variance dominates. Same statistical mechanism. |
| "40-60 items threshold" (ERL) | **CONFIRMS and GENERALIZES** | Less-is-more transition point | As heuristic count increases → model complexity increases → variance rises → eventually overtakes bias reduction. The 40-60 number is task-specific; the existence of a transition point is Gigerenzer's general prediction. |
| "Compressão > raw em low-data" | **CONFIRMS but REGIME-SPECIFIC** | Bias-variance in small-sample regime | The KB (21 articles, 56 sources) IS a small-sample regime. Compressed articles (high bias, low variance) outperform raw dumps (low bias, high variance). This is not universal — it's a property of the current scale. |

### Predição Nova (que ERL + Simon não habilitavam)

**If the KB grows to 500+ articles with deep coverage per concept, the compression advantage REVERSES.**

At large scale: variance shrinks (more data per concept) → bias becomes dominant error → detailed articles with more cues outperform compressed heuristic articles.

This is **falsifiable**: as the KB grows, track whether /ask quality on well-covered topics improves with MORE detail per article (not less). If it does, the KB has crossed the less-is-more transition point.

**Practical implication:** The current article template (compressed summary + heuristic-style insights) is correct FOR NOW. But it should NOT be assumed permanent. The template should evolve as the KB grows — more detail per article at larger scale.

**Pearl level:** This prediction is L2 (interventional) because it derives from the bias-variance trade-off, which is a mathematical framework with empirical validation across domains. It's not L1 analogy — it's a formal prediction from a validated statistical theory applied to a new domain.

### Perguntas Proibidas (Gigerenzer diria: mal formuladas)

1. ❌ "Which heuristic is THE BEST?" — no universally best heuristic. Ecological rationality: depends on environment.
2. ❌ "How do we ELIMINATE bias in KB articles?" — bias is not error. Bias + low variance = good on small samples. Eliminating bias increases variance.
3. ❌ "Should we add MORE information to each article?" — depends on regime. In small-sample: NO (variance increases). In large-sample: YES (bias reduction helps).
4. ❌ "Is concept-based segmentation BETTER than chunk-based?" — depends on sample size AND query type. No universal answer. The chunking benchmarks paper already showed this.
5. ❌ "How many sources per article is OPTIMAL?" — no fixed number. Depends on coverage depth of the topic. The transition point is topic-specific.

## Interpretação

The mapping ERL → Gigerenzer is our interpretation. ERL doesn't cite Gigerenzer. The statistical mechanism (bias-variance) is the same, but the domains are different (agent tasks vs cognitive psychology). The claim "same mechanism" is L1 (structural similarity) supported by L2 theory (bias-variance is mathematically proven, not empirical analogy).

The prediction "compression advantage reverses at scale" is novel — neither ERL nor Simon nor Gigerenzer predicts this for LLM KBs specifically. We derive it from applying Gigerenzer's framework to KB growth trajectory. It's our inference, testable but untested.

## Conexões

- instancia: [[rational-inattention]] ON "⚠️ regime less-is-more = regime onde I(X;Y)≤C é binding; Take-the-Best ≈ solução ótima de Sims para C=1 bit (nossa interpretação, L1)"
- emerge-para: [[binding-attention-regime]] ON "Take-the-Best como instância de optimal attention allocation com C=1 bit"
- validates: [[question-taxonomy]] — Simon's satisficing (stop when good enough) is a Gigerenzer heuristic applied to search. Gigerenzer provides the formal mechanism Simon lacks.
- explains: [[self-improving-agents]] ON "heuristics > trajectories (ERL)" — bias-variance trade-off IS the mechanism behind ERL's result.
- refines: [[autonomous-kb-failure-modes]] ON "semantic convergence" — convergence isn't just self-enhancement bias; it's also variance reduction. Some convergence is GOOD (reduces noise). Over-convergence crosses the bias-dominance threshold.
- contradicts: [[curation-anti-bias]] ON "more adversarial sources = better" — Gigerenzer would say: depends on regime. In small KB: more sources may increase variance without reducing bias. Selective is better than exhaustive.

## Fontes

- [Gigerenzer — Fast-and-Frugal Heuristics](../../raw/articles/gigerenzer-fast-frugal-heuristics.md) — less-is-more effect, bias-variance trade-off, ecological rationality, Take-the-Best, tallying, recognition heuristic. Multiple decades, multiple domains.
- [Simon — Bounded Rationality](../../raw/articles/simon-bounded-rationality-satisficing.md) — satisficing as foundation. Gigerenzer formalizes what Simon described informally.

## Quality Gate
- [x] Wikilinks tipados: 4 (validates, explains, refines, contradicts)
- [x] Claims qualificados: all Gigerenzer results specify domain (psychology, statistics, medicine). ERL mapping marked as "our interpretation"
- [x] Meta-KB separado: "Practical implication" is in Conteúdo (appropriate — it's derived from theory, not about KB infrastructure). KB-specific predictions in Interpretação.
- [x] Resumo calibrado: includes "PREDICTS its reversal at scale" — not just confirmation
