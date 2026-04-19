# Q4 — Tree search (LATS/RAP/MCTS) em inner loops agênticos

**Query**: sob que condições dominam single-trajectory+critic? Métricas de decisão?

## Resposta

### Gap de corpus reconhecido

**Layer 0 sem hit relevante** (scores 0.01-0.015 em artigos não-relacionados). O wiki metaxon **não tem** artigo específico sobre LATS (Language Agent Tree Search, Zhou et al. 2023), RAP (Reasoning via Planning, Hao et al. 2023), ou MCTS aplicado a LLMs. O wiki mais próximo é [[self-improving-agents]] que cobre Reflexion (single-trajectory com replay), não árvore.

Resposta construída com conhecimento paramétrico + framework do KB. Marcar como **confiança média** e **registrar gap de ingestão**.

### Framework conceitual para decisão

Single-trajectory (Reflexion-style): uma run, critic pós-hoc, retry se falha. **Custo**: linear em turns. **Problema**: trajectórias ruins são abandonadas sem extrair sinal; commit cedo a um path.

Tree search (LATS/RAP/MCTS): múltiplos paths explorados em paralelo ou sequencial com backtracking; value function pontua nodes; best path selecionado. **Custo**: exponencial em branching factor, amortizado por poda.

### Onde tree search ganha (evidências reportadas na literatura)

Com base em LATS (Zhou 2023, HumanEval/HotPotQA) e RAP (Hao 2023):
- **Stage multi-passo com ação reversível**: navegar web, sequência de comandos shell; backtracking é barato.
- **Ação irreversível cara** (migration DB, commit, PR): tree search é **inviável** sem rollback determinístico do estado do mundo. *Exatamente o caso do inner_agent do pipeline*.
- **Espaço de ação pequeno e discreto**: ajuda value function.
- **Critic confiável como value function**: se o critic é ruidoso ([[llm-as-judge]] CALM bias), MCTS amplifica ruído (propaga erros ao longo dos backups).

### Aplicado ao claude-pipeline

O inner_agent opera em **filesystem real** (git worktree, mas ainda assim estado compartilhado com venv, DB se houver). Ações como `file_write`, `bash git commit` são quase-irreversíveis localmente:
- Rollback requer `git reset` + reinstalar deps se pyproject mudou
- Testes podem ter side effects em fixtures compartilhadas
- Custo por "explorar branch alternativo" é **alto** — prompt 07 worktree efêmero resolve para **isolamento inter-ticket**, não para **tree search intra-ticket**

**Condição necessária para tree search intra-ticket no pipeline**: checkpointing turn-level (prompt 18) + worktree per-branch. Prompt 18 + 07 juntos são pré-requisitos, não substitutos.

### Onde single-trajectory é ótimo aqui

1. **Stage com exit_condition binário claro** (test passa ou não): não há o que explorar; é pass/fail + reflection.
2. **Budget de tokens limitado** (prompt 15): árvore multiplica tokens ~branching_factor × depth. Tight budget = single trajectory.
3. **Critic é rubric LLM** (não PRM treinado): value function é ruidosa, MCTS acumula erros.

### Onde tree search poderia ganhar no pipeline (híbrido)

- **Planner stage, não inner_agent**: gerar 3 planos alternativos, rodar cheap heuristic (AC coverage, file conflicts estimate), escolher melhor. Custo: 3x planner calls, mas planner é muito mais barato que execução.
- **Investigator mode (prompt 08)**: 5-round hypothesis generation é natural tree (múltiplas hipóteses, cada uma com evidence gathering). **Já é semi-tree implícito**, falta formalizar com value function.
- **Debug/Reflexion em inner_agent ao fim**: quando stage falha attempt N, em vez de só retry com self-reflection, *gerar K diff alternativos da última ação*, aplicar cada em checkpoint, escolher melhor via critic. **Micro-MCTS localizado**.

### Métricas de decisão (quando ligar tree search)

Framework proposto (não existe no roadmap):

| Métrica | Single-trajectory | Tree search |
|---|---|---|
| Reversibilidade do estado | qualquer | alta (rollback cheap) |
| Value function signal/noise ratio | qualquer | > 3 (senão ruído domina) |
| Branching factor efetivo | 1-2 | 3-8 (acima: poda precisa ser boa) |
| Budget tokens | tight | folga ≥ 5x |
| AC claro binário | ✓ | — |
| AC ambíguo multi-dim | — | ✓ |

Concretamente: **pipeline deveria ligar tree search em `planner` e `investigator`, NUNCA em `inner_agent` sem checkpointing turn-level + worktree-per-branch.**

### Conexão com conceito de rational inattention

[[binding-attention-regime]]: tree search é o **caso-livre** (C folgado) — você pode explorar múltiplos paths porque capacidade sobra. Single-trajectory é o **caso-binding** (C apertado) — Take-the-Best, commit ao path mais promissor cedo. Roadmap atual opera implicitamente em binding regime; tree search exige afrouxar C primeiro.

