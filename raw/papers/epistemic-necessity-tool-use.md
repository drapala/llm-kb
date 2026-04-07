---
title: "Position: Agent Should Invoke External Tools ONLY When Epistemically Necessary"
arxiv: "2506.00886"
year: 2025
type: paper
quality: secondary
note: "Síntese paramétrica — conhecimento de pré-treino, não texto primário recuperado"
---

# Position: Agent Should Invoke External Tools ONLY When Epistemically Necessary

## Metadados

- **Autores**: Não especificado (paramétrico)
- **Ano**: 2025/2026
- **arXiv**: 2506.00886
- **Status**: Síntese paramétrica baseada em conhecimento de treinamento

## Sumário

Position paper que propõe epistemic necessity como critério normativo para decisão de uso de ferramentas externas por agentes LLM. Reframing fundamental: uso de ferramentas não deve ser otimização de performance, mas decisão de aprendizado sob incerteza. Agentes devem invocar ferramentas externas apenas quando genuinamente necessário do ponto de vista epistêmico — quando o conhecimento interno é insuficiente para resolver a query com confiança adequada.

## Key Claims

1. **Epistemic necessity como critério normativo**: A pergunta relevante não é "esta ferramenta melhora minha resposta?" mas "eu genuinamente preciso desta ferramenta para resolver isto?" A distinção é entre uso como amplificação de performance vs. uso como resolução de ignorância real.

2. **Reframes tool use de performance optimization para learning-critical decision under uncertainty**: Usar ferramentas indiscriminadamente mascara as fronteiras do conhecimento do agente, impede calibração epistêmica, e cria dependência desnecessária. O critério de necessity preserva a transparência sobre o que o agente sabe vs. o que ele busca.

3. **Uso necessário vs. uso oportunístico**: A distinção central é entre:
   - **Necessário**: o agente não pode resolver a query com conhecimento interno sem risco de erro significativo (dados em tempo real, informação específica não no corpus de treinamento, cálculos que excedem capacidade interna)
   - **Oportunístico**: o agente poderia resolver internamente, mas usa ferramentas como atalho ou validação redundante

4. **Implicações para design de agentes**: Agentes devem ter mecanismos de self-assessment epistêmico antes de decidir invocar ferramentas. O custo de invocação não é apenas latência/tokens — é também custo epistêmico de não exercitar raciocínio interno.

5. **Calibração como consequência do critério**: Aplicar epistemic necessity força o agente a manter melhor calibração sobre seus próprios limites de conhecimento — sabe onde precisa de ajuda externa vs. onde pode raciocinar de forma confiante.

## Conexões com literatura

- Relacionado a trabalhos sobre calibração em LLMs (saber o que não sabe)
- Conecta a literatura de metacognição e epistemic uncertainty
- Relevante para tool-use benchmarks (ToolBench, API-Bank, etc.)
- Dialogue com posição oposta: "use tools liberally for grounding" (e.g., ReAct, Toolformer)

---

## Full Text (extracted from PDF, 13 pages)

Position: Agent Should Invoke External Tools
ONLY When Epistemically Necessary

Hongru Wang 1 2 Cheng Qian 3 Manling Li 4 Jiahao Qiu 5 Boyang Xue 2
Mengdi Wang 5 Heng Ji 3 Amos Storkey 1 Kam-Fai Wong 2

arXiv:2506.00886v2 [cs.AI] 29 Jan 2026

Abstract

Question: Are Giuseppe Verdi and Ambroise Thomas both Opera composers ?
Answer: Yes
Giuseppe Verdi

As large language models evolve into toolaugmented agents, a central question remains unresolved: when is external tool use actually justified? Existing agent frameworks typically treat
tools as ordinary actions and optimize for task
success or reward, offering little principled distinction between epistemically necessary interaction and unnecessary delegation. This position
paper argues that agents should invoke external
tools only when epistemically necessary. Here,
epistemic necessity means that a task cannot be
completed reliably via the agent’s internal reasoning over its current context, without any external
interaction. We introduce the Theory of Agent
(ToA), a framework that treats agents as making
sequential decisions about whether remaining uncertainty should be resolved internally or delegated externally. From this perspective, common
agent failure modes (e.g., overthinking and overacting) arise from miscalibrated decisions under
uncertainty rather than deficiencies in reasoning
or tool execution alone. We further discuss implications for training, evaluation, and agent design, highlighting that unnecessary delegation not
only causes inefficiency but can impede the development of internal reasoning capability. Our
position provides a normative criterion for tool
use that complements existing decision-theoretic
models and is essential for building agents that
are not only correct, but increasingly intelligent.

Reasoning

Acting

Ambroise Thomas

Reasoning

Acting

Yes

Agent A
Epistemic behavior: Epistemic effort
allocated to external interaction despite
internal sufficiency.

Reasoning
Agent B

Learning consequence:
Internal reasoning capability is
bypassed → no consolidation.

To answer the question of whether Giuseppe Verdi and
Ambroise Thomas are both Opera composers, let‘s first
reason through the information: 1) Giuseppe ….; 2)
Ambroise …. Based on this reasoning, …

Epistemic behavior: Epistemic effort
resolved internally when sufficient.

Yes

Learning consequence: Internal
reasoning is exercised → capability
preserved and strengthened.

Figure 1. Tool-use decisions shape the trajectory of agent intelligence. Two agents may achieve comparable task success through
different allocations of epistemic effort. An over-delegating agent
frequently invokes external tools even when internal reasoning suffices, resulting in stagnant internal capability despite correctness.
In contrast, an epistemically calibrated agent invokes external tools
only when necessary, allowing internal reasoning capability to
expand over time as experience accumulates. This figure illustrates
our central position: external tools should be invoked only when
epistemically necessary, since unnecessary delegation reshapes not
just efficiency, but the trajectory of agent intelligence itself. The
example is drawn from Wang et al. (2025a).

1. Introduction
Large Language Models (LLMs) have rapidly evolved beyond text generation into autonomous agents capable of
independently planning and executing complex tasks with
minimal human oversight (Kolt, 2025). These emerging
capabilities have enabled a broad range of real-world applications, including travel planning (Xie et al., 2024a),
human-computer interaction (Xie et al., 2024b; Wang et al.,
2024b; Qin et al., 2025), and scientific research (Wu et al.,
2025; Nguyen et al., 2024; Edwards et al., 2024; 2025). As a
result, a central question in agent design has emerged: when
should an agent rely on its internal reasoning (e.g, continue
existing reasoning processing), and when should it interact
with the external world?

1

University of Edinburgh 2 The Chinese University of Hong
Kong 3 University of Illinois Urbana-Champaign 4 Northwestern
University 5 Princeton University. Correspondence to: Hongru Wang <hongru.carrywang@gmail.com>, Cheng Qian
<chengq9@illinois.edu>.

This paper takes a clear position: an agent should invoke
external tools only when epistemically necessary. That is,

Preprint. January 30, 2026.

1

Submission and Formatting Instructions for ICML 2026

external interaction is justified if and only if the remaining
uncertainty required to complete a task cannot be resolved
through internal reasoning alone. Despite the prevalence
of tool-augmented agents, existing paradigms lack a principled criterion for this decision. Agents are often trained to
maximize task success, minimize cost, or follow predefined
workflows. These approaches permit agents to overuse tools
as long as answers are correct, treating tool use as a free
shortcut rather than an epistemic commitment. As a consequence, agents exhibit common failure modes—such as
overthinking (Cuadron et al., 2025) and overacting (Wang
et al., 2025a)—that are poorly explained as isolated reasoning or execution errors.

