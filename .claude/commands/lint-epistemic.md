# /lint-epistemic

Audita saúde epistêmica da KB. Computa 4 métricas e gera relatório.

## Passo 1 — Stance ratio por tipo de fonte

O threshold adversarial se aplica diferentemente a fontes core vs. laterais.

### Classificação core vs. lateral

Fonte é **lateral** se seus concepts no _registry.md mapeiam para qualquer artigo
da lista de domínios Zone 3:

```
heuristics-and-biases, prospect-theory, social-choice-aggregation,
complexity-stability-tradeoff, resource-competition-coexistence,
zipf-law-power-laws, falsificationism-demarcation, scientific-research-programmes,
episodic-semantic-memory, complementary-learning-systems, stigmergic-coordination,
complexity-emergence, predictive-processing, requisite-variety,
viable-system-model-beer, bibliometrics, bradford-law-scattering,
fast-frugal-heuristics, groupthink-and-cascades, immune-inspired-credit-assignment,
causal-reasoning-pearl, formal-ontology-for-kbs
```

Tudo que não mapeiar para essa lista é **core** (AI/ML + Info Theory + Meta-KB).

Quando ambíguo (e.g., fonte que alimentou tanto artigo core quanto lateral): classifique como core.

### Cálculo separado

**Fontes core:**
- Compute challenging / total_core por mês
- **Threshold de alerta:** challenging < 20% em mês com ≥5 fontes core → `⚠️ ALERTA adversarial`

**Fontes laterais:**
- Threshold de stance NÃO se aplica
- Compute Bradford Zone3/Zone2: `(fontes laterais acumuladas) / (fontes Zone 2 acumuladas)`
- **Threshold de alerta:** Zone3/Zone2 < 0.8 → `⚠️ ALERTA cobertura lateral`
- Atual referência: Zone3/Zone2 = 1.05 → pausa (não expandir Zone 3)

### Output desta seção

```
## Stance Ratio

### Fontes Core
| Mês | Confirming | Neutral | Challenging | Total | % Challenging | Status |
...

### Fontes Laterais (Bradford)
Zone3/Zone2 atual: X.XX → [expandir / pausa / ok]
```

## Passo 2 — Synthesis ratio

Para cada artigo em `wiki/concepts/*.md` (excluindo `_index*.md`):
- Conte itens em seção `### Especulação` (linhas começando com `-` dentro dessa seção)
- Conte itens em `### Descrição` + `### Interpretação` como proxy de claims totais
- Compute: speculation_items / total_items por artigo

Agregue: % de artigos com speculation_ratio > 50% (sinal de over-synthesis estrutural).

Não leia todos os arquivos de uma vez. Use Glob para listar, depois leia em lotes.
Circuit breaker: se ≥10 artigos sem seções epistêmicas (sem `### Especulação` nem `### Descrição`), note como "artigos sem níveis epistêmicos" — não tente inferir.

## Passo 3 — Quarantine rate

Da lista de artigos, conte:
- `quarantine: true` → em quarentena
- `quarantine: false` + `quarantine_promoted` preenchido → promovidos
- sem campo quarantine → não aplicável (artigos antigos)

Compute: quarantine_rate = quarentena_ativa / total_artigos

Liste artigos em quarentena com suas razões.

## Passo 4 — Hub health

De `wiki/_registry.md`, identifique artigos com `reads: 0`:
- Se `last_read` é nulo ou data < (hoje - 30 dias) → hub não utilizado

Compare com in-degree do grafo (se disponível de análise anterior).
Artigos com in-degree ≥ 5 e reads = 0 são candidatos a revisão: muito linkados mas nunca lidos diretamente via /ask.

## Passo 5 — Output

Salve em `outputs/reports/epistemic-lint-YYYY-MM-DD.md` com:

```markdown
---
date: YYYY-MM-DD
---

## Stance Ratio — Fontes Core
[tabela por mês: confirming/neutral/challenging/total/% challenging/status]
[⚠️ ALERTA se challenging < 20% em mês com ≥5 fontes core]

## Bradford Coverage — Fontes Laterais
Zone3/Zone2: X.XX → expandir (<0.8) | pausa (0.8–1.2) | ok (>1.2)
[lista de domínios Zone 3 cobertos e descobertos]

## Synthesis Ratio

[% artigos com speculation_ratio > 50%]
[lista dos 3 mais especulativos]

## Quarantine Rate

[N quarentenados / N total = X%]
[lista artigos em quarentena com razão]

## Hub Health

[N artigos com reads=0]
[destaque: hubs in-degree ≥5 com reads=0]

## Ações recomendadas

[lista priorizada baseada nos alertas]
```

## Notas

- Circuit breaker: se _registry.md tiver > 200 linhas, não leia inteiro — use Bash/awk para extrair stances
- Não modifique nenhum artigo durante o lint — é operação read-only
- Se algum metric não for computável (dados ausentes), reporte como "não mensurável" em vez de estimar
