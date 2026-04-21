# DuckDB com CNPJ da Receita Federal — caso brasileiro

source: https://medium.com/@guilherme-oliveira/empowering-local-large-dataset-data-analysis-with-duckdb-case-study-on-brazilian-companies-5cab4c6e8bea
fetched: 2026-04-09
type: article
notes: >
  Fonte secundária/anecdotal, mas com alto valor contextual porque usa exatamente
  a base P0 do Zelox: CNPJ/QSA da Receita Federal.

---

## Por que importa

Mesmo sendo blog/Medium, esta é uma rara evidência prática usando a base certa:
- CNPJ/RFB;
- volume brasileiro;
- análise local com DuckDB.

## Valor para o Zelox

- confirma aderência operacional da stack ao dado brasileiro que o produto vai usar;
- reduz o risco de escolher ferramenta só com benchmark abstrato;
- reforça DuckDB como camada de exploração e preparação analítica local.

## Limite epistemológico

Não deve ser tratada como prova arquitetural principal.

Uso correto:
- `confirmatory anecdote`

Não uso correto:
- base única para decidir storage de produção.
