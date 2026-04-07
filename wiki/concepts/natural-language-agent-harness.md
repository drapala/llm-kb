---
title: "Natural-Language Agent Harness"
sources:
  - path: raw/papers/natural-language-agent-harnesses-pan-2026.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-06
updated: 2026-04-06
tags: [agent-architecture, harness-engineering, context-engineering, orchestration]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
quarantine: false
quarantine_promoted: 2026-04-06
quarantine_criteria_met:
  auto_promote: false
  gates_passed: [1, 2, 3]
  gate3_run: 2026-04-06
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  challenge_verdict: PRECISA_CORREÇÃO
  corrections_applied: true
  promoted_by: manual_promote
---

## Resumo

A Natural-Language Agent Harness (NLAH) externaliza a lógica de controle de agentes LLM como artefato natural-language executável — contratos, papéis, estágios, adaptadores e semântica de estado — executado por um runtime compartilhado (IHR). A premissa central: harness engineering domina performance em sistemas multi-step, mas raramente é tratada como objeto científico portátil.

## Conteúdo

### O que é um harness

Um harness é a camada de orquestração que governa múltiplas chamadas de modelo ou agente para uma família de tarefas. Especifica três dimensões:

| Dimensão | Descrição |
|----------|-----------|
| **Control** | Como o trabalho é decomposto e agendado |
| **Contracts** | Quais artefatos devem ser produzidos, quais gates devem ser satisfeitos, quando parar |
| **State** | O que persiste através de steps, branches e workers delegados |

**Distinção harness vs. context engineering:** context engineering design o prompt e contexto recuperado para uma única chamada. Harness subsume isso e gerencia estrutura multi-step, mediação de ferramentas, verificação e estado durável. (Pan et al., 2026)

### Componentes de um NLAH

| Componente | Função |
|------------|--------|
| **Contracts** | Inputs/outputs obrigatórios, constraints de formato, validation gates, permissões, regras de retry/stop |
| **Roles** | Prompts por papel (solver, verifier, researcher, orchestrator) com responsabilidades não-sobrepostas |
| **Stage structure** | Topologia de workload explícita (ex: plan → execute → verify → repair) |
| **Adapters e scripts** | Hooks determinísticos nomeados (testes, verifiers, retrieval, parsing) |
| **State semantics** | O que persiste (artefatos, ledgers, workspaces) e como é reaberto (paths, manifests) |
| **Failure taxonomy** | Modos de falha nomeados que dirigem recovery (missing artifact, wrong path, verifier failure, tool error, timeout) |

### Intelligent Harness Runtime (IHR)

IHR é o runtime que interpreta NLAHs. Decomposto em 3 partes:

1. **In-loop LLM** — lê (i) o harness, (ii) estado e ambiente atual, (iii) runtime charter, e seleciona próxima ação consistente com contratos e budgets
2. **Backend** — terminal tools + interface multi-agente (spawn_agent, wait_agent, ingestão de artefatos retornados)
3. **Runtime charter** — define semântica de contratos, estado, orquestração e ciclo de vida de child agents

**Separação explícita:** runtime charter (política compartilhada) vs. harness skill (lógica específica da família de tarefas). Isso permite ablações controladas.

### File-backed state

Módulo opcional que externaliza estado durável em artefatos path-addressable. Três propriedades:

- **Externalized** — estado escrito em artefatos, não mantido só em contexto transiente
- **Path-addressable** — stages posteriores reabrem objeto exato pelo path
- **Compaction-stable** — sobrevive a truncação, restart e delegação

Motivação: autonomia de longa duração falha quando estado crítico permanece implícito ou efêmero. (Pan et al., 2026)

### Resultados experimentais

Avaliação em SWE-bench Verified (125 amostras) e OSWorld (36 amostras), modelo GPT-5.4, raciocínio xhigh, Docker containers.

**RQ1 — Efeito comportamental:**
- Harness logic muda métricas de processo muito mais que taxa de resolução
- TRAE Full IHR: ~91.5% de tokens/chamadas ocorrem em child agents delegados, não no parent thread (média por sample, Tabela 4 — resultado de run específico, não verificável externamente)
- Full IHR cria "solved-set replacer" em vez de expansor uniforme de fronteira: cria algumas vitórias Full-only mas perde reparos de caminho direto que configurações mais leves retêm

**RQ2 — Ablação de módulos** (adicionando um por vez sobre baseline Basic):

| Módulo | SWE Verified | OSWorld |
|--------|-------------|---------|
| File-backed state | +1.6 | +5.5 |
| Evidence-backed answering | +0.0 | +0.0 |
| Verifier | −0.8 | −8.4 |
| Self-evolution | +4.8 | +2.7 |
| Multi-candidate search | −2.4 | −5.6 |
| Dynamic orchestration | +0.0 | +2.7 |

