# Firecrawl para ingestão documental do Zelox

source: https://docs.firecrawl.dev/features/crawl
fetched: 2026-04-09
type: article
notes: >
  Avaliação pragmática de Firecrawl como camada de crawl/scrape/extract para
  ingestão documental. Foco: se vale a pena para o Zelox, não benchmark geral
  de web scraping.

---

## O que Firecrawl oferece

### 1. `crawl`

Recursivamente descobre e raspa subpáginas de um site, lidando com sitemap,
 JS rendering e rate limiting, com retorno por polling, WebSocket ou webhook.

### 2. `scrape`

Converte uma URL em markdown/html/structured outputs e suporta:
- páginas dinâmicas;
- PDFs;
- screenshots;
- `actions` para navegação/interação.

### 3. `extract`

Executa extração estruturada guiada por prompt/schema sobre uma ou mais URLs.
Também aceita wildcard de domínio e pode expandir a busca com `enableWebSearch`.

## O que isso resolveria no Zelox

Firecrawl é potencialmente útil para:
- camada documental fora do PNCP estruturado;
- páginas/portais com HTML ruim ou JS pesado;
- coleta de atas, notices, portais de TCE, juntas e conselhos;
- protótipos rápidos de `crawl -> markdown -> claim extraction`.

## Onde ele ajuda muito

- descoberta rápida de links (`/map`);
- scrape de portais heterogêneos sem escrever crawler dedicado cedo demais;
- captura de markdown limpo para RAG/evidência;
- jobs assíncronos com polling/webhook;
- crawling de domínio pequeno/médio com pouca infraestrutura própria.

## Onde ele NÃO substitui a stack principal

### 1. Não substitui loaders oficiais

Se existe API/dataset oficial estável (`PNCP`, `Portal`, `Compras.gov`,
 `Transferegov`), Firecrawl não deveria ser a camada principal.

### 2. `extract` ainda é beta/experimental

O endpoint `/extract` é poderoso, mas a própria doc marca limitações:
- cobertura imperfeita em sites grandes;
- inconsistências entre execuções;
- feature ainda em beta/alpha em partes.

### 3. Não resolve governança/freshness por si

Firecrawl pode acelerar coleta, mas não resolve:
- lineage institucional;
- contratos de schema;
- staleness policy;
- política factual vs inferencial.

## Veredicto para o Zelox

Vale a pena como:
- `enrichment crawler`
- `document acquisition layer`
- `rapid crawler for heterogeneous portals`

Não vale como:
- backbone primário de ingestão dos sistemas P0.

## Regra prática

- usar `API oficial > download oficial > scraper dedicado > Firecrawl`
- Firecrawl entra onde a alternativa seria ficar sem dado ou demorar demais para
  construir crawler especializado.
