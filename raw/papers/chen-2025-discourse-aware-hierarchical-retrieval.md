# Beyond Chunking: Discourse-Aware Hierarchical Retrieval for Long Document Question Answering

**Autores:** Huiyao Chen, Yi Yang, Yinghui Li, Meishan Zhang (corresponding), Baotian Hu, Min Zhang  
**Instituições:** Institute of Computing and Intelligence, Harbin Institute of Technology (Shenzhen); Shenzhen Loop Area Institute (SLAI)  
**arXiv:** 2506.06313  
**URL:** https://arxiv.org/abs/2506.06313  
**Código:** https://github.com/DreamH1gh/DISRetrieval  
**Data:** 2025  

---

## Abstract

Sistemas existentes de question answering em documentos longos tipicamente processam textos como sequências flat ou usam chunking heurístico, ignorando as estruturas de discurso que naturalmente guiam a compreensão humana. Este trabalho apresenta **DISRetrieval** (Discourse-aware hierarchical Retrieval), um framework discourse-aware hierárquico que aproveita a teoria da estrutura retórica (RST) para question answering em documentos longos. A abordagem converte árvores de discurso em representações em nível de sentença e emprega representações de nós aprimoradas por LLM para fazer ponte entre informações estruturais e semânticas. O framework envolve três inovações-chave: parsing de discurso universal-linguístico para documentos extensos, aprimoramento baseado em LLM de nós de relações de discurso, e recuperação hierárquica guiada por estrutura. Experimentos extensos em quatro datasets demonstram melhorias consistentes sobre abordagens existentes através da incorporação de estrutura de discurso, em múltiplos gêneros e idiomas.

---

## 1. Introdução e Motivação

LLMs alcançaram sucesso notável em QA de documentos curtos (SQuAD: média de 117 palavras, F1 >85%). Porém, conforme o comprimento do documento aumenta, o desempenho degrada significativamente. Em datasets desafiadores de documentos longos como QASPER, modelos de ponta alcançam menos de 50% de F1.

### Limitações das abordagens atuais

**Modelagem flat sequencial (chunking padrão):** Processa textos como sequências lineares ou os divide em chunks de tamanho fixo. Amplamente adotado por simplicidade e eficiência computacional.

**Métodos baseados em árvore existentes:**
- *Semantic clustering (RAPTOR):* Agrupa conteúdo similar recursivamente
- *Bisection-based:* Mantém coerência local por agrupamento de segmentos adjacentes

Ambos representam melhorias mas capturam apenas similaridade semântica ou coerência textual — ignoram como humanos *organizam e compreendem* informação em documentos.

### Por que estrutura de discurso?

Estrutura de discurso fornece fundação linguística principiada para organização de documentos que vai além de similaridades superficiais. Considere um documento onde:
- Sentença 1: declaração de tópico
- Sentenças 2-3: ideias contrastantes
- Sentenças 4-5: evidência de suporte paralela
- Sentença 6: declaração conclusiva

Essas relações de discurso capuram naturalmente como humanos organizam e compreendem informação, fornecendo orientação para chunking mais semanticamente apropriado e organização hierárquica para recuperação.

RST (*Rhetorical Structure Theory*) formaliza isso representando documentos como árvores hierárquicas onde nós-folha correspondem a unidades elementares de discurso (EDUs) e nós internos codificam relações retóricas (contraste, elaboração, resumo, etc).

---

## 2. Framework DISRetrieval

O framework opera em três estágios:
1. Construção de árvores de discurso hierárquicas via parsing RST em nível de sentença
2. Enriquecimento de nós da árvore com representações semânticas via aprimoramento LLM e encoding denso
3. Recuperação de evidências guiada por estrutura

### 2.1 Construção de Árvore Discourse-Aware

#### Adaptações RST

**Adaptação de Granularidade:** RST tradicional opera em EDUs de granularidade fina, criando overhead computacional e fragmentação semântica para documentos longos. Solução: shift do processamento RST para o *nível de sentença*, alcançando melhor eficiência mantendo coerência semântica. O parser em nível de sentença é treinado convertendo datasets EDU existentes via: (1) fusão de EDUs intra-sentença em unidades de sentença unificadas, (2) determinação de relações inter-sentença via análise de ancestral comum mais baixo nas árvores EDU originais.

