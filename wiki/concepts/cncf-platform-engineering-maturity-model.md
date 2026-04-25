---
title: "CNCF Platform Engineering Maturity Model"
sources:
  - path: raw/articles/cncf-platform-engineering-maturity-model.md
    type: whitepaper
    quality: primary
    stance: neutral
created: 2026-04-25
updated: 2026-04-25
tags: [cncf, platform-engineering, maturity-model, devex, lateral, organizational-design]
source_quality: medium
interpretation_confidence: high
quarantine: true
quarantine_created: 2026-04-25
quarantine_reason: "Domínio lateral recém-ingerido — aguarda review frio"
resolved_patches: []
provenance: source
---

## Resumo

CNCF (App Delivery TAG, 2023) define um modelo de maturidade para platform engineering com **5 aspectos × 4 níveis**. Aspectos: **Investment, Adoption, Interfaces, Operations, Measurement**. Níveis: **Provisional → Operational → Scalable → Optimizing**. Princípio explícito: o modelo é para self-reflection, não escalada aspiracional — reaching Optimizing não é objetivo automático; depende do contexto e da relação custo-benefício do investimento. O nível Optimizing inclui awareness anti-Goodhart ("sensitive to unintended consequences of measurement itself").

## Conteúdo

### Princípio fundamental

> "Every organization relies on an internal platform crafted for its own organization — even if that platform is just documentation on how to use third party services." (CNCF)

O modelo serve para identificar onde investir; não para hierarquizar maturidade como virtude.

### Os 5 aspectos

**1. Investment** — "How are staff and funds allocated to platform capabilities?"
- Provisional: emerge de necessidade, sem funding central
- Operational: budget persistente, mas cost-center mode
- Scalable: investment espelha product development (PMs, UX)
- Optimizing: maintainers enable specialist domains a integrar requisitos

**2. Adoption** — "Why and how do users discover and use internal platforms and platform capabilities?"
- Provisional: esporádica, conversas ao acaso
- Operational: por mandato/incentivo externo
- Scalable: usuários escolhem por valor claro (cognitive load reduzido)
- Optimizing: product teams contribuem features de volta

**3. Interfaces** — "How do users interact with and consume platform capabilities?"
- Provisional: custom por capability, manual
- Operational: golden paths existem, mas deviations são complexas
- Scalable: one-click, autonomous provisioning
- Optimizing: integração transparente em tools existentes; building blocks compostáveis

**4. Operations** — "How are platforms and their capabilities planned, prioritized, developed and maintained?"
- Provisional: reativo, ad hoc
- Operational: documentação central, upgrades manuais
- Scalable: continuous delivery, prioritization org-wide
- Optimizing: lifecycle automatizado, zero-impact updates

**5. Measurement** — "What is the process for gathering and incorporating feedback and learning?"
- Provisional: ad-hoc, anedótico
- Operational: surveys, channels padronizados — translation a roadmap é hard
- Scalable: outcome-driven, dedicated analysts
- Optimizing: feedback permeia cultura; balance quanti + quali; **awareness de Goodhart effects**

### Princípio anti-Goodhart embutido

O nível Optimizing explicitamente diz "sensitive to unintended consequences of measurement itself" — o modelo carrega awareness que maturity models podem virar próprios alvos de Goodhart. Self-aware design.

## Interpretação

(vazia por design)

## Conexões

- relatedTo: [[dora-2025-ai-as-amplifier]] — DORA descreve a *tese* da plataforma como amplifier; CNCF descreve a *trajetória* operacional pra construí-la
- relatedTo: [[goodhart-law]] — quando existir; Optimizing-level já tem awareness embutida

## Fontes

- [CNCF Platform Engineering Maturity Model](../../raw/articles/cncf-platform-engineering-maturity-model.md) — 5 aspects, 4 levels, princípio anti-Goodhart

> ⚠️ QUARENTENA: artigo recém-ingerido em domínio lateral. Critérios pendentes: tempo (24h), review frio.
