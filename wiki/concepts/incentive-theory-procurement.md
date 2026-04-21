---
title: "Incentive Theory in Procurement (Laffont & Tirole 1993)"
sources:
  - path: raw/papers/laffont-tirole-1993-theory-incentives-procurement.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [economics, procurement, principal-agent, adverse-selection, moral-hazard, incentives, b2g]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 3
retrievals_correct: 2
retrievals_gap: 0
last_read: 2026-04-08
quarantine: false
---

## Resumo

Laffont & Tirole (1993) é o livro canônico de teoria de contratos em procurement e regulação. Desenvolve teoria completa de design de mecanismos quando regulador (comprador) tem informação incompleta sobre custo e esforço do fornecedor. Resultado central: o contrato ótimo é uma combinação de preço fixo e custo mais margem — a mistura depende da incerteza de custo e do custo das rendas informacionais. MIT Press.

⚠️ Stub — full text não lido. Conteúdo baseado em descrições secundárias.

## Conteúdo

### O Modelo Básico (Capítulo 1)

**Setup:** Regulador (principal) contrata firma regulada (agente) com informação privada sobre parâmetro de eficiência θ ∈ [θ_baixo, θ_alto]. Função de custo da firma: `C = β - e`, onde β = parâmetro de produtividade (info privada) e e = esforço (não observável pelo regulador).

**Bem-estar social:** `W = S(q) - (1+λ)(C + t) + t - U`
- S(q) = excedente do consumidor
- λ = custo das rendas públicas (shadow cost of public funds)
- t = transferência ao fornecedor
- U = renda informacional da firma (lucro)

**Princípio da Revelação:** Mecanismo ótimo = menu de contratos (t(β̂), q(β̂)) que incentiva revelação verdadeira. Firma declara seu tipo; o contrato correspondente é o ótimo para esse tipo.

### Trade-off Eficiência–Renda (Capítulo 2)

**Resultado central:** Regulador enfrenta trade-off fundamental:
- Tipos eficientes (θ baixo, custos baixos) recebem rendas informacionais `U > 0` para revelar sua eficiência
- Tipos ineficientes (θ alto) recebem renda zero mas output distorcido para baixo
- O regulador troca eficiência produtiva por extração de renda

**Contratos fixos (fixed-price/FP):** Firma assume todo o risco de custo → máximo incentivo para redução de custos. Adequado quando: incerteza de custo baixa, esforço é a variável crítica.

**Contratos custo mais margem (cost-plus/C+):** Regulador assume todo o risco de custo → nenhum incentivo para redução de custos (moral hazard). Adequado quando: incerteza de custo alta, adaptação de escopo frequente.

**Contrato ótimo:** Parcialmente expõe firma ao risco de custo. Parâmetro de compartilhamento α* depende de:
- Variância dos choques de custo
- Curvatura da desutilidade do esforço
- Custo sombra dos fundos públicos λ

### Dinâmica e Hold-Up (Capítulo 3)

Estende análise estática para settings dinâmicos com renegociação (construindo sobre Tirole 1986).

**Hold-up dinâmico:** Após firma investir, regulador observa custo (ou infere via custo realizado) e propõe novo contrato capturando valor gerado pelo investimento. Firma antecipa → underinvestment.

**Commitment:** Mecanismo ótimo requer compromisso de não-renegociar — mas governos frequentemente não conseguem comprometer-se credivamente. Esta é a tensão fundamental em procurement de infraestrutura.

### Relação com Seleção Adversa (Akerlof)

Laffont-Tirole formaliza o que Akerlof (1970) descreve qualitativamente: quando comprador não pode observar qualidade do fornecedor, o mecanismo de preço puro falha. Laffont-Tirole prescreve o mecanismo ótimo (menu de contratos) que minimiza a ineficiência residual.

## Interpretação

⚠️ Interpretação do compilador — não está explicitamente em Laffont & Tirole nesta forma.

**Aditivos sob a teoria Laffont-Tirole:** Os aditivos do sistema brasileiro (Lei 8.666/93 + limite de 25%) podem ser analisados como:

1. Regulador (governo) forçado a usar FP-like contracts (licitação por menor preço) mesmo para projetos complexos → alta incerteza de custo → teoricamente deveria usar C+ ou mix
2. Aditivos = renegociação ex-post que converte parcialmente o FP em C+
3. Mas a conversão acontece *depois* que a firma ganhou o leilão → sem o efeito de revelação de tipo do mecanismo ótimo → renda informacional maior para o fornecedor

O sistema atual é subótimo por design: força FP em contratos que deveriam ser mix, depois permite renegociação que produz C+ sem o design de incentivos correto.

## Quality Gate
- [x] Wikilinks tipados: sourced from tirole 1986
- [x] Instance→class: λ = shadow cost of public funds (específico ao modelo L-T)
- [x] Meta-KB separado: Zelox context em Interpretação
- [x] Resumo calibrado: ⚠️ stub mencionado

## Conexões

- extends: [[procurement-renegotiation]] ON "Capítulo 3 formaliza dinamicamente o hold-up de Tirole 1986"
- derivedFrom: [[market-for-lemons]] ON "formalização ótima da assimetria de informação em procurement"
- relaciona: [[corruption-audits-brazil]] ON "modelo prediz padrões de extração de renda observados em dados CGU"

## Fontes

- [Laffont & Tirole (1993)](../../raw/papers/laffont-tirole-1993-theory-incentives-procurement.md) — MIT Press. Capítulos 1-3: modelo básico, trade-off eficiência-renda, contrato ótimo mix FP/C+, hold-up dinâmico. ⚠️ Stub — texto completo não lido.
