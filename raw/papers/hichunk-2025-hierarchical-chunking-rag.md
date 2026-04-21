# HiChunk: Evaluating and Enhancing Retrieval-Augmented Generation with Hierarchical Chunking

**Autores:** Wensheng Lu*, Keyu Chen*, Ruizhi Qiao, Xing Sun (* = igual contribuição)  
**Afiliação:** Tencent Youtu Lab  
**ArXiv ID:** 2509.11552  
**URL:** https://arxiv.org/abs/2509.11552  
**Código:** https://github.com/TencentYoutuResearch/HiChunk  
**Dados:** https://huggingface.co/datasets/Youtu-RAG/HiCBench  
**Publicado:** 15 de setembro de 2025

---

## Abstract

Retrieval-Augmented Generation (RAG) enhances the response capabilities of language models by integrating external knowledge sources. However, document chunking as an important part of RAG system often lacks effective evaluation tools. This paper first analyzes why existing RAG evaluation benchmarks are inadequate for assessing document chunking quality, specifically due to evidence sparsity. Based on this conclusion, the authors propose HiCBench, which includes manually annotated multi-level document chunking points, synthesized evidence-dense question answer (QA) pairs, and their corresponding evidence sources. Additionally, they introduce the HiChunk framework, a multi-level document structuring framework based on fine-tuned LLMs, combined with the Auto-Merge retrieval algorithm to improve retrieval quality. Experiments demonstrate that HiCBench effectively evaluates the impact of different chunking methods across the entire RAG pipeline. Moreover, HiChunk achieves better chunking quality within reasonable time consumption, thereby enhancing the overall performance of RAG systems.

---

## 1. Problema: Benchmarks Existentes são Inadequados para Avaliar Chunking

### Evidence Sparsity

O problema central: benchmarks RAG existentes (Qasper, HotpotQA, GutenQA, OHRBench) sofrem de **evidence sparsity** — apenas poucas sentenças do documento são relevantes para cada query. Nessa configuração, chunking methods diferentes produzem resultados quase idênticos porque qualquer método razoável recupera as poucas sentenças relevantes.

**Evidência (Tabela 1 — estatísticas dos datasets):**

| Dataset | Docs | Sent/doc | Words/doc | QAs | Words/evidence | Sent/evidence |
|---------|------|----------|-----------|-----|----------------|---------------|
| Qasper | 416 | 164 | 4.2k | 1,372 | 239.4 | 10.5 |
| OHRBench | 1,261 | 176 | 5.4k | 8,498 | 36.5 | 1.7 |
| GutenQA | 100 | 5,373 | 146.5k | 3,000 | 39.3 | 1.7 |

OHRBench e GutenQA têm evidence de apenas 1.7 sentenças em média — insuficiente para diferenciar qualidade de chunking.

### Limitação dos Métodos Existentes

Métodos de chunking existentes tratam documentos como estrutura linear (sequência plana de parágrafos/sentenças), sem capturar hierarquia multi-nível (seções, subseções, parágrafos). Isso dificulta a adaptação da granularidade de retrieval ao tipo de query — algumas queries requerem contexto de múltiplos parágrafos relacionados, outras apenas uma sentença.

---

## 2. HiCBench: Benchmark para Avaliação de Chunking

### Construção

HiCBench é construído sobre os documentos do corpus OHRBench, filtrando documentos com menos de 4.000 palavras e mais de 50 páginas. Os documentos retidos recebem **anotação manual de estrutura hierárquica** (chunking points em múltiplos níveis).

### Critérios para QA Pairs

Para que os pares QA avaliem efetivamente a qualidade do chunking:

1. **Evidence Completeness and Density:** Evidências devem ser completas e necessárias; a proporção de evidência no contexto deve ser significativa (filtro: razão evidência/contexto < 10% → descartado)
2. **Fact Consistency:** Respostas geradas com contexto completo devem ser consistentes com as respostas de referência (métrica: Fact-Cov > 80% em 5 repetições)

### Três Tipos de Tarefa

- **T₀ (Evidence-Sparse QA):** Evidência limitada a 1-2 sentenças (equivalente aos benchmarks existentes)
- **T₁ (Single-Chunk Evidence-Dense QA):** Evidência constitui parcela substancial de um chunk semântico completo; chunk size entre 512 e 4096 words
- **T₂ (Multi-Chunk Evidence-Dense QA):** Evidência distribuída por múltiplos chunks semânticos completos; chunk size entre 256 e 2048 words

### Processo de Construção QA

1. **Anotação e sumarização hierárquica:** Geração de summaries por seção via LLM (DeepSeek-R1-0528)
2. **Geração de pares:** Seleção de 1-2 chunks como contexto C, geração de (Q, A) condicionada em (S, C)
3. **Garantia de completude:** Extração de sentenças de evidência via LLM, repetida 5 vezes, retendo sentenças com ≥4 aparições
4. **Filtragem de consistência:** Cálculo do Fact-Cov metric repetido 5 vezes; descarte de amostras com média < 80%

**Estatísticas do HiCBench (Tabela 2):**

