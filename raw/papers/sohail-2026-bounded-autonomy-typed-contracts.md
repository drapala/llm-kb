# Bounded Autonomy for Enterprise AI: Typed Action Contracts and Consumer-Side Execution

**arXiv:** 2604.14723  
**Authors:** Sarmad Sohail, Ghufran Haider  
**Published:** 2026-04-16  
**Categories:** cs.SE, cs.AI  
**Note:** PDF conversion unavailable — summary from abstract only

## Abstract

LLMs used as natural-language interfaces to enterprise software remain unsafe as direct system operators. Model errors propagate into unauthorized actions, malformed requests, cross-workspace execution. This is primarily an execution architecture problem, not a model capability problem.

## Bounded-Autonomy Architecture

Key principles:
1. **Typed action contracts** — all executable behavior constrained by schema
2. **Permission-aware capability exposure** — only permitted actions surfaced to model
3. **Scoped context** — model sees only relevant workspace
4. **Validation before side effects** — all actions validated before execution
5. **Consumer-side execution boundaries** — enterprise app remains source of truth for business logic
6. **Optional human approval** — escalation mechanism for high-risk actions

**Published actions manifest**: orchestration engine operates over explicit declared actions (not arbitrary tool use).

## Results (25 Scenarios, 7 Failure Families, Multi-Tenant Enterprise App)

| Condition | Tasks completed | Unsafe executions |
|---|---|---|
| Manual operation | baseline | 0 |
| Unconstrained AI (safety disabled) | 17/25 | multiple |
| Bounded autonomy (full) | **23/25** | **0** |

- 13-18x speedup over manual operation (both AI conditions)
- **Counter-intuitive finding**: removing safety layers made system LESS useful — structured validation feedback guided model to correct outcomes in fewer turns; unconstrained system hallucinated success
- Wrong-entity mutations: only disambiguation + confirmation mechanisms intercept this failure class (not structural enforcement)
- Several safety properties enforced by code structure: intercepted all targeted violations regardless of model output

## Key Insight

"Structured validation feedback guided the model to correct outcomes in fewer turns, while the unconstrained system hallucinated success."

Safety constraints improve task completion, not just safety. The model uses validation errors as feedback to self-correct.

## Implications

- Enforcement by code structure (not prompts) is the most reliable safety mechanism
- Typed contracts reduce model hallucination by constraining the output space
- Consumer-side execution = enterprise app remains authoritative (model is interpreter, not executor)
- Published actions manifest = explicit capability registry (analogous to MCP tool list)

## Relation to KB

- CONFIRMS agentic-codebase-enforcement-patterns: enforcement by code > enforcement by prompt
- EXTENDS codified-context-codebase-agents: typed action contracts = formalized version of CLAUDE.md boundary constraints
- CONFIRMS liu-2026-claude-code-design-space: permission system + ML classifier = instantiation of typed contract enforcement
- NEW: "safety as feedback" — constraints help model converge, not just restrict
