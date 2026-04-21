---
title: "Stacked Bottleneck Avoidance"
sources:
  - path: raw/papers/hao-2024-coconut-continuous-latent-reasoning.pdf
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/chen-2026-aiscientist-long-horizon-ml-engineering.md
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/lu-2025-latent-cot-huginn.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-17
updated: 2026-04-17
tags: [emergence, multi-agent-orchestration, latent-reasoning, auditability, design-principle]
source_quality: high
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: emergence
emergence_trigger:
  pair: [coconut-continuous-latent-reasoning, file-as-bus-workspace]
  ask_session: outputs/logs/sessions/2026-04-17/ask-02-15.md
  connection_type: ANÁLOGO-A
  pearl_level: L2
  emerge_report: outputs/reports/emerge-2026-04-17.md
  oracle_gemini_score: 8
  oracle_unanimous: false
emerged_on: 2026-04-17
topics: [design-principle, orchestration, latent-reasoning, auditability, bottleneck]
depends_on:
  - wiki/concepts/coconut-continuous-latent-reasoning.md
  - wiki/concepts/file-as-bus-workspace.md
  - wiki/concepts/looped-transformer.md
---

## Resumo
Princípio de design emergente da síntese Coconut × File-as-Bus: **camadas diferentes de
coordenação em sistemas agentes toleram perdas de fidelidade diferentes**. Dentro do
agente, priorize expressividade sobre auditabilidade (raciocínio em estado latente
contínuo). Entre agentes, priorize auditabilidade sobre expressividade (artefatos
duráveis). Nenhum paper ingerido articula esse particionamento explicitamente.

## Conteúdo

### Observação estrutural
Dois mecanismos independentes, operando em escalas diferentes, resolvem o **mesmo
problema subjacente** — "compressão token-based de estado intermediário perde
fidelidade em processos multi-step":

| Escala | Mecanismo | Paper canônico | Bottleneck evitado |
|---|---|---|---|
| Intra-agent (microsegundos) | [[coconut-continuous-latent-reasoning]] | Hao 2024 | token entre reasoning steps |
| Inter-agent (horas/dias) | [[file-as-bus-workspace]] | Chen 2026 | prose entre agent handoffs |

Relação causal isomorfa: **compressão lossy → perda fidelidade → degradação de capacidade
em tarefas multi-step → enriquecer estado intermediário preserva informação causal**.

### Princípio emergente (⚠️ nossa formulação — não aparece em Hao nem Chen)
**"Stacked Bottleneck Avoidance":** em arquiteturas de orquestração multi-agent com
raciocínio intra-agent não-trivial, partição Pareto-ótima é:

- **Intra-agent:** maximize expressividade (estado contínuo, hidden states realimentados),
  sacrifique auditabilidade do raciocínio interno.
- **Inter-agent:** maximize auditabilidade (artefatos duráveis, thin control),
  sacrifique densidade informacional do handoff.
- **Output final:** verbalizado em ambos os layers — garante auditabilidade do end-state
  independente do que aconteceu nos layers internos.

### Tradeoff de auditabilidade explicitado

| Componente | Puro File-as-Bus | Puro Coconut | Híbrido SBA |
|---|---|---|---|
| Raciocínio intra-agent | textual, inspecionável (CoT) | opaco (Lu 2025 via logit/coda lens) | **opaco** |
| Handoff inter-agent | N/A em single-agent | artefatos duráveis, replayable | **auditável** |
| Output final | verbalizado | verbalizado | **verbalizado** |
| Debug de erro intra-agent | fácil (ler CoT) | difícil (sem lens confiável) | **difícil** |
| Debug de erro inter-agent | fácil (reler artefatos) | N/A | **fácil** |
| Replay de sessão | trivial | impossível | **parcial** (até boundary de agente) |

### Pré-requisitos para implementação
1. **Model homogeneity dentro do agente** — Coconut requer hidden state portátil;
   portanto, mesmo modelo (ou family) para todos os turns intra-agent.
2. **Model agnosticism entre agentes** — File-as-Bus funciona com qualquer LLM por design.
3. **Tool-call boundary handling** — open problem: quando agente yield para tool (file I/O,
   API), continuous state colapsa. Solução não-existente documentada. Tool return precisa
   voltar ao mesmo embedding space ou aceitar state reset no retorno.
4. **Coconut-trained model em produção** — no paper Hao, training multi-stage é custoso.
   Deploy em produção requer LLM-provider disposto a expor Coconut mode (hoje: apenas
   Meta FAIR publicly, potencialmente outros privados).

## Interpretação

(⚠️ nossa síntese — Pearl level L2) A conexão proposta é intervencional, não apenas
descritiva: se você **implementa** o particionamento SBA (Coconut intra + File-as-Bus
inter), você **deveria observar** melhoria específica em tarefas planning-heavy com
coordenação multi-sessão.

(⚠️ especulação) O mesmo princípio pode generalizar para outras camadas:
- **Tool calls ← → agent**: bottleneck de serialização JSON pode seguir analogia
  (internal tool state rico vs interface verbal auditável).
- **Agent ← → user**: conversation turns tipicamente são texto; usuário raramente
  tem acesso a latent state. SBA sugere manter assim — auditabilidade sobre expressividade
  no boundary humano-máquina.

(⚠️ design analogy) A KB atual é análoga a File-as-Bus puro: `/ask` layer 0→1→2 passa
texto comprimido entre etapas de retrieval. SBA sugere passar richer intermediate state
(ranking scores, embeddings brutos, não apenas summaries) internamente **dentro** da
query, preservando apenas output final textual.