| Métrica | HiCBench T₁ | HiCBench T₂ |
|---------|------------|------------|
| Documentos | 130 | 130 |
| Sent/doc | 298 | 298 |
| Words/doc | 8.5k | 8.5k |
| QA pairs | 659 | 541 |
| Words/question | 31.0 | 33.0 |
| Words/answer | 130.1 | 126.4 |
| Words/evidence | 561.5 | 560.5 |
| Sent/evidence | 20.5 | 20.4 |

Evidence com 20.5 sentenças em média — contraste direto com os 1.7 sentenças dos benchmarks com evidence sparsity.

---

## 3. HiChunk: Framework de Chunking Hierárquico

### Visão Geral

HiChunk é um framework de estruturação hierárquica de documentos baseado em LLMs fine-tuned. O objetivo: compreender as relações hierárquicas dentro de um documento e organizá-lo em estrutura hierárquica com dois subtasks via text generation:

1. **Identificação de chunking points** (onde dividir)
2. **Determinação de hierarchy levels** (que nível hierárquico cada ponto pertence)

**Modelo base:** Qwen3-4B, learning rate 1e-5, batch size 64, max training length 8192 tokens, max inference length 16384 tokens. Comprimento de cada sentença limitado a 100 caracteres.

**Dados de treinamento:** Gov-report, Qasper, Wiki-727 (datasets com estrutura explícita de documento) + augmentação por shuffling aleatório de capítulos e deleção de conteúdo.

### Processo de Inferência

Dado documento D:
1. Sentence tokenization → S[1:N] (cada sentença recebe ID único)
2. HiChunk gera Global Chunk Points GCP₁:ₖ (pontos de chunking em k níveis hierárquicos)
3. Fixed-size chunking é aplicado sobre os resultados do HiChunk para produzir C[1:M]

### Iterative Inference para Documentos Longos

Para documentos que excedem o comprimento máximo de inferência L:
- Inicializa a = 0 (sentence ID inicial)
- Determina b = argmaxb̂(S[a:b̂] ≤ L) para garantir que o input não exceda L
- Obtém Local Chunk Points LCP₁:ₖ via HiChunk(S[a:b])
- Merge de LCP₁:ₖ em GCP₁:ₖ globais
- Atualiza a para a próxima iteração

**Problema de hierarchical drift:** Quando há apenas 1 chunk de nível 1 no resultado local, ocorre drift hierárquico. Solução: construção de "residual text lines" com estrutura conhecida do documento para guiar o modelo.

### Auto-Merge Retrieval Algorithm

Para balancear completude semântica e granularidade dos chunks recuperados, o algoritmo Auto-Merge percorre os chunks C[1:M] ordenados por relevância para a query:

Em cada passo i, o algoritmo considera fazer merge do chunk atual com seu nó pai na hierarquia. O merge ocorre quando três condições são satisfeitas:

- **Cond₁:** O nó pai p já tem ≥2 filhos em node_ret (chunks já recuperados)
- **Cond₂:** A soma do comprimento dos filhos de p em node_ret ≥ θ*, onde θ* é threshold adaptativo: θ*(tkₒᵤᵣ, p) = len(p)/3 × (1 + tkₒᵤᵣ/T). À medida que o orçamento de tokens aumenta, θ* aumenta de len(p)/3 para 2×len(p)/3 — chunks com ranking mais alto têm maior chance de merge
- **Cond₃:** O orçamento de tokens restante T - tkₒᵤᵣ ≥ len(p)

O resultado é um contexto que combina automaticamente chunks fine-grained quando formam uma unidade semântica maior.

---

## 4. Resultados Experimentais

### Métodos de Comparação

- **FC200:** Fixed chunking, size = 200 sentences merged
- **SC:** Semantic chunker com bge-large-en-v1.5
- **LC (LumberChunker):** LLM-based, usando Deepseek-r1-0528, temperatura 0.1
- **HC200:** HiChunk + fixed chunking (size 200) sem Auto-Merge
- **HC200+AM:** HC200 + Auto-Merge retrieval

Embedding para retrieval: bge-m3. LLMs de resposta: Llama3.1-8B, Qwen3-8B, Qwen3-32B. Orçamento máximo de contexto recuperado: 4096 tokens.

### 4.1 Chunking Accuracy (Tabela 3)

| Método | Qasper F1_L1 | Qasper F1_Lall | Gov-Report F1_L1 | Gov-Report F1_Lall | HiCBench F1_L1 | HiCBench F1_Lall |
|--------|-------------|---------------|-----------------|-------------------|---------------|-----------------|
| SC | 0.0759 | 0.1007 | 0.0298 | 0.0616 | 0.0487 | 0.1507 |
| LC | 0.5481 | 0.6657 | 0.1795 | 0.5631 | 0.2849 | 0.4858 |
| **HC** | **0.6742** | **0.9441** | **0.9505** | **0.9882** | **0.4841** | **0.5450** |

HC supera significativamente SC e LC em todos os datasets, especialmente em Gov-report (in-domain). Em HiCBench (out-of-domain), HC também mostra melhoria substancial.

