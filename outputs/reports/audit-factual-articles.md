# Epistemic Audit — Factual Wiki Articles

Auditor: Claude Opus 4.6 (1M context)
Date: 2026-04-03

---

## 1. context-management.md

**Source:** raw/articles/claude-code-internals-harness-engineering.md

### FACTS (verified):

- "Auto-Compaction triggered at `context_window - 13,000` tokens" → confirmed in raw source (Section 10)
- "Strip images/documents from older messages" → confirmed (step 1 of auto-compaction)
- "Group messages by API round" → confirmed (step 2)
- "Call compaction model for summary" → confirmed (step 3)
- "Replace old messages with CompactBoundaryMessage" → confirmed (step 4)
- "Re-inject up to 5 files + skills post-compaction (50K for files, 25K for skills)" → confirmed (step 5)
- "Circuit breaker: max 3 consecutive failures" → confirmed
- "Microcompaction: time-based, size-based, tool-specific" → confirmed
- "Tool-specific: only compacts FileRead, Bash, Grep, Glob, WebSearch, WebFetch, FileEdit, FileWrite" → confirmed
- "Cache-aware: preserves prompt cache integrity" → confirmed (raw: "cached variant preserves prompt cache integrity via CacheEditsBlock")
- "Snip Compaction: history truncation preserving assistant's protected tail" → confirmed
- "Non-destructive: full history kept in REPL for scrollback" → confirmed
- "Context Collapse: committed only when API returns 413" → confirmed ("committed lazily — only when API returns 413")
- "Cascade: collapse drain → reactive compact → surface error" → confirmed
- "System context (memoized): git status, cache breaker" → confirmed
- "User context (memoized): CLAUDE.md contents, current date" → confirmed
- "Both memoized per session" → confirmed

### INTERPRETATIONS:

- "a pattern directly applicable to any knowledge base retrieval system" → KB editorial claim, not from source
- "Bandwidth-Aware Retrieval Pattern" section (Layer 1/2/3 mapping to _index.md, wiki/, raw/) → analogy created by KB authors, not from source. Should be in Interpretacao section.

### SPECULATIONS:

- None identified.

### POTENTIAL ERRORS:

- **"4-Layer Compaction Hierarchy" ordering.** Wiki presents microcompaction as layer 1 (lightest) and snip as layer 2, claiming they are "triggered in order." However, the raw source's query loop lists the order as "snip, microcompact, context collapse" — putting snip BEFORE microcompact. The wiki's numbering contradicts the source's execution order.
- **"Triggered in order" framing.** The raw source describes these as separate mechanisms applied during the query loop, not as a progressive cascade where each triggers the next. The hierarchical framing is a KB construction.

---

## 2. memory-consolidation.md

**Sources:** raw/articles/claude-code-internals-harness-engineering.md, raw/articles/dream-memory-consolidation-skill.md

### FACTS (verified):

- "KAIROS running as a forked subagent" → confirmed (raw: "background memory consolidation agent that runs as a forked subagent")
- "Trigger Gates — Time-based: default 24h" → confirmed
- "Session-based: minimum sessions since last run (default 5)" → confirmed
- "Lock-based: file locks prevent concurrent consolidation" → confirmed
- "Scan throttling: every 10 minutes" → confirmed
- "4-Phase Dream Cycle: Orient, Gather, Consolidate, Prune" → confirmed in both sources
- "Bash restricted to read-only operations" → confirmed (raw lists: ls, find, grep, cat, stat, wc, head, tail)
- "File writes go through standard Edit/Write tools only" → confirmed
- "4 Memory Types: User, Feedback, Project, Reference" → confirmed in both sources
- "MEMORY.md (~25KB max) serves as the table of contents" → confirmed
- "Sonnet-powered relevance selector scans up to 200 memory files and returns the 5 most relevant" → confirmed
- "Demand-driven, not static" → confirmed
- "Deliberate Exclusions: code patterns, architecture, file paths, git history, debugging solutions" → confirmed in both sources
- "Dream is a standalone open-source implementation of KAIROS auto-dreaming" → confirmed (Dream: "standalone open-source implementation of the KAIROS auto-dreaming subsystem")
- "KAIROS runs automatically via gates; Dream is manually invoked via /dream" → confirmed
- "Enhanced mode (--memory): proactive memory saving during normal work" → confirmed
- "KAIROS is internal to Claude Code; Dream is a one-file skill anyone can install" → confirmed (Dream: "Installs one file: ~/.claude/skills/dream/SKILL.md")

