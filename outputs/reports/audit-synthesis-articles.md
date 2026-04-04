# Epistemic Audit — Synthesis Articles

Audited: 2026-04-03
Auditor: Claude (automated epistemic review)
Method: Each claim in wiki articles checked against cited raw/ sources.

**NOTE:** Article 2 (`wiki/concepts/reflexion-weighted-knowledge-graphs.md`) does not exist in the KB. Audit covers the remaining 5 articles.

---

## 1. kb-architecture-patterns.md

### FACTS (verified):
- "Karpathy: ~100 articles and ~400K words" → confirmed in raw/articles/karpathy-llm-knowledge-bases.md ("mine on some recent research is ~100 articles and ~400K words")
- "Karpathy: LLM writes and maintains all of the data of the wiki, I rarely touch it directly" → confirmed in raw/articles/karpathy-llm-knowledge-bases.md
- "Karpathy: index files + brief summaries sufficient... without RAG at small scale" → confirmed ("I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files")
- "Karpathy: outputs filed back into wiki" → confirmed ("I end up filing the outputs back into the wiki")
- "Karpathy: LLM health checks for linting" → confirmed ("I've run some LLM health checks over the wiki")
- "Elvis/DAIR.ai: uses QMD for indexing" → confirmed in raw/articles/elvis-personal-kb-agents.md ("indexed using @tobi's qmd cli tool")
- "Elvis: tuned Skill for paper discovery" → confirmed ("tuned a Skill for months to find high-signal, relevant papers")
- "Elvis quote: research questions are only as good as the insights agents have access to" → confirmed (verbatim in source)
- "Paulo Silveira: Telegram as input, Whisper transcribes, Claude Sonnet classifies" → confirmed in raw/articles/paulo-silveira-open-claw-pkm.md
- "Paulo: anti-slop philosophy" → confirmed ("aquele ar de slop")
- "Paulo: historical references to Zettelkasten and Dostoevsky" → confirmed in source
- "ERL: heuristics +7.8% vs trajectories -1.9% on Gaia2" → confirmed in raw/papers/erl-experiential-reflective-learning.md
- "LC 56.3% vs RAG 49.0%" → confirmed in raw/papers/long-context-vs-rag-evaluation.md
- "RAPTOR summary nodes contribute 23-57% of useful retrieved content" → confirmed in raw/papers/raptor-recursive-abstractive-retrieval.md (NarrativeQA 57.4%, QASPER 23%, QuALITY 32.3% — range is derived from these)

### INTERPRETATIONS:
- "Pattern 1 scale limited to ~200 articles" → inferred from Karpathy's description of ~100 articles working well, not a stated limit. Karpathy never claims a ceiling.
- "Pattern 2 scales to 1000+ papers" → inferred; Elvis mentions "100s of papers" but never claims 1000+.
- "Pattern 3 scale ~50 outputs" → entirely inferred by the KB; Paulo never quantifies a limit.
- "_index.md is analogous to RAPTOR root node" → acknowledged as analogy in the article itself ("this is an analogy, not a validation"), correctly labeled.
- "ERL validates concept articles as superior to raw source dumps" → interpretation. ERL tested heuristics vs trajectories for agent task execution, not knowledge compilation. The article notes this but still frames it as validation.
- "RAPTOR analogy table (raw chunks = leaf, concepts = mid, index = top)" → KB's own mapping, not from RAPTOR paper.
- "KAIROS-Review parallel" → the article references KAIROS but KAIROS is not among the cited raw sources for this article. The parallel is the KB's own construction.

### SPECULATIONS:
- "Pattern 4: Bandwidth-Aware Retrieval as universal meta-pattern" → proposed by KB. Claude Code internals describe compaction hierarchy, but calling it a "universal pattern" applicable to all KB architectures is the KB's extrapolation.
- "When to use" guidance for each pattern → entirely the KB's judgment, not stated by any source author.
- Comparison matrix bottleneck column ("Ingest quality", "Tooling setup", "Human time", "Context budget") → KB's original categorization, not from sources.

### POTENTIAL ERRORS:
- "Elvis: BM25 + vector + reranking (QMD)" → Elvis's raw source says QMD provides "semantic search and surfacing insights" but does NOT specify BM25 + vector + reranking as the mechanism. The specific retrieval architecture is assumed by the KB, not stated by Elvis.
- "Elvis: MCP tools power interactive visualizations inside agent orchestrator" → Elvis says "mcp tools inside my agent orchestrator system" but the raw source describes "interactive artifact generator" — the KB's characterization of "MCP visual artifacts" as a formal pattern name is the KB's construction.
- "Pattern 3: Human retains editorial control over final synthesis" → partially confirmed. Paulo says he won't let machines "generate final drafts" but the raw source is more nuanced than "human writes final output" suggests.

