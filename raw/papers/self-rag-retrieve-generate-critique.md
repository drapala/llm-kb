---
source: https://arxiv.org/abs/2310.11511
authors: Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi
date: 2023-10-17
type: paper
arxiv: "2310.11511"
---

# Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

## Abstract

Framework where models adaptively retrieve passages on-demand and generate/reflect on retrieved passages using special critique tokens. Enables controllable behavior during inference to match varying task demands.

## Core Innovation

Self-RAG adds reflection tokens to the generation process:
- **[Retrieve]**: should I retrieve? (yes/no/continue)
- **[IsRel]**: is the retrieved passage relevant? (relevant/irrelevant)
- **[IsSup]**: is the response supported by the passage? (fully/partially/no)
- **[IsUse]**: is the response useful? (1-5 scale)

The model learns WHEN to retrieve (not always), WHAT is relevant (not all retrieved content), and WHETHER its response is supported (not blindly trusting itself).

## Key Insight

Self-RAG is Reflexion applied to retrieval. Instead of reflecting on task failures verbally, it reflects on retrieval quality via structured tokens. This creates a fast, in-line feedback loop — not post-hoc like Reflexion's retry cycle.

## Relevance to KB

Our /ask does Layer 3 verification (check wiki claims against raw/) but without structured self-critique. Self-RAG suggests adding explicit reflection checkpoints:
- After Layer 1: "are these the right articles?" (equivalent to [IsRel])
- After Layer 2: "is my synthesis supported by what I read?" (equivalent to [IsSup])
- After Layer 3: "did raw/ verification change my answer?" (equivalent to structured reflection)

This would formalize the circuit breaker we added to /ask and make the self-critique traceable.

---

*Nota: conteúdo baseado no abstract. Consultar PDF para token design, training procedure, e benchmark comparisons.*
