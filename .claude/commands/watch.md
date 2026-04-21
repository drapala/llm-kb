# /watch <topic>

Cria vigilância recorrente sobre um tópico de pesquisa usando WebSearch nativo.
Adaptado de getcompanion-ai/feynman (MIT License) para o runtime do Claude Code.

## Passo 1 — Derivar slug e ler estado

Derive um slug curto do argumento `$ARGUMENTS` (lowercase, hífens, ≤5 palavras, sem stopwords).

Leia `outputs/state/watch-topics.yaml`. Se o slug já existe: imprima "⚠️ Watch já existe
para [slug]. Use /watch-check <slug> para rodar manualmente ou edite watch-topics.yaml
para alterar configuração." e **pare aqui**.

## Passo 2 — Plano de monitoramento

Escreva o plano em `outputs/.plans/<slug>-watch.md`:

```markdown
# Watch Plan — <slug>

## Tópico
<topic original>

## O que monitorar
- [lista: papers, acórdãos, regulações, datasets, eventos concretos]

## Sinais que importam (o que conta como "novo material")
- [ex: paper novo com dados empíricos, acórdão novo do TCU, benchmark novo]

## O que NÃO conta como novo
- [ex: posts de blog, resumos sem nova evidência, notícias sem dados]

## Queries de busca (2-3 variações)
1. "<query principal>"
2. "<query variante — site:específico ou termos alternativos>"
3. "<query de crítica/limitação>"

## Frequência
weekly | monthly

## Baseline criado em
<data>
```

Apresente o plano ao usuário. Se o usuário aprovar (ou não responder em 30s),
prossiga. Se pedir ajuste, incorpore antes de continuar.

## Passo 3 — Baseline sweep

Execute WebSearch com as 2-3 queries do plano. Se WebSearch retornar menos de 3 resultados
relevantes ou apenas snippets curtos sem conteúdo útil, use `mcp__tavily__tavily_search`
como fallback para extração de conteúdo completo. Para cada resultado relevante, extraia:
- Título
- URL
- Data de publicação (se disponível)
- 1-2 frases de resumo da relevância

Salve em `outputs/watch/<slug>-baseline.md`:

```markdown
# Watch Baseline — <slug>
**Criado em:** YYYY-MM-DD
**Topic:** <topic>
**Queries usadas:**
- "<query 1>"
- "<query 2>"

## Resultados

### 1. [Título]
- **URL:** <url>
- **Data:** <data ou "n/a">
- **Relevância:** <1-2 frases>

### 2. ...

## Total de resultados: N
## Próxima verificação: <data conforme frequência>
```

## Passo 4 — Registrar em watch-topics.yaml

Adicione o tópico em `outputs/state/watch-topics.yaml`:

```yaml
- slug: <slug>
  topic: <topic original>
  queries:
    - "<query 1>"
    - "<query 2>"
    - "<query 3 opcional>"
  frequency: weekly | monthly
  created: YYYY-MM-DD
  last_check: YYYY-MM-DD
  baseline: outputs/watch/<slug>-baseline.md
  inbox_prefix: watch-<slug>
  active: true
```

## Passo 5 — Instruções finais

Imprima:

```
✓ Watch criado: <slug>
  Baseline: outputs/watch/<slug>-baseline.md (<N> resultados)
  Config: outputs/state/watch-topics.yaml
  Frequência: <frequência>

Para ativar o check diário automático (já configurado para 09:00):
  launchctl load scripts/com.metaxon.watch.plist

Para rodar manualmente:
  bash scripts/watch-check.sh <slug>

O check escreve em outputs/inbox/ quando encontra material novo.
O METAXON detecta automaticamente na próxima sessão.
```

## Quando chamar

- `/watch <tópico>` — setup inicial de um novo tópico de monitoramento
- `bash scripts/watch-check.sh <slug>` — verificação manual
- Launchd roda `scripts/watch-check.sh` diariamente às 09:00 (via `com.metaxon.watch.plist`)
- Quando `outputs/inbox/watch-*.md` aparece na sessão → `/ingest outputs/inbox/watch-<slug>-YYYY-MM-DD.md`
