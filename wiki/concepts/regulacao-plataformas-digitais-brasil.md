---
title: "Regulação de Plataformas Digitais no Brasil — PL 4675/2025 (Lei de Mercados Digitais)"
sources:
  - path: raw/articles/pl-4675-2025-mercados-digitais-brasil.md
    type: article
    quality: secondary
    stance: neutral
created: 2026-04-08
updated: 2026-04-08
tags: [regulacao, plataformas-digitais, brasil, cade, mercados-digitais, b2g, govtech, pl-4675, antitrust]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: false
quarantine_promoted: 2026-04-08
quarantine_criteria_met:
  auto_promote: false
  promoted_after_corrections: true
  gates_passed: [1, 2, 3, 4]
  gate3_run: 2026-04-08
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  gate3_claims_challenged: 8
  gate3_claims_survived: 1
  gate3_claims_weakened: 3
  gate3_claims_invalidated: 4
  challenge_verdict: CORRIGIDO_PROMOVIDO
  corrections_applied:
    - "6 critérios: de checklist cumulativo para avaliação holística (modelo DMA)"
    - "GovTech threshold: adicionado caveat de grupo econômico (Neoway/B3)"
    - "Data de votação: marcada como fonte 2026 com caveat de staleness"
    - "10 anos renovável: marcado como previsto mas sujeito a alteração"
    - "Cease and Desist: substituído por TCC (terminologia brasileira correta)"
---

## Resumo

PL 4675/2025 cria regime ex ante de regulação concorrencial para plataformas "de relevância
sistêmica" no Brasil: R$50B+ global OU R$5B+ no Brasil, mais 6 critérios qualitativos. Estimativa:
5-10 plataformas designadas (Big Tech). GovTechs e B2G analytics ficam abaixo do threshold —
o PL não cria barreira regulatória contra concorrentes de médio porte, apenas contra Big Tech.

## Conteúdo

### Contexto e Origem

Enviado ao Congresso em setembro 2025 pelo Governo Federal. Resultado de 2 anos de estudos,
inspirado no Digital Markets Act (DMA) europeu. Câmara aprovando regime de urgência em
18/02/2026 (276 × 186) *conforme fontes de 2026 — modelos com cutoff anterior podem não
conhecer este evento*. Em tramitação — texto ainda sujeito a ajustes.

CADE já atuou preventivamente: **TCC (Termos de Compromisso de Cessação)** com Apple e Google
sobre ecosystem governance e restrições contratuais (pré-PL 4675).

### Critérios de Designação de Relevância Sistêmica

**Threshold financeiro** (pelo menos um):
- Faturamento bruto anual **global > R$ 50 bilhões**, OU
- Faturamento **no Brasil > R$ 5 bilhões**

**6 critérios qualitativos** (avaliados conjunta e holisticamente — modelo DMA):
1. Atuação em mercados de múltiplos lados (two-sided markets)
2. Forte efeito de rede
3. Integração vertical
4. Presença em mercados adjacentes
5. Acesso relevante a dados
6. Posição estratégica para negócios de terceiros

*Qualificação:* os 6 critérios não funcionam como checklist cumulativo estrito (todos devem
coexistir simultaneamente). Seguindo a lógica do DMA europeu, são avaliados de forma holística
— combinação e peso relativo determinam a designação, não presença obrigatória de todos.

**Estimativa:** 5 a 10 plataformas designadas — foco em Google, Meta, Apple, Amazon, Microsoft.

### Obrigações das Plataformas Designadas

**Transparência:**
- Divulgação de termos de uso, critérios técnicos, políticas de dados, estrutura de preços
- Critérios de ranqueamento e exibição de conteúdos/ofertas (anti self-preferencing)

**Abertura tecnológica:**
- Portabilidade de dados
- Interoperabilidade obrigatória
- Permissão a aplicações externas
- Condições isonômicas de acesso à infraestrutura

**Proibições:**
- Dificultar participação de concorrentes
- Auto-preferenciamento (self-preferencing)

**Conformidade:** Relatórios periódicos à nova Superintendência de Mercados Digitais do CADE.
Enquadramento por até 10 anos, renovável *(prazo previsto no texto atual — sujeito a alteração
durante tramitação).*

### Superintendência de Mercados Digitais (CADE)

Nova unidade dentro do CADE com poderes:
- Monitoramento contínuo de plataformas designadas
- Requisição de informações e instauração de processos administrativos
- Atuação tanto repressiva (pós-conduta) quanto preventiva
- Proposta de medidas ao Tribunal do CADE (que decide)

### Implicações por Faixa de Faturamento

