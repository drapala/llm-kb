# /verify

Testa predições L2 do corpus contra dados externos.
É o oracle de longo prazo: o mundo real valida (ou invalida) as hipóteses emergidas.

## Quando rodar

- Mensalmente
- Após acumular >= 3 predições L2 não testadas
- Antes de publicar synthesis baseado em predições do corpus
- Quando dados novos se tornam disponíveis (PNCP update, novo paper, resultado de experimento)

## Passo 1 — Coleta predições

Lê todos os artigos em `wiki/concepts/` com `provenance: emergence` ou
`interpretation_confidence: low` que contenham seção `## Verificação adversarial`.

Para cada artigo, extrai:
- Texto da predição (geralmente "Evidência que confirmaria / Evidência que refutaria")
- Pearl level declarado
- Data de criação
- Status atual: `untested | confirmed | refuted | partially_confirmed`

Lê `outputs/reports/predictions-ledger.md` para verificar quais já foram testadas.

## Passo 2 — Classifica por testabilidade

Para cada predição não testada, classifica:

| Tipo | Exemplo | Dados necessários | Testável agora? |
|------|---------|------------------|-----------------|
| **PNCP/Zelox** | "contratação integrada tem menor taxa de aditivo_teto" | Query PNCP por modalidade | Sim (ver Passo 3a) |
| **Bibliométrico** | "autoresearch sem oracle externo confirma >80%" | Rodar experimento | Não — placeholder |
| **Literário** | "multiagent debate mitiga self-enhancement" | Du et al. ingerido? | Verificar ingest_queue |
| **Empírico externo** | "efeito de prefeito em último mandato" | Dados Ferraz & Finan | Sim, já em raw/ |

## Passo 3a — Testa predições PNCP (Zelox)

Para predições verificáveis no PNCP, gera a query estruturada:

```
PREDIÇÃO: contracts under contratação integrada têm taxa de aditivo_teto
          significativamente menor que contratos tradicionais de igual complexidade

QUERY PNCP:
  - Busca inicial: `GET https://pncp.gov.br/api/search?tipos_documento=contrato&q=<termo>&pagina=N`
  - Detalhe de contrato: `GET https://pncp.gov.br/api/pncp/v1/orgaos/{orgao_cnpj}/contratos/{ano}/{sequencial}`
  - Termos do contrato: `GET https://pncp.gov.br/api/pncp/v1/orgaos/{orgao_cnpj}/contratos/{ano}/{sequencial}/termos?pagina=1`
  - Chaves obtidas no search: `item_url`, `orgao_cnpj`, `ano`, `numero_sequencial`, `modalidade_licitacao_nome`
  - Campos obtidos no detalhe: `niFornecedor`, `valorInicial`, `valorGlobal`, `objetoContrato`, `categoriaProcesso`, `tipoContrato`
  - Filtros: `modalidade_licitacao_nome IN ('Contratação Integrada', 'Contratação Semi-Integrada', 'Concorrência', 'Pregão - Eletrônico', ...)`
             AND `categoriaProcesso.nome` = [mesma categoria]
             AND `valorInicial` BETWEEN [faixa]
  - Métrica operacional: `aditivo_ratio = (valorGlobal - valorInicial) / valorInicial`
  - Proxy de alerta: `COUNT(aditivo_ratio >= 0.23) / COUNT(*)`
  - Resultado esperado: `taxa_integrada < taxa_tradicional * 0.7`

STATUS: `search` + `detail` mapeados e testados em 2026-04-08; consulta pública funciona
LIMITAÇÃO: `api/search` é textual e exige pós-filtro por `detail.niFornecedor`; termos podem retornar `204`
```

Salva query em `outputs/reports/pncp-queries/[artigo]-YYYY-MM-DD.md`.
Quando dados disponíveis: rodar query, comparar com predição, atualizar ledger.

## Passo 3b — Testa predições bibliométricas

Para predições verificáveis via literatura (novo paper confirma/refuta):

```bash
# Para cada predição literária não testada:
python3 scripts/cross-model-challenge.py --mode auto << 'EOF'
{
  "article_a": {"title": "...", "summary": "[predição]", "mechanism": "..."},
  "article_b": {"title": "Prior Work Found", "summary": "[paper recente]", "mechanism": "..."},
  "proposed_connection": "Este paper confirma/refuta a predição?",
  "connection_type": "INSTANCIA",
  "pearl_level": "L2"
}
EOF
```

## Passo 4 — Atualiza ledger

Mantém `outputs/reports/predictions-ledger.md`:

```markdown
# Predictions Ledger

Última atualização: YYYY-MM-DD

## Predições ativas

### [artigo] — [predição resumida]
- Pearl level: L2
- Criada: YYYY-MM-DD
- Status: untested | confirmed | refuted | partially_confirmed
- Dados necessários: [o que falta]
- Próximo passo: [ação específica]

## Predições testadas

### [artigo] — [predição resumida]
- Resultado: confirmed | refuted
- Evidência: [o que foi testado, com link]
- Data: YYYY-MM-DD
- Impacto: [o que muda na KB se refutado]
```

## Passo 5 — Ações derivadas

Para cada predição **refutada**:
- Abre `> [!patch]` no artigo wiki correspondente com o resultado
- Adiciona entrada em `next_actions`: `/review [artigo] — predição L2 refutada`

Para cada predição **confirmada**:
- Atualiza frontmatter do artigo: `prediction_status: confirmed`
- Eleva `interpretation_confidence` se era `low` → `medium`

Para predições com `dados necessários` mapeados mas não disponíveis:
- Adiciona em `ingest_queue_priority` com `why: "necessário para verificar predição L2 de [artigo]"`

## O que /verify NÃO faz

- Não modifica claims diretamente — abre patches para revisão humana
- Não descarta predições por falta de dados — registra como "dados pendentes"
- Não substitui /challenge — /verify testa predições existentes; /challenge avalia novos claims
