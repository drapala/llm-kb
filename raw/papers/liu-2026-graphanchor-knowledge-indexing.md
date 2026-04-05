# GraphAnchor: Graph-Anchored Knowledge Indexing for Retrieval-Augmented Generation

**Authors:** Zhenghao Liu, Mingyan Wu, Xinze Li, Yukun Yan, Shuo Wang, Cheng Yang, Minghe Yu, Zheni Zeng, Maosong Sun
**arXiv:** 2601.16462
**January 2026**
**Code:** https://github.com/NEUIR/GraphAnchor

---

## Abstract

GraphAnchor transforma grafos de estruturas estáticas em índices de conhecimento ativos e evolutivos *durante iterative retrieval*. Mantém grafo G=(V,E) que cresce a cada passo de retrieval, ancorando entidades e relações salientes extraídas dos documentos recuperados. O grafo guia geração de subqueries e modula atenção do LLM na geração final.

**Distinção crítica:** o grafo é ephemeral (criado e descartado por query). Não é um índice persistente que sobrevive entre queries — é uma estrutura temporária que melhora retrieval multi-hop dentro de uma única sessão de resposta.

---

## Arquitetura — Loop iterativo

Em cada passo t:

1. **Retrieval:** `D_t = Retriever(q_{t-1})` — top 5 documentos via bge-large-en-v1.5
2. **Graph Update:** `G_t = M(q_0, D_t, o_{t-1})` — LLM extrai RDF triples dos docs condicionado ao raciocínio anterior
3. **Sufficiency Judgment:** LLM produz reasoning trace `<think>` + julgamento `<judgement>: sufficient | insufficient`
4. **Query Generation:** se insufficient, formula próxima subquery q_t baseada no grafo atual
5. **Repeat até k=4 passos ou sufficient**
6. **Final Answer:** gerado a partir de todos os documentos recuperados + grafo final G_k

**Graph Evolution:**
```
ΔG_{t-1→t} = Index(D_t, {R_{t-1}, q_{t-1}})
```
Extração condicionada a traces de raciocínio e queries anteriores — context-aware, não apenas entidades dos novos docs.

**Linearização do grafo:**
```
<graph>
X(entidade_1), X(entidade_2), ...
X(sujeito, relação, objeto), ...
</graph>
```

---

## Diferença de GraphRAG / HippoRAG

| Aspecto | HippoRAG / GraphRAG | GraphAnchor |
|---------|--------------------|-|
| Quando o grafo é construído | Offline (pré-indexação) | Online (durante query) |
| Persistência | Permanente | Ephemeral (per query) |
| Propósito | Index de retrieval | Guia de atenção + subquery |
| Atualização | Rebuild ou incremental | Descartado após query |

---

## Resultados (Qwen2.5-7B-Instruct)

| Dataset | Vanilla RAG F1 | GraphAnchor F1 | Delta |
|---------|---------------|---------------|-------|
| MuSiQue | 18.05 | 32.60 | +14.55 |
| HotpotQA | 50.93 | 66.03 | +15.10 |
| 2WikiMQA | 38.54 | 61.64 | +23.10 |
| Bamboogle | 21.62 | 34.25 | +12.63 |

Consistente em Llama3.1-8B, Qwen2.5-14B, Qwen3-32B.

## Ablação

| Variante | MuSiQue F1 | 2WikiMQA F1 |
|---------|-----------|------------|
| Sem grafo | 22.99 | 50.64 |
| Sem iteração | 16.89 | 40.72 |
| Full GraphAnchor | 32.60 | 61.64 |

Iteração contribui mais que grafo isoladamente. Remover iteração: -10% F1. Remover grafo: -6%.

---

## Mecanismo de atenção

- Grafo recebe maioria dos attention weights durante geração final
- Entropia de atenção aumenta com iterações mais profundas (foco mais seletivo)
- Atenção a entidades ancoradas aumenta progressivamente; perplexidade da resposta diminui

---

## O que o paper NÃO documenta

- Mecanismo explícito de remoção de nós/arestas — grafo acumula monotonicamente
- Resolução de conflitos entre triplas contraditórias de diferentes documentos
- Comportamento com documentos que se atualizam entre queries (índice persistente)
