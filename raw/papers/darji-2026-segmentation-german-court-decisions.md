# Segmentation and Processing of German Court Decisions from Open Legal Data

**Authors:** Harshil Darji, Martin Heckelmann, Christina Kratsch, Gerard de Melo  
**Affiliation:** HTW Berlin / Hasso-Plattner Institute / University of Potsdam  
**arXiv:** 2601.01449 | **Published:** 2026-01-04  
**URL:** https://arxiv.org/abs/2601.01449

---

## Abstract

The availability of structured legal data is important for advancing NLP techniques for the German legal system. The Open Legal Data dataset provides a large-scale collection of German court decisions. While the metadata is consistently structured, decision texts are inconsistently formatted and often lack clearly marked sections. Reliable separation of sections is important for rhetorical role classification and downstream tasks such as retrieval and citation analysis.

This work introduces a cleaned and sectioned dataset of 251,038 German court decisions. The pipeline systematically separates three sections: Tenor (operative part), Tatbestand (facts of the case), and Entscheidungsgründe (judicial reasoning). Manual verification of 384 cases (statistically representative at 95% confidence, 5% margin) confirmed 97.40% ± 1.59% correct segmentation. The dataset is available in JSONL format via Hugging Face datasets.

---

## Key Finding

**Rule-based regex with fixed-vocabulary headers achieves 97.40% accuracy on structured legal documents.** For documents where boundary vocabulary is known and stable, rule-based approaches outperform ML — and have the advantage of being transparent, deterministic, and zero-shot.

---

## Methodology

### Extraction Pipeline

1. **HTML parsing:** Parse `content` attribute with HTML parser, iterate over `p`, `h1–h4`, `td`, and custom `rd` tags. Whitespace normalization; empty and duplicate lines skipped.

2. **Metadata normalization:** Resolve city and state identifiers via Open Legal Data public APIs. Missing entries set to `Unspecified`.

3. **Section boundary detection:** Fixed-vocabulary header recognition via two exact line-level patterns per section:
   - Compact form: `^\s*<marker>\s*:*$`
   - Spaced-letter form: `^\s*<m a r k e r>\s*:*$`
   
   Applied with **case insensitivity** and **full-line match** requirement.
   
   Section vocabulary: `tenor`, `tatbestand`, `entscheidungsgründe`, `gründe`

4. **Default section:** Active section defaults to `Tenor` until first header encountered — consistent with German legal drafting where all court decisions begin with Tenor.

5. **Decision type handling:**
   - *Urteile* (decisions with hearing): three sections explicit (Tenor + Tatbestand + Entscheidungsgründe)
   - *Beschlüsse* (decisions without hearing): Tenor + Gründe, where Gründe I = Tatbestand, Gründe II = Entscheidungsgründe

6. **Reference extraction:** Legal Reference Extraction tool identifies law citations and case citations by type.

### Verification Process (Cochran's Formula)

Sample size calculation for manual verification:

```
n₀ = Z² · p · (1-p) / e² = 1.96² · 0.5 · 0.5 / 0.05² ≈ 384
```

384 cases selected uniformly at random and manually reviewed. Correctness defined as: absence of overlap between sections.

**Result:** 97.40% correct segmentation (95% CI: 95.8%–98.9%)

Errors originated from rare HTML formatting irregularities, not model failure.

---

## Results

### Section Coverage (251,038 decisions)

| Section | Count | % |
|---------|-------|---|
| Tenor | 220,273 | 87.7% |
| Tatbestand | 164,222 | 65.4% |
| Entscheidungsgründe | 238,666 | 95.1% |
| Rechtsmittelbelehrung | 8,335 | 3.3% |

### Structural Composition

| Structure | Count | % |
|-----------|-------|---|
| All three sections | 144,383 | 57.5% |
| Tenor + Entscheidungsgründe only | 63,720 | 25.4% |
| Tenor only | 11,388 | 4.5% |

176 decisions (0.07%) had blank content fields — all sections absent.

---

## Applicability to RAG

The paper explicitly notes the RAG application: "In RAG systems, section-aware chunking can improve interpretability and prevent the model from mixing argumentative and operative content."

The segmented structure allows retrieval pipelines to separately index case summaries, statutory references, and reasoning paragraphs.

---

## Limitations

- German court decisions have **nationally uniform section vocabulary** — the fixed-vocabulary approach works because Tenor/Tatbestand/Entscheidungsgründe are legally mandated labels
- Brazilian DOs (Diário Oficial) have variable structure by UF, órgão, and municipal administration — section vocabulary is NOT stable
- The 2.60% error rate (1 in ~38 documents) comes from HTML irregularities — a problem also present in DO PDFs with OCR artifacts

---

## Design Implication for Non-Uniform Documents

The paper validates a design principle: **"regex where the vocabulary is stable; ML where it is not."**

For documents with predictable header vocabulary (federal DOE, São Paulo state), regex tier 1 is sufficient and preferable (deterministic, fast, zero training cost). For municipal DOs with variable formatting, a second tier (sequence labeler or structural classifier) is needed.

---

## Source

Dataset available at: https://huggingface.co/datasets/harshildarji/openlegaldata (JSONL, 251,038 decisions)