### INTERPRETATIONS:

- "define the current state of the art" → editorial claim by KB, not from sources

### SPECULATIONS:

- None identified.

### POTENTIAL ERRORS:

- **KAIROS scope reduction.** Wiki says "KAIROS is Claude Code's internal mechanism for background memory consolidation." Raw source says "KAIROS is an alternate UX mode where Claude functions as a long-lived autonomous agent persisting across sessions. The most concrete subsystem is auto-dreaming." KAIROS is a broader UX mode; auto-dreaming/memory consolidation is just one subsystem. The wiki incorrectly equates KAIROS with memory consolidation specifically.
- **Index entry description.** Wiki says MEMORY.md contains "only pointers (~150 chars per entry), not content." The raw source says "MEMORY.md (~25KB max) serves as table of contents loaded into every conversation" but does NOT specify "~150 chars per entry." The 150-char detail appears to come from the KB's own CLAUDE.md rules for _index.md, not from the KAIROS source. This is a cross-contamination of the KB's own design rules into a factual description of KAIROS.

---

## 3. multi-agent-orchestration.md

**Sources:** raw/articles/claude-code-internals-harness-engineering.md, raw/papers/deep-research-survey-autonomous-agents.md

### FACTS (verified):

- "CLAUDE_CODE_COORDINATOR_MODE=1 transforms Claude Code into a multi-agent orchestrator" → confirmed
- "Never write 'based on your findings'" → confirmed
- "coordinator must synthesize worker research into specific specs with file paths, line numbers" → confirmed
- "4-Phase Workflow: Research, Synthesis, Implementation, Verification" → confirmed
- "Workers push `<task-notification>` XML messages on completion. Coordinator never polls." → confirmed
- "Concurrency rules" (read-only parallel, write-heavy serial, verification alongside) → confirmed
- "Continue vs. Spawn Decision" table → all 5 rows confirmed against source
- "Three isolation levels: Default, Worktree, Remote (CCR)" → confirmed
- "Task IDs: base-36 encoding with type prefixes (b=bash, a=agent, r=remote)" → confirmed
- "Lock retries: 30 attempts with 5-100ms backoff (~2.6s max wait)" → confirmed
- Single-agent examples (DeepResearcher, WebThinker, Search-R1) → confirmed in survey
- Multi-agent examples (AgentRxiv, AI Scientist, OpenResearcher) → confirmed in survey

### INTERPRETATIONS:

- "The Deep Research Pipeline Parallel" section mapping survey stages to Coordinator Mode phases → KB-created analogy, neither source draws this parallel
- "The convergence suggests this is a fundamental pattern for agent coordination, not specific to code or research" → pure KB editorial, not in any source
- Despite these, article claims "Nenhuma interpretacao significativa"

### SPECULATIONS:

- None beyond the interpretations above.

### POTENTIAL ERRORS:

- **The 4-stage mapping is misleading.** Wiki maps "Web Exploration → Implementation (gathering)" and "Report Generation → Verification (output)." In the survey, Web Exploration is information retrieval (search/browse), not implementation. Report Generation is synthesizing a report, not verifying code. The analogy is forced and could mislead readers into thinking the survey endorses this mapping.
- **"Context pollution" as single-agent weakness.** Wiki table lists "context pollution, sequential bottleneck" as single-agent weaknesses. The survey describes single-agent advantage as "integrated end-to-end learning" but does NOT use the term "context pollution." This term comes from the Claude Code coordinator source (about wrong context polluting retries). The wiki cross-contaminates sources and presents the result as a factual taxonomy.
- **"Context isolation" as multi-agent weakness.** The survey does not list "context isolation" as a multi-agent weakness. This term appears borrowed from Claude Code's isolation modes. The survey mentions advantages ("independent optimization, parallelism, flexibility") but the stated weaknesses in the wiki are KB constructions.

---

## 4. hybrid-search.md

**Source:** raw/articles/qmd-query-markup-documents.md

### FACTS (verified):

