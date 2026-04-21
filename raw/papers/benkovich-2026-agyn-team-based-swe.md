# Agyn: A Multi-Agent System for Team-Based Autonomous Software Engineering

**arXiv:** 2602.01465  
**Authors:** Nikita Benkovich, Vitalii Valkov (Agyn; Mila – Quebec AI Institute)  
**Published:** 2026-02  
**Categories:** cs.SE, cs.AI

## Abstract

Most autonomous SWE systems treat issue resolution as monolithic or pipeline-based. Real software development is organized as collaborative team activity with role separation, communication, and review. This paper presents a fully automated multi-agent system that models software engineering as an organizational process — replicating the structure of an engineering team.

**SWE-bench 500 result: 72.2%** (without benchmark-specific tuning; production-deployed system).

## Architecture: GitHub-Native Team Workflow

### Four specialized roles
- **Manager**: coordination, process control, decides which agent to invoke next, applies development methodology
- **Researcher**: issue understanding, repository exploration, root cause analysis, produces task specifications
- **Engineer**: implementation, code modification, test execution, iterative refinement
- **Reviewer**: evaluates changes via PR review, leaves inline comments, approves or requests changes

### PR-centric completion protocol
**A task is considered complete only when the pull request is explicitly approved by the reviewer agent.**

This is the key design choice for PR creation orchestration:
1. Engineer opens PR against task-specific base branch
2. Reviewer inspects diff, leaves inline review comments
3. Engineer iterates on feedback
4. Reviewer approves → task complete

All coordination is mediated through GitHub artifacts (issues, PRs, reviews) — not through private inter-agent messages.

### Role-specific model allocation
- Manager + Researcher: GPT-5 (large, general-purpose — reasoning-heavy tasks)
- Engineer + Reviewer: GPT-5-Codex (smaller, code-specialized — iterative execution tasks)

This reflects production constraints: different roles have different compute profiles.

### GitHub tooling
- Primary: `gh` CLI (compact, human-oriented output vs. API metadata bloat)
- Custom extension: `gh-pr-review` for inline review reading/authoring
- Agents have separate GitHub accounts to appear as distinct contributors

### Context management
- Large shell outputs (>50K tokens) auto-redirected to file; agent receives file reference
- Automatic context summarization when accumulated history reaches threshold
- Earlier context replaced with compact representation preserving key decisions

## Key Design Principles for Zero-HI Pipeline

1. **PR as acceptance signal** — not a natural language "done" message; must be machine-verifiable
2. **Separation of finish tool from send_message** — prevents conversational behaviors from signaling premature completion
3. **Automation-first prompting** — explicitly discourage "ask for approval" behaviors in all agent prompts
4. **Manager controls loop termination** — must invoke explicit `finish` tool; non-functional output triggers continuation

## Production vs. Benchmark Tension

System designed for production (not benchmark-tuned). Key tensions identified:
- Legacy dependency failures dominate some trajectories (benchmark infrastructure drift)
- Over-engineering: agents improve test coverage/linting beyond minimal benchmark patch
- Long-running tests cause tool timeout; agents adapt with subset execution

## Results

| System | Model | SWE-bench 500 |
|---|---|---|
| agyn | GPT-5 / GPT-5-Codex | **72.2%** |
| OpenHands | GPT-5 | 71.8% |
| mini-SWE-agent | GPT-5.2 high reasoning | 71.8% |
| mini-SWE-agent | GPT-5 medium | 65.0% |

7.4% improvement over mini-SWE-agent baseline under comparable models.

## Relation to KB

- PRIMARY source for "pr-creation-orchestration" concept
- Concrete PR protocol: PR opened → reviewer approves → task complete (not verdict string)
- VALIDATES externalization-agent-infrastructure: roles = externalized skills; GitHub = externalized protocol; PR review loop = externalized coordination structure
- REFINES claude-code-architecture-analysis: worktree-per-agent + GitHub-native workflow extends Claude Code's worktree isolation pattern to multi-agent settings
- REFINES agentic-coding-failure-taxonomy: role specialization addresses heterogeneous task requirements that overwhelm single-agent setups
