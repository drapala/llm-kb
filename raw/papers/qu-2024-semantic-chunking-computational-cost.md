# Is Semantic Chunking Worth the Computational Cost?

**Autores:** Renyi Qu, Forrest Bao, Ruixuan Tu  
**Instituições:** Vectara, Inc.; University of Wisconsin–Madison  
**arXiv:** 2410.13070  
**URL:** https://arxiv.org/abs/2410.13070  
**Data:** 2024  

---

## Abstract

Avanços recentes em sistemas RAG popularizaram o **semantic chunking**, que visa melhorar o desempenho de recuperação dividindo documentos em segmentos semanticamente coerentes. Apesar de sua crescente adoção, os benefícios reais sobre o **fixed-size chunking** (divisão em segmentos consecutivos de tamanho fixo) permanecem obscuros. Este estudo avalia sistematicamente a eficácia do semantic chunking usando três tarefas relacionadas a recuperação: recuperação de documentos, recuperação de evidências e geração de respostas baseada em recuperação. Os resultados mostram que os custos computacionais associados ao semantic chunking **não são justificados por ganhos de desempenho consistentes**. Esses achados desafiam suposições anteriores sobre semantic chunking e destacam a necessidade de estratégias de chunking mais eficientes em sistemas RAG.

---

## 1. Introdução

Em sistemas RAG, como documentos são divididos em "chunks" tem efeito crucial tanto em recuperação quanto em geração. A abordagem tradicional — **fixed-size chunking** — corta documentos em chunks de comprimento fixo (ex: 200 tokens). Embora computacionalmente simples, essa abordagem pode fragmentar conteúdo semanticamente relacionado.

Recentemente houve surto de interesse em **semantic chunking**, onde documentos são segmentados com base em similaridade semântica, com algumas aplicações industriais sugerindo melhorias prometedoras de desempenho (LangChain, LlamaIndex). Porém, **não existe evidência sistemática** de que semantic chunking produza ganho de desempenho em tarefas downstream suficiente para justificar o overhead computacional em relação ao fixed-size chunking.

**Contributions principais:**
- Framework de avaliação em larga escala comparando semantic e fixed-size chunking em tarefas diversas
- Demonstração de que semantic chunking apresenta benefícios inconsistentes que frequentemente não justificam o custo computacional

---

## 2. Estratégias de Chunking Avaliadas

Três estratégias foram avaliadas (todos os documentos primeiro divididos em sentenças via SpaCy):

### Fixed-size Chunker (baseline)
Divide documento sequencialmente em chunks de tamanho fixo com base em número predefinido de sentenças. Para manter alguma continuidade contextual, usa sentenças sobrepostas entre chunks consecutivos.

### Breakpoint-based Semantic Chunker
Percorre a sequência de sentenças e decide onde inserir um breakpoint. Um breakpoint é inserido se a distância semântica entre duas sentenças consecutivas excede um limiar, indicando mudança significativa de tópico. Testados quatro limiares relativos (conforme proposta LangChain) e dois limiares absolutos.

**Limitação:** toma decisões usando apenas duas sentenças de cada vez — estratégia pode ser localmente gananciosa.

### Clustering-based Semantic Chunker
Usa algoritmos de clustering para agrupar sentenças semanticamente, capturando relações globais e permitindo agrupamentos não-sequenciais. Para mitigar perda de informação contextual por proximidade, define nova medida de distância combinando distâncias posicional e semântica:

```
d(x_a, x_b) = λ · d_pos(x_a, x_b) + (1-λ) · d_cos(x_a, x_b)
```

Onde:
- `d_pos(x_a, x_b) = |a-b| / n` (diferença de índice normalizada)
- `d_cos` = 1 − max(cos(emb(x_a), emb(x_b)), 0)
- λ = parâmetro de peso entre posicional e semântico

Algoritmos testados: single-linkage agglomerative clustering e DBSCAN.

---

## 3. Design Experimental

Três tarefas proxy para avaliação indireta de qualidade de chunking (sem ground-truth em nível de chunk):

### 3.1 Recuperação de Documentos
- Avalia eficácia dos chunkers em recuperar documentos relevantes para uma query
- 10 datasets (maioria do benchmark BEIR), incluindo 6 com documentos curtos que foram artificialmente concatenados para criar documentos mais longos
- 100 queries amostradas aleatoriamente de cada dataset; top-k chunks recuperados (k ∈ {1,3,5,10})
- Cada chunk recuperado mapeado ao documento-fonte; avaliado contra conjunto de documentos relevantes

### 3.2 Recuperação de Evidências
- Avaliação em granularidade mais fina: localização de sentenças de evidência ground-truth
- Datasets do RAGBench (Friel et al., 2024)
- Mede número de sentenças de evidência ground-truth presentes nos top-k chunks recuperados

### 3.3 Geração de Respostas
- Mede como chunkers impactam qualidade de respostas geradas por LLM
- Modelo generativo: gpt-4o-mini
- Top-5 chunks recuperados como input para o LLM
- Respostas avaliadas via similaridade semântica (BERTScore) contra respostas ground-truth

**Métrica:** F1@5 — medida balanceada que considera tanto precisão quanto recall  
**Embedder utilizado:** `dunzhang/stella_en_1.5B_v5` (melhor entre os testados no MTEB Leaderboard)

---

## 4. Resultados

### 4.1 Recuperação de Documentos

**Tabela: F1@5 para Recuperação de Documentos (%)**

