# Q1 — Process Reward Models vs rubric LLM-as-judge para gates adversariais

**Query**: trade-off custo/ruído/treinabilidade para `post_stage_critic` (rubric LLM) + `oracle_critic` (N modelos) do claude-pipeline. Como audit-risk e audit-deterrence informam o mix ótimo?

## Resposta

### O que PRMs resolvem que rubric LLM-judge não resolve

**Rubric LLM-as-judge** (o que o pipeline já faz em `post_stage_critic.py`):
- Baixo custo de bootstrapping (escreveu prompt e tem um juiz)
- Alto ruído: [[llm-as-judge]] documenta 12 vieses sistemáticos; self-enhancement até 16.1% de erro (CALM), GPT-4o **quase random em tarefas difíceis** (JudgeBench). Inflate a métrica em benchmarks fáceis.
- Não-treinável: melhora só via prompt engineering; sinal de eval não fecha loop
- Self-enhancement é o ponto crítico: o inner_agent é Claude, o critic é Claude — mesmo modelo gera e julga = loop inflacionário documentado

**PRM (Process Reward Model)**:
- Modelo *treinado* em trajectories rotuladas (stage-by-stage, não só outcome)
- Requer dataset — justamente o que o eval harness (prompt 06) vai produzir
- Ruído calibrável (loss decrescente, não prompt rewrite)
- Detecta *process errors* (o agente tomou passo errado no turn 7) vs só *outcome errors* (test falhou no final) — esse é o diferencial que rubric LLM perde

### O que audit-deterrence-corruption (Olken 2007) ensina

Efeito da auditoria é **não-linear**: o que importa é certeza percebida de auditoria, não intensidade. 4%→100% causa ≈8pp queda em fraude; aumentar intensidade dentro do regime "certa" não dá ganho proporcional.

**Aplicação ao claude-pipeline**: rodar oracle_critic (N=3 modelos) em **100% dos stages** é overkill. O que Olken sugere é: garantir probabilidade **alta e previsível** de auditoria em stages críticos, não auditoria densa em todos. Isso economiza 40-60% do custo de oracle se combinado com stage-risk scoring.

**Aplicação direta**: introduzir campo `stage.audit_prob` no profile — stages triviais (formatting, imports) recebem auditoria estocástica baixa, stages de alto blast radius (migrations, auth, crypto) recebem auditoria determinística N=3. Isso está **ausente** do roadmap atual.

### O que audit-risk-rent-extraction (Zamboni & Litschig 2018) ensina

Auditoria externa e accountability local são **substitutos, não complementos**. Onde a accountability local é forte, efeito marginal da auditoria externa é menor.

**Tradução**: `oracle_critic` (auditoria externa forte) e `post_stage_critic` (rubric local) são parcialmente **substitutos**. O roadmap atual trata como complementares (prompt 02 empilha em cima de post_stage_critic). Se Zamboni-Litschig generaliza, há diminishing returns mensuráveis em rodar os dois em stages onde o rubric local já detecta desvio.

**Aplicação direta**: eval harness (prompt 06) deveria reportar **marginal lift** de oracle_critic dado que post_stage_critic existe, não taxa absoluta. Se marginal lift < 3pp em tickets simples, oracle é desperdício nessa classe.

### Mecanismo de rent extraction (por que o mix importa)

O agente (inner_agent) tem incentivo perverso: produzir solução que *passa* no critic sem satisfazer AC real. Isso é análogo ao burocrata Zamboni-Litschig: otimiza para o sinal observável (rubric), não para o objetivo final (ticket resolvido). [[self-preference-bias-llm-judge]] + [[curse-of-knowledge-llm-judge]] amplificam: mesmo modelo julga seu próprio output com viés sistemático.

**Gates adversariais hierarquizados** (baseado em audit theory):
1. Rubric local barato (post_stage_critic) — deterrence diária
2. Oracle multi-model **estocástico em stages random** — raridade + surpresa aumenta deterrence sem custo proporcional
3. PRM (quando treinável) — detecta process-level rent extraction que outcome-level gates perdem

### Trade-off formalizado

| Dim | Rubric LLM | Oracle N-model | PRM trained |
|---|---|---|---|
| Custo/stage | $0.01-0.05 | $0.05-0.20 | $0.001 (inference) + $$$$ one-time training |
| Ruído | Alto (12 biases) | Médio (debate reduz ~30%) | Baixo se dataset bom |
| Bootstrappable | Imediato | Imediato | Precisa eval harness maduro |
| Detecta process error | Não | Parcial | Sim |
| Self-enhancement vuln | Sim | Parcial (se modelos diferentes) | Não (modelo separado) |
| Treinável com feedback | Não | Não | Sim |