when task performance remains high. Section 5 contrasts
this epistemic view with prevailing agent paradigms that optimize for correctness, reward, or workflow execution. We
conclude by arguing that tool-use decisions are not merely
an efficiency concern, but a defining factor in the long-term
trajectory of agent intelligence.

2. Foundations
2.1. Reasoning and Acting as Alternative Means of
Knowledge Acquisition
Intelligent agent behavior is commonly described in terms
of two capabilities: reasoning and acting (Yao et al., 2023;
Wang et al., 2024c). Reasoning allows an agent to infer,
plan, reflect, and manipulate information already available
to it, while acting allows the agent to intervene in or query
the external environment to obtain new information or cause
state changes. In most agent frameworks, these capabilities
are treated as qualitatively different stages (e.g., reasoning
first, action later), or as loosely coupled components in a
pipeline. We argue that this separation obscures a more fundamental question faced by autonomous agents: how should
an agent decide whether remaining uncertainty should be resolved internally or through external interaction? To make
this decision explicit, we adopt a unifying abstraction in
which both reasoning and acting are treated as forms of tool
use for knowledge acquisition.

We argue that these behaviors are best understood as failures
of sequential decision making under epistemic uncertainty.
At each step of execution, an agent must decide how to allocate epistemic effort: whether to resolve uncertainty internally through reasoning, or to delegate it externally through
interaction. This decision cannot eliminate epistemic difficulty; it can only reallocate where that difficulty is resolved.
Crucially, unnecessary delegation does more than introduce
inefficiency—it suppresses the development of internal reasoning capability, shaping the long-term intelligence of the
agent, as shown in Figure 1. To formalize this view, we introduce the Theory of Agent (ToA), a framework that models
agents as tool-use decision makers governed by epistemic
constraints. ToA defines a knowledge boundary that separates tasks solvable internally from those requiring external
interaction. Because this boundary is latent, agents must
approximate it through belief-based solvability estimates
and policy-dependent thresholds. We further introduce the
notion of epistemic effort, an invariant task requirement that
no policy can eliminate, only redistribute between internal
reasoning and external interaction. Within this framework,
alignment is not defined by correctness alone, but by effortconsistent decision making: allocating epistemic effort in
a manner consistent with the agent’s internal capabilities
and long-term development. This perspective yields concrete implications for evaluation, revealing why correctness
with excessive tool use is still misaligned, and why learning
systems that over-delegate stagnate in internal reasoning
capability.

This unification is not a claim that reasoning and acting
are identical, nor a restatement of standard agent pipelines.
Rather, it reframes both as decision alternatives for resolving uncertainty. The distinction between them lies in the
provenance of information they access: internal tools reorganize or recombine existing information, whereas external
tools introduce new information or effects that were not
previously available to the agent.
Position: Reasoning and Acting as KnowledgeAcquisition Tools
Reasoning and acting are treated as alternative tools for reducing epistemic uncertainty: reasoning entails an internal
cognitive tool that operate exclusively over information
already available within the agent (e.g., parameters and
context), while acting entails an external physical tools
acquire new information or induce state changes through
interaction with the environment.

The remainder of the paper develops this position in a stepwise manner. Section 2 reframes reasoning and acting as
alternative means of knowledge acquisition, providing a unified foundation for analyzing tool-use decisions. Section 3
introduces the core theoretical objects of ToA-including internal and world task sets, knowledge boundaries, and epistemic effort-and shows how common agent failures arise
from misaligned effort allocation rather than insufficient capability. Section 4 then examines how these principles shape
learning and training dynamics, explaining why unnecessary
delegation can stall internal reasoning development even

Under this view, internal cognitive tools refer to internal
cognitive mechanisms that support systematic or investigative thinking to solve problems (Jonassen, 1992; Kommers
et al., 1992), while external physical tools refer to modules
or interfaces outside the model that are invoked through
specific triggers, such as rules, actions, or special tokens,
whose outputs are then incorporated into the model’s context to inform subsequent reasoning (Hao et al., 2023; Lu
2

Submission and Formatting Instructions for ICML 2026

et al., 2025). As a result, internal reasoning can fail when
required information lies outside this scope, leading to fail
trajectories. Conversely, external interaction is not intrinsically superior or more reliable. When agents invoke external
tools despite sufficient internal information, they introduce
unnecessary interaction, latency, and dependency on the
environment. More importantly, such delegation bypasses
opportunities for internal knowledge consolidation and reasoning development 1 .

2023), which can be viewed as special cases where internal
tool steps (e.g., reasoning) are treated as monolithic thought
units ri , leveraging the model’s pre-trained cognitive abilities without requiring explicit tool separation. (2) It aligns
with findings from large reasoning models (LRMs), which
show that outcome-based reinforcement learning (RL) can
effectively train agents to discover and utilize internal cognitive tools (Team, 2025). The same principle applies to
external physical tools, as shown in recent studies on toolaugmented agents (Jin et al., 2025). Thus, the framework
provides a coherent foundation for agentic learning across
both domains. (3) Most importantly, this perspective leads
to a new learning paradigm: next tool prediction. Just as
next-token prediction enables LLMs to learn lots of world
knowledge from text, next-tool prediction allows agents to
learn procedural knowledge through interaction.

Treating reasoning and acting as alternative, co-available
tools clarifies that neither should be privileged a priori. They
are co-equal in the precise sense that each is justified only
insofar as it can reduce remaining epistemic uncertainty.
This perspective goes beyond the status quo by making
tool-use decisions explicit objects of analysis. Rather than
optimizing reasoning quality or action efficiency in isolation, it enables principled evaluation of when interaction
is epistemically necessary and when it constitutes unnecessary delegation, setting the stage for the normative position
developed in Section 3.

3. Position: Agent Should Invoke External
Tools ONLY When Epistemically Necessary
Autonomous agents based on large language models repeatedly face a fundamental decision during task execution:
Should I continue reasoning internally, or should I interact
with the external world to obtain more information? This
decision arises at every step of agent execution and underlies
common failure modes such as overthinking and overacting.
We argue that these behaviors are best understood as failures
in sequential decision-making under epistemic uncertainty,
rather than as isolated deficiencies of reasoning or tool execution. In this section, we formalize agent behavior from
this perspective and articulate a small set of propositions
that together characterize effective tool-use decisions.

2.2. Tool-Integrated Agents
Building on the unification of reasoning and acting, we
further propose a redefinition of the agent grounded in this
integrated perspective:
Position: Definition of Agent
An agent is an entity that coordinates internal cognitive
tools (which transform or recombine existing internal
information) and external physical tools (which acquire
new information or induce state changes) to achieve a
goal.

3.1. Task Sets and Knowledge Boundary

Let an agent with model m interact with an environment
M over discrete steps. At step t, the agent chooses an
action/tool at ∈ T and receives an observation ot . We
partition the tool/action set into

We now define the core ontological object in our framework.
Definition 3.1 (Internal and World Task Sets). Let Q denote
the space of solvable tasks defined by the environment. For a
given fixed agent 2 or model m and environment M, define:

