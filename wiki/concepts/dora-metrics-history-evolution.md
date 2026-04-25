---
title: "DORA Metrics — Evolution from 4 to 5 Metrics (2014–2024)"
sources:
  - path: raw/articles/dora-metrics-history.md
    type: insight-article
    quality: primary
    stance: neutral
created: 2026-04-25
updated: 2026-04-25
tags: [dora, software-delivery-metrics, throughput, instability, lateral, devex]
source_quality: medium
interpretation_confidence: high
quarantine: true
quarantine_created: 2026-04-25
quarantine_reason: "Domínio lateral recém-ingerido — aguarda review frio"
resolved_patches: []
provenance: source
---

## Resumo

As métricas DORA evoluíram de 3 (2014) → 4 (2015, dual throughput/stability) → 5 (2024, com **deployment rework rate**). Em 2023, "MTTR" foi renomeado para **"Failed Deployment Recovery Time"** — refinando o escopo (só falhas causadas por deploys, não outages externos). Em 2024, change fail rate ganhou companhia: **deployment rework rate** mede diretamente o burden de retrabalho que change fail rate só aproximava. O modelo atual divide as 5 entre **Throughput** (lead time, deployment frequency, failed deployment recovery time) e **Instability** (change fail rate, deployment rework rate).

## Conteúdo

### Cronologia

| Ano | Mudança |
|---|---|
| 2014 | Estudo inicial: 4 candidatas; 3 entram no modelo (deployment frequency, lead time, MTTR). Change fail rate exclusa por correlação fraca. |
| 2015 | Dual model: Throughput vs Stability. Change fail rate readmitida na Stability ao lado de MTTR. |
| 2016–2017 | Os 4 viram padrão da indústria. |
| 2018 | "Availability" adicionada como 5ª; rebranding "IT performance" → "Software Delivery and Operational (SDO) performance". |
| 2021 | "Availability" expandida para "Reliability" (inclui latency, performance, scalability). |
| 2023 | **MTTR renomeado/redefinido** como "Failed Deployment Recovery Time" — só falhas causadas por deploys, não outages externos. |
| 2024 | **Deployment rework rate** introduzida como 5ª métrica. Change fail rate vira "proxy for rework burden"; rework rate mede direto. |

### Modelo atual (5 métricas, 2024+)

**Software Delivery Throughput:**
- **Change lead time** — code commit → production deployment
- **Deployment frequency** — cadência de deploy
- **Failed deployment recovery time** — velocidade de recuperação após falha de deploy

**Software Delivery Instability:**
- **Change fail rate** — % de deploys que falham
- **Deployment rework rate** — % de deploys corretivos não-planejados

### Insight metodológico

> "The research debunked the myth that speed comes at the expense of stability, finding that high performers excelled at both." (DORA 2015)

A separação Throughput/Stability não é tradeoff — é evidência de que high performers são bons em ambos.

### Padrão evolutivo

Cada renomeação tighten a definição operacional. Cada métrica nova ataca um fenômeno antes aproximado por proxy. O modelo prioriza precisão sobre continuidade histórica.

## Interpretação

(vazia por design — domínio lateral, claim factual)

## Conexões

- relatedTo: [[dora-2025-ai-as-amplifier]] — DORA 2025 usa o framework de 5 métricas; AI amplifica throughput, mas sem plataforma amplifica também instability

## Fontes

- [DORA Metrics History](../../raw/articles/dora-metrics-history.md) — cronologia completa, definições, dual model

> ⚠️ QUARENTENA: artigo recém-ingerido em domínio lateral. Critérios pendentes: tempo (24h), review frio.
