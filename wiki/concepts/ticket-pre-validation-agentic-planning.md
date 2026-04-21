---
title: "Ticket Pre-Validation in Agentic Planning: Detecting Underspecification Before Execution"
sources:
  - path: raw/papers/vijayvargiya-2026-ambig-swe-underspecification.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/edwards-2026-ask-or-assume-clarification.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-19
updated: 2026-04-19
tags: [agents, clarification, underspecification, pre-validation, coding-agents, swe]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - raw/papers/vijayvargiya-2026-ambig-swe-underspecification.md
  - raw/papers/edwards-2026-ask-or-assume-clarification.md
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
topics: [ticket-validation, underspecification, clarification, pre-planning, agentic-coding]
depends_on: []
---

## Resumo

Agentes de coding que recebem tickets underspecified e procedem diretamente ao planejamento incorrem em falhas de Phase 1 (Understanding) que se propagam e amplificam ao longo do pipeline. Dois papers (AMBIG-SWE, ICLR 2026; Ask or Assume, arXiv 2603.26233) convergem: **detectar underspecification antes da execução e solicitar clarificação produz +74% de resolve rate** no SWE-bench Verified. O gargalo não é gerar perguntas, mas **detectar que perguntas são necessárias**.

## Conteúdo

### O problema: LLMs default para execução sem questionar

LLMs são treinados predominantemente para completar tarefas autonomamente. Quando recebem instrução underspecified, o comportamento padrão é assumir — não perguntar. Isso é contraproducente em pipelines de software engineering onde:

- ACs ambíguos geram planos incorretos desde o início
- O agente só descobre a ambiguidade após múltiplos tool calls (quando o trajectory já está comprometido)
- Retries consomem tokens sem corrigir a causa raiz (underspecification, não execution error)

### Resultado central: +74% com clarificação

**AMBIG-SWE (Vijayvargiya et al., ICLR 2026):**
- Dataset: SWE-Bench Verified com informação sistematicamente removida das issues
- Condição 1: underspecified + sem interação → baseline
- Condição 2: underspecified + interação habilitada → **+74% sobre baseline**

**Ask or Assume (Edwards & Schuster, arXiv 2603.26233, Março 2026):**
- Multi-agent scaffold (OpenHands + Claude Sonnet 4.5)
- Resolve rate: 69.40% (underspecified + clarificação) vs. 61.20% (underspecified, sem clarificação)
- Comparado com fully-specified baseline: ~71%
- Clarificação fecha ~80% do gap entre underspecified e fully-specified

### O gargalo: detecção, não geração

Ambos os papers convergem no mesmo finding: **gerar perguntas úteis é mais fácil do que detectar que perguntas são necessárias**.

- Claude Sonnet 4 detecta underspecification com 89% de acurácia
- Claude Sonnet 3.5: 84%
- Maioria dos outros modelos: performance substancialmente pior

Sem encouragement explícito, LLMs default para comportamento não-interativo mesmo quando a instrução é ambígua.

### Arquitetura: separação de detection e execution

A principal contribuição arquitetural de Ask or Assume: **decoupling explícito de detecção de underspecification e execução de código** em agentes distintos.

```
[Ticket] → [Detector Agent] → ambíguo? → [Clarificação] → contexto completo → [Execution Agent]
                            → claro?   ──────────────────────────────────────→ [Execution Agent]
```

**Por que separar?** Um único agente que faz tudo tende a assumir durante a execução (já está no "modo de execução"). O agente de detecção tem um único objetivo: avaliar se a especificação é suficiente.

**Benefício adicional:** o sistema exibe **uncertainty calibrada** — conserva queries em tasks simples, busca informação proativamente em tasks complexas. Evita o failure mode oposto (perguntar demais em tickets bem especificados).

### Tipos de underspecification relevantes para SWE

