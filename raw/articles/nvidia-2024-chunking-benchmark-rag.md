# NVIDIA Chunking Benchmark — 7 Strategies across 5 Datasets (2024)

**Origem:** NVIDIA Technical Report / Firecrawl blog  
**URL:** firecrawl.dev/blog/best-chunking-strategies-rag  
**Publicado:** 2024  
**Type:** STUB — relatório técnico/blog; sem arxiv

---

## Hipótese Central

Page-level chunking maximiza acurácia (0.648, menor variância) para documentos paginados. O **tipo de query** determina o chunk size ótimo: factoid queries → 256-512 tokens; analytical queries → 1024+ tokens.

---

## Evidências

- 7 estratégias testadas em 5 datasets com métricas quantificadas
- Page-level chunking: acurácia 0.648, menor variância entre estratégias
- Semantic chunking melhora recall em até 9% mas com custo 10× maior
- Adaptive chunking alinhado a topic boundaries: 87% accuracy vs 13% fixed-size (MDPI Bioengineering 2025)
- Chunk size sensitivity: small chunks (64-128 tokens) → fact-based queries; large chunks (512-1024) → contextual/analytical

---

## Limitações / Falsificadores

- "Page-level" não é relevante para DOs onde o ato não tem correlação com páginas físicas
- Datasets são de domínio geral — gap de domínio para português jurídico-administrativo
- 87% accuracy do adaptive chunking é de paper MDPI 2025, não do benchmark NVIDIA diretamente

---

## Design Implication para Zelox

O insight de **query-type → chunk size** é transferível:

| Query type | Exemplo Zelox | Chunk size |
|-----------|---------------|-----------|
| Factoid (entidade) | "CNPJ 00.000/0001-00 tem quantos contratos?" | 256 tokens (chunk = trecho do ato com entidade) |
| Analytical | "Padrão de superfaturamento em categoria X no estado Y" | 1024+ tokens (chunk = ato completo ou seção) |

Isso confirma a arquitetura de **três camadas de chunk** para Zelox:
- Layer 0: entidades extraídas (CNPJ, valor, modalidade)
- Layer 1: ato completo
- Layer 2: resumo + metadados do ato (para queries analíticas cross-document)

---

## Conexões

- Confirma: Qu 2024 (semantic chunking não justifica custo para queries factoids)
- Complementa: SAC 2025 (summary como prefixo do chunk cobre o caso de queries analíticas)
- Confirma: hierarquia DO→ato→entidade como design correto
