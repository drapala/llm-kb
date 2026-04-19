# Q8 — Audit deterrence em agentes: oracle externo vs reflexion interno

**Query**: mix ótimo entre gates externos adversariais (oracle multi-model) e auto-correção interna (reflexion)?

## Resposta

### Framing

Q1 cobriu PRM vs rubric. Aqui o eixo é diferente: **externo vs interno**. Reflexion é mecanismo interno (o agente se auto-corrige); oracle é externo (outro agente julga).

Zamboni & Litschig 2018 (linha conceitual): **auditoria externa e accountability local são substitutos, não complementos**. Olken 2007: intensidade importa menos que certeza.

### Eixos independentes

| Eixo | Interno (reflexion, self-critique) | Externo (oracle, human review) |
|---|---|---|
| Custo marginal | Baixo (mesmo modelo já carregado) | Alto (N model calls paralelos) |
| Self-enhancement bias | **Alto** (até 16% CALM) | Baixo se modelo diferente |
| Detecção de genuine blind spots | **Baixa** (blind spot é não saber o que não sabe) | Alta |
| Velocidade | Rápido | Lento (N calls paralelos mas síncronos) |
| Deterrence signal | Fraco (agente negocia consigo) | Forte (auditoria externa = Olken) |
| Novidade de perspectiva | Zero | Positiva se diversity de modelos |

### A trap do all-internal

Reflexion puro (prompt 15, context compaction + self-critique) cria loop fechado:
- Agente escreve código
- Mesmo modelo julga código
- Mesmo modelo reflete sobre falha
- Mesmo modelo aplica lição

[[autonomous-kb-failure-modes]] documenta isto como "Layer 3 Circularity Problem". No pipeline, equivalente: inner_agent → post_stage_critic (mesma família de modelos) → self-reflection → retry. Loop 100% circular se não houver oracle externo ou test determinístico.

### A trap do all-external

Oracle em todos os stages em todos os tickets: custo explode (3-5× por gate). Zamboni-Litschig: **diminishing returns onde accountability local já cobre**. Post-stage critic + test quality gate já detectam maioria. Oracle redundante adiciona <3pp em maioria dos casos.

### Mix ótimo derivado

Olken: certeza > intensidade. Tradução:
- **Reflexion em 100% dos stages** (barato, imediato) — como linter roda sempre.
- **Oracle em subset estratégico** com política **determinística + probabilística**:
  - **Determinístico**: stages de red-zone (prompt 20 zonas) — sempre oracle.
  - **Probabilístico**: 15-25% dos stages green/yellow zone, aleatoriamente selecionados — cria certeza de que *alguns* serão auditados sem custo proporcional.
  - **Trigger-based**: oracle automatic se reflexion indicar baixa confiança.

Isso é **Olken aplicado**: certeza de auditoria > intensidade. Agente sabe que stages red-zone sempre auditados + qualquer stage pode ser auditado → deterrence sem custo explosivo.

### Reflexion como mecanismo de accountability local forte

Zamboni-Litschig: forte accountability local → auditoria externa tem efeito marginal menor.

**Fortalecer reflexion como accountability local**:
- Reflexion hoje no pipeline é implícito (inner_agent re-executa após failure). Deveria ser **explícito**: rodada de "self-critique" antes de commitar, com rubric forte.
- Custo: 1 LLM call extra por stage.
- Benefício: reduz casos que chegam ao oracle com qualidade baixa (reduz carga de oracle). Análogo a "accountability local forte reduz demanda por auditoria externa".

**Isto muda o prompt 15** (context compaction, onde reflexion moraria): adicionar `pre_commit_reflexion: required` como stage implícito — agente critica próprio diff contra exit_condition antes de sinalizar completed.

### Ordem ideal de gates (defesa em profundidade)

1. **Determinístico barato** (scope_precheck, secret_scan, hook_enforcement): sempre, primeiro — Q6 displacement
2. **Reflexion interno** (pre_commit_self_critique): sempre, segundo — accountability local
3. **Rubric LLM local** (post_stage_critic): sempre, terceiro — Q1
4. **Oracle externo multi-model**: determinístico em red-zone + probabilístico 15-25% + trigger-based — Olken certainty
5. **Humano**: PR review local (prompt 05) — final, determinístico em repos de trabalho

### Reflexion com anti-cascade structural

Reflexion puro sofre de **confirmation bias em cascata**: agente justifica seu próprio erro. Du et al. 2023 ([[multiagent-debate-du-2023]]) mostra que mitigation é **debate estrutural** — múltiplas instâncias do mesmo modelo com histórico de conversação distintos.

**Implicação**: reflexion no pipeline deveria ser **multi-instance self-critique**, não single-instance. Custo: 2-3× LLM calls (mas ainda mesmo modelo, não oracle externo caro). Estrutura:
- Instância 1 escreve diff
- Instância 2 (fresh context, só lê diff + AC + exit_condition) critica
- Instância 1 responde à crítica
- Consenso ou escalar para oracle externo