T = Tint ∪ Text ,
where Tint denotes internal cognitive tools (e.g., reasoning,
reflection), and Text denotes external physical tools (e.g.,
search, APIs, UI actions). The interaction history (context)
up to step t is

• The internal task set Qint (m, M) as the set of tasks
that the agent can complete reliably using internal reasoning alone, without invoking external tools.
• The world task set Qworld (M) as the set of all tasks
that are in principle solvable in the environment given
access to appropriate external interaction. By construction, Qint (m, M) ⊆ Qworld (M)

τt ≜ (q, a1 , o1 , . . . , at−1 , ot−1 ),
where q denotes the task/query specification. A (possibly
stochastic) agent policy π maps context to tool choices:
at ∼ π(· | τt ).

Definition 3.2 (Knowledge Boundary). The knowledge
boundary of an agent model m is defined by the separation between its internal task set Qint (m, M) and the
world task set Qworld (M). Tasks in Qext (m, M) =

This unified framework offers several key advantages: (1)
It generalizes prior approaches such as ReAct (Yao et al.,
1
We provide more concrete examples for internal cognitive tool
and external physical tool in Appendix A.

2

3

A fixed agent means the memory and tools are also fixed.

Submission and Formatting Instructions for ICML 2026
World
Task Set

Knowledge
boundary

World
Task Set

World
Task Set

Minimal
task set

Definition 3.5 (Context-Conditioned Internal Solvability
(Operational Estimate)). For a task q, agent model m, environment M, and interaction context τt , define

Maximal task set

Internal
Task Set

pint
t (q, m; M) ≜ Pr(S = 1 | q, m, τt , M, π ∈ Πint ) (3)
Figure 2. The high-level illustration of internal, world and
population-relative task sets.

where Πint denotes policies that do not invoke external tools
and S = 1 indicates successful task completion.

Qworld (M) \ Qint (m, M) require external interaction to
be completed reliably by the agent.

It is a belief-like operational surrogate used by the agent to
estimate whether the current task lies within its internal task
set given the available context.

Observation 1: Model-Specific Knowledge Boundaries.
For a given environment M, different agent models may
exhibit different internal task sets Qint (m, M) due to differences in training data, architecture, memory, and available
tools. In sufficiently simple environments, these sets may
coincide across models. However, in realistic or challenging
task regimes, the location of the knowledge boundary is
model-dependent, implying that no single tool-use policy
can be uniformly appropriate across all agents. We provide
a illustration in Fig 2.

Definition 3.6 (Operational Threshold). Let α ∈ (0, 1)
denote a policy-dependent confidence threshold. An
agent treats a task q as internally solvable at step t if
pint
t (q, m; M) ≥ α.
Observation 2: Belief-Dependent Classification. Different agents, or the same agent at different stages of interaction, may assign different values of pint
t (q, m; M) to the
same task. Moreover, even given identical estimates, agents
may exhibit different tool-use behavior due to different policy thresholds α, reflecting differences in risk tolerance,
efficiency preferences, or deployment constraints.

Definition 3.3 (Population-relative Task Sets). Let Magents
denote a fixed population of agent models. We define minimal and maximal task set as:
\
Qmin ≜
Qint (m),
(1)

From Belief to Action. Given an operational estimate
pint
t (q, m; M) and a policy-dependent threshold α, a natural class of tool-use policies can be expressed as beliefconditioned decision rules. For example, an agent may
choose to rely on internal reasoning when pint
t (q, m; M) ≥
α, and invoke external tools otherwise. Crucially, this rule
does not define the agent’s true knowledge boundary, but
only specifies how epistemic beliefs are translated into actions under uncertainty. Different agents may adopt different
thresholds or more complex mappings, leading to diverse
tool-use behaviors even when underlying task sets coincide.

m∈Magents

Qmax ≜

[

Qint (m).

(2)

m∈Magents

Qmin captures competence shared by all agents in the population, while Qmax represents the envelope of internal
competence achievable within the population 3 .
Proposition 3.4 (Population-Relative Tool Necessity). For
a fixed agent population Magents , any task

Although internal solvability is latent, it is not static. As
agents reason or interact, the available context typically
expands, incorporating intermediate results, partial conclusions, or newly acquired information. For tasks where such
context is relevant, this expansion can strictly increase the
agent’s internal solvability estimate, effectively shifting the
knowledge boundary during execution. We formalize this
monotonicity property in Appendix B.

q ∈ Qworld \ Qmax
cannot be solved internally by any agent in the population.
Consequently, successful completion of such tasks requires
external interaction for all agents in Magents .
3.2. Tool Use as Belief-Based Classification
In practice, Qint (m) is latent and cannot be observed directly. Therefore, it is important make tool-use decisions
under epistemic uncertainty, based on the agent’s internal estimates of whether a task lies within its internal task set. As
a result, tool-use behavior reflects a stochastic and contextdependent classification of tasks relative to the knowledge
boundary, rather than a fixed decision boundary.

3.3. Effort Allocation under Epistemic Uncertainty
While task sets and knowledge boundaries define what an
agent can solve internally, they do not determine how an
agent should allocate internal reasoning and external interaction during execution. To capture this, we introduce the notion of epistemic effort, which captures the task-dependent
informational burden that must be resolved for successful
completion. Importantly, epistemic effort is not a measure

3
Throughout this subsection, we assume a fixed environment
M and omit it from notation when unambiguous.

4

Submission and Formatting Instructions for ICML 2026
Overthinking and
Overacting Area

Underthinking and
Overacting Area

Underthinking and
Underacting Area

high

Interpretation. This proposition formalizes a fundamental constraint on agent behavior. External tools do not remove epistemic difficulty; they shift where the difficulty is
resolved. Stronger agents—those with larger internal task
sets—can satisfy a greater fraction of E ⋆ (q, m) internally,
while weaker agents rely more heavily on external interaction. However, the total epistemic effort required by the task
is invariant to the agent’s strategy.

Overthinking and
Underacting Area

high

A
Solvable Area
𝐸

!"

# +

𝐸

$%

& =

𝐸∗

low

C
low

Internal Reasoning

𝐸

!"

External Interaction

External Interaction

A

Solvable Area

𝐸

$%

& =

𝐸∗

B

low

high

(a) Epistemic Effort for Internal Task Set

# +

low

Internal Reasoning

high

This invariance explains why agents with different internal
capabilities may achieve similar task performance through
different effort allocations, and why excessive internal reasoning or excessive tool use both represent inefficient responses to epistemic uncertainty. We provide a high-level
illustration in Fig 3.

(b) Epistemic Effort for External Task Set

Figure 3. A high-level illustration of epistemic effort allocation and failure modes in tool-augmented agents for: (a) task
in Qint (m, M); and (b) task in Qext (m, M). The difference is
the internal and external efforts can transfer freely for internal
task (e.g., the segment AC), but external efforts are necessary for
external task. Point A represents pure delegation in which the
agent immediately calls an external tool (e.g., a stronger agent)
with negligible internal reasoning. Point B denotes the ideal frontier, corresponding to the minimal external effort required to solve
the task when internal reasoning is fully exploited. Point C represents pure internal reasoning without any external interaction.
The shaded regions illustrate characteristic misallocations of effort, such as underthinking, overacting, and their combinations,
arising from decision-boundary misalignment rather than insufficient capability. The solvable area represents the set of feasible
internal–external effort allocations under which the agent can successfully solve a problem.

Proposition 3.8 (Delegation-Induced Capability Stagnation). If an agent systematically allocates epistemic effort
to external interaction for tasks that lie within its internal
task set, then its internal reasoning capability for those
tasks will not improve through experience, even when such
improvement is possible in principle 4 .
Relation to Autonomous Intelligence. Our position
aligns closely with LeCun’s vision of autonomous machine
intelligence (LeCun, 2022), which emphasizes minimizing
real-world actions by internalizing knowledge about the
world. Within our framework, this principle arises naturally:
external actions are minimized when internal reasoning is
sufficient to satisfy the remaining epistemic effort. Crucially, ToA makes explicit the decision mechanism underlying this behavior—external interaction is justified only
when epistemically necessary—and shows that unnecessary
delegation not only reduces efficiency, but also impedes the
development of internal intelligence.

of cost or efficiency, but a structural requirement imposed
by the task relative to the agent’s capabilities.
An agent may satisfy this requirement through a combination of internal reasoning and external interaction. We
express this decomposition as
E(q, m) = Eint (q, m) + Eext (q, m),

(4)

where Eint (q, m) denotes effort satisfied through internal cognitive tools and Eext (q, m) denotes effort satisfied
through external physical tools.

Implications for Evaluation. Although the internal task
set Qint (m, M) and the minimal epistemic effort E ⋆ (q, m)
are latent and cannot be directly observed, Proposition 3.7
provides a principled basis for evaluating agent behavior.
Since epistemic effort cannot be eliminated, agents can only
differ in how they allocate effort between internal reasoning and external interaction. As a result, evaluation should
focus not solely on task success, but on patterns of effort
reallocation: whether agents increasingly satisfy epistemic
requirements internally as their competence grows, whether
they invoke external tools only when internal reasoning is
insufficient, and whether additional effort contributes meaningfully to task progress. Agents that achieve correctness
while systematically over-allocating either internal or external effort can therefore be identified as miscalibrated, even
when their final answers are correct.

Proposition 3.7 (Epistemic Effort as an Unavoidable Requirement). Fix an agent m, environment M, and task
q ∈ Qworld (M). Let Πsucc (q, m, M) denote the set of policies that successfully complete q. Define the task’s minimal
required epistemic effort as the infimum
E ⋆ (q, m) ≜

inf
π∈Πsucc (q,m,M)




π
π
Eint
(q, m) + Eext
(q, m) .
(5)

Then for any successful policy π ∈ Πsucc (q, m, M),
π
π
Eint
(q, m) + Eext
(q, m) ≥ E ⋆ (q, m).

(6)

By definition, no successful policy can eliminate this requirement; it can only reallocate effort between internal
reasoning and external interaction.

4

External tools can compensate for missing information, but
they cannot replace the experience required to develop it. We
provide detailed explanations in Appendix C.1.

5

Submission and Formatting Instructions for ICML 2026

3.4. Alignment as Effort-Consistent Decision Making

eliminate epistemic effort, only decide whether it is resolved
internally or delegated externally. This section examines
the consequences of this view for learning and training. We
argue that effective agents require calibrated meta-cognition
to allocate effort consistently with their internal capabilities
(Section 4.1), and that misallocation not only causes inefficiency but also shapes long-term intelligence development.
We analyze how this principle manifests during training
and inference, characterize observable behavioral regimes
(Section 4.2), and discuss practical pathways toward effortconsistent agent behavior (Section 4.3).

The preceding analysis motivates a central behavioral requirement for agents: tool-use decisions should allocate
epistemic effort in a manner consistent with both immediate
task requirements and long-term capability development. At
each step of execution, an agent implicitly chooses how to
allocate epistemic effort. Invoking internal reasoning allocates effort to Eint , while invoking external tools allocates
effort to Eext . Because the total required effort E ⋆ (q, m) is
fixed, misallocation does not reduce difficulty—it merely
shifts inefficiency and alters learning dynamics.

4.1. Meta-Cognition as Solvability Assessment

Effort-Consistent Alignment. An agent is aligned if its
tool-use decisions allocate epistemic effort in a manner
consistent with its internal task set. Specifically, internal
reasoning should be applied when it meaningfully reduces
epistemic uncertainty, and external interaction should be
invoked only when internal reasoning is insufficient to do
so. To make this concrete, consider an agent’s internal
solvability estimate pint
t (q) at step t. A simple decision rule
illustrates the principle:
(
at ∈ Tint , pint
t (q, m, M) ≥ α,
π(at | τt ) =
(7)
at ∈ Text , pint
t (q, m, M) < α,

Given that epistemic effort must be allocated rather than
eliminated, agents require a mechanism for deciding where
remaining uncertainty should be resolved. We argue that
this mechanism is meta-cognition (Dunlosky & Metcalfe,
2008; Ackerman & Thompson, 2017): the agent’s ability to
assess whether internal reasoning can meaningfully reduce
epistemic uncertainty, or whether external interaction is
necessary.
Training-time Alignment. After pretraining, a model’s
internal reasoning capability, reflected in its distribution of
internal solvability across tasks, is relatively stable. In contrast, the policy that maps solvability estimates to tool-use
decisions remains adjustable during alignment. Training
thus plays a critical role in calibrating how agents translate
epistemic uncertainty into action. As illustrated in Section 3.4, systematic miscalibration leads to two dominant
failure modes. Overestimating internal solvability causes
agents to rely on internal reasoning where it is unreliable,
resulting in hallucination or incorrect reasoning (Gekhman
et al., 2024). Underestimating internal solvability leads
agents to invoke external tools unnecessarily, incurring
avoidable interaction overhead and inefficiency (Qian et al.,
2025). Importantly, these failures arise not from deficiencies in reasoning or tools themselves, but from misaligned
meta-cognitive judgments. Effective training therefore aims
to calibrate tool-use decisions with respect to internal solvability. Approaches such as supervised fine-tuning with
explicit tool-use supervision, or reinforcement learning with
task-level feedback, can encourage agents to invoke external
tools primarily when internal solvability is low, and to rely
on internal reasoning otherwise, as elaborated in Section 4.3.

where α is a policy-dependent operating threshold. Crucially, this rule is not optimal because it minimizes cost or
latency, but because it respects the epistemic effort invariant:
external tools are invoked only when internal effort cannot
satisfy the remaining epistemic requirement.
Proposition 3.9 (Effort-Consistent Decision Alignment).
Effective tool-use policies allocate epistemic effort such
that internal reasoning is used for tasks within the agent’s
internal task set, while external interaction is used primarily
for tasks outside it. Systematic deviation from this allocation
leads to inefficiency without reducing the total epistemic
effort required for task completion.
Corollary 3.10 (Failure Modes as Effort Misallocation).
Systematic overuse of internal reasoning allocates effort
where it cannot reduce uncertainty, leading to overthinking
and hallucination. Systematic overuse of external tools
reallocates effort unnecessarily, leading to overacting and
inefficiency. Both failure modes violate effort-consistent
alignment, even when final task success is achieved.
Together, these results show that alignment is not merely
about producing correct outputs, but about allocating epistemic effort in a way that supports both reliable behavior
and the continued development of internal intelligence.

Inference-time Alignment. During inference, agents operate under incomplete and evolving information. Initial
contexts may be insufficient to determine whether internal
reasoning alone will succeed. By interacting with external
tools—such as querying APIs or executing actions—the
agent incrementally augments its context, which in turn updates its internal solvability estimate. Inference thus unfolds

4. Implications for Learning and Training
Until now, we establish that tool-use behavior is governed by
epistemic effort allocation under uncertainty: agents cannot
6

Submission and Formatting Instructions for ICML 2026

as a sequential feedback loop, in which the agent alternates between internal reasoning and external interaction
while continuously reassessing whether further information
is needed. Meta-cognition is essential to regulating this
loop: without accurate self-assessment, the agent may terminate prematurely, persist in unproductive reasoning, or
overuse tools inefficiently. Robust inference-time behavior emerges when agents can adaptively balance internal
reasoning and external interaction in response to changing
epistemic conditions.

internal scope. This mode corresponds to overestimating
internal solvability and is a common source of hallucination
or logically consistent but factually incorrect outputs.
Low internal reasoning and low external tool use. This
mode represents the most efficient observable behavior:
the agent solves tasks using minimal internal deliberation
and invokes external tools only when epistemically necessary (Arora & Zanette, 2025; Wang et al., 2025a) (e.g., point
B in Fig 3). Such behavior reflects well-calibrated metacognition and effective alignment between internal solvability estimates and tool-use decisions. However, achieving
this regime reliably is non-trivial: overly aggressive minimization risks underthinking or premature termination on
complex tasks. Training agents to operate in this regime
therefore requires careful balancing of correctness and efficiency signals.

4.2. Behavioral Regimes under Tool-Use Uncertainty
We therefore examine four representative behavior modes
defined by how agents allocate epistemic effort between
internal reasoning and external interaction to solve the task
successfully, and discuss their consequences for alignment,
efficiency, and long-term capability development.

4.3. Paths toward Aligned and Efficient Agent Behavior

High internal reasoning and high external tool use. In
this mode, the agent invokes extensive internal reasoning
while also frequently calling external tools, regardless of
epistemic necessity. Although this behavior may achieve
correctness, it is inefficient and obscures the underlying decision logic. The agent neither trusts its internal competence
nor relies selectively on external information, effectively
treating tool use as brute-force exploration. This pattern
reflects poor calibration of internal solvability estimates
and leads to unnecessary computational overhead, increased
latency, and higher risk of cascading errors.

The behavioral regimes above reveal that alignment is not
achieved by maximizing external tool use or maximizing internal reasoning, but by learning when each mode of effort
allocation is epistemically justified. This reframes training as a problem of calibrating decisions under uncertainty
rather than optimizing a fixed notion of optimal behavior. In
the following, we outline several complementary approaches
that move agents toward this objective.
Agentic Pretraining. Large language models acquire extensive world knowledge through next-token prediction,
effectively compressing information into their parametric space (Kaplan et al., 2020). However, this objective
alone does not teach agents how to acquire new knowledge through interaction. To address this gap, we advocate
extending pretraining with next-tool prediction, where interaction itself becomes a first-class modeling target. By
learning to predict which tool to invoke given a context, the
agent is trained not only to reason, but to decide how to
reduce uncertainty. Modeling interactions (e.g., API calls,
UI navigation, or environment actions) as structured outputs
enables agents to learn procedural knowledge acquisition,
rather than relying solely on static compression. As agent
architectures become more unified, this shift opens the door
to a new form of scaling: one that governs knowledge acquisition through interaction, rather than knowledge storage
alone (Xie et al., 2024b; Li et al., 2024).

Low internal reasoning and high external tool use.
Here, the agent systematically defers to external tools while
underutilizing its internal reasoning capability (e.g., from
point B to point A for external task; from point C to point
A for internal task as shown in Fig 3). This behavior may be
effective for weaker models or information-intensive tasks,
but it introduces persistent inefficiency and dependence on
external systems. More critically, it undermines the goal
of model scaling and continual learning: by outsourcing
problems that could be solved internally, the agent fails
to consolidate and exploit its own parametric knowledge.
From the perspective of Section 3, this mode corresponds to
underestimating internal solvability.
High internal reasoning and low external tool use. In
this regime, the agent relies heavily on internal reasoning
and avoids external interaction, even when external information could simplify or disambiguate the task (Wang et al.,
2025a). This behavior reflects strong internal competence
and autonomy, and is desirable in constrained or offline environments. However, excessive internal deliberation can
lead to overthinking, long reasoning traces, or brittle inference when required information lies outside the model’s

Agentic Supervised Fine-Tuning. Supervised fine-tuning
(SFT) remains a common approach for teaching agents how
and when to use tools, often through curated demonstrations
on specific tasks (Gou et al.; Li et al., 2025a). However, such
approaches frequently assume a uniform internal capability
across models. As discussed in Section 3.1, this assump7

Submission and Formatting Instructions for ICML 2026

tion is unrealistic: what constitutes appropriate tool use
for a small model may be redundant or counterproductive
for a larger one. One approach is to tailor SFT datasets to
each model’s internal competence, but this quickly becomes
resource-intensive. A more scalable alternative is to train
agents to defer selectively when faced with unfamiliar or
low-solvability contexts, approximating a conservative upper envelope of internal capability (Qian et al., 2025) (e.g.,
by assuming some tasks naturally fall into Qworld \ Qmax in
Proposition 3.4). While this improves generality, it may
sacrifice precision in specialized domains, illustrating a
fundamental trade-off between scalability and fine-grained
alignment.

internal solvability and allocate effort accordingly—whether
through pretraining, supervision, reinforcement learning, or
prompting—are better positioned to produce efficient, robust, and adaptable agents. In this sense, alignment is not
a fixed target but an emergent property of well-calibrated
decision-making. The paths outlined above represent complementary strategies for steering agents away from systematically misaligned regimes and toward behavior that
balances reasoning and acting in realistic environments.

5. Alternative Views
Intelligent agents have been conceptualized through several
dominant paradigms, each emphasizing a different computational bottleneck. We briefly contrast them with our
position: 1) Agents as planners view decision-making as
plan optimization over an internal world model. This perspective presumes sufficient internal knowledge and offers
no principled criterion for deciding when external information must be acquired; 2) Agents as policy learners (e.g.,
in reinforcement learning) treat tool use as just another action optimized for reward. While effective for control, this
view does not distinguish epistemically necessary tool use
from unnecessary delegation, allowing agents to overuse
tools as long as rewards are achieved; 3) Agents as workflow
orchestrators focus on coordinating tools and procedures
to complete tasks reliably. These approaches emphasize
execution but largely ignore whether tool use is justified,
permitting correctness at the cost of inefficiency and limited
internal capability growth.

