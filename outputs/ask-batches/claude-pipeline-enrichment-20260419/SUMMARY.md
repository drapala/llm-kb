# SUMMARY — Enrichment /ask batch para claude-pipeline roadmap

**Data**: 2026-04-19  
**Escopo**: 12 /ask queries cruzando conceitos do vault metaxon com gaps do claude-pipeline roadmap (prompts 01-21, IMPLEMENTATION_ROADMAP.md).  
**Objetivo**: identificar mudanças concretas ao roadmap — modificações a prompts existentes e prompts novos propostos.

---

## TL;DR por query

| # | Query | TL;DR acionável | Prompt(s) do roadmap afetado(s) |
|---|---|---|---|
| 01 | PRM vs rubric LLM | Rubric tem 16% self-enhancement (CALM), JudgeBench near-random em hard tasks; PRM resolve mas precisa dataset — eval harness (06) é o caminho. Olken: oracle estocástico + determinístico em red-zone > oracle sempre. Zamboni-Litschig: medir *marginal lift* do oracle, não absoluto. | 02, 06, 10; **novo 25** (PRM training) |
| 02 | Rational inattention | Context compaction precisa hierarquia de 12 níveis de preservação (AC/diff/exit nunca compactam); budget adaptativo por sinal de incerteza; breakpoint cache não-arbitrário (cache_priority_score = I/cost); compactor não-LLM-puro. | 15; **novo 29** (C_LLM measurement) |
| 03 | Self-mod safety gaps | Prompt 20 traffic-light não cobre: dependency closure transitivo, prompt drift em agent_prompts/, oracle cross-family, canary longitudinal, fixture provenance audit. Voyager: compositionality test em skills. AI Scientist: file-as-bus mostra drift de 10 mods isoladas. | 20, 16, 21; **novos 30** (heuristic unlearning), **31** (cross-config invalidation) |
| 04 | Tree search | Inviável no inner_agent sem checkpointing turn-level + worktree-per-branch (07+18). Ganho real de literatura recente = **best-of-N sampling**, não MCTS. Aplicação imediata: prompt 07 + `parallel_attempts: N`. | 07, 08, 18; **novo 32** (tree search, pós-07+18) |
| 05 | Lemons plan quality | Planner é Akerlof seller (info assimétrica). Signalling: plan_predictions falsificáveis + test skeletons pré-submit + cost variance. Licensing: structural gate simbólico pré-execução. Planner reputation cross-ticket como moat interno. | 04 (estender para planner rep); **novo 33** (Plan Structural Gate) |
| 06 | Task displacement | 50-70% dos "stages LLM" podem migrar para tooling determinístico (A&R). Ticket validator, post_stage_critic em stages triviais, failure_classifier são candidatos. Ripple effect: inner_agent muda padrão (linter ≠ LLM critic). | 06, 10, 12; **novos 34** (Stage Classification), **35** (Determinism-first refactor) |
| 07 | Bradford antipatterns | Registry deve ter `bradford_multiplier` + category diversity score (< 40% por categoria). `concrete_evidence_count >= 2` para active (não inferência). Threshold mínimo match_score no retriever (silent se core não cobre). | 11, 16, 19, 06 |
| 08 | Audit mix | Reflexion interno (accountability local) + oracle externo em red-zone determinístico + 15-25% estocástico + trigger-based. Multi-instance self-critique como oracle barato. `oracle_models` default multi-family. | 15, 02, 06, 09; **novo 36** (multi-instance self-critique) |
| 09 | Platform flywheel | **Moat structural = 0 hoje**. Roadmap 1-21 é excelente single-tenant mas sem network effects. Moat requer multi-tenant aggregation com privacy + marketplace governance + reputation + schema cross-compat. Projeto separado. | 11, 16; **novos 37** (multi-tenant), **38** (skills validation canary) |
| 10 | Procurement AC design | Ticket template deve ter FP (simple) vs C+ (complex) — hoje força FP → aditivos estruturais. Efficient vs strategic escalation classifier. AC gaming detector (4 sinais Decarolis). Screening menu Laffont-Tirole. | 09, 10, 15; **novos 39** (AC gaming detector), **40** (screening AC menu) |
| 11 | Ontology unificada | `metaxon/ontology/core.py` cobre ~70% do pipeline via subclasses de KnowledgeArtifact (Antipattern, Lesson, Skill). Separar continuant (antipattern) de occurrent (antipattern_match) habilita feedback quantitativo. **Pré-requisito para Q9 moat.** | 04, 11, 16, 19; **novo 41** (ontology alignment) |
| 12 | Neurosymbolic gates | Gates 13 e 14 **domínio symbolic completo, manter**. Gate 12 deve ter ordem estrita symbolic→neural→symbolic (não LLM sempre). LLM reviewer retorna veredicto estruturado para auditabilidade. Compliance gate per-repo é extensão natural. | 12; **novo 42** (compliance gate) |

---

## Tabela mestra — mudanças a prompts existentes

