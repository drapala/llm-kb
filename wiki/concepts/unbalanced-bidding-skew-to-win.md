---
title: "Unbalanced Bidding — Skew to Win vs. Skew to Profit (JPP 2019)"
sources:
  - path: raw/papers/skew-to-win-unbalanced-bidding-2019.md
    type: paper
    quality: primary
    stance: confirming
    challenging_type: null
created: 2026-04-08
updated: 2026-04-08
tags: [procurement, unbalanced-bidding, underbid, auction-theory, b2g, zelox-signals]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 1
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-08
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Gate 1 — auto-promote pending; stub com full text não verificado"
quarantine_criteria_met:
  gates_passed: []
  gates_failed: [1]
  gate1_reason: "stub — conteúdo baseado em descrição de scout, full text não lido"
---

## Resumo

Paper game-teórico (Journal of Public Procurement, 2019) que distingue dois motivos para unbalanced bidding em contratos públicos: "skew to win" (distorcer bid para maximizar win rate, não profit) vs. "skew to profit" (front-end loading para extração imediata). Achado: firmas informadas preferem skew-to-win — a extração de profit é mecanismo separado e posterior ao bid.

⚠️ Stub — full text não verificado (Emerald paywall).

## Conteúdo

### A Distinção Central

**Skew to profit (modelo clássico):**
Firma distorce preços unitários para itens de alto volume real — ganha mais que o bid aparente. Front-end loading. Lucro extraído diretamente via distorção de preços unitários, visível no bid.

**Skew to win (resultado principal do paper):**
Firmas *informadas* sobre próprios custos ajustam a distribuição de preços unitários para reduzir o bid total *aparente* — sem necessariamente extrair profit nos preços unitários. O objetivo é maximizar win rate. Profit vem de mecanismo separado posterior.

**Por que informação muda o resultado:**
Firmas com informação privada sobre suas próprias eficiências usam unbalanced bids como sinal estratégico — não como mecanismo de extração direta.

### Implicação para Detecção

Bid anormalmente baixo em licitante informado = sinal de "skew to win", não necessariamente de low quality bid ou erro de cálculo. A extração acontece após o contrato, não no bid.

Consequência para algoritmos de detecção:
- Algoritmos que só olham o bid price não capturam a estratégia completa
- O sinal deve ser o bid price + comportamento pós-contrato (change orders, aditivos)
- "Abnormally low bid" por si só tem alta taxa de falso positivo se não combinado com sinal de execução

## Interpretação

⚠️ Interpretação do compilador.

**Refinamento crucial para o Zelox:** se skew-to-win é a estratégia, então:
- O bid baixo é sinal necessário mas não suficiente
- O sinal completo é: `bid_gap < threshold` AND `change_order_rate > threshold` (combinação)
- Phoenix firms pós-debarment com delta_pct ≈ 0% no contrato inicial são consistentes com skew-to-win: ganharam o contrato, ainda não executaram a extração posterior

**Falso positivo importante:** firmas eficientes genuínas também biddem baixo. O discriminador é o comportamento de execução, não o bid.

## Verificação adversarial

**Claim mais fraco:** stub. Detalhes do modelo game-teórico não verificados — pode haver condições de equilíbrio que limitam o resultado ao contexto específico.

**O que provavelmente NÃO cobre:** phoenix firms; dados brasileiros; ML features.

## Quality Gate
- [x] Wikilinks tipados
- [x] Instance→class: stub marcado
- [x] Meta-KB separado: Zelox em Interpretação
- [x] Resumo calibrado: ⚠️ stub explicitado

## Conexões

- extends: [[quality-manipulation-underbid-procurement]] ON "fundamenta mecanismo separado de extração pós-bid — skew to win é fase 1, quality manipulation é fase 2-3"
- extends: [[procurement-contract-design]] ON "refinamento da distinção underbid eficiente vs estratégico — adiciona motivação de win rate separada de profit"
- relates: [[procurement-manipulation-signals]] ON "bid baixo deve ser combinado com sinal de execução, não usado isoladamente como red flag"

## Fontes

- [Skew to Win (JPP 2019)](../../raw/papers/skew-to-win-unbalanced-bidding-2019.md) — Journal of Public Procurement 19(1). Game theory: firmas informadas bid baixo para win rate, não profit. ⚠️ Stub.

> ⚠️ QUARENTENA: Gate 1 — stub. Promover após leitura do paper completo.
