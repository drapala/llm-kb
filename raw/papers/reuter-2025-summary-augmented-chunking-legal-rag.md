# Towards Reliable Retrieval in RAG Systems for Large Legal Datasets

**Autores:** Markus Reuter, Tobias Lingenberg, Rūta Liepiņa, Francesca Lagioia, Marco Lippi, Giovanni Sartor, Andrea Passerini, Burcu Sayin  
**Instituições:** TU Darmstadt, University of Florence, University of Bologna (ALMA-AI), University of Trento, European University Institute  
**arXiv:** 2510.06999  
**URL:** https://arxiv.org/abs/2510.06999  
**Código:** https://github.com/DevelopedByMarkus/summary-augmented-chunking  
**Data:** 2025  

---

## Abstract

Retrieval-Augmented Generation (RAG) é uma abordagem promissora para mitigar alucinações em LLMs em aplicações legais, mas sua confiabilidade é criticamente dependente da acurácia da etapa de recuperação. Isso é particularmente desafiador no domínio legal, onde grandes bases de dados de documentos estruturalmente similares frequentemente fazem os sistemas de recuperação falharem. O paper define e quantifica uma falha crítica denominada **Document-Level Retrieval Mismatch (DRM)**, onde o retriever seleciona informações de documentos-fonte completamente incorretos. Para mitigar o DRM, os autores propõem **Summary-Augmented Chunking (SAC)**, uma técnica simples e computacionalmente eficiente que enriquece cada chunk de texto com um resumo sintético em nível de documento, injetando contexto global crucial que seria perdido durante o processo padrão de chunking. Os experimentos no LegalBench-RAG demonstram que SAC reduz drasticamente o DRM e melhora precisão e recall de recuperação em nível de texto. Surpreendentemente, uma estratégia de sumarização genérica supera uma abordagem que incorpora conhecimento especializado de domínio legal.

---

## 1. Introdução e Motivação

LLMs são adotados crescentemente em domínios de alto risco como o direito, mas permanecem limitados por alucinações. Estudos recentes reportam taxas de alucinação entre 58–80% para LLMs de uso geral em tarefas legais. RAG foi estabelecido como abordagem líder para melhorar confiabilidade.

Em documentos legais longos e estruturalmente similares, identificar o trecho de texto relevante como "agulha no palheiro" torna-se prioridade central. O paper foca no **estágio pré-retrieval**: a engenharia da base de conhecimento que forma a fundação de qualquer sistema RAG confiável.

### Desafios únicos de texto legal para RAG

1. **Redundância Lexical:** Linguagem jurídica é altamente padronizada, com cláusulas boilerplate e terminologia especializada repetidas em milhares de documentos. NDAs dentro de uma base de dados podem ser estruturalmente quase idênticos, diferindo apenas em variáveis críticas como nomes das partes ou datas.

2. **Estrutura Hierárquica:** Textos legais são organizados em layouts complexos com seções aninhadas, subseções e referências cruzadas densas. Estratégias padrão de chunking ignoram a hierarquia do documento.

3. **Informação Fragmentada:** Responder a uma questão legal frequentemente exige sintetizar informações espalhadas por múltiplas seções ou até documentos diferentes.

4. **Proveniência e Rastreabilidade:** Em aplicações legais, a proveniência da informação é de alta importância. Recuperar uma cláusula de um contrato similar mas distinto compromete a validade legal do output gerado e corrói a confiança do usuário.

---

## 2. Document-Level Retrieval Mismatch (DRM)

### Definição

DRM é definido como a proporção de chunks top-k recuperados que **não se originam do documento contendo o texto ground-truth**.

### Observação empírica

Em experimentos com pipeline RAG padrão no ContractNLI (362 documentos de NDAs), os autores observaram taxas de DRM superiores a **95%** — o retriever quase sempre selecionava chunks do documento errado.

Hipótese dos especialistas legais: a natureza altamente padronizada e boilerplate dos NDAs, uniformes exceto por poucos variáveis-chave, confunde modelos de recuperação que dependem de similaridade semântica ou correspondência de keywords.

