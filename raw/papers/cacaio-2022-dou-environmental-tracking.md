# Tracking Environmental Policy Changes in the Brazilian Federal Official Gazette

**Source:** arXiv 2202.10221  
**Authors:** Flávio Nakasato Cação, Anna Helena Reali Costa, Natalie Unterstell, Liuca Yonaha, Taciana Stec, Fábio Ishisaki  
**Published:** 2022-02-11  
**Venue:** cs.IR, cs.LG  
**URL:** https://arxiv.org/pdf/2202.10221v1

---

## Abstract

Even though most of its energy generation comes from renewable sources, Brazil is one of the largest emitters of greenhouse gases in the world, due to intense farming and deforestation of biomes such as the Amazon Rainforest, whose preservation is essential for compliance with the Paris Agreement. Still, regardless of lobbies or prevailing political orientation, all government legal actions are published daily in the Brazilian Federal Official Gazette (BFOG, or "Diário Oficial da União" in Portuguese). However, with hundreds of decrees issued every day by the authorities, it is absolutely burdensome to manually analyze all these processes and find out which ones can pose serious environmental hazards. In this paper, we present a strategy to compose automated techniques and domain expert knowledge to process all the data from the BFOG. We also provide the Government Actions Tracker, a highly curated dataset, in Portuguese, annotated by domain experts, on federal government acts about the Brazilian environmental policies. Finally, we build and compared four different NLP models on the classification task in this dataset. Our best model achieved a F1-score of 0.714 ± 0.031. In the future, this system should serve to scale up the high-quality tracking of all official documents with a minimum of human supervision and contribute to increasing society's awareness of government actions.

---

## Key Findings

### Dataset: Government Actions Tracker (GAT)
- **Source:** Brazilian Federal Official Gazette (DOU — Diário Oficial da União)
- **Language:** Portuguese
- **Domain:** Federal government acts on environmental policies
- **Annotation:** Domain experts (environmental policy specialists)
- **Task:** Multi-class classification of government acts by environmental relevance

### NLP Pipeline
- **Input:** Raw text from DOU acts
- **Task type:** Document classification (not segmentation)
- **Models compared:** 4 NLP models (not specified in abstract — likely BERT variants + baselines)
- **Best F1:** 0.714 ± 0.031
- **Approach:** Composing automated NLP with domain expert knowledge

### Relevance to DOU Processing
This paper demonstrates:
1. **DOU text is processable at act level** — the pipeline operates on individual government acts, implying the DOU was already segmented or acts were individually sourced
2. **Domain expert annotation is necessary** — F1=0.714 reflects the challenge of domain-specific classification in the DOU
3. **Portuguese NLP for government acts works** — DOU text is machine-readable (digital PDF assumed, not scanned images)

## Gaps / Limitations (from abstract)

- Does not cover segmentation (assumes acts are pre-extracted)
- Does not address PDF quality or OCR pipeline
- Classification-only — no extraction of structured entities (CNPJ, valor, objeto)
- Domain-specific (environmental) — not general-purpose DOU processing

## Relevance to Zelox

- **Confirms:** DOU acts can be individually classified/processed with NLP in Portuguese
- **Confirms:** F1~0.71 is achievable for classification even with expert-annotated dataset
- **Gap it reveals:** The paper doesn't explain how individual acts were isolated from the DOU — the segmentation problem is implicit/assumed solved
- **Analog:** Zelox does segmentation + NER on the SAME corpus (DOU/DOE); classification is downstream of what Zelox does
