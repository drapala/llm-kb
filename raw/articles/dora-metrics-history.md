---
source: https://dora.dev/insights/dora-metrics-history/
fetched: 2026-04-25
type: insight-article
publisher: DORA / Google Cloud
---

# Evolution of DORA Software Delivery Metrics

## Origins (2014–2015)

The 2014 study introduced 4 candidate variables: deployment frequency, lead time for changes, MTTR, change fail rate. Statistical analysis revealed change fail rate didn't correlate strongly enough — 2014 model used 3.

By 2015, the framework evolved into a dual model:

> "The research debunked the myth that speed comes at the expense of stability, finding that high performers excelled at both."

The throughput-stability dichotomy emerged:
- **Throughput:** Deployment frequency, deployment lead time
- **Stability:** MTTR, change fail rate

## Standardization (2016–2018)

The 4 metrics became industry standards through 2016–2017. In 2018, DORA added "availability" as a 5th measure and renamed "IT performance" → "Software Delivery and Operational (SDO) performance."

## Refinement (2021–2023)

- 2021: "availability" expanded to "reliability" (encompasses latency, performance, scalability)
- 2023: "mean time to recover" renamed/redefined as "failed deployment recovery time" — to separate software-caused failures from external (data center outages). New definition focuses specifically on service restoration following production changes caused by deployments.

## Structural transformation (2024)

DORA introduced a **5th metric: deployment rework rate**. Reasoning: "change failure rate functioned as a proxy for rework burden" — measure rework directly.

## Current 5-metric model

**Software Delivery Throughput:**
- **Change lead time** (code commit → production deployment)
- **Deployment frequency** (deployment cadence)
- **Failed deployment recovery time** (recovery speed)

**Software Delivery Instability:**
- **Change fail rate** (% of failing deployments)
- **Deployment rework rate** (% of unplanned corrective deployments)

## Pattern of evolution

Renaming and re-grouping reflects DORA's commitment to precision over historical continuity. Each rename (MTTR → Failed Deployment Recovery Time) tightens the operational definition; each new metric (rework rate) targets a phenomenon previously approximated by a proxy.
