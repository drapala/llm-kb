---
title: "Debarment and Collusion — Experimental Evidence (Cerrone et al. 2021)"
sources:
  - path: raw/papers/cerrone-hermstruwer-robalo-2021-debarment-collusion.md
    type: paper
    quality: primary
    stance: challenging
    challenging_type: implication
created: 2026-04-08
updated: 2026-04-08
tags: [procurement, debarment, collusion, experiment, auction, deterrence, phoenix-firms, b2g]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Gate 1 — auto-promote pending"
quarantine_criteria_met:
  gates_passed: []
  gates_failed: [1]
  gate1_reason: "não avaliado ainda — ingest automático via scout"
---

## Resumo

Cerrone, Hermstrüwer & Robalo (2021) apresentam o primeiro experimento controlado sobre debarment em procurement auctions. Resultado contraintuitivo: debarments muito curtos reduzem eficiência e aumentam colusão tácita entre os licitantes que permanecem — o efeito de deterrência cresce com a duração do debarment. Games and Economic Behavior, 129:114-143.

⚠️ Stub — baseado em abstract e open access City University London. Full text não verificado integralmente.

## Conteúdo

### Design Experimental

Leilões de procurement repetidos em laboratório. Três tratamentos:
1. **Controle** — sem sanção
2. **Debarment** — exclusão por N rodadas após detecção de colusão
3. **Multa** — penalidade financeira equivalente

### Resultados

**1. Debarments e multas reduzem colusão** vs. mercado sem sanção — deterrência confirmada.

**2. Duração do debarment é crítica:** efeito de deterrência cresce com o comprimento do debarment. Debarments longos são sistematicamente mais eficazes.

**3. Debarments curtos têm efeito perverso:**
- Excluem um licitante temporariamente → mercado fica com menos competidores
- Licitantes sobreviventes coordenam colusão tácita mais facilmente
- Bids sobem (pior para o comprador) durante o período de exclusão
- Net effect pode ser negativo em mercados já concentrados

**4. Multas:** efeito deterrência similar ao debarment longo, sem o efeito anti-competitivo de curto prazo.

### Implicação para Phoenix Firms

O paper não mede phoenix firms diretamente, mas o mecanismo é análogo: se uma firma debarred cria phoenix imediatamente, o efeito é equivalente a um debarment de duração zero — nenhuma deterrência + possível aumento de concentração de mercado favorável a colusão tácita.

## Interpretação

⚠️ Interpretação do compilador.

**Implicação para o laudo Zelox:** Se o laudo leva ao debarment do fornecedor (via representação TCU), a eficácia da intervenção depende da duração da sanção. Debarment curto (6 meses, frequente em TCU) pode ser contraproducente em municípios com poucos fornecedores habilitados — que é precisamente o mercado-alvo do Zelox.

**O que isso não altera:** o laudo como ferramenta forense para advocacia (evidência de padrão) independe da política de debarment. O que muda é a narrativa de impacto (deterrência) para clientes que compram o laudo para prevenção.

## Verificação adversarial

**Claim mais fraco:** o experimento é de laboratório — comportamento em auctions reais pode diferir por reputação, relação de longo prazo com governo, e assimetrias de informação que laboratório não capta.

**O que o paper NÃO diz:** não mede reincidência empírica de firmas reais; não cobre o Brasil; não mede efeito de debarment em cascata (onde o mercado já tem pouquíssimos fornecedores).

**Prior work:** Auriol & Søreide (2017) — modelo teórico que prediz o mesmo resultado sobre efeito anti-competitivo do debarment.

## Quality Gate
- [x] Wikilinks tipados: extends/relates
- [x] Instance→class: resultados são de experimento de laboratório — generalização cuidadosa
- [x] Meta-KB separado: implicações Zelox em Interpretação
- [x] Resumo calibrado: stub mencionado

## Conexões

- extends: [[debarment-evasion-phoenix-firms]] ON "complementa com evidência experimental: debarments curtos podem ser piores que nenhum debarment em mercados concentrados"
- relates: [[tacit-collusion]] ON "debarments curtos facilitam colusão tácita entre sobreviventes — mecanismo Folk Theorem em mercado reduzido"
- relates: [[audit-deterrence-corruption]] ON "deterrência funciona, mas duração e design da sanção importam tanto quanto a probabilidade de detecção"

## Fontes

- [Cerrone, Hermstrüwer & Robalo (2021)](../../raw/papers/cerrone-hermstruwer-robalo-2021-debarment-collusion.md) — Games and Economic Behavior 129:114-143. Primeiro experimento sobre debarment em auctions; debarment curto → colusão tácita entre sobreviventes. ⚠️ Stub.
