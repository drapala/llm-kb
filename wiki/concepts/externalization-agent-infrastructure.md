---
title: "Externalization in LLM Agents: Memory, Skills, Protocols, Harness"
sources:
  - path: raw/papers/zhou-2026-externalization-llm-agents.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-18
updated: 2026-04-18
tags: [agents, harness, memory, skills, protocols, externalization, survey]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
reads: 1
last_read: 2026-04-18
retrievals_correct: 1
provenance: source
freshness_status: current
quarantine: false
quarantine_promoted: 2026-04-18
quarantine_criteria_met:
  auto_promote: true
  gates_passed: [1, 2, 3, 4]
  gate3_skipped: staleness
  challenge_verdict: PUBLICÁVEL
topics: [harness-engineering, agent-memory, externalization, cognitive-artifacts, weights-to-harness]
depends_on: []
---

## Resumo

Zhou et al. (2026) propõem "externalization" como princípio organizador do design de agentes LLM: capacidades antes esperadas internamente no modelo são relocadas para infraestrutura externa. **Memory externaliza estado, Skills externalizam expertise procedimental, Protocols externalizam estrutura de interação, Harness unifica os três em execução governada.** A progressão histórica: weights → context → harness.

## Conteúdo

### Framework: 3 Formas de Externalização

**1. Memory — externaliza estado ao longo do tempo**
- Transforma recall em retrieval
- Tipos: episódico, semântico, procedimental, working memory
- Chave: decay policy (o que esquecer vs. persistir)

**2. Skills — externaliza expertise procedimental**
- Transforma geração improvisada em composição guiada
- Reutilizável, composável, inspecionável
- Chave: skill discovery e invocação

**3. Protocols — externaliza estrutura de interação**
- Transforma coordenação ad hoc em troca estruturada
- Inclui: tool-use protocols, comunicação multi-agente, padrões human-agent
- Chave: negociação e evolução de protocolos

### Harness Engineering: Camada de Unificação

O harness coordena memory + skills + protocols em execução governada.

"The harness is not just infrastructure — it changes the task the model is being asked to solve."

Propriedades do harness efetivo: **persistente, inspecionável, reutilizável, governável**.

Tendência emergente: **self-evolving harnesses** — o harness atualiza a si mesmo com base em padrões de falha do agente.

### Progressão Histórica: Weights → Context → Harness

| Camada | O que muda | Exemplos |
|---|---|---|
| Weights | Training do modelo | Fine-tuning, RLHF |
| Context | O que está na context window | RAG, memory injection, tool results |
| Harness | Organização do runtime | Hooks, MCP, skills, session management |

A pesquisa migrou progressivamente para fora em direção ao harness.

### Por que Externalização Funciona

"Externalization transforms hard cognitive burdens into forms that the model can solve more reliably."

- Memory: recall → retrieval (mais confiável)
- Skills: geração improvisada → composição guiada (mais confiável)
- Protocols: coordenação ad hoc → troca estruturada (mais confiável)

Trade-off: algumas capacidades permanecem melhor tratadas parametricamente (nos pesos); outras tornam-se mais confiáveis quando externalizadas.

### Paralelo Histórico Humano

Externalização cognitiva humana: linguagem falada → escrita → impressão → computação digital.

A progressão de agentes espelha esse arco: pesos → context → harness.

### Desafios em Aberto

1. Como particionar capacidade entre modelo e infraestrutura?
2. Como avaliar sistemas externalizados independentemente?
3. Como governar artefatos compartilhados (skills, memory, protocolos)?
4. Co-evolução de longo prazo: modelos e infraestrutura mudam juntos

## Verificação adversarial

**Claim mais fraco:** "externalization transforms cognitive burdens into forms the model solves more reliably" — é uma afirmação teórica sem benchmark direto de comparação paramétrico vs. externalizado para a mesma tarefa.

**O que o paper NÃO diz:**
1. Não fornece dados empíricos comparando performance com vs. sem cada forma de externalização
2. Não define quando externalização torna-se overhead (threshold onde o custo de coordenação supera o benefício)
3. Não aborda colisão entre formas: skills e protocols podem conflitar ao evoluir independentemente

**Simplificações feitas:** a analogia com cognitive externalization humana é ilustrativa, não demonstrativa.

**Prior work citado:** MemGPT, ReAct, Reflexion, DSPy, RLHF, CoALA — cobre o landscape bem.

## Interpretação

(⚠️ nossa interpretação) "Self-evolving harnesses" é convergente com ERL (Experiential Reflective Learning): o harness que se atualiza com base em falhas é precisamente o que ERL faz para heurísticas. A diferença é que ERL atualiza as heurísticas do agente (content), enquanto self-evolving harness atualizaria os mecanismos de execução (structure).

(⚠️ nossa interpretação) A triad Memory/Skills/Protocols mapeia diretamente para a estrutura de hot/cold memory da KB: Memory = estado cross-sessão (quente); Skills = .claude/commands/ (fria); Protocols = hooks + CLAUDE.md (sempre quente).

## Conexões

- supersedes: [[natural-language-agent-harness]] ON "provê framework teórico (externalization) que fundamenta o conceito de NLAH — harness é a unification layer da triad MSP"
- validates: [[agent-memory-architectures]] ON "Memory como externalization of state — confirma a separação episódico/semântico/procedimental como eixos de externalização"
- validates: [[codified-context-codebase-agents]] ON "hot/cold memory = externalização de estado (Memory) + expertise (Skills); constituição = Protocol"
- refines: [[self-improving-agents]] ON "self-evolving harnesses = ERL aplicado ao harness, não apenas a heurísticas de conteúdo"

## Fontes

- [Zhou et al. 2026 — Externalization in LLM Agents (arXiv 2604.08224)](../../raw/papers/zhou-2026-externalization-llm-agents.md) — survey completo

## Quality Gate

- [x] Wikilinks tipados: 4 (supersedes, validates×2, refines)
- [x] Instance→class: claims teóricos sem números; corretamente apresentados como framework, não empiria
- [x] Meta-KB separado: interpretações na seção correta
- [x] Resumo calibrado: limitações (teórico, sem benchmark) documentadas