---

## 2. reflexion-weighted-knowledge-graphs.md

**FILE DOES NOT EXIST.** Cannot audit. The article `wiki/concepts/reflexion-weighted-knowledge-graphs.md` is not present in the KB.

---

## 3. autonomous-kb-failure-modes.md

### FACTS (verified):
- "Self-enhancement bias (CALM: 16.1% error)" → confirmed in raw/papers/calm-llm-judge-biases.md ("up to 16.1% error rate (Qwen2)")
- "Reflexion ablation: self-reflection without independent grounded feedback degrades to 52%" → confirmed in raw/papers/reflexion-verbal-reinforcement-learning.md ("Self-reflection alone (without test generation) degrades performance to 52%")
- "JudgeBench: self-assessment on difficult problems is near-random" → confirmed in raw/papers/judgebench-evaluating-llm-judges.md ("GPT-4o performs just slightly better than random guessing")
- "ERL: random heuristic inclusion degrades after 40-60 items" → confirmed in raw/papers/erl-experiential-reflective-learning.md ("Random selection peaks at 40-60 heuristics then degrades")
- "ERL: LLM-based selective retrieval (k=20) peaks at 56.1%" → confirmed in source

### INTERPRETATIONS:
- "The 4 failure modes (semantic convergence, authority bias cascade, index bloat, forced tension resolution)" → entirely the KB's framework. No source paper describes these 4 specific failure modes for knowledge bases.
- "~30 days degradation timeline (Day 1-7 honeymoon, Day 7-14 convergence, etc.)" → complete speculation presented with false precision. No source provides a timeline for KB degradation.
- "KB equivalent of reward hacking" → KB's analogy, not from any cited source.
- "Layer 3 Circularity Problem" → original KB analysis. Reflexion's distinction is correctly cited, but applying it to raw/ verification is the KB's interpretation.
- "Multiagent debate as middle ground for /review" → application of Du et al. to KB context is interpretation.

### SPECULATIONS:
- The entire "Degradation Timeline" section with specific day ranges → no empirical basis whatsoever. Presented as if observed but entirely speculative.
- "Mitigations" table → KB's proposed solutions, not evidence-based. No source tested these mitigations.
- "The fix is not more rules — it's external ground truth" with 3 concrete options → KB's design recommendation, not from any source.
- "Semantic convergence starts invisible in Week 1-2" → no source provides a timeline.

### POTENTIAL ERRORS:
- **"Self-enhancement bias (CALM: 16.1% error)" presented as universal** → The CALM paper reports 16.1% for Qwen2 specifically, not as a general rate for all LLMs. Claude-3.5 showed "greatest overall resilience." The article uses 16.1% repeatedly as if it's a universal constant, but it's a worst-case for one specific model.
- **"Reflexion without independent grounded feedback degrades to 52%"** → Misleading reframing. The Reflexion paper says "self-reflection alone WITHOUT TEST GENERATION" degrades to 52%. The key missing element is automated test generation on HumanEval (a programming benchmark), not "independent grounded feedback" in general. The KB reinterprets "test generation" as "independent grounded feedback" to fit its narrative about raw/ verification.
- **"Authority bias makes LLM trust cited claims more" → circular validation loop** → CALM defines authority bias as favoring answers with citations (even fake ones), which is correct. But the leap to "circular validation loop" where the LLM confirms its own interpretations because raw/ was the original source is the KB's construction, not demonstrated by CALM.
- **"Tim Kellogg — 'compression becomes cognitive work'"** → Tim Kellogg is not among the cited sources in the frontmatter. The quote attribution cannot be verified from the listed sources.

---

## 4. tension-resolution.md

### FACTS (verified):
- "Reflexion: self-reflection without grounded feedback degrades to 52% (ablation)" → confirmed in raw/papers/reflexion-verbal-reinforcement-learning.md (with caveat about test generation vs. grounded feedback)
- "CALM: self-enhancement bias up to 16.1%" → confirmed (for Qwen2 specifically) in raw/papers/calm-llm-judge-biases.md
- "ERL: heuristics (+7.8%) vs trajectories (-1.9%)" → confirmed in raw/papers/erl-experiential-reflective-learning.md
- "Knowledge Conflicts Survey: 3 conflict types (context-memory, inter-context, intra-memory)" → confirmed in raw/papers/knowledge-conflicts-llms-survey.md
- "GPT-4 shows 13% inconsistency rate on paraphrased queries" → confirmed in raw/papers/knowledge-conflicts-llms-survey.md
- "LLMs show strong confirmation bias toward parametric knowledge" → confirmed in raw/papers/knowledge-conflicts-llms-survey.md
- "Models favor semantically coherent info, susceptible to misleading prompts" → confirmed in raw/papers/knowledge-conflicts-llms-survey.md

