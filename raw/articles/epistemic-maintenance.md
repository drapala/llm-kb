---
author: "João Drapala"
year: 2026
type: article
quality: primary
stance: neutral
status: unprocessed
domain: meta-kb
---

# LLM Wiki — Epistemic Maintenance

A companion to [LLM Wiki](llm-wiki.md). That document describes how to build a persistent, compounding knowledge base using LLMs. This one describes how to keep it honest.

## The problem the first document doesn't mention

The LLM Wiki pattern solves the maintenance problem: the LLM does the bookkeeping that humans abandon. Cross-references stay current. Summaries get updated. The wiki grows without the usual cost.

But there's a second maintenance problem that's harder to see. The wiki accumulates mechanical knowledge correctly — and accumulates epistemic drift silently, for free, at the same rate. Every review pass by the same LLM that wrote the article is slightly self-confirming. Every source you add is one you chose to add. Every synthesis the LLM writes reflects what it already believes. Over time, the wiki becomes a high-fidelity mirror of the compiler's priors, not of reality.

The dangerous part is that the wiki looks healthy throughout. Links are valid. Cross-references work. Pages are well-written. The degradation is invisible at the structural level — it shows up in the quality of claims, not the integrity of the file system. You only notice when you ask a question and the wiki answers confidently, coherently, and wrong.

This is the problem epistemic maintenance addresses.

## Three failure modes

**Curation bias.** You add sources that confirm what you already believe, because those are easier to find and more satisfying to read. The wiki grows more detailed and more confident in a direction set by your initial priors. A wiki built entirely on confirming sources is a sophisticated echo chamber.

**Over-synthesis.** The LLM connects dots that the sources don't connect. An analogy here, an inference there — each individually plausible, none explicitly in any source, together building a structure with no foundation. Over-synthesized claims look like insights. They read like the best part of the wiki. They're the most likely to be wrong.

**Self-confirming review.** You ask the LLM to review a wiki page it wrote. The LLM finds the page coherent, well-supported, and largely accurate — because it's being asked to evaluate its own output using the same internal model that produced it. It can catch surface errors (a wrong date, a missed link). It can't catch the systematic biases it introduced when writing.

These three failures compound. Biased curation produces over-synthesized claims. Self-confirming review validates them. After enough cycles, the wiki reflects the compiler's worldview back at you with the authority of a well-maintained reference.

## The architecture of epistemic maintenance

Epistemic maintenance is a layer on top of the mechanical maintenance described in the LLM Wiki document. It has three components:

**Adversarial sourcing.** Build a rule into your schema: some fraction of sources you ingest should actively challenge the wiki's existing claims — not just confirm them. A practical threshold: 1 in 5 sources should hold a stance that contradicts, challenges, or complicates what the wiki currently says on the relevant topic. This isn't about balance for its own sake. It's about preventing the wiki from becoming a closed loop. The LLM can help you find adversarial sources once you've identified a topic the wiki covers confidently — "what would a serious critic of this position say? what papers or authors argue the opposite?"

**Claim provenance.** Every claim in the wiki should be traceable to a specific source. Not just cited — traceable. If the LLM writes "X causes Y," there should be a raw source file where that claim appears, and the wiki page should link to it. If a claim is the LLM's synthesis across multiple sources rather than something any single source says, it should be marked as such — visually, explicitly, unambiguously. The convention doesn't matter (a flag, a section header, a metadata field — pick what works for you). What matters is that synthesis is distinguishable from citation. When you read the wiki six months later, you should be able to tell at a glance which claims come from sources and which come from the LLM's interpretation of sources.

**Temporal separation.** The same session that ingests a source and writes an article about it should not also evaluate the quality of that article. Evaluation should happen later — in a different session, when the LLM doesn't have the original source fresh in context and is reading the wiki page as a reader, not as its author. This is a small procedural constraint with a large effect. The LLM reading its own work cold, without the source material immediately available, is a genuinely different cognitive act than the LLM reviewing what it just wrote. It will catch different things. The temporal gap is the mechanism; the duration matters less than the break.

## Operations