Resultado: "mais estrutura não significa automaticamente melhor performance." Em GPT-5.4 nestes datasets, self-evolution e file-backed state são os módulos mais confiáveis; verifier e multi-candidate search aumentam custo sem ganho consistente. (N=36 OSWorld é insuficiente para ranking estável — generalização cross-model requer cautela.)

**RQ3 — Migração code-to-text:**
- OS-Symphony nativo (código): 30.4% OSWorld
- OS-Symphony como NLAH sob IHR: 47.2% OSWorld
- O ganho está correlacionado com relocalização de mecanismos de confiabilidade (de GUI repair local para artifact-backed closure e state durável) — causalidade não isolada; confounders incluem diferenças de prompt, tool interface e runtime

### Por que natural language ainda importa

O paper rebate a preocupação de que modelos mais fortes tornam controle em linguagem natural irrelevante. O argumento: NL permanece importante quando especifica lógica de harness (roles, contratos, verification gates, semântica de estado, delegation boundaries), não apenas phrasing de prompt único. (Pan et al., 2026)

## Interpretação

(⚠️ nossa interpretação) A distinção harness/context-engineering é análoga à distinção arquitetura/prompt que esta KB usa em outros contextos: o harness é a estrutura permanente que governa como prompts são formados — não é ele mesmo um prompt.

(⚠️ nossa interpretação) Os resultados de ablação sugerem que módulos melhoram quando "apertam o caminho do comportamento intermediário até a condição de aceitação do avaliador." Isso ressoa com o conceito de evaluation-order-independence na KB: estrutura que não alinha seu critério de sucesso local com o critério final do benchmark não ajuda.

(⚠️ nossa interpretação) File-backed state como módulo positivo consistente confirma o padrão de "estado durável como infraestrutura de confiabilidade" que aparece em MemGPT e outros artigos de agent memory. O nome muda, a motivação é a mesma.

## Verificação adversarial

**Claim mais fraco:** a migração code-to-text (RQ3) mostra +16.8 pontos em OSWorld. Isso é a comparação mais frágil porque envolve reimplementação do harness, não uma adição isolada — variáveis de confusão inevitáveis.

**O que o paper NÃO diz:**
- Não afirma que NLAHs são superiores a harnesses em código em geral — RQ3 é uma comparação de migração, não de paradigma
- Não demonstra que o framework escala para tasks mais complexas que SWE-bench/OSWorld
- Não compara IHR contra outros runtimes em condições controladas (só ablações internas)

**Simplificações feitas:**
- Experimentos rodam subsets (125 SWE, 36 OSWorld) com seed fixo — não benchmarks completos
- "GPT-5.4 com raciocínio xhigh" é o único modelo testado — sem validação cross-model

**Prior work:** cita ReAct (Yao 2023), RAG (Lewis 2021), Reflexion (Shinn 2023), MemGPT, LangChain, OpenAI como trabalhos que estabelecem controlabilidade em peças — mas não como harness portátil unificado.

## Aplicação à KB

O conceito de NLAH mapeia diretamente para o que esta KB já faz com skills (CLAUDE.md, skill files): cada skill é um harness parcial com contratos implícitos e uma taxonomia de comportamento. A diferença: NLAHs tornam contratos explícitos e executáveis por um runtime, em vez de interpretados ad-hoc por um LLM.

## Quality Gate
- [x] Wikilinks tipados: 4 substituições realizadas
- [x] Instance→class: claims numéricos qualificados com modelo+dataset
- [x] Meta-KB separado: referências a esta KB em ## Aplicação à KB
- [x] Resumo calibrado: mantido — body tem caveats de subset experimental

## Conexões

- derivedFrom: [[multi-agent-orchestration]] — harness é a formalização da camada de orquestração; NLAH especifica o que multi-agent-orchestration deixa implícito
- complementsAt: [[context-management]] — context engineering é sub-caso de harness; harness inclui contexto mas governa também state, contracts e delegation
- validates: [[agent-memory-architectures]] — file-backed state como módulo positivo confirma importância de estado externalizável (Pattern 1: MemGPT hierarchy)
- complementsAt: [[meta-harness-optimization]] — Pan define O QUE é um harness portátil; Lee define COMO otimizá-lo automaticamente
- emerge-para: [[prometheus-as-nlah-substrate]] ON "harnesses como artefatos NL portáteis com contratos e state semantics"

## Fontes

- [Natural-Language Agent Harnesses (Pan et al., 2026)](../../raw/papers/natural-language-agent-harnesses-pan-2026.pdf) — formalização de NLAHs, IHR, ablações de módulos, migração code-to-text
