# Relatório Meta: Claims Pré-2024 com Risco de Obsolescência

date: 2026-04-04
query: "Quais claims da KB dependem de papers publicados antes de 2024 e têm maior probabilidade de terem sido superados por trabalho posterior?"
confidence: média (análise interna, sem web search de verificação)

---

## Fontes Pré-2024 na KB (9 papers computacionais)

| Fonte | Data | Claims que fundamenta |
|-------|------|----------------------|
| LMs Know What They Know | 2022-07 | "Mostly calibrated, fails on hard" |
| Socratic Prompting | 2023-02 | 6 Socratic techniques for LLMs |
| Reflexion | 2023-03 | 91% HumanEval, 52% sem testes, +8pp verbal |
| Multiagent Debate | 2023-05 | Multi-LLM debate melhora factuality |
| Model Collapse | 2023-05 | "Tails disappear" em self-consumption |
| CoALA | 2023-09 | Cognitive architecture framework |
| Promptbreeder | 2023-09 | Self-referential prompt evolution |
| MemGPT | 2023-10 | Virtual context management, FIFO eviction |
| Self-RAG | 2023-10 | Structured reflection tokens |

Nota: fontes de epistemologia (Popper 1934, Lakatos 1970, Simon 1956, Pearl 2018) e ontologia (BFO, DOLCE, OWL, Noy) NÃO envelhecem da mesma forma — são frameworks teóricos, não benchmarks. Excluídas desta análise.

---

## RISCO ALTO — Claims provavelmente superados

### 1. Reflexion: "91% pass@1 no HumanEval" (2023-03)

**O claim:** Reflexion com GPT-4 atinge 91% no HumanEval, superando GPT-4 baseline (80.1%).

**Por que provavelmente superado:**
- HumanEval é um benchmark de 2021 com 164 problemas. Em 2026, modelos frontier provavelmente excedem 91% SEM Reflexion — o delta que Reflexion adicionava (80→91) pode ter sido absorvido pelo modelo base.
- O claim importa para a KB não pelo número absoluto (91%) mas pelo MECANISMO (verbal reflection + testes = melhoria). O mecanismo pode continuar válido mesmo que o benchmark esteja saturado.
- Verificado em raw/: 91% confirmado no paper. Mas "surpassing GPT-4" refere-se ao GPT-4 de 2023, não ao GPT-4o/4.1 de 2025-2026.

**Impacto na KB:** Alto — Reflexion é citada em 5+ artigos como evidência de que verbal reflection funciona. Se o delta verbal diminuiu em modelos mais novos (porque o baseline subiu), a magnitude do efeito que a KB cita está inflada.

**Pearl level:** O mecanismo (L2: ablation mostra que testes importam) provavelmente sobrevive. O número (L1: 91% neste benchmark) provavelmente não.

**Ação:** /scout por "Reflexion 2025 2026" para verificar se o mecanismo foi replicado em modelos mais recentes.

### 2. MemGPT: Virtual context management com FIFO (2023-10)

**O claim:** MemGPT usa hierarchical tiers com FIFO eviction + memory pressure warnings como paradigma de agent memory.

**Por que provavelmente superado:**
- MemGPT evoluiu pra **Letta** (o próprio raw/ documenta isso). A KB cita MemGPT como arquitetura fundacional, mas Letta formalizou e refinou os 4 blocos.
- Context windows cresceram dramaticamente (8K → 128K → 1M+). A motivação original de MemGPT ("context windows are too small") é menos premente com modelos de 200K-1M tokens.
- Hindsight (2025, 83.6% LongMemEval com 20B), Zep (2025, 94.8% DMR), e A-MEM (2025) SUPERAM MemGPT em benchmarks modernos. O artigo agent-memory-architectures já documenta isso.
- Synapse (2026) SUPERA MemGPT explicitamente no LoCoMo (40.5 vs 28.0 F1).

**Impacto na KB:** Médio — a KB já tem 7 patterns mais recentes em agent-memory-architectures. MemGPT é histórico, não current SOTA. Mas o artigo context-management ainda usa MemGPT como referência principal para virtual context — deveria referenciar os sucessores.

**Pearl level:** O paradigma (tiered memory) sobrevive em todos os sucessores. Os números específicos de MemGPT (benchmarks com GPT-4-turbo 2023) estão obsoletos.

**Ação:** Qualificar MemGPT como "foundational (2023), superseded by Letta, Hindsight, Zep, A-MEM" nos artigos que o citam.

### 3. LMs Know What They Know: "Mostly calibrated" (2022-07)

**O claim:** Larger models show good calibration. Models can estimate P(True) and P(IK). Calibration breaks down on unfamiliar tasks.

**Por que possivelmente superado:**
- Testado em modelos até 2022 (GPT-3, early GPT-4). Modelos 2025-2026 (GPT-4.1, Claude Opus, Gemini) podem ter calibração diferente (melhor ou pior).
- JudgeBench (2024-2025) já complementa: "GPT-4o near random on hard tasks." Mas JudgeBench testa AVALIAÇÃO, não calibração de conhecimento próprio.
- A tensão "mostly calibrated vs near random" documentada em llm-as-judge pode ter resolução diferente com modelos mais recentes.

