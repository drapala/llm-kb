# Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems

**arXiv:** 2604.14228  
**Authors:** Jiacheng Liu, Xiaohan Zhao, Xinyi Shang, Zhiqiang Shen (VILA-Lab)  
**Published:** 2026-04-14  
**Categories:** cs.SE, cs.AI, cs.CL, cs.LG  
**GitHub:** https://github.com/VILA-Lab/Dive-into-Claude-Code

## Abstract

Analysis of Claude Code's publicly available TypeScript source (v2.1.88) and comparison with OpenClaw. Identifies 5 human values → 13 design principles → specific implementation choices. Describes the complete architectural landscape of the system.

## 5 Human Values

1. **Human decision authority** — model proposes, human approves high-stakes actions
2. **Safety and security** — per-action ML classification, graduated permission modes
3. **Reliable execution** — deterministic harness around non-deterministic model
4. **Capability amplification** — tools, MCP, extensibility mechanisms
5. **Contextual adaptability** — hooks, skills, session recovery

## Core Architecture: While-Loop + Dense Harness

The core is simple: `while(true) { call_model(); run_tools(); }`. Most code lives in systems AROUND this loop:

### Permission System
- 7 modes (from fully manual to fully autonomous)
- ML-based classifier for per-action safety evaluation
- Graduated trust: some actions always allowed, some always require approval, most context-dependent

### Context Management (5-Layer Compaction Pipeline)
- Layer 1: Raw context accumulation
- Layer 2: Tool output compression
- Layer 3: Conversation summarization
- Layer 4: Long-term session compression
- Layer 5: Cross-session memory (append-oriented session storage)

### Extensibility (4 Mechanisms)
- **MCP**: external tools/servers
- **Plugins**: first-party extensions
- **Skills**: reusable agent workflows
- **Hooks**: event-triggered automation

### Delegation
- Subagent dispatch mechanism
- Worktree isolation (each subagent in separate git worktree)
- Orchestration at agent level, not just tool level

### Storage
- Append-oriented session storage (never overwrites, always appends)
- Enables session recovery and replay

## Comparison: Claude Code vs OpenClaw

Same design questions, different answers by deployment context:

| Design Question | Claude Code | OpenClaw |
|---|---|---|
| Safety model | Per-action ML classification | Perimeter-level access control |
| Execution model | Single CLI while-loop | Embedded runtime in gateway control plane |
| Extensibility | Context-window extensions (MCP, hooks) | Gateway-wide capability registration |
| Composition | Can be hosted by OpenClaw via ACP | Multi-channel gateway hosting CC |

## 6 Open Design Directions (Future Agent Systems)

1. **Human capability preservation** — current systems provide limited mechanisms for long-term human understanding; sustainability gap as first-class design problem
2. **Codebase coherence** — agents can break architectural patterns; no mechanisms to enforce consistency
3. **Developer pipeline integration** — CI/CD, review, merge — agents operate outside these feedback loops
4. **Permission model evolution** — 7 modes are static; dynamic trust calibration
5. **Multi-agent coordination standards** — no standardized protocols for CC ↔ OpenClaw type compositions
6. **Evaluation methodology** — SWE-bench is insufficient for measuring long-term maintainability effects

## Key Finding

"The most consequential open question is not how to add more autonomy, but how to preserve human capability over time. The architecture provides limited mechanisms that explicitly preserve long-term human understanding, codebase coherence, or the developer pipeline."

## Implications

- Confirms: hooks + CLAUDE.md + MCP are the 4 extensibility mechanisms (not arbitrary)
- Confirms: worktree isolation is architectural, not just convenient
- Challenges: codebase coherence and pipeline integration are open problems (not solved by CLAUDE.md alone)
- New: ML-based per-action classifier is separate from explicit permission modes
