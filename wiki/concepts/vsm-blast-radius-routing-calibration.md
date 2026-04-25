---
title: "VSM-Grounded Blast-Radius Routing — Calibração como Variety Attenuation S1"
sources:
  - path: wiki/concepts/specification-grounded-review.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/viable-system-model-beer.md
    type: synthesis
    quality: primary
created: 2026-04-23
updated: 2026-04-23
tags: [vsm, blast-radius, routing, variety-attenuation, code-review, pre-pr-review, ashby]
source_quality: medium
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: true
quarantine_created: 2026-04-23
quarantine_reason: "Artigo emergido de /ask cross-domain — aguarda confirmação adversarial e review frio"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
provenance: emergence
emergence_trigger:
  pair: [specification-grounded-review, viable-system-model-beer]
  ask_session: outputs/logs/sessions/2026-04-23/ask-emerge-pairs.md
  connection_type: ANÁLOGO-A
  pearl_level: L2
emerged_on: 2026-04-23
topics: [vsm, blast-radius, routing-calibration, variety-attenuation, pre-pr-review, code-review]
---

## Resumo

Blast-radius routing em pipelines de pre-PR review implementa variety attenuation do VSM: os thresholds da routing table (pagerank, community count, entry points) são os parâmetros que definem o que S1 (mechanical check) absorve autonomamente e o que escala para S3/S4 (full pipeline). A calibração do pipeline — qual threshold define quando rodar cross-file-invariants — é equivalente a encontrar o setpoint de variety attenuation do S1. O pior erro de calibração é injetar o fingerprint topológico completo no subagent LLM, misturando as camadas S1 e S4 e causando attention dilution.

## Conteúdo

### O que viable-system-model-beer contribui

Beer (1974): sistemas viáveis sobrevivem via combinação de atenuação de variety (reduzir V(D)) e amplificação de variety (aumentar V(R)), recursivamente em múltiplos níveis. S1 (operações) absorve distúrbios localmente; S3 (controle) coordena quando S1 é insuficiente; S4 (inteligência) adapta o sistema; S5 (política) define identidade. "Variety não absorvida pela função central DEVE ser absorvida por função descentralizada — por Ashby's Law, variety tem que ir para algum lugar." Autonomia de S1 requer modelos explícitos de quais distúrbios pertencem a cada nível.

### O que specification-grounded-review / agentic-codebase-enforcement-patterns contribuem

Blast-radius fingerprint de um PR: N símbolos modificados, pagerank máximo, número de comunidades tocadas, entry points, ADR hits. Routing table: baixo blast (≤3 símbolos, sem entry points, pagerank < 0.2) → apenas mechanical; alto blast (entry points, ≥3 communities, pagerank ≥ 0.5) → full pipeline. Cada camada adicional (cross-file-invariants, fresh-eyes-pr, spec-compliance-audit) tem custo computacional e tempo — não devem ser rodadas desnecessariamente.

### O que emerge da combinação

(⚠️ nossa interpretação) O mapeamento VSM → blast-radius routing é funcional: S1 = mechanical check (linting, type errors, diff-only review); S3 = cross-file-invariants + test-rubric-audit (coordenação cross-módulo); S4 = fresh-eyes-pr + spec-compliance (inteligência, adaptação ao contexto arquitetural); S5 = docs-coherence-audit (garantia de ADR alignment = identidade do sistema).

(⚠️ nossa interpretação) Os thresholds da routing table (pagerank ≥ 0.5, ≥3 communities, entry point touch) são literalmente os parâmetros de variety attenuation do S1. Eles definem quais "distúrbios" (tipos de PR) S1 pode absorver sem escalar. Calibrar os thresholds = calibrar o setpoint do S1. Beer é explícito: autonomia de S1 requer modelos explícitos — sem tabela de routing explícita, não é possível distinguir o que é autonomia de S1 e o que requer S3.

(⚠️ nossa interpretação) O erro de injetar o fingerprint topológico completo (pagerank, reverse edges, communities) no subagent LLM é um erro de design VSM: ele mistura S1 (routing decision) com S4 (review content) na mesma camada, causando exatamente a attention dilution documentada por Kumar 2026. A separação correta é VSM-nativa: blast-radius decide qual S-level ativa, mas cada S-level recebe apenas o contexto mínimo necessário para sua função específica.

## Especulação

- PRs roteados ao full pipeline que não geram findings além do mechanical indicam que o setpoint de S1 está subcalibrado (muito baixo) — calibrável com dados de produção
- A proporção de PRs em cada tier (mechanical-only vs. full pipeline) deve seguir uma distribuição power-law pelo blast radius — análogo à distribuição de variety nos sistemas de Beer
- O custo ótimo por PR (em tokens/tempo de LLM) é minimizado quando os thresholds de S1 são calibrados exatamente ao ponto onde cross-file-invariants começa a gerar findings > 0

## Verificação adversarial

**Pergunta falsificável:** PRs roteados ao full pipeline com zero findings além do mechanical devem diminuir à medida que o threshold de blast-radius é calibrado upward. Se >20% dos full-pipeline PRs têm zero findings adicionais, o threshold atual está muito baixo.

**Evidência que confirmaria:** Dados de produção do pipeline mostrando taxa de "zero findings além de mechanical" por tier de blast-radius.

**Evidência que refutaria:** Full-pipeline PRs têm taxa de findings adicionais uniforme independente do blast-radius — sugerindo que blast-radius não prediz a necessidade de camadas extras, tornando a routing table ineficaz.

## Conexões

- emerge-de: [[specification-grounded-review]] ON "blast-radius como roteador de qual camada de review ativar"
- emerge-de: [[viable-system-model-beer]] ON "S1→S5 como hierarquia de variety attenuation com autonomia local"
- implica-em: [[attention-dilution-llm-context]] — separação S1/S4 evita injeção de contexto topológico no LLM
- partOf: [[agentic-codebase-enforcement-patterns]] — formaliza o design space da routing table

## Fontes

- [[specification-grounded-review]] — blast-radius routing, pré-PR review pipeline, routing table
- [[viable-system-model-beer]] — Beer 1974, S1→S5, variety attenuation, autonomia com modelos explícitos
- [Log /ask 2026-04-23](../../outputs/logs/sessions/2026-04-23/ask-emerge-pairs.md) — sessão que confirmou a conexão

> ⚠️ QUARENTENA: artigo emergido de /ask cross-domain. Critérios pendentes: tempo (24h), review frio, adversarial.