**Impacto na KB:** Médio — a tensão está documentada como difficulty-contingent ("calibrado em fácil, falha em difícil"). Essa resolução provavelmente sobrevive mesmo com modelos novos, porque é estrutural (fácil = in-distribution, difícil = out-of-distribution).

**Pearl level:** O padrão (L1: calibration degrades with difficulty) provavelmente é robusto. Os números específicos (r=0.78-0.81 consistency on wrong answers, testado em 26 modelos de 2022) podem ter mudado.

**Ação:** Baixo urgência. O padrão qualitativo provavelmente se mantém.

---

## RISCO MÉDIO — Claims possivelmente complementados

### 4. Model Collapse: "Tails disappear" (2023-05, publicado Nature 2024)

**Status:** O paper foi publicado na Nature em 2024 — revisado por pares, robusto. O mecanismo (recursive self-consumption) é formal e independente de modelo específico. Provavelmente ROBUSTO, mas com nuances:
- Paper posterior (2024): "Is Model Collapse Inevitable?" mostra que mistura de dados reais+sintéticos previne collapse. Nossa KB já documenta essa mitigação.
- A aplicação de model collapse a KBs (nossa interpretação) permanece não testada.

### 5. Multiagent Debate: "Melhora factuality" (2023-05)

**Status:** Multi-agent approaches evoluíram muito desde 2023. O claim específico (debate melhora factuality) provavelmente se mantém, mas o landscape de multi-agent é muito mais sofisticado agora (AgentRxiv, AI Scientist, OpenResearcher, coordinator mode do Claude Code).

### 6. CoALA: Cognitive architecture framework (2023-09)

**Status:** Framework conceitual, não benchmark. A taxonomia (working/episodic/semantic/procedural) é de ciência cognitiva, não de ML — não "envelhece" como benchmarks. A Memory Survey (2025, 47 authors) propõe taxonomia diferente (forms/functions/dynamics) que complementa mas não invalida CoALA.

### 7. Self-RAG: Reflection tokens (2023-10)

**Status:** O conceito de reflection tokens ([Retrieve], [IsRel], [IsSup], [IsUse]) provavelmente foi absorvido por frameworks mais recentes. O claim no wiki (Section em retrieval-augmented-generation) é usado como inspiração para /ask checkpoints, não como SOTA.

### 8. Promptbreeder: Self-referential improvement (2023-09)

**Status:** O conceito (evolve both task prompts AND mutation prompts) é citado na KB como "Fase 3 potential" — nunca como claim factual. Baixo risco de obsolescência porque nunca foi claim central.

---

## RISCO BAIXO — Claims provavelmente robustos

### 9. Socratic Prompting (2023-02)

**Status:** Framework de técnicas (definition, elenchus, dialectic, maieutics, generalization, counterfactual). São técnicas milenares aplicadas a LLMs — não envelhecem.

---

## Resumo de Ações

| Prioridade | Fonte | Ação |
|-----------|-------|------|
| ALTA | Reflexion (2023) | /scout por replicação em modelos 2025-2026. Verificar se delta verbal se mantém. |
| ALTA | MemGPT (2023) | Qualificar como "foundational, superseded" nos artigos que citam. |
| MÉDIA | LMs Know (2022) | Verificar se calibration pattern se mantém com modelos 2025-2026. |
| BAIXA | Model Collapse, CoALA, Multiagent Debate, Self-RAG, Promptbreeder, Socratic | Monitorar, não agir agora. |

## Padrão Geral

A KB tem uma **assimetria temporal**: papers de MECANISMO (como Reflexion funciona, como Model Collapse funciona) envelhecem mais devagar que papers de BENCHMARK (91% no HumanEval, 28.0 F1 no LoCoMo). 

A KB deveria distinguir:
- **Claims de mecanismo** (L2): "verbal reflection + testes = melhoria" — provavelmente robusto
- **Claims de benchmark** (L1): "91% no HumanEval com GPT-4" — provavelmente obsoleto

O Quality Gate CHECK 2 (instance→class) já captura parcialmente isso. Mas deveria haver um CHECK adicional: **temporal freshness** — quando o número foi medido, com qual modelo, e se o benchmark está saturado.

---

**Fontes wiki:** [[self-improving-agents]], [[agent-memory-architectures]], [[llm-as-judge]], [[causal-reasoning-pearl]], [[retrieval-augmented-generation]]

**Fontes raw verificadas:**
- [Reflexion](raw/papers/reflexion-verbal-reinforcement-learning.md) — 91%, 52%, +8pp confirmados
- [MemGPT](raw/papers/memgpt-llms-as-operating-systems.md) — FIFO, Letta evolution confirmados
- [LMs Know](raw/papers/lm-know-what-they-know.md) — "mostly", r=0.78-0.81 confirmados

**Confiança:** média — análise de obsolescência sem verificação via web search (não busquei se Reflexion foi replicado em 2025-2026, apenas inferi probabilidade)

**Gaps:**
- Nenhuma verificação de "Reflexion 2025 2026" feita — /scout necessário
- Nenhuma verificação de benchmarks atuais de HumanEval — saturação provável mas não confirmada
