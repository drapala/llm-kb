# Q2 — Rational inattention aplicada a context compaction

**Query**: hierarquia de descarte que preserva performance agêntica; contexto prompt 15 do roadmap.

## Resposta

### Framework transferível

Sims (2003): agente com constraint `I(X;Y) ≤ C` minimiza `E[(Y-X)²]`. Traduzido ao pipeline:
- **X** = conteúdo disponível (ticket + workspace + test output + file reads + message history)
- **Y** = próxima ação do inner_agent
- **C** = context window budget em tokens (200k Claude, mas budget efetivo é menor — prompt caching tier 1 breakpoint)
- **Distortion** = degradação da ação (stage fail, hallucination de API inexistente, AC perdido)

A solução ótima **não é** truncar uniformemente. É alocar capacidade onde o sinal tem maior informação para a ação. [[binding-attention-regime]] formaliza: o regime de binding é precisamente onde compaction vira decisão crítica (`retrievals_gap` sobe quando informação relevante foi descartada).

### Hierarquia de descarte derivada (alto I(X;Y) → baixo)

Ordem de **preservação** (descarte inverso):

1. **AC do ticket + exit_condition do stage corrente** — `I = alto` (determina verdict). Nunca compacta.
2. **Diff acumulado + arquivos em `allowed_files` já tocados** — alto I, estado mutável do mundo. Nunca compacta.
3. **Últimas N tool calls do turno corrente** (janela rolling ~5-10 turns) — alto I para próximo passo.
4. **Test output: apenas failures + traceback** — `I(test_output; action) ≈ I(failures; action)` porque passing tests não mudam próxima ação. Prompt 15 já faz.
5. **Workspace.md cross-stage notes** — I decai com idade; keep head+tail, compact middle.
6. **Antipatterns e lessons (retrieval)** — injetar via RAG **apenas** os top-k pelo ticket, nunca dump completo. I por item é alto mas budget é fixo.
7. **Recovery refs de attempts anteriores do MESMO stage** — alto I se `attempt > 1`, senão descartável.
8. **File reads fora do diff atual** — manter apenas skeleton (symbols) + trechos tocados; body integral descarta após uso.
9. **Histórico de turns antigos do stage ANTERIOR** — compactar para 1 parágrafo summary + verdict.
10. **Recovery refs de OUTROS stages** — descartáveis após completed_stages marker.
11. **Console logs do tooling (uv install, pre-commit chatter)** — ruído puro se exit=0. Descartar.
12. **Explicações do critic/reviewer em rounds anteriores APROVADOS** — I → 0 após aprovação. Descartar.

### A assimetria que rational inattention ensina

Sims (§III): `Var(Y|X) = Var(X)/e^{2C}`. Consequência operacional: **quando varianza do estado do mundo cresce (bug complexo, codebase novo), precisa mais C para manter mesma precisão**. Pipeline hoje usa budget **estático** (prompt 15 propõe ContextBudget fixo).

Correção: budget adaptativo por sinal de incerteza.
- Stage com `attempt > 1` após fail → aumenta budget (sinal de alta variância).
- Oracle disagreement detectado → aumenta budget (variância entre juízes).
- Antipattern match de complexidade alta (arquitetural) → aumenta budget.

**Isto muda o prompt 15**: ContextBudget deve ter `adaptive_scaling: {signal → budget_delta}`, não só `soft/hard` thresholds.

### Anti-padrão: compactação sobre o retrieval errado

[[llm-as-judge]] documenta **position bias** e **authority bias** no LLM judge. Aplicado a compaction: se o compactor é um LLM decidindo o que descartar, ele herda esses vieses.

- Position bias → compactor preserva o começo e fim, descarta o miolo indistintamente mesmo quando o miolo tinha AC-crítico.
- Authority bias → preserva conteúdo com citations/links mesmo quando irrelevante.

Implicação: compactor não deve ser LLM puro. Deve ser **LLM com regras duras de preservação** (AC, diff, exit_condition são não-negociáveis) + LLM só decide ordem de descarte entre itens já classificados como "compactable".

### Conexão com fast-frugal heuristics (caso-limite)

Matějka & McKay (2011): solução ótima para choice discreta com rational inattention = multinomial logit. Take-the-Best é caso-limite quando há **dominância clara** entre opções. Aplicado:

