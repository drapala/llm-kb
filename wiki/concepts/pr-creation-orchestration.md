---
title: "PR Creation Orchestration in Agentic SWE Pipelines"
sources:
  - path: raw/papers/benkovich-2026-agyn-team-based-swe.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-19
updated: 2026-04-19
tags: [agents, pull-request, orchestration, swe, github, multi-agent, production]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
reads: 1
retrievals_correct: 1
retrievals_gap: 0
freshness_status: current
quarantine: false
quarantine_promoted: 2026-04-18
quarantine_criteria_met:
  auto_promote: true
  gates_passed: [1, 2, 3, 4]
  gate3_skipped: staleness
  challenge_verdict: PUBLICÁVEL
topics: [pr-creation, github-workflow, multi-agent, role-specialization, agentic-coding]
depends_on: []
---

## Resumo

O Agyn (Benkovich & Valkov, arXiv 2602.01465, produção-deployed) documenta o padrão de PR como acceptance signal em pipelines autônomos: **uma task só é considerada completa quando o PR é explicitamente aprovado por um reviewer agent** — não quando o agente emite uma mensagem de conclusão. 72.2% SWE-bench 500 sem tuning específico de benchmark, via workflow GitHub-nativo com 4 roles especializados.

## Conteúdo

### O problema: "done" não é verificável por texto

Pipelines single-agent encerram quando o agente emite `STATUS: stage_complete` ou equivalente. Isso é auto-report — não há verificação externa de que o trabalho satisfaz os requisitos. O PR como acceptance signal resolve isso: o reviewer agent inspeciona o diff e aprova ou solicita mudanças, criando um critério de completude **observável e verificável externamente**.

### Arquitetura: 4 roles + GitHub-native workflow

**Agyn** configura uma equipe de 4 agentes especializados:

| Role | Responsabilidade | Modelo |
|---|---|---|
| Manager | Coordenação, controle de processo, metodologia | GPT-5 (large) |
| Researcher | Análise da issue, exploração do repo, task specification | GPT-5 (large) |
| Engineer | Implementação, testes, refinamento iterativo | GPT-5-Codex (code-specialized) |
| Reviewer | Inspeção do diff via PR review, approve/request-changes | GPT-5-Codex |

**Resultado SWE-bench 500:** 72.2% (vs. mini-SWE-agent+GPT-5: 65.0%; OpenHands+GPT-5: 71.8%)

### Protocolo de completion via PR

1. Engineer cria branch com task identifier no nome
2. Engineer abre PR contra base branch específica do ticket
3. Reviewer lê diff via `gh pr review` + `gh-pr-review` (extensão customizada para inline reviews)
4. Reviewer deixa inline comments se encontrar problemas → Engineer itera
5. Reviewer aprova → Manager invoca `finish` tool → task completa

**Invariante:** a task NÃO é completa até que o PR esteja aprovado. O manager é proibido de invocar `finish` sem aprovação do reviewer.

### Separação finish/send_message

Problema identificado: LLMs fine-tuned para interação conversacional tendem a emitir mensagens de "pronto" mesmo sem completar o trabalho. Solução:

- `send_message` tool: comunicação de status/progresso, **não** sinal de completude
- `finish` tool: invocação exclusiva pelo manager quando PR aprovado
- Manager que produz output não-funcional (texto em vez de tool call) recebe instrução forçando continuação

Essa separação previne "hallucination of completion" — o failure mode mais frequente em pipelines autônomos.

### Automação-first prompting

Comportamentos incompatíveis com pipelines autônomos (e como são prevenidos):

| Comportamento indesejado | Prevenção |
|---|---|
| "Posso prosseguir com X?" | Prompts enfatizam autonomous task completion |
| "Planejo fazer X, confirma?" | Acceptance criteria objetivos no nível do sistema |
| Output textual em vez de tool call | Sistema responde com instrução de continuação |
| Pedir aprovação antes de commit | Apenas o reviewer agent tem veto |

### Role-specific model allocation

A escolha de modelos diferentes por role reflete restrições de produção:
- Reasoning-heavy (Manager, Researcher): modelos maiores, contexto maior
- Execution-heavy (Engineer, Reviewer): modelos menores especializados em código, ciclos rápidos

Isso é explicitamente análogo à separação Expert-Executor de Liu 2025 (agentic-coding-failure-taxonomy): tarefas heterogêneas requerem configurações de agente diferentes.

