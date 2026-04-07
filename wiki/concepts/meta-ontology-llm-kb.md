---
title: "Meta-Ontologia do metaxon — Upper, Domain e Pipeline"
sources:
  - path: wiki/concepts/formal-ontology-for-kbs.md
    type: article
    quality: primary
    stance: confirming
  - path: wiki/concepts/viable-system-model-beer.md
    type: article
    quality: primary
    stance: confirming
  - path: wiki/concepts/upper-ontology-for-kbs.md
    type: article
    quality: primary
    stance: confirming
  - path: wiki/concepts/neurosymbolic-ai-for-kbs.md
    type: article
    quality: primary
    stance: confirming
created: 2026-04-07
updated: 2026-04-07
tags: [ontology, meta-kb, class-hierarchy, pipeline, bfo, vsm, algedonic, pydantic]
source_quality: high
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: synthesis
synthesis_sources:
  - wiki/concepts/formal-ontology-for-kbs.md
  - wiki/concepts/viable-system-model-beer.md
  - wiki/concepts/upper-ontology-for-kbs.md
  - wiki/concepts/neurosymbolic-ai-for-kbs.md
quarantine: true
quarantine_created: 2026-04-07
quarantine_reason: "síntese nova — hierarchy and pipeline mappings are compiler interpretations, not direct claims from sources; 24h + challenge adversarial required"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: null
epistemic_status: L1
---

## Resumo

Este artigo descreve a meta-ontologia do metaxon em três camadas: (1) upper ontology baseada em BFO que distingue continuantes (artigos, conceitos) de ocorrentes (sessões, events); (2) domain ontologies específicas do KB (KnowledgeArtifact, Claim, DisturbanceEvent); (3) mapeamento entre schema Pydantic (`ontology/core.py`) e os 4 Gates do pipeline de promoção. O VSM de Beer fundamenta o canal algedônico; Luong 2026 justifica o grounding ontológico onde o LLM tem cobertura fraca.

## Conteúdo

### 1. Upper Ontology Transversal (BFO como fundação)

A upper ontology usa a divisão BFO (Basic Formal Ontology) como fundação, replicada de [[upper-ontology-for-kbs]] e [[formal-ontology-for-kbs]]:

```
Entity (BFO:top)
├── Continuant — existe integralmente a qualquer momento
│   ├── MaterialEntity — existência física
│   │   └── (não aplicável ao KB digital)
│   ├── ImmaterialEntity — existência informacional
│   │   └── KnowledgeArtifact  ← ponto de entrada do domain
│   └── Quality — propriedade de continuante
│       ├── SourceQuality (HIGH|MEDIUM|LOW)
│       └── InterpretationConfidence (HIGH|MEDIUM|LOW)
│
└── Occurrent — desdobra-se no tempo
    ├── Process — tem partes temporais
    │   ├── IngestSession
    │   ├── AskSession
    │   ├── PromoteGating
    │   └── EmergenceProcess
    └── SpatiotemporalRegion
        └── DisturbanceEvent  ← ocorrente com localização temporal
```

**Gap que esta divisão resolve:** o KB historicamente tratou tudo como continuante (artigos estáticos). Sessões de /ask, ciclos de /ingest e /promote são OCCURRENTs com início, fim, entradas e saídas. Sem essa distinção, não há como rastrear quais artigos foram usados em qual /ask, quando, e com que resultado.

### 2. Domain Ontologies — Hierarquia KB-específica

A hierarquia domain estende BFO com entidades próprias do metaxon:

#### 2.1 KnowledgeArtifact (continuante)

```
KnowledgeArtifact
├── Source            — raw/, imutável; instância de IngestSession
└── Article           — wiki/, derivado; instância de PromoteGating
    ├── SourceArticle        (provenance: source)
    ├── SynthesisArticle     (provenance: synthesis)
    └── EmergenceArticle     (provenance: emergence)
        ├── L1 — confirma hipótese com evidência cross-paper
        ├── L2 — propõe mecanismo novo com falsificador
        └── L0 — conjecture sem raw/ (requer promoção manual)
```

