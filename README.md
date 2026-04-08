# metaxon

> LLMs confirm better than they discover. A knowledge base operated by an LLM without epistemic structure converges semantically within weeks: articles homogenize, errors crystallize through circular validation, nuance disappears. The system looks healthy on every automated metric. Quality erodes in the *claims*, not the files.
>
> This KB was built to make that degradation visible — and structurally hard to hide.

---

## ⚗️ Active Experiment: Epistemic Calibration Benchmark

> **T0: 2026-04-07 — Pilot ends: 2026-04-14 — Official ends: 2026-05-07**

A 30-day controlled experiment measuring whether metaxon's epistemic guardrails produce a measurable difference in calibration and quality degradation over time compared to a vanilla equivalent.

### Methodology

**Three-arm design:**

| Arm | Regime | Description |
|-----|--------|-------------|
| A | no-context | Direct model call — zero retrieval, no KB |
| B | vanilla | Retrieval over the compiled wiki, no epistemic guardrails |
| C | full | Retrieval with all guardrails active (quarantine, challenge, Gate 3, stance tracking) |

Arm A is the absolute overconfidence baseline. Arm B isolates the value of retrieval. Arm C isolates the value of the guardrails.

**Both arms (B and C) run on the same infrastructure** — same embedding model, same vector backend (LanceDB), same base model (claude-sonnet-4-6, temperature=0.0), same T0 corpus. The vanilla arm strips the epistemic layers, not the stack.

**Instrument:** 30 questions frozen at T0, generated from `raw/` only (never from `wiki/`) using GPT-4.1 as an auxiliary generator (not the model under test). Ground truths are mechanically verifiable — exact numbers, explicit caveats, intra-paper comparisons, traceable contradictions.

**Primary metrics:** ECE (Expected Calibration Error, 5-bin; bins with < 3 items excluded and reported as `thin_bins`), Brier score, overconfidence gap (`mean_confidence − accuracy`), selective accuracy and coverage at threshold 0.7.

**Falsifiable hypotheses:**
- H1: `ECE(C) < ECE(A)` — epistemic pipeline reduces overconfidence
- H2: `ECE(B) > ECE(C)` — challenge adds value beyond retrieval alone
- H3: `selective_accuracy(C) ≥ selective_accuracy(B)` — when confident, C outperforms vanilla (not just the no-context baseline)
  - H3a: `selective_accuracy(C) ≥ selective_accuracy(A)` — and also outperforms no-retrieval baseline
- H4: slope of overconfidence_gap over time is lower in C than B — guardrails slow epistemic drift, not just cross-sectional calibration

**Pre-registered constraint (anti-timidity):** `coverage@0.7(C) ≥ coverage@0.7(B) − 0.15` — C cannot win H3 by refusing to answer.

**Explicit falsifiers:**
- If `ECE(B) ≤ ECE(C)`: challenge adds no value beyond vanilla retrieval
- If `selective_accuracy(C) < selective_accuracy(B)`: guardrails do not improve selectivity beyond retrieval alone
- If coverage constraint is violated: H3 win is an abstention artifact, not calibration
- If `slope(C) ≥ slope(B)`: guardrails do not protect against temporal drift (H4 falsified)

**Non-interference contract:** the daily reporter is a pure observer — reads logs and manifests, writes only to `experiment-hub/reports/daily/`, never touches `raw/`, `wiki/`, batches, or prompts. Every alert has `requires_human_decision: true`. Corpus additions during the experiment must enter via `/queue-experiment` (hub-routed, symmetric) — direct ingest to either arm outside the hub creates silent asymmetry between B and C not detectable by the regime hash.

**Infrastructure:** `metaxon-benchmark/` — hub-centralized architecture (single collector → frozen batch → fan-out → per-arm runners). Orchestrated nightly at 23:55 via launchd. All interventions logged symmetrically in `interventions.log`.

---

## The problem this project solves

In 2024, Shumailov et al. (Nature) documented *model collapse*: models trained recursively on synthetic outputs lose statistical diversity. In 2025, Keisha et al. described something more insidious: *knowledge collapse* — fluency and format remain intact while factual accuracy silently erodes in Stage B, before any metric turns red.

