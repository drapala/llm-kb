# Q6 — Task displacement (Acemoglu-Restrepo) reflexivo

**Query**: quais stages do próprio pipeline agêntico são substituíveis por tooling determinístico vs LLM?

## Resposta

### Framework

Acemoglu-Restrepo (2022): automação desloca tarefas, não trabalhadores. Reinstatement (2019 JEP) cria tarefas novas. Aplicado ao pipeline: **cada componente é um "trabalhador"; o humano operador é o capital**. Substituição LLM→tooling determinístico = automação; tooling→LLM = reinstatement.

Pergunta reflexiva: onde o LLM está ocupando nicho que tooling determinístico faz melhor/barato/mais confiável?

### Stages Pareto-dominados por tooling determinístico (candidatos a displacement)

| Componente atual | Implementação atual | Alternativa determinística | Ganho |
|---|---|---|---|
| `ticket_validator.py` (coherence check) | LLM rubric | Regex + AST + schema validator (pydantic) | 10-100x mais rápido, zero hallucination, auditável |
| `scope_precheck.py` | Match de filepath contra `allowed_files` | Já é determinístico — correto |
| `secret_scan_gate.py` | Regex + gitleaks wrapper | Já determinístico — correto |
| `hook_enforcement_gate.py` | Detection de husky/pre-commit | Já determinístico — correto |
| `injection_scanner.py` | Regex patterns + LLM `tool_call_reviewer` (prompt 12) | Regex é determinístico; LLM layer adiciona custo marginal duvidoso |
| `pr_checklist.py` | ? | Template-based |
| `plan_splitter.py` | ? | AST de plan.md |

### Stages atualmente LLM que deveriam ter **fallback determinístico**

1. **`post_stage_critic` em stages triviais**: se o stage é "add import", não precisa LLM critic — precisa de `pyright` ou `ruff` para validar. Deveria ter **stage classification** (trivial/medium/complex), e trivial stages usam linter + test runner apenas.
2. **`meta_planner`**: se plan já respeita estrutura canônica (AC ↔ stage 1:1, allowed_files bounded), não precisa LLM meta-planning. Só precisa quando AC count > N ou complexity signal.
3. **`failure_classifier`**: classificar falha por tipo (test fail, import error, type error, timeout) é AST/regex sobre traceback, não LLM. Confirmar se já é determinístico.

### Stages genuinamente LLM-necessárias (não-automatizáveis sem perda)

- **`inner_agent`**: escrever código novo ou adaptar é LLM-core
- **`planner`**: decompor ticket em stages requer compreensão semântica
- **`rule_curator` / `antipattern_miner`**: extração de padrões abstratos é síntese, precisa LLM
- **`local_pr_review`**: adversarial reasoning precisa LLM
- **`investigator`**: geração de hipótese abdutiva precisa LLM

### Reinstatement — tarefas NOVAS que o pipeline cria (e onde LLM é único capaz)

Acemoglu-Restrepo 2019: reinstatement cria tarefas novas que só humanos (ou no caso, LLMs) podem fazer. Pipeline reinstatement candidates:
- **Cross-stage integration narrative**: "stage 1 mudou a API assim; stage 2 precisa adaptar por isso". Narrativa cross-turn não é reduzível a diff.
- **Lesson synthesis**: destilar heurística abstrata de N failures específicas — puramente LLM.
- **Ticket enrichment pré-planning**: ticket underspecified → elaboração em ACs falsificáveis. Prompt 08 (investigator) já faz para incidentes; *deveria fazer para tickets comuns também*.

### Displacement percentual estimado

Aplicando A&R: se 50-70% das tarefas atualmente-LLM podem migrar para tooling determinístico, isso reduziria custo por ticket em **40-60%** (pois LLM calls são >80% do custo). Ganho adicional: determinismo aumenta testabilidade e reprodutibilidade do pipeline.

Mas isso depende de **custo de reinstatement** (engineering time para criar ferramentas determinísticas). Pareto practical:

| Componente | Engineering cost | Reduction token | Priority |
|---|---|---|---|
| Stage classification (trivial → linter-only) | 2 dias | -30% | **Alta** |
| Failure classification AST | 1 dia | -5% (mas correctness++) | Alta |
| Plan structural gate (Q5) | 3 dias | -2% (mas prevents lemons) | Alta |
| Determinizar ticket validator | 2 dias | -3% | Média |
| Symbol-graph scope_precheck (Q inicial) | 5 dias | correctness (reduz false positives) | Média |

### Ripple effects no pipeline

A&R: deslocamento afeta **além dos diretamente deslocados**. Aplicado:

