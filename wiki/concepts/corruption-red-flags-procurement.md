---
title: "Corruption Red Flags in Procurement — Empirical Evidence (Italy 2022)"
sources:
  - path: raw/papers/corruption-red-flags-italian-procurement-2022.md
    type: paper
    quality: primary
    stance: confirming
    challenging_type: null
created: 2026-04-08
updated: 2026-04-08
tags: [procurement, corruption, red-flags, italy, signals, zelox-signals, bid-rigging, competition]
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
quarantine_reason: "Gate 1 — auto-promote pending"
quarantine_criteria_met:
  gates_passed: []
  gates_failed: [1]
  gate1_reason: "não avaliado ainda — ingest automático via scout"
---

## Resumo

Análise empírica de dados de procurement italiano (PLOS ONE, 2022, open access) identificando red flags observáveis de corrupção. Quatro sinais empíricos: abnormally low bids, bid clustering, three-bidder minimum patterns, e winner concentration. Confirma sinais de risco com evidência italiana independente de Decarolis et al.

⚠️ Stub — conteúdo baseado em descrição de scout. Full text disponível open access (PMC) — verificar antes de usar claims específicos.

## Conteúdo

### Red Flags Identificados

**1. Abnormally Low Bids**
Bids significativamente abaixo do referencial de mercado (SINAPI-equivalente italiano). Sinal de underbid estratégico (skew-to-win) OU de qualidade que será cortada na execução.

**2. Bid Clustering**
Múltiplos licitantes com preços muito próximos entre si. Indica coordenação prévia — licitantes não chegaram ao mesmo preço por acaso.

**3. Three-Bidder Minimum Pattern**
Repetidamente aparece exatamente o número mínimo legal de competidores. O processo "parece competitivo" mas a competição é artificial.

**4. Winner Concentration**
Mesmo fornecedor vencendo proporção anormal de contratos por órgão ou categoria de objeto. Análogo ao single-bidding de Villamil (2024) mas com múltiplos processos em vez de um.

### Combinações de Sinais

O paper provavelmente analisa combinações de red flags (não verificado no full text). A lógica é: cada sinal individualmente tem taxa de falso positivo alta; combinações têm menor falso positivo.

## Interpretação

⚠️ Interpretação do compilador.

**Relevância para Zelox signal stack:**
- Abnormally low bid: novo sinal para incluir no laudo (complementar ao aditivo)
- Bid clustering: detectável via análise de distribuição de bids por processo no PNCP
- Three-bidder minimum: facilmente computável via PNCP (contagem de propostas por processo)
- Winner concentration: já parcialmente coberto pelo Zelox via histórico de contratos por CNPJ

**Evidência independente:** Itália 2022 confirma os mesmos sinais que Decarolis (Itália 2000-2016) com dados diferentes. Robustez temporal elevada.

**Open access:** paper disponível em PMC — citável sem caveat de paywall.

## Verificação adversarial

**Claim mais fraco:** stub — magnitudes e metodologia não verificados.
**Prior work:** Decarolis et al. (2020) cobrem terreno similar com dados mais antigos.

## Quality Gate
- [x] Wikilinks tipados
- [x] Instance→class: stub marcado; "provavelmente" qualificado
- [x] Meta-KB separado: Zelox em Interpretação
- [x] Resumo calibrado: ⚠️ stub explicitado

## Conexões

- validates: [[procurement-manipulation-signals]] ON "confirma empiricamente red flags de bid rigging (abnormally low bids, bid clustering, three-bidder minimum) com dados italianos independentes"
- relates: [[quality-manipulation-underbid-procurement]] ON "abnormally low bid como red flag compartilhado — bid baixo é pré-condição de ambos os mecanismos"
- relates: [[zelox-mvp-laudo-aditivos]] ON "three-bidder minimum e winner concentration são features computáveis diretamente do PNCP no laudo"

## Fontes

- [Corruption Red Flags Italian Procurement (PLOS ONE 2022)](../../raw/papers/corruption-red-flags-italian-procurement-2022.md) — PMC open access. 4 red flags empíricos: abnormally low bids, bid clustering, three-bidder minimum, winner concentration. ⚠️ Stub.

> ⚠️ QUARENTENA: Gate 1 — auto-promote pending.
