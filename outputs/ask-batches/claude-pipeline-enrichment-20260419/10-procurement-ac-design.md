# Q10 — Procurement contract design → design de ACs para agentes

**Query**: anti-gaming, renegotiation, variety gap aplicam ao design de acceptance criteria para agentes?

## Resposta

### Mapping estrutural

| Procurement concept | AC (Acceptance Criterion) analog |
|---|---|
| Contract (FP vs C+) | AC specification style (test-binary vs descriptive) |
| Scope ambiguity | AC underspecification |
| Aditivos (renegotiation) | AC revision mid-execution |
| Bid rigging | Agent gaming do AC |
| Variety gap (V(regulator) < V(regulated)) | AC complexity gap (AC linguagem estrutural não captura o domínio) |
| Reference price (SINAPI) | Expected-range para métricas de stage |

Procurement tem **décadas de maturidade em contract design sob adversarial agent**. AC design em agentic pipelines é nascente. Transferência é rica.

### Bajari-Tadelis: FP vs C+ aplicado a AC

**FP (Fixed-price)**: contratante assume risco, incentivo forte para redução de custo, **caro quando escopo muda**. Tradução: AC **rígido e binário** (test-based, "test X passes") — incentiva agente a resolver direto, mas cai em hold-up quando requisito real divergia do AC.

**C+ (Cost-plus)**: comprador assume risco, incentivo fraco, **barato quando escopo muda**. Tradução: AC **descritivo e interpretável** ("resolver o problema descrito no ticket") — adapta mas permite agente alegar progresso subjetivo.

**Predição Bajari-Tadelis**: projetos simples → FP domina; complexos → C+ domina. Aplicado:
- **Ticket simples** (bug fix, 1 AC claro): AC deve ser **FP-style** — test-binary. Pipeline atual já tende a isso.
- **Ticket complexo** (refactor cross-module, UX change): AC deve ser **C+-style híbrido** — AC descritivo + sub-ACs de test parciais. Pipeline atual força FP-style sempre → reproduz o problema da Lei 8.666.

### Aditivos = AC revision mid-execution

Lei 8.666 força FP → aditivos estruturalmente inevitáveis para projetos complexos. Pipeline equivalente: se o ticket é forçado a ter só test-binary ACs mesmo sendo complexo, stages vão "renegociar" implicitamente — agente pede escalação, humano libera, AC muda na prática.

Bajari-Tadelis identifica **2 tipos de aditivos**:
- **Eficientes**: mudança genuína de escopo, precoce, justificado
- **Estratégicos**: underbid deliberado + extração posterior

Aplicado ao claude-pipeline: **escalation pattern analysis** (prompt 09) pode distinguir:
- Eficiente: escalação cedo no stage 1-2, com question específica, budget baixo consumido
- Estratégico: escalação tardia, após muitos turns consumidos, pedindo expansão de `allowed_files`

**Isto muda o prompt 09**: adicionar classifier de escalation tipo (efficient/strategic). Strategic escalation sobe flag para humano *antes* de auto-decide.

### Decarolis — bid rigging = agent gaming do AC

Decarolis: 2 canais de manipulação. Mapeio para AC gaming:

**Canal 1 — Bid rigging com propostas coordenadas**  
Análogo no pipeline: agente submete **tests** que passam trivialmente + **código** que atende ao test mas não ao AC real. "Cooperation" entre code-writer turn e test-writer turn do mesmo agente. Post-stage critic vê test passing → aprova.

Detecção (inspirado Decarolis ownership overlap): **test e código escritos no mesmo turn, pelo mesmo agente, sem revisão externa**. Red flag. Já detectado parcialmente por `test_quality_gate` (assertion density, SUT linkage) — mas não especificamente por "same-turn authorship".

**Isto muda o prompt 10**: adicionar check "test file modified in same agent turn as SUT" → requer test separation ou human/oracle approval.

**Canal 2 — Exploração da regra de exclusão por média**  
Itália usa average-bid auction, agente manipula média. Análogo pipeline: exit_condition baseado em **média** de métricas (ex: "mean coverage > 80%") → agente escreve tests trivialmente passando para arrastar média, code real tem coverage 0%. Agregação oculta variância.

Defesa: exit_conditions em **min, max, ou distribuição**, não média. `p95 coverage > 70%` é mais robusto que `mean`.

**Isto muda o prompt 10 e design de AC**: evitar agregações ingênuas nos exit_conditions.

### Incentive theory (Laffont-Tirole) — AC como contrato ótimo

Laffont-Tirole prescreve contrato ótimo quando:
- Principal observa outcome mas não effort
- Agente tem custo privado

Pipeline: principal (orchestrator) observa diff + test pass/fail. Não observa **qualidade intrínseca** do diff (pode passar test mas ser frágil). Agente tem custo privado (tokens/turns).

Contrato ótimo Laffont-Tirole: **high-powered incentives + screening contracts** (oferece menu, agente autoseleciona). Aplicado:
- **Screening menu**: ticket oferece 2 ACs ao agente — "Pragmatic AC" (permissive, test-based, low-reward) e "Rigorous AC" (incluindo property-based tests, high-reward). Agente escolhe baseado em custo real. Self-selection revela complexidade.

Isso é design inovador **não no roadmap**. Inspirado Laffont-Tirole.

### Procurement-variety-gap: AC complexity gap

Ashby's law applied: V(AC) precisa ≥ V(domain_problem). Se AC é simples demais para problema complexo, sistema fica subespecificado.