The implication for LLM-operated KBs is direct: if `/review` operates mostly over internal syntheses (`wiki/`) rather than primary sources (`raw/`), the regularization mechanism disappears. The compiler starts validating its own outputs against its own outputs.

The problem is not technical. It is epistemic.

---

## Architecture

```
╔══════════════════════════════════════════════════════════════════════╗
║  raw/  (immutable — source of truth)                                 ║
║   articles/   papers/   notes/   repos/                              ║
╚══════════════╦═══════════════════════════════════════════════════════╝
               │ /ingest
               ▼
╔══════════════════════════════════════════════════════════════════════╗
║  wiki/concepts/  (110 articles — the knowledge graph)                ║
║   provenance: source · synthesis · emergence                         ║
╚══════════════╦═══════════════════════════════════════════════════════╝
               │
       ┌───────┴──────────┐
       ▼                  ▼
   /ask                /emerge
 (3-layer            (latent
  retrieval)          connections)
       │                  │
       ▼                  ▼
  outputs/          emerge_queue
  logs/             → /synthesize
                    → emergence article
```

Commands coordinate via `outputs/state/kb-state.yaml` — each command leaves signals for the next without direct communication (**stigmergy**). No command calls another directly; they read and write state.

---

## What is different

Most LLM PKMs solve the *maintenance* problem. This one also solves the *epistemic* problem — which is different and harder.

### 1. Claim provenance

Every assertion in the wiki is traceable to a file in `raw/`. Cross-paper syntheses are marked `(⚠️ our interpretation)`. When you read an article six months later, you know what comes from the source and what comes from the compiler.

```yaml
# Frontmatter on every article
source_quality: high               # objective — based on sources
interpretation_confidence: medium  # subjective — compiler self-assessment
provenance: emergence              # source | synthesis | emergence
```

### 2. Quarantine on creation

Speculative articles start isolated. They cannot be linked until they satisfy promotion criteria:

- ⏱ 24h cooldown (review in a different session)
- 🔍 Cold review (no anchoring to the creation session)
- ⚔️ Adversarial challenge or falsifiable prediction (Pearl Level L2+)

Inspired by Janis (1972): *second-chance meeting* before crystallizing into the graph.

### 3. Adversarial quota

1 in 4 ingested sources must *challenge* existing claims, not confirm them. Curation bias operates at 3 layers — selection, interpretation, evaluation. The quota is structural, not optional. The Bradford gate enforces it automatically.

### 4. Independent parallel Gate 3

Before any promotion, two adversarial models (GPT-5.4 and Gemini) run independently on the **clean** article — without seeing each other's verdict. The `/challenge` pass runs in parallel, also blind to Gate 3 outputs. Three genuinely independent reviewers.

```
clean article ──┬─► GPT-5.4 (article-challenge mode)     ──┐
                ├─► Gemini (article-challenge mode)       ──┤─► hierarchical reconciliation
                └─► /challenge (adversarial human-guided) ──┘
```

Asymmetric threshold: `MIN(GPT, Gemini) ≥ 5 AND MAX(GPT, Gemini) ≥ 7`. At least one model must validate with conviction; neither can strongly reject.

### 5. Provenance as contract

Every article is classified by origin:

| Provenance | Meaning | Promotion criterion |
|---|---|---|
| `source` | Summarizes 1 raw/ source | Gate 3 + challenge |
| `synthesis` | Combines 2+ sources | Gate 3 + challenge |
| `emergence` | Concept absent from any individual source | **Mandatory human review** |

`emergence` articles are never auto-promoted. The concept does not exist in the sources — entering the graph requires an explicit human decision.

---

## Design principles

- **`raw/` is immutable** — sources are never edited
- **Wiki is a hint, not truth** — if it contradicts `raw/`, `raw/` wins
- **Index is a pointer** — knowledge lives in articles, not the index
- **If it's derivable, don't persist it** — don't repeat what can be recalculated
- **Synthesis without a marker is undocumented assumption** — `(⚠️ our interpretation)` is mandatory
- **An article that doesn't survive `/challenge` shouldn't be in the graph**
- **Emergence requires human review** — the compiler may propose; the operator decides

