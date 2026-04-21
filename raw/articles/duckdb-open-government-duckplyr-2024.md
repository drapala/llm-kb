# DuckDB / duckplyr em Open Government Data

source: https://duckdb.org/2024/10/09/analyzing-open-government-data-with-duckplyr
fetched: 2026-04-09
type: article
notes: >
  Post oficial da DuckDB Foundation sobre análise de dado governamental aberto.
  Relevância para o Zelox: prova de ergonomia/viabilidade de trabalhar com
  arquivos grandes e joins dimensionais sem infraestrutura distribuída.

---

## Cenário do artigo

O artigo usa um dataset governamental aberto da Nova Zelândia com:
- arquivo principal CSV grande (~800 MB);
- múltiplas tabelas de dimensão;
- padrão tipo star schema;
- necessidade explícita de vários joins.

## O que interessa para o Zelox

### 1. DuckDB lida bem com arquivos grandes diretamente

O artigo mostra leitura streaming de CSV e consulta direta sobre arquivos, sem
 necessidade de carregar tudo em RAM de forma ansiosa.

Para o Zelox isso importa porque boa parte do trabalho inicial será:
- validar joins;
- explorar snapshots brutos;
- medir cobertura e inconsistência;
- sem precisar operar um cluster.

### 2. Joins dimensionais em dado público aberto

O exemplo é quase uma caricatura útil do nosso problema:
- arquivo factual grande;
- arquivos de lookup/dimensão;
- limpeza;
- filtros empurrados para baixo;
- agregação final.

Isso reforça que DuckDB é boa escolha para:
- prototipagem analítica;
- validação de join;
- exploração local;
- testes de cobertura antes de persistir tudo.

### 3. Lazy execution + pushdown são mais relevantes que "banco da moda"

O texto mostra um ganho forte de ergonomia e execução por conta de construção
 lazy do plano, pushdown de filtros e leitura só das colunas usadas.

No contexto Zelox:
- isso é muito mais valioso agora do que decidir sistema distribuído.

## Limites

- o artigo não prova operação multiusuário;
- não prova latência de produto compartilhado;
- não responde concorrência de escrita operacional;
- não substitui `Postgres` como core transacional.

## Tradução prática

DuckDB parece excelente para:
- `join validation`;
- analytics local;
- desenvolvimento;
- exploração de snapshots brutos;
- batchs analíticos menores.

Não é evidência suficiente para:
- fazer dela a única base operacional do produto.
