# Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

**arXiv:** 2604.08224  
**Authors:** Chenyu Zhou et al. (21 authors, Weinan Zhang group)  
**Published:** 2026-04-09  
**Categories:** cs.SE, cs.MA

## Abstract

LLM agents are increasingly built by reorganizing the runtime around models rather than changing weights. This paper reviews the shift through "externalization" — capabilities expected internally are now externalized into memory stores, reusable skills, interaction protocols, and surrounding harness. Framework: memory externalizes state, skills externalize procedural expertise, protocols externalize interaction structure, harness engineering unifies into governed execution.

## Core Framework: Externalization as Organizing Principle

**Historical parallel**: human cognitive externalization (speech → writing → printing → digital) mirrors agent externalization (weights → context → harness).

### 3 Forms of Externalization

**1. Memory** — externalizes state across time
- Turns recall into retrieval
- Types: episodic, semantic, procedural, working memory
- Key challenge: decay policy (what to forget vs. persist)

**2. Skills** — externalizes procedural expertise
- Turns improvised generation into guided composition
- Reusable, composable, inspectable
- Key challenge: skill discovery and invocation

**3. Protocols** — externalizes interaction structure
- Turns ad hoc coordination into structured exchange
- Includes: tool-use protocols, multi-agent communication, human-agent interaction patterns
- Key challenge: protocol negotiation and evolution

### Harness Engineering: The Unification Layer
- Coordinates memory + skills + protocols into governed execution
- "The harness is not just infrastructure — it changes the task the model is being asked to solve"
- Properties: persistent, inspectable, reusable, governable
- Trend: self-evolving harnesses (harness updates itself based on agent performance)

## Historical Progression: Weights → Context → Harness

| Layer | What changes | Example |
|---|---|---|
| Weights | Model training | Fine-tuning, RLHF |
| Context | What's in the window | RAG, memory injection, tool results |
| Harness | Runtime organization | Hooks, MCP, skills, session management |

Most research has migrated progressively outward toward harness.

## Key Claims

- **Representational transformation**: externalization doesn't just add components — it changes what the model is asked to solve
  - Memory: recall → retrieval
  - Skills: improvised generation → guided composition
  - Protocols: ad hoc coordination → structured exchange
- **Parametric vs. externalized trade-off**: some burdens remain well handled in weights; others become more reliable once externalized
- **Evaluation gap**: no standard way to measure contribution of externalized systems independently from model capability

## Emerging Directions

1. **Self-evolving harnesses** — harness updates based on agent failure patterns (connects to EAGER/ERL)
2. **Shared agent infrastructure** — multiple agents share skills, memory, protocols (connects to multi-agent coordination)
3. **Governance of externalized artifacts** — who controls/audits the harness?

## Open Challenges

- How to partition capability between model and infrastructure?
- How to evaluate externalized systems independently?
- How to govern shared artifacts?
- Long-term co-evolution of models and external infrastructure

## Relation to Existing KB

- Subsumes and provides theoretical grounding for: agent-memory-architectures, natural-language-agent-harness, codified-context-codebase-agents, file-as-bus-workspace
- Provides vocabulary: "externalization" as the unified concept
- Connects harness evolution to self-improving agents (self-evolving harnesses = ERL applied to harness)