- Quando um signal domina (stage exit_condition é inequívoco, test output é binário pass/fail), use heurística frugal: **ignore tudo que não é esse signal**. Isso está sub-aproveitado no pipeline atual.
- Quando sinais são próximos (multiple failing tests, ambíguo qual AC falhou), NÃO use heurística — mantenha espectro de evidência.

**Implicação direta**: detector de "binding regime" no compactor. Se o signal do stage é unambíguo → compactação agressiva (30-40% do budget livre). Se ambíguo → compactação conservadora (5-10% livre).

### Rate-distortion para cache tier

Prompt 15 menciona "Prompt caching com Tier 1 breakpoint". Rate-distortion insight: o **breakpoint ótimo** não é "onde houver estabilidade sintática" (o que cachers usam); é **onde `I(X_cached; Y_next) / token_cached` for máximo**. 

Tokens com alta reutilização (security preamble, rubric do critic, AC do ticket) têm `I/cost` alto → Tier 1. Tokens raros-mas-volumosos (big file reads) têm `I/cost` baixo após primeira leitura → nunca Tier 1.

Isto muda o prompt 15: breakpoint não é arbitrário — é computável. Adicionar `cache_priority_score = I_estimate / tokens` e usar top-k para breakpoint.

### Gap teórico (precisa ingestão)

Matějka & McKay (2015) — *"Rational Inattention to Discrete Choices: A New Foundation for the Multinomial Logit Model"* — formaliza o caso discreto, que é o que o pipeline de fato tem (decisões de compactação são binárias: descarta ou mantém). [[binding-attention-regime]] já sinaliza esse gap.

## Fontes wiki
- `[L0]` [[binding-attention-regime]] — emergence de Sims×Gigerenzer, regime identification, aplicação KB 3-camadas
- `[L0]` [[rational-inattention]] — formalismo Sims 2003, I(X;Y)≤C, solução Gaussiana
- `[L1]` [[rational-inattention-discrete]] — Matějka-McKay 2015 (se existir; in_degree baixo)
- `[L1]` [[llm-as-judge]] — position bias + authority bias como armadilha no compactor

## Confiança
**Média.** Transferência Sims → LLM context é interpretação (⚠️ já marcada em binding-attention-regime). Mecanismo é sólido; calibração de `C_LLM` é especulativa — precisa benchmark empírico (CONTEXT-BOMB do prompt 15 é veículo ideal).

## Gaps
- Matějka & McKay (2015) não ingerido como raw/ (wiki tem referência mas não full text)
- Nenhum paper indexado sobre prompt caching como rate-distortion problem
- Falta corpus sobre **measurement de C_LLM** empírico (quanto de sinal um modelo realmente processa vs. tokens fornecidos)

## Mudanças no roadmap
- **Prompt 15**: (a) hierarquia de preservação explícita com 12 níveis, (b) adaptive budget em função de sinais de incerteza (`attempt > 1`, oracle disagreement), (c) `cache_priority_score` derivado ao invés de breakpoint arbitrário, (d) compactor não-LLM-puro (regras duras de preservação sobre AC/diff/exit_condition).
- **Fixture adversarial nova**: `ATTENTION-MISALLOC` — stage onde o sinal de interesse está no meio do contexto, testa se compactor preserva por posição (ruim) ou por I(X;Y) (bom).
- **Prompt novo proposto (29)**: C_LLM measurement — benchmark empírico de quanto sinal cada modelo *efetivamente* usa, para calibrar budget adaptativo.

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Compaction com preservação hierárquica + budget adaptativo reduz falhas por perda de contexto sem aumentar custo total.

**Experiment**
- Comparar `compaction_static` vs `compaction_adaptive` em suíte com tickets longos + `ATTENTION-MISALLOC`.
- Coletar: `approve_rate`, `context_overflow_events`, `replan_due_to_context_loss`, `tokens_total`.

**Success Metric**
- Redução >= 30% em `replan_due_to_context_loss`.
- `approve_rate` +2pp ou melhor.
- `tokens_total` não aumenta >10% frente ao baseline estático.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| Formulação RI (`I(X;Y) <= C`) | Measured (theory) | Resultado teórico consolidado. |
| "12 níveis é hierarquia ótima para pipeline" | Projected | Exige benchmark empírico local. |
| "budget adaptativo melhora robustez" | Projected | Validar em suíte adversarial dedicada. |
