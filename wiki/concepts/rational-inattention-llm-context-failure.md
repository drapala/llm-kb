---
title: "Rational Inattention como Design Target para Context Windows de LLMs"
sources:
  - path: wiki/concepts/attention-dilution-llm-context.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/rational-inattention.md
    type: synthesis
    quality: primary
created: 2026-04-23
updated: 2026-04-23
tags: [rational-inattention, attention-dilution, llm, context-window, channel-capacity, sparse-attention]
source_quality: medium
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: true
quarantine_created: 2026-04-23
quarantine_reason: "Artigo emergido de /ask cross-domain — aguarda confirmação adversarial e review frio"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
provenance: emergence
emergence_trigger:
  pair: [attention-dilution-llm-context, rational-inattention]
  ask_session: outputs/logs/sessions/2026-04-23/ask-emerge-pairs.md
  connection_type: ANÁLOGO-A
  pearl_level: L2
emerged_on: 2026-04-23
topics: [rational-inattention, llm-context, channel-capacity, sparse-attention, context-window]
---

## Resumo

Attention dilution em LLMs é a falha de rational inattention: Sims (2003) formaliza que agentes com channel capacity C limitada processam observações com ruído crescente além de C. LLMs têm uma "capacidade efetiva" C de atenção que, quando excedida por contextos longos, produz o mesmo padrão de degradação que Sims prevê para agentes. A diferença crítica: rational inattention descreve alocação ÓTIMA dado C; attention dilution é SUBÓTIMA — o LLM não concentra C nos tokens mais informativos. Isso define um design target: modelos com sparse attention com learned allocation implementam computacionalmente rational inattention.

## Conteúdo

### O que rational-inattention contribui

Sims (2003): agentes têm channel capacity C entre observações X e ações Y, com constraint I(X;Y) ≤ C. Para Gaussian X: Var(Y|X) = Var(X)/e^{2C} — variância residual irredutível dado o canal. Agentes com rational inattention alocam C onde o ganho esperado é maior (price stickiness em macroeconomia, atenção seletiva em mercados financeiros). O modelo prevê: quanto maior o excesso de variância de X sobre e^{2C}, maior o ruído na ação Y.

### O que attention-dilution-llm-context contribui

Kumar 2026 (350 PRs, SWE-PRBench): degradação monotônica de config_A (diff only) para config_C (full context) em todos os 8 modelos frontier. Colapso específico em Type2_Contextual issues ao adicionar contexto além do diff. O mecanismo é estruturalmente análogo ao canal de Sims saturado: tokens extras além da capacidade efetiva C aumentam ruído na detecção de issues sem aumentar sinal.

### O que emerge da combinação

(⚠️ nossa interpretação) O isomorfismo é estrutural mas a teleologia é invertida: rational inattention é alocação ÓTIMA de C dado constraint; attention dilution é alocação SUBÓTIMA onde C é desperdiçado em tokens irrelevantes. Um LLM com true rational inattention resolveria attention dilution automaticamente — alocaria seus bits de atenção para os tokens com maior I(X;Y) para a task de review, ignorando tokens de baixa relevância.

(⚠️ nossa interpretação) Isso define um design target para arquiteturas de LLM: **sparse attention com learned allocation** é a implementação computacional de rational inattention. Modelos que aprendem a alocar atenção seletivamente (não uniformemente distribuída) deveriam mostrar menor degradação A→B→C no benchmark de Kumar porque concentram C onde ele é mais informativo.

(⚠️ nossa interpretação) A analogia também sugere que o threshold de degradação (o ponto onde config_B começa a perder para config_A) é análogo ao ponto onde I(X;X_review) excede C — a "capacidade efetiva de atenção" do modelo para a task específica de code review. Modelos maiores têm C maior e, portanto, threshold mais alto.

## Especulação

- Modelos com sparse attention explícita (LongFormer, BigBird, Flash-Linear-Attention) devem mostrar menor degradação A→B→C que modelos full-attention no benchmark de Kumar — verificável se os modelos testados incluírem arquiteturas sparse
- Modelos com extended thinking (Claude 3.7, DeepSeek R1) podem estar implementando rational inattention implicitamente ao focar "pensamento" em partes específicas do contexto
- O threshold de capacidade efetiva C para code review varia por tipo de issue: Type1_Direct < Type2_Contextual, sugerindo que C é task-specific, não apenas model-specific

## Verificação adversarial

**Pergunta falsificável:** Modelos com sparse attention explícita devem degradar menos que modelos full-attention quando contexto aumenta de config_A para config_C no benchmark SWE-PRBench.

**Evidência que confirmaria:** Dado os 8 modelos testados por Kumar — se algum for LongFormer ou similar e não degradar monotonicamente, confirma.

**Evidência que refutaria:** Todos os modelos, independente de arquitetura de atenção, degradam monotonicamente — sugerindo que a degradação é causada por outro mecanismo além da distribuição de atenção (ex: comprimento da geração, posição relativa, KV cache).

## Conexões

- emerge-de: [[attention-dilution-llm-context]] ON "degradação monotônica quando |context| > capacidade efetiva C"
- emerge-de: [[rational-inattention]] ON "I(X;Y) ≤ C como constraint de capacidade de processamento"
- implica-em: [[attention-dilution-llm-context]] — sparse attention com learned allocation como solução arquitetural

## Fontes

- [[attention-dilution-llm-context]] — SWE-PRBench, degradação A→B→C, Type2_Contextual collapse
- [[rational-inattention]] — Sims 2003, I(X;Y) ≤ C, Var(Y|X) = Var(X)/e^{2C}
- [Log /ask 2026-04-23](../../outputs/logs/sessions/2026-04-23/ask-emerge-pairs.md) — sessão que confirmou a conexão

> ⚠️ QUARENTENA: artigo emergido de /ask cross-domain. Critérios pendentes: tempo (24h), review frio, adversarial.