Se `post_stage_critic` for substituído por linter em 60% dos stages (trivial class), isso **muda o skill set** que o inner_agent precisa ter:
- Hoje: inner_agent escreve código que passa LLM critic (ambíguo, pode blefar)
- Pós-displacement: inner_agent escreve código que passa linter determinístico (específico, não blefa)

**Consequência positiva**: menos self-preference bias, menos ambiguidade de critério.  
**Consequência negativa**: linter pode ser rígido demais (false positives em padrões legítimos não-canônicos) — risco de "deslocamento com ripple" tipo A&R: agente aprende a evitar padrões válidos porque linter rejeita.

**Mitigação (análoga ao reinstatement)**: exception_list.yaml auditável, revisada por humano, com TTL.

### Mecanismo do lemon analógico (conexão com Q5)

Risco específico do displacement parcial: se 60% dos stages usam tool determinístico, o planner pode **game** classificando stages complexos como triviais para evitar critic LLM rigoroso. Isso é lemon-behavior do planner.

Contra-mecanismo: classificação de stage é rechecked post-hoc por um gate separado que observa diff final — se diff tem complexidade alta em stage classificado como trivial, sinaliza gaming.

### Tarefas LLM residuais são "qualificação alta"

A&R observa: pós-deslocamento, demanda por tarefas high-skill aumenta relativamente. Pipeline pós-displacement: **demanda por planner de qualidade aumenta** (porque stages críticas são menos, cada uma mais importante). Implicação: investir em prompt do planner vale mais pós-displacement que hoje.

### Reflexão meta

Pipeline atual está no regime "LLM-first", com tooling determinístico como gate secundário. A literatura de automação sugere inversão do padrão em produção: **tooling-first, LLM como fallback/escalação**. Isso não está no roadmap explicitamente.

## Fontes wiki
- `[L0 parcial]` [[acemoglu-restrepo-task-displacement]] — 50-70% mudança salarial via automação, ripple effects
- `[L1]` [[acemoglu-restrepo-reinstatement-new-tasks]] — framework dual (referência)

## Confiança
**Média-alta.** Framework é claramente aplicável (principal-agent com substituibilidade LLM↔tool). Estimativas de percentual (40-60% custo) são projeção — exigem benchmark real.

## Gaps
- Wiki não tem artigo sobre **cost-of-LLM-call** em agentic pipelines — dados para calibrar trade-off.
- Literatura sobre **deterministic fallbacks em agentic systems** (Frugal GPT, cascades) não indexada.

## Mudanças no roadmap
- **Prompt novo (34)** — Stage Classification Gate: classifica cada stage em trivial/medium/complex pré-execução; trivial rodam sem LLM critic, usam linter/type-checker apenas.
- **Prompt 10** (test quality gate): substituir mutation smoke LLM por `mutmut`/`cosmic-ray` determinísticos onde possível.
- **Prompt 12** (injection): avaliar se `tool_call_reviewer` LLM é custo-efetivo vs regex + allowlist. Pode ser que LLM layer seja overkill.
- **Prompt 6** (eval harness): métrica nova — `llm_call_ratio` (stages LLM / stages total). Meta: reduzir sem perder qualidade.
- **Novo prompt 35** (proposto): Determinism-first refactor — inverter padrão "LLM-first com tool gate" → "tool-first com LLM escalação". Requer análise módulo-a-módulo.
- **Verificar o que já é determinístico**: alguns componentes na tabela (pr_checklist, plan_splitter, failure_classifier) podem já ser — auditoria explícita vale 1 dia.

## Sugestão de ingestão
- Acemoglu & Restrepo 2019 JEP (reinstatement) — complementa o 2022 ingerido
- FrugalGPT (Chen et al. 2023) — model cascades

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Classificação de stage + política tool-first reduz custo mantendo qualidade.

**Experiment**
- Introduzir `Stage Classification Gate` e executar em subset controlado de tickets.
- Comparar baseline vs policy nova em `llm_call_ratio`, `cost_per_ac`, `approve_rate`, `false_reject_rate`.

**Success Metric**
- `llm_call_ratio` -30% ou melhor.
- `cost_per_ac` -20% ou melhor.
- `approve_rate` dentro de -1pp do baseline.
- `false_reject_rate` <= 5%.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| 50-70% (A&R, task displacement macro) | Measured (external economics literature) | Não é métrica de pipeline diretamente. |
| 40-60% redução de custo no pipeline | Projected | Exige benchmark com telemetria de custo real. |
| Stage classification em 2 dias | Projected | Estimativa de engenharia local. |
