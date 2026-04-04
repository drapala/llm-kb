---
title: "Question Taxonomy"
sources:
  - path: raw/articles/miles-seven-research-gaps-taxonomy.md
    type: article
    quality: primary
  - path: raw/articles/socratic-prompting-llms.md
    type: paper
    quality: primary
  - path: raw/articles/oblique-strategies-lateral-thinking.md
    type: note
    quality: tertiary
  - path: raw/articles/popper-falsifiability-scientific-method.md
    type: article
    quality: primary
  - path: raw/articles/lakatos-research-programmes.md
    type: article
    quality: primary
  - path: raw/articles/systematic-review-gap-framework.md
    type: article
    quality: primary
created: 2026-04-04
updated: 2026-04-04
tags: [meta-kb, methodology, questioning, epistemology]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
---

## Resumo

The quality of KB insights depends more on the questions asked than the sources ingested. Six frameworks inform systematic questioning: Miles' 7 Research Gaps (where to look), Socratic Methods (how to probe), Oblique Strategies (how to reframe), Popper's falsifiability (how to form testable hypotheses), Lakatos's research programmes (how to evaluate if the KB is progressing or degenerating), and AHRQ's gap framework (how to structure questions via PICOS). Together they enable typed questions that open investigation rather than close it.

## Conteúdo

### 7 Types of Research Gaps (Miles, 2017)

| Gap Type | What it finds | /ask Template |
|----------|-------------|---------------|
| **Evidence** (contradiction) | Conflicting findings between sources | "Papers X and Y reach opposite conclusions about Z. What assumption differs?" |
| **Knowledge Void** | Unstudied territory | "What has NO ONE studied in this domain?" |
| **Practical-Knowledge** | Theory-practice disconnect | "Research says X works, practitioners do Y. Why?" |
| **Methodological** | Method-limited findings | "All studies used method A. What would method B reveal?" |
| **Empirical** (evaluation void) | Claims without data | "This sounds compelling. Where's the evidence?" |
| **Theoretical** (application void) | Theory not applied to relevant domain | "Theory T works for D1. What happens in D2?" |
| **Population** | Context-limited findings | "This works for X. Does it work for Y?" |

### 6 Socratic Techniques (Chang, 2023)

| Technique | Purpose | /ask Application |
|-----------|---------|-----------------|
| **Definition** (τί ἐστι) | Clarify before reasoning | "Before answering, define [concept] in this context" |
| **Elenchus** (cross-examination) | Find contradictions | /challenge command is elenchus applied to articles |
| **Dialectic** (thesis→antithesis→synthesis) | Resolve opposing views | Tension resolution table IS dialectic |
| **Maieutics** (intellectual midwifery) | Guided discovery from what's already known | Follow wikilinks to discover unstated connections |
| **Generalization** (induction) | Specific examples → general principle | How taxonomy articles (kb-architecture-patterns) are generated |
| **Counterfactual** | "What if the opposite were true?" | Most powerful /challenge question: "Under what conditions does this fail?" |

### Oblique Strategies for KB Questioning

Default /ask: direct question → direct answer. Linear.

Oblique approach: reframe BEFORE answering.

| Strategy | Application |
|----------|------------|
| "Reverse" | Invert: "when does this NOT work?" |
| "Use an old idea" | Apply foundational concept to modern problem |
| "What is the reality of the situation?" | Strip interpretation, look at raw/ only |
| "Emphasize differences" | Find divergence, not convergence |
| "Look closely at the most embarrassing details" | Focus on weakest claim |
| "Do nothing for as long as possible" | Don't ask yet — let questions emerge naturally |

### Popper's Falsifiability: Questions That Test, Not Confirm

Popper's cycle: **P₁ → TT → EE → P₂** (problem → tentative theory → error elimination → new problem)

| Principle | /ask Application |
|-----------|-----------------|
| "The scientist begins with PROBLEMS, not observations" | /question exists because of this — start with the question, not the data |
| Falsifiability as demarcation | Every wiki claim should answer: "what would disprove this?" If nothing can, it's unfalsifiable assertion, not knowledge |
| Bold conjectures > safe summaries | The most valuable articles make RISKY predictions. Our synthesis articles are bold conjectures — value comes from being testable, not correct |
| Corroboration ≠ verification | An article surviving /challenge is "corroborated," not "verified." It could still be wrong |
| Value improbable theories | Prefer questions that could generate surprising answers over questions with predictable outcomes |

**Falsifiability test for /ask:** Before accepting an answer, ask: "What evidence would make me change this answer?" If nothing would, the answer is unfalsifiable.

### Lakatos: Is the KB Progressing or Degenerating?

| Concept | KB Application |
|---------|---------------|
| **Hard core** (protected assumptions) | Blueprint principles: raw/ immutable, wiki as hint, retrieval is skeptical |
| **Protective belt** (modifiable) | Commands, heuristics, confidence thresholds, review checks |
| **Progressive programme** | Each new source generates novel predictions (insights not in existing articles) AND some predictions corroborate |
| **Degenerating programme** | New sources only confirm what's already "known." Novel synthesis fails when tested (RWKG subsumed by prior work) |
| **Ad hoc adjustments** | Qualifying numbers after the fact (16.1% → "on Qwen2"). Are these genuine refinements or degenerative patches? |

