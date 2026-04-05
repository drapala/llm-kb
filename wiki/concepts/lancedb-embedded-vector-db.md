---
title: "LanceDB — Embedded Vector Database"
sources:
  - path: raw/papers/liu-2026-graphanchor-knowledge-indexing.md
    type: paper
    quality: secondary
    stance: neutral
created: 2026-04-05
updated: 2026-04-05
tags: [tooling, vector-db, retrieval, single-brain, infrastructure]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: emergence
emergence_trigger:
  pair: [single-brain-phase1-design, hybrid-search]
  ask_session: null
  connection_type: INSTANCIA
  pearl_level: L1
emerged_on: 2026-04-05
---

## Resumo

LanceDB is an embedded, serverless vector database built on the Lance columnar format (Apache Arrow-compatible). It runs entirely in-process — no daemon, no network — making it the pragmatic choice for local-first AI applications. Natively supports hybrid search (BM25 FTS + dense vector), multi-modal data, and reranking without external services.

## Conteúdo

### Arquitetura

LanceDB armazena dados no formato **Lance** — um formato colunar derivado do Apache Arrow otimizado para random-access em arrays de alta dimensão (vetores). Diferente de FAISS (índice em RAM) ou Chroma/Qdrant (servidores separados), LanceDB persiste diretamente em disco com operações ACID.

```
LanceDB
├── Lance format (columnar, disk-persisted)
├── ANN index (IVF-PQ, HNSW — criado on-demand)
├── FTS index (Tantivy — BM25 sobre text fields)
└── Python/Rust/JS APIs
```

**Propriedades chave:**
- **Embedded**: importa como biblioteca, sem servidor. `lancedb.connect("./path")` → pronto.
- **Schema via PyArrow**: schema definido com `pa.schema([pa.field("vector", pa.list_(pa.float32(), 768)), ...])`.
- **Upsert nativo**: `table.delete("source = 'X'")` + `table.add(rows)` — padrão de re-ingest.
- **Versioning**: toda escrita cria nova versão (snapshot). `table.checkout(version=N)` para rollback.

### Hybrid Search

LanceDB suporta os dois modos e fusão nativa:

```python
# Vector search
table.search(embed_vector).limit(10).select(["id","content"]).to_list()

# FTS (BM25)
table.search("query text", query_type="fts").limit(10).to_list()

# Híbrido nativo (experimental no LanceDB ≥0.5)
table.search("query", query_type="hybrid").limit(10).to_list()
```

Para controle fino sobre RRF weights, implementar fusão manual — ver [[hybrid-search]].

### FTS Index

O índice BM25 usa Tantivy internamente e precisa ser criado explicitamente:

```python
table.create_fts_index("content", replace=False)
```

**Gotcha:** `replace=False` falha silenciosamente se o índice já existe — encapsular em `try/except`. O índice persiste entre sessões mas precisa ser recriado após `--rebuild`.

### Reranking Nativo

LanceDB ≥0.5 inclui rerankers integrados:

```python
from lancedb.rerankers import CrossEncoderReranker, ColbertReranker

reranker = CrossEncoderReranker()  # ms-marco-MiniLM-L-6-v2 por default
results = table.search("query").limit(20).rerank(reranker).limit(5).to_list()
```

Alternativa: `ColbertReranker` — mais preciso, mais lento (~100ms vs ~20ms para cross-encoder).

### Gotchas de API

| Operação | Correto | Errado |
|----------|---------|--------|
| Listar tabelas | `db.table_names()` | `db.list_tables()` — retorna objeto, não lista |
| Verificar existência | `"table" in db.table_names()` | `db.list_tables()` — comparação falha silenciosamente |
| Criar se não existe | `db.create_table(name, schema=schema)` | Sem schema → schema inferido do primeiro batch |
| Drop para rebuild | `db.drop_table(name)` antes de `get_or_create_table()` | Inverter a ordem → erro de schema mismatch |

### Performance (corpus llm-kb)

Medições em 2026-04-05 no corpus de ~717 chunks / 77 artigos:

| Operação | Latência |
|----------|----------|
| Vector search (top-10) | ~15ms |
| BM25 FTS (top-10) | ~5ms |
| Hybrid manual RRF | ~25ms |
| Full ingest (77 artigos) | ~8 min (bottleneck: Ollama embed) |

### Quando usar LanceDB

**Use quando:**
- Aplicação local-first sem infra de servidor
- Corpus < ~1M vetores (embedded escala bem até aqui)
- Precisar de hybrid search e reranking no mesmo processo

**Considere alternativas quando:**
- Multi-tenant ou acesso concorrente pesado → Qdrant/Weaviate
- Corpus > 10M vetores → Pinecone/Weaviate hosted
- Precisar de filtering complexo em SQL → pgvector

## Interpretação

(⚠️ nossa interpretação) LanceDB resolve o problema de fricção de infra para agentes locais: não há serviço para subir, credenciais para gerenciar ou latência de rede. Para o padrão Single Brain — onde o agente é o único consumidor — embedded é a escolha ótima. O custo é a falta de acesso concorrente multi-processo.

(⚠️ nossa interpretação) O suporte nativo a reranking via `CrossEncoderReranker` torna LanceDB a opção de menor fricção para o próximo passo do Single Brain: reranker sobre os 717 chunks para resolver colisões semânticas (Hindsight vs Reflexion, autonomous-kb vs CLS).

## Conexões

- [[hybrid-search]] — RRF fusion manual com LanceDB como backend
- [[single-brain-phase1-design]] — LanceDB como Layer 0 do world model
- [[retrieval-augmented-generation]] — LanceDB instancia o padrão RAG localmente
- [[agent-memory-architectures]] — embedded vector DB = working memory tier

## Fontes

- Implementação em `scripts/single-brain/ingest.py` e `api/core.py` — fonte primária operacional
- [LanceDB docs](https://lancedb.github.io/lancedb/) — API reference
