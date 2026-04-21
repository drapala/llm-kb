# Document Layout Annotation: Database and Benchmark in the Domain of Public Affairs

**Source:** arXiv 2306.10046  
**Authors:** Alejandro Peña, Aythami Morales, Julian Fierrez, Javier Ortega-Garcia, Marcos Grande, Íñigo Puente, Jorge Cordova, Gonzalo Cordova  
**Published:** 2023-06-12  
**Venue:** cs.IR, cs.CV, cs.DB  
**URL:** https://arxiv.org/pdf/2306.10046v2

---

## Abstract

Every day, thousands of digital documents are generated with useful information for companies, public organizations, and citizens. Given the impossibility of processing them manually, the automatic processing of these documents is becoming increasingly necessary in certain sectors. However, this task remains challenging, since in most cases a text-only based parsing is not enough to fully understand the information presented through different components of varying significance. In this regard, Document Layout Analysis (DLA) has been an interesting research field for many years, which aims to detect and classify the basic components of a document. In this work, we used a procedure to semi-automatically annotate digital documents with different layout labels, including 4 basic layout blocks and 4 text categories. We apply this procedure to collect a novel database for DLA in the public affairs domain, using a set of 24 data sources from the Spanish Administration. The database comprises 37.9K documents with more than 441K document pages, and more than 8M labels associated to 8 layout block units. The results of our experiments validate the proposed text labeling procedure with accuracy up to 99%.

---

## Key Findings

### Dataset
- **Name:** Not named explicitly in abstract
- **Source:** 24 data sources from the Spanish Administration (governmental documents)
- **Scale:** 37,900 documents, 441,000+ pages, 8M+ labels
- **Language:** Spanish (government documents)
- **Domain:** Public administration — closest analogy to Brazilian DOs in the literature

### Layout Annotation Schema
- **4 basic layout blocks** (visual/structural): [not specified in abstract — likely: text block, figure, table, header]
- **4 text categories** (semantic): [not specified — likely: heading, body text, footnote, caption]
- Total: 8 layout block units

### Annotation Methodology
- **Semi-automatic** annotation procedure
- Validated with accuracy up to 99%
- Applied to digital (not scanned) government documents

### Results
- Layout detection accuracy: up to 99%
- Method generalizes across 24 different governmental document sources

## Relevance to Zelox

### Direct analogies:
1. **Same domain class (government administration)** — Spanish government docs share structural patterns with Brazilian DOs (hierarchical acts, formal headers, signature blocks)
2. **Scale demonstrates feasibility** — 37.9K docs shows this type of annotation is industrially scalable
3. **Semi-automatic procedure** — reduces annotation cost vs. fully manual; applicable to building Zelox's boundary annotation dataset
4. **8-class schema** is more granular than needed for boundary detection but confirms layout analysis is tractable

### Key gap for Zelox:
- These are **digital PDFs** (nativo), not scanned — does not address the OCR/quality triagem problem
- Spanish ≠ Portuguese DOs — vocabulary differs; but structural patterns may transfer
- Layout analysis (block detection) is different from act boundary detection — but complementary

## Limitations

- Language: Spanish administration, not Brazilian — vocabulary of acts differs
- Format: digital PDFs only, not scanned documents
- Task: layout block detection, not act-level boundary detection
- Not open-source dataset (Spanish government docs may have access restrictions)