Agentic Reinforcement Learning: Calibrating Decisions
through Experience. RL provides a natural mechanism
for aligning tool-use decisions with internal solvability, as
agents can learn from interaction outcomes rather than static
demonstrations. Crucially, effective RL for agents must go
beyond correctness-based rewards. Optimizing solely for
task success ignores how solutions are reached, allowing
inefficient or miscalibrated behaviors to persist (Jin et al.,
2025; Li et al., 2025b). Recent methods such as OTCPO (Wang et al., 2025a) explicitly balance correctness with
penalties for unnecessary tool use, encouraging agents to
act with restraint. More broadly, RL enables agents to learn
process-level preferences: when to reason, when to act,
and when to stop. We further envision an iterative training
paradigm, RL → SFT → RL, where reinforcement learning
discovers aligned trajectories under uncertainty, and supervised fine-tuning consolidates these behaviors for stability
and generalization. Such cycles gradually refine both decision policies and meta-cognitive calibration.5 In addition, it
is extremely promising to consider RL during pre-training
stage with sufficient computing resources.

In contrast, we argue that an agent should invoke external
tools only when epistemically necessary. External interaction is justified if and only if the remaining epistemic effort
required to complete a task cannot be satisfied through internal reasoning alone. Tool use reallocates epistemic effort; it
does not eliminate it. Unnecessary delegation is therefore
not merely inefficient—it suppresses the development of
internal reasoning capability. This position is most appropriate when the central bottleneck is epistemic efficiency
and intelligence development, rather than control optimality
or execution speed. It provides a normative criterion for
tool use, explains failure modes such as overthinking and
overacting, and directly informs training and evaluation.

