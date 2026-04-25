---
title: "DORA 2025 — AI as Platform Amplifier"
sources:
  - path: raw/articles/dora-2025-ai-amplifier.md
    type: report
    quality: primary
    stance: neutral
  - path: raw/articles/dora-platform-engineering-capability.md
    type: capability-page
    quality: primary
    stance: neutral
created: 2026-04-25
updated: 2026-04-25
tags: [dora, platform-engineering, devex, ai-adoption, lateral, organizational-design]
source_quality: medium
interpretation_confidence: low
quarantine: true
quarantine_created: 2026-04-25
quarantine_reason: "Domínio lateral recém-ingerido — aguarda review frio + verificação adversarial"
resolved_patches: []
provenance: source
---

## Resumo

DORA 2025 (Google Cloud + partners) estabelece como tese central que AI é **amplificador** da qualidade organizacional preexistente — não causa primária de ganho. Quando a plataforma interna é de alta qualidade, AI tem efeito forte e positivo na performance organizacional; quando a plataforma é fraca, o efeito de AI é negligível. Plataforma de qualidade funciona como camada de governança/distribuição para AI. 90% das organizações têm internal developer platforms (2025); 76% têm time dedicado de plataforma. Adoção de AI sem plataforma boa: ganhos individuais "frequently disappear into downstream disorder" — bottlenecks em testing, security review, deploy.

## Conteúdo

### Tese central — AI amplifica, não cria

> "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses." (DORA 2025)

> "The greatest returns on AI investment come not from the tools themselves, but from a strategic focus on the underlying organizational system." (DORA 2025)

Reformula adoção de AI como problema **organizacional**, não tecnológico.

### Plataforma como governance layer para AI

> "When platform quality is high, the effect of AI adoption on organizational performance becomes strong and positive. Conversely, when platform quality is low, the effect of AI adoption on organizational performance is negligible." (DORA 2025)

Mecanismo: plataforma fornece "standardized, secure pathways for AI-generated code" — converte velocidade em melhoria sistêmica.

### "Shift down", não "shift left"

> "shift down this complexity into the platform itself" (DORA, citing Richard Seroter)

Plataformas absorvem complexidade (Kubernetes, security, networking) em vez de empurrar pra developers via shift-left clássico. Platform oferece self-service golden paths intuitivas.

Dado empírico (DORA 2024): developer independence (tarefas sem dependência de enabling team) → "5% improvement in productivity at both the team and individual levels."

### Métricas correlacionadas com UX positivo

DORA 2025: a correlação mais forte com experiência positiva é **"clear feedback on the outcome of my tasks"** — não velocidade, não tooling. Feedback claro vence sobre features.

### Práticas (DORA capability page)

- **Product management mindset** para a plataforma — não infra ticket system
- **MVP platform:** "identify the golden path for the most common workflow and build just enough to make that specific journey demonstrably better"
- **Extensibility by design:** APIs claras + contribution models previnem que platform team vire bottleneck
- Tracking: software delivery metrics (lead time, deployment frequency, recovery time, failure rates) + dev satisfaction (CSAT, NPS, H.E.A.R.T.)

### Anti-patterns documentados (DORA 2025)

- Build sem user research validation
- Standards rígidos sem collaboration
- Platform como "reactive infrastructure vending machine"
- Big-bang releases ao invés de iterativo
- One-size-fits-all que ignora diversidade de times

### Adoção em 2025

- 90% das organizações: internal developer platforms
- 76%: dedicated platform teams

## Interpretação

(intencionalmente vazia — domínio lateral, claims factuais. Conexões com VSM/Ashby/lemons emergem em /ask, não /ingest.)

## Conexões

- relatedTo: [[viable-system-model-beer]] — plataforma como sistema viável que absorve variety; "shift down" é variety attenuation no S1 do desenvolvedor (⚠️ analogia editorial)
- relatedTo: [[requisite-variety]] — extensibility-by-design = mecanismo de variety amplification do regulador
- relatedTo: [[market-for-lemons]] — "platform quality" como problema de signaling para adoção interna

## Fontes

- [DORA 2025 Report (landing)](../../raw/articles/dora-2025-ai-amplifier.md) — tese AI as amplifier, methodology partners
- [DORA Platform Engineering capability](../../raw/articles/dora-platform-engineering-capability.md) — definition, shift-down, governance-for-AI quote, best practices

> ⚠️ QUARENTENA: artigo recém-ingerido em domínio lateral (platform engineering). Critérios pendentes: tempo (24h), review frio.
