---
title: "Zelox MVP — Laudo de Padrão de Aditivos por CNPJ"
sources:
  - path: wiki/concepts/procurement-renegotiation.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/procurement-variety-gap.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/audit-risk-rent-extraction.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/inexigibilidade-notoria-especializacao.md
    type: synthesis
    quality: primary
    stance: confirming
created: 2026-04-08
updated: 2026-04-08
tags: [zelox, procurement, b2g, mvp, aditivo, pncp, advocacia, tcu, produto, hold-up, estrategia]
source_quality: medium
interpretation_confidence: low
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - wiki/concepts/procurement-renegotiation.md
  - wiki/concepts/procurement-variety-gap.md
  - wiki/concepts/audit-risk-rent-extraction.md
  - wiki/concepts/inexigibilidade-notoria-especializacao.md
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-12
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Gate 1 — interpretation_confidence: low (proposta de produto sem validação de mercado)"
quarantine_criteria_met:
  gates_passed: []
  gates_failed: [1]
  gate1_reason: "interpretation_confidence: low"
---

## Resumo

Primeiro caso de uso mínimo pagável do Zelox: laudo de padrão de aditivos por CNPJ para escritório de advocacia construindo representação no TCU. Usa apenas dado PNCP — `aditivo_acumulado / valor_original` — sem Risk Score completo, sem grafo societário. Threshold legal (Art. 125, Lei 14.133: 25%) torna o produto auditável sem ML.

## Conteúdo

### O sinal: `aditivo_teto`

Art. 125, Lei 14.133/2021: aditivos acumulados não podem superar 25% do valor original do contrato (obras de engenharia; 50% para acréscimos em contratos de serviço, mas 25% é o limite mais citado em jurisprudência TCU para obras).

Cálculo: `aditivo_acumulado / valor_original_contrato`

Dados necessários: PNCP — contrato original (valor + data) + aditivos sequenciais (valor + data). Aritmética simples, sem ML.

**Por que é "doloroso" para dois compradores distintos:**

| Comprador | Dor | Consequência sem o dado |
|-----------|-----|------------------------|
| Escritório de advocacia | Precisam de evidência documental de padrão para representação TCU ser admitida | 3-5h de busca manual no PNCP por CNPJ para montar o histórico |
| Gestor público (controle interno) | Se aprovam aditivo que leva acumulado acima de 25%, respondem por ato de improbidade | Não têm visibilidade do portfólio antes da decisão de aprovação |

### O mecanismo: hold-up de Tirole aplicado a aditivos

Tirole (1986): fornecedor ganha licitação com proposta baixa → solicita aditivos iterativos → captura surplus ex-post (hold-up). O governo está "held up" porque trocar fornecedor a meio contrato tem custo ainda maior.

O padrão detectável via `aditivo_teto`:
1. Proposta inicial substancialmente abaixo do mercado (sinal de underbidding)
2. Sequência de aditivos em direção ao teto de 25%
3. Múltiplos contratos do mesmo CNPJ com o mesmo padrão → evidência de comportamento sistemático

O que torna o padrão **evidência legal** e não apenas estatística: o Art. 125 é um threshold objetivo. Não é necessário provar intenção — basta demonstrar que o fornecedor habitualmente chega próximo ao teto em múltiplos contratos. O TCU usa esse tipo de evidência para admitir representações.

### Por que o escritório de advocacia paga primeiro

Zamboni & Litschig (2018): o efeito de monitoramento se concentra onde accountability local é fraca — municípios menores, menor cobertura de mídia, menor competição política. Esses são precisamente os municípios com mais irregularidades de aditivo não auditadas, e onde escritórios de contencioso administrativo buscam casos com evidência disponível.

Vantagem de ciclo de decisão:
- Escritório: 1–3 dias (honorário profissional, sem licitação)
- Órgão público: meses (ciclo de compras governamental)

Vantagem de especificidade:
- Escritório tem um caso específico em mão, precisa do dado agora
- Não precisa de assinatura — relatório one-shot por CNPJ

## Interpretação

⚠️ Interpretação do compilador. Proposta de produto não está em nenhuma das fontes.

**Deliverable mínimo:**

Para um CNPJ fornecido, relatório com:
- Todos os contratos públicos no PNCP (por CNPJ)
- Por contrato: valor original + aditivos acumulados + % do teto + data de cada aditivo
- Semáforo: <15% verde / 15–20% amarelo / 20–25% vermelho / >25% violação
- Timeline de aditivos (para mostrar iteração estratégica em direção ao limite)
- Resumo executivo: quantos contratos por faixa, valor médio de extração estimada

**Por que não o Risk Score completo ainda:**

O Risk Score requer ground truth (contratos confirmados como irregulares) para calibrar pesos. Sem isso, produz um número sem interpretação defensável ao TCU. O laudo de aditivos não precisa de calibração — threshold legal (25%) é dado pela lei. Objetividade é o produto diferenciador.

**Preço indicativo:** R$500–2.000 por CNPJ, one-shot. Sem assinatura necessária para o primeiro cliente.

**Escalabilidade da receita:** escritório satisfeito compra laudos de múltiplos CNPJs por processo; processo de TCU normalmente envolve 5–20 fornecedores a verificar.

**Limitações não resolvidas pelo corpus:**
- Não sabemos se o PNCP expõe aditivos de forma granular por contrato na API pública
- Não sabemos se o TCU efetivamente exige ou aceita esse formato como evidência suficiente para admissão de representação
- Preço de R$500–2.000 é estimativa sem referência de mercado no corpus

## Quality Gate
- [x] Wikilinks tipados: synthesis_sources declaradas
- [x] Instance→class: "25%" referenciado ao Art. 125 Lei 14.133; "R$500-2000" marcado como estimativa sem referência
- [x] Meta-KB separado: proposta de produto em Interpretação
- [x] Resumo calibrado: source_quality:medium (synthesis de fontes primárias verificadas); interpretation_confidence:low (proposta de produto sem validação de mercado)

## Conexões

- emerge-de: [[procurement-renegotiation]] ON "hold-up de Tirole = mecanismo exato do underbid+aditivo que o laudo detecta"
- emerge-de: [[procurement-variety-gap]] ON "aditivo_teto é o sinal primário; Art. 125 provê o threshold legal objetivo"
- relaciona: [[audit-risk-rent-extraction]] ON "escritório com laudo = mecanismo de audit risk percebido; municípios fraca accountability = maior concentração de casos"
- relaciona: [[inexigibilidade-notoria-especializacao]] ON "inexigibilidade é a via para vender o laudo sem licitação — notória especialização em inteligência de procurement"

## Fontes

- [[procurement-renegotiation]] — Tirole (1986): hold-up; underbid + renegociação via aditivos como estratégia documentada
- [[procurement-variety-gap]] — `aditivo_teto` como sinal; Art. 125 Lei 14.133; aritmética PNCP
- [[audit-risk-rent-extraction]] — Zamboni & Litschig: municípios com fraca accountability = maior valor de monitoramento externo
- [[inexigibilidade-notoria-especializacao]] — mecanismo legal para contratação do laudo sem licitação