[[procurement-variety-gap]] formaliza Lei 8.666 como "mandato de V(R)=1 para todos os projetos". AC em pipeline tem análogo se template de ticket força V fixo (ex: "sempre 3 sub-ACs"). Problemas complexos violam isso.

**Implicação**: ACs devem ter **variety matching**. Template de ticket deveria variar estrutura com complexity estimate:
- Simple: 1 AC binário
- Medium: 2-3 ACs com exit conditions explícitos
- Complex: 1 AC descritivo + N sub-ACs de aspectos (performance, correctness, security, maintainability)

**Isto muda o ticket_validator**: não validar só forma, validar **variety match** com complexity signal.

### Procurement-manipulation-signals aplicado

Decarolis lists sinais observáveis de rigging:
1. Empresas com sócios sobrepostos
2. Preços agrupados próximo de referência de exclusão
3. Vencedor com preço acima de referência de mercado
4. Mesmo fornecedor >50% contratos por categoria

Análogos em agentic pipeline:
1. **Test e código mesma turn/agente** → rigging canal 1
2. **Métricas agrupadas próximo de threshold** (coverage exatamente 80% quando threshold é 80%) → rigging canal 2 (agente calibra para o mínimo)
3. **Diff maior que estimativa do planner** (análogo "preço acima de referência") → indica escopo creeping
4. **Mesmo antipattern não detectado em N tickets consecutivos** → indica registry gaming (Q7)

Cada um é sinal de gaming detectável pós-hoc. **Detector de AC gaming** (prompt novo 39) orquestra isso.

### Renegociação sob hold-up (Tirole 1986)

Hold-up: agente sabotagem após investment sunk. No pipeline: agente consome tokens em stage 5 e só então pede escalação — orchestrator paga sunk cost mesmo se negar escalação.

Tirole prescreve: **design ex-ante que reduz hold-up**. Aplicado:
- **Sub-budgets por stage, stop-on-exhaust**: agente consumiu orçamento do stage → para, não pede "mais um pouquinho".
- **Pre-commitment de escopo**: `allowed_files` + `exit_condition` são commitments, mudanças exigem full re-plan, não aditivo.

Prompt 15 (context compaction) tem budget mas não stop-on-exhaust por stage. **Isto muda prompt 15**.

### Conexão direta com Q5 (lemons)

Q5 identifica lemon plan como adverse selection. Q10 complementa: **AC design é a contraparte do plan design**. Lemon plan + weak AC = rigging environment ideal.

Anti-lemon measures de Q5 (licensing, signalling) + anti-gaming de Q10 (screening menu, variety match) são complementares.

## Fontes wiki
- `[L0]` [[procurement-contract-design]] — Bajari-Tadelis, FP vs C+, aditivos
- `[L0]` [[procurement-manipulation-signals]] — Decarolis, 2 canais, sinais detectáveis
- `[L1]` [[incentive-theory-procurement]] — Laffont-Tirole (stub na KB)
- `[L1]` [[procurement-renegotiation]] — Tirole 1986 hold-up
- `[L1]` [[procurement-variety-gap]] — variety match

## Confiança
**Alta.** Procurement literature tem modelos bem formalizados; transferência ao AC design é estrutural direta (principal-agent adversarial).

## Gaps
- Laffont-Tirole full text é stub no wiki — screening menu prescription mereceria expansion.
- Wiki sem paper específico sobre **spec gaming em RL/LLM agents** — seria confirmação domain-native.

## Mudanças no roadmap
- **Prompt 09** (escalation): classifier efficient/strategic escalation (Bajari-Tadelis); strategic sobe flag humano antes de auto-decide.
- **Prompt 10** (test quality gate): check "test e código same-turn authorship" → require separation; evitar agregações ingênuas em exit_conditions.
- **Ticket validator / plan structural gate (Q5)**: variety match com complexity signal; templates variando por complexity.
- **Prompt 15**: sub-budgets por stage com stop-on-exhaust (Tirole anti-hold-up).
- **Prompt novo 39 (proposto)**: AC Gaming Detector — 4 sinais Decarolis-inspired pós-hoc.
- **Prompt novo 40 (proposto)**: Screening AC Menu — Laffont-Tirole, oferece 2 ACs ao agente; self-selection revela complexity percebida.
- **Design explicit FP vs C+ AC types**: ticket template exige classificar-se; pipeline usa validation diferente para cada.

## Sugestão de ingestão
- Laffont & Tirole 1993 *Theory of Incentives in Procurement* — já na fila, priorizar.
- Paper sobre reward hacking em LLM agents (ex: Pan et al. 2024).

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- AC design tipado (FP vs C+) + detector de gaming reduz escalation estratégica e retrabalho tardio.

**Experiment**
- Introduzir tipagem de AC em tickets novos e habilitar `AC Gaming Detector` em modo observação.
- Depois de 2 semanas, habilitar bloqueio gradual para sinais de alta confiança.
- Medir: `strategic_escalation_rate`, `late_stage_replan_rate`, `false_alert_rate`.

**Success Metric**
- `strategic_escalation_rate` -30% ou melhor.
- `late_stage_replan_rate` -20% ou melhor.
- `false_alert_rate` <= 10% após calibração.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| FP vs C+ trade-off (Bajari-Tadelis) | Measured (external literature) | Evidência em procurement tradicional. |
| "same-turn test+code indica gaming no pipeline" | Projected | Heurística plausível; validar precisão/recall. |
| "screening menu revela complexidade percebida" | Projected | Hipótese de desenho de contrato no domínio agentic. |