**Adaptação de Linguagem:** Para habilitar aplicabilidade cross-lingual além do inglês, é desenvolvido parser de discurso universal-linguístico via aumento de dados multilíngue baseado em LLM. GPT-4o é utilizado para traduzir o corpus de treinamento RST-DT para idiomas-alvo preservando estruturas de discurso em nível de sentença.

#### Processo de Construção em Duas Fases

**Fase 1 — Construção de Árvore em Nível de Parágrafo:**  
Cada sequência de sentenças de parágrafo é transformada em árvore de discurso local usando o parser. Cada árvore captura conexões de sentença dentro do parágrafo.

**Fase 2 — Construção de Árvore em Nível de Documento:**  
Construção de estrutura global do documento através de aprimoramento LLM bottom-up. Para cada nó interno na árvore de parágrafo:
- Se comprimento combinado dos filhos ≥ limiar τ: LLM gera resumos concisos
- Caso contrário: concatenação direta de conteúdo

As representações raiz das árvores de parágrafo servem como input para construção de árvore de documento, criando estrutura hierárquica capturando relações de discurso em nível de documento.

### 2.2 Representação de Nós Discourse-Aware

**Aprimoramento Semântico Bottom-up:** A árvore de documento inicialmente carece de conteúdo semântico concreto em nós internos. Mesma estratégia de aprimoramento LLM bottom-up é aplicada para gerar representações textuais significativas, transformando nós internos de placeholders estruturais abstratos em representações semanticamente ricas.

**Integração de Árvore Multi-Nível:** Cada nó-folha da árvore de documento é sistematicamente substituído pela árvore de discurso em nível de parágrafo correspondente. Habilita modelagem de discurso multi-granularidade, onde relações intra-parágrafo finas coexistem com conexões inter-parágrafo grossas em estrutura hierárquica única.

**Encoding de Nós:** Para habilitar recuperação eficiente, a árvore integrada é transformada em embeddings densos usando encoder pré-treinado.

### 2.3 Recuperação de Evidências Guiada por Estrutura

**Estratégia de Seleção Dual:**
- *Seleção direta de folhas* para sentenças de alta relevância
- *Expansão hierárquica* com seleção top-k das subárvores para nós internos
- *Eliminação de redundância* para prevenir duplicatas

**Algoritmo:**
1. Computar similaridades semânticas para todos os nós via cosine similarity com a query
2. Para nós-folha com alta relevância: seleção direta
3. Para nós internos: seleção controlada de subárvore — selecionar top-k folhas mais relevantes não-utilizadas da subárvore
4. Preservar ordem original do documento (não ordem de ranking)

Esse mecanismo garante que tanto evidências específicas em nível de sentença quanto segmentos de discurso coerentes sejam capturados, eliminando redundância.

---

## 3. Configuração Experimental

**Datasets (quatro benchmarks desafiadores):**
- **QASPER** (Dasigi et al., 2021): papers de pesquisa, média 4.170 palavras — métricas: F1-Match e Recall em nível de token
- **QuALITY** (Pang et al., 2022): compreensão leitora, média 5.022 palavras — métrica: acurácia
- **NarrativeQA** (Kočiský et al., 2018): narrativas de livros, média 51.372 palavras (máx 346.902) — métricas: BLEU/ROUGE/METEOR
- **MultiFieldQA-zh** (Bai et al., 2024): documentos em chinês, média 6.701 palavras — métrica: F1-Match

**Baselines:**
- **Flatten-chunk:** chunks de max 100 palavras preservando fronteiras de sentença
- **Flatten-sentence:** divisão em nível de sentença com recuperação direta
- **RAPTOR:** árvore semântica via embedding recursivo, clustering e sumarização
- **Bisection:** compartilha representações de nós LLM-enhanced e mecanismo de recuperação hierárquica do DISRetrieval, mas constrói árvores dividindo sentenças em subárvores binárias balanceadas (isola a contribuição específica da estrutura de discurso)

