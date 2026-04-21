# /scout

Descobre papers adjacentes que a KB não contém. Usa arxiv MCP como fonte primária.

## Processo

1. **Identificar conceitos centrais dos artigos de síntese:**
   Leia wiki/concepts/ e selecione artigos com interpretation_confidence:medium ou low.
   Para cada um, extraia os 2-3 conceitos centrais que definem o artigo.

2. **Gerar queries de busca:**
   Para cada conceito, gere 2-3 queries para usar em `search_papers`:
   - "[conceito] survey" com date_from: ano-2 até hoje
   - "[conceito] benchmark" com categorias relevantes (cs.AI, cs.LG, cs.CL etc.)
   - "[conceito] limitations OR failure" sem filtro de categoria

3. **Busca via arxiv MCP + triagem:**
   Para cada query, chame `search_papers` (arxiv MCP).
   Para conceitos fora do escopo arxiv (ex: economia, biologia), use web search como fallback.
   Para cada resultado:
   - Chame `list_papers` para verificar se o arXiv ID já está em raw/papers/ — se sim, skip.
   - Cobre terreno similar a algum artigo de síntese?
   - Potencialmente invalida, confirma ou refina algum claim?

4. **Rankear candidatos:**
   Priorize por:
   a. Papers que INVALIDAM claims de síntese (maior valor epistêmico)
   b. Papers que REFINAM claims com dados novos
   c. Papers que CONFIRMAM com evidência independente
   d. Surveys recentes que cobrem o mesmo terreno

4.5. **Citation expansion (top 3 candidatos):**
   Para cada um dos top 3 do ranking, chame `citation_graph` (arxiv MCP).
   Examine referências e citantes — adicione ao ranking qualquer paper que:
   - Contradiga claims existentes no wiki
   - Seja survey do mesmo terreno com cobertura maior
   Limite: max 3 candidatos extras via citation_graph (não inflar o pool).

5. **Salvar report:**
   Gere outputs/reports/scout-YYYY-MM-DD.md com:

   ```
   # Scout Report — YYYY-MM-DD

   ## Artigos de síntese analisados
   - [artigo]: conceitos buscados

   ## Candidatos a ingestão (rankeados)

   ### 1. [Título do paper]
   - URL: arxiv.org/abs/XXXX
   - Relevante para: [artigo wiki]
   - Impacto: INVALIDA | REFINA | CONFIRMA
   - Claim afetado: "[texto do claim]"
   - Justificativa: [por que esse paper importa]

   ### 2. ...

   ## Já presente na KB (skip)
   - [papers encontrados que já estão em raw/]

   ## Descartados
   - [papers irrelevantes + motivo]
   ```

6. **Baixar e ingerir os top 2-3 candidatos (prioridade ALTA/MÉDIA) após o relatório.**
   Para cada candidato, chame `download_paper` (arxiv MCP) com o arXiv ID.
   O arquivo vai para `raw/papers/` automaticamente (ARXIV_STORAGE_PATH configurado).
   Depois, rode /ingest nestes arquivos sem confirmação.
   Reportar o que foi baixado e ingerido ao final.

## Quando rodar

- Antes de publicar qualquer síntese (LinkedIn post, report externo)
- Mensalmente como manutenção
- Quando /challenge encontrar "Prior work não verificado"
- Quando `fast_cycle.ingest_count_since_last_scout >= 10` em kb-state.yaml

## Utility Analysis (roda junto com scout periódico)

Para cada artigo em wiki/concepts/, leia frontmatter e calcule:

`utility_score = retrievals_correct / reads` (se reads = 0: null)

Classifique:

| Perfil | Condição | Ação |
|--------|----------|------|
| ALTO USO + ALTA UTILIDADE | reads >= 5, utility >= 0.7 | Hub article — /challenge prioritário (erros propagam) |
| ALTO USO + BAIXA UTILIDADE | reads >= 5, utility < 0.3 | Consultado mas não ajuda — /review conteúdo ou retrieval? |
| BAIXO USO | reads < 3 | Subutilizado — verificar ponteiro no _index.md |
| NUNCA LIDO | reads = 0 | Candidato a remoção ou melhoria de ponteiro |
| ALTO GAP | retrievals_gap >= 3 | Existe mas retrieval não chega — melhorar ponteiro ou wikilinks |

Salve análise em `outputs/reports/utility-YYYY-MM-DD.md`

---

## Pipeline — kb-state.yaml

### Lê (início)
- `fast_cycle.ingest_count_since_last_scout` — para contextualizar escopo do scout (quanto mudou desde o último)
- `slow_cycle.emerge.top_pairs` — se /emerge identificou pares com alto potencial, inclua os artigos desses pares no escopo da busca
- `challenge.recent_verdicts` — artigos com prior_work_found=true são candidatos prioritários para scout

### Escreve (final)
```yaml
updated: YYYY-MM-DD
fast_cycle:
  ingest_count_since_last_scout: 0  # reset
slow_cycle:
  scout:
    last_run: YYYY-MM-DD
    candidates_pending:
      - title: [título]
        url: [url]
        impact: INVALIDA | REFINA | CONFIRMA
        article: [artigo wiki afetado]
```

### Gatilhos — verifique ao final

| Condição | Gatilho |
|----------|---------|
| `candidates_pending` contém artigos com `impact: INVALIDA` | `⚠️ /ingest urgente — paper encontrado que invalida claim. Artigo: [nome]` |
| Artigo com `provenance: emergence` tem prior work que subsome | `⚠️ /challenge [artigo] — prior work pode subsumir emergência. Verifique antes de publicar.` |
| Utility analysis revela artigos com `reads=0` e in-degree ≥5 | `💡 Hub não utilizado: [artigo]. Melhore ponteiro em _index.md.` |
