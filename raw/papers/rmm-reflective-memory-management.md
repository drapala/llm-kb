---
source: https://aclanthology.org/2025.acl-long.413/
authors: Zhen Tan, Jun Yan, I-Hung Hsu, Rujun Han, Zifeng Wang, Long Le, Yiwen Song, Yanfei Chen, Hamid Palangi, George Lee, Anand Rajan Iyer, Tianlong Chen, Huan Liu, Chen-Yu Lee, Tomas Pfister
date: 2025-07-01
type: paper
venue: ACL 2025
stance: challenging
---

# RMM: In Prospect and Retrospect — Reflective Memory Management for Long-term Personalized Dialogue Agents

## Abstract

LLMs struggle to retain and retrieve relevant information from long-term interactions. RMM combines prospective reflection (dynamically summarizes interactions across granularities into memory bank) with retrospective reflection (iteratively refines retrieval via online RL based on LLM's cited evidence). +10% accuracy over baseline without memory management on LongMemEval.

## Key Innovation: Retrospective Reflection via Online RL

This is the closest existing work to RWKG's "Reflexion-weighted retrieval" proposal:
- **Prospective reflection** = our /ingest (summarize interactions into structured memory)
- **Retrospective reflection** = Reflexion applied to retrieval, refined via online RL

The critical difference: RMM uses REINFORCEMENT LEARNING to adapt retrieval, not edge weight modification on a graph. RL provides a formal optimization framework with reward signals; RWKG's proposed "modify edge weights based on verbal reflection" is ad-hoc by comparison.

## Direct Challenge to RWKG

RMM demonstrates that the "retrieval adaptation from failure feedback" concept exists and works — but via RL, not via graph topology modification. This is prior work that partially covers RWKG's proposed mechanism, using a more principled approach (RL with reward signals vs. verbal reflection → weight change).

+10% accuracy suggests the mechanism works. The question becomes: does graph topology modification offer advantages over RL-based retrieval refinement? RWKG doesn't answer this.

---

*Nota: conteúdo baseado no abstract + metadados. Consultar PDF (ACL 2025) para arquitetura completa, RL formulation, e ablation studies.*
