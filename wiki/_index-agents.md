# Index — Agents

<!-- ~28 artigos: agent memory, self-improvement, LLM-as-judge, harnesses, multi-agent, transformer internals -->
<!-- RWKG (quarentena) = gap estrutural do cluster: hub de adaptação de topologia bloqueado -->

- [Multi-Agent Orchestration](concepts/multi-agent-orchestration.md) — Coordinator mode, single vs multi-agent, 4-phase workflow, isolation modes
- [Autonomous Research Agents](concepts/autonomous-research-agents.md) — 4-stage pipeline (plan→question→explore→report), benchmarks, 5 open challenges
- [Agent Memory Architectures](concepts/agent-memory-architectures.md) — STORAGE STRUCTURES: MemGPT tiers, Synapse graph, Letta compression, CoALA cognitive taxonomy, EM-LLM surprise segmentation
- [Self-Improving Agents](concepts/self-improving-agents.md) — Reflexion (verbal) + ERL (heuristics) + RMM (RL) + TextGrad + Absolute Zero. L2: verbal +8pp, ancoragem +39pp
- [LLM-as-Judge](concepts/llm-as-judge.md) — 12 biases (self-enhancement most critical), GPT-4o near random on hard evals, dynamic criteria > static rubrics
- [Position Bias in LLM-as-a-Judge](concepts/position-bias-llm-judge.md) — L2 causal evidence via position-swapping (do-operator): PC=0.57–0.82; worst in close-quality comparisons
- [Reflexion-Weighted Knowledge Graphs](concepts/reflexion-weighted-knowledge-graphs.md) — ⏳QUARANTINED. Adaptive retrieval topology where graph restructures based on failure feedback
- [Immune-Inspired Credit Assignment](concepts/immune-inspired-credit-assignment.md) — PARADIGM ALTERNATIVE: amplify successes, let failures die (CLONALG). Never applied to KGs (confirmed gap)
- [AI Scientist — Autonomous Research](concepts/ai-scientist-autonomous-research.md) — Lu 2024 + Chen 2026 (AiScientist): loop end-to-end + File-as-Bus. PaperBench 33.73, MLE-Bench 81.82% Any Medal%
- [File-as-Bus Workspace](concepts/file-as-bus-workspace.md) — Protocolo: artefatos em disco como substrato de coordenação multi-agente. Thin control over thick state. Ablação: −31.82% sem File-as-Bus
- [Multiagent Debate — Du et al. 2023](concepts/multiagent-debate-du-2023.md) — Múltiplas instâncias LLM debatem em rounds: melhora factualidade. Middle ground entre single-evaluator bias e human oversight
- [Self-Preference Bias in LLM-as-a-Judge](concepts/self-preference-bias-llm-judge.md) — LLMs preferem outputs com menor perplexidade. GPT-4 bias=0.520. Explica Layer 3 Circularity via familiaridade distribucional
- [Natural-Language Agent Harness](concepts/natural-language-agent-harness.md) — Pan (2026): NLAH externaliza harness como artefato NL executável; IHR runtime. Mais estrutura ≠ melhor performance
- [DeerFlow — Async Agent Concurrency](concepts/deer-flow-concurrency.md) — ⏳QUARANTINED. ByteDance: AsyncStreamBridge, RunManager atômico, rate limiting. 3 claims com erros de API asyncio
- [Meta-Harness: Otimização Automática](concepts/meta-harness-optimization.md) — Lee/Stanford (2026): outer-loop coding agent busca harnesses via histórico. +7.7 pts vs. ACE, 4x menos tokens
- [Prometheus como Substrato de NLAHs](concepts/prometheus-as-nlah-substrate.md) — ⚠️ EMERGIDO. .claude/commands/ = coleção de NLAHs; outputs/logs/ = filesystem de histórico. Prometheus a um outer-loop
- [Pressure-Field Coordination](concepts/pressure-field-coordination.md) — ⏳QUARANTINED. Rodriguez (2026): implicit coordination via quality-signal gradients + temporal decay. 3 claims invalidados
- [Emergent Coordination Measurement](concepts/emergent-coordination-measurement.md) — ⏳QUARANTINED. Riedl (2025): PID+time-delay detecta transição de agregados para coletivos. Persona suficiente sem comunicação direta
- [Self-Organizing LLM Agents (Endogeneity Paradox)](concepts/self-organizing-agents-stigmergy.md) — ⏳QUARANTINED. Dochkina 2026: 25k tarefas, Sequential hybrid +14% vs centralizado, +44% vs autônomo
- [Epistemic Necessity para Uso de Ferramentas](concepts/epistemic-necessity-tool-use.md) — ⏳QUARANTINED. Wang et al. 2026: Theory of Agent (ToA); overacting/overthinking como miscalibração
- [GenAI-Native System Design](concepts/genai-native-system-design.md) — Vandeputte (2025): 5 pilares (reliability→assurance) + 3 padrões (cells/substrates/routers); Bucaioni: 14 contrib AI, 6 AICH não resolvidos
- [Codified Context para Agentes em Codebase](concepts/codified-context-codebase-agents.md) — Vasilopoulos (2026): constituição (hot) + 34 docs (cold) + 19 agentes; 108K LOC, 283 sessões; instância concreta de hot/cold memory
- [Agent Context Files — Evidência Empírica](concepts/agent-context-files-evidence.md) — ⏳QUARANTINED · Lulla -28.6% runtime; Gloaguen -task success, +20% cost; Chatlatanagulchai 2.303 files, security em 14.5%
- [Agentic Codebase Enforcement Patterns](concepts/agentic-codebase-enforcement-patterns.md) — ⏳QUARANTINED · EMERGIDO. Tabela hook/CLAUDE.md/linter por tipo de constraint; mapeamento Codified Context → Claude Code stack
- [Looped Transformer (Recurrent-Depth)](concepts/looped-transformer.md) — Kohli 2026 + Wang 2024 + Lu 2025 + Gao 2025: bloco L×R; Huginn GSM8K 4.93% vs CoT 24.87%; URM ARC-AGI 53.8%/16.0% SOTA via ConvSwiGLU + TBPTL
- [Huginn-3.5B (Geiping 2025) — Foundational RDT em escala](concepts/huginn-3.5b-recurrent-depth.md) — prelude/recurrent/coda; 3.5B params, 800B tokens, AMD Frontier; r̄=32 → effective depth 132; truncated backprop k=8; primeiro pretrain RDT em escala
- [Retrofitting Recurrence (McLeish 2025)](concepts/mcleish-2025-retrofitted-recurrence.md) — converte TinyLlama/OLMo/Llama-3.2-1B em RDT via continued pretraining; pretrained-init ~950B tokens à frente de random; curriculum de recurrence; viabiliza adoção sem pretrain from-scratch
- [Parcae — LTI-stable Looped Transformers (Prairie 2026)](concepts/parcae-lti-stable-looped.md) — reframe de loop como sistema dinâmico LTI; ρ(Ā)<1 via diagonal negativa; 770M Parcae ≈ 1.3B Transformer Core; -6.3% PPL vs Huginn; primeira lei de escala test-time looping
- [Coconut — Chain of Continuous Thought](concepts/coconut-continuous-latent-reasoning.md) — Hao 2024 Meta FAIR: hidden state como input embedding (não token); BFS emergent sobre paths; ProsQA ~95% vs CoT ~82%
- [Stacked Bottleneck Avoidance](concepts/stacked-bottleneck-avoidance.md) — ⏳QUARANTINED · EMERGIDO. Princípio: intra-agent prioriza expressividade (Coconut), inter-agent prioriza auditabilidade (File-as-Bus). Pareto-ótimo conjecturado, H1 falsificável.
- [Grokking of Implicit Reasoning](concepts/grokking-implicit-reasoning.md) — Wang 2024 + Kohli 2026 + Lin 2025: 3 estágios grokking; fixed-pattern 99% OOD mas shuffled 23% (Variable as Subtrahend Plight — shortcut learning)
- [Depth Extrapolation + Overthinking](concepts/depth-extrapolation-recurrent.md) — Kohli 2026 §6: R_train>4 habilita scaling inference-time; overthinking degrada >15 iter; halting KL+entropia
- [Agentic Coding Failure Taxonomy](concepts/agentic-coding-failure-taxonomy.md) — Liu 2025: 3 fases, 25 subcategorias; cognitive deadlock = falha dominante agentic; Expert-Executor +22.2% intratáveis
- [AgentOps — MAS Failure Management](concepts/agentops-mas-failure-management.md) — EAGER: falhas em MAS fixos são concentradas (top-2 cobrem 75-95%); BGE-M3 falha em traces (NDCG@10=14.5%); step-wise detection F1 63-86%
- [Uncertainty-Aware Workflow Denoising](concepts/uncertainty-aware-workflow-denoising.md) — DenoiseFlow KDD2026: Noisy MDP; Sensing→Regulating→Correcting; 83.3% avg 6 benchmarks; 40-56% cost reduction via adaptive branching
- [[ticket-pre-validation-agentic-planning]] — AMBIG-SWE + Ask or Assume: +74% em SWE-bench com detecção de underspecification pré-execução; gargalo é detectar, não perguntar (ICLR 2026)
- [[pr-creation-orchestration]] — Agyn 72.2% SWE-bench 500: PR aprovado por reviewer agent como acceptance signal; 4 roles; automation-first prompting; produção-deployed
