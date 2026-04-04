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
```