### INTERPRETATIONS:
- "Reflexion → grounded verification required for tension resolution" → interpretation. Reflexion tested programming tasks with unit tests, not KB tension resolution.
- "CALM → self-enhancement is THE central risk" → interpretation. CALM identified 12 biases; self-enhancement is not singled out as "central" by the paper.
- "ERL → resolutions become heuristics" → applying ERL's heuristic generation to tension resolution is the KB's analogy.
- "Synapse → graph-based discovery" → Synapse listed as source but not among audited sources. Claim about wikilink traversal is the KB's interpretation.
- The Known Tensions table → each resolution is the KB's own analysis; no source paper resolved these specific tensions.

### SPECULATIONS:
- "A /tensions command is the same pipeline as /review with 'contradiction' instead of 'overlap'" → KB design opinion, not evidence-based.
- Resolution Protocol (4 steps) → entirely the KB's proposed methodology.
- "For each pair of articles sharing 2+ raw/ sources, compare key claims" → KB's proposed discovery method, not from any source.

### POTENTIAL ERRORS:
- **"Reflexion: self-reflection without grounded feedback degrades to 52%"** → Same issue as article 3. The actual finding is about self-reflection without TEST GENERATION on HumanEval (programming benchmark), not about "grounded feedback" in the general sense.
- **"13% inconsistency rate" validates "our circuit breaker: don't trust a single /ask response"** → The Knowledge Conflicts survey reports 13% as intra-memory conflict. The survey doesn't recommend circuit breakers — it discusses faithful-to-context decoding, discriminators, and disentangling. The design implication is the KB's, not the survey's.
- **Resumo says "Five mechanisms" but Conteudo lists 6** → Internal inconsistency. The summary claims 5 mechanisms but the content section adds a 6th ("Knowledge Conflicts Survey → Formal Conflict Taxonomy").

---

## 5. curation-anti-bias.md

### FACTS (verified):
- "CALM: self-enhancement bias 16.1%" → confirmed (for Qwen2) in raw/papers/calm-llm-judge-biases.md
- "ERL: random inclusion degrades after 40-60 items" → confirmed in raw/papers/erl-experiential-reflective-learning.md
- "Knowledge Conflicts: LLMs show strong confirmation bias toward parametric knowledge" → confirmed in raw/papers/knowledge-conflicts-llms-survey.md
- "GPT-4 13% inconsistency" → confirmed in raw/papers/knowledge-conflicts-llms-survey.md

### INTERPRETATIONS:
- "LLM self-assessment is reliable for factual claims but degrades on interpretive synthesis" → partially supported. raw/papers/lm-know-what-they-know.md says models are "mostly" calibrated and that "calibration breaks down on out-of-distribution tasks." The KB reinterprets "out-of-distribution" as "interpretive synthesis" which is reasonable but not directly stated.
- "When /ingest has 15 articles about sophisticated memory architectures, it reads the 16th paper with confirming lenses" → KB's application of confirmation bias finding to KB scenario. Plausible but not tested.
- "3 Layers of Bias (selection, interpretation, evaluation)" → KB's own framework, not from any source.
- "5 Improvements" → entirely the KB's proposed mitigations, not from any source paper.

### SPECULATIONS:
- "Adversarial Source Quota: after 5 consecutive confirming sources, alert user" → KB's proposed design, no empirical basis for the number 5.
- "ERL-Based Ingest Threshold: when wiki exceeds 40 articles, require novelty score; when exceeds 80, require sub-indices" → KB extrapolates ERL's 40-60 heuristic degradation threshold to article count thresholds. ERL tested agent task execution, not wiki management. The 40 and 80 thresholds are invented.
- "Multiagent Spot-Check: 2-3 random articles per /review with different system prompts" → KB's proposed design, not from any source.

### POTENTIAL ERRORS:
- **"LMs Know What They Know confirms: LLM self-assessment is reliable for factual claims but degrades on interpretive synthesis"** → The paper says models are "mostly" calibrated on multiple choice/true-false and calibration "breaks down on out-of-distribution tasks." It does NOT distinguish "factual claims" from "interpretive synthesis." The KB's distinction is its own interpretive layer.
- **Split Confidence Scoring lists "interpretation_confidence: medium|medium|low"** → Appears to be a typo. Should likely be "high|medium|low" to parallel source_quality. Minor but could cause confusion.

---

## 6. raptor-vs-flat-retrieval.md