**Degeneracy test:** If /ask keeps generating the same TYPE of insights regardless of new sources, the KB is degenerating — confirming itself, not discovering. The /question command should detect this pattern.

### AHRQ Gap Framework: Structured Questions via PICOS

| Element | What it specifies | Example for KB |
|---------|------------------|---------------|
| **P**opulation | Which concept/article? | "For agent-memory-architectures..." |
| **I**ntervention | What mechanism/approach? | "...does temporal decay (Synapse)..." |
| **C**omparison | Against what alternative? | "...compared to experience-weighted edges (RWKG)..." |
| **O**utcome | Measured by what? | "...result in better retrieval accuracy on multi-hop QA..." |
| **S**etting | In what context/scale? | "...for KBs with 50+ articles?" |

**4 Reasons a Gap Exists:**

| Reason | KB Equivalent |
|--------|--------------|
| Insufficient info | source_quality:low, too few sources |
| Biased info | stance ratio (all confirming, no challenging) |
| Inconsistent results | documented tensions between articles |
| Not the right info | over-synthesis — sources don't say what we claim |

### Question Types for /ask

| Type | When to use | Template |
|------|-----------|----------|
| **CONTRADIÇÃO** | Two articles disagree | "X and Y reach opposite conclusions. What assumption differs?" |
| **ESCALA** | Mechanism described at one scale | "This works with 10 nodes. At what point does it break?" |
| **FRONTEIRA** | Need to find limits | "Simplest case where this is necessary — and most complex where it still works?" |
| **MECANISMO OCULTO** | Paper describes WHAT works but not WHY | "What underlying mechanism explains the observed results?" |
| **AUSÊNCIA** | Need to find blind spots | "What did all three authors NOT ask? What was out of scope for institutional, not intellectual reasons?" |
| **TRANSFERÊNCIA** | Concept from one domain | "Theory T works in D1. What happens in D2?" |
| **EMPÍRICA** | Claim without evidence | "This framework sounds compelling. What would a test look like?" |
| **FALSIFICAÇÃO** (Popper) | Claim accepted as true | "What evidence would disprove this? If nothing can, is it really knowledge?" |
| **DEGENERESCÊNCIA** (Lakatos) | KB producing same insights | "Are the last 5 /ask answers the same TYPE of insight? Is the KB confirming itself?" |

### Perguntas Proibidas (fecham em vez de abrir)

- "Is X better than Y?" → binary, kills nuance. Better: "Under what conditions does X outperform Y?"
- "What is X?" → definitional, no insight. Better: "What does X explain that nothing else does?"
- "Summarize X" → compression, not discovery. Better: "What does X imply that the author didn't explore?"
- "Do you agree with X?" → asks LLM for opinion (self-enhancement bias). Better: "What evidence would change your mind about X?"

## Interpretação

This taxonomy is our synthesis — Miles, Chang, Eno, Popper, Lakatos, and AHRQ didn't design these for LLM knowledge bases. The mappings (research gaps → /ask templates, falsifiability → wiki claim testing, research programmes → KB health evaluation, PICOS → structured queries) are our interpretations. The "perguntas proibidas" list is our prescription based on over-synthesis experience.

## Conexões

- [[tension-resolution]] — Evidence Gap questions are the discovery mechanism for tensions
- [[curation-anti-bias]] — Knowledge Void and Population Gap questions identify missing sources
- [[autonomous-kb-failure-modes]] — Empirical Gap questions detect speculative claims
- [[llm-as-judge]] — "Do you agree?" is a prohibited question due to self-enhancement bias
- [[kb-architecture-patterns]] — Lakatos's progressive vs degenerating directly evaluates KB health
- [[reflexion-weighted-knowledge-graphs]] — Popper's bold conjectures: RWKG is a testable hypothesis, not a proven architecture

## Fontes

- [Miles — 7 Research Gaps](../../raw/articles/miles-seven-research-gaps-taxonomy.md) — taxonomy of 7 gap types with definitions, widely cited in research methodology
- [Socratic Prompting](../../raw/articles/socratic-prompting-llms.md) — 6 Socratic techniques mapped to LLM prompting: definition, elenchus, dialectic, maieutics, generalization, counterfactual
- [Oblique Strategies](../../raw/articles/oblique-strategies-lateral-thinking.md) — lateral thinking via reframing: "honor thy error as hidden intention," reverse, emphasize differences
- [Popper — Falsifiability](../../raw/articles/popper-falsifiability-scientific-method.md) — P₁→TT→EE→P₂ cycle, bold conjectures > safe summaries, "scientist begins with problems not observations"
- [Lakatos — Research Programmes](../../raw/articles/lakatos-research-programmes.md) — hard core vs protective belt, progressive vs degenerating programmes, when to abandon a framework
- [AHRQ — Gap Framework](../../raw/articles/systematic-review-gap-framework.md) — PICOS structure for gap characterization, 4 reasons gaps exist (insufficient, biased, inconsistent, wrong info)
