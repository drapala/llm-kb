---
title: "Hierarchical Chunking para RAG (HiChunk)"
sources:
  - path: raw/papers/hichunk-2025-hierarchical-chunking-rag.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/chen-2025-discourse-aware-hierarchical-retrieval.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-13
updated: 2026-04-13
tags: [chunking, rag, hierarquia, retrieval, benchmark]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - wiki/concepts/retrieval-augmented-generation.md
  - wiki/concepts/late-chunking-contextual-embeddings.md
---

## Resumo

Chunking hierárquico (seções → subseções → parágrafos) melhora retrieval em documentos com evidence densa vs evidência esparsa. HiChunk (Tencent Youtu, 2025) fine-tuna LLM para identificar pontos de divisão em múltiplos níveis + algoritmo Auto-Merge que recupera chunks de granularidade adaptativa. DISRetrieval (Harbin IT, 2025) usa RST (Rhetorical Structure Theory) para construir hierarquia discourse-aware. Ambos superam baselines em benchmarks com evidence densa (+7-9% ERec); LumberChunker permanece competitivo em LongBench geral.

## Conteúdo

### Problema: Evidence Sparsity nos Benchmarks

Benchmarks RAG existentes (GutenQA, OHRBench) têm evidência de apenas 1.7 sentenças por query. Nessa condição, todos os métodos de chunking parecem equivalentes — qualquer abordagem razoável recupera as poucas sentenças relevantes.

HiCBench resolve: evidence com 20+ sentenças por query, distribuída em múltiplos chunks semanticamente coesos. Esse setting revela diferenças reais entre métodos.

### HiChunk (Tencent Youtu Lab, 2025)

**Arquitetura:** Qwen3-4B fine-tunado em Gov-report + Qasper + Wiki-727 para dois subtasks:
1. Identificar pontos de divisão em documento
2. Determinar nível hierárquico de cada ponto (L1-L4)

**Auto-Merge Algorithm:** ao recuperar chunks, verifica se chunks adjacentes de mesmo nó-pai formam unidade semântica completa. Merge ocorre quando ≥2 filhos do mesmo pai já foram recuperados e a soma excede limiar adaptativo.

**Resultado-chave (HiCBench T₁, Qwen3-32B):**

| Método | ERec | Fact-Cov | Rouge |
|--------|------|---------|-------|
| Fixed-size 200 | 74.06% | 63.20% | 35.70% |
| Semantic | 71.26% | 61.09% | 35.64% |
| LumberChunker | 75.53% | 64.76% | 36.15% |
| **HiChunk+AutoMerge** | **81.03%** | **68.12%** | **37.29%** |

Em evidence sparsity (GutenQA): diferenças mínimas (ERec 67.07% vs 68.31%) — confirma que evidence sparsity mascara qualidade de chunking.

**Custo temporal:** HC é 3× mais lento que SC mas 2.2-10× mais rápido que LumberChunker. Aceitável para produção.

**Hierarquia necessária:** L1-L3 são suficientes e necessários; L4+ sem mudança significativa.

### DISRetrieval — Discourse-Aware Hierarchical Retrieval

**Arquitetura:** árvore RST (Rhetorical Structure Theory) convertida em embeddings densas. Dois níveis: árvore por parágrafo + árvore de documento.

**RST adapatado:** opera em nível de sentença (não EDU) para eficiência. Parser multilíngue (RST-DT + dados Chinese traduzidos por GPT-4o).

**Estratégia de recuperação dual:**
- Seleção direta de folhas para sentenças de alta relevância
- Expansão hierárquica top-k para nós internos
- Preserva ordem original do documento (não ordem de ranking)

**Resultados (GPT-4.1-mini, contexto 400w):**

| Método | QASPER F1 | QuALITY Acc |
|--------|-----------|-------------|
| flatten-chunk | 44.78% | 71.05% |
| RAPTOR | 43.85% | 70.71% |
| Bisection | 45.69% | 72.00% |
| **DISRetrieval** | **46.31%** | **73.54%** |

DISRetrieval é 3× mais rápido que RAPTOR (103s vs 338s para 50K palavras). Modelos 7B suficientes para o nó de aprimoramento.

**Achado crítico:** Bisection (hierarquia sem RST) supera flat — estrutura hierárquica ajuda independente da linguística. Mas DISRetrieval (hierarquia com RST) supera Bisection — estrutura de discurso adiciona valor além da hierarquia geométrica.

### Comparação Direta entre Abordagens Hierárquicas

| Dimensão | HiChunk | DISRetrieval | RAPTOR |
|----------|---------|-------------|--------|
| Base da hierarquia | LLM fine-tuned (chunking points) | RST discourse parser | GMM clustering semântico |
| Velocidade | Médio | 3× mais rápido que RAPTOR | Mais lento |
| Linguística | Não | Sim (RST) | Não |
| Cross-lingual | Não testado | Sim (PT não testado) | Não |
| Requer fine-tuning | Sim (Qwen3-4B) | Não (parser separado) | Não |

## Interpretação

(⚠️ nossa interpretação) Para o Zelox: hierarquia de 3 níveis (DO → ato → entidade) é analoga à hierarquia L1-L3 do HiChunk. Auto-Merge equivale à lógica de recuperar o ato completo quando múltiplos chunks do mesmo ato são relevantes.

(⚠️ nossa interpretação) DISRetrieval é mais relevante para atos longos com estrutura retórica (despachos motivados, pareceres jurídicos). Para atos curtos e estruturados (extratos de contrato), HiChunk ou fixed-size são suficientes.

(⚠️ nossa interpretação) Verificação adversarial: ambos os papers testam em inglês/chinês — a aplicação a português administrativo requer validação separada. RST para PT-BR não tem corpus de referência equivalente ao RST-DT inglês.

(⚠️ nossa interpretação) O benchmark HiCBench de evidence-density é metodologia transferível para validar o pipeline Zelox: construir mini-benchmark de atos com evidence distribuída em múltiplos chunks para comparar abordagens de segmentação.

## Conexões

- validates: [[retrieval-augmented-generation]] — hierarquia multi-nível supera flat para documentos com evidence densa
- complementa: [[late-chunking-contextual-embeddings]] — late chunking + hierarquia são ortogonais; combinação possível
- contradicts: [[raptor-vs-flat-retrieval]] — DISRetrieval supera RAPTOR em QASPER com menor custo computacional
- contradicts: [[semantic-chunking-cost-benefit]] — hierarquia resolve o problema que semantic chunking simples não resolve

## Fontes

- [HiChunk 2025 (Tencent Youtu)](../../raw/papers/hichunk-2025-hierarchical-chunking-rag.md) — HiCBench benchmark, Auto-Merge algorithm, +9.4% ERec vs fixed-size em evidence-dense
- [DISRetrieval 2025 (Harbin IT)](../../raw/papers/chen-2025-discourse-aware-hierarchical-retrieval.md) — RST-based hierarchy, 3× mais rápido que RAPTOR, cross-lingual, 7B models suficientes
