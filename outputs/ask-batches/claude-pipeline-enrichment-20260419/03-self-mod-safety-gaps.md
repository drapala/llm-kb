# Q3 — Self-improving agents (AI Scientist, Voyager) vs self-mod protocol traffic-light + canary

**Query**: safety gaps que os papers cobrem e o protocolo manual não cobre; contexto prompts 20, 21.

## Resposta

### Failure modes documentados no AI Scientist (Lu 2024) que o prompt 20 endereça parcialmente

| Failure Mode (Lu 2024) | Traffic-light cobre? | Gap real |
|---|---|---|
| Modifica próprios scripts → recursão infinita | **Parcial** — zona vermelha impede auto-modificar gates críticos, mas zona verde permite mod em módulos novos. Um módulo "novo" pode criar tool que toca gate. | Falta **dependency analysis transitiva**: self_mod_map.yaml lista arquivos diretos, não o *dependency closure*. Se `repo_explorer.py` importa `file_reader` e mod no file_reader muda semântica, zona verde vira zona vermelha implicitamente. |
| Estende timeouts em vez de otimizar | **Não** | Nenhum mecanismo contra o agente modificar budgets/thresholds para fazer test pass. Precisa gate "agente não pode tocar thresholds de gates". |
| Baselines injustas (confirmation bias) | **Parcial** — canary compara contra baseline hardcoded | Mas a escolha dos 50 fixtures é feita por humano inicialmente; agente pode propor fixtures novas que favorecem seu próprio mod. Gap: **fixture provenance audit** — qual fixture foi sugerida por self-mod run vs human? Se self-mod propõe fixture, não conta para canary. |
| Reviewer com positivity bias | **Parcial** — oracle unanimous em yellow zone | Mesmo modelo oracle pode ter positivity bias sistemático ([[llm-as-judge]] CALM: até 16% erro em self-enhancement). Gap: **oracle modelos de famílias diferentes** (Anthropic + OpenAI + open-weight), não só multi-instância do mesmo. |

### O que Voyager (Wang et al. 2023) adiciona que o prompt 20 não tem

Voyager tem **skill library evolutiva com compositionality check**:
- Nova skill só entra na library se: (a) passa test suite, (b) é composível com skills existentes sem conflito, (c) não subsume skill existente ambígua (merge/replace decision).

Prompt 16 (loadable skills) tem schema + dedup, mas não tem:
- **Compositionality test**: skill A + skill B em sequência produz resultado esperado?
- **Skill subsumption detection**: nova skill é caso particular de skill existente?

**Aplicação**: quando prompt 16 promover skills, adicionar check de composição: rodar um teste sintético onde a nova skill + 2 skills aleatórias da library produzem resultado previsível.

### O que AiScientist 2026 (Chen et al.) ensina sobre self-mod em longo horizonte

Chen 2026 roda 24h por tarefa. Single-stage self-mod do prompt 20 (~1 ticket) não revela:
- **Drift de self-mod acumulado**: 10 mods zona-verde cada uma validada isoladamente pode produzir sistema com comportamento emergente não-testado.
- **File-as-Bus coord**: state persistente pode "esconder" regressão que não aparece em single-run canary.

**Aplicação**: canary de 10 tickets precisa virar **canary longitudinal** — N mods consecutivos rodando suite combinada, não cada mod isoladamente. Isto muda o prompt 20: adicionar `longitudinal_canary: rolling_N_mods`.

### O que Reflexion + ERL ensinam

[[self-improving-agents]]: ERL descobre que **heurísticas > trajetórias** para transfer (+7.8% vs -1.9%). Self-mod hoje persiste trajetórias ("diff X foi aplicada, canary passou") — mais próximo do caso que *não funciona*. Deveria destilar **heurística de modificação** ("mudanças em `*_retriever.py` abaixo de 50 linhas historicamente não regridem").

**Aplicação**: `self_mod_timeline.jsonl` deve ter campo `distilled_heuristic` pós-sucesso. Rule curator (04) + antipattern miner (11) rodam sobre esse log para produzir heurísticas.

### O que Absolute Zero ensina: sintetização de testes pelo próprio agente

Absolute Zero: agente gera tasks + resolve + avalia via code execution. Risco: agente otimiza para tasks que sabe resolver. O prompt 20 tem esse gap: **50 fixtures curadas por humano** é gargalo. Se humano não cura nova classe de bugs, self-mod não é testada contra ela.

**Mitigação possível (não no roadmap)**: chaos lab (prompt 21) gera "canários adversariais" sintéticos com tripwires. Mas chaos lab opera em branch isolado — não retroalimenta o pool de fixtures do 20.

**Gap**: cross-feedback chaos lab → self-mod. Descobertas do 21 (fixture que expôs regressão em zona-verde mod) deveriam ser promovidas para pool canônico do 20.

### TextGrad + auto-compactação como risco oculto

