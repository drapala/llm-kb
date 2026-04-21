# Legal Document Segmentation and Labeling Through Named Entity Recognition Approaches

**Título completo:** Legal Document Segmentation and Labeling Through Named Entity Recognition Approaches  
**Journal:** Journal of Information and Data Management (JIDM), 2024, 15:1  
**DOI:** 10.5753/jidm.2024.3368  
**Autores:** Gabriel M. C. Guimarães, Felipe X. B. da Silva, Lucas A. B. Macedo, Victor H. F. Lisboa, Ricardo M. Marcacini (USP), Andrei L. Queiroz, Vinicius R. P. Borges, Thiago P. Faleiros, Luís P. F. Garcia — Universidade de Brasília  
**URL:** https://journals-sol.sbc.org.br/index.php/jidm/article/view/3368  
**Recebido:** 29 April 2023 | **Publicado:** 23 February 2024

**Versão anterior:** da Silva et al. 2022 (KDMiLe) — este paper expande com novos experimentos e IAA detalhado

---

## Abstract

The document segmentation task allows us to divide documents into smaller parts, known as segments, which can then be labelled within different categories. We tackle the problem of document segmentation and segment labeling focusing on official gazettes or legal documents. They have a structure that can benefit from token classification approaches, especially Named Entity Recognition (NER), since they are divided into labelled segments. We use word-based and sentence-based CRF, CNN-CNN-LSTM and CNN-biLSTM-CRF models to bring together text segmentation and token classification. We propose a new annotated dataset named PersoSEG composed of 127 documents in Portuguese from the Official Gazette of the Federal District, published between 2001 and 2015, with a Krippendorff's alpha agreement coefficient of 0.984. CRF word-based achieved average F1-Score of 75.65% for 12 different categories of segments.

---

## Dataset: PersoSEG

- **Fonte:** Diário Oficial do Distrito Federal (DODF), Seção II (atos de pessoal)
- **Período:** 2001–2015
- **Documentos:** 127 gazettes (seção II extraída)
- **Atos anotados:** 9.058 atos, 12 tipos
- **IAA:** Krippendorff's alpha = **0.984** (qualidade muito alta)
- **Disponível:** open access (notebooks e scripts também)

### 12 Tipos de Ato (Seção II — Pessoal):
- Permanence Allowance (Abono de Permanência)
- Cession (Cessão)
- Dismissal of Commissioned Position
- Dismissal of Effective Position
- Nomination of Commissioned Position
- Nomination of Effective Position
- Rectification of Commissioned Appointment
- Rectification of Effective Appointment
- Reversal
- Substitution
- Rendered Ineffective Retirement Acts
- Rendered Ineffective Dismissal or Nomination

---

## Abordagem: Segmentação como NER

- IOB tagging: B-X (início de ato), I-X (interior), E-X (fim), O (fora de ato)
- Modelos word-based: cada palavra tem label individual
- Modelos sentence-based: uma label por sentença
- Formulação evita separação em dois passos (segmentar → classificar) — faz os dois simultaneamente

---

## Resultados

### Modelos Word-Based (Table 4)

| Act type | CRF (%) | CNN-CNN-LSTM (%) | CNN-biLSTM-CRF (%) |
|----------|---------|-----------------|---------------------|
| Permanence Allowance | 19.67 ± 39.35 | 71.51 ± 17.18 | 66.86 ± 20.69 |
| Cession | 99.10 ± 0.68 | 96.31 ± 1.94 | 86.15 ± 6.39 |
| Dismissal Commissioned | 99.50 ± 0.10 | 39.73 ± 48.65 | 14.37 ± 24.89 |
| Dismissal Effective | 97.58 ± 1.40 | 42.10 ± 42.05 | 0.0 ± 0.0 |
| Nomination Commissioned | 99.72 ± 0.11 | 43.44 ± 32.59 | 74.90 ± 17.61 |
| Nomination Effective | 92.26 ± 7.05 | 55.40 ± 21.88 | 37.53 ± 16.47 |
| Rectification Commissioned | 86.38 ± 2.92 | 39.24 ± 32.44 | 26.57 ± 31.53 |
| Rectification Effective | 96.19 ± 0.58 | 84.63 ± 8.10 | 81.59 ± 10.49 |
| Reversal | 7.01 ± 14.03 | 52.63 ± 26.91 | 30.63 ± 35.27 |
| Substitution | 99.78 ± 0.26 | 77.15 ± 38.62 | 53.71 ± 38.97 |
| Rendered Ineffective Retirement | 12.66 ± 25.31 | — | — |
| Rendered Ineffective Dismissal/Nomination | 97.90 ± 1.30 | — | — |
| **Mean** | **75.65 ± 7.76** | — | — |

**CRF supera CNN-CNN-LSTM e CNN-biLSTM-CRF na maioria dos tipos.**

### Padrão Crítico: Volume de Dados vs Desempenho

- Act types com >1000 exemplos → F1 >90% em todos os modelos
- Act types com <100 exemplos (Reversal: 58, Rendered Ineffective Retirement: 20) → F1 muito baixo, alta variância
- Implicação direta: frequência de tipo de ato controla desempenho; tipos raros precisam de oversampling ou estratégias específicas

---

## Relação com Trabalho Anterior (KDMiLe 2022)

- Da Silva et al. 2022 (KDMiLe) é versão preliminar: dataset idêntico, CNN models com problemas de encoding
- JIDM 2024 reprocessou CNN-CNN-LSTM e CNN-biLSTM-CRF (encoding corrigido) — resultados diferentes
- KDMiLe 2022 reportou "CRF sentence-based melhor"; JIDM 2024 reporta "CRF word-based melhor"
- **Versão autoritativa:** JIDM 2024

---

## Limitações

- Dataset cobre apenas **Seção II (atos de pessoal)** do DODF — NÃO cobre contratos, licitações, portarias normativas
- Período 2001–2015: formato pode ter mudado; desde maio 2020 DODF já vem segmentado online
- 127 documentos; 9.058 atos: pequeno para deep learning; adequado para CRF
- Não testado em outros estados (generalização cross-UF desconhecida)
- Não usa BERT/transformers fine-tuned: baseline forte não testado

---

## Implicações para Zelox

1. **Dataset de referência**: PersoSEG é o único dataset público de segmentação de DODF por tipo de ato
2. **CRF word-based F1=75.65%** para atos de pessoal — baseline para comparação
3. **Gap crítico**: Seção II (pessoal) ≠ Seção III (contratos/licitações) — PersoSEG não cobre o domínio B2G
4. **Padrão de volume**: tipos raros precisam de pelo menos ~300 exemplos para CRF convergir — confirma estimativa de MultiLegalSBD
