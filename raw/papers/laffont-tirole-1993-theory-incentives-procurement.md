# A Theory of Incentives in Procurement and Regulation

**Authors:** Jean-Jacques Laffont and Jean Tirole
**Source:** MIT Press, 1993. ISBN: 978-0-262-12171-4
**Chapters recommended:** 1-3 (sufficient foundation)

## Overview

The canonical textbook of public procurement theory. Develops a complete theory of optimal incentive design for procurement and regulatory contracts under asymmetric information. Extends and unifies the principal-agent literature (Mirrlees 1971, Myerson 1981, Holmstrom 1979) to procurement settings.

## Key Concepts (Chapters 1-3)

### Chapter 1: The Basic Regulatory Model

**Setup:** A regulator (principal) contracts with a regulated firm (agent) that has private information about its efficiency parameter θ ~ [θ_low, θ_high]. The firm's cost function: C = β - e, where β is a productivity parameter (private info) and e is effort (not observable).

**Social welfare:** W = S(q) - (1+λ)(C + t) + t - U
where S(q) = consumer surplus, λ = cost of public funds, t = transfer, U = firm's rent.

**Revelation principle:** Optimal mechanism is a menu of contracts (t(β̂), q(β̂)) that incentivizes truthful revelation of β̂ = β.

**Efficiency-rent tradeoff:** Efficient types get information rents (U > 0); inefficient types get zero rent but distorted output. The regulator trades off productive efficiency against rent extraction.

### Chapter 2: Adverse Selection in Procurement

**Fixed-price contracts:** Appropriate when cost uncertainty is low and effort incentives dominate. Firm bears full cost risk → maximum incentive for cost reduction.

**Cost-plus contracts:** Appropriate when cost uncertainty is high and moral hazard is less critical. Regulator bears full cost risk → no incentive distortion from uncertainty, but reduced effort incentives.

**Optimal sharing rule:** Intermediate between fixed-price and cost-plus. Cost-sharing parameter α* depends on: variance of cost shocks, curvature of disutility of effort, and shadow cost of public funds λ.

### Chapter 3: Moral Hazard and the Hold-Up Problem

Extends Chapter 2 to dynamic settings with renegotiation (building on Tirole 1986).

**Dynamic hold-up:** After firm invests, regulator observes cost (or infers it from realized cost) and proposes new contract exploiting the information. Firm anticipates this → underinvestment.

**Commitment:** Optimal mechanism requires commitment to not renegotiate — but governments often cannot credibly commit. This is the fundamental tension in infrastructure procurement.

## Relevance for B2G / Risk Score

**Aditivos interpretation:** In the Laffont-Tirole framework, additive contracts (aditivos) are a specific form of renegotiation where the regulator (governo) agrees to expand scope + price. This can be:
1. *Efficient renegotiation:* scope genuinely changed → aditivo is appropriate mechanism
2. *Strategic renegotiation:* firm lowballed the bid knowing it would request aditivo → hold-up

The theory predicts that if the government cannot commit to rejecting renegotiation, firms will systematically underbid + request aditivos.

**Optimal procurement design implication:** Fixed-price contracts with strong non-renegotiation commitment reduce strategic aditivos but expose government to legitimate cost uncertainty. Monitoring systems (like Zelox) increase the cost of strategic hold-up by making the pattern detectable.

## Prior Work

- Mirrlees (1971): optimal income tax under private information — foundation for principal-agent theory
- Myerson (1981): optimal auction design, revelation principle
- Holmstrom (1979): moral hazard in teams
- Tirole (1986): procurement and renegotiation — direct predecessor

## Citation

Laffont, J.-J., & Tirole, J. (1993). *A Theory of Incentives in Procurement and Regulation*. MIT Press.

## Access

- Available via library (MIT Press). Not freely available online.
- Chapters 1-3 cover the foundational material sufficient for Risk Score context.
