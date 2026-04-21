---
title: "Trade Secrets and AI — Reasonable Measures Requirement (Hrdy 2025)"
sources:
  - path: raw/papers/hrdy-2025-trade-secrets-ai.md
    type: legal-article
    quality: primary
    stance: confirming
created: 2026-04-20
updated: 2026-04-20
tags: [multi-tenancy, e39, nda-ip, trade-secrets, legal-doctrine, ai-training, scout-e39]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
provenance: source
quarantine: true
quarantine_created: 2026-04-20
quarantine_reason: "Ingerido via Deep Research Gap E39 (Gap 3 NDA/IP) — aguarda challenge"
download_blocked: ssrn_auth_required
download_attempt_2026_04_20: "WebFetch retornou HTTP 403; SSRN exige login para PDF. Claims atuais baseados em abstract SSRN + RIIPL 2025-09-24 secondary content. Full doctrinal verification pendente."
freshness_status: current
depends_on:
  - raw/papers/hrdy-2025-trade-secrets-ai.md
topics: [trade-secrets, ai-training, reasonable-measures, model-weights, nda-ip-compliance]
---

## Resumo

Hrdy 2025 (Rutgers Law School Research Paper; Elgar Encyclopedia chapter forthcoming) é mapeamento doutrinário compacto (7pp) da interação trade secret law × AI. Identifica que **reasonable measures requirement** (DTSA 2016 + state UTSA) é o test operacional central: sem access controls + NDA + technical barriers, protection de trade secret evapora. Categoriza training data, model weights, prompts, telemetry e fine-tuning procedures como AI-era trade secret candidates, com model weights como emerging conceito distinto de código tradicional.

## Conteúdo

### Categorias protegíveis (contexto AI)
1. Training data proprietário
2. Model weights (emerging category)
3. System prompts / prompt engineering artifacts
4. Telemetry / usage patterns agregados
5. Fine-tuning procedures / alignment pipelines

### Reasonable measures requirement (core doctrine)
Para qualificar como trade secret sob DTSA 2016 + state UTSA equivalents, a informação deve ser:
(a) economically valuable (derive independent economic value from not being generally known)
(b) not generally known / not readily ascertainable
(c) **subject to reasonable efforts to maintain secrecy**

Falha em (c) — ausência de access controls, NDA, technical barriers — pode invalidar proteção mesmo se info é objetivamente secreta. Este é o test que interessa diretamente a cross-tenant AI pipelines.

### Overlap jurisdicional
Trade secret × patent × copyright × contract são sobrepostas em AI. Contract law (NDA, MSA clauses) é frequentemente **primary defensive layer** porque patent/copyright têm cobertura limitada em training corpora e model weights.

### Evolução 2023-2025
Cases envolvendo trade secrets em AI cresceram (referenciado pela autora em Hrdy & Corsello USPTO presentation setembro 2025). Model weights emergem como conceito merecendo tratamento distinto; prior frameworks tratavam weights como derivative code, mas doutrina atual reconhece independent economic value.

## Interpretação

(⚠️ nossa interpretação) **Reasonable measures requirement transforma tenant isolation em compliance question, não apenas arquitetura.** Se claude-pipeline opera cross-tenant sem isolation, cliente A pode ser argumentado a ter falhado em "reasonable measures" (permitiu que informação proprietária fluísse para sistema compartilhado com cliente B) — **invalidando o próprio claim de trade secret de A**. Isto significa: ausência de isolation prejudica legalmente **o cliente, não apenas o pipeline**. Argumento forte para isolation-by-default como compliance feature, não feature arquitetural opcional.

(⚠️ nossa interpretação) **Model weights como trade secret relevante para E39.** Rules/lessons derivadas de codebase proprietária contêm **derivative information** de contextos/weights expostos a esses padrões. Se model weights qualificam como trade secret, derivatives deles — especialmente patterns estruturais identificáveis como signature do cliente — herdam status. Isto argumenta contra promoção cross-tenant de rules com abstraction_level=idiomatic ou codebase-specific (AC14 em V2.E39.T03 já faz esse gate).

(⚠️ design analogy) **Contract is primary layer ⇒ ADR é não-opcional.** Hrdy enfatiza que NDA/MSA clauses dominam análise. Tradução para E39 T01 constraint: ADR por deployment declarando (a) contract clauses aplicáveis, (b) reasonable measures em place, (c) trigger list para opt-out — é arquitetura-alinhada-à-doutrina, não burocracia evitável.

## Conexões
- complementa: [[enterprise-data-trade-secrets-chen-2025]] — Chen 2025 foca em enterprise data compilations; Hrdy 2025 foca em AI-specific artifacts; cobertura complementar.
- instancia: [[autonomous-kb-failure-modes]] — FM de "vazamento de contexto proprietário" ganha framing doutrinário via reasonable measures requirement.

## Fontes
- [Hrdy 2025 — Trade Secrets and AI](../../raw/papers/hrdy-2025-trade-secrets-ai.md) — Rutgers Law / SSRN 5350892; forthcoming Elgar Encyclopedia 2026. Doutrinal map; reasonable measures requirement; model weights emergent trade secret.
