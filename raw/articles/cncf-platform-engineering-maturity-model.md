---
source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
fetched: 2026-04-25
type: whitepaper
publisher: CNCF (App Delivery TAG)
year: 2023
---

# CNCF Platform Engineering Maturity Model

## Purpose

> "Every organization relies on an internal platform crafted for its own organization — even if that platform is just documentation on how to use third party services."

The model is for self-reflection, not aspirational climbing. Reaching the highest level should not be an automatic goal; orgs should evaluate whether the investment at each level aligns with their context.

## Structure: 5 Aspects × 4 Levels

### Aspect 1 — Investment
**Question:** "How are staff and funds allocated to platform capabilities?"

- **Provisional:** Capabilities emerge from necessity, no central funding. Hit teams form for urgent needs, disband quickly.
- **Operational:** Dedicated teams, persistent budget — but cost-center mode, no measured value-stream impact.
- **Scalable:** Investment mirrors product development — PMs, UX specialists. Data-driven decisions.
- **Optimizing:** Core maintainers enable specialist domains (security, performance, marketing) to integrate requirements into platform frameworks.

### Aspect 2 — Adoption
**Question:** "Why and how do users discover and use internal platforms and platform capabilities?"

- **Provisional:** Sporadic, haphazard, driven by chance conversations.
- **Operational:** External incentives or mandates — users lack motivation to explore beyond required.
- **Scalable:** Users choose platform because of clear value — reduced cognitive load, superior experience.
- **Optimizing:** Product teams contribute fixes/features back; shared ownership beyond platform engineers.

### Aspect 3 — Interfaces
**Question:** "How do users interact with and consume platform capabilities?"

- **Provisional:** Custom processes per capability, manual intervention, personal support from providers.
- **Operational:** Standardized tooling and golden paths exist — but deviations become complex fast.
- **Scalable:** One-click implementations; autonomous provisioning with minimal support.
- **Optimizing:** Capabilities integrate transparently into existing tools/workflows. Observability + identity provision automatically. Composable building blocks.

### Aspect 4 — Operations
**Question:** "How are platforms and their capabilities planned, prioritized, developed and maintained?"

- **Provisional:** Reactive, ad hoc requests, informal maintenance, no planned updates.
- **Operational:** Central documentation, ownership registers, compliance burndown — upgrades manual.
- **Scalable:** Cross-infrastructure coordination, org-wide prioritization, continuous delivery.
- **Optimizing:** Fully automated lifecycle. Zero-impact updates. Shared responsibility models.

### Aspect 5 — Measurement
**Question:** "What is the process for gathering and incorporating feedback and learning?"

- **Provisional:** Ad-hoc metrics, anecdotal evidence, incomplete data.
- **Operational:** Standardized feedback channels, surveys, categorized priorities — translation to roadmap is hard.
- **Scalable:** Outcome-driven metric selection, dedicated analysts, industry frameworks guide strategy.
- **Optimizing:** Data + feedback permeate culture. Cross-functional teams identify hypotheses, measure post-delivery, balance quantitative + qualitative — sensitive to unintended measurement consequences.

## Key principle (anti-Goodhart)

The Optimizing level explicitly notes "sensitive to unintended consequences of measurement itself" — built-in awareness that maturity models can themselves become Goodhart targets.
