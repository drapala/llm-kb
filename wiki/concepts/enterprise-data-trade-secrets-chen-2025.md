---
title: "Enterprise Data como Trade Secrets — Três Categorias (Chen 2025)"
sources:
  - path: raw/papers/chen-2025-enterprise-data-trade-secrets.md
    type: legal-article
    quality: primary
    stance: confirming
created: 2026-04-20
updated: 2026-04-20
tags: [multi-tenancy, e39, nda-ip, trade-secrets, enterprise-data, comparative-law, scout-e39]
source_quality: high
interpretation_confidence: medium
resolved_patches:
  - date: 2026-04-20
    original: "Post-PDF verification completa. Stub não requer correções substantivas."
    replacement: "PDF completo (2674 linhas via pdftotext) confirma: 3 categorias na TOC; Compulife 959 F.3d 1288 (11th Cir. 2020); DTSA 2016; Directive 2016/943; Anti-Unfair Competition Law 2019. Nota editorial: paper cita seu próprio ano de publicação como 'Fall 2025 / 29 Stan. Tech. L. Rev. 1 (2026)' — há ambiguidade entre data SSRN 2025-06-12 e data de print (2026). Mantém citation year 2025 (SSRN post), mas publicação formal é 2026."
    source: "Post-PDF verification."
provenance: source
quarantine: true
quarantine_created: 2026-04-20
quarantine_reason: "Ingerido via Deep Research Gap E39 (Gap 3 NDA/IP) — aguarda challenge"
freshness_status: current
depends_on:
  - raw/papers/chen-2025-enterprise-data-trade-secrets.md
topics: [enterprise-data, trade-secrets, comparative-jurisdictions, semi-public-compilations, reasonable-steps]
---

## Resumo

Chen 2025 (Stanford Tech Law Review, vol. 29) propõe taxonomia de três categorias de enterprise data qualificáveis como trade secret: (1) **confidential enterprise data**, (2) **private data compilations**, (3) **semi-public enterprise data compilations** — com front-end públicas mas back-end privadas. Compara jurisdições US/China/EU e critica normativamente a proteção da categoria 3, argumentando que Compulife standard é overly lenient quando scraping technology é factored in, e que extensão da proteção incentiva arms race ineficiente.

## Conteúdo

### Taxonomia (três categorias)
1. **Confidential enterprise data** — fully private, access-controlled (client lists, internal metrics, proprietary research).
2. **Private data compilations** — agregados privados derivados de operações internas (usage telemetry, analytics aggregates, behavior patterns de clientes corporativos).
3. **Semi-public enterprise data compilations** — front-end publicly accessible, back-end compilation private. Exemplo: platform cujas listagens individuais são públicas mas cujo aggregate ranking/index/score é secret.

Reconhecimento das categorias 1 e 2 cresce em todas as jurisdições. Categoria 3 é contestada.

### Jurisdições (US, China, EU)
- **US**: DTSA 2016 + state UTSA (uniform trade secrets act). Compulife v. Newport (11th Cir. 2020) expandiu proteção a scraping-vulnerable compilations, mas com standards incertos.
- **China**: Anti-Unfair Competition Law 2019. Standards mais formais (deferência a explicit secrecy marking / confidentiality agreements).
- **EU**: Trade Secrets Directive 2016/943. Exige **reasonable steps** demonstrados; mais restritivo que US.

### Crítica de Chen à Categoria 3

1. **Compulife standard over-lenient**: ruling hinged em dificuldade de reconstrução por **human manual effort**. Ignora scraping technology atual. Chen: quando assistance tecnológica é fatorada, most semi-public compilations são **readily ascertainable** e portanto não qualificam.

2. **Arms race inefficiency**: proteger semi-public incentiva escalation defensiva (IP blocking, CAPTCHAs, device fingerprinting, rate limiting agressivo). Arms race cresce; proteção torna-se perpetuamente provisional. Trade secret law deveria **reduzir**, não **incentivar**, este race.

3. **Normative standard proposto**: proteção para semi-public apenas se **front-end access is meaningfully restricted to a limited number of users**. Exemplo: plataforma B2B com logins corporativos. Se UI é open-to-all-internet, Chen argumenta que proteção não serve objetivos de trade secret law.

### Arms race implications
Sobre scraping: não-intrusive scraping (acesso via front-end público sem breach of access controls) não deveria ser sancionável via trade secret law. Somente breach of access controls ou circumvention of genuine restrictions deveria triggerar liability.

## Interpretação

(⚠️ nossa interpretação) **Category 2 (Private data compilations) é a categoria dominante para E39.** Rules/lessons/antipatterns derivados de codebase interno do cliente são **private enterprise data compilations**: derivam de operações internas, não são readily ascertainable, têm independent economic value. Default treatment: trade secret. Isto reforça T01 isolation-by-default como compliance-aligned arquitetura, não paranóia.

(⚠️ nossa interpretação) **EU é o constraining binding para multi-jurisdictional deploy.** EU Directive 2016/943 exige reasonable steps demonstrados, não apenas intenção. Se claude-pipeline deploya multi-tenant sem isolation e cliente A é EU-based, pipeline pode **por si só** failar em "reasonable steps expected of the information holder" — invalidando claim de A independente de NDA com cliente B. Argumento forte: jurisdictional matrix é prerequisito, não nice-to-have.

(⚠️ design analogy) **Compulife over-lenient argument corta os dois lados.** Se scraping technology torna compilations "readily ascertainable", argumento pode ser usado **contra** clientes que não protegem adequadamente. Translation para pipeline: se isolation é deploy-able but not deployed, pipeline becomes instrumento via o qual cliente perde proteção — argumentável que pipeline tem **obrigação afirmativa** de oferecer isolation default.

(⚠️ nossa interpretação) **Category 3 critique é irrelevant para claude-pipeline internal state.** Rules/lessons não são front-end públicas em nenhum cenário concebível. Category 3 discussion é útil como framing doutrinário mais amplo, mas scope direto é Categoria 2.

## Conexões
- complementa: [[trade-secrets-ai-hrdy-2025]] — Hrdy 2025 foca em AI-specific artifacts (weights, training data, prompts); Chen 2025 foca em enterprise data taxonomy; ambos cobrem trade secret × AI por ângulos distintos.
- contextualiza: [[autonomous-kb-failure-modes]] — "vazamento de contexto proprietário" ganha arcabouço comparativo US/China/EU.

## Fontes
- [Chen 2025 — Enterprise Data as Trade Secrets](../../raw/papers/chen-2025-enterprise-data-trade-secrets.md) — 29 Stan. Tech. L. Rev. 1; SSRN 5456754. Três categorias; comparative US/China/EU; Compulife critique; reasonable steps requirement.
