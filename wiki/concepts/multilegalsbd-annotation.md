---
reads: 1
last_read: 2026-04-13
retrievals_correct: 1
title: "MultiLegalSBD — Metodologia de Anotação para Boundary Detection"
sources:
  - path: raw/articles/multilegalsbd-2023-sentence-boundary-detection.md
    type: article
    quality: primary
    stance: confirming
  - path: raw/papers/pena-2023-document-layout-public-affairs.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-13
updated: 2026-04-14
tags: [anotacao, boundary-detection, legal, nlp, dataset, zelox]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
---

## Resumo

**Distinção crítica:** DLA/layout analysis (Peña 2023) e act boundary detection são tarefas diferentes — usar como inspiração de anotação/bootstrapping, não como solução substituta.

MultiLegalSBD (arXiv 2305.01211) fornece dataset multilíngue de sentence boundary detection em textos legais com guidelines explícitos de anotação, atingindo F1 98.5% in-distribution e 81.1% out-of-distribution (alemão não-visto). O gap in→out é crítico: 17 pp de degradação. O problema do Zelox (act boundary detection em DOs) é um nível acima de sentence boundary — não existe dataset público para esse problema.

## Conteúdo

### Guidelines de Anotação (Transferíveis)

- Ferramenta: Prodigy (ou alternativa open source: Doccano, Label Studio)
- Decisão: anotar o span completo da sentença, não apenas terminadores — incentiva leitura completa pelo anotador
- Divisão de documentos longos: 1-3 artigos por chunk; divisão apenas acima de ~15.000 caracteres
- **Regras para casos ambíguos documentadas:** colons + newline, listas com itens incompletos, abreviações

### Resultados de Generalização

| Configuração | F1 |
|-------------|-----|
| CRF in-distribution | 98.5% |
| NN in-distribution | 98.5% |
| CRF out-of-distribution (alemão não-visto) | 81.1% |
| Modelos multilíngues zero-shot PT (abstract 2305.01211) | 91.6% |

**Dataset completo:** 130.000+ sentenças anotadas em 6 línguas. Modelos multilíngues superam todos os baselines em zero-shot PT — relevante para Zelox: um modelo multilíngue treinado no corpus MultiLegalSBD pode aplicar zero-shot a DOs em PT sem fine-tuning adicional, com F1~91.6% para sentence boundary (não act boundary).

**Gap in→out: 17 pp.** Implica: modelo treinado em um estado de DO pode degradar 17+ pp em outro estado com vocabulário de cabeçalhos diferente. Validação por UF é necessária.

### O Gap Para o Zelox

MultiLegalSBD resolve sentence boundary (onde termina a sentença). O Zelox precisa de act boundary (onde termina o ato administrativo).

| Problema | Nível | Status |
|----------|-------|--------|
| Sentence boundary em texto legal | Token-level | Resolvido (F1 98.5%) |
| Act boundary em DOs brasileiros | Documento-level | Não existe dataset público |

Act boundary é estruturalmente diferente: envolve reconhecer cabeçalhos, assinaturas, numerações de atos — não apenas terminadores de sentença.

### Anotação Semi-Automática em Escala: Peña et al. 2023

Peña et al. (2023) construíram um dataset de Document Layout Analysis para a administração pública espanhola usando anotação **semi-automática**: 37.900 documentos, 441.000+ páginas, 8M+ labels, accuracy até 99%. Fontes: 24 datasets da administração espanhola.

Implicação para custo de anotação Zelox: o método semi-automático reduz drasticamente o custo vs. anotação manual pura. A estimativa de 250h por UF (baseada em 30 min/doc × 500 atos) pode ser reduzida com procedimento semi-automático — porém apenas para layout block detection (4 blocos estruturais + 4 categorias de texto), não diretamente para act boundary detection.

**Gap de transferência:** DLA (Document Layout Analysis) e act boundary detection são tarefas diferentes:
- DLA: detectar blocos visuais (texto, tabela, figura, header) → problema de visão computacional
- Act boundary: detectar onde termina um ato administrativo → problema de NLP estrutural

A metodologia semi-automática de Peña 2023 é transferível para a fase de bootstrapping do dataset Zelox, mas não resolve diretamente a tarefa de boundary detection.

### Schema de Anotação Necessário (Para Zelox)

Transferindo a metodologia do paper ao domínio de DOs:

1. **Definição formal de "ato":** o que é e o que não é um ato completo (extrato de contrato, portaria, aviso, despacho)
2. **Casos ambíguos:**
   - Atos que referenciam outros ("nos termos do Contrato nº X")
   - Republicações ("Republicado por incorreção")
   - Erratas
   - Atos conjuntos de múltiplos órgãos
3. **Critério IAA** (Inter-Annotator Agreement): definir antes de treinar
4. **Tamanho mínimo por UF:** 300-500 exemplos para CRF-LSTM convergir

### Paper Relacionado: Leitner et al. (Fine-Grained NER Legal)

67.000 sentenças, 54.000 entidades, 19 classes semânticas. Finding central: não existe tipologia uniforme de conceitos semânticos legais — as guidelines precisam ser construídas do zero para cada domínio.

Implicação: o Annotation Schema Document para Zelox deve definir as entidades do domínio B2G brasileiro antes de anotar qualquer linha.

## Interpretação

(⚠️ nossa interpretação) O gap 98.5%→81.1% out-of-distribution tem implicação direta para Zelox multi-UF: um modelo treinado em DODF (Brasília) pode degradar para 80% em DOM-SP por diferenças de formatação. Estratégia de mitigação: tier 1 regex (para vocabulário estável) + tier 2 ML (com dados de cada UF).

(⚠️ nossa interpretação) Tamanho mínimo de 300-500 exemplos por UF é custo de anotação concreto para planejar. A 30 min por documento, 500 atos = ~250h de anotação por UF.

## Conexões

- partOf: [[diario-oficial-segmentation-strategies]] — metodologia de referência para construir dataset de boundary detection
- partOf: [[legal-bert-pt-models]] — modelos de base para treinar após dataset construído

## Fontes

- [MultiLegalSBD 2023](../../raw/articles/multilegalsbd-2023-sentence-boundary-detection.md) — guidelines, F1 98.5% in-dist / 81.1% OOD, gap de generalização crítico, schema de anotação transferível
- [Peña et al. 2023](../../raw/papers/pena-2023-document-layout-public-affairs.md) — 37.9K docs administração espanhola; DLA semi-automático; accuracy 99%; metodologia de bootstrapping transferível
