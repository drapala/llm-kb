# Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models

**Autores:** Michael Günther, Isabelle Mohr, Daniel James Williams, Bo Wang, Han Xiao  
**Afiliações:** Jina AI GmbH (Berlin); Weaviate B.V. (Amsterdam)  
**ArXiv ID:** 2409.04701  
**URL:** https://arxiv.org/abs/2409.04701  
**Código:** https://github.com/jina-ai/late-chunking  
**Publicado:** Setembro 2024

---

## Abstract

Many use cases require retrieving smaller portions of text, and dense vector-based retrieval systems often perform better with shorter text segments, as the semantics are less likely to be "over-compressed" in the embeddings. Consequently, practitioners often split text documents into smaller chunks and encode them separately. However, chunk embeddings created in this way can lose contextual information from surrounding chunks, resulting in sub-optimal representations.

This paper introduces a novel method called "late chunking", which leverages long context embedding models to first embed all tokens of the long text, with chunking applied **after** the transformer model and just before mean pooling — hence the term "late" in its naming. The resulting chunk embeddings capture the full contextual information, leading to superior results across various retrieval tasks. The method is generic enough to be applied to a wide range of long-context embedding models and works without additional training. To further increase the effectiveness of late chunking, the authors propose a dedicated fine-tuning approach for embedding models.

---

## 1. Problema: Perda de Contexto no Chunking Naive

### Motivação

Em sistemas RAG (Retrieval Augmented Generation), documentos são divididos em chunks menores para indexação vetorial. O problema fundamental: modelos de embedding de contexto longo (e.g., jina-embeddings-v2-small com 8192 tokens) ainda performam melhor em textos curtos. Chunking melhora a recuperação, mas introduz um novo problema: dependências semânticas de longa distância.

**Exemplo concreto:** Um artigo sobre Berlin é dividido em chunks por sentenças. Frases como "its" e "the city" referenciam "Berlin", que aparece apenas na primeira sentença. O modelo de embedding, ao processar cada chunk isoladamente, não consegue linkar essas referências à entidade correta.

**Evidência quantitativa (cosine similarity para query "Berlin"):**

| Texto | Sim. Naive | Sim. Late |
|-------|-----------|-----------|
| "Berlin is the capital and largest city of Germany..." | 0.8486 | 0.8495 |
| "Its more than 3.85 million inhabitants make it the EU's most populous city..." | 0.7084 | 0.8249 |
| "The city is also one of the states of Germany..." | 0.7535 | 0.8498 |

Com chunking naive, sentenças que não contêm a palavra "Berlin" têm scores de similaridade baixos, apesar de referirem-se à cidade em contexto. Com late chunking, os scores são consistentemente altos.

---

## 2. Método: Late Chunking

### Ideia Central

A diferença arquitetural entre naive chunking e late chunking é **quando** o chunking ocorre:

- **Naive chunking:** Divide o texto em substrings → passa cada chunk independentemente ao modelo → mean pooling por chunk
- **Late chunking:** Tokeniza e processa o texto inteiro no transformer → obtém embeddings de token com contexto completo → aplica mean pooling por chunk **depois**

O modelo processa o texto inteiro, permitindo que os embeddings de token do chunk "Its more than 3.85 million inhabitants..." já capturem a informação de que "its" = "Berlin" antes do pooling.

### Algoritmo (Late Chunking — Algorithm 1)

1. Aplica chunking strategy S ao texto T, obtendo (c₁, ..., cₙ)
2. Tokeniza T inteiro → (τ₁, ..., τₘ) com offsets de caracteres
3. Aplica o transformer a todos os tokens → (ϑ₁, ..., ϑₘ) (token embeddings contextualizados)
4. Traduz definições de chunks em posições de token (boundary cues)
5. Para cada chunk i, aplica mean pooling apenas sobre os token embeddings correspondentes: eᵢ = mean(ϑ_start..ϑ_end)

**Nota importante:** Late chunking ainda requer boundary cues de um algoritmo de chunking (fixed-size, sentence-based, semantic), mas esses cues são usados **após** obter os token embeddings — daí o nome "late".

