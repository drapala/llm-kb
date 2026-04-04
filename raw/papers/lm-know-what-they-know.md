---
source: https://arxiv.org/abs/2207.05221
authors: Saurav Kadavath, Tom Conerly, Amanda Askell, et al. (Anthropic)
date: 2022-07-11
type: paper
arxiv: "2207.05221"
---

# Language Models (Mostly) Know What They Know

## Abstract

Investigates whether LLMs can assess correctness of own statements and predict which questions they'll answer accurately. Larger models show good calibration on multiple choice/true-false. Models can estimate P(True) — probability their answers are correct — and P(IK) — probability they "know" an answer without seeing specific proposals. Models struggle maintaining calibration on unfamiliar tasks.

## Key Findings

- Larger models are better calibrated (know what they know)
- Models can predict their own accuracy via P(True) estimates
- P(IK) — "probability I know" — works without reference answers
- Calibration breaks down on out-of-distribution tasks
- Suggests path toward "more honest models"

## The Epistemological Tension

This paper's "mostly" is critical. Models MOSTLY know what they know — but the failure cases are exactly the hard evaluation tasks that JudgeBench tests (where GPT-4o is near-random). The calibration is good on easy questions and degrades precisely when it matters most.

## Relevance to KB

Creates direct tension with our confidence scoring system. Our /ingest assigns confidence (high/medium/low) using the same LLM. This paper says that's mostly reliable — but "mostly" has a long tail. The failure case aligns with JudgeBench: on genuinely difficult claims (the ones where confidence matters most), the LLM's self-assessment degrades to near-random.

The tension: should we trust LLM confidence scores or not? Answer: trust on easy claims (factual, well-sourced), distrust on hard claims (interpretive, novel synthesis). Our confidence scoring should distinguish between these.