| Faixa no Brasil | Status sob PL 4675 | Regime |
|---|---|---|
| > R$ 5B | Potencialmente designada | Obrigações ex ante + fiscalização contínua |
| R$ 1–5B | Abaixo do threshold | Liberdade operacional plena; CADE pode atuar preventivamente |
| < R$ 1B | Claramente abaixo | Sem obrigações específicas do PL |

**Plataformas GovTech / B2G analytics de escala pequena/média** (Fonte de Preços, demais
players de procurement analytics): faturamento provavelmente abaixo de R$ 5B no Brasil —
**não são afetadas pelo PL 4675 diretamente**. *Qualificação importante: verificar grupo
econômico. Neoway, por exemplo, integra o grupo B3 (faturamento >> R$ 5B) — plataformas
subsidiárias de grandes grupos financeiros podem ser designadas pela receita consolidada
do grupo, não da subsidiária isolada.*

## Interpretação

⚠️ Interpretação do compilador.

**Implicação central para Zelox:**

O PL 4675/2025 cria um escudo regulatório **assimétrico**: protege Zelox e demais
plataformas de médio porte apenas contra entrada de Big Tech com obrigações de interoperabilidade
e portabilidade. Não cria fricção contra concorrentes GovTech de escala similar a Zelox.

**Três cenários competitivos:**

| Cenário | Efeito do PL 4675 |
|---|---|
| Big Tech (Google, AWS) entra em B2G analytics | PL 4675 pode exigir interoperabilidade e transparência algorítmica — aumenta custo de entrada |
| GovTech mid-size (Neoway, Quaest) expande para procurement risk | PL 4675 NÃO se aplica — competição direta sem barreira regulatória |
| Zelox cresce até R$ 5B | PL 4675 começa a se aplicar — obrigações de transparência e interoperabilidade |

**Consequência estratégica:** O moat regulatório do PL 4675 é real mas limitado. Para competição
com concorrentes de médio porte, o moat deve ser epistêmico + legal (inexigibilidade), não
regulatório-derivado do PL 4675.

**O que NÃO esperar do PL 4675 como proteção:** O PL não protege Zelox do que é concretamente
a maior ameaça — plataformas de risk scoring de licitações com R$ 50-500M de faturamento que
commoditizem o segmento de menor valor (análise de preços, alertas simples de irregularidade).

## Verificação adversarial

**Claim mais fraco:** "GovTechs estão abaixo do threshold" — correto para a situação atual,
mas o setor pode crescer rapidamente; threshold pode ser reduzido em versão final do PL.

**O que o documento NÃO diz:**
- Não há jurisprudência ainda (lei em tramitação) — aplicação prática é incerta
- Não cobre setores regulados específicos (saúde, financeiro, advocacia) — apenas plataformas digitais gerais
- Texto ainda pode mudar substancialmente durante tramitação

**Simplificações:** Trata PL como lei consolidada quando está em tramitação. A versão final pode
alterar thresholds financeiros ou critérios qualitativos.

**Prior work:** DMA europeu (2022) é a referência; EUA discute Similar Bill Of Rights for
digital markets mas sem lei equivalente; Brasil está alinhado com tendência global de regulação
ex ante de Big Tech.

## Quality Gate
- [x] Wikilinks tipados
- [x] Instance→class: R$50B global / R$5B Brasil são thresholds do PL — pode mudar
- [x] Meta-KB separado: análise Zelox em Interpretação
- [x] Resumo calibrado: nota de tramitação incluída

## Conexões

- complementa: [[platform-moat-entrenchment]] ON "PL 4675 implementa no Brasil a lógica ex ante que OECD recomenda — obrigações de interoperabilidade e portabilidade mitigam os mecanismos de entrenchment 3, 4 e 5 da taxonomia OECD"
- complementa: [[platform-economics]] ON "regulação ex ante altera o resultado 'plataformas quase sempre vencem' para plataformas designadas — obrigações de portabilidade reduzem switching costs estruturais"
- complementa: [[inexigibilidade-notoria-especializacao]] ON "o PL 4675 não regula contratos personalíssimos — inexigibilidade permanece o mecanismo de escape do bidding independente do PL"
- complementa: [[procurement-variety-gap]] ON "PL 4675 adiciona dimensão de regulação de plataformas ao contexto B2G brasileiro — mas atinge apenas Big Tech, não o segmento de GovTech de procurement analytics"

## Fontes

- [PL 4675/2025 — análise Mazzucco&Mello](../../raw/articles/pl-4675-2025-mercados-digitais-brasil.md) — Critérios de designação, obrigações, Superintendência CADE, implicações para médio porte.
