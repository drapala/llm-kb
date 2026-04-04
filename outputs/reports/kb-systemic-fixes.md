---
title: "KB Systemic Fixes Report"
date: 2026-04-04
---

# KB Systemic Fixes Report

## 1. ARTIGOS CORRIGIDOS

### Erros Factuais
| Artigo | Erro | Correção | Tipo |
|--------|------|----------|------|
| context-management | "4-Layer Hierarchy" ordering wrong (micro before snip) | Reordered per raw source: snip → microcompact. Removed "triggered in order" cascade framing. | ERRO FACTUAL |
| memory-consolidation | KAIROS equated with memory consolidation only | Corrected: KAIROS is broader UX mode; auto-dreaming is one subsystem. | SIMPLIFICAÇÃO EXCESSIVA |
| memory-consolidation | "~150 chars per entry" attributed to KAIROS | Noted: this is KB's own design rule, not from KAIROS source. Cross-contamination. | ERRO FACTUAL |
| hybrid-search | "No cloud dependency" | Corrected: initial download requires HuggingFace. Local after first run. | ERRO FACTUAL |
| autonomous-research-agents | Question Developing challenges: 1 of 3 listed | Added all 3 challenges from survey. | SIMPLIFICAÇÃO EXCESSIVA |
| obsidian-agent-workflow | "Three independent practitioners" | Corrected: Kepano explicitly references Karpathy. Not independent. | ERRO FACTUAL |
| obsidian-agent-workflow | "Recommended pattern" for vault separation | Corrected: personal preference ("I prefer"), not official recommendation. | SIMPLIFICAÇÃO EXCESSIVA |

### Erros Interpretativos
| Artigo | Erro | Correção | Tipo |
|--------|------|----------|------|
| multi-agent-orchestration | Deep Research Pipeline Parallel as fact | Moved to ## Interpretação, noted imprecise mapping. | ESPECULAÇÃO NÃO MARCADA |
| multi-agent-orchestration | "Context pollution" term from Claude Code attributed to survey | Corrected source attribution in Interpretação. | ERRO FACTUAL |
| tension-resolution | "52% degradation = self-reflection without grounded feedback" | Reframed: 52% is without TEST GENERATION on HumanEval. Raw/ verification is weaker grounding than unit tests. | SIMPLIFICAÇÃO EXCESSIVA |
| tension-resolution | "Five mechanisms" in resumo but 6 in body | Fixed: "Six mechanisms" | ERRO FACTUAL |
| raptor-vs-flat-retrieval | "exactly what RAPTOR does via clustering" | Reframed: RAPTOR uses statistical GMM; we use LLM judgment. Fundamentally different. | SIMPLIFICAÇÃO EXCESSIVA |
| raptor-vs-flat-retrieval | "LLM-guided concept extraction is more precise" | Reframed: untested claim, no source compares them. | ESPECULAÇÃO NÃO MARCADA |
| llm-as-judge | 16.1% used as universal constant | Qualified: Qwen2-specific worst case. Claude-3.5 most resilient. | SIMPLIFICAÇÃO EXCESSIVA |

### Cross-Cutting Fixes
| Fix | Articles Affected |
|-----|-------------------|
| 3 articles falsely claimed "Nenhuma interpretação significativa" | multi-agent-orchestration, autonomous-research-agents, obsidian-agent-workflow |
| 16.1% qualified as model-specific | llm-as-judge (primary), referenced in 5+ articles |
| "52% degradation" reframed as test-generation-specific | tension-resolution (primary), autonomous-kb-failure-modes |

## 2. ARTIGOS DE SÍNTESE COM ESTRUTURA EPISTÊMICA

| Artigo | Especulações não marcadas (pre-fix) | Severity |
|--------|-------------------------------------|----------|
| autonomous-kb-failure-modes | ~30 day timeline with no empirical basis, 4 mitigations untested, "KB reward hacking" analogy | ALTO — most speculation presented as observation |
| reflexion-weighted-knowledge-graphs | Entire concept is speculative, PoC tested 1 wikilink, credit assignment unsolved | ALTO — entire article is speculation |
| raptor-vs-flat-retrieval | Sub-indices as RAPTOR nodes, 50-80 article threshold, "QMD better at 200+" | MÉDIO — extrapolations from validated data |
| kb-architecture-patterns | "When to use" guidance, comparison matrix bottlenecks, Pattern 4 as "universal" | MÉDIO — framework is useful but unfounded |
| curation-anti-bias | All 5 improvements proposed, "5 consecutive confirming" threshold, 40/80 article limits | MÉDIO — prescriptions without empirical backing |
| tension-resolution | Resolution protocol, Known Tensions resolutions, "never force" heuristic | BAIXO — explicitly framed as design choices |

## 3. MECANISMOS ADICIONADOS

| Mecanismo | Implementado? | Arquivo |
|-----------|---------------|---------|
| /challenge command | SIM | .claude/commands/challenge.md |
| /ingest verificação adversarial (step 10) | SIM | .claude/commands/ingest.md |
| Níveis epistêmicos em synthesis articles | SIM (3 de 6) | autonomous-kb-failure-modes, reflexion-weighted-kg, raptor-vs-flat |

## 4. GAPS RESTANTES

### Verificação manual necessária
- kb-architecture-patterns: KAIROS reference not among cited sources — needs source addition or removal
- curation-anti-bias: needs Níveis epistêmicos section (not yet added)
- tension-resolution: needs Níveis epistêmicos section (not yet added)

### Cross-article systemic issues
- **"Relevance to Knowledge Bases" sections in raw/ files**: several raw/ sources contain KB-specific editorial mappings that wiki articles cite as if from the original papers. These sections should be marked as editorial in raw/ or removed.
- **ERL 40-60 threshold extrapolation**: used in 3+ articles as KB design basis but validated only for Gaia2 agent tasks. All derived thresholds (40 articles, 80 articles, 50-80 selection limit) are unvalidated.
- **16.1% figure**: qualified in llm-as-judge but still used unqualified in 5+ other articles. Full migration needed.

### Prior work not verified
- reflexion-weighted-knowledge-graphs: GNN with attention mechanisms may cover similar territory
- autonomous-kb-failure-modes: no empirical study of KB degradation rates exists
- All synthesis articles: "rodar /curate antes de publicar" — adversarial search not yet run specifically for synthesis claims
