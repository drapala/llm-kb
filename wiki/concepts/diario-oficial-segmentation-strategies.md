---
reads: 1
last_read: 2026-04-13
retrievals_correct: 1
title: "Segmentação de Diários Oficiais — Estratégias"
sources:
  - path: raw/articles/unb-ppgi-2021-segmentacao-diario-oficial.md
    type: note
    quality: primary
    stance: confirming
  - path: raw/papers/darji-2026-segmentation-german-court-decisions.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/articles/aumiller-2021-structural-text-segmentation-legal.md
    type: article
    quality: secondary
    stance: confirming
  - path: raw/articles/okbr-querido-diario-ecosystem.md
    type: note
    quality: secondary
    stance: confirming
  - path: raw/papers/cacaio-2022-dou-environmental-tracking.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-13
updated: 2026-04-14
reads: 1
retrievals_correct: 1
last_read: 2026-04-14
tags: [segmentacao, diario-oficial, boundary-detection, ner, zelox, nlp]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - wiki/concepts/semantic-chunking-cost-benefit.md
---

## Resumo

**Anchor estabelecido pelo corpus (2026-04-14):** A literatura existente de NLP em DOs brasileiros parte de atos já extraídos — nenhum paper resolve a extração bruta. Act boundary detection permanece o primeiro bottleneck não resolvido no campo.

**Resultado empírico H1 (2026-04-14):** Regex tier 1 validado em DODF **e DOE-SP** — Precision 0.980, Recall 1.000, F1 **0.990**, Pk 0.001. Acima do threshold de GO (0.95). Generalização cross-UF confirmada para pelo menos dois estados. Tier 2 ML não obrigatório para DODF/DOE-SP no MVP.

Segmentação de Diários Oficiais brasileiros por ato administrativo é um problema de boundary detection estrutural, não de classificação semântica. Abordagem correta é sequence labeling análogo a NER (CRF-LSTM) sobre tokens estruturais — segmentação semântica falha porque atos compartilham vocabulário similar. Para documentos com vocabulário de cabeçalhos estável (DOs federais), regex rule-based (97.4% acurácia) é suficiente e preferível. O Querido Diário (OKBR) resolve o acesso aos PDFs e faz segmentação por município em DOs agregados — mas deixa o fatiamento por ato explicitamente em aberto. Adicionalmente: PDF Imagem não é suportado pelo QD.

## Conteúdo

### O Problema: Três Topologias de DO

O OKBR/Querido Diário identificou empiricamente três padrões de publicação:

| Topologia | Descrição | Estratégia |
|-----------|-----------|-----------|
| Individual | Cada ato publicado como arquivo separado | Trivial — sem segmentação necessária |
| Fragmentado | PDF com atos por quebra de página | Regex por estrutura de página |
| Agregado | DO completo em único PDF, atos não separados | O problema difícil |

Para a maioria dos municípios (topologia Agregada): o pipeline é PDF → PyMuPDF (extração texto) → OpenSearch (full-text), sem segmentação por ato. Isso é insuficiente para retrieval por entidade de contrato.

### Por que Semantic Segmentation Falha para DOs

UnB/PPGI (2021): experimentos com segmentação semântica/tópica falharam no DODF. Razão: atos administrativos compartilham vocabulário especializado similar entre categorias (portaria, extrato, aviso usam os mesmos termos normativos). Não há sinal tópico suficiente para detectar fronteiras.

Aumiller et al. (2021) — baseline negativo: modelos transformer para topical coherence prediction funcionam em decisões judiciais europeias (narrativa argumentativa), mas documentos administrativos têm mais fórmulas fixas e menos argumentação.

### Abordagem Correta: Sequence Labeling Análogo a NER

CRF-LSTM identificando tokens de fronteira estrutural foi validado com dados quantitativos: Guimarães et al. (JIDM 2024) publicaram PersoSEG — 127 docs DODF, 9.058 atos, 12 categorias — com CRF word-based atingindo **F1=75.65%** médio. Atos frequentes (>1000 exemplos): F1>90%. Atos raros (<100 exemplos): F1<20%.

Tokens-alvo para sequence labeling:
- Cabeçalhos tipográficos: `PORTARIA Nº`, `EXTRATO DE CONTRATO`, `AVISO DE LICITAÇÃO`
- Padrões de numeração: `Art. X`, `§ Y`, `item Z`
- Tokens de assinatura/autoridade: `Secretário de Estado`, `Prefeito Municipal`
- Datas e locais de publicação

A formulação correta é: detectar tokens de fronteira estrutural (análogo a B-ENT/I-ENT em NER), não classificar o conteúdo semanticamente.

### Evidência de Vocabulário Estável: Darji 2026 (Alemanha)

Para documentos com vocabulário de cabeçalhos legalmente mandatório e estável, regex rule-based supera ML:

- 251.038 decisões judiciais alemãs segmentadas com 97.40% ± 1.59% de acurácia
- Pipeline: regex com case-insensitivity + full-line match para `tenor`, `tatbestand`, `entscheidungsgründe`
- Erros (2.6%) originam de irregularidades HTML, não de falha do modelo
- Custo: zero — determinístico, sem treinamento

**Princípio derivado: "regex onde o vocabulário é estável; ML onde não é."**

Aplicabilidade ao Brasil:
- DOs federais (Senado, Casa Civil) têm estrutura parcialmente mandatória → tier 1 regex plausível
- DOs municipais têm estrutura variável por UF e gestão → ML necessário (tier 2)