Agentic Prompting. Prompting-based methods enable
agents to exhibit complex tool-use behaviors without parameter updates (Chen et al., 2023; Qiu et al., 2025). While
effective in practice, these approaches often lack systematic evaluation of decision quality, allowing overthinking or
overacting to persist beneath correct outputs. Recent work
incorporating memory or workflow abstractions (Zhang
et al., 2024) demonstrates that prompting can guide more efficient behavior, but sustaining alignment typically requires
integration with learning-based methods.

6. Conclusion
This paper introduces the Theory of Agent (ToA), a framework that views modern agents as tool-use decision makers
operating under epistemic uncertainty. We argue that the
central challenge in agent behavior is not how to reason or
act, but when external interaction is epistemically necessary.
By distinguishing an agent’s internal task set from the world
task set, ToA formalizes a knowledge boundary that governs

Summary and Implications Across these approaches,
a common theme emerges: improving agent behavior is
less about maximizing reasoning or minimizing tool use,
and more about calibrating decisions under epistemic uncertainty. Methods that encourage agents to estimate their own
5

Additional future directions are discussed in Appendix E.

8

Submission and Formatting Instructions for ICML 2026

rational tool use. Thus, tool use does not eliminate epistemic
difficulty but reallocates it. Agents that invoke external
tools for internally solvable tasks may achieve correctness
yet hinder the development of internal reasoning capability,
while agents that rely on internal reasoning beyond their
knowledge boundary exhibit overthinking and hallucination.
These failure modes stem from misaligned effort allocation
rather than deficiencies in reasoning or tools. We hope this
framework informs future work on agent alignment, evaluation, and design, contributing to the development of more
capable and autonomous machine intelligence.