### Por que DRM é crítico

Mesmo que a resposta gerada seja factualmente correta por coincidência, profissionais legais exigem raciocínio documento-fiel: cada pedaço de informação deve ser validável contra sua fonte específica no documento original. DRM é, portanto, medida fundamental de confiabilidade de sistema.

---

## 3. Summary-Augmented Chunking (SAC)

### Metodologia

SAC funciona em quatro passos:

1. **Sumarização:** Para cada documento no corpus, um LLM gera um único resumo conciso de ~150 caracteres como "impressão digital do documento".
2. **Chunking:** Aplicação de recursive character splitting para particionar o conteúdo do documento em chunks menores (chunk size de 500 caracteres, sem overlap, como baseline).
3. **Augmentação:** O resumo em nível de documento é prepended a cada chunk derivado daquele documento.
4. **Indexação:** Os chunks augmentados com resumo são então embarcados e indexados em base de dados vetorial para recuperação.

**Prompt genérico de sumarização:**
```
System: You are an expert legal document summarizer.
User: Summarize the following legal document text. Focus on extracting the most 
important entities, core purpose, and key legal topics. The summary must be concise, 
maximum {char_length} characters long, and optimized for providing context to smaller 
text chunks. Output only the summary text.
```

O método requer apenas uma chamada adicional de LLM por documento e integra-se facilmente em pipelines RAG existentes com overhead computacional mínimo.

### Sumarização Guiada por Especialistas

Os autores também testaram uma abordagem alternativa de "meta-prompt" desenvolvida com dois especialistas legais (professor associado e pesquisador pós-doutoral em direito, especialistas em proteção de dados e direito privado). O meta-prompt instrui o LLM a gerar resumos o mais **distintos possível** dentro de um tipo de documento, identificando e priorizando variáveis legais-chave diferenciadoras:
- Para políticas de privacidade: partes, categorias de dados e seu processamento
- Para NDAs: definições de informação confidencial, partes, prazo, lei aplicável

---

## 4. Setup Experimental

**Benchmark:** LegalBench-RAG (Pipitone e Alami, 2024) — especificamente projetado para isolar e avaliar o componente de recuperação de sistemas RAG no domínio legal.

**Datasets avaliados:**
- **CUAD** (Contract Understanding Atticus Dataset): contratos gerais
- **MAUD** (Merger Agreement Understanding Dataset): acordos de fusão
- **ContractNLI**: acordos de não-divulgação (NDAs)
- **PrivacyQA**: políticas de privacidade de aplicações móveis

**Métricas:**
- DRM (métrica primária): mismatch em nível de documento
- Precisão em nível de caractere: fração do texto recuperado que é parte do ground-truth
- Recall em nível de caractere: fração do ground-truth encontrada pelo sistema

**Configuração técnica:**
- Resumos gerados com gpt-4o-mini (~150 caracteres)
- Embeddings: `thenlper/gte-large`
- Banco vetorial: FAISS com similaridade por cosseno
- Também testado: BM25 híbrido (dense+sparse) — melhorou DRM mas reduziu precision/recall, introduziu overhead adicional

---

## 5. Resultados

### SAC reduz DRM pela metade

SAC reduz dramaticamente o DRM em comparação ao baseline em toda gama de hiperparâmetros, **efetivamente reduzindo a taxa de mismatch à metade**. Essa melhoria na acurácia em nível de documento se traduz diretamente em qualidade de recuperação melhorada: sistemas RAG usando SAC superam significativamente o baseline RAG padrão em precisão e recall em nível de caractere.

Caso exemplar (ContractNLI, NDA Evelozcity):
- **Baseline (sem resumo):** Recupera documento errado (NDA-ROI-Corporation) — falha completa por distração pela similaridade estrutural
- **SAC genérico (150 chars):** Recupera documento correto (NDA-Evelozcity) com 97% precisão, 50% recall
- **SAC expert-guided:** Recupera documento correto mas snippet irrelevante (boilerplate introdutório)