- Hybrid pipeline diagram → matches raw source exactly
- "Query Expansion → 2 alternative queries" → confirmed
- "Original Query (x2 weight)" → confirmed
- "RRF Fusion (k=60)" → confirmed
- "Top-rank bonus: +0.05/#1, +0.02/#2-3" → confirmed
- "Top 30 → LLM Re-ranking (qwen3-reranker, yes/no + logprobs)" → confirmed
- "Position-Aware Blend" percentages → confirmed exactly
- Score normalization table → confirmed exactly
- "~900-token pieces with 15% overlap" → confirmed
- Break point scores → confirmed (raw: "headings: 100-50, code fences: 80, horizontal rules: 60, blank lines: 20, list items: 5")
- "Code fence protection" → confirmed
- AST-Aware Chunking with tree-sitter, supported languages → confirmed
- GGUF models table (all three) → confirmed exactly
- "Auto-downloaded, cached in ~/.cache/qmd/models/" → confirmed
- Integration modes (CLI, MCP Server, SDK, HTTP) → confirmed
- MCP tools (query, get, multi_get, status) → confirmed

### INTERPRETATIONS:

- "Design insight: Pure RRF can dilute exact matches when expanded queries don't match" → KB editorial, not stated in source
- "For our KB, QMD represents the Fase 2-3 upgrade path when _index.md flat retrieval hits its limits (~200 articles)" → KB editorial planning

### SPECULATIONS:

- None identified.

### POTENTIAL ERRORS:

- **Heading break point score order.** Wiki says "Headings: 50-100 (H6-H1)." Raw source says "headings: 100-50." Same range expressed differently — wiki implies H6=50 ascending to H1=100 while raw lists high-to-low. Not technically wrong but the inverted presentation could confuse.
- **"No cloud dependency" claim.** Wiki states all models run locally with "No cloud dependency." Raw source says models are "auto-downloaded from HuggingFace." There IS a cloud dependency for initial download. The claim is misleading for first-run scenarios.
- **"QMD is the tool Elvis (@omarsar0) uses to index his research paper collection."** This claim cites the elvis-personal-kb-agents.md source, not the QMD source. The QMD source does not mention Elvis at all. Cannot verify this claim against the assigned source.

---

## 5. autonomous-research-agents.md

**Source:** raw/papers/deep-research-survey-autonomous-agents.md

### FACTS (verified):

- "4-stage pipeline: planning, question developing, web exploration, report generation" → confirmed
- Planning key approaches (WebDreamer, WebPilot, AgentSquare, MindSearch, SimpleDeepSearcher) → confirmed
- "Plans lack robustness to ambiguous questions. Hallucinated steps propagate errors downstream" → confirmed
- Two paradigms: Reward-optimized and Supervision-driven → confirmed
- Reward-optimized examples (DeepResearcher, Search-R1, ZeroSearch) → confirmed
- "Format rewards enforce syntax; answer rewards (F1-based) improve relevance" → confirmed
- Supervision-driven examples (ManuSearch, Search-o1) → confirmed
- "Multi-agent systems with separate planning, searching, extraction agents" → confirmed
- "More controllable but limited by demonstration quality" → confirmed
- Web exploration categories (Browser-based, Multimodal, API-based) → confirmed
- "WebVoyager (59% task success with GPT-4V)" → confirmed
- Commercial systems table → all 4 entries confirmed
- Benchmarks table → confirmed
- 5 Open Challenges → all 5 match survey's Technical Challenges
- Report generation: structure control and factual integrity → confirmed
- "Most methods optimize single stages, not the full pipeline" → confirmed

### INTERPRETATIONS:

- Karpathy quote and connection to deep research → from a different source (karpathy-llm-knowledge-bases.md), not the survey. The link between them is KB editorial.
- "An LLM knowledge base is a persistent instance of what deep research agents do ephemerally" → KB editorial synthesis, not from either source.
- Despite these, article claims "Nenhuma interpretacao significativa."

### SPECULATIONS:

- None identified.

### POTENTIAL ERRORS:

- **Incomplete characterization of Question Developing challenges.** Wiki says "Generated queries are too narrow for open-ended problems" as THE open challenge. Raw survey lists THREE challenges: (1) over-reliance on subgoal clarity, (2) lack of contextual coherence / repetitive questions, (3) overly narrow queries for open-ended problems. The wiki cherry-picks one and omits two.
- **Perplexity DeepResearch infrastructure.** Wiki says "Bing-style index + Sonar API." Raw source says the same. Confirmed — no error.
- **Article self-classification as purely factual** is incorrect given the Karpathy-survey connection and "persistent instance" claim are interpretive.

