---
title: "Procurement Contract Design — FP vs C+ (Bajari & Tadelis 2001)"
sources:
  - path: raw/papers/bajari-tadelis-2001-incentives-transaction-costs.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [economics, procurement, contract-design, incentives, transaction-costs, b2g, aditivos]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-04
quarantine: false
---

## Resumo

Bajari & Tadelis (2001) derivam quando compradores deveriam usar contratos de preço fixo (FP) versus custo mais margem (C+). Trade-off: FP oferece incentivos mais fortes para redução de custos, mas impõe custos de transação maiores quando o escopo muda. C+ facilita adaptação mas enfraquece incentivos. Predição empírica confirmada com dados de construção civil: projetos simples usam FP, complexos usam C+. RAND 2001.

⚠️ Stub — full text não lido. Conteúdo baseado em descrições secundárias.

## Conteúdo

### O Trade-off Central

**Fixed-price (FP):** Contratante assume todo o risco de custo.
- Incentivo máximo para reduzir custos (contratante fica com toda economia)
- Mas: quando escopo muda, renegociar cada mudança é custoso (transação por transação)
- Adequado para: projetos bem especificados, baixa incerteza de design

**Cost-plus (C+):** Comprador assume todo o risco de custo.
- Incentivo mínimo para redução de custos (comprador paga tudo de qualquer forma)
- Mas: mudanças de escopo são baratas de acomodar (apenas reimbursar custos adicionais)
- Adequado para: projetos complexos, alta incerteza de design, adaptação frequente

**Contrato ótimo:** minimiza [perda de incentivo] + [custo de adaptação].

Para projetos simples (poucas mudanças previstas): custo de adaptação baixo → FP domina.
Para projetos complexos (muitas mudanças previstas): custo de adaptação alto → mix ou C+.

### Evidência Empírica

Usando dados de construção civil (EUA):
- Residencial (simples, especificações claras) → prevalência maior de FP
- Comercial/industrial (complexo, alta incerteza) → prevalência maior de C+

Padrão consistente com a teoria: compradores escolhem o tipo de contrato que minimiza os custos de transação dado o nível de complexidade.

### Por que Aditivos Ocorrem Estruturalmente

A Lei 8.666/93 no Brasil exige licitação competitiva para novos contratos, essencialmente forçando o uso de contratos tipo FP (baseado em preço) mesmo para projetos complexos.

**O problema:** Projetos complexos (infraestrutura, TI, obras públicas) têm alta incerteza de design → alta frequência de mudanças de escopo. Mas a lei força FP → cada mudança requer renegociação formal (aditivo).

**Resultado estrutural:** O sistema legal cria inevitabilidade de aditivos para projetos complexos:
1. Projeto complexo → design incompleto na licitação (por necessidade técnica)
2. Lei força FP (licitação por menor preço)
3. Mudanças de escopo ocorrem durante execução (inevitável dado design incompleto)
4. Cada mudança → aditivo (único mecanismo legal de adaptação)

**Dois tipos de aditivos através da lente Bajari-Tadelis:**

| Tipo | Origem | Sinal | Risco |
|------|--------|-------|-------|
| Eficiente | Mudança genuína de escopo em projeto complexo | Precoce, justificado, abaixo do limite | Baixo |
| Estratégico | Underbid deliberado + extração posterior | Tardio, próximo ao limite de 25%, padrão repetitivo | Alto |

### Classificação de Projetos por Complexidade

Bajari & Tadelis implicam que a complexidade do projeto deveria ser a *variável de controle* principal ao avaliar aditivos. Um modelo de risk scoring deve:
1. Estimar complexidade esperada do projeto (tipo de objeto, valor, prazo)
2. Calcular taxa de aditivos *esperada* dado a complexidade
3. Sinalizar quando a taxa observada excede a esperada para aquele tipo de projeto

## Interpretação

⚠️ Interpretação do compilador.

**Implicação direta para Feature Engineering do Zelox:**

O sinal "aditivo próximo de 25%" precisa ser condicionado pela complexidade do projeto. Sem esse controle, o modelo comete dois erros:
1. **Falso positivo:** projeto de infraestrutura complexa com aditivo justificado → sinalizado incorretamente
2. **Falso negativo:** projeto simples com aditivo estratégico que ainda está abaixo do limiar → não sinalizado

**Feature a derivar:** `(taxa_aditivo_observada - taxa_aditivo_esperada_por_tipo) / desvio_padrao` — z-score de aditivo dado a categoria do objeto licitado.

## Quality Gate
- [x] Wikilinks tipados: explains/relaciona
- [x] Instance→class: evidência empírica é sobre construção civil EUA; aplicação ao Brasil é extrapolação
- [x] Meta-KB separado: Zelox feature engineering em Interpretação
- [x] Resumo calibrado: ⚠️ stub mencionado

## Conexões

- explains: [[procurement-renegotiation]] ON "formaliza quando renegociação (aditivos) é eficiente vs. quando é hold-up — preenche o 'por que' de Tirole 1986"
- relates: [[incentive-theory-procurement]] ON "Laffont-Tirole prescreve contrato ótimo; Bajari-Tadelis explica por que aditivos ocorrem sob contratos subótimos"
- relates: [[corruption-audits-brazil]] ON "aditivos ineficientes são uma das 3 categorias de corrupção documentadas por Ferraz & Finan"
- emerge-para: [[procurement-variety-gap]] ON "FP vs C+ = reguladores com V(R) baixo vs alto; Lei 8.666 como mandato de V(R)=1 para todos os projetos"

## Fontes

- [Bajari & Tadelis (2001)](../../raw/papers/bajari-tadelis-2001-incentives-transaction-costs.md) — RAND 32(3), 387-407. Trade-off incentivos/custos de transação, FP vs C+, evidência construção civil. ⚠️ Stub — texto completo não lido.