function-infused and synthesis-friendly modular chemical
language model. In arxiv, 2025.
Gekhman, Z., Yona, G., Aharoni, R., Eyal, M., Feder, A.,
Reichart, R., and Herzig, J. Does fine-tuning llms on
new knowledge encourage hallucinations? arXiv preprint
arXiv:2405.05904, 2024.
Gou, Z., Shao, Z., Gong, Y., Yang, Y., Huang, M., Duan,
N., Chen, W., et al. Tora: A tool-integrated reasoning
agent for mathematical problem solving. In The Twelfth
International Conference on Learning Representations.
Han, D., McInroe, T., Jelley, A., Albrecht, S. V., Bell, P., and
Storkey, A. LLM-personalize: Aligning LLM planners
with human preferences via reinforced self-training for
housekeeping robots. In Rambow, O., Wanner, L., Apidianaki, M., Al-Khalifa, H., Eugenio, B. D., and Schockaert, S. (eds.), Proceedings of the 31st International Conference on Computational Linguistics, pp. 1465–1474,
Abu Dhabi, UAE, January 2025. Association for Computational Linguistics. URL https://aclanthology.
org/2025.coling-main.98/.

Acknowledgement
We would like to express our sincere gratitude to the HotDesk group at the University of Edinburgh for their valuable
feedback and insightful suggestions, with special appreciation to Jushi Kai, Shujia Liu, and Miao Li. We will continue
to enrich this theory of agent, and welcome to join us!

References
Ackerman, R. and Thompson, V. A. Meta-reasoning: Monitoring and control of thinking and reasoning. Trends
in Cognitive Sciences, 21(8):607–617, 2017. ISSN
1364-6613. doi: https://doi.org/10.1016/j.tics.2017.05.
004. URL https://www.sciencedirect.com/
science/article/pii/S1364661317301055.

Hao, S., Liu, T., Wang, Z., and Hu, Z. Toolkengpt: Augmenting frozen language models with massive tools via
tool embeddings. Advances in neural information processing systems, 36:45870–45894, 2023.
Hongru, W., Cai, D., Zhong, W., Huang, S., Pan, J. Z., Liu,
Z., and Wong, K.-F. Self-reasoning language models:
Unfold hidden reasoning chains with few reasoning catalyst. In Workshop on Reasoning and Planning for Large
Language Models, 2025.

Arora, D. and Zanette, A. Training language models to
reason efficiently, 2025. URL https://arxiv.org/
abs/2502.04463.
Chen, G., Dong, S., Shu, Y., Zhang, G., Sesay, J., Karlsson, B. F., Fu, J., and Shi, Y. Autoagents: A framework for automatic agent generation. arXiv preprint
arXiv:2309.17288, 2023.

Jin, B., Zeng, H., Yue, Z., Wang, D., Zamani, H., and
Han, J. Search-r1: Training llms to reason and leverage
search engines with reinforcement learning, 2025. URL
https://arxiv.org/abs/2503.09516.

Cuadron, A., Li, D., Ma, W., Wang, X., Wang, Y., Zhuang,
S., Liu, S., Schroeder, L. G., Xia, T., Mao, H., Thumiger,
N., Desai, A., Stoica, I., Klimovic, A., Neubig, G., and
Gonzalez, J. E. The danger of overthinking: Examining
the reasoning-action dilemma in agentic tasks, 2025. URL
https://arxiv.org/abs/2502.08235.

Jonassen, D. H. What are cognitive tools? In Cognitive
tools for learning, pp. 1–6. Springer, 1992.
Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B.,
Chess, B., Child, R., Gray, S., Radford, A., Wu, J.,
and Amodei, D. Scaling laws for neural language models, 2020. URL https://arxiv.org/abs/2001.
08361.

Dunlosky, J. and Metcalfe, J. Metacognition. Sage Publications, 2008.

Kolt, N.
Governing ai agents.
arXiv:2501.07913, 2025.

Edwards, C., Naik, A., Khot, T., Burke, M., Ji, H., and
Hope, T. Synergpt: In-context learning for personalized
drug synergy prediction and drug design. In Proc. 1st
Conference on Language Modeling (COLM2024), 2024.

arXiv preprint

Kommers, P. A., Jonassen, D. H., and Mayes, J. T. Cognitive
tools for learning. Springer, 1992.

Edwards, C., Han, C., Lee, G., Nguyen, T., Prasad, C. K.,
Szymkuc, S., Grzybowski, B. A., Jin, B., Diao, Y., Han,
J., Liu, G., Peng, H., Burke, M. D., and Ji, H. mclm: A

LeCun, Y. A path towards autonomous machine intelligence
version 0.9. 2, 2022-06-27. Open Review, 62(1):1–62,
2022.
9

Submission and Formatting Instructions for ICML 2026

