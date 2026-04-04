---
title: "Procurement and Renegotiation (Tirole 1986)"
sources:
  - path: raw/papers/tirole-1986-procurement-renegotiation-jpe.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [economics, procurement, incomplete-contracts, hold-up, renegotiation, b2g, public-contracts]
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

Tirole (1986) modela procurement como contrato incompleto de dois períodos. Comprador e vendedor assinam contrato inicial; depois adquirem informação privada sobre custos e valorações; têm incentivo para renegociar. Resultado central: o fornecedor *underinvest* no período pré-contrato porque antecipa que o comprador tentará se apropriar do valor gerado pelo investimento via renegociação. Este é o "hold-up problem" em procurement. JPE 94(2), pp. 235-259.

⚠️ Fonte primária (PDF) não acessível no ingest — artigo baseado em descrição secundária de working paper MIT e search results. Tratar como source_quality: medium até obter acesso direto.

## Conteúdo

### O Modelo de Dois Períodos

**Período 1 (pré-contrato):** Fornecedor (vendor) investe em capacidade/qualidade. O investimento é custoso e não-verificável por terceiros (não pode ser contratado diretamente).

**Após o contrato:** Comprador e vendedor adquirem informação privada — o vendedor aprende seus custos reais, o comprador aprende sua valoração real. Essa informação não estava disponível quando o contrato foi assinado.

**Período 2 (renegociação):** Como o contrato inicial é incompleto (não especifica todas as contingências), as partes têm incentivo para renegociar à luz das informações adquiridas.

### O Hold-Up Problem

O problema central: o fornecedor antecipa a renegociação do período 2 e, portanto, reduz seu investimento no período 1.

**Mecanismo:**
1. Fornecedor investe I no período 1, criando valor V
2. No período 2, comprador observa (ou infere) V e propõe renegociação
3. O surplus de renegociação é dividido entre as partes (Nash bargaining)
4. Fornecedor antecipa que capturará apenas fração α do valor criado → investe apenas se αV ≥ I
5. O investimento ótimo socialmente requer V ≥ I → subinvestimento quando α < 1

**Resultado:** Em equilíbrio, o fornecedor underinvests relativamente ao ótimo social. O grau de underinvestment depende do poder de barganha relativo das partes na renegociação.

### Implicações para Design de Contratos

**Contratos de preço fixo (fixed-price):** Comprador não pode renegociar para baixo se custos do fornecedor forem menores → fornecedor tem full incentive to invest to reduce costs. Mas expõe o comprador a custos imprevistos.

**Contratos de custo mais margem (cost-plus):** Comprador repassa todos os custos → fornecedor sem incentivo para investir em redução de custos (moral hazard).

**Contratos ótimos:** Combinam elementos dos dois — parcialmente expõe o fornecedor ao risco para preservar incentivos, parcialmente protege contra custos imprevistos. A mistura ótima depende da distribuição de incerteza e do poder de barganha.

### Contratos Incompletos e Renegotiation-Proofness

Um contrato é "renegotiation-proof" se nenhuma das partes tem ganho de propor renegociação ex-post. Para procurement, a condição é rara porque:
- Custos reais diferem dos estimados no contrato
- Scope do projeto evolui
- Eventos não antecipados ocorrem

A impossibilidade de contratos completos (especificando todas as contingências para todos os estados da natureza) é a premissa fundamental da teoria de contratos incompletos (Grossman & Hart 1986; Hart & Moore 1990 — contemporâneos a Tirole 1986).

### Aplicações em Procurement Público

Em procurement público, o hold-up problem tem dimensões adicionais:
- **Comprador = governo:** restrições legais e políticas limitam flexibilidade de renegociação
- **Fornecedor knows:** em contratos de obra pública, o fornecedor geralmente tem informação superior sobre custos reais
- **Additive contracts (aditivos):** a legislação brasileira (Lei 8.666/93) permite que contratos sejam aumentados em até 25% sem nova licitação — esse mecanismo é *precisamente* o canal de renegociação que Tirole modela, e que fornecedores estratégicos podem explorar

### Relação com Renegotiação Estratégica

Tirole distingue renegociação *eficiente* (mútuo ganho real, ex: scope mudou genuinamente) de renegociação *estratégica* (extração de renda pelo fornecedor que underperforma intencionalmente para forçar renegociação).

Em procurement público, a distinção é crítica: aditivos legítimos vs aditivos como instrumento de corrupção.

## Interpretação

⚠️ Interpretação do compilador — conexão B2G não está em Tirole 1986.

**Aditivos como hold-up instrument:** Fornecedores que ganham licitações com proposta baixa (winning on price) e depois solicitam aditivos de 25% podem estar executando estratégia de hold-up: comprometimento ex-ante com preço baixo, extração de surplus ex-post via renegociação. O comprador (governo) está "held up" porque trocar o fornecedor a meio contrato é ainda mais custoso (sunk costs, prazos).

**Implicação para risk scoring:** Histórico de aditivos por fornecedor (taxa de contratos que chegam ao limite de 25%, ou que solicitam aditivos nas fases finais) é proxy de comportamento estratégico de renegociação. Esse sinal pode ser calculado via dados PNCP/TCU.

**Limite do modelo:** Tirole modela dois períodos com duas partes. Procurement público envolve múltiplos contratos ao longo do tempo, reputação acumulada, e possibilidade de exclusão de fornecedores — dimensões que o modelo original não capta mas que são relevanets para design de sistema de risk scoring.

## Verificação adversarial

**O que esta versão NÃO tem:**
- Fonte primária direta (JPE paper) não lida no ingest — baseado em secondary sources
- Não cobre extensões do paper (versão publicada AER vs working paper MIT 1985)
- Provavelmente existem claims do paper que esta versão simplifica ou omite

**Prior work:** Grossman & Hart (1986) "The Costs and Benefits of Ownership" formaliza contratos incompletos. Hart & Moore (1988/1990) estende. Williamson (1975) "Markets and Hierarchies" discute hold-up informalmente antes da formalização. Tirole (1986) é um dos primeiros modelos formais de procurement como contrato incompleto.

## Conexões

- [[market-for-lemons]] ON "assimetria de informação sobre custos reais do fornecedor no momento da licitação"
- [[corruption-audits-brazil]] ON "aditivos irregulares são forma documentada de corrupção em procurement municipal"
- [[information-asymmetry-b2g]] ON "hold-up como mecanismo de extração de renda em contratos públicos"

## Fontes

- Tirole, J. (1986). "Procurement and Renegotiation." *Journal of Political Economy*, 94(2), 235-259. DOI: 10.1086/261372. MIT working paper 362 (1985).
- Descrição secundária via RepEC e Semantic Scholar — acesso direto ao PDF pendente.
