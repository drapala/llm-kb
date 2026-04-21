# Index — Retrieval & Architecture

<!-- ~20 artigos: RAG, hybrid search, context, memory, Single Brain, graph retrieval, chunking, legal RAG, DOs -->
<!-- raptor-vs-flat-retrieval (quarentena) = bridge RAPTOR↔retrieval bloqueado -->
<!-- 2026-04-13: +8 artigos Zelox RAG pipeline (chunking, segmentação DOs, modelos PT-BR) -->

- [Retrieval-Augmented Generation](concepts/retrieval-augmented-generation.md) — LC vs RAG eval: LC wins 56.3% vs 49%, but RAG irreplaceable for ~10%. Hybrid recommended
- [Hybrid Search](concepts/hybrid-search.md) — QMD: BM25+vector+reranking on-device, RRF fusion, smart chunking, MCP integration
- [Context Management](concepts/context-management.md) — WITHIN-SESSION: 4-layer compaction (micro→snip→auto→collapse). Operate within finite token budgets
- [Memory Consolidation](concepts/memory-consolidation.md) — CROSS-SESSION: KAIROS/Dream 4-phase cycle (orient→gather→consolidate→prune). Persist knowledge between sessions
- [RAPTOR vs. Flat 3-Layer Retrieval](concepts/raptor-vs-flat-retrieval.md) — ⏳QUARANTINED. Tree vs flat comparison: structural parallels (not validation). Chunking benchmarks challenge concept-based segmentation
- [Graph-Anchored Iterative Retrieval](concepts/graph-anchored-iterative-retrieval.md) — Liu et al. 2026: grafo ephemeral durante query guia subqueries. +14-23% F1 multi-hop. Resolve /ask iterativo com sufficiency judgment
- [Obsidian as Agent Wiki](concepts/obsidian-agent-workflow.md) — Default frontend for LLM KBs, vault separation pattern, 4-piece stack (app+clipper+CLI+skills)
- [LanceDB — Embedded Vector DB](concepts/lancedb-embedded-vector-db.md) — serverless, Lance format, hybrid search nativo (BM25+vector), reranking via CrossEncoder/ColBERT. Backend do Single Brain
- [Single Brain Data Ontology](concepts/single-brain-data-ontology.md) — ⏳QUARANTINED. EMERGIDO. Hindsight 4 redes epistêmicas → ontologia para world model multi-agente. Separação previne authority bias cascade
- [Single Brain — Phase 1 Design](concepts/single-brain-phase1-design.md) — ⏳QUARANTINED. EMERGIDO. Schema LanceDB 4 namespaces + provenance desde Dia 1. Agente único agora, multi-agent-ready
- [Multi-Agent Memory Consistency](concepts/multi-agent-memory-consistency.md) — Yu et al. 2026: consistência de memória multi-agente não foi formalmente definida. 2 gaps: cache sharing + access protocol
- [Collaborative Memory and Access Control](concepts/collaborative-memory-access-control.md) — Rezazadeh et al. 2025: grafos bipartidos G_UA/G_AR, dual memory (privado+compartilhado), provenance imutável. -61% resource calls
- [Summary-Augmented Chunking](concepts/summary-augmented-chunking.md) — SAC: prepend resumo doc a cada chunk. DRM >95%→47% em NDAs. Genérico supera especializado. Zelox: desambiguação entre atos boilerplate
- [Semantic Chunking — Custo vs. Benefício](concepts/semantic-chunking-cost-benefit.md) — Qu 2024 (NAACL): semantic NÃO justifica custo vs fixed-size em docs reais. Fixed-size wins. Query-type → chunk size ótimo
- [Late Chunking — Embeddings Contextuais](concepts/late-chunking-contextual-embeddings.md) — Jina AI: chunk após transformer (+3.5% nDCG). Preserva contexto cross-chunk sem LLM. Chunking +24% vs sem chunking
- [Hierarchical Chunking para RAG](concepts/hierarchical-chunking-rag.md) — HiChunk+Auto-Merge +9.4% ERec em evidence-dense. DISRetrieval RST 3× mais rápido que RAPTOR. L1-L3 suficiente
- [Blended RAG — Three-Way Retrieval](concepts/blended-rag-three-way-retrieval.md) — IBM: BM25+dense+SPLADE optimal. ColBERT in-database. Zelox: CNPJ/keyword + semântico + jargão normativo BR
- [Segmentação de Diários Oficiais](concepts/diario-oficial-segmentation-strategies.md) — Boundary detection como sequence labeling (NER). Regex 97.4% para vocabulário estável; CRF F1=75.65% DODF. QD: segmentação municipal (não ato)
- [MultiLegalSBD — Metodologia de Anotação](concepts/multilegalsbd-annotation.md) — F1 98.5% in-dist / 81.1% OOD. Zero-shot PT 91.6%. Schema de anotação para act boundary em DOs
- [PersoSEG — Segmentação NER no DODF](concepts/persoseg-dodf-ner-segmentation.md) — UnB/USP 2024: 127 docs DODF, CRF F1=75.65%. Atos frequentes >90%; raros <20%. Seção II≠contratos
- [Modelos BERT/RoBERTa Legal PT-BR](concepts/legal-bert-pt-models.md) — RoBERTaLexPT (2024) supera LegalBert-pt em PortuLex (4 tarefas). Legal-BERTimbau-sts BLOQUEADO 128 tok
- [Hard Negative Mining para Embeddings](concepts/embedding-hard-negative-mining.md) — NV-Retriever: positive-aware mining remove false negatives. MTEB 60.9 (#1 Jul 2024)
- [Document Image Quality Assessment](concepts/document-image-quality-assessment.md) — DocIQ 2025: DIQA-5000, 5 tipos de distorção, SRCC=0.91 com OCR accuracy. Triagem nativo/escaneado/degradado para pipeline Zelox