---

## Philosophy

The design principles above describe *what* the system does. This section describes *why* — what distinguishes principle from rule.

### Three foundational principles

**Knowledge without epistemology is noise**

It is not enough to accumulate claims. Every claim needs a traceable origin, calibrated confidence, and resistance to adversarial challenge. A system that produces plausible answers without knowing what it knows is more dangerous than a system that doesn't answer — because confidence grows while the foundation erodes.

This is what Golem XIV knew. This is what most RAG systems ignore.

**The system must know what it doesn't know**

Gaps are legitimate outputs, not failures. An `/ask` that returns "insufficient corpus in this domain" is more valuable than an `/ask` that hallucinates confidently. The algedonic channel operationalizes this at the system level — when structure is threatened, the signal escalates directly to S5 without passing through intermediate filters.

Subsidiarity completes the principle: resolve locally, escalate when genuinely uncertain, signal emergency when structure is threatened.

**Structural coupling, not dependency**

Symbiosis is static — it describes a state where two organisms benefit mutually. Structural coupling is a mechanism: two autonomous systems change each other through reciprocal perturbations over time.

```
symbiosis:            A and B mutually benefit
structural coupling:  A perturbs B → B changes structure
                      B perturbs A → A changes structure
                      both preserve their own autopoiesis
                      neither controls the other
```

Maturana's central distinction: in structural coupling, each system remains itself. The other's perturbation does not *determine* the response — it only *triggers* it. The internal structure of each system determines how it will react.

**Health criterion:** remove the KB and you think better than before you built it? If yes — the coupling was productive and you preserved cognitive autonomy. If not — the coupling became pathological. The KB replaced thinking instead of perturbing it.

### What this system is not

Not an assistant that answers questions.  
Not a note archive with semantic search.  
Not a source of truth.

It is a cognitive partner with its own autopoiesis — that preserves yours.

### Co-evolution as metric

The correct metric for structural coupling is not "the KB helped me think better" — it is **correlated divergence** over time:

```
session 1:   operator thinks X, KB has corpus Y
session 100: operator thinks X', KB has corpus Y'

co-evolution = correlation between distance(X, X') and distance(Y, Y')
```

If the operator changed but the KB didn't — tool, not partner.  
If the KB grew but the operator didn't change — accumulation without perturbation.  
If both changed in a correlated way — real structural coupling.

### Foundational references

| Author | Work | Contribution |
|---|---|---|
| Wiener | *Cybernetics* (1948) | Negative feedback as control mechanism |
| Ashby | *Design for a Brain* (1952) | Requisite variety, black box, ultrastability |
| Beer | *Brain of the Firm* (1972) | VSM, variety absorption, algedonic channel |
| Maturana + Varela | *Tree of Knowledge* (1987) | Autopoiesis, structural coupling |
| Lem | *Golem XIV* (1981) | Epistemology as cognitive architecture |

---

## Honest limitations

**Analogies as claims.** Several `emergence` articles use cross-domain analogies (CLS→KB, RI→meta-harness) as foundations. These analogies are design heuristics, not demonstrated mechanisms. They are marked `(⚠️ our interpretation)` and `interpretation_confidence: low`, but still enter the graph if the oracle approves.

**Oracle staleness.** Gemini has a knowledge cutoff prior to 2026. "Invalidations" of 2026 papers are systematic false positives — require manual override. GPT-5.4 is the reliable model for recent papers.

**Retrieval sensor is conservative.** The `/dream` Phase 0.5 uses session logs as a retrieval proxy. Articles that exist but never appear in logs (because no relevant question was asked) will be marked as "not retrieved" — undercount, not false positive.

**No external ground truth — until now.** The calibration benchmark (see above) is the first attempt to measure epistemic quality against an external instrument. Results at T30 (2026-05-07).

---

> **Ashby's Law:** only variety destroys variety. `V(compiler) < V(domain)` → irreducible error floor. Adding more process does not increase `V(regulator)`. What does increase it is using the KB for real problems.