| Prompt | Mudança proposta | Origem | Prioridade |
|---|---|---|---|
| 02 | `oracle_sampling_policy` (deterministic+stochastic mix); default multi-family models | Q1, Q8 | Alta |
| 04 | Estender rule_curator para planner-reputation cross-ticket | Q5 | Alta |
| 06 | Métrica `llm_call_ratio`, `marginal_oracle_lift`, registry bradford health longitudinal | Q1, Q6, Q7, Q8 | Alta |
| 07 | `parallel_attempts: N` + selector (best-of-N) | Q4 | **Muito alta** (ganho rápido) |
| 09 | Classifier efficient/strategic escalation; oracle triggers além de humano | Q8, Q10 | Alta |
| 10 | Feedback loop test_quality → eval; check same-turn test+code authorship; evitar agregações ingênuas em exit_conditions | Q1, Q10, Q6 | Alta |
| 11 | Bradford multiplier métrica; category diversity; `concrete_evidence_count >= 2`; separar matches (occurrents) de antipatterns (continuants) | Q7, Q11 | Alta |
| 12 | Ordem estrita symbolic→neural; veredicto estruturado; LLM só se inconclusive | Q12 | Alta |
| 15 | Hierarquia 12-níveis preservação; budget adaptativo; `pre_commit_reflexion`; stop-on-exhaust por stage | Q2, Q8, Q10 | Alta |
| 16 | Compositionality test; reward sharing mechanism; quota 20% antipattern no retrieval; schema per-skill com parametric_coverage; pipeline_core.py herança | Q3, Q7, Q9, Q11 | Média |
| 19 | Threshold mínimo match_score cross-registry | Q7 | Alta |
| 20 | `dependency_closure` computado; regra "agente não toca thresholds"; fixture provenance audit; oracle cross-family; canary longitudinal; agent_prompts/*.md sempre yellow-zone mínimo | Q3 | Alta |
| 21 ↔ 20 | Pipeline de promoção cross (fixture do chaos vira fixture canônica) | Q3 | Média |

## Tabela mestra — prompts novos propostos

| # | Prompt | Origem | Esforço estimado | Dependências |
|---|---|---|---|---|
| 25 | PRM training pipeline (trajectories do eval harness) | Q1 | 10d | 6, 11 completos |
| 29 | C_LLM measurement — quanto signal cada modelo usa | Q2 | 5d | 15 |
| 30 | Heuristic unlearning — retração de lessons/antipatterns | Q3 | 4d | 11, 04 |
| 31 | Cross-config invalidation (embedding, model change) | Q3 | 3d | 19 |
| 32 | Tree search intra-ticket no inner_agent | Q4 | 12d | 07 + 18 **completos e estáveis** |
| 33 | Plan Structural Gate (simbólico pré-execução) | Q5 | 3d | — |
| 34 | Stage Classification Gate (trivial/medium/complex) | Q6 | 2d | — |
| 35 | Determinism-first refactor (inversão do padrão) | Q6 | 15d | 06, 34 |
| 36 | Multi-instance self-critique (pre-commit) | Q8 | 3d | 15 |
| 37 | Multi-tenant antipattern aggregation (privacy) | Q9 | 30d | 11, 41 |
| 38 | Skills validation canary (análogo 20 para knowledge) | Q9 | 8d | 20, 37 |
| 39 | AC Gaming Detector (4 sinais Decarolis) | Q10 | 4d | 10, 15 |
| 40 | Screening AC Menu (Laffont-Tirole) | Q10 | 3d | — |
| 41 | Ontology alignment — pipeline_core.py herda core.py | Q11 | 12d | — |
| 42 | Compliance gate per-repo (Ajithp pattern) | Q12 | 6d | 12 |

---

## Top 5 descobertas cross-query (emergência)

### 1. Moat é sempre multi-tenant (Q9 ↔ Q11)
A conclusão mais surpreendente: **roadmap 1-21 não gera moat estrutural**. Q9 identifica ausência de network effects; Q11 mostra que **ontology alignment é pré-requisito** para cross-tenant compat. Não são duas discussões — é uma: "quer moat → ontology → multi-tenant".

### 2. Symbolic > LLM em MAIS stages do que o roadmap assume (Q6 ↔ Q12)
Q12 mostra que gates 13+14 são exemplares de displacement correto. Q6 generaliza: 50-70% dos "stages LLM" do pipeline podem migrar para tool-first. Isso inverte o *default mindset* do roadmap atual ("LLM first, tool gate secondary") → deveria ser "tool first, LLM escalation". **Prompt 35 (Determinism-first refactor) é meta-mudança**, não feature.

### 3. AC design + plan design são problema único (Q5 ↔ Q10)
Lemon plan (Q5) e AC gaming (Q10) são duas faces da mesma moeda: principal-agent adversarial. Bajari-Tadelis (FP vs C+) + Akerlof (signalling) + Laffont-Tirole (screening) formam um **framework unificado de contract design** que o roadmap não aplica. Ticket template forçando sempre FP (tests binários) reproduz patologia da Lei 8.666 no Brasil. **Prompt 33 + 39 + 40 são uma família**.

### 4. Oracle atual é caro e mal-calibrado (Q1 ↔ Q8)
Olken 2007 + Zamboni-Litschig aplicado a oracle_critic: intensidade não importa, certeza sim. Oracle sempre em todos os stages = desperdício. Oracle em red-zone determinístico + 15-25% estocástico = mesmo deterrence, 60% menos custo. Além disso, "oracle" hoje pode ser multi-instance Claude — não é externo genuíno. **Multi-family default** é ajuste cheap com impacto estrutural.

### 5. Registry feedback está cego por falta de BFO distinction (Q7 ↔ Q11)
Pipeline hoje armazena antipatterns (continuants) mas não matches (occurrents). Feedback loop do prompt 11 é ilusão: sem registro de "este antipattern foi retrieved em ticket X e foi útil sim/não", não há como calibrar decay. Isto é bug estrutural, não feature request. **Prompt 11 precisa refactor, não só add features.**

---

## Riscos transversais nas mudanças propostas

1. **Sobreposição com metaxon core.py**: Q11 propõe herança; cuidado com divergência se core.py evoluir.
2. **Custo engineering acumulado**: 15 prompts novos × 3-12 dias = 80-150 dias adicionais. Priorização obrigatória — nem todos entram.
3. **Moat (Q9) é decisão de produto**: não técnica. Sem anchor de demanda multi-tenant, prompts 37-38 são especulação.
4. **Determinism-first refactor (35)** é refactor de arquitetura, não feature. Blast radius alto. Priorizar pequenos passos (34 primeiro, 35 só depois de validação).

## Priorização sugerida (top 10 por Pareto ROI)

1. **Prompt 07 + `parallel_attempts: N`** — 1 dia, 10pp ganho SWE-bench estimado (Q4)
2. **Prompt 02 oracle_sampling_policy** — 1 dia, ~50% redução custo oracle (Q1, Q8)
3. **Prompt 33 Plan Structural Gate** — 3 dias, previne lemon plans (Q5)
4. **Prompt 34 Stage Classification** — 2 dias, -30% LLM calls (Q6)
5. **Prompt 11 refactor continuant/occurrent** — 3 dias, destrava feedback quantitativo (Q7, Q11)
6. **Prompt 15 hierarquia 12-níveis + pre_commit_reflexion** — 4 dias, reduz oracle load (Q2, Q8)
7. **Prompt 12 ordem estrita symbolic→neural** — 2 dias, -70% LLM reviewer calls (Q12)
8. **Prompt 06 métricas marginal_lift + llm_call_ratio** — 2 dias, observabilidade do roadmap (Q1, Q6)
9. **Prompt 20 fixture provenance + cross-config invalidation** — 4 dias, anti-Goodhart em self-mod (Q3)
10. **Prompt 41 ontology alignment** — 12 dias, pré-requisito para moat (Q9, Q11)

**Total Top 10**: ~34 dias — cabe em ~Fase 4-5 do roadmap original.

---

## Fontes
- Queries individuais: `01-prm-vs-rubric.md` … `12-neurosymbolic-gates.md` no mesmo diretório.
- KB vault metaxon: `wiki/concepts/*.md` consumidos com identifier `[L0]`/`[L1]`.
- Roadmap: `~/projects/claude-pipeline/docs/prompts/IMPLEMENTATION_ROADMAP.md`.

## Gaps de corpus identificados
Priorizar ingestão:
1. **Matějka & McKay 2015** — rational inattention discreta (Q2)
2. **MAST taxonomy arXiv 2503.13657** — 14 failure modes (Q7) — já na fila ingest
3. **LATS + RAP + Tree of Thoughts** (Q4)
4. **Spence 1973** — job market signaling (Q5)
5. **Acemoglu-Restrepo 2019 JEP** — reinstatement framework (Q6)
6. **FrugalGPT Chen et al. 2023** — model cascades (Q6)
7. **Pan et al. 2024** — reward hacking em LLM agents (Q10)
8. **Laffont & Tirole 1993** — incentive theory procurement (Q10) — já na fila

## Confiança geral
**Alta.** 8 das 12 queries com confiança alta (corpus robusto), 3 média (transferência sólida mas magnitude especulativa), 1 média-baixa (Q4 tree search — corpus ausente, resposta paramétrica).

---

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- O pacote de mudanças de maior ROI (Top 10) melhora qualidade e custo do pipeline sem aumentar risco operacional.

**Experiment**
- Executar rollout em 2 sprints com:
  - baseline frozen de métricas do eval harness,
  - feature flags por prompt alterado,
  - análise incremental por coorte de tickets.
- Documento operacional gerado em `SUMMARY_EXECUTABLE.md`.

**Success Metric**
- `approve_rate` +3pp ou melhor.
- `cost_per_ac` -20% ou melhor.
- `false_approve_rate` sem piora.
- Pelo menos 7/10 itens do Top 10 entregues com DoD verificado.

## Estimate Classification (Global)

| Claim class | Status |
|---|---|
| Métricas históricas de papers econômicos/auditoria | Measured (external) |
| Ganhos/custos esperados no claude-pipeline | Projected (to validate via eval harness) |
| Estimativas de esforço em dias | Projected (engineering estimates) |

## Output adicional

- Plano de execução pronto para sprint planning: `SUMMARY_EXECUTABLE.md`