### Risco de over-engineering

Devin/OpenHands experimentaram tree search extenso em SWE-Bench; resultados variáveis. O ganho mais reportado é não via MCTS puro, mas via **best-of-N sampling** (Reflexion com N tentativas paralelas, critic escolhe melhor). Best-of-N:
- Custo linear em N (não exponencial)
- Não precisa value function continua
- Não precisa rollback fino
- **Compatível com worktree efêmero (prompt 07) rodando N em paralelo**

**Aplicação direta no roadmap (lowest-hanging fruit)**: em vez de novo prompt "tree search", adicionar ao prompt 07: `parallel_attempts: N` com `selector: oracle_critic | test_pass_rate`. Isso é 80% do ganho com 20% do custo de engineering.

### Stages irreversíveis e o trade-off verdadeiro

A pergunta implícita é "vale investir em infra pesada de tree search?" A resposta metaxon-grounded: **só depois de 18 + 07 estáveis**, porque antes disso o custo de rollback corrompe o benefício. Mesmo depois, o ganho empírico em ambientes de produção é **contestado** na literatura agêntica recente — o consenso 2025-2026 tende a **test-time scaling via best-of-N + PRM** (ver [[self-improving-agents]] SWE-TRACE Han 2026: 71.2% SWE-bench com HG-TTS, não tree search).

## Fontes wiki
- `[L1]` [[self-improving-agents]] — Reflexion (single-trajectory + reflection), SWE-TRACE HG-TTS (test-time scaling sem tree full)
- `[L1]` [[llm-as-judge]] — critic noise como limite para value function
- `[L1]` [[binding-attention-regime]] — binding vs free regime
- `[L1]` [[ai-scientist-autonomous-research]] — AI Scientist usa timeout, não tree search

## Fontes raw
- Nenhuma verificada. Claims sobre LATS/RAP/MCTS vêm de conhecimento paramétrico.

## Confiança
**Média-baixa.** Argumento estrutural sólido (reversibilidade, critic noise), mas sem corpus primário no wiki. Ganho reportado de tree search em código (LATS HumanEval) não foi verificado aqui.

## Gaps
- **Ingestão necessária**: Zhou et al. 2023 *LATS*, Hao et al. 2023 *RAP*, Yao et al. 2023 *Tree of Thoughts*. Sem isto, esta resposta é paramétrica.
- Sem paper sobre **best-of-N vs MCTS** em SWE agents.
- Sem artigo sobre test-time scaling (HG-TTS mencionado só como claim em self-improving-agents).

## Mudanças no roadmap
- **Prompt 07** (worktree): adicionar `parallel_attempts: N` + `selector`. É **best-of-N sampling, não tree search**. Baixo risco, alto ganho.
- **Prompt 08** (investigator): formalizar 5-round hypothesis como tree com value function (usa critic como eval); já é implícito.
- **Novo prompt 32 (proposto)**: tree search intra-ticket no inner_agent. **Precondição dura**: prompts 07 + 18 completos e estáveis. Justificativa: sem rollback fino, não há como explorar.
- **NÃO adicionar tree search no inner_agent sem pré-req**. Risco de corromper estado > ganho marginal.
- **Prioridade baixa vs PRM (Q1)**: test-time scaling com PRM + best-of-N é Pareto-dominante vs tree search para o domínio do pipeline (ações irreversíveis, critic ruidoso).

## Sugestão de ingestão
Adicionar à fila de /ingest:
- Zhou et al. 2023 *Language Agent Tree Search* (LATS)
- Hao et al. 2023 *Reasoning via Planning* (RAP)
- Han et al. 2026 *SWE-TRACE* (verificar se HG-TTS é tree ou best-of-N)

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Best-of-N em worktree paralelo entrega a maior parte do ganho prático antes de tree search completo.

**Experiment**
- Rodar 3 modos no mesmo conjunto de tickets:
  1. `single_trajectory`,
  2. `best_of_n=3` (worktrees paralelos),
  3. `best_of_n=5`.
- Medir: `approve_rate`, `tokens_total`, `wall_clock`, `regression_rate`.

**Success Metric**
- `best_of_n=3` com ganho >= 5pp em `approve_rate` vs `single_trajectory`.
- Aumento de `tokens_total` <= 2.5x.
- Sem piora de `regression_rate`.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| "sem 07+18 tree intra-ticket é arriscado" | Projected (architecture constraint) | Derivado de reversibilidade do estado local. |
| "best-of-N é Pareto-dominante aqui" | Projected | Validar com benchmark real do pipeline. |
| Ganho de LATS/RAP em literatura | Measured (external literature, pending ingest) | Ainda não verificado no corpus local. |
