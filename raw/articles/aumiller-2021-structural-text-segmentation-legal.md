# Structural Text Segmentation of Legal Documents

**Authors:** Aumiller et al.  
**arXiv:** 2012.03619  
**Published:** 2021  
**URL:** https://arxiv.org/abs/2012.03619  
**Type:** STUB — arxiv HTML não disponível; conteúdo baseado em análise do usuário

---

## Hipótese Central

Modelos transformer (BERT/RoBERTa) podem detectar fronteiras de segmentos em documentos legais multi-parágrafo com maior precisão que métodos baseados em sentença, formulando o problema como detecção de mudança tópica (topical coherence prediction).

---

## Evidências

- Ensemble de modelos transformer supera baselines de segmentação por sentença em Boundary Error Rate (Pk metric)
- Abordagem de topical coherence prediction funciona em granularidade de parágrafo, preservando coerência que modelos sentence-level perdem
- Ensembling com majority voting adiciona ganho sobre modelos individuais

---

## Limitações / Falsificadores

- Paper trabalha com documentos legais **judiciais europeus** — vocabulário compartilhado entre seções de DO brasileiro pode tornar a detecção tópica ineficaz (confirmado empiricamente pelo paper da UnB/PPGI)
- Custo computacional de ensemble pode ser proibitivo em contexto de processamento em escala
- Documentos legais administrativos (DOs) têm características diferentes de decisões judiciais: mais fórmulas fixas, menos argumentação narrativa

---

## Design Implication

Este paper representa o **baseline negativo** — a abordagem a NÃO adotar como estratégia primária para DOs brasileiros. A detecção tópica/semântica falha porque atos administrativos compartilham vocabulário similar independente de fronteiras. A alternativa correta é sequence labeling sobre tokens estruturais.

---

## Conexão com outros papers

- Contrasta com: Darji 2026 (rule-based supera ML para vocabulário estável)
- Contrasta com: UnB/PPGI 2021 (semantic segmentation falhou empiricamente para DOs)
- Relaciona com: HiCoBERT 2025 (hierarquia entre chunks como solução para docs longos)
