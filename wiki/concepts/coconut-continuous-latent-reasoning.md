---
title: "Coconut — Chain of Continuous Thought"
sources:
  - path: raw/papers/hao-2024-coconut-continuous-latent-reasoning.pdf
    type: paper
    quality: primary
    stance: challenging
    challenging_type: implication
created: 2026-04-17
updated: 2026-04-17
tags: [latent-reasoning, continuous-thought, BFS, planning, COLM-2025]
source_quality: high
interpretation_confidence: high
resolved_patches: []
quarantine: false
quarantine_promoted: 2026-04-17
quarantine_criteria_met:
  auto_promote: true
  gates_passed: [1, 2, 4]
  gate3_skipped: openai_401_blocked
  gate3_gemini_only: true
  gemini_claims_survived: 2
  gemini_claims_weakened: 1
  gemini_weakened_fixed_inplace: true
  challenge_verdict: PUBLICÁVEL
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: source
topics: [latent-reasoning, continuous-thought, BFS-search, token-bottleneck, planning]
depends_on:
  - raw/papers/hao-2024-coconut-continuous-latent-reasoning.pdf
---

## Resumo
Coconut (Hao et al. 2024, COLM 2025) realimenta o **last hidden state** da LLM
diretamente como input embedding do próximo token, em vez de decodar para palavra. Cria
"continuous thoughts" que codificam **múltiplas alternativas simultâneas** — exploração
BFS-like emergente. Outperforma CoT em tarefas de planejamento (ProsQA), gerando
significativamente menos tokens.

## Conteúdo

### Mecanismo
- LLM padrão: `H_t = Transformer(E_t)`, `M(x_{t+1}|x_≤t) = softmax(W·h_t)` — sempre
  decodifica hidden state para token, então re-embeda.
- Coconut: insere tokens especiais `<bot>` e `<eot>` para marcar **latent mode**.
  Entre eles, `E_t = [e(x_1),...,e(x_i), h_i, h_{i+1},..., h_{j-1}]` — hidden states
  são reusados como embeddings, **bypass do mapping language↔embedding**.
- Continuous thoughts são totalmente diferenciáveis → otimizáveis end-to-end via
  gradient descent.

### Treino multi-stage (curriculum, inspirado em iCoT/Deng 2024)
- **Stage 0**: treina com CoT língua completo (warmup).
- **Stage k**: substitui os primeiros k passos de raciocínio por k×c continuous thoughts
  (c=1 default). Reset do otimizador a cada switch de stage.
- **Stage N**: zero passos língua, N×c continuous thoughts.
- Loss: cross-entropy nos tokens restantes (questão + thoughts são masked).
- Crítico: objetivo **NÃO comprime** o language thought — facilita predição do
  raciocínio futuro, permitindo representações mais efetivas que linguagem natural.

### Inferência
- Insere `<bot>` após question. Duas estratégias:
  a) Binary classifier para decidir terminate latent
  b) Pad para length constante
- Empirico: (b) funciona comparavelmente, é a default usada.

### BFS emergente (ProsQA, §4)
ProsQA = directed acyclic graph de relações lógicas; tarefa = encontrar caminho válido.
Requer planning não-trivial.

- CoT tradicional: commit early para um path. Falha em backtracking. Halucina edges
  inexistentes.
- Coconut k=6: encoda múltiplas alternativas no continuous thought. Visualização via
  forçar verbalização parcial mostra distribuição sobre múltiplos next nodes (Fig 5).
- Resultado: redução substancial de "Hallucination" e "Wrong Target" categories vs CoT.

### Resultados empíricos
- **GSM8k math**: continuous thoughts beneficiam accuracy **comparavelmente** a CoT —
  Coconut não supera CoT significativamente em math word problems, mas opera com
  substancialmente menos tokens de inferência.
- **ProsQA logical planning** (é onde Coconut ganha): "outperforms language space CoT
  reasoning" com significativamente fewer tokens. k=6 atinge ~95% accuracy vs CoT
  ~82% (Fig 3). Gains concentram em tasks que requerem search/planning, não em
  cálculo aritmético direto.

## Interpretação

