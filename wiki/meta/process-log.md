# Process Log Schema

## Por que isso existe

A KB documenta entidades (continuants). Este schema documenta processos (occurrents) — o que acontece quando a KB é usada. Sem esse registro, não é possível saber quais artigos foram úteis, quais retrievals falharam, ou quais respostas foram corretas. É o pré-requisito de qualquer mecanismo de learning-from-experience.

## Occurrents registrados

### /ask session
```yaml
session_id: [timestamp-uuid]
date: YYYY-MM-DD HH:MM
query: "[pergunta exata]"
articles_read: [lista de wiki/ lidos]
articles_read_but_unused: [lidos mas não usados na resposta]
raw_sources_verified: [lista de raw/ consultados]
response_confidence: high|medium|low
retrieval_gaps: [artigos que deveriam ter sido consultados mas não foram]
synthesis_type: association|contradiction|gap|mechanism|scale|abduction|frontier|absence|falsification|sufficiency
output_saved: [caminho se salvo, null se não]
follow_up_flags: [claims a /challenge, perguntas para /ask dedicado]
```

### /ingest run
```yaml
session_id: [timestamp-uuid]
date: YYYY-MM-DD HH:MM
source_file: [raw/ ingerido]
article_created: [wiki/ gerado ou atualizado]
article_action: created|updated
quality_gate_results:
  wikilinks_typed: N
  claims_qualified: N
  meta_kb_moved: N
  resumo_altered: sim|não
ontology_proposals: [lista de tipos novos propostos]
cross_reference_results: [artigos de síntese afetados]
```

### /review run
```yaml
session_id: [timestamp-uuid]
date: YYYY-MM-DD HH:MM
article: [wiki/ revisado]
trigger: manual|scheduled|challenge-flag|ingest-conflict|audit|ontology-violation
changes:
  - type: factual|epistemic|ontological|structural
    before: "[claim anterior]"
    after: "[claim corrigido]"
    reason: "[por que mudou]"
propagation_check: [artigos afetados downstream]
net_epistemic_change: "[direção da correção]"
```

### /challenge run
```yaml
session_id: [timestamp-uuid]
date: YYYY-MM-DD HH:MM
article: [wiki/ desafiado]
claims_challenged: N
claims_survived: N
claims_weakened: N
claims_invalidated: N
prior_work_found: [lista de papers encontrados via web search]
verdict: solid|needs-revision|speculative-unmarked
```

## Campos obrigatórios vs opcionais

**Obrigatórios**: session_id, date, tipo de operação
**Opcionais**: tudo mais — log parcial é melhor que log ausente

## Localização dos logs

```
outputs/logs/sessions/YYYY-MM-DD/
  ask-HH-MM.md
  ingest-[source-slug]-HH-MM.md
  review-[article-slug]-HH-MM.md
  challenge-[article-slug]-HH-MM.md
  promote-[article-slug]-HH-MM.md
```

## Quarantine Protocol

Inspired by Janis' "second-chance meeting" prescription: synthesis articles need cooling-off time before being linked by other articles. Prevents groupthink cascade where hot-context synthesis crystallizes before critical evaluation.

### Quando um artigo entra em quarentena

Artigos de síntese com interpretation_confidence: low ou medium entram em quarentena quando criados.

**Trigger automático no /ingest:** se o artigo gerado contém seção "## Níveis epistêmicos" com mais de 3 items em "### Especulação" → `quarantine: true` automático.

### Critérios de promoção (TODOS obrigatórios)

**CRITÉRIO 1 — Tempo:** Mínimo 24h após `quarantine_created`. Janis: "second-chance meeting" — give time for residual doubts to surface.

**CRITÉRIO 2 — Review frio:** /review rodado em sessão DIFERENTE da que criou o artigo. Evidência: log em outputs/logs/sessions/ com data diferente de quarantine_created.

**CRITÉRIO 3 — Um dos três (documentar qual):**
- a) /challenge externo não destruiu claim central (verdict: solid ou needs-revision, não destroyed)
- b) /scout não encontrou paper que subsume >80%
- c) Predição falsificável formulada com nível Pearl L2 mínimo

### Frontmatter de quarentena

```yaml
quarantine: false          # true quando em quarentena
quarantine_created: null   # data de entrada
quarantine_reason: null    # por que entrou
quarantine_promoted: null  # data de promoção (se promovido)
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
```
