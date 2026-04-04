# /scout

Descobre papers adjacentes que a KB não contém. Olha pra fora via web search.

## Processo

1. **Identificar conceitos centrais dos artigos de síntese:**
   Leia wiki/concepts/ e selecione artigos com interpretation_confidence:medium ou low.
   Para cada um, extraia os 2-3 conceitos centrais que definem o artigo.

2. **Gerar queries de busca:**
   Para cada conceito, gere 2-3 queries:
   - "[conceito] arxiv 2024 2025 2026"
   - "[conceito] survey OR benchmark site:arxiv.org"
   - "[conceito] limitations OR criticism"

3. **Web search + triagem:**
   Rode web search. Para cada resultado:
   - Já existe em raw/papers/? Se sim, skip.
   - É paper primary (arxiv, conference, journal)? Descartar blogs/tweets.
   - Cobre terreno similar a algum artigo de síntese?
   - Potencialmente invalida, confirma ou refina algum claim?

4. **Rankear candidatos:**
   Priorize por:
   a. Papers que INVALIDAM claims de síntese (maior valor epistêmico)
   b. Papers que REFINAM claims com dados novos
   c. Papers que CONFIRMAM com evidência independente
   d. Surveys recentes que cobrem o mesmo terreno

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

6. **NÃO ingira automaticamente.**
   Reporte candidatos. Usuário decide quais ingerir.

## Quando rodar

- Antes de publicar qualquer síntese (LinkedIn post, report externo)
- Mensalmente como manutenção
- Quando /challenge encontrar "Prior work não verificado"
- Após ingerir 5+ papers novos (o landscape pode ter mudado)

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
