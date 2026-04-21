---
title: "GNN para Detecção de Fraude em Supply Chain Finance"
sources:
  - path: raw/papers/wu-2024-gnn-supply-chain-fraud.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-11
updated: 2026-04-11
tags: [GNN, graph-neural-networks, fraud-detection, supply-chain, heterogeneous-graphs, multi-task-learning, explainability]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
status: promoted
promoted_date: 2026-04-11
freshness_status: current
---

## Resumo
Wu et al. (Information Systems 2024) propõe MultiFraud: framework de detecção de fraude em supply chain finance usando GNNs heterogêneas com aprendizado multitarefa. O key insight: fraude em supply chains envolve múltiplos tomadores coordenados — análise por entidade isolada é insuficiente. Requer ground truth (labels supervisionados) para treinamento.

## Conteúdo

### O Problema

MultiFraud é otimizado para fraudes envolvendo múltiplos tomadores coordenados — um padrão distribuído no grafo que modelos por transação individual não capturam nativamente. Nota: nem toda fraude em supply chain tem este formato; métodos não-GNN (agregações por entidade, detecção de anéis) também detectam padrões relacionais, sem a escala de GNNs.

### Arquitetura MultiFraud

**Grafo heterogêneo:**
- Nós: empresas, tomadores, fornecedores, instituições financeiras
- Arestas heterogêneas: transações, relacionamentos comerciais, ownership, CNPJ overlaps

**Multi-view por domínio:**
- Grafos separados por tipo de relação (preserva semântica de cada tipo)
- GNNs heterogêneas aplicadas a cada view separadamente
- Mecanismo de atenção para compartilhamento de embeddings entre entidades

**Multi-task learning:**
- Treina detecção de múltiplos tipos de entidade fraudulenta simultaneamente
- Regulariza o modelo, mitigando (não eliminando) overfitting a um único tipo de fraude — negative transfer é possível se as tarefas forem muito diferentes

**Explicabilidade:**
- Gera pesos de features por predição (atributos da entidade)
- Gera pesos de arestas (relações no grafo)
- Caveat: scores de atenção em GNNs são contestados como explicações causais — indicam correlação interna do modelo, não causalidade verificável

### Resultados

Avaliado em 5 datasets (privados, sem acesso público). Autores reportam que supera state-of-the-art nos seus benchmarks — métricas específicas não verificáveis externamente.

### Pré-requisitos para Uso

**Obrigatório:** ground truth supervisionado — labels indicando quais entidades são fraudulentas vs. legítimas. Sem isso, MultiFraud não treina.

**Tipos de dados necessários:**
- Transações entre entidades (grafo de relacionamentos)
- Atributos das entidades (valor, tipo, histórico)
- Labels de fraude confirmada (CGU, TCU, investigação judicial, etc.)

### Limitações

- Supervisão necessária — não é unsupervised anomaly detection
- Dados de treinamento podem ter viés de confirmação (fraudes conhecidas ≠ todas as fraudes)
- Métricas e datasets não publicados abertamente
- Escalabilidade para grafos muito grandes não discutida

## Verificação adversarial

**Claim mais fraco:** STUB — métricas de performance ("supera state-of-the-art") sem números verificáveis no abstract. Classificação como "state-of-the-art" é relativa ao benchmark e ao período.

**O que o paper não diz:** (1) como lidar com concept drift (fraude adapta padrões ao longo do tempo — Niehaus & Sukhtankar 2013 documenta isso); (2) como gerar ground truth inicial quando não há casos confirmados; (3) falsos positivos vs. falsos negativos tradeoff para uso operacional.

**Prior work citado:** métodos tradicionais de detecção por entidade isolada; GNNs homogêneos para fraude financeira.

## Quality Gate
- [x] Wikilinks tipados: sem wikilinks externos — artigo novo
- [x] Instance→class: "supera state-of-the-art" marcado como sem métricas verificáveis; "5 datasets" sem detalhes
- [x] Meta-KB separado: sem referências ao KB no Conteúdo
- [x] Resumo calibrado: source_quality medium (1 primary, STUB)

## Conexões
- neurosymbolic-ai-knowledge-graphs partOf gnn-fraud-detection-supply-chain (GNN = Categoria 1/2 DeLong: embeddings aprendidos com/sem logical constraints)

## Fontes
- [Wu et al. 2024](../../raw/papers/wu-2024-gnn-supply-chain-fraud.md) — MultiFraud, heterogeneous GNN, multi-task, supply chain fraud (STUB — Information Systems 2024)