Equilíbrio ótimo (aterrado no roadmap):
- **Curto prazo** (Fase 4): rubric em 100%, oracle estocástico em 30% + determinístico em stages red-zone. **Isto muda o prompt 02** — adicionar `oracle_sampling_policy: {deterministic_stages: [...], stochastic_rate: 0.3}`.
- **Médio prazo** (pós-Fase 6): usar eval harness (06) + antipattern registry (11) + lessons.jsonl como dataset base para treinar PRM. **Adicionar prompt novo 25** (PRM training).
- **Longo prazo**: PRM substitui post_stage_critic em stages conhecidos; oracle vira reservado para stages novos ou red-zone.

### Implicação para o test quality gate (prompt 10)

Prompt 10 é **exatamente o PRM que falta**, mas implementado como regras fixas (assertion density, SUT linkage, mutation smoke). É um PRM simbólico estático. Três consequências:

1. **Não aprende**: falso-positivos/negativos não retroalimentam o gate. Isto muda o prompt 10 — adicionar loop de feedback: test_quality_gate.verdict → eval_harness.ground_truth → ajuste de thresholds.
2. **Cobertura estreita**: detecta só quality de *testes*, não de *código*. Um PRM treinado generalizaria.
3. **Mutation smoke (3 tipos, cap 9)** é proxy barato de PRM — deveria ser ampliado para diff-level mutation, não só test-level, uma vez que PRM existe.

## Fontes wiki

- `[L0]` [[audit-deterrence-corruption]] — Olken 2007, auditoria não-linear (4%→100% = -8pp)
- `[L0]` [[audit-risk-rent-extraction]] — Zamboni & Litschig 2018, substitutabilidade auditoria/accountability, -15-20% irregularidades
- `[L1]` [[llm-as-judge]] — 12 biases CALM, JudgeBench (near-random em hard tasks), CARMO (dynamic > static rubric)
- `[L1]` [[multiagent-debate-du-2023]] — debate estrutural como mitigation de self-enhancement; instâncias mesmo-modelo compartilham priors (limitação)
- `[L1]` [[self-preference-bias-llm-judge]] — mecanismo de bias em self-evaluation

## Fontes raw verificadas
- `raw/papers/zamboni-litschig-2018-audit-risk-rent-extraction.md` (stub)
- `raw/papers/olken-2007-monitoring-corruption.md` (stub)
- `raw/papers/calm-llm-judge-biases.md` via wiki
- `raw/papers/multiagent-debate-factuality.md` via wiki

## Confiança
**Média-alta.** A tradução audit theory → pipeline gates é analogia estrutural forte (mecanismo: principal-agent com audit cost, mesmo formato). Específicos numéricos (8pp, 15-20%) são do contexto original (Indonésia, Brasil procurement) — direção transfere, magnitude não.

## Gaps
- **Corpus ausente**: papers específicos sobre PRMs em LLM agents (OpenAI Let's Verify Step by Step, DeepSeek-R1 PRM). Não indexados no wiki — seriam fontes primárias diretas.
- **Mutation testing theory**: prompt 10 usa mutation smoke sem literatura formal; wiki não tem artigo sobre mutation testing como PRM proxy.

## Mudanças no roadmap (sumário)
- **Prompt 02**: adicionar `oracle_sampling_policy` (stochastic+deterministic mix baseado em stage-risk) — baseado em Olken.
- **Prompt 02**: eval harness reporta *marginal lift* de oracle, não absoluto — baseado em Zamboni-Litschig substitutability.
- **Prompt 10**: adicionar feedback loop test_quality_gate → eval ground truth → threshold adjustment.
- **Prompt novo 25** (proposto): PRM training pipeline sobre trajectories do eval harness. Dependência: Fases 4+6 completas.

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Oracle com política mista (determinístico em red-zone + amostragem estocástica fora dela) mantém qualidade e reduz custo.

**Experiment**
- Rodar `eval harness` em 3 braços no mesmo conjunto de tickets:
  1. `oracle_full` (oracle em 100% dos stages),
  2. `oracle_mixed` (red-zone 100% + 20% amostragem),
  3. `oracle_off` (controle inferior).
- Reportar `pass_rate`, `cost_per_ac`, `marginal_oracle_lift_pp`, `false_approve_rate`.

**Success Metric**
- `oracle_mixed` com `pass_rate` dentro de -1pp de `oracle_full`.
- `cost_per_ac` ao menos 25% menor que `oracle_full`.
- `marginal_oracle_lift_pp` >= 3pp apenas nas classes de ticket onde oracle permanecerá obrigatório.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| 8pp (Olken) e 15-20% (Zamboni-Litschig) | Measured (external literature) | Medido em contexto não-pipeline. |
| "oracle em 100% é overkill no pipeline" | Projected | Precisa A/B em eval harness. |
| "economia 40-60% com política mista" | Projected | Hipótese operacional; validar por classe de ticket. |