Li, C., Xue, M., Zhang, Z., Yang, J., Zhang, B., Wang, X.,
Yu, B., Hui, B., Lin, J., and Liu, D. Start: Self-taught
reasoner with tools, 2025a. URL https://arxiv.
org/abs/2503.04625.
Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, E. L., Zhang, R., et al.
Embodied agent interface: Benchmarking llms for embodied decision making. Advances in Neural Information
Processing Systems, 37:100428–100534, 2024.
Li, X., Zou, H., and Liu, P. Torl: Scaling tool-integrated
rl, 2025b. URL https://arxiv.org/abs/2503.
23383.
Lu, P., Chen, B., Liu, S., Thapa, R., Boen, J., and Zou, J.
Octotools: An agentic framework with extensible tools
for complex reasoning. arXiv preprint arXiv:2502.11271,
2025.

Linguistics: EMNLP 2023, pp. 12047–12064, Singapore, December 2023. Association for Computational
Linguistics. doi: 10.18653/v1/2023.findings-emnlp.
806. URL https://aclanthology.org/2023.
findings-emnlp.806/.
Wang, H., Wang, H., Wang, L., Hu, M., Wang, R., Xue,
B., Huang, Y., and Wong, K.-F. Tpe: Towards better
compositional reasoning over cognitive tools via multipersona collaboration. In Natural Language Processing
and Chinese Computing: 13th National CCF Conference,
NLPCC 2024, Hangzhou, China, November 1–3, 2024,
Proceedings, Part II, pp. 281–294, Berlin, Heidelberg,
2024a. Springer-Verlag. ISBN 978-981-97-9433-1. doi:
10.1007/978-981-97-9434-8 22. URL https://doi.
org/10.1007/978-981-97-9434-8_22.
Wang, H., Wang, R., Xue, B., Xia, H., Cao, J., Liu, Z., Pan,
J. Z., and Wong, K.-F. AppBench: Planning of multiple
APIs from various APPs for complex user instruction. In
Al-Onaizan, Y., Bansal, M., and Chen, Y.-N. (eds.), Proceedings of the 2024 Conference on Empirical Methods in
Natural Language Processing, pp. 15322–15336, Miami,
Florida, USA, November 2024b. Association for Computational Linguistics. doi: 10.18653/v1/2024.emnlp-main.
856. URL https://aclanthology.org/2024.
emnlp-main.856/.

Nguyen, T., Torres-Flores, T., Hwang, C., Edwards, C.,
Diao, Y., and Ji, H. Glad: Synergizing molecular graphs
and language descriptors for enhanced power conversion
efficiency prediction in organic photovoltaic devices. In
Proc. 33rd ACM International Conference on Information
and Knowledge Management (CIKM 2024), 2024.
Qian, C., Acikgoz, E. C., Wang, H., Chen, X., Sil, A.,
Hakkani-Tür, D., Tur, G., and Ji, H. Smart: Self-aware
agent for tool overuse mitigation, 2025. URL https:
//arxiv.org/abs/2502.11435.

Wang, H., Qian, C., Zhong, W., Chen, X., Qiu, J., Huang, S.,
Jin, B., Wang, M., Wong, K.-F., and Ji, H. Acting less is
reasoning more! teaching model to act efficiently, 2025a.
URL https://arxiv.org/abs/2504.14870.

Qin, Y., Ye, Y., Fang, J., Wang, H., Liang, S., Tian, S.,
Zhang, J., Li, J., Li, Y., Huang, S., Zhong, W., Li, K.,
Yang, J., Miao, Y., Lin, W., Liu, L., Jiang, X., Ma, Q.,
Li, J., Xiao, X., Cai, K., Li, C., Zheng, Y., Jin, C., Li, C.,
Zhou, X., Wang, M., Chen, H., Li, Z., Yang, H., Liu, H.,
Lin, F., Peng, T., Liu, X., and Shi, G. Ui-tars: Pioneering
automated gui interaction with native agents, 2025. URL
https://arxiv.org/abs/2501.12326.

Wang, H., Xue, B., Zhou, B., Zhang, T., Wang, C., Wang,
H., Chen, G., and Wong, K.-F. Self-DC: When to reason and when to act? self divide-and-conquer for compositional unknown questions. In Chiruzzo, L., Ritter,
A., and Wang, L. (eds.), Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 6510–
6525, Albuquerque, New Mexico, April 2025b. Association for Computational Linguistics. ISBN 979-8-89176189-6. URL https://aclanthology.org/2025.
naacl-long.331/.

Qiu, J., Qi, X., Zhang, T., Juan, X., Guo, J., Lu, Y., Wang, Y.,
Yao, Z., Ren, Q., Jiang, X., Zhou, X., Liu, D., Yang, L.,
Wu, Y., Huang, K., Liu, S., Wang, H., and Wang, M. Alita:
Generalist agent enabling scalable agentic reasoning with
minimal predefinition and maximal self-evolution, 2025.
URL https://arxiv.org/abs/2505.20286.

Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang,
J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X.,
Wei, Z., and Wen, J. A survey on large language model
based autonomous agents. Frontiers of Computer Science,
18(6), March 2024c. ISSN 2095-2236. doi: 10.1007/
s11704-024-40231-1. URL http://dx.doi.org/
10.1007/s11704-024-40231-1.

Team, D.-A. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL
https://arxiv.org/abs/2501.12948.
Wang, H., Wang, R., Mi, F., Deng, Y., Wang, Z., Liang,
B., Xu, R., and Wong, K.-F. Cue-CoT: Chain-of-thought
prompting for responding to in-depth dialogue questions
with LLMs. In Bouamor, H., Pino, J., and Bali, K.
(eds.), Findings of the Association for Computational

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi,
E., Le, Q. V., Zhou, D., et al. Chain-of-thought prompting
10

Submission and Formatting Instructions for ICML 2026

elicits reasoning in large language models. Advances in
neural information processing systems, 35:24824–24837,
2022.
Wu, J., Zhu, J., and Liu, Y. Agentic reasoning: Reasoning
llms with tools for the deep research. arXiv preprint
arXiv:2502.04644, 2025.
Xie, J., Zhang, K., Chen, J., Zhu, T., Lou, R., Tian, Y.,
Xiao, Y., and Su, Y. Travelplanner: A benchmark for
real-world planning with language agents. arXiv preprint
arXiv:2402.01622, 2024a.
Xie, T., Zhang, D., Chen, J., Li, X., Zhao, S., Cao, R., Hua,
T. J., Cheng, Z., Shin, D., Lei, F., et al. Osworld: Benchmarking multimodal agents for open-ended tasks in real
computer environments. Advances in Neural Information
Processing Systems, 37:52040–52094, 2024b.
Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan,
K., and Cao, Y. React: Synergizing reasoning and acting in language models. In International Conference on
Learning Representations (ICLR), 2023.
Zhang, J., Xiang, J., Yu, Z., Teng, F., Chen, X., Chen, J.,
Zhuge, M., Cheng, X., Hong, S., Wang, J., et al. Aflow:
Automating agentic workflow generation. arXiv preprint
arXiv:2410.10762, 2024.
Zhou, P., Pujara, J., Ren, X., Chen, X., Cheng, H.-T., Le,
Q. V., Chi, E., Zhou, D., Mishra, S., and Zheng, H. S. Selfdiscover: Large language models self-compose reasoning
structures. Advances in Neural Information Processing
Systems, 37:126032–126058, 2024.

11

Submission and Formatting Instructions for ICML 2026

