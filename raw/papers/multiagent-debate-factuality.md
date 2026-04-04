---
source: https://arxiv.org/abs/2305.14325
authors: Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, Igor Mordatch
date: 2023-05-23
type: paper
arxiv: "2305.14325"
---

# Improving Factuality and Reasoning in Language Models through Multiagent Debate

## Abstract

Multiple LLM instances engage in multi-round debates to improve responses. Significantly enhances mathematical and strategic reasoning. Improves factual validity, reducing fallacious answers and hallucinations.

## Core Mechanism

Instead of one LLM generating and self-evaluating (single-agent with self-enhancement bias), multiple LLM instances:
1. Generate independent responses
2. Read each other's responses
3. Debate across multiple rounds
4. Converge toward consensus

## Key Insight for KB

This is the distributed systems answer to self-enhancement bias. Our wiki is written and evaluated by the same LLM — exactly the single-agent self-evaluation that CALM documents as biased (16.1% error). Multiagent debate proposes the fix: multiple independent evaluators debating.

Tension with single-agent approach: Tim Kellogg's article documents Cognition's critique that multi-agent creates "fragile systems" with "dispersed decision-making." So multi-agent debate fixes bias but introduces coordination fragility. Neither approach dominates.

## Relevance to /review

A /review that uses multiagent debate (multiple model calls evaluating each article independently, then debating disagreements) would mitigate self-enhancement bias without requiring a human. This is a middle ground between full autonomy (failure mode documented in autonomous-kb-failure-modes) and full human oversight.

---

*Nota: conteúdo baseado no abstract. Consultar PDF para benchmark results e debate protocol details.*