Isto é meio-termo entre reflexion puro e oracle — "oracle barato via self-instances". [[multiagent-debate-du-2023]] documenta que instâncias compartilham priors do modelo, então isso **não substitui** oracle multi-family; complementa.

**Isto muda o prompt 15 ou cria prompt 36**: Multi-instance pre-commit critique.

### Quando o mix certo é zero oracle externo

Casos onde reflexion + rubric + test determinístico cobrem:
- Ticket bulldozer profile, escopo simples (< 50 LOC diff, 1 AC claro)
- Stage triviais (imports, formatting)

Zamboni-Litschig predict: forte accountability local (tests + rubric cobrindo) → marginal lift de oracle ≈ 0. Gastar oracle aqui é desperdício.

**Isto muda o prompt 6** (eval harness): reportar **marginal lift de oracle por ticket class**. Profiles onde lift < 3pp → desabilitar oracle nesse profile.

### Quando reflexion sozinho é insuficiente e precisa oracle

- Stage red-zone (prompt 20): sempre oracle determinístico.
- Oracle disagreement histórica naquele arquivo/módulo (lesson retrieved): oracle esta vez também.
- Attempt > 1 com failure pattern novo (antipattern não matched): oracle para detectar padrão.
- Diff cross-subsystem (tocou módulos de categorias diferentes): oracle porque rubric local é treinado por categoria.

Isto são gatilhos explícitos para escalação — ausentes do roadmap.

### Analogia com corporate governance

Interno = CFO auditing próprio departamento  
Externo = Big Four auditing  
Best practice (Sarbanes-Oxley): ambos, com **separation of duties** explícita.

Pipeline hoje não tem separation:
- `inner_agent` e `post_stage_critic` usam mesma família de modelos (Claude)
- `oracle_critic` pode ser configurado para múltiplos modelos mas default não é

**Isto muda o prompt 02**: default de `oracle_models` deve ser **multi-family** (Anthropic + OpenAI + open-weight), não multi-instance Claude. Caso contrário, "externo" é externo só nominalmente.

## Fontes wiki
- `[L1]` [[audit-deterrence-corruption]] — Olken 2007, certeza > intensidade
- `[L1]` [[audit-risk-rent-extraction]] — Zamboni-Litschig, substitutabilidade auditoria/accountability local
- `[L1]` [[multiagent-debate-du-2023]] — debate estrutural como anti-cascade
- `[L1]` [[self-improving-agents]] — Reflexion, grounded feedback via tests executáveis
- `[L1]` [[autonomous-kb-failure-modes]] — Layer 3 Circularity Problem
- `[L1]` [[llm-as-judge]] — self-enhancement bias 16%

## Confiança
**Alta.** Framework audit é bem mapeado ao domínio. Claims numéricas (15-25% sampling, 3pp lift threshold) são heurísticas — precisam calibração pelo eval harness.

## Gaps
- Sem paper ingerido sobre **oracle model family diversity** empírico (se modelos diferentes produzem veredictos genuinamente independentes).

## Mudanças no roadmap
- **Prompt 15**: adicionar `pre_commit_reflexion` como stage obrigatório implícito antes de commit (accountability local forte).
- **Prompt 02**: (a) default `oracle_models` multi-family; (b) política determinística + probabilística (15-25%) + trigger-based; (c) gatilhos explícitos para escalação a oracle.
- **Prompt 06**: reportar **marginal lift de oracle** por ticket class; auto-desabilitar em profile onde lift < 3pp.
- **Prompt novo 36**: Multi-instance self-critique — instância fresh context critica diff da primeira, antes de oracle externo. "Oracle barato" intermediário.
- **Prompt 09** (escalation): adicionar triggers de oracle (não só human): attempt>1 novo padrão, diff cross-subsystem, lesson com oracle disagreement histórica.

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Mix reflexion+oracle amostrado mantém deterrence com menor custo que oracle sempre ativo.

**Experiment**
- Três políticas em paralelo:
  1. `oracle_full`,
  2. `oracle_mixed` (red-zone 100% + 20% sample),
  3. `oracle_trigger_only`.
- Coletar `cost_per_ticket`, `false_approve_rate`, `security_escape_rate`, `review_reopen_rate`.

**Success Metric**
- `oracle_mixed` com `false_approve_rate` não pior que `oracle_full` por >0.5pp.
- `cost_per_ticket` -25% ou melhor vs `oracle_full`.
- `review_reopen_rate` estável ou melhor.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| Deterrence: certeza > intensidade (Olken) | Measured (external literature) | Evidência robusta em auditoria pública. |
| Sampling 15-25% como ponto ótimo | Projected | Parâmetro inicial para calibração local. |
| Lift threshold de 3pp para manter oracle | Projected | Regra de decisão operacional, não fato empírico. |
