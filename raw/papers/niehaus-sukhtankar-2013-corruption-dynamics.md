# Corruption Dynamics: The Golden Goose Effect

**Authors:** Paul Niehaus and Sandip Sukhtankar
**Source:** American Economic Journal: Economic Policy, Vol. 5, No. 4 (November 2013), pp. 230-269
**DOI:** 10.1257/pol.5.4.230

## Abstract

We study how corruption responds to an increase in program size using a natural experiment in India's National Rural Employment Guarantee Scheme (NREGS). We find that as program spending increased, corruption scaled less than proportionally — bureaucrats "protected their golden goose" by not extracting too much from a larger program that they could extract from over a longer horizon. Corruption was higher in places with better enforcement. Implications: anticorruption policy may perversely increase corruption by threatening the long-term extraction horizon.

## Key Results

**Setting:** India's NREGS (large rural employment program). Natural experiment: abrupt increase in program size creates variation in the scale of funds flowing through bureaucrats.

**Main finding (Golden Goose Effect):** When program funds increase, corruption does NOT scale proportionally. Bureaucrats extract a *smaller share* from a larger program.

**Mechanism:** Bureaucrats have a long-term extraction relationship ("golden goose"). Extracting too aggressively risks killing the goose (detection, program termination). With a bigger program, the future flow of rents is more valuable → more restraint.

**Perverse enforcement effect:** In areas with stronger monitoring/enforcement, corruption was *higher*, not lower. Explanation: anticipation of future enforcement reduces the horizon → bureaucrats extract more aggressively today ("if I'm going to get caught anyway, extract more now").

## Key Implication: Dynamics of Detection

When detection risk increases, corrupt actors may *increase* corruption in the short run (before being caught) and then drastically reduce it after enforcement is established. This creates a U-shaped response: 
1. Pre-enforcement: low/moderate corruption
2. When detection risk increases: peak corruption (race to extract)
3. Post-enforcement establishment: low corruption

## Relevance for B2G / Risk Score

**Adaptive behavior of fraudulent suppliers:** Zelox is detecting corruption signals in procurement data. If suppliers learn that these signals are monitored, their behavior may evolve:
- Short run: adapt signals (avoid specific detectable patterns → shift to less detectable forms)
- Medium run: extract more aggressively before the "window closes" (golden goose threatened)
- Long run: reduce corruption if detection risk is credibly permanent

**Signal evolution:** The specific signals Zelox uses (additive contracts near 25% limit, phantom firms, etc.) may become less predictive over time as suppliers learn to avoid them. New signals (deviation from these patterns) become informative.

**Implication for risk model:** A static model trained on historical patterns will lose predictive power as suppliers adapt. Need either:
1. Continuous retraining on new data
2. Signals that are hard to manipulate (fundamental features, not easily gamed)
3. Ensemble of diverse signals (if some are evaded, others still detect)

## Citation

Niehaus, P., & Sukhtankar, S. (2013). Corruption dynamics: The golden goose effect. *American Economic Journal: Economic Policy*, 5(4), 230-269.

## Access

- AEJ: paywalled. NBER or SSRN version may be available.
