---
source: https://dora.dev/capabilities/platform-engineering/
fetched: 2026-04-25
type: capability-page
publisher: DORA / Google Cloud
year: 2025
---

# DORA — Platform Engineering Capability

## Definition

DORA defines platform engineering as:

> "a sociotechnical discipline where engineers focused on the intersection of social interactions between teams and the technical aspects of automation, self-service, and repeatability."

The practice centers on constructing an Internal Developer Platform delivering "shared, high-quality tools, services, and 'golden paths'".

## Adoption (2025)

- 90% of organizations use internal developer platforms
- 76% have established dedicated platform teams

## AI amplification effect (2025 research)

> "AI is an amplifier: it magnifies an organization's existing strengths, but also its dysfunctions."

Risk: while orgs equip developers with AI tools, productivity gains "frequently disappear into downstream disorder" — bottlenecks in testing, security reviews, deployment.

> "When platform quality is high, the effect of AI adoption on organizational performance becomes strong and positive. Conversely, when platform quality is low, the effect of AI adoption on organizational performance is negligible."

A high-quality platform functions as the "essential governance layer for AI adoption" — converting speed into systemic improvements.

## "Shift down" (cognitive load)

> "shift down this complexity into the platform itself"

Rather than forcing developers to master Kubernetes/networking/security, platforms provide intuitive self-service golden paths. 2024 research: developer independence (tasks without enabling-team reliance) → "5% improvement in productivity at both the team and individual levels."

## Implementation best practices (DORA)

- Adopt **product management mindset** for the platform
- "Identify the golden path for the most common workflow and build just enough to make that specific journey demonstrably better" (MVP platform)
- Design for **extensibility** — clear APIs and contribution models prevent platform team bottlenecks
- Track **software delivery metrics** (lead time, deployment frequency, recovery time, failure rates) + **developer satisfaction** (CSAT, NPS, H.E.A.R.T.)
- Strongest correlation with positive UX (DORA 2025): "clear feedback on the outcome of my tasks"

## Common pitfalls (DORA 2025)

- Building without user research validation
- Imposing rigid standards without collaboration
- Operating as reactive infrastructure vending machines
- Big-bang releases instead of iterative
- One-size-fits-all ignoring team diversity
