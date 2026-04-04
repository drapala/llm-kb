---
source: https://arxiv.org/abs/2407.04363
authors: Petr Anokhin, Nikita Semenov, Artyom Sorokin, Dmitry Evseev, Andrey Kravchenko, Mikhail Burtsev, Evgeny Burnaev
date: 2024-07-05
type: paper
arxiv: "2407.04363"
venue: IJCAI 2025
stance: challenging
github: https://github.com/AIRI-Institute/AriGraph
---

# AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents

## Abstract

Addresses unstructured memory representations that impede reasoning and planning. AriGraph enables agents to construct and update a memory graph integrating semantic and episodic memories while exploring the environment. Ariadne agent demonstrates strong performance on complex interactive text games and competitive multi-hop QA. Substantially outperforms existing memory methods and RL baselines.

## Key Contribution

AriGraph constructs and UPDATES a knowledge graph ONLINE during environment exploration — not just at indexing time. This is the missing piece from HippoRAG (static post-indexing) and Synapse (spreading activation but not structural update).

## Direct Challenge to RWKG

AriGraph demonstrates that the "adaptive graph topology" concept from RWKG is not novel — AriGraph already does online graph updates based on environmental exploration. The difference: AriGraph updates graph STRUCTURE (add/remove nodes and edges), while RWKG proposes updating edge WEIGHTS. AriGraph is the more radical approach — it restructures the topology itself.

---

*Nota: conteúdo baseado no abstract + metadados. Consultar PDF para arquitetura completa, TextWorld results, e ablation studies.*