Invariante implementada em `ontology/core.py`:
- `EmergenceArticle` exige `emergence_trigger: {pair, connection_type, pearl_level}`
- `L0` nunca entra em /auto-promote (Gate 1 permanente bloqueado)

#### 2.2 Claim (continuante, parte de Article)

```
Claim
├── FactualClaim      — direto da fonte; sem ⚠️
├── VerifiedClaim     — confirmado por 2+ fontes independentes
├── InterpretedClaim  — síntese do compilador; marcado ⚠️
└── EmergentClaim     — emerge de cross-domain; marcado ⚠️; candidato a novo Article
```

A distinção FactualClaim vs InterpretedClaim é a base da disciplina de escrita do CLAUDE.md: "⚠️ nossa interpretação" em InterpretedClaims e EmergentClaims.

#### 2.3 DisturbanceEvent (ocorrente)

```
DisturbanceEvent (BFO Occurrent)
├── type: DisturbanceType  — RETRIEVAL_FAILURE | L1_CONTRADICTION | QUARANTINE_REPEAT
│                          | CROSS_SESSION_DRIFT | GATE_FAILURE | QUARANTINE_STALE
├── severity: SeverityLevel  — DERIVED (nunca input); MEDIUM|HIGH|CRITICAL
└── bypass_s3: bool         — DERIVED; true = canal algedônico S5 direto (Beer VSM)
```

Invariante: `severity` e `bypass_s3` são sempre derivados por `DisturbancePolicy.rules` via `model_validator(mode='before')` — impossível injetar valores incorretos.

### 3. Herança e Invariantes (ontology/core.py)

O schema Pydantic em `ontology/core.py` implementa as invariantes da hierarquia. Mapeamento entre classes ontológicas e implementação:

| Classe ontológica | Pydantic class | Invariante enforçada |
|-------------------|----------------|---------------------|
| KnowledgeArtifact | `KnowledgeArtifact` | `provenance` obrigatório; `emergence_trigger` se emergence |
| EmergenceArticle L0 | `KnowledgeArtifact` | `epistemic_status=L0` → `quarantine=true` permanente |
| Claim | `Claim` | `confidence ∈ [0.0, 1.0]` |
| DisturbanceEvent | `DisturbanceEvent` | severity/bypass_s3 sobrescritos via `mode='before'` |
| AlgedonicChannel | `AlgedonicPolicy` | `emit()` é único factory; `can_auto_resolve()` → False para CRITICAL |
| ResolutionSignal | `ResolutionSignal` | `source_diversity ≥ 0`; `confidence_by_domain ∈ [0.0, 1.0]` |

**Hierarquia de resolução** (Beer VSM Subsidiarity):
```
STIGMERGIC → resolve local, sem perturbação externa (confidence ≥ 0.8 AND diversity ≥ 3)
SUBSIDIARY → precisa ferramenta externa (/ask, /scout) mas não emergência S5
ALGEDONIC  → bypass S3/S4 direto para S5 (has_contradictions = True OR severity = CRITICAL)
```

### 4. O que Prometheus Adiciona ao VSM

Beer VSM descreve S1-S5 sem especificar o conteúdo epistêmico dos sinais. O metaxon ("Prometheus") acrescenta:

| VSM Beer | Gap original | Prometheus preenche |
|----------|-------------|---------------------|
| S1 — Operational | "o que aconteceu" (sem tipagem) | `FactualClaim` com rastreabilidade a raw/ |
| S2 — Coordination | anti-oscilação entre S1s | Bradford quota (max 25% challenging) previne semantic convergence |
| S3 — Operational mgmt | variety engineering local | Gates 1-4 como filtro de variety; promote = amplificação controlada |
| S4 — Intelligence | sensing do ambiente | `/scout`, `/foresight` — hipóteses sobre domínios não cobertos |
| S5 — Policy | identidade e valores | Canal algedônico: recebe `bypass_s3: true` events diretamente |