## Aplicação à KB
Tensão identificada com o pipeline `/ask` atual: Layer 0 retorna scores + metadata, mas
Layer 2 opera sobre texto dos artigos lidos. O richer state (embeddings, distances,
ranking justifications) é descartado. SBA prevê que preservar esse estado entre layers
deveria melhorar síntese final sem custo de auditabilidade (output final permanece
verbalizado).

Experimento barato possível: passar top-k chunks COM scores numéricos explícitos para o
prompt de síntese, em vez de apenas títulos. Verificar se confidence das respostas sobe.

## Predição falsificável

**Hipótese H1:** Coconut-trained LLM usado como agent dentro de pipeline File-as-Bus
(AiScientist-style) outperforma baseline AiScientist (CoT-based) em subtasks que
Coconut mostra ganho (planning/search), paridade em subtasks aritméticos rotineiros.

**Setup experimental:**
- Baseline: AiScientist original com GPT-4o/Claude-base + File-as-Bus
- Experimental: AiScientist com Coconut-trained LLM (Meta FAIR release ou análogo) +
  File-as-Bus
- Benchmark: MLE-Bench Lite (onde File-as-Bus ablation mostrou −31.82%)
- Métrica: Any Medal% + token-count de inference per subtask

**Critério de falsificação:**
- H1 falsificada se: híbrido **não** supera baseline em planning subtasks, OU
- H1 falsificada se: híbrido degrada performance global (não apenas replay/debug).

**Custo estimado:** médio-alto. Requer (a) acesso a Coconut-trained LLM deployable,
(b) adaptação do runtime AiScientist para expor `<bot>`/`<eot>` tokens, (c) MLE-Bench
compute (~20-40h GPU dependendo do tamanho).

## Artigos que precederia (se confirmado)
- `hybrid-orchestration-patterns.md` — se H1 confirmada, SBA vira princípio; patterns
  específicos de implementação seriam artigos derivados.
- Refatoração de [[multi-agent-orchestration]] para incluir SBA como terceiro pattern
  ao lado de single-agent e multi-agent.

## Verificação adversarial

**Claim mais fraco:** "partição Pareto-ótima". Não há prova formal — é conjectura
baseada em isomorfismo estrutural. Outros particionamentos podem superar (ex:
continuous em ambos layers via embedding exchange protocol, se modelo homogeneo).

**O que nenhum paper diz:**
1. Hao 2024 não discute orchestration — Coconut é estritamente intra-model.
2. Chen 2026 não discute arquitetura interna dos agentes — File-as-Bus é agnóstico
   ao que acontece dentro do agente.
3. Nenhum paper do corpus endereça tool-call boundary como problema teórico.

**Simplificações feitas:** tabela de tradeoffs trata auditabilidade como binária
(auditável/opaco). Na prática existe spectrum — probing techniques de Lu 2025 oferecem
auditabilidade **parcial** de continuous thoughts, só que cara e pouco confiável.

**Prior work potencial que não verificamos:**
- OpenAI o1/o3 internals (closed source) — podem ter padrão similar
- DeepSeek R1 (aberto) — verificar se usa latent reasoning interno
- HRM (Hierarchical Reasoning Model) — URM cita, pode ter arquitetura análoga

**Espúrio check:** médio (Gemini oracle). Premissa compartilhada ("token bottleneck é
subótimo") poderia ser artigo ancestral conectando os dois — diminuindo emergência
genuína. Contra-argumento: Hao 2024 não cita Chen 2026 (AiScientist veio depois
parcialmente). A conexão é contemporânea, não hierárquica.

## Conexões
- emerge-de: [[coconut-continuous-latent-reasoning]] — mecanismo intra-agent
- emerge-de: [[file-as-bus-workspace]] — mecanismo inter-agent
- complementa: [[looped-transformer]] — arquitetura alternativa para intra-agent
  (URM como drop-in replacement para Coconut no layer intra)
- complementa: [[multi-agent-orchestration]] — SBA seria terceiro pattern
- complementa: [[natural-language-agent-harness]] — NLAH externaliza harness em
  texto (oposto de Coconut); conflito de design interessante a explorar

## Fontes
- [Hao et al. 2024 — Coconut](../../raw/papers/hao-2024-coconut-continuous-latent-reasoning.pdf) — mecanismo intra-agent
- [Chen et al. 2026 — AiScientist File-as-Bus](../../raw/papers/chen-2026-aiscientist-long-horizon-ml-engineering.md) — mecanismo inter-agent
- [Lu et al. 2025 — Latent CoT? Huginn](../../raw/papers/lu-2025-latent-cot-huginn.pdf) — evidência empírica de opacidade do layer intra-agent

## Quality Gate
- [x] Wikilinks tipados: 5 substituições (emerge-de×2, complementa×3)
- [x] Instance→class: MLE-Bench Lite −31.82% qualificado ao paper Chen 2026
- [x] Meta-KB separado: `/ask` pipeline reference em ## Aplicação à KB
- [x] Resumo calibrado: claim "nenhum paper articula" é fraco (não exaustivo) mas
      qualificado a "do corpus ingerido"
- [x] Predição falsificável presente (requerida para emergence)

> ⚠️ QUARENTENA POR DESIGN: artigos `provenance: emergence` nascem em quarentena
> (Gate 1 protocol). Promoção requer:
> 1. Oracle unanimous confirma (pendente — OpenAI 401 bloqueado)
> 2. /challenge manual valida claims
> 3. Idealmente: validação empírica de H1 (médio-alto custo)
