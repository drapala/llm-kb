---
title: "Quality Manipulation Corruption — Underbid + Change Orders (EER 2018)"
sources:
  - path: raw/papers/quality-manipulation-corruption-procurement-2018.md
    type: paper
    quality: primary
    stance: confirming
    challenging_type: null
created: 2026-04-08
updated: 2026-04-08
tags: [procurement, corruption, underbid, quality-manipulation, change-orders, aditivos, b2g, zelox-signals]
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

Paper (European Economic Review, 2018) modela corrupção em procurement auctions via manipulação de qualidade: firmas corruptas submetem low bids para maximizar win rate → reduzem qualidade na execução → extraem rendas via change orders e modificações contratuais. Fornece fundamento teórico formal para o mecanismo underbid + aditivo observado empiricamente.

⚠️ Stub — conteúdo baseado em descrição de scout. Full text não verificado (Elsevier paywall).

## Conteúdo

### Mecanismo de Três Estágios

**Fase 1 — Licitação (bid baixo):**
Firma corrupta submete bid abaixo do custo real para maximizar probabilidade de vitória. O preço baixo não é objetivo — é instrumento de entrada.

**Fase 2 — Execução (qualidade reduzida):**
Firma reduz qualidade abaixo do especificado no contrato. Corte de qualidade não é verificável pelo comprador ex-ante (assimetria de informação pós-contrato).

**Fase 3 — Renegociação (change orders / aditivos):**
Firma solicita modificações contratuais alegando necessidades técnicas, scope creep, ou condições imprevistas. Os change orders recuperam a margem sacrificada no bid + extraem renda adicional.

**Equação de extração:**
```
Renda líquida = valor(change orders) + economia(qualidade cortada) − [custo_real − bid]
```

Para que a estratégia seja racional: `valor(change orders) + economia_qualidade > [custo_real − bid]`

### Por que é Equilibrio

O comprador tem incentivo para aceitar change orders porque:
- Trocar o fornecedor a meio contrato é ainda mais custoso (hold-up — Tirole 1986)
- A qualidade reduzida não é verificável ex-post sem auditoria especializada
- O change order parece tecnicamente justificado

### Sinal Combinado

O sinal de corrupção não está nem no bid baixo (que pode ser agressividade legítima) nem no change order (que pode ser scope genuíno), mas na **combinação**:
- Bid significativamente abaixo da referência de mercado + change orders próximos ao teto legal = estratégia de dois estágios

## Interpretação

⚠️ Interpretação do compilador.

**Validação da hipótese de underbid no bid_engine.db:** o achado empírico de avg delta_pct ≈ 0% em contratos iniciais de phoenix candidates é consistente com este mecanismo — o sinal de extração não está no primeiro contrato, mas nos change orders de contratos maduros (execução avançada).

**Feature design para Zelox:**
- Feature 1: `bid_gap = (bid_vencedor − referencia_mercado) / referencia_mercado` — deve ser negativo e significativo
- Feature 2: `change_order_rate` em contratos com bid_gap < −15% — combinação é o sinal
- Feature 3: `bid_gap × change_order_rate` como feature de interação

**Limitação:** o paper modela qualidade, não phoenix firms especificamente. A aplicação a phoenix é nossa extensão.

## Verificação adversarial

**Claim mais fraco:** stub — mecanismo descrito é baseado em abstract/scout, não full text. Detalhes do modelo (extensões de equilíbrio, condições de sustentabilidade) não verificados.

**O que o paper provavelmente NÃO diz:** não menciona phoenix firms; não testa com dados brasileiros; provavelmente não mede bid_gap como feature de ML.

**Prior work:** Tirole (1986) modela hold-up como mecanismo adjacente; Bajari & Tadelis (2001) modelam trade-off FP vs C+ sem corrupção explícita.

## Quality Gate
- [x] Wikilinks tipados
- [x] Instance→class: stub marcado, mecanismo qualificado como baseado em scout
- [x] Meta-KB separado: Zelox features em Interpretação
- [x] Resumo calibrado: ⚠️ stub explicitado

## Conexões

- extends: [[procurement-contract-design]] ON "formaliza mecanismo underbid+extração que Bajari-Tadelis deixa como interpretação do compilador"
- extends: [[procurement-renegotiation]] ON "complementa Tirole 1986: hold-up + quality manipulation = dois canais de extração via renegociação"
- relates: [[procurement-phoenix-graph-architecture]] ON "phoenix firms pós-debarment com bid baixo + aditivos futuros = instância deste mecanismo de três estágios"
- relates: [[procurement-manipulation-signals]] ON "bid baixo como red flag complementar a win rate e single bidding de Villamil/Decarolis"

## Fontes

- [Quality Manipulation Corruption EER 2018](../../raw/papers/quality-manipulation-corruption-procurement-2018.md) — European Economic Review. Mecanismo formal underbid + quality cut + change orders. ⚠️ Stub.

> ⚠️ QUARENTENA: Gate 1 — stub com full text não verificado. Promover após leitura do paper completo.