**Implementação:**
- Parser de discurso treinado no RST-DT com backbone `gte-multilingual-base`, aumentado com dados chineses traduzidos via GPT-4o
- Todas as sumarizações (DISRetrieval e baseline RAPTOR): Llama3.1-8B-Instruct
- Encoder de sentença: Sentence-BERT e OpenAI text-embedding-3-large
- Top-K = 5; limiar τ = 0 para QASPER, τ = 50 para QuALITY/NarrativeQA
- Modelos de geração: UnifiedQA-3B, GPT-4.1-mini, Deepseek-v3

---

## 4. Resultados

### 4.1 Desempenho de Geração (QASPER e QuALITY)

**Superioridade consistente em todos os cenários.** DISRetrieval supera todos os baselines independentemente de comprimento de contexto, modelo de embedding, ou arquitetura de geração.

Resultado representativo (400 palavras de contexto, UnifiedQA-3B):
- vs flatten-sentence (QASPER): +2.66% F1-Match
- vs flatten-sentence (QuALITY): +3.60% acurácia

**Estrutura de discurso supera clustering semântico.** Comparado ao RAPTOR (QASPER, OpenAI embeddings, contexto 300w): DISRetrieval 40.03% vs RAPTOR 39.96% F1-Match.

**Discurso linguístico essencial para modelagem hierárquica.** A ablação Bisection valida a hipótese central: enquanto organização hierárquica ajuda (Bisection > flat baselines), incorporar estrutura de discurso é crucial (DISRetrieval > Bisection consistentemente).

**Tabela representativa (GPT-4.1-mini, contexto 400w):**

| Método | QASPER F1 SBERT | QASPER F1 OpenAI | QuALITY Acc SBERT | QuALITY Acc OpenAI |
|--------|-----------------|-------------------|--------------------|--------------------|
| flatten-chunk | 42.72 | 44.78 | 67.69 | 71.05 |
| flatten-sentence | 42.44 | 45.78 | 65.24 | 69.94 |
| RAPTOR | 42.50 | 43.85 | 67.26 | 70.71 |
| Bisection | 43.49 | 45.69 | 67.93 | 72.00 |
| **DISRetrieval** | **44.95** | **46.31** | **69.37** | **73.54** |

### 4.2 Desempenho de Recuperação (QASPER)

DISRetrieval supera consistentemente todos os baselines em F1 e Recall com ambos os modelos de embedding (SBERT e OpenAI). Para contextos mais longos (300-400 palavras), enquanto todos os métodos mostram alguma degradação de F1, DISRetrieval mantém desempenho superior, particularmente em métricas de Recall.

Exemplo (contexto 200w, OpenAI): DISRetrieval F1=30.27%, Recall=65.33% vs flatten-sentence F1=28.25%, Recall=62.78%.

**Achado importante:** Evidência golden (média 129 palavras) atinge F1 de 50.71%, superando significativamente full document (4.170 palavras, F1=48.81%). Recuperação concisa e precisa é mais eficaz do que usar contexto substancialmente maior. Adicionar evidências recuperadas ao documento completo produz melhoras consistentes de 0.73-1.39%.

### 4.3 Eficácia Cross-Lingual (MultiFieldQA-zh, chinês)

DISRetrieval supera todos os baselines com GPT-4.1-mini (35.25% F1 no contexto 400w) e Deepseek-v3 (29.54% F1). Melhorias particularmente notáveis em contextos mais longos (+1.30 a +1.56% sobre Bisection com Deepseek-v3). Valida que estruturas de discurso linguisticamente fundamentadas transcendem fronteiras linguísticas.

### 4.4 Documentos Extremamente Longos (NarrativeQA)

DISRetrieval supera flatten-chunk baseline por: +1.15% BLEU, +1.89% ROUGE, +1.46% METEOR.

Notavelmente, tanto DISRetrieval quanto RAPTOR superam substancialmente métodos flat, confirmando que abordagens estruturadas são mais eficazes que flat para recuperação em documentos extremamente longos. DISRetrieval oferece vantagens consistentes sobre RAPTOR.