Beer não previu claims tipados. VSM fala de "variety" de forma abstrata. A distinção `FactualClaim` vs `InterpretedClaim` vs `EmergentClaim` é o que permite ao S3 avaliar a qualidade da variety que S1 produz — não apenas quantidade.

**Adição específica de Luong 2026 ([[neurosymbolic-ai-for-kbs]]):** o grounding ontológico tem valor inversamente proporcional à cobertura paramétrica do LLM. Para este KB, isso justifica tipagem explícita de claims em domínios Zone 3 (procurement, B2G, organizational design) — justamente onde o LLM tem menos treino.

### 5. Acoplamento Estrutural na Ontologia

(⚠️ nossa interpretação — sem raw/ direto de Maturana. Ver [[structural-coupling-maturana]] para a hipótese completa.)

A meta-ontologia implica uma forma de acoplamento estrutural com o LLM que a usa:

- O LLM perturba a KB via /ask (queries que expõem gaps)
- A KB perturba o LLM via search results (altera o estado interno do LLM por retrieval)
- Nenhum controla o outro — ambos mantêm autopoiese: o LLM via pesos, a KB via gates

A evidência de acoplamento saudável é co-evolução: o número de EmergentClaims cresce, a taxa de retrieval_failure cai, os domínios cobertos expandem. A evidência de patologia: removal test — remover a KB piora a qualidade das respostas do LLM (dependência real, não cosmética).

**Critério operacional de saúde da ontologia:**
```
Sinal verde: articles_promoted / articles_quarantined > 0.6
Sinal amarelo: ratio 0.3–0.6 (gates bloqueando mas pipeline fluindo)
Sinal vermelho: ratio < 0.3 OU algedonic_events[bypass_s3=true] > 0 não resolvidos
```

## Interpretação

(⚠️ nossa interpretação)

A meta-ontologia resolve o paradoxo que toda KB enfrenta: quanto mais estruturada, mais rígida; quanto mais fluída, menos rastreável. A solução aqui é **separar planos**:

- **Plano continuante** (artigos, conceitos): estrutura explícita via class hierarchy e typed claims
- **Plano ocorrente** (sessões, events): rastreabilidade temporal via DisturbanceEvent e logs
- **Plano invariante** (regras de derivação): implementação Pydantic que torna violações impossíveis, não apenas detectáveis

O resultado é uma KB que sabe *o que não sabe* (gaps explícitos via retrieval_failure), *quando deixou de saber* (DisturbanceEvent com timestamp), e *por que* (evidence list no evento). Beer chamaria isso de variety engineering do próprio regulador.

## Conexões

- [[formal-ontology-for-kbs]] — BFO, gaps de class hierarchy, typed relations
- [[upper-ontology-for-kbs]] — hierarquia KnowledgeArtifact → Article → {Source/Synthesis/Emergence}
- [[viable-system-model-beer]] — S1-S5, variety engineering, algedonic channel
- [[neurosymbolic-ai-for-kbs]] — inverse parametric knowledge effect, Zone 3 grounding
- [[structural-coupling-maturana]] — mecanismo de co-evolução KB×LLM (⚠️ L0, sem raw/)
- [[single-brain-data-ontology]] — 4 redes epistêmicas de Hindsight (eixo ortogonal)
- [[autonomous-kb-failure-modes]] — o que acontece quando invariantes são violadas

## Fontes

- [formal-ontology-for-kbs](formal-ontology-for-kbs.md) — BFO/DOLCE/OWL2: upper ontology e typed relations
- [viable-system-model-beer](viable-system-model-beer.md) — VSM S1-S5, algedonic channel, variety engineering
- [upper-ontology-for-kbs](upper-ontology-for-kbs.md) — hierarquia de classes KB-específica, Hindsight 4 redes
- [neurosymbolic-ai-for-kbs](neurosymbolic-ai-for-kbs.md) — grounding ontológico + inverse parametric knowledge effect