A. Explanation about Internal Tools and External Tools
Internal cognitive tools. Cognitive tools refer to internal cognitive mechanisms that support systematic or investigative
thinking to solve problems (Jonassen, 1992; Kommers et al., 1992). In the context of intelligent agents, various reasoning
modules (Zhou et al., 2024; Hongru et al., 2025), such as Chain-of-Thought (Wei et al., 2022), reflection, decomposition (Wang et al., 2025b), and alternative-thinking, function as cognitive processes that enable the retrieval and manipulation
of internal knowledge to guide problem-solving. Beyond these, other cognitive tools appear in diverse applications, such
as conversational strategies in dialogue systems (Wang et al., 2024a) and psychologically inspired mechanisms designed
to model uncertainty, emotion, or user intent (Wang et al., 2023). Despite their varied forms, these tools share a common
function: they serve as triggers for internal knowledge retrieval, allowing the model to reason and act based on its internal
knowledge.
External physical tools. External physical tools refer to modules or interfaces outside the model that are invoked through
specific triggers, such as rules, actions, or special tokens, whose outputs are then incorporated into the model’s context to
inform subsequent reasoning (Hao et al., 2023; Lu et al., 2025). These tools provide access to information or functionality
that lies beyond the agent’s internal knowledge. Examples include querying a search engine (Jin et al., 2025), calling
an API (Wang et al., 2024b), interacting with a user interface (Han et al., 2025), or executing actions in an embodied
environment (Li et al., 2024). This perspective enables a unified treatment of diverse forms of interaction as structured tool
use: they serve as interfaces for external knowledge acquisition, allowing the model to access and interact with knowledge
beyond its internal capability.

B. Proofs and More preposition
Proposition B.1 (Context Expansion Tends to Increase Internal Solvability). Let τt ⊆ τt′ for t′ > t denote that the available
context is expanded. For tasks q for which the additional context is relevant and non-degrading,
int
pint
t (q, m; M) ≤ pt′ (q, m; M),

and hence

int
Qint
t (m; M) ⊆ Qt′ (m; M).

(8)

This proposition formalizes the intuition that, as interaction proceeds, agents may accumulate relevant intermediate results,
clarifications, or partial progress in τt that enables more tasks to be solved internally.

C. Discussions
C.1. Why Over-Delegation Leads to Capability Stagnation
The stagnation effect in Proposition 3.8 is not merely behavioral but arises from the learning dynamics induced by overdelegation. In most training settings, agents are optimized using outcome-based objectives—such as task success, correctness,
or sparse terminal reward—without explicit supervision over how uncertainty is resolved. When an external tool is available
and reliably produces correct information, invoking it becomes a low-risk strategy that guarantees reward, regardless of
whether the task could have been solved internally.
As a result, external tools act as a reward shortcut: they collapse epistemic uncertainty externally before internal reasoning
is exercised. This has a direct consequence for learning. Because the agent achieves success without relying on internal
reasoning, gradient signals associated with internal cognitive tools become sparse or uninformative. Internal reasoning
trajectories are neither required nor reinforced, and therefore receive little to no learning signal. Over time, the policy learns
to associate delegation—not reasoning—with reward.
This dynamic closely mirrors reward hacking in reinforcement learning. When the objective only measures task success,
the agent naturally exploits the most reliable path to reward, even if that path bypasses the intended capability. External
tools “save” the agent from failure, but in doing so, they also shield internal reasoning from both error signals and corrective
feedback. The agent becomes increasingly dependent on delegation, while its internal reasoning capability remains
under-trained or even degrades relative to what it could have achieved.
Crucially, this stagnation can occur even when internal reasoning is sufficient in principle. The issue is not that the agent
lacks capacity, but that the training signal fails to distinguish epistemically necessary tool use from unnecessary delegation.
In this sense, over-delegation is not simply inefficient—it actively alters the learning trajectory by suppressing opportunities
for internal knowledge consolidation and skill acquisition.
12

Submission and Formatting Instructions for ICML 2026

D. Impact Statements
This paper advances a conceptual understanding of tool-augmented agents by arguing that tool-use decisions shape not only
task efficiency but the long-term development of agent intelligence. By introducing epistemic necessity as a normative
criterion for external interaction, the Theory of Agent (ToA) reframes tool use from a performance optimization problem
to a learning-critical decision under uncertainty. This perspective has practical implications for the design, training, and
evaluation of autonomous agents: agents that over-delegate to external tools may achieve short-term correctness but risk
stagnating their internal reasoning capability, while epistemically calibrated agents can preserve and expand internal
competence over time.
Beyond improving efficiency or reducing hallucinations, this work highlights a broader societal implication: as agents
increasingly rely on external systems, unprincipled delegation may entrench dependency, fragility, and limited autonomy. By
emphasizing when external interaction is epistemically necessary rather than merely convenient, our framework encourages
the development of agents that learn more effectively, generalize better, and remain robust in settings where external access
is constrained or unreliable. We hope this work informs future research on agent alignment, evaluation, and long-horizon
learning, contributing to the development of more capable and autonomous machine intelligence.

E. Future Directions
Vision Agent. Vision agents extend our unified framework of reasoning and acting by incorporating visual affordances as
part of the decision-making loop. In our definition, external physical tools are invoked based on an agent’s knowledge gaps;
in vision agents, visual input becomes a direct means of detecting such gaps and informing tool use decisions. To realize this,
future systems should treat visual understanding not as passive recognition but as actionable epistemic input. This involves
embedding affordance-aware modules into vision-language models that not only recognize objects but predict possible
interactions. Moreover, meta-cognitive control should guide visual attention: the agent must actively attend to regions most
likely to resolve its uncertainty. Training in simulation with reinforcement learning can allow agents to learn the utility of
visual exploration for acquiring external knowledge, enabling more precise tool invocation grounded in perception.
Embodied Agent. Embodied agents concretize the external physical tool dimension by extending it into the physical world,
where the agent’s own body becomes a tool, and the environment imposes dynamic constraints. Within our framework,
this embodiment means that the agent’s knowledge boundary is not only cognitive but also physically bounded (e.g., what
can be seen, reached, or manipulated). To operationalize this, agents should be equipped with real-time sensorimotor
feedback loops and control modules that treat actions as epistemic moves: physical actions (e.g., MoveTo, PickUp) should
be treated like external tool calls that yield knowledge from the environment. Learning here must be closed-loop and
incremental—using reinforcement signals from physical interaction to adjust the decision boundary over time. Physical
meta-cognition, such as failure detection or confidence in execution, should guide whether to reason further, retry an action,
or explore alternatives.
Multi-Agent Coordination. Multi-agent coordination extends our framework from individual agents aligning their
decision and knowledge boundaries to a collective setting where these boundaries are distributed across multiple agents.
In this paradigm, each agent operates with a local view (its own knowledge and decision boundaries), but contributes to a
shared task by reasoning about and interacting with other agents. The key challenge is aligning these distributed boundaries
to form a coherent collective intelligence. To achieve this, agents must be equipped with mechanisms to communicate
epistemic state, and dynamically delegate subtasks to peers whose knowledge boundaries better match the problem context.
This requires structured communication protocols, role inference strategies, and shared meta-cognitive modules that manage
when to ask, respond, or act. Practically, this can be developed through multi-agent reinforcement learning in environments
where cooperation is required for successful task completion, with reward functions encouraging efficient division of
cognitive and physical labor.

13

