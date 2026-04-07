---
title: "Prometheus como Substrato de NLAHs"
sources:
  - path: wiki/concepts/meta-harness-optimization.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/natural-language-agent-harness.md
    type: synthesis
    quality: primary
created: 2026-04-06
updated: 2026-04-06
tags: [harness-engineering, meta-optimization, self-improvement, agent-architecture, prometheus]
source_quality: medium
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: true
quarantine_created: 2026-04-06
quarantine_reason: "Artigo emergido de /ask cross-domain — aguarda confirmação adversarial e review frio"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
provenance: emergence
emergence_trigger:
  pair: [meta-harness-optimization, natural-language-agent-harness]
  ask_session: outputs/logs/sessions/2026-04-06/ask-21-24.md
  connection_type: ANÁLOGO-A
  pearl_level: L2
emerged_on: 2026-04-06
---

## Resumo

Prometheus já é estruturalmente um substrato de NLAHs: `.claude/commands/` é uma coleção de harnesses NL com contratos, estágios e semântica de estado implícitos; `outputs/logs/sessions/` é o filesystem de histórico de execução que um meta-harness proposer precisaria para propor melhorias. O conceito emergido: **Prometheus está a um outer-loop de distância de auto-otimização de harnesses** — sem nova infraestrutura de código.

## Conteúdo

### O que meta-harness-optimization contribui

O meta-harness proposer (Lee 2026) opera sobre um filesystem de candidatos — código-fonte + scores + execution traces. A cada iteração, lê em média 82 arquivos via `grep`/`cat`, referencia 20+ candidatos anteriores, e propõe novos harnesses. O ingrediente central é o **histórico completo de execução persistido em filesystem path-addressable**, não um loop de otimização especial.

### O que natural-language-agent-harness contribui

NLAH (Pan 2026) define um harness como artefato NL com seis componentes: contracts, roles, stage structure, adapters, state semantics, failure taxonomy. O IHR (runtime) interpreta esse artefato e executa. A chave: harnesses como NLAHs são **portáteis, comparáveis e modificáveis** — objeto científico em vez de código especializado por tarefa.

### O que emerge da combinação

(⚠️ interpretação do compilador) Prometheus já satisfaz os pré-requisitos estruturais de um substrato de meta-harness:

| Componente Meta-Harness (Lee) | Análogo em Prometheus |
|-------------------------------|----------------------|
| Filesystem de candidatos avaliados | `outputs/logs/sessions/YYYY-MM-DD/` |
| Source code de cada candidato | `.claude/commands/*.md` (um harness por command) |
| Execution traces | `outputs/logs/sessions/*/ask-*.md`, `challenge-*.md`, `promote-*.md` |
| Scores de qualidade | `quarantine_criteria_met`, `gate3_claims_*`, `confidence` no frontmatter |
| Proposer que lê filesystem | Claude Code (já usa grep/cat em comandos) |
| NLAHs como formato de harness | `.claude/commands/` são NLAHs implícitos (contracts, roles, stages já presentes) |

A diferença entre Prometheus atual e um sistema com auto-otimização é **apenas o outer-loop**: um agente que lê `outputs/logs/` periodicamente e propõe `[!patch]` nos arquivos `.claude/commands/`.

(⚠️ interpretação do compilador) O arquivo `outputs/logs/sessions/2026-04-06/challenge-deer-flow-concurrency-*.md` é um execution trace da mesma forma que os traces no Meta-Harness: registra quais claims falharam, qual modelo os invalidou, e qual ação foi tomada. Um proposer poderia ler esses logs e propor mudanças no comando `/challenge` para reduzir false positives.

## Especulação

- Um meta-harness proposer poderia ler `outputs/logs/` e identificar que `/ask` com Layer 0 scores < 0.02 sistematicamente retorna respostas paramétricas → propor `[!patch]` no comando `/ask` adicionando Corpus Sufficiency Check (que foi adicionado manualmente na sessão 8)
- O loop de melhoria manual (João lê logs → identifica padrão → atualiza command) **é** o meta-harness rodando com humano como proposer — a automação seria substituir o humano por um agente nesse loop específico
- Risco de auto-validação (autonomous-kb-failure-modes): um meta-harness que propõe e avalia via a mesma KB que otimiza pode convergir para harnesses que maximizam métricas KB em vez de qualidade epistêmica

## Verificação adversarial

**Pergunta falsificável:** se um agente lesse `outputs/logs/sessions/` dos últimos 30 dias e propusesse patches para `.claude/commands/`, pelo menos 1 patch seria aceito e melhoraria uma métrica mensurável de qualidade (ex: `retrievals_correct` em `/ask`, `claims_survived` em `/challenge`)?

**Evidência que confirmaria:** o corpus Sufficiency Check foi descoberto manualmente lendo logs de sessions onde Layer 0 retornou scores baixos — um proposer poderia ter feito o mesmo. Isso é evidência indireta de que o loop funciona.

**Evidência que refutaria:** se os logs não contiverem sinal suficiente para distinguir falhas de harness de falhas de corpus, o proposer produziria patches irrelevantes. Logs de `/ask` com gaps identificados como "corpus ausente" não são falhas do harness `/ask` — são limitações do corpus.

## Conexões

- emerge-de: [[meta-harness-optimization]] ON "filesystem de histórico como canal de feedback para proposer"
- emerge-de: [[natural-language-agent-harness]] ON "harnesses como artefatos NL portáteis com contratos e state semantics"
- related: [[autonomous-kb-failure-modes]] — risco de self-validation em loops de auto-melhoria
- related: [[complementary-learning-systems]] — meta-harness outer-loop ≈ sleep replay (lê traces passados para consolidar/melhorar)

## Fontes

- [[meta-harness-optimization]] — filesystem como canal de feedback, proposer via grep/cat, +7.7pts vs ACE
- [[natural-language-agent-harness]] — harnesses como NLAHs portáteis, file-backed state, contracts/roles/stages
- [Log /ask](../../outputs/logs/sessions/2026-04-06/ask-21-24.md) — sessão que descobriu a conexão

> ⚠️ QUARENTENA: artigo emergido de /ask cross-domain. Critérios pendentes: tempo (24h), review frio, adversarial.