### FACTS (verified):
- "RAPTOR: GMM soft clustering, chunk → cluster → summarize → re-embed → repeat" → confirmed in raw/papers/raptor-recursive-abstractive-retrieval.md
- "0.28 compression ratio (72% compression)" → confirmed in RAPTOR paper
- "Collapsed tree outperforms tree traversal" → confirmed in RAPTOR paper
- "Non-leaf nodes contribute 23-57% of retrieved content" → confirmed (23% QASPER, 32.3% QuALITY, 57.4% NarrativeQA)
- "RAPTOR 38.5% vs chunk-based 20-22%" → confirmed in raw/papers/long-context-vs-rag-evaluation.md
- "LC 56.3% vs RAG 49.0%" → confirmed in raw/papers/long-context-vs-rag-evaluation.md
- "NVIDIA study: page-level chunking won at 0.648 accuracy" → confirmed in raw/papers/chunking-strategies-rag-comparison.md
- "Chroma: up to 9% recall variation across chunking methods" → confirmed in source
- "Proposition chunking outperforms concept-level for factoid queries" → confirmed in source
- "Factoid queries best at 256-512 tokens, analytical at 1024+" → confirmed in source
- "4% hallucination rate in RAPTOR sampled nodes" → confirmed in RAPTOR paper

### INTERPRETATIONS:
- "_index.md is a RAPTOR root node" → acknowledged as analogy. Note: the "Relevance to Knowledge Bases" section in raw/papers/raptor-recursive-abstractive-retrieval.md supports this mapping, but that section is itself an editorial addition in the raw/ note, not from the RAPTOR authors.
- "Layer 1→2→3 escalation ≈ collapsed tree" → KB's analogy. RAPTOR's collapsed tree selects by cosine similarity across all levels simultaneously; the KB's layers are sequential escalation. Structurally different despite the analogy.
- "Concept-based > chunk-based supported by RAPTOR 38.5% vs 20-22%" → interpretation. RAPTOR uses summarization-based retrieval, different from concept-based extraction.
- "ERL selection degradation at 40-60 items → real degradation starts at 50-80 articles" → significant extrapolation. ERL tested agent task execution heuristics; applying its selection limit to _index.md is unvalidated.

### SPECULATIONS:
- "Sub-indices (_index-agents.md, _index-retrieval.md) as RAPTOR mid-level nodes" → KB's proposed architecture, not from any source.
- "Two-step selection stays within ERL-validated selection window" → combining ERL's limit with RAPTOR's structure to justify sub-indices is novel reasoning with no empirical backing.
- "LLM-guided concept extraction is more precise for knowledge bases than statistical embedding clustering" → presented as fact but entirely unsupported.
- "At ~200 articles, QMD solves this better than DIY embeddings" → unsupported claim.

### POTENTIAL ERRORS:
- **"RAPTOR outperforms chunk-based retrievers (38.5% vs 20-22%)" attribution** → The 38.5% figure comes from raw/papers/long-context-vs-rag-evaluation.md, not from the RAPTOR paper itself. The RAPTOR paper reports QuALITY 82.6%, QASPER 55.7%, NarrativeQA 30.8%. The wiki article conflates results from two different papers.
- **"Our /ingest groups by concept — exactly what RAPTOR does via clustering"** → RAPTOR clusters by embedding similarity (statistical). The KB groups by LLM semantic judgment. These are fundamentally different mechanisms. "Exactly what RAPTOR does" overstates the parallel.
- **"LLM-guided concept extraction is more precise for knowledge bases than statistical embedding clustering"** → presented as fact ("is more precise") but is an unsupported assertion. No source compares these approaches.

---

## Summary of Most Serious Findings

### Cross-Article Patterns:

1. **The "52% degradation" from Reflexion is systematically misrepresented.** The actual finding is about self-reflection without automated TEST GENERATION on HumanEval (a programming benchmark). The KB consistently reframes this as "self-reflection without independent grounded feedback" to make it applicable to KB verification. Executable unit tests are a much stronger form of grounding than reading raw/ sources. Used in articles 3, 4, and 5.

2. **The 16.1% self-enhancement bias is model-specific (Qwen2) but used as universal.** CALM tested 6 models with varying bias rates. Claude-3.5 showed the "greatest overall resilience." Using the worst-case number from one model as a general constant is misleading. Used across all articles.

3. **ERL's 40-60 heuristic degradation threshold is extrapolated far beyond its domain.** ERL tested agent task heuristics on Gaia2. The KB applies this to _index.md selection, wiki article count limits, and sub-index migration triggers — none of which are validated. Used in articles 3, 5, and 6.

4. **Degradation timelines are pure speculation.** The "~30 days" timeline in autonomous-kb-failure-modes.md has no empirical basis but is presented with specific day ranges suggesting observation.

5. **"Relevance to Knowledge Bases" sections in raw/ sources are editorial additions, not paper claims.** Several raw/ files include KB-specific mappings that wiki articles then cite as if they come from the original papers.
