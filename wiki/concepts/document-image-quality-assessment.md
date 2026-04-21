---
title: "Document Image Quality Assessment (DIQA)"
sources:
  - path: raw/papers/ma-2025-dociq-document-image-quality.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-14
updated: 2026-04-14
tags: [ocr, pdf, qualidade, zelox, computer-vision, nlp]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
reads: 0
retrievals_correct: 0
last_read: null
---

## Resumo

**Escopo:** DIQA é relevante para PDFs escaneados — não justifica complexidade extra no caminho nativo. Para DOs em PDF nativo, heurística de densidade textual (chars/página < N → acionar OCR) é suficiente.

Document Image Quality Assessment (DIQA) é o problema de avaliar a qualidade de imagens de documentos — distinto de IQA para cenas naturais. DocIQ (Ma et al. 2025) introduz DIQA-5000 (5000 imagens, 5 tipos de distorção) e um modelo no-reference que supera SOTA geral em correlação com acurácia de OCR (SRCC=0.91). Aplicabilidade ao pipeline Zelox: triagem automática nativo/escaneado/degradado antes da extração de texto.

## Conteúdo

### Por que DIQA é diferente de IQA geral

Modelos de IQA treinados em cenas naturais (KonIQ-10k, CLIVE, CSIQ) falham em documentos porque:
- Padrões de degradação são estruturalmente diferentes (blur, sombra, vincos, moiré)
- O critério de qualidade relevante é legibilidade/OCR accuracy, não apelo visual
- Documentos têm layout semântico (texto, tabelas, figuras) que afeta a percepção de qualidade

### DIQA-5000 Dataset

- **500 documentos base:** PDFs públicos impressos a 300 dpi — cobrindo layouts textual, tabular e misto
- **5 tipos de distorção simulados:**
  1. Shadow — iluminação desigual (captura por smartphone)
  2. Occlusion — obstrução parcial por objetos
  3. Blurring — blur de movimento ou defocus
  4. Creases — vincos em papel dobrado
  5. Moiré Patterns — artefatos de captura de tela exibindo documentos
- **10 versões processadas por imagem** via pipeline de 6 operações (dewarp, demoisé, deblur, deshadow, occlusion removal, enhancement) em combinações aleatórias → 5.000 imagens totais
- **3 dimensões de rating:** overall quality, sharpness, color fidelity
- **15 anotadores humanos** por imagem, limpeza via ITU-R BT.500

### DocIQ — Modelo

Arquitetura de 4 componentes:
1. **Layout Fusion Downsampler** — downsampling com máscara semântica de layout (texto, tabelas, figuras); reduz resolução sem perder regiões críticas
2. **Backbone ResNet50** — extração hierárquica de features em múltiplas escalas (pré-treinado ImageNet)
3. **Feature Fusion Module** — combina features de baixo nível (bordas, textura) com alto nível (semântica); hyper-structures bottleneck progressivos
4. **Parallel Quality Regressors** — cabeças independentes por dimensão; prediz distribuição de scores por anotador → agrega em MOS final

### Resultados

| Dataset | Métrica | DocIQ | Melhor baseline anterior |
|---------|---------|-------|------------------------|
| DIQA-5000 (Overall) | SRCC | **0.8832** | 0.8554 (MUSIQ) |
| DIQA-5000 (Sharpness) | SRCC | **0.8615** | 0.8460 (MUSIQ) |
| DIQA-5000 (Color) | SRCC | **0.8666** | 0.8557 (RichIQA) |
| SmartDoc-QA (CACC) | SRCC | **0.9086** | 0.8921 (StairIQA) |
| SmartDoc-QA (WACC) | SRCC | **0.8989** | 0.8857 (StairIQA) |

SmartDoc-QA mede correlação com acurácia de OCR (Character/Word Accuracy) — demonstra que DocIQ prediz bem a legibilidade real, não apenas apelo visual.

### Ablation (contribuição de cada componente, SRCC overall)