---

## 5. Ablações e Discussões

### RQ3: Estratégia de recuperação hierárquica é eficaz?

Comparação de cinco variantes em QuALITY:
1. Leaf-only baseline
2. Summary-based retrieval
3. All filtered-leaves
4. Top-K com ordem de ranking
5. **Top-K com ordem original** (método proposto)

Achados:
1. Recuperação baseada em resumo underperforma o baseline leaf, confirmando que preservar detalhes originais de texto é crucial
2. All filtered-leaves mostra melhorias marginais; métodos Top-K seletivos são superiores por redução de ruído
3. Top-K origin consistentemente alcança melhor desempenho preservando fluxo natural do documento

### RQ4: Escala do LLM afeta qualidade da estrutura?

Modelos menores (Llama-3.1-8B, Qwen2.5-7B, Mistral-7B) alcançam desempenho comparável a modelos maiores, com diferenças abaixo de 0.5%. DISRetrieval **não depende fortemente da escala do LLM** — possibilita deployment de baixo custo com modelos 7B.

DISRetrieval é **3× mais rápido que RAPTOR** (50K palavras: 103s vs 338s), com custos de pré-processamento amortizados em múltiplas queries.

### RQ5: Capacidade do parser de discurso impacta desempenho?

Desempenho melhora consistentemente conforme a escala de dados de treinamento do parser aumenta (0-100% do RST-DT). Apesar do parser ser treinado predominantemente em texto de notícias (RST-DT), DISRetrieval supera todos os baselines em gêneros diversos (papers de pesquisa, ficção, scripts de filmes), demonstrando robustez prática e potencial extensível conforme tecnologia de parsing avança.

---

## 6. Conclusão

DISRetrieval apresenta framework de recuperação hierárquica discourse-aware que sistematicamente incorpora RST em QA de documentos longos. Três inovações-chave: (1) parsing universal-linguístico de discurso, (2) representações de nós LLM-enhanced, (3) seleção de evidências guiada por estrutura.

Experimentos em QASPER, QuALITY, NarrativeQA e MultiFieldQA-zh demonstram melhorias substanciais sobre métodos existentes, validando que:
- Estrutura de discurso provê organização mais principiada que clustering semântico
- Recuperação precisa supera quantidade maior de contexto
- Estruturas de discurso linguisticamente fundamentadas transcendem fronteiras linguísticas
- Modelos 7B são suficientes para aprimoramento de nós

O trabalho demonstra que abordagens linguisticamente fundamentadas permanecem valiosas na era de LLMs, oferecendo alternativas principiadas a métodos puramente orientados a dados para recuperação em documentos longos.

---

## Limitações

1. Desempenho do parser de discurso limita efetividade geral do sistema — qualidade do parser impacta diretamente desempenho downstream
2. Estratégia de sumarização adaptativa com limiar τ é relativamente simples (τ=0 para papers, τ=50 para narrativas); thresholding dinâmico mais sofisticado baseado em complexidade de conteúdo poderia otimizar trade-off
3. Métricas de avaliação atuais podem não capturar totalmente os benefícios nuançados da recuperação discourse-aware, como preservação de coerência estrutural e fluxo hierárquico de informação
4. Avaliação multilíngue atualmente limitada a inglês e chinês

---

## Datasets e Baselines Principais

**Benchmark datasets:**
- QASPER: Dasigi et al. (2021) — papers de pesquisa
- QuALITY: Pang et al. (2022) — compreensão leitora
- NarrativeQA: Kočiský et al. (2018) — narrativas de livros/filmes
- MultiFieldQA-zh: Bai et al. (2024) — documentos multi-domínio em chinês (LongBench)

**Trabalhos relacionados-chave:**
- RAPTOR (Sarthi et al., 2024): clustering semântico hierárquico recursivo
- RST-DT (Carlson et al., 2001): corpus de discurso estruturado
- Flatten-chunk/sentence: métodos baseline amplamente usados
- DPR (Karpukhin et al., 2020): dense passage retrieval