### Tooling GitHub-native

**Lição aprendida:** GitHub API raw retorna metadata volumoso que infla o contexto e degrada performance em workflows de review. A troca para `gh` CLI (output compacto, human-oriented) melhorou performance especialmente em review-heavy tasks.

**Extensão customizada:** `gh-pr-review` — expõe interface compacta para ler review threads e submeter inline comments. Sem isso, agents não conseguem participar plenamente do loop de PR review iterativo.

### Context management para runs longos

Agyn implementa summarização automática de contexto:
- Quando accumulated history atinge threshold: earlier context → compact summary
- Summary preserva key decisions, artifacts, status do plano
- Outputs de shell >50K tokens: redirecionados para arquivo; agent recebe referência

Isso é implementação do princípio de compactação documentado em claude-code-architecture-analysis (5-layer pipeline).

### Limitações identificadas em produção

1. **Infrastructure drift:** SWE-bench tasks de repositórios antigos têm dependências legacy que falham (CI deprecated, Python versions antigas). Agentes gastam context tentando corrigir isso.
2. **Over-engineering:** agentes melhoram test coverage/linting além do que o benchmark exige → patches corretos funcionalmente mas divergem do gold patch minimal.
3. **Long-running tests:** time limits causam terminação prematura; agentes adaptam com subset execution.

## Verificação adversarial

**Claim mais fraco:** 72.2% foi medido em SWE-bench 500 (subset) com o sistema rodando em MacBook Pro (resource constraints). Performance em produção com escala e infra adequada pode diferir.

**O que o paper NÃO diz:**
1. Não mede custo por ticket resolvido (tokens + latência do loop multi-agent)
2. Não compara com single-agent equivalente no mesmo hardware/budget
3. Não documenta taxa de falha do reviewer agent (approvals incorretos que passam código defeituoso)

**Simplificações:** o sistema usa contas GitHub separadas por agente — isso adiciona overhead de setup que não está documentado. Em ambientes de produção real sem controle do repo, criar contas separadas pode não ser viável.

**Prior work:** SWE-agent (Yang et al. 2024), OpenHands (Wang et al. 2024), TRAE, Prometheus.

## Interpretação

(⚠️ nossa interpretação) O padrão PR-como-acceptance-signal é diretamente aplicável ao claude-pipeline: substituir `verdict=approve` (string auto-report) por "PR aprovado por reviewer agent" como condição de completude. Isso requer: (1) `git push` habilitado após todos os stages aprovados pelo critic; (2) `gh pr create` com body gerado; (3) reviewer agent opcional que inspeciona o diff final antes de sinalizar conclusão.

(⚠️ nossa interpretação) A separação `finish`/`send_message` mapeia para a distinção entre `STATUS: stage_complete` (sinal de completude) e qualquer output informativo intermediário do agente. A lição é que o orchestrator não deve confiar em texto livre do agente para determinar completude — só em sinais estruturados verificáveis.

## Conexões

- validates: [[externalization-agent-infrastructure]] ON "Protocols externalizam estrutura de interação: o loop PR→review→approve é protocol externalizado que governa quando o trabalho está completo"
- refines: [[claude-code-architecture-analysis]] ON "worktree isolation por agente + GitHub-native workflow estende o padrão de worktree do Claude Code para coordenação multi-agente"
- refines: [[agentic-coding-failure-taxonomy]] ON "role specialization (Manager/Researcher/Engineer/Reviewer) como resposta arquitetural a tarefas heterogêneas que overwhelm single-agent setups"
- validates: [[agentops-mas-failure-management]] ON "failure concentration: reviewer agent como gate específico para classe de falhas de 'completion hallucination'"

## Fontes

- [Benkovich & Valkov 2026 — Agyn (arXiv 2602.01465)](../../raw/papers/benkovich-2026-agyn-team-based-swe.md) — 72.2% SWE-bench 500; PR-centric protocol; automation-first design; produção-deployed

## Quality Gate

- [x] Wikilinks tipados: 4 (validates×2, refines×2)
- [x] Instance→class: 72.2% atribuído a Agyn/SWE-bench 500; todos os comparativos com contexto de modelo
- [x] Meta-KB separado: interpretações sobre claude-pipeline na seção Interpretação
- [x] Resumo calibrado: limitação de SWE-bench 500 (subset) e MacBook documentadas