### Querido Diário — O que Já Existe (e o que Não)

Pipeline atual do OKBR (documentação oficial 2026):
- **350+ municípios** integrados; meta: 5570 — ainda longe da cobertura total
- Stack: Scrapy → **Apache Tika** (extração de texto PDF/DOC/DOCX) → OpenSearch (full-text + filtros temáticos)
- Armazenamento: DO Spaces (arquivos) + PostgreSQL (metadados) + OpenSearch (índice)
- API pública: FastAPI em api.queridodiario.ok.org.br/docs
- Spiders open source reutilizáveis; naming convention `uf_nome_do_municipio`; IBGE territory_id

**Distinção crítica — "segmentadores" do QD ≠ segmentação por ato:**

O QD implementa "segmentadores" para DOs agregados (um PDF cobrindo múltiplos municípios), que fatiam o arquivo **por município** — produzem arquivos TXT individuais por município. Isso é segmentação de nível municipal, não de nível de ato.

| Nível | O que o QD faz | Status |
|-------|---------------|--------|
| Município | Segmentador: fatia DO estadual por município | Suportado (DOs agregados) |
| Ato | Portaria / Extrato / Aviso individual | **Em aberto — não implementado** |

**Limitações explicitadas na documentação:**
- **PDF Imagem não suportado** — OCR com baixa qualidade não está integrado; DOs em formato scaneado ficam de fora
- **Fragmentados não suportados** — limitação de modelagem do banco de dados
- `power` field (Gazette class): `'executive'` ou `'executive_legislative'` — útil como filtro mas não como sinal de ato

Gap explicitamente em aberto: fatiamento por ato, extração de entidades, estrutura hierárquica.

### Evidência de Processabilidade do DOU: Cação et al. 2022

Cação et al. (2022) construíram o Government Actions Tracker — dataset de atos do DOU federal anotados por especialistas em política ambiental, em português. Resultado: F1=0.714 ± 0.031 em classificação de atos por relevância ambiental.

Implicação crítica para Zelox: o paper opera sobre atos individualmente, pressupondo que a segmentação já foi resolvida. O paper **não explica** como os atos foram isolados — a etapa de boundary detection é tratada como pré-requisito implícito, confirmando que ela é o bottleneck real do pipeline DOU.

Implicação adicional: F1=0.714 para classificação temática com anotação de especialistas é o teto de referência para tasks downstream em DOs. Segmentação (o problema Zelox) é upstream e gating para este F1.

O que o Zelox faz além do QD:
1. Segmentação por ato (boundary detection — o problema que o QD deixou em aberto)
2. Extração de entidades (CNPJ, valor, modalidade, objeto)
3. Indexação tri-camada (entidade / ato / resumo)
4. Suporte a PDF Imagem via OCR (gap não coberto pelo QD)

## Interpretação

(⚠️ nossa interpretação) Arquitetura de dois tiers para Zelox:

**Tier 1 — Regex (DOs com vocabulário estável):** Regex para cabeçalhos padronizados (ex: DOE-SP, DOU). Determinístico, sem custo de treinamento. Aplica Darji 2026 ao contexto BR.

**Tier 2 — Sequence Labeling (DOs com vocabulário variável):** CRF-LSTM ou BERT fine-tuned como sequence labeler para boundary detection. Treinado por UF ou cluster de UFs. Aplica abordagem UnB/PPGI.

(⚠️ nossa interpretação) Gap de dados: nenhum dataset público de boundary annotation para DOs brasileiros existe. Construção do dataset de anotação (seguindo metodologia MultiLegalSBD) é pré-requisito para o tier 2.

## Conexões

- validates: [[semantic-chunking-cost-benefit]] — semantic segmentation não é a abordagem correta para DOs
- derivedFrom: [[legal-bert-pt-models]] — modelos PT-BR para sequence labeling
- derivedFrom: [[multilegalsbd-annotation]] — metodologia de anotação para construir dataset de boundary detection
- complementa: [[hybrid-search]] — após segmentação, indexação tri-camada para retrieval
- partOf: [[document-image-quality-assessment]] — DIQA como triagem da Camada 2 (antes da segmentação)

## Fontes

- [UnB/PPGI — Micael Lima / Prof. Faleiros](../../raw/articles/unb-ppgi-2021-segmentacao-diario-oficial.md) — semantic segmentation falhou para DODF; CRF-LSTM como abordagem correta para boundary detection
- [Darji et al. 2026](../../raw/papers/darji-2026-segmentation-german-court-decisions.md) — 97.40% com regex rule-based em 251.038 decisões; "regex onde vocabulário é estável"
- [Aumiller et al. 2021](../../raw/articles/aumiller-2021-structural-text-segmentation-legal.md) — baseline negativo: topical coherence falha para documentos administrativos
- [OKBR Querido Diário](../../raw/articles/okbr-querido-diario-ecosystem.md) — 350+ municípios; segmentadores = nível municipal (não ato); PDF Imagem não suportado; stack: Apache Tika + OpenSearch + FastAPI; spiders reutilizáveis
- [Cação et al. 2022](../../raw/papers/cacaio-2022-dou-environmental-tracking.md) — DOU Federal como corpus NLP; F1=0.714 em classificação de atos ambientais; segmentação implicitamente assumida resolvida
