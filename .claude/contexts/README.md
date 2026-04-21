# contexts/ — Project Context Protocol

Each file here wires a real-world project into METAXON's /ask command.

## Structure

```
contexts/
  <project>.yaml     # gate criteria + implementation state + output paths
```

## How /ask uses these

When a /ask session touches articles in a project-adjacent cluster,
/ask reads the project's `.yaml` for implementation state before synthesizing.
This prevents suggesting features that already exist, or treating planned
features as deployed.

## How to add a new project

1. Copy the zelox.yaml structure as template
2. Define `gate_criteria` — what data/actions are available in this project?
3. Add `implementation_state` — what's deployed, pending, blocked?
4. Define which KB index clusters are "project-adjacent" (in ask.md Gatilhos)
5. Create `scripts/gen-context.py` in the project to auto-update `implementation_state`
   and write `raw/notes/<project>-codebase-snapshot.md`

## Minimal template

```yaml
name: my-project
description: "One-line description for /prioritize"

gate_criteria:
  dados_disponiveis:
    description: "What data/APIs does this project have access to?"
    sources_available: [...]
    fail_condition: "..."

  consequencia_acionavel:
    description: "What actions can KB insights drive?"
    acceptable_actions: [...]
    fail_condition: "..."

implementation_state:
  deployed_features: [...]
  pending_features: [...]
  key_files:
    main_entry: "src/..."

output:
  priority_report: "outputs/reports/priority-<project>-{date}.md"
```

## gen-context.py pattern

Each project has `scripts/gen-context.py` that:
1. Reads key source files via AST
2. Extracts feature keys, class names, deployed logic
3. Writes `llm-kb/raw/notes/<project>-codebase-snapshot.md`
4. Triggered via `make context`

The snapshot is the authoritative source of truth for implementation state.
The `.yaml` has stable gate criteria; the snapshot has volatile code state.