---

## 6. obsidian-agent-workflow.md

**Sources:** raw/articles/kepano-obsidian-agent-workflow.md, raw/articles/karpathy-llm-knowledge-bases.md

### FACTS (verified):

- "Local-first: all data is plain markdown files on disk" → confirmed (Kepano: "local-first markdown editor")
- "Human-first philosophy" quote → confirmed exactly in Kepano source
- The Four Pieces (Obsidian app, Web Clipper, CLI, Skills) → confirmed exactly
- Reference URL https://obsidian.md/help/headless → confirmed
- Vault Separation quotes → confirmed exactly
- Karpathy uses Obsidian as IDE frontend → confirmed
- Karpathy uses Web Clipper → confirmed
- Karpathy uses Marp for slides → confirmed
- Karpathy uses hotkey for image download → confirmed

### INTERPRETATIONS:

- "Obsidian is emerging as the default frontend/IDE for LLM-compiled knowledge bases" → KB editorial; "default" is extrapolated from only 3 practitioners
- "Three independent practitioners converge on the same setup" → they may not be independent (Kepano explicitly references Karpathy: "I like @karpathy's Obsidian setup")
- "An [[llm-knowledge-base]] like this one is the 'agent vault'" → KB self-referential editorial
- Despite these, article claims "Nenhuma interpretacao significativa"

### SPECULATIONS:

- None identified.

### POTENTIAL ERRORS:

- **"Graph view: visual exploration of concept connections."** Neither Kepano nor Karpathy sources mention graph view. This is a general Obsidian feature presented as part of the workflow without source support.
- **"Plugin ecosystem: Marp for slides, Web Clipper for ingestion, community plugins for visualization."** Karpathy mentions Marp and "a few Obsidian plugins to render and view data" but does not say "community plugins for visualization" specifically. Minor embellishment.
- **"Kepano (CEO of Obsidian) endorses vault separation as the recommended pattern."** Kepano expresses personal preference ("I prefer," "I like") on X/Twitter. Calling it "the recommended pattern" implies official Obsidian guidance. The source is personal opinion, not an official recommendation.
- **"Three independent practitioners converge."** Kepano explicitly references Karpathy ("I like @karpathy's Obsidian setup"), so they are not independent. The convergence framing is factually inaccurate.
- **Elvis column claims.** "MD vaults for research papers. Visual artifact generator with MCP tools. Interactive data views." These are attributed to the Elvis source (raw/articles/elvis-personal-kb-agents.md) which was NOT in scope for this audit. Cannot verify these specific claims against the two assigned sources.

---

## Summary of Critical Findings

### Most concerning POTENTIAL ERRORS:

1. **context-management.md**: The "4-Layer Hierarchy" ordering (microcompact first, snip second) contradicts the raw source's query loop ordering (snip, microcompact, context collapse). The sequential cascade framing is unsupported.

2. **memory-consolidation.md**: KAIROS is reduced to "memory consolidation mechanism" when the source describes it as a broader "alternate UX mode." The "~150 chars per entry" detail for MEMORY.md is not from the KAIROS source — it's from the KB's own CLAUDE.md rules, cross-contaminated into a factual claim.

3. **multi-agent-orchestration.md**: The Deep Research Pipeline Parallel table is a KB-created analogy presented as fact in the Conteudo section. "Context pollution" and "context isolation" as taxonomy terms are cross-sourced from Claude Code docs, not from the survey.

4. **hybrid-search.md**: "No cloud dependency" is misleading — initial model download requires HuggingFace access.

5. **autonomous-research-agents.md**: Question Developing challenges are incomplete (1 of 3 listed). Karpathy connection is interpretive but presented as factual.

6. **obsidian-agent-workflow.md**: Practitioners are NOT independent (Kepano cites Karpathy). "Recommended pattern" overstates a personal preference. Graph view and community plugins lack source support.

### Cross-cutting issue:

Articles 3, 5, and 6 all claim "Nenhuma interpretacao significativa" in their Interpretacao section, yet each contains substantive interpretations in the Conteudo section. Per the KB's own CLAUDE.md rules, these should be prefixed with "(warning) nossa interpretacao" or moved to the Interpretacao section.
