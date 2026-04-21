---
reads: 1
last_read: 2026-04-13
retrievals_correct: 1
title: "PersoSEG — Dataset e Resultados de Segmentação NER para DODF"
sources:
  - path: raw/papers/guimaraes-2024-persoseg-dodf-ner-segmentation.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/articles/unb-ppgi-2021-segmentacao-diario-oficial.md
    type: note
    quality: primary
    stance: confirming
created: 2026-04-14
updated: 2026-04-14
tags: [segmentacao, diario-oficial, ner, crf, dataset, zelox, dodf, persoseg]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
---

## Resumo

Guimarães et al. (JIDM 2024) do grupo UnB/USP (Faleiros, Garcia et al.) apresentam PersoSEG: primeiro dataset público de segmentação por tipo de ato do DODF — 127 documentos, 9058 atos, 12 categorias, Seção II (pessoal). CRF word-based atingiu F1=75.65% médio. Resultado crítico: atos com >1000 exemplos → F1>90%; atos raros (<100 exemplos) → F1 muito baixo. Seção II (pessoal) ≠ Seção III (contratos/licitações) — gap direto para Zelox.

## Conteúdo

### Dataset PersoSEG

- **Corpus:** Diário Oficial do Distrito Federal (DODF), Seção II — atos de pessoal (nomeações, exonerações, cessões, aposentadorias)
- **Período:** 2001–2015 (127 documentos, 9.058 atos anotados)
- **12 categorias de ato:** Permanence Allowance, Cession, Dismissal (Commissioned/Effective), Nomination (Commissioned/Effective), Rectification (2 tipos), Reversal, Substitution, Rendered Ineffective Retirement, Rendered Ineffective Dismissal/Nomination
- **IAA:** Krippendorff's alpha = 0.984 (qualidade de anotação muito alta)
- **Open access:** dataset + notebooks + scripts + hiperparâmetros

### Abordagem: Segmentação como NER

IOB tagging aplicado a atos administrativos:
- B-X: token inicial do ato tipo X
- I-X: token interno do ato
- E-X: token final do ato
- O: fora de qualquer ato

Modelos testados:
- Word-based: cada palavra recebe label IOB
- Sentence-based: cada sentença recebe label IOB
- Arquiteturas: CRF (clássico), CNN-CNN-LSTM, CNN-biLSTM-CRF

### Resultados Word-Based

| Modelo | F1 médio |
|--------|---------|
| **CRF word-based** | **75.65% ± 7.76%** |
| CNN-CNN-LSTM | inferior (encoding issues na versão 2022 corrigidos) |
| CNN-biLSTM-CRF | inferior |

CRF word-based superou as abordagens neurais na maioria dos tipos de ato.

### Padrão de Desempenho vs Volume

| Volume de exemplos | F1 típico |
|--------------------|-----------|
| > 1.000 exemplos | > 90% em todos os modelos |
| 100–1.000 exemplos | 80–96% (CRF) |
| < 100 exemplos | < 20% (alta variância) |

- Cession (frequente): CRF F1 = 99.10%
- Reversal (58 exemplos): CRF F1 = 7.01% ± 14.03%
- Rendered Ineffective Retirement (20 exemplos): CRF F1 = 12.66% ± 25.31%

**Implicação direta:** tipos raros precisam de oversampling, data augmentation, ou threshold mínimo de exemplos antes de treinar.

### Relação com a Versão KDMiLe 2022

Da Silva et al. 2022 (KDMiLe) é a versão preliminar do mesmo trabalho. O paper JIDM 2024:
- Corrige problemas de encoding nos modelos CNN
- Adiciona IAA detalhado (Krippendorff's alpha)
- Revisão da conclusão: KDMiLe 2022 reportou "CRF sentence-based melhor"; JIDM 2024 corrige para "CRF word-based melhor"
- **Versão autoritativa para citação:** JIDM 2024

Este grupo (Faleiros, Garcia, Borges, Queiroz, UnB) é o mesmo do seminário PPGI que estabeleceu a hipótese de NER-as-segmentation para DOs.

## Interpretação

(⚠️ nossa interpretação) O PersoSEG é o único dataset público de segmentação de atos do DODF. Mas cobre **Seção II (pessoal)** — portarias de nomeação, exoneração, cessão. O Zelox precisa da **Seção III (contratos, extratos de licitação, avisos)** — vocabulário diferente, estrutura diferente, tipos de ato diferentes.

(⚠️ nossa interpretação) F1=75.65% para atos de pessoal é um baseline conservador. Para atos de contrato (extratos com CNPJ, valor, modalidade), o vocabulário é mais padronizado (fórmulas jurídicas fixas) — CRF provavelmente atinge F1 mais alto, mais próximo dos 90-99% observados nos tipos frequentes do PersoSEG.

(⚠️ nossa interpretação) O padrão "volume > 1000 → F1 > 90%" calibra a estimativa de anotação: para tipos de ato de licitação frequentes (extrato de contrato, aviso de licitação), 1000 exemplos por UF provavelmente garante F1 > 90%. Para tipos raros (dispensa de licitação por emergência), oversampling ou fewer-shot é necessário.

(⚠️ nossa interpretação) BERT fine-tuned não foi testado — seria o próximo passo natural. LegalBert-pt ou RoBERTaLexPT como backbone para sequence labeling pode superar CRF (hipótese não testada neste paper).

## Verificação Adversarial

**Claim mais fraco:** "CRF word-based atinge 75.65% F1 médio" — este número é média de 12 categorias com altíssima variância (7% a 99%). A média não é representativa.

**O que o paper NÃO diz:**
1. Não testa em outros estados (DOM-SP, DOE-RJ) — zero dados de generalização
2. Não testa BERT/transformers — CRF pode não ser o teto
3. Não cobre Seção III (contratos) — o domínio mais relevante para Zelox

**Simplificações feitas:** o resumo "CRF melhor que CNN" oculta que CNN-biLSTM-CRF teve F1=0% em Dismissal Effective — falha total em alguns tipos, não apenas desempenho inferior.

**Prior work:** Aumiller et al. 2021 (baseline negativo para topical coherence), Barrow et al. 2020 (S-LSTM), Arnold et al. 2019 (SECTOR).

## Conexões

- validates: [[diario-oficial-segmentation-strategies]] — confirma NER/CRF como abordagem correta com dados quantitativos para DODF
- partOf: [[diario-oficial-segmentation-strategies]] — PersoSEG é o dataset de referência para segmentação de DODF
- partOf: [[multilegalsbd-annotation]] — metodologia de anotação complementar; MultiLegalSBD é sentence-level, PersoSEG é act-level
- derivedFrom: [[legal-bert-pt-models]] — LegalBert-pt/RoBERTaLexPT como possível backbone para superar CRF (hipótese não testada)

## Fontes

- [Guimarães et al. 2024 (JIDM)](../../raw/papers/guimaraes-2024-persoseg-dodf-ner-segmentation.md) — PersoSEG dataset, CRF F1=75.65%, padrão volume→F1
- [UnB/PPGI Seminar](../../raw/articles/unb-ppgi-2021-segmentacao-diario-oficial.md) — hipótese original (mesmo grupo); versão oral do mesmo trabalho

## Quality Gate

- [x] Wikilinks tipados: 4 relações tipadas
- [x] Instance→class: F1=75.65% qualificado como "em DODF Seção II, dataset PersoSEG"
- [x] Meta-KB separado: sim — referências Zelox em Interpretação
- [x] Resumo calibrado: sim — gap PersoSEG→contratos explicitado
