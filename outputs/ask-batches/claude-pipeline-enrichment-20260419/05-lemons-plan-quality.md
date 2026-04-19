# Q5 — Market-for-lemons aplicado a plan quality

**Query**: detectar plano subótimo antes de execução consumir turns caros. Signalling possível?

## Resposta

### Mapping: procurement Akerlof → pipeline planning

| Akerlof (1970) | Claude-pipeline |
|---|---|
| Vendedor conhece qualidade do carro | Planner "conhece" (gerou) complexidade real do plano |
| Comprador vê só preço + distribuição média | Orchestrator vê só plan.md formatado |
| Preço médio expulsa carros bons | Aprovação reflexiva aprova planos decentes + lemons indistintamente |
| Gresham generalizada (ruins expulsam bons) | Lemon plans que passam exit_condition shallow expulsam plans rigorosos (mais trabalhosos de validar) |

**Assimetria real no pipeline**: planner gera plan.md; orchestrator aprova em `plan_approved.txt` via humano (keranos) ou heurística (bulldozer). O humano não tem como validar se o plan é lemon em 30 segundos — ele vê forma, não conteúdo.

### Mecanismo do lemon plan

Um plan lemon tem:
- Stages que *parecem* exit_condition claro mas o AC implícito é trivial (ex: "tests pass" quando os tests são os que o agente vai escrever — auto-confirmação)
- `allowed_files` amplo demais (agente terá liberdade depois, esconde escopo real)
- Ausência de stage de integração (cada stage passa, união falha)
- Ordem de stages não-forçada (permite ao agente reordenar de modo que evidência de falha seja postergada para o fim)

Todos esses são detectáveis *antes* de executar, mas requerem **inspeção não-rasa**. Plan.md atual é inspecionado rasamente (human glance ~30s em keranos, heurística em bulldozer).

### Aplicações Akerlof → sinais observáveis

Akerlof identifica 4 instituições contrabalançadoras. Mapeio cada uma:

**1. Garantias (transfere risco ao vendedor)**  
Planner deve assinar predições falsificáveis: "stage 3 terá diff de ≤N linhas", "test quality gate passará sem excepções". Se predição falha, planner pagou preço (reputation score baixa no lesson_retriever). **Ausente no pipeline atual** — planner gera plan e some.

**Isto muda o prompt 10 e 04**: `plan.md` deve incluir `plan_predictions: [{stage, metric, expected_range}]`; rule_curator incrementa score do planner-profile baseado em acerto.

**2. Marcas (reputação via histórico)**  
Planner-profile acumula score cross-ticket: taxa de plans que resultam em approve vs revise, custo médio por AC. Isso é uma *brand* do planner. Lesson_retriever (prompt 19) já tem infra; prompt 04 rule_curator é candidato a acomodar planner-reputation.

**Gap no roadmap**: prompt 04 rule curator é para *rules*, não para *planner patterns*. Distinction importa.

**3. Licenciamento (certificação mínima)**  
Ticket validator (`coherence_gate.py`, `ticket_validator.py`) já é uma forma de licenciamento do **ticket**, não do **plan**. Falta licenciamento do plan. Proposta:
- **Plan licensing gate**: plano só "passa" se satisfaz checks estruturais mínimos:
  - Todo AC do ticket é owned por exatamente 1 stage
  - Exit_condition de cada stage é verificável sem rodar a próxima stage (não-circular)
  - `allowed_files` está bounded (não contém `**` em paths sensíveis)
  - Ordem de stages respeita dependências declaradas
- Esses são checks simbólicos sobre o plan, não LLM.

**Isto é um prompt novo (33 proposto)**: Plan Structural Gate — checks simbólicos pré-execução.

**4. Redes de confiança (monedalendor model)**  
Moneylender aceita risco alto porque conhece intimamente o cliente. Tradução: humano que já trabalhou com o planner-profile conhece seus padrões de erro. Isso é o que *keranos* tenta ser (human-in-the-loop), mas é pontual, não acumulativo. O *personal knowledge* virou dado quando lessons.jsonl é suficientemente rico — mas só se for indexado por planner-pattern, não por failure-type geral.

### Signalling possível (o que o planner pode gastar para separar de lemons)

Spence (1973) — signalling requer custo diferencial: boa qualidade paga custo menor que má qualidade para enviar o mesmo sinal. Aplicado:

- **Auto-critique pré-submit**: planner gera plan + roda self-critique com rubric forte + expõe dificuldades identificadas. Um plan bom tem dificuldades identificadas honestas; um lemon omite. Custo pequeno para bom plan, custo grande para lemon (precisa elaborar disfarce).
- **Test skeleton pré-submit**: planner escreve esqueleto de testes para cada stage *antes* da execução. Bom plan gera test skeletons coerentes com AC; lemon gera testes circulares.
- **Cost estimate com variance**: planner estima turns e custo por stage **com intervalos de confiança**. Plan honesto tem intervalos estreitos; lemon esconde incerteza em intervalos largos ou os omite.

