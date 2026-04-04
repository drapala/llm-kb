---
source: https://plato.stanford.edu/entries/bounded-rationality/ + https://en.wikipedia.org/wiki/Gerd_Gigerenzer
author: Gerd Gigerenzer (sources: SEP + Wikipedia synthesis)
date: 1999-01-01
type: article
quality: primary
stance: confirming
---

# Gigerenzer: Fast-and-Frugal Heuristics and Ecological Rationality

## Core Framework

Fast-and-frugal heuristics are simple decision rules designed for uncertain environments. They work NOT despite their simplicity but BECAUSE of it — in the right environment, simplicity is a feature, not a bug.

## The 3 Key Heuristics

### Take-the-Best
- Examine cues sequentially in order of validity
- Select option based on FIRST discriminating cue
- Ignore all remaining cues
- Dramatically reduces computation vs linear regression
- Used naturally by experienced experts (police, professional burglars, airport security)

### Tallying
- Assign unit weights (+1 or -1) to features
- Count: more positives = choose this option
- "Equal-weight regression and unit-weight tallying commonly outperform proper linear models on small data sets"
- Simple improper models outperform proper linear models in OUT-OF-SAMPLE prediction

### Recognition Heuristic
- If you recognize one option but not the other, choose the recognized one
- "Semi-ignorant people who rely on recognition are as good as or better than ATP Rankings and experts at predicting Wimbledon outcomes"
- Less knowledge → better prediction (in specific conditions)

## When Heuristics Beat Complex Models: The Less-Is-More Effect

**Definition:** Scenarios where additional information or complexity DEGRADES decision outcomes. Counter to the conventional accuracy-effort trade-off.

**Formal mechanism: Bias-Variance Trade-off**

Total error = bias² + variance + irreducible noise

- **Bias**: systematic deviation from true values (heuristics have MORE bias)
- **Variance**: inconsistency of predictions across samples (heuristics have LESS variance)
- **On small samples**: variance dominates. Reducing variance (via simpler model) helps MORE than reducing bias (via complex model).

"A mind can be better off with an adaptive toolbox of biased, specialized heuristics."

**Conditions where heuristics win:**
1. **Small training samples** — variance dominates, simple models generalize better
2. **High-dimensional cue spaces** — more features = more variance = more over-fitting
3. **Unknown distributions** — can't optimize what you can't model
4. **Out-of-sample prediction** — in-sample fit ≠ generalization
5. **Knightian uncertainty** — uncertainty that can't be quantified as probability

**Conditions where heuristics LOSE:**
1. Large training samples (variance shrinks, bias dominates)
2. Low-dimensional spaces (few features, each informative)
3. Known distributions (can optimize directly)
4. In-sample fit (complex models always fit better in-sample)

## Ecological Rationality

A heuristic is "ecologically rational to the degree that it is adapted to the structure of an environment." There is no universally best heuristic — the environment determines which one works.

This rejects:
- "More information is always better" (Good's principle fails under uncertainty)
- "Complex models are always more accurate" (bias-variance shows otherwise)
- "Heuristics are cognitive shortcuts born from laziness" (they're adaptive tools evolved for specific environments)

## Key Empirical Results

- Tallying outperforms regression on out-of-sample prediction with small samples
- Take-the-Best matches or exceeds multiple regression in city-size estimation tasks
- Recognition heuristic outperforms ATP rankings for Wimbledon prediction
- Less-is-more shown "experimentally, analytically, and by computer simulations"
- Restricted working memory facilitates correlation detection in small samples

## Relevance to LLM Knowledge Bases

### Direct connection to KB claims:

**ERL "heuristics > trajectories" (+7.8% vs -1.9%):**
Gigerenzer EXPLAINS this. Heuristics = low-variance, high-bias. Trajectories = low-bias, high-variance. On Gaia2 (finite tasks, limited examples per task): variance dominates → heuristics win. This is EXACTLY the less-is-more effect. Not a coincidence — it's the same statistical mechanism operating in a different domain.

**ERL "40-60 items threshold then degrades":**
Gigerenzer PREDICTS this. As heuristic count increases: the "model" becomes more complex (more rules to search through) → variance increases → eventually variance overtakes the bias reduction from having more heuristics. The 40-60 number is an INSTANCE of the less-is-more transition point, specific to ERL's task and model. The existence of a transition point is Gigerenzer's general prediction; the specific number is task-dependent.

**"Compressão > raw em low-data":**
Gigerenzer CONFIRMS and GENERALIZES. Compression = bias increase + variance decrease. In the KB's regime (21 articles, ~56 sources — small sample by any standard): variance is the dominant error. Compressed articles (heuristics) will outperform raw source dumps (trajectories) not because compression is inherently better, but because the KB operates in a small-sample regime where variance dominates.

**The prediction Gigerenzer adds that ERL + Simon don't:**
If the KB grows to 500+ articles with deep coverage per concept (large-sample regime), the advantage of compressed heuristic articles REVERSES. At that scale, detailed articles with more cues (like trajectories) would generalize better because variance shrinks and bias becomes the dominant error. The KB's current "compression beats raw" finding is REGIME-SPECIFIC, not universal.

This is falsifiable: as the KB grows, track whether /ask quality on well-covered topics improves with MORE detail per article (not less). If it does, the KB has crossed the less-is-more transition point.