TextGrad itera prompts via "gradientes textuais". Aplicável a agent_prompts/. Se o agente tem permissão de modificar prompts (zona amarela? verde?), o protocolo 20 precisa explicitar:
- Modificação de `_security_preamble.md` = **zona vermelha sempre**, mesmo que seja "apenas adicionar exemplo".
- Modificação de qualquer `.md` em `agent_prompts/` = **zona amarela no mínimo** (porque prompt drift silencioso é auto-sabotagem do reviewer).

**Isto muda o prompt 20**: self_mod_map.yaml deve ter seção específica para `agent_prompts/` com regra "modificações em prompts de critic/reviewer/planner sempre yellow-zone com oracle unanimous, nunca green".

### Safety gaps novos que nenhum paper cobriu

1. **Mecanismo de rollback de heurística aprendida** — se lessons.jsonl acumula heurística ruim (antipattern que na verdade é padrão normal), pipeline herda sem mecanismo de unlearning. Papers assumem memory bank monotônico; prompt 20 também.
2. **Interação self-mod × RAG evolução** — prompt 19 muda embedding model → retrieval muda → antipatterns retrievados mudam → planner recebe contexto diferente → canary validado em embedding velho não generaliza. Gap em 20: `canary_invalidates_on: rag_config_change`.
3. **Adversarial self-mod via injection** — prompt 12 defende contra injection no ticket, mas o *chaos agent* do 21 é auto-instruído. Se o 21 escreve sobre arquivos que o 20 lê (cross-pipeline data flow), há vetor. Gap: isolamento entre timelines.

### Comparação de fixture volume

| Sistema | Fixtures |
|---|---|
| AI Scientist (Lu) | 3 templates × 50 ideas |
| AiScientist (Chen 2026) | PaperBench (dezenas de papers) + MLE-Bench Lite |
| Voyager | Minecraft skills emergentes, não-curadas |
| Prompt 20 roadmap | 50 fixtures, 10/ticket canary |

50 é insuficiente para detectar regressão em agentic pipeline com ~30 módulos. Chen 2026 estressa com 24h-runs; prompt 20 canary é muito mais curto. **Aplicação**: adicionar tier 2 de canary "long-horizon" (pelo menos 1 ticket de 20+ turns) antes de promote.

## Fontes wiki
- `[L0]` [[ai-scientist-autonomous-research]] — Lu 2024 failure modes; Chen 2026 File-as-Bus + ablações
- `[L0]` [[self-improving-agents]] — Reflexion, ERL (heurística > trajetória), TextGrad, Absolute Zero, SWE-TRACE Rubric PRM
- `[L1]` [[autoresearch-reliability-triad]] — Pilar 2 (anti-cascade) + Pilar 3 (stopping criterion)
- `[L1]` [[llm-as-judge]] — positivity bias em reviewer automated
- `[L1]` [[autonomous-kb-failure-modes]] — Layer 3 circularity

## Confiança
**Média-alta.** Mapping de failure modes → gaps do prompt 20 é direto (mesma estrutura: agente tentando maximizar sinal). Claims sobre canary longitudinal e cross-oracle family são projeção — precisariam ser testados.

## Gaps
- Voyager full text não em raw/ (referenciado apenas)
- Sem paper sobre **agentic dependency closure** — análise estática de impacto de self-mod
- SWE-TRACE (Han 2026) tem rubric PRM mas não self-mod protocol

## Mudanças no roadmap
- **Prompt 20**: (a) self_mod_map.yaml com `dependency_closure` computado, não lista manual; (b) regra "agente não toca thresholds de gates" explícita; (c) fixture provenance audit — fixtures sugeridas por self-mod não contam para canary; (d) oracle cross-family (Anthropic + OpenAI + open-weight) em yellow zone; (e) canary longitudinal rolling-N; (f) `agent_prompts/*.md` sempre yellow-zone mínimo.
- **Prompt 16**: compositionality test para skills promovidas (inspiração Voyager).
- **Prompt 21 ↔ 20**: pipeline de promoção cross (fixture descoberta no chaos vira fixture do canary 20).
- **Prompt novo (30)**: heuristic unlearning — quando lesson/antipattern é invalidada, mecanismo de retração.
- **Prompt novo (31)**: cross-config invalidation — quando config (embedding, model version) muda, canários recentes precisam re-run.

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Guardrails adicionais de self-mod (dependency closure, provenance, canary longitudinal) reduzem regressões silenciosas de evolução.

**Experiment**
- Simular 20 ciclos de self-mod em ambiente controlado com duas variantes:
  1. protocolo atual,
  2. protocolo reforçado (gaps Q3 aplicados).
- Medir: `regressions_after_promote`, `rollback_rate`, `time_to_detect_regression`, `false_block_rate`.

**Success Metric**
- Queda >= 40% em `regressions_after_promote`.
- `time_to_detect_regression` <= 1 ciclo de canary.
- `false_block_rate` <= 10%.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| Failure modes do AI Scientist (recursão/timeout/bias) | Measured (external literature) | Evidência fora do pipeline. |
| "canary longitudinal melhora segurança acumulada" | Projected | Requer experimento multi-ciclo local. |
| "oracle cross-family reduz positivity bias" | Projected | Precisa comparar acordo inter-famílias em eval. |