### Long Late Chunking (Algorithm 2)

Para documentos com mais tokens do que o modelo suporta, o algoritmo processa o texto em "macro chunks" de lₘₐₓ tokens com sobreposição de ω tokens entre chunks adjacentes. Os tokens adicionais servem como contexto suplementar. O método é provadamente mais eficaz que truncação.

### Método de Treinamento: Span Pooling

Late chunking funciona sem treinamento adicional, mas o paper propõe um método de fine-tuning chamado "span pooling" para aumentar o desempenho:

- **Dados de treinamento:** Tuplas (query q, documento d, ⟨start, end⟩) onde ⟨start, end⟩ anota o span relevante no documento
- **Durante o treinamento:** Para documentos, os token embeddings são obtidos normalmente, mas o mean pooling é aplicado **apenas ao span anotado** (ao invés do documento inteiro)
- **Loss:** InfoNCE (contrastive), versão bidirecional
- **Datasets usados:** FEVER (spans = sentence annotations) e TriviaQA (spans = nomes, datas) — ambos disponibilizados no HuggingFace

---

## 3. Avaliação

### 3.1 Benchmark de Retrieval (BeIR — Section 4.1)

Avaliação em 4 datasets BeIR (SciFact, NFCorpus, FiQA, TRECCOVID) com 3 modelos de embedding (jina-embeddings-v2-small J2s, jina-embeddings-v3 J3, nomic-embed-text-v1 Nom) e 3 estratégias de chunking.

**Resultados (nDCG@10 [%]) — médias:**

| Estratégia | Naive AVG | Late AVG | Ganho Relativo |
|-----------|-----------|----------|---------------|
| Fixed-Size (256 tokens) | 52.2 | 54.0 | +3.46% |
| Sentence Boundaries (5 sentences) | 52.4 | 54.3 | +3.63% |
| Semantic Sentence Boundaries | 52.4 | 53.8 | +2.70% |

**Substituir naive chunking por late chunking quase sempre melhora o desempenho**, independente do modelo ou estratégia de chunking.

**Tabela completa (seleção):**

| Dataset | J2s Naive Fixed | J2s Late Fixed | J3 Naive Fixed | J3 Late Fixed |
|---------|-----------------|----------------|----------------|---------------|
| SciFact | 64.2 | 66.1 | 71.8 | 73.2 |
| NFCorpus | 23.5 | 30.0 | 35.6 | 36.7 |
| FiQA | 33.3 | 33.8 | 46.3 | 47.6 |
| TRECCOVID | 63.4 | 64.7 | 73.0 | 77.2 |

### 3.2 Influência do Tamanho do Chunk (Section 4.2)

Avaliação em NFCorpus (BeIR) e datasets LongEmbed com tamanhos de chunk variáveis:

- **Late chunking supera naive chunking especialmente para chunks pequenos**
- Para NFCorpus: late chunking consistentemente superior em todos os tamanhos
- Para datasets sintéticos (Needle-8192, Passkey-8192): late chunking **não** é útil — contexto adicional do documento é irrelevante (informação relevante está embebida em texto não relacionado)
- **Limitação identificada:** Em tarefas de reading comprehension que requerem encontrar uma sentença específica em contexto não relacionado, naive chunking com chunks grandes pode superar late chunking

### 3.3 Long Late Chunking (Section 4.3)

Avaliação em 3 datasets de reading comprehension não-sintéticos sem truncação. Long late chunking supera naive chunking. Comparação direta com a Seção 4.2: scores nDCG maiores que na versão com truncação (8192 tokens), confirmando que truncação causa perda de informação.

### 3.4 Treinamento com Span Pooling (Section 4.4)

Modelos: jina-embeddings-v3 e jina-embeddings-v2-small-en. Chunk size fixo: 64 tokens.

**Resultados (nDCG@10 [%]):**