| Configuração | SRCC |
|-------------|------|
| Full model (todos os componentes) | **0.8832** |
| Sem multi-rater strategy | 0.8636 (−0.0196) |
| Sem layout fusion | 0.8696 (−0.0136) |
| Sem feature fusion | 0.8448 (−0.0384) |
| Sem layout + sem feature fusion | 0.8162 (−0.0670) |

Feature fusion é o componente de maior impacto isolado.

### SmartDoc-QA — Contexto

Dataset público de 2.130 imagens de documentos capturados por smartphone, avaliados por métricas de OCR (CACC = Character ACCuracy, WACC = Word ACCuracy). Correlação SRCC=0.91 de DocIQ com CACC confirma que o modelo prediz legibilidade funcional.

## Interpretação

(⚠️ nossa interpretação) **Aplicação ao pipeline Zelox (Camada 2 — triagem OCR):**

O gap identificado no pipeline Zelox é ausência de triagem automática de PDFs: nativo vs. escaneado vs. degradado. DIQA resolve uma parte disso:

- **Documentos escaneados degradados** → DIQA score baixo → rota OCR + pós-processamento (deblur, deshadow)
- **PDFs nativos** → DIQA score alto (não se aplica ao modelo de captura, mas pode identificar casos de extração falha)
- **Triagem por threshold:** DIQA score ≥ X → extração direta com PyMuPDF; DIQA score < X → fallback OCR

Limitação: DIQA-5000 foi construído com documentos impressos e capturados por smartphone. DOs públicos em PDF escaneado têm padrões de degradação distintos (scanner, não smartphone). Validação no domínio de DOs seria necessária antes de adotar threshold de produção.

(⚠️ nossa interpretação) **Alternativa mais simples para triagem:** para DOs, a distinção primária é PDF nativo (PyMuPDF extrai texto diretamente) vs. PDF imagem (sem texto extraível). Isso pode ser detectado com heurística: se PyMuPDF retorna < N chars por página → PDF imagem → acionar OCR. DIQA seria útil apenas para documentos imagem com qualidade variável.

## Verificação adversarial

**Claim mais fraco:** "DocIQ prediz OCR accuracy" — demonstrado apenas em SmartDoc-QA (documentos capturados por smartphone). Não validado em scanners de alta resolução ou PDFs governamentais.

**O que o paper NÃO diz:**
1. Não cobre detecção de PDFs nativos vs. imagem — apenas avalia qualidade de imagens já escaneadas
2. Não avalia desempenho em documentos administrativos/legais — dataset é de documentos genéricos
3. Não oferece threshold de qualidade para decisão de pipeline (acionar OCR ou não)

**Simplificações:** DIQA-5000 usa apenas 500 documentos base com distorções sintéticas. DOs reais têm distorções orgânicas (tinta desbotada, papel amarelado, ruído de scanner) que podem não estar no domínio de treinamento.

**Prior work:** SmartDoc-QA (Nayef et al. 2015), IQA geral (HyperIQA, MUSIQ, StairIQA).

## Conexões

- partOf: [[diario-oficial-segmentation-strategies]] — DIQA resolve triagem da Camada 2; segmentação é Camada 3
- derivedFrom: [[multilegalsbd-annotation]] — pipeline análogo: annotation quality gate para documentos legais

## Fontes

- [Ma et al. 2025 — DocIQ](../../raw/papers/ma-2025-dociq-document-image-quality.md) — DIQA-5000 dataset, DocIQ model, SRCC=0.91 com OCR accuracy em SmartDoc-QA

## Quality Gate

- [x] Wikilinks tipados: 2 relações (partOf, derivedFrom)
- [x] Instance→class: SRCC=0.9086 qualificado como "em SmartDoc-QA (smartphone-captured docs)"
- [x] Meta-KB separado: interpretação Zelox em ## Interpretação, não em ## Conteúdo
- [x] Resumo calibrado: limita claim a "correlação com OCR accuracy", não "prediz qualidade de DOs"