(⚠️ design analogy) Coconut e [[looped-transformer]] resolvem o mesmo problema (raciocínio
latente sem token bottleneck) por caminhos arquitetônicos **distintos**:
| Dimensão | Looped Transformer | Coconut |
|---|---|---|
| Mecanismo | Mesmo bloco aplicado R vezes | Hidden state realimentado como embedding |
| Compute scaling | R iterations | N continuous thoughts |
| Compartilhamento | Pesos compartilhados em layers | Pesos compartilhados por reuso de hidden state |
| Treino | from-scratch synthetic | Multi-stage curriculum a partir de pretrained |
| Search structure | Sequential refinement | Emergent BFS sobre alternativas |

(⚠️ nossa interpretação) Continuous thought como "superposition" — Hao §2 cita Zhu 2025
para a hipótese formal de que continuous CoT pode codificar múltiplos paths em
superposition states. Se verdade, Coconut tem **vantagem teórica de capacidade** sobre
discrete CoT em tarefas de search.

(⚠️ design analogy) Para a [[grokking-implicit-reasoning]] / shortcut learning de Lin
2025: Coconut treina via supervisão multi-stage que internaliza language reasoning steps.
Pode evitar o shortcut pattern matching (Variable as Subtrahend Plight) porque a
representação latente não é constrained pela ordem de premisas — testagem empírica
contra o setup de Lin permanece aberta.

## Aplicação à KB

`/ask` em Layer 0→1→2 é análogo a chain-of-discrete-thoughts entre artigos. Coconut
sugere padrão alternativo: **hidden state da resposta intermediária realimentado como
contexto direto**, sem verbalizar. Não temos tokens latentes na KB (operamos via
markdown e texto), mas o paralelo é: ranking de docs em Layer 1 poderia ser usado como
"continuous prior" em Layer 2 sem decodificar para summary intermediário.

## Verificação adversarial

**Claim mais fraco:** "Coconut outperforms CoT em planning tasks". Provado em ProsQA
(setup sintético DAG) + GSM8k (math). Generalização para tarefas reais de planning
(coding, multi-hop QA não-DAG) não demonstrada nesse paper.

**O que o paper NÃO diz:**
1. Não compara com Looped Transformer head-to-head — diferentes paradigmas, sem
   benchmark comum.
2. Não testa interpretabilidade — continuous thoughts são opacos por design (vs Lu 2025
   logit lens em Huginn). Não-auditabilidade é tradeoff, não bug.
3. Não mostra que **emergem** alternativas BFS sem treino explícito — só afirma que
   "advanced reasoning mechanism surpasses traditional CoT".

**Simplificações feitas:** Artigo trata curriculum como "k stages substituem k passos";
na prática c=1 é hyperparameter, valores diferentes não foram avaliados em depth no paper.

**Prior work citado:** Deng 2024 (iCoT — internalize CoT), Wei 2022 (CoT original),
Yang 2024 (latent reasoning recoverable from hidden states), Pfau 2024 (filler tokens
limitations), Goyal 2023 (`<pause>` tokens), Zhu 2025 (theoretical superposition framing).

## Conexões
- complementa: [[looped-transformer]] — paradigma alternativo de raciocínio latente
  (recurrent-depth vs continuous-thought feedback). Diferentes tradeoffs.
- complementa: [[grokking-implicit-reasoning]] — Coconut treina via curriculum, não
  via grokking espontâneo. Pode ser caminho para systematic generalization sem o
  shortcut learning de Lin 2025.
- depende-de: [[depth-extrapolation-recurrent]] — ambos abordam test-time compute
  scaling, com mecanismos distintos (iterations vs continuous thoughts).

## Fontes
- [Hao et al. 2024 — Coconut (COLM 2025)](../../raw/papers/hao-2024-coconut-continuous-latent-reasoning.pdf) — paper primário Meta FAIR + UCSD

## Quality Gate
- [x] Wikilinks tipados: 3 substituições (complementa, complementa, depende-de)
- [x] Instance→class: ProsQA k=6 ~95% vs CoT ~82% qualificado ao setup
- [x] Meta-KB separado: referência a `/ask` em ## Aplicação à KB
- [x] Resumo calibrado: claim "outperforms CoT" qualificado para "planning requiring search" + GSM8k