| Modelo | Pooling Treinamento | Dataset Treino | SciFact | NarrativeQA | NFCorpus | TREC-COV | FiQA |
|--------|---------------------|----------------|---------|-------------|----------|-----------|------|
| J3 | Span-Based | TriviaQA+FEVER | 72.61 | 44.01 | 36.80 | 77.59 | 48.22 |
| J3 | Mean | TriviaQA+FEVER | 72.59 | 43.83 | 36.77 | 77.21 | 47.40 |
| J2s | Span-Based | TriviaQA+FEVER | 65.20 | 47.29 | 29.96 | 65.18 | 34.52 |
| J2s | Mean | TriviaQA+FEVER | 64.77 | 47.31 | 29.70 | 64.73 | 33.87 |

Span pooling consistentemente supera mean pooling no treinamento por margem pequena. Os dois datasets de treinamento (~470k pares totais) são todos da Wikipedia, o que limita a diversidade e provavelmente restringe os ganhos potenciais.

### 3.5 Comparação com Contextual Embedding (Anthropic) — Section 4.5

Experimento pequeno comparando late chunking com a abordagem de Contextual Retrieval da Anthropic (blog post, 2024), que usa um LLM para gerar texto contextual que é adicionado ao início de cada chunk antes do embedding.

**Documento financeiro fictício, query:** "What is ACME Corp's revenue growth for Q2 2023?"

| Chunk | Similarity Late | Similarity Contextual | Similarity Naive |
|-------|----------------|----------------------|-----------------|
| "The recent SEC filing provided insights..." | 0.8305 | 0.8069 | 0.8505 |
| "It highlighted a 3% revenue growth..." (relevante) | 0.8516 | 0.8590 | 0.6343 |
| "The company, which had a revenue of $314M..." | 0.8424 | 0.8546 | 0.6169 |
| "They attributed this growth to strategic initiatives..." | 0.7997 | 0.8234 | 0.5191 |

**Conclusão:** Ambos os métodos identificam corretamente o chunk relevante com scores altos. Naive chunking falha (score do chunk relevante mais baixo que outros chunks). Late chunking tem a vantagem de **não requerer um LLM adicional**, sendo computacionalmente mais eficiente.

---

## 4. Limitações

1. **Documentos sintéticos com contexto irrelevante:** Late chunking não ajuda (e pode prejudicar) quando o contexto do documento não é relevante para o chunk — e.g., "needle in a haystack" tasks
2. **Chunks grandes em reading comprehension:** Naive chunking com chunks grandes pode superar late chunking em algumas tarefas específicas
3. **Diversidade de dados de treinamento limitada:** Os datasets de span pooling (~470k pares) são exclusivamente da Wikipedia, potencialmente limitando ganhos de treinamento

---

## 5. Benefícios Adicionais Documentados

**Chunking melhora retrieval mesmo com modelos de contexto longo (Appendix A.1):**

| Dataset | No Chunking (8192 tok) | Chunking 128 tok | Chunking 512 tok |
|---------|----------------------|-----------------|-----------------|
| NarrativeQA (nDCG@10) | 32.73 | 46.28 | 47.63 |
| 2WikiMultiHopQA | 70.32 | 91.36 | 86.30 |
| SummScreenFD | 91.24 | 88.21 | 89.71 |
| QMSum | 36.81 | 47.99 | 48.34 |

Melhoria média relativa do chunking (512 tokens): **+24.47%** — confirmando que chunking é benéfico mesmo quando todos os textos cabem na janela do modelo.

**Overlapping chunks não ajudam (Appendix A.2):** Experimentos com sobreposição de 16 tokens em chunks de 256 tokens mostram que overlap não melhora (nem prejudica) significativamente o desempenho com jina-embeddings-v2-small.

---

## 6. Conclusão

Late chunking resolve o problema de perda de contexto no chunking sem exigir treinamento adicional, sem usar LLMs, e com compatibilidade com qualquer estratégia de chunking existente (fixed-size, sentence-based, semantic). A melhoria média de 3.46-3.63% (relativa) em nDCG@10 é consistente através de modelos e datasets. O método de long late chunking estende a técnica para documentos que excedem a janela de contexto do modelo. Span pooling como método de treinamento oferece ganhos adicionais modestos, mas consistentes.