Cada um desses é custo adicional no planner stage, mas sinal separador. **Isto muda o prompt correspondente ao planner** (não tem prompt dedicado ao planner na lista 1-21; **gap no roadmap**).

### Limite de aplicabilidade

Akerlof: "no exchange at any positive price" no caso extremo linear. Pipeline não está nesse extremo porque o **orchestrator eventualmente vê o resultado**, não só o plan. Isto é diferente do used-car market — repeated game, reputação funciona.

A armadilha real não é colapso total do mercado, é **degradação gradual**: orchestrator acumula cansaço de validar, heurísticas de aprovação ficam rasas, planner aprende que plans superficiais passam. Kurtosis para o pior pode ser lenta.

### Sintomas já visíveis que caberiam neste framework

Olhando o KB: `failure_classifier.py` existe, mas é **pós-execução**. Sintomas de lemon plan (circular exit_conditions, AC sem owner claro) poderiam ser detectados **pré-execução** com ruleset simbólico barato.

### Conexão com audit-deterrence (Q1)

Se plan licensing gate (licenciamento) existe e é **determinístico + sempre aplicado**, o planner "sabe" que não passa lemon. Olken 2007: o que importa é certeza de auditoria, não intensidade. Um gate pré-exec rodando 100% deterministicamente em 2s é mais valioso que oracle multi-model probabilístico rodando sobre o plan — baixo custo, alta deterrence.

### Inspeção baseada em procurement-manipulation-signals

[[procurement-manipulation-signals]] cataloga sinais de bid rigging (preços muito próximos, rotação, etc). Análogo em planning:
- **Stage duration rotation**: planner sempre coloca stage crítico no meio (evita último = menos escrutínio)?
- **Allowed_files clustering**: stages compartilham arquivos de forma que isola responsabilidade?
- **Exit_condition template repetition**: exit_conditions copia-colados entre stages com pequenas variações = red flag.

Detectáveis com regex/AST sobre plan.md.

## Fontes wiki
- `[L0]` [[market-for-lemons]] — Akerlof 1970, adverse selection, 4 instituições contrabalançadoras
- `[L1]` [[procurement-manipulation-signals]] — sinais observáveis de gaming
- `[L1]` [[audit-deterrence-corruption]] — certeza > intensidade
- `[L1]` [[llm-as-judge]] — critic ruidoso ≠ auditor simbólico

## Fontes raw
- `raw/papers/akerlof-1970-market-for-lemons.pdf` via wiki

## Confiança
**Alta.** Mapping estrutural direto (principal-agent com assimetria de informação). Spence signalling é extensão canônica do framework.

## Gaps
- Wiki não tem artigo sobre **Spence signalling** formal — mapping depende dele.
- Sem corpus sobre "plan-as-contract" em agentic systems.

## Mudanças no roadmap
- **Prompt novo (33)** — Plan Structural Gate: checks simbólicos pré-execução (AC ownership, exit_condition não-circular, allowed_files bounded, ordem respeita deps). Alto ROI, baixo risco.
- **Prompt correspondente ao planner** (se criar): adicionar `plan_predictions` falsificáveis + auto-critique pré-submit + test skeleton pré-submit + cost estimate com variance.
- **Prompt 04** (rule curator): estender para registrar **planner-reputation** (taxa de plans approve vs revise cross-ticket), não só rules técnicas.
- **Prompt 10** (test quality gate): check adicional — tests escritos pelo agente devem preceder código (TDD signal), senão é sinal de lemon (tests circulares).

## Sugestão de ingestão
- Spence (1973) *Job Market Signaling* — formaliza custo diferencial
- Tirole — Theory of Incentives in Procurement (já na fila)

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Um gate estrutural simbólico de plano reduz execução de planos lemon e retrabalho de stage.

**Experiment**
- A/B em tickets novos:
  1. fluxo atual,
  2. fluxo com `Plan Structural Gate` (AC ownership, circularidade, bounded scope, deps).
- Medir: `plan_reject_rate_pre_exec`, `revise_after_stage1`, `tokens_wasted_before_replan`.

**Success Metric**
- Redução >= 25% em `revise_after_stage1`.
- Redução >= 30% em `tokens_wasted_before_replan`.
- `plan_reject_rate_pre_exec` <= 20% (evitar gate hiper restritivo).

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| Mecanismo de adverse selection (Akerlof) | Measured (theory) | Estrutura teórica consolidada. |
| "Structural gate tem alto ROI no pipeline" | Projected | Requer medição em suíte real. |
| "planner reputation melhora seleção de planos" | Projected | Precisa série histórica suficiente. |