| Dataset | Fixed-size | Breakpoint | Clustering |
|---------|-----------|------------|------------|
| Miracl* | 69.45 | **81.89** | 67.35 |
| NQ* | 43.79 | **63.93** | 41.01 |
| Scidocs* | 16.82 | 17.60 | **19.87** |
| Scifact* | 35.27 | **36.27** | 35.70 |
| BioASQ* | 61.86 | 61.87 | **62.49** |
| NFCorpus* | **21.36** | 21.07 | 22.12 |
| HotpotQA | **90.59** | 87.37 | 84.79 |
| MSMARCO | **93.58** | 92.23 | 93.18 |
| ConditionalQA | **68.11** | 64.44 | 65.94 |
| Qasper | **90.99** | 89.27 | 90.77 |

*Datasets marcados com * são "stitched" (concatenados artificialmente)

**Interpretação:** Semantic chunkers (especialmente Breakpoint) superam Fixed-size em datasets stitched com alta diversidade de tópicos. Em datasets originais (documentos longos naturais), Fixed-size chunker frequentemente supera ou iguala chunkers semânticos. Conforme o comprimento do documento aumenta, a vantagem dos semantic chunkers diminui.

**Achado crítico:** Documentos stitched têm diversidade artificialmente alta de tópicos devido à concatenação aleatória. Na vida real, os tópicos em um documento podem não ser tão diversificados, então semantic chunkers podem não ter vantagem sobre fixed-size.

### 4.2 Recuperação de Evidências

**Tabela: F1@5 para Recuperação de Evidências (%)**

| Dataset | Fixed-size | Breakpoint | Clustering |
|---------|-----------|------------|------------|
| ExpertQA | **47.11** | 47.08 | 46.87 |
| DelucionQA | 43.05 | 43.24 | **43.36** |
| TechQA | **28.98** | 28.49 | 27.96 |
| ConditionalQA | 18.23 | **19.83** | 19.14 |
| Qasper | **8.66** | 8.16 | 8.50 |

Fixed-size chunker teve melhor desempenho em 3 de 5 datasets. Diferenças entre estratégias são **mínimas** — nenhuma vantagem clara para qualquer abordagem.

Inspeção detalhada revelou que apesar das variações em métodos de chunking, os top-k chunks recuperados frequentemente continham as mesmas sentenças de evidência, explicando as diferenças mínimas de desempenho.

### 4.3 Geração de Respostas

**Tabela: BERTScore para Geração de Respostas**

| Dataset | Fixed-size | Breakpoint | Clustering |
|---------|-----------|------------|------------|
| ExpertQA | 0.65 | 0.65 | 0.65 |
| DelucionQA | 0.76 | 0.76 | 0.76 |
| TechQA | 0.68 | 0.68 | 0.68 |
| ConditionalQA | 0.42 | **0.43** | **0.43** |
| Qasper | 0.49 | 0.49 | **0.50** |

Semantic chunkers performaram ligeiramente melhor com base no BERTScore, mas as diferenças são **mínimas**, tornando difícil tirar conclusões definitivas.

---

## 5. Discussão

### Por que semantic chunking não supera claramente fixed-size?

O desempenho dos chunkers é amplamente determinado pela eficácia dos modelos de embedding em capturar a riqueza semântica de sentenças individuais, em vez da estratégia de chunking em si.

- Quando embeddings são fortes, diferenças entre estratégias de chunking tornam-se menos relevantes
- Fixed-size chunking com overlap captura alguma continuidade contextual sem overhead semântico adicional

### Quando semantic chunking pode ajudar

Documentos com **alta diversidade de tópicos** (como documentos multi-tópico stitched), Breakpoint-based chunking pode oferecer vantagem ao preservar integridade de tópico. Nesses casos, a estratégia semântica produz chunks que se assemelham mais aos documentos originais, reduzindo ruído de recuperação.

---

## 6. Conclusão

Semantic e fixed-size chunking foram avaliados em sistemas RAG em recuperação de documentos, recuperação de evidências e geração de respostas. Semantic chunking ocasionalmente melhorou desempenho, particularmente em datasets stitched com alta diversidade de tópicos. Porém, esses benefícios foram:

1. **Altamente dependentes de contexto**
2. **Não consistentemente justificados** pelo custo computacional adicional
3. Frequentemente **ofuscados pela qualidade dos embeddings**

Em datasets não-sintéticos (melhor representação do mundo real), fixed-size chunking frequentemente performou melhor. **Fixed-size chunking permanece escolha mais eficiente e confiável para aplicações práticas de RAG**, especialmente quando recursos computacionais são limitados ou ao trabalhar com estruturas de documentos padrão.

---

## 7. Limitações

**Chunking em nível de sentença:** O estudo foca em chunking em nível de sentença, onde cada sentença é tratada como segmento para agrupamento. Essa abordagem resulta em embeddings de sentença que carecem de informação contextual.

**Ausência de métricas de qualidade de chunk:** Enquanto os chunks de output diferiram entre métodos, desempenhos de recuperação e geração foram similares entre chunkers. Scores de relevância query-chunk no nível de ground-truth forneceriam avaliações mais precisas.

**Falta de datasets adequados:** Um dataset ideal incluiria documentos longos representativos de casos de uso reais, tipos de query diversos, respostas geradas por humanos, scores de relevância query-documento e sentenças de evidência rotuladas por humanos. Os documentos sintéticos do estudo tinham diversidade artificialmente alta de tópicos por concatenação aleatória.

---

## Datasets Utilizados

**Recuperação de Documentos:**
- MIRACL, NQ, Scidocs, Scifact, BioASQ, NFCorpus (todos stitched)
- HotpotQA, MSMARCO, ConditionalQA, Qasper (originais)

**Recuperação de Evidências e Geração:**
- ExpertQA, DelucionQA, TechQA, ConditionalQA, Qasper (do RAGBench)