### 4.2 RAG Pipeline Evaluation (Tabela 4 — seleção com Qwen3-32B)

| Método | LongBench Score | Qasper ERec | Qasper F1 | GutenQA ERec | GutenQA Rouge | OHRBench ERec | HiCBench T₁ ERec | HiCBench T₁ FC | HiCBench T₁ Rouge |
|--------|----------------|-------------|-----------|-------------|--------------|--------------|-----------------|---------------|------------------|
| FC200 | 46.33 | 84.32 | 46.49 | 67.07 | 46.89 | 74.06 | 74.06 | 63.20 | 35.70 |
| SC | 46.29 | 82.22 | 46.39 | 62.18 | 45.43 | 71.26 | 71.26 | 61.09 | 35.64 |
| LC | 47.43 | 87.43 | 46.82 | 68.79 | 47.92 | 75.53 | 75.53 | 64.76 | 36.15 |
| HC200 | 46.71 | 86.49 | 46.99 | 68.57 | 47.71 | 77.68 | 77.68 | 63.93 | 36.55 |
| **HC200+AM** | **46.92** | **87.85** | **47.25** | **68.31** | **47.89** | **81.03** | **81.03** | **68.12** | **37.29** |

**Achados principais:**

1. **GutenQA e OHRBench (T₀):** Evidence sparsity (1.7 sentenças) faz com que métodos diferentes mostrem variação mínima. Exemplo GutenQA: ERec de FC200 = 64.5 vs HC200+AM = 65.53; Rouge de FC200 = 44.86 vs HC200+AM = 44.94.

2. **Qasper e HiCBench (T₁, T₂):** Evidence densa revela diferenças significativas. Exemplo HiCBench T₁ com Qwen3-32B: ERec FC200 = 74.06 vs HC200+AM = 81.03 (+9.4%); Fact-Cov FC200 = 63.20 vs HC200+AM = 68.12 (+7.8%); Rouge FC200 = 35.70 vs HC200+AM = 37.29 (+4.5%).

3. **LumberChunker permanece baseline forte em LongBench** (LongBench Score: LC = 47.43 vs HC200+AM = 46.92), mas HC200+AM alcança performance ótima ou sub-ótima na maioria dos subsets.

### 4.3 Influência do Token Budget de Retrieval (Section 5.6)

Avaliação em HiCBench T₁ com budgets de 2k, 2.5k, 3k, 3.5k e 4k tokens. HC200+AM mantém desempenho superior consistentemente em todos os budgets.

### 4.4 Efeito do Nível Hierárquico Máximo (Section 5.7)

Máximo hierárquico variando de L1 a L4 (LA = sem limite):

- **L1:** Auto-Merge degrada RAG por granularidade grosseira demais
- **L1 → L3:** Evidence recall melhora progressivamente
- **L3 → L4+:** Mudança mínima

Conclusão: estrutura hierárquica com ≥3 níveis é suficiente e necessária.

### 4.5 Custo Temporal (Tabela 5)

| Dataset | Avg. Words | SC Time(s/doc) | LC Time(s/doc) | HC Time(s/doc) |
|---------|-----------|----------------|----------------|----------------|
| Qasper | 4,166 | 0.49 | 5.50 | 1.50 |
| Gov-report | 13,153 | 1.32 | 15.43 | 4.34 |
| OHRBench | 26,808 | 3.09 | 37.39 | 14.58 |
| GutenQA | 146,507 | 16.50 | 132.49 | 60.19 |
| HiCBench | 8,519 | 1.02 | 13.44 | 5.75 |

SC é mais rápido, mas consistentemente inferior em qualidade. LC tem boa performance, mas velocidade muito inferior (3.7x mais lento que HC no Qasper, 2.2x no Gov-report). HC atinge melhor qualidade de chunking entre todos os baselines com custo de tempo aceitável — adequado para uso em RAG systems reais.

---

## 5. Relacionado: Late Chunking

O paper cita diretamente Late Chunking (Günther et al., 2024): "embeds entire documents before chunking to preserve global context, but produces flat chunk lists without modeling hierarchical relationships." HiChunk cria representações multi-nível (seções → subseções → parágrafos), permitindo que sistemas RAG recuperem informação no nível de abstração apropriado para cada query.

---

## 6. Conclusão

O paper demonstra dois contribuições interligadas:

1. **HiCBench** resolve o problema de evidence sparsity nos benchmarks existentes, com pares QA onde evidência abrange 20+ sentenças distribuídas em chunks semanticamente coesos — necessário para diferenciar qualidade de chunking methods

2. **HiChunk + Auto-Merge** supera baselines (SC, LC, FC) em qualidade de chunking (F1_Lall de 0.94 vs 0.67 do LC no Qasper) e em métricas end-to-end de RAG em datasets com evidence densa, com custo de tempo aceitável para produção

A evidência central: benchmarks com evidence sparsity fazem todos os métodos parecer equivalentes; o problema de chunking só é revelado com datasets como Qasper e HiCBench onde a evidência está semanticamente distribuída por múltiplos chunks contíguos.
