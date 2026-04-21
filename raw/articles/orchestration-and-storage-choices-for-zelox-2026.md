# Orchestration and Storage Choices for Zelox (2026)

source: mixed
fetched: 2026-04-09
type: synthesis
notes: >
  Síntese arquitetural orientada a decisão. Baseada em:
  - Brazil Data Commons (arXiv)
  - DuckDB official open-government article
  - PostgreSQL docs
  - ClickHouse docs
  - Dagster docs / Dagster-vs-Prefect vendor comparison
  - Scrapy docs
  - Firecrawl docs

---

## Decisão de storage por fase

### V1

- `filesystem raw` para snapshots, ZIPs, JSON, PDFs
- `Postgres` para core operacional/transacional
- `DuckDB` para analytics local, validação de joins e exploração de snapshots

### V2+

- considerar `ClickHouse` quando existir:
  - analytics compartilhado multiusuário;
  - necessidade real de OLAP de baixa latência;
  - volume suficientemente alto para justificar mais uma engine

## Justificativa

### Postgres

Continua a escolha mais natural para:
- entidades persistentes;
- workflows operacionais;
- constraints, triggers, concorrência, integridade transacional.

### DuckDB

É a melhor candidata para:
- exploração local;
- validação de joins;
- consultas diretas a arquivos;
- batch analítico local.

### ClickHouse

É candidata de fase posterior para:
- OLAP massivo;
- analytics de alta simultaneidade;
- leitura em larga escala com baixa latência.

Não é a primeira coisa que o Zelox precisa antes de provar o pipeline.

## Decisão de orquestração/crawl por fase

### V1

- `Scrapy` como engine principal de crawlers dedicados
- `Dagster` como hipótese principal de orquestração
- `Firecrawl` como camada complementar para portais/documentos difíceis

### Mais tarde

- avaliar `scrapy-redis` ou scale-out equivalente se houver pressão real de crawl
- só considerar outra orquestração se Dagster provar fricção excessiva

## Justificativa

### Scrapy

Resolve bem:
- spiders por fonte;
- pipelines;
- scheduler;
- broad crawls;
- deduplicação de requests.

### Dagster

É forte quando a orquestração precisa ser:
- asset-aware;
- com lineage;
- freshness/observability no centro;
- integrada à semântica dos dados, não só às tasks.

### Firecrawl

Ajuda onde o custo de escrever crawler dedicado é alto e o portal é ruim/dinâmico.
Mas não substitui ingestão oficial nem modelagem semântica.

## Conclusão

A decisão mais honesta hoje é:
- **não** escolher infra distribuída pesada cedo demais;
- **sim** escolher stack híbrida simples:
  - `filesystem raw + Postgres + DuckDB`
  - `Scrapy + Dagster`
  - `Firecrawl` como suplemento documental

Essa escolha maximiza:
- reprodutibilidade;
- velocidade de validação;
- baixo custo de erro arquitetural.
