---
source: https://en.wikipedia.org/wiki/The_Book_of_Why
authors: Judea Pearl, Dana Mackenzie
date: 2018-05-15
type: article
quality: primary
stance: neutral
---

# The Book of Why: The New Science of Cause and Effect (Chapters 1-3)

## The Ladder of Causation

Three levels encoding different concepts, corresponding to seeing, doing, and imagining.

### Level 1 — Association (Seeing)

**Formal:** P(y|x) = p — "the probability of Y=y given that we OBSERVED X=x is p"

**Question:** "What is?" / "How likely is Y given I see X?"

**Operators:** conditional probability, correlation, regression

**Example:** Observing that a crowing rooster correlates with sunrise. Cannot determine direction.

**Limitation:** Cannot distinguish cause from effect. Cannot determine if changing X would change Y. All of traditional statistics operates here.

### Level 2 — Intervention (Doing)

**Formal:** P(y|do(x), z) — "the probability of Y=y given that we INTERVENE and SET X to x, then observe Z=z"

**Question:** "What if I do X?" / "What would Y be if I change X?"

**Operators:** do-calculus, randomized controlled trials, causal diagrams, front-door criterion, instrumental variables

**Key distinction from Level 1:** Intervention is NOT conditional probability. P(y|do(x)) ≠ P(y|x). Seeing someone take aspirin (observation) ≠ making someone take aspirin (intervention). The causal effect is do(x), not x.

**Example:** Does smoking cause lung cancer? Requires intervention logic, not just correlation.

**Limitation:** Tells you what WILL happen if you intervene. Cannot tell you what WOULD HAVE happened if you hadn't.

### Level 3 — Counterfactual (Imagining)

**Formal:** P(y_x | x', y') — "given that X was x' and Y was y', what would Y have been if X had been x instead?"

**Question:** "Why?" / "What if X hadn't happened — would Y still have occurred?"

**Operators:** structural causal models (SCMs), twin networks, cross-world reasoning

**Example:** "Was it the drug that cured me?" requires imagining a world where you didn't take the drug but everything else was the same.

**Limitation:** Requires a causal MODEL, not just data. Two datasets can agree on all Level 1 and Level 2 queries while disagreeing on Level 3. Counterfactuals are under-determined by data alone.

## Key Principle: Levels Are Not Reducible

"No machine can derive answers to Level 2 queries from Level 1 data alone, regardless of how much data it has. No machine can derive Level 3 answers from Level 1 or Level 2 data alone."

This is a FORMAL impossibility, not a practical limitation. More data doesn't help. You need the right LEVEL of reasoning.

## Do-Calculus

3 rules that allow removing the do-operator from a query and reformulating it using only standard probability:
1. Insertion/deletion of observations
2. Action/observation exchange
3. Insertion/deletion of actions

If a causal effect is identifiable (derivable from data + causal diagram), do-calculus can find it. If not, no amount of data will help — you need an experiment (RCT) or stronger assumptions.

## Relevance to LLM Knowledge Bases

The KB's /ask has been operating almost entirely at Level 1:
- "X and Y co-occur in the corpus" (association)
- "Papers X and Y reach opposite conclusions" (associative tension)
- "5 sources observe this pattern" (associative evidence)

The anomaly "verbal reflection improves but self-assessment fails" was classified at Level 2 (intervention: ablation of test generation), but the explanation "LLM as amplifier" is Level 1 (co-occurrence of improvement + ancoragem in the same system).

The question "is verbalidade epifenômeno da ancoragem?" is Level 3 (counterfactual: "if verbal reflection hadn't been used, would the improvement still have occurred with the same ancoragem?"). The KB correctly identified it couldn't answer this — Pearl explains WHY it can't: Level 3 requires a causal model, not more data.