1. **ACs não-verificáveis:** "tornar mais rápido", "melhorar UX" — sem threshold ou critério concreto
2. **Referências externas ausentes:** "como discutido na reunião de segunda", "seguindo o padrão do módulo X" sem descrever o padrão
3. **Escopo implícito:** "adicionar autenticação" sem especificar qual endpoint, qual método, quais edge cases
4. **Conflito entre ACs:** AC-01 e AC-03 são incompatíveis, agente descobre só no meio da implementação

### Cascading failure sem pre-validation

Underspecification em tasks complexas cria múltiplos gaps interdependentes que emergem dinamicamente. O agente pode executar muitos steps antes de reconhecer que falta informação — e nesse ponto o trajectory já está comprometido (arquivos modificados, testes rodados em direção errada). Reset e retry = custo total do attempt sem benefit.

## Verificação adversarial

**Claim mais fraco:** o +74% de AMBIG-SWE é medido em condição controlada (informação sistematicamente removida do issue original). Em produção, underspecification real pode ser mais sutil e menos detectável.

**O que os papers NÃO dizem:**
1. Não definem threshold de complexidade acima do qual clarificação não-interativa (batch) é suficiente
2. Não comparam custo de clarificação (latência + tokens da conversa adicional) vs. custo de retry sem clarificação
3. Não abordam o caso onde o stakeholder que escreveu o ticket também não sabe a resposta (ambiguidade genuína de produto)

**Simplificações:** os resultados assumem um usuário/oracle disponível para responder perguntas. Em pipelines CI/CD onde o agente roda automaticamente (sem humano disponível), clarificação interativa não é opção — o pré-validation deve ser um hard gate, não uma conversa.

**Prior work citado:** SWE-bench (Jimenez et al. 2024), OpenHands (Wang et al. 2024), ClarifyGPT.

## Interpretação

(⚠️ nossa interpretação) Para pipelines fully-autonomous (sem humano disponível para responder perguntas), a arquitetura de detecção pode ser adaptada como **hard gate não-interativo**: se o detector classifica o ticket como underspecified, retorna `ticket_not_ready` imediatamente com a lista de ACs problemáticos, sem tentar planejar. Isso preserva o valor da detecção sem requerer interatividade.

(⚠️ nossa interpretação) A separação detector/executor mapeia para o padrão de pipeline: `ticket_validator.py` (detection agent) → `planner.py` (execution agent). O detector não precisa chamar o planner; só precisa avaliar a especificação.

## Conexões

- refines: [[agentic-coding-failure-taxonomy]] ON "Phase 1 (Understanding) failures têm intervenção empírica direta: detection + clarification antes de planning; +74% em SWE-bench Verified"
- validates: [[uncertainty-aware-workflow-denoising]] ON "ambiguidade detectada pré-execução é análoga ao Sensing step do DenoiseFlow — mas aplicada ao ticket-input em vez do plan-level"
- validates: [[agentops-mas-failure-management]] ON "step-wise failure detection; aqui o 'step' é o próprio ticket-input, antes do primeiro tool call"
- partOf: [[agentic-codebase-enforcement-patterns]] ON "pré-validation é enforcement de qualidade de input, não de output — complementa scope precheck e critic"

## Fontes

- [Vijayvargiya et al. 2026 — AMBIG-SWE (arXiv 2502.13069)](../../raw/papers/vijayvargiya-2026-ambig-swe-underspecification.md) — +74% com interatividade; detecção como gargalo; ICLR 2026
- [Edwards & Schuster 2026 — Ask or Assume (arXiv 2603.26233)](../../raw/papers/edwards-2026-ask-or-assume-clarification.md) — arquitetura decoupled detection/execution; +8.2pp; uncertainty calibrada

## Quality Gate

- [x] Wikilinks tipados: 4 (refines, validates×2, partOf)
- [x] Instance→class: +74% atribuído a AMBIG-SWE/SWE-bench Verified; +8.2pp atribuído a Ask or Assume/OpenHands+Claude
- [x] Meta-KB separado: interpretações de pipeline na seção Interpretação
- [x] Resumo calibrado: caveat sobre oracle disponível documentado em Verificação adversarial