### Sumarização genérica supera a especializada

Surpreendentemente, a sumarização guiada por especialistas **não produziu melhorias** sobre o prompt genérico. Apenas em alguns cenários específicos (chunk sizes maiores) houve ligeiras melhorias.

**Hipóteses para este resultado contraintuitivo:**
1. Resumos genéricos podem alcançar melhor equilíbrio entre distintividade e alinhamento semântico amplo com maior variedade de queries potenciais. Dicas altamente específicas podem "overfitar" a características estreitas.
2. A linguagem densa e estruturada dos resumos especializados pode apresentar desafios para modelos de embedding menores, que devem comprimir tanto o resumo quanto o chunk em um único vetor.

### Avaliação qualitativa de especialistas legais

Especialistas legais avaliam os resumos expert-guided (especialmente com 300 chars) como mais ricos, estruturados e contendo informação altamente discriminativa para diferenciar NDAs. Porém, essa avaliação legal contrasta com o desempenho de recuperação observado: resumos especialistas, apesar de legalmente mais informativos, não se traduzem em melhor recuperação de snippet em nível de texto.

---

## 6. Discussão

### Valor da abordagem

A solução SAC é **prática, escalável e facilmente integrável**:
- Ao contrário de soluções arquiteturalmente complexas (knowledge graphs, late chunking, modelos de contexto longo), SAC é barato, requerendo apenas um resumo adicional por documento
- Integra-se perfeitamente em pipelines RAG existentes
- Escalável mesmo para bases legais grandes e dinamicamente mutáveis

### Limitações

1. Experimentos restritos a categorias específicas de documentos legais e conduzidos exclusivamente em inglês
2. Contextos legais restritos a common-law; significado legal é altamente específico por jurisdição
3. Análise focou em intervenção isolada dentro de pipeline RAG padrão — taxas residuais de mismatch permanecem significativas
4. Não inclui avaliação end-to-end (somente etapa de recuperação); trabalhos futuros incluirão benchmarking completo geração

### Próximos passos

- Estender o princípio de sumarização hierarquicamente (nível de parágrafo, seção, documento)
- Aplicar métodos de otimização de query (transformação, expansão, roteamento)
- Adicionar etapa de reranking
- Comparar SAC contra Late Chunking e RAPTOR

---

## 7. Conclusão

O paper demonstra que **Document-Level Retrieval Mismatch** é uma falha dominante em RAG aplicado a documentos legais, onde language boilerplate padronizada causa frequente confusão cross-document. **Summary-Augmented Chunking (SAC)** — prepending de resumo em nível de documento a cada chunk — reduz drasticamente esse mismatch e melhora precision e recall de recuperação.

Achado-chave: resumos genéricos superam resumos especializados com conhecimento de domínio legal. Sinais semânticos amplos provam ser mais robustos e generalizáveis do que informação legal densa e estruturada para fins de guiar retrievers.

SAC não é solução completa isoladamente, mas oferece intervenção prática e escalável para sistemas RAG legais mais confiáveis, representando passo em direção à visão de "LLMs como leitores legais".

---

## Fontes Principais Citadas

- LegalBench-RAG: Pipitone e Alami (2024) — benchmark para recuperação isolada em RAG legal
- LegalBench: Guha et al. (2023) — benchmark de capacidades de raciocínio LLM
- CUAD: Hendrycks et al. (2021) — Contract Understanding Atticus Dataset
- MAUD: Wang et al. (2023) — Merger Agreement Understanding Dataset
- ContractNLI: Koreeda e Manning (2021) — NDAs
- PrivacyQA: Ravichander et al. (2019) — políticas de privacidade
- RAPTOR: Sarthi et al. (2024) — abordagem hierárquica alternativa
- Late Chunking: Günther et al. (2024) — chunking em nível de embedding
- Contextual Retrieval: Anthropic — técnica de enriquecimento de contexto similar
