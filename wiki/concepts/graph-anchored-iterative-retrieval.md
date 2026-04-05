---
title: "Graph-Anchored Iterative Retrieval (GraphAnchor)"
sources:
  - path: raw/papers/liu-2026-graphanchor-knowledge-indexing.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-05
updated: 2026-04-05
tags: [retrieval, graph, iterative, multi-hop, rag, single-brain]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-05
quarantine: false
---

## Resumo

Liu et al. (2026): GraphAnchor constrói grafo ephemeral durante iterative retrieval para guiar subqueries e modular atenção. +14-23% F1 em benchmarks multi-hop vs. vanilla RAG. Grafo é descartado após cada query — não é índice persistente. Distinção crítica: resolve "como recuperar melhor durante uma query", não "como manter índice quando documentos mudam." Esses são problemas diferentes.

## Conteúdo

### O que GraphAnchor faz

Loop iterativo por query (máx k=4 passos):

```
query q₀
  → retriever: top 5 docs D₁
  → LLM extrai RDF triples de D₁ → grafo G₁
  → LLM raciocina sobre G₁ + D₁ → sufficient?
  → se não: formula subquery q₁ baseada em G₁
  → retriever: top 5 docs D₂
  → LLM atualiza G₁ com D₂ → grafo G₂
  → ... repete até sufficient ou k=4
  → answer gerado de todos D₁..Dₖ + grafo final Gₖ
```

**Graph evolution por passo:**
```
ΔG_{t-1→t} = Index(D_t, {raciocínio_anterior, query_anterior})
```
Extração context-aware: entidades relevantes para o raciocínio em curso, não todas as entidades dos documentos.

**Grafo linearizado como prompt:**
```
<graph>
X(entidade_1), X(entidade_2)
X(sujeito, relação, objeto)...
</graph>
```

### Distinção de GraphRAG / HippoRAG

| Dimensão | HippoRAG/GraphRAG | GraphAnchor |
|----------|-------------------|-------------|
| Quando constrói | Offline (pré-indexação) | Online (por query) |
| Persistência | Permanente — sobrevive entre queries | Ephemeral — descartado após query |
| Propósito principal | Retrieval via PageRank/spreading activation | Guia atenção + geração de subqueries |
| Resolve "documentos mudam"? | Sim (HippoRAG: incremental edge addition) | Não |

### Resultados (Qwen2.5-7B-Instruct, 4 benchmarks multi-hop)

| Dataset | Vanilla RAG F1 | GraphAnchor F1 | Delta |
|---------|---------------|---------------|-------|
| MuSiQue | 18.05 | 32.60 | **+14.55** |
| HotpotQA | 50.93 | 66.03 | **+15.10** |
| 2WikiMQA | 38.54 | 61.64 | **+23.10** |
| Bamboogle | 21.62 | 34.25 | **+12.63** |

Consistente em Llama3.1-8B, Qwen2.5-14B, Qwen3-32B.

**Ablação — o que importa:**

| Variante | MuSiQue | HotpotQA | 2WikiMQA |
|---------|---------|----------|---------|
| Sem iteração | 16.89 | 53.25 | 40.72 |
| Sem grafo | 22.99 | 55.05 | 50.64 |
| Full | **32.60** | **66.03** | **61.64** |

Iteração é mais importante que o grafo. Remover iteração: -10% F1. Remover grafo: -6%.

### O que o paper não resolve

- Sem mecanismo de remoção de nós — grafo acumula monotonicamente durante a query
- Sem resolução explícita de triplas contraditórias entre documentos
- Sem persistência: não endereça o problema de manter índice quando documentos são atualizados

## Interpretação

### Relevância para Single Brain (⚠️ nossa síntese)

**O que desbloqueia — /ask iterativo:**

O padrão do GraphAnchor mapeia diretamente para uma melhoria do /ask no llm-kb. Atualmente /ask é linear (Layer 1 → Layer 2 → Layer 3). GraphAnchor sugere iteração:

```
/ask atual (linear):
  _index.md → artigos candidatos → raw/ verificação → resposta

/ask GraphAnchor-style (iterativo):
  _index.md → candidatos iniciais
  → constrói grafo de entidades relevantes
  → avalia suficiência: "tenho evidência suficiente?"
  → se não: formula subquery, busca mais artigos
  → responde com grafo como contexto de atenção
```

Ganho esperado: queries multi-hop no KB (ex: "como autoresearch-reliability-triad se relaciona com procurement-variety-gap via requisite-variety?") — exatamente o caso de uso do /ask cross-cluster.

**O que NÃO desbloqueia — Bloqueio 2 do single-brain-phase1-design:**

Bloqueio 2 era: "quando um artigo wiki é atualizado, como o LanceDB atualiza?" GraphAnchor não responde isso — seu grafo é ephemeral e per-query.

A solução para Bloqueio 2 é mais simples do que precisava de um paper: ID estável por fragmento (sha256 do source_path) + delete-by-id + reinsert. LanceDB suporta isso nativamente. Não era um problema de pesquisa — era uma decisão de implementação.

### Limitação de generalização

Resultados medidos em multi-hop QA benchmarks (MuSiQue, HotpotQA, 2WikiMQA, Bamboogle) com documentos curtos e factuais. KB do llm-kb tem artigos mais longos, com interpretações marcadas e estrutura epistêmica. Ganho pode ser diferente — possivelmente maior em queries cross-cluster, possivelmente menor em queries single-article.

## Verificação adversarial

**Claim mais fraco:** "+14-23% F1" — medido com Qwen2.5-7B em benchmarks específicos de multi-hop. Não testado em KBs com conteúdo epistemicamente heterogêneo (fatos + interpretações + especulações). O ganho pode não replicar diretamente no /ask do llm-kb.

**O que o paper NÃO diz:**
1. Não testa em documentos com claims conflitantes ou marcados com confiança
2. Não mede latência por query — 1207s/100 queries = ~12s/query (relevante para uso interativo)
3. Não testa com documentos em português

**Prior work que o paper constrói:**
- IRCoT, Iter-RetGen: iterative retrieval sem grafo — GraphAnchor supera em ~10%
- HippoRAG, GraphRAG: grafos estáticos — GraphAnchor complementa (estático para retrieval, dinâmico para geração)

## Conexões

- complements: [[agent-memory-architectures]] — GraphAnchor é retrieval-time graph (ephemeral); HippoRAG/Synapse são index-time graphs (persistent); usos complementares
- validates: [[hybrid-search]] — iterative retrieval + grafo supera BM25+vector sozinho em multi-hop; QMD pode ser o retriever no loop
- derivedFrom: [[retrieval-augmented-generation]] — instância de iterative RAG com estrutura intermediária
- contradicts: [[single-brain-phase1-design]] ON "GraphAnchor resolve Bloqueio 2" — Bloqueio 2 (index maintenance) não é problema de GraphAnchor; solução é delete-by-id nativo do LanceDB

## Fontes

- [Liu et al. 2026](../../raw/papers/liu-2026-graphanchor-knowledge-indexing.md) — arquitetura GraphAnchor, loop iterativo, +14-23% F1 multi-hop, ablação iteração vs. grafo

## Quality Gate
- [x] Wikilinks tipados: 4 (complements, validates, derivedFrom, contradicts)
- [x] Instance→class: "+14-23% F1" qualificado como "Qwen2.5-7B, benchmarks multi-hop específicos"
- [x] Meta-KB separado: /ask improvement e Bloqueio 2 em Interpretação
- [x] Resumo calibrado: "grafo ephemeral — não é índice persistente" explícito