**Ingest with stance tracking.** When you add a source, record its stance toward the wiki's current claims: confirming, neutral, or challenging. Review the distribution periodically. If challenging sources are under-represented, that's a signal about your sourcing, not a signal that the wiki's claims are strong.

**Quarantine speculative articles.** When the LLM writes a page that rests heavily on its own synthesis rather than direct source content — a cross-paper comparison, an original framework, an analogy it developed — treat that page differently from pages that summarize a single source. Don't let it be linked from other pages immediately. Let it sit. Come back to it in a later session, read it cold, and ask: is this what the sources actually say, or is this what I thought the sources were pointing toward? Promote it to full status only when you've confirmed it in a separate pass.

**Challenge passes.** Periodically, ask the LLM to argue against specific wiki pages rather than review them. Not "is this accurate?" but "what's the strongest case that this is wrong?" The LLM is better at adversarial analysis than at neutral review — it has to actively construct a counterargument, which forces it to engage with the claim rather than pattern-match to its own style. A page that can't survive a challenge pass probably shouldn't be in the wiki.

**Lint for epistemic health.** The standard lint (orphan pages, missing cross-references, stale claims) checks structural health. Add an epistemic lint: how many pages contain claims that aren't traced to a source? How many synthesis claims are marked as such vs. unmarked? What's the ratio of confirming to challenging sources ingested this month? These numbers don't tell you whether the wiki is right — they tell you whether the wiki is epistemically honest about what it knows.

## Why the protocols work

None of these protocols make the LLM smarter or more accurate. They create structural friction against self-confirmation. The friction is the feature.

Adversarial sourcing doesn't improve any individual article — it ensures the wiki has encountered its own counterarguments. Claim provenance doesn't catch false claims — it makes false claims harder to hide and easier to trace when found. Temporal separation doesn't make the LLM's review better — it removes the confirmation bias that comes from reviewing what you just wrote.

The parallel in software is code review and CI. A linter doesn't make a programmer smarter. A code review doesn't mean the reviewer is better than the author. The value is structural: a second pass, by a different context, looking for different things, with a different mandate. The process catches what the individual pass misses — not because the second pass is superior, but because it's independent.

Epistemic maintenance applies the same logic to knowledge. The wiki is the codebase. Every claim is a function. The protocols are the test suite and code review process. A claim that hasn't been challenged hasn't been tested. A synthesis that hasn't been marked as synthesis is an undocumented assumption. A page that hasn't survived a cold read is a function that's never been called from outside the module that wrote it.

## Calibrating to your context

The full protocol described above is heavier than most contexts need. Calibrate to your use case.

For personal wikis — health tracking, reading notes, hobby research — a lighter version is usually enough: mark synthesis explicitly, occasionally add a source that challenges a position you hold confidently, and review important pages cold before acting on them.

For research or professional contexts where the wiki informs decisions — competitive analysis, due diligence, technical research — the full protocol matters more. The cost of an over-synthesized claim that gets acted on is higher than the cost of running a challenge pass.

The minimum viable epistemic practice is two things: mark synthesis (so you know what's interpretation), and add adversarial sources (so the wiki has encountered its own counterarguments). Everything else builds on these.

## Note

Like the LLM Wiki document, this is intentionally abstract. The specific conventions — how you mark synthesis, what counts as a challenging source, how you structure a challenge pass — depend on your domain, your LLM, and what you're building toward. Share this document with your LLM agent and work out the specifics together. The document's only job is to name the problem and sketch the shape of the solution. Your LLM can figure out the implementation.

The LLM Wiki document ends by crediting Vannevar Bush's Memex. Bush's vision was a personal, actively curated knowledge store with associative trails between documents. The part he couldn't solve was maintenance. The LLM handles that.

The part Bush also couldn't solve — because it wasn't a technical problem — was the curator's own biases shaping what got filed and how it got connected. That part doesn't get easier just because the maintenance is free. It gets harder, because now the wiki grows fast enough that the biases compound before you notice them.

Epistemic maintenance is the answer to the half of the Memex problem that wasn't about maintenance.
