---
title: "Epistemic Dependency Copula"
sources:
  - path: wiki/concepts/copula-dependency-modeling.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/formal-ontology-for-kbs.md
    type: synthesis
    quality: primary
created: 2026-04-12
updated: 2026-04-12
tags: [meta-kb, dependency-modeling, emergence, epistemic-structure, typed-relations, wikilinks]
source_quality: medium
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: true
quarantine_created: 2026-04-12
quarantine_reason: "Artigo emergido de /ask cross-domain — aguarda confirmação adversarial e review frio"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
provenance: emergence
emergence_trigger:
  pair: [copula-dependency-modeling, formal-ontology-for-kbs]
  ask_session: outputs/logs/sessions/2026-04-12/ask-copula-analogy.md
  connection_type: ANÁLOGO-A
  pearl_level: L2
emerged_on: 2026-04-12
---

## Resumo

Wikilinks tipados capturam dependência epistêmica declarada entre artigos — análoga à cointegração linear, simétrica por definição. Mas artigos que co-ativam consistentemente em sessões /ask sem wikilink explícito exibem dependência empírica não-linear: as "fat tails epistêmicas" do KB. O Cumulative Mispricing Index (CMI) das cópulas financeiras tem análogo epistêmico: rastrear divergência cumulativa de co-ativações pode detectar staleness de pares antes que artigos individuais se tornem obsoletos.

## Conteúdo

### O que copula-dependency-modeling contribui

Pelo Teorema de Sklar, qualquer distribuição conjunta F(x₁, x₂) decompõe-se em:
```
F(x₁, x₂) = C(F₁(x₁), F₂(x₂))
```
A cópula C captura exclusivamente a estrutura de dependência — separada das distribuições marginais. As famílias de cópulas revelam que dependência pode ser:
- **Simétrica** (Gaussian, Frank): co-movimentos iguais em ambas as direções
- **Assimétrica de cauda inferior** (Clayton): dependência mais forte em co-crashes
- **Assimétrica de cauda superior** (Gumbel): dependência mais forte em co-booms

O CMI (Cumulative Mispricing Index) agrega desvios da relação esperada ao longo do tempo:
```
CMI_t = CMI_{t-1} + (h_t - 0.5)
```
sinalizando divergência persistente entre dois ativos antes que cada ativo individualmente mostre anomalia.

### O que formal-ontology-for-kbs contribui

Wikilinks tipados (parte-de, contradiz, deriva-de) capturam a estrutura de dependência **declarada** entre artigos — o que o compilador enuncia explicitamente. Mas o artigo identifica que 114 wikilinks atuais são não-tipados: semanticamente equivalentes, sem distinção de força ou direção.

Mais relevante: a distinção BFO entre **continuants** (artigos, que persistem) e **occurrents** (sessões /ask, que se desdobram no tempo) expõe uma lacuna — o KB rastreia entidades mas não processos. Não há registro de quais artigos co-ocorreram em quais sessões.

### O que emerge da combinação

(⚠️ interpretação do compilador — ausente em ambas as fontes individualmente)

**Wikilinks tipados = cointegração epistêmica.** São relações declaradas, lineares, simétricas por convenção (ou assimétricas por tipagem explícita). Capturam o que o compilador sabe que sabe. Análogo à cointegração gaussiana: funciona bem em regime normal, falha em regimes de dependência não-linear.

**Co-ativações empíricas sem wikilink = fat tails epistêmicas.** Quando dois artigos co-ativam consistentemente em sessões /ask sem wikilink declarado, isso revela dependência estrutural latente — não articulada pelo compilador mas real no uso. Clayton sugere: a dependência pode ser mais forte em "queries de falha" (quando um artigo está stale, o outro também tende a estar). Gumbel sugere: em queries de alta confiança, ambos tendem a contribuir em conjunto.

**CMI epistêmico como proxy de staleness de pares.** Se dois artigos frequentemente co-ativados começam a divergir em utilidade — um sendo corrigido, o outro não — o CMI epistêmico acumularia sinal de desalinhamento antes que qualquer um dos dois dispare threshold de staleness individual. Isso permitiria detectar "pares de artigos cointegrados que divergiram" antes do sinal individual.

**Design proposto:** adicionar ao utility tracker campos de co-ativação:
```yaml
# em cada sessão /ask, logar:
co_activated_with: [artigo-B]
dependency_type: observed   # vs declared (wikilink)
regime: failure_query | success_query | exploratory
```
Acumulados em N sessões, esses dados permitem estimar empiricamente quais pares têm dependência forte — e de que tipo.

## Especulação

- Assimetria de dependência epistêmica (Clayton vs Gumbel no KB) é empiricamente observável no utility tracker — mas requer dados de ≥50 sessões /ask documentadas com co-ativações. Atualmente não existe esse volume (⚠️ claim especulativo, pré-dados).
- CMI epistêmico pode não exibir comportamento mean-reverting se dois artigos legitimamente divergem de domínio ao longo do tempo — o sinal seria positivo falso de staleness.
- O análogo ao Kendall's Tau para medir correlação rank entre artigos seria: frequência de co-ativação dividida por frequência de ativação individual. Mais robusto que contagem simples.
- Bibliometria já formalizou co-citation analysis como dependência epistêmica em corpus científico — este conceito pode ser instância de framework existente (gap identificado no /ask: wiki/concepts/bibliometrics.md ausente).

## Verificação adversarial

**Pergunta falsificável:** "A frequência de co-ativação de pares sem wikilink correlaciona com a existência de wikilink descoberto posteriormente pelo compilador?"

**Evidência que confirmaria:** Em ≥50 sessões /ask, pares com alta frequência de co-ativação sem wikilink teriam >70% de probabilidade de receberem wikilink em /review subsequente — indicando que a dependência empírica precede a declaração formal.

**Evidência que refutaria:**
- Co-ativações refletem apenas estrutura de queries do compilador (viés de amostragem), não dependência real entre artigos
- O compilador consulta artigos adjacentes por hábito, não por necessidade epistêmica
- Wikilinks tipados já capturam toda dependência relevante — co-ativações são ruído de query

**Gap identificado no /ask que invalida parcialmente:** wiki/concepts/bibliometrics.md (co-citation analysis) e wiki/concepts/bradford-law-scattering.md foram identificados como artigos DEVERIA ter sido consultados mas não foram — sugerindo que a analogia pode ser instância de framework bibliométrico já formalizado, não conceito genuinamente novo.

## Conexões

- emerge-de: [[copula-dependency-modeling]] ON "Teorema de Sklar: separação marginal/dependência; CMI como sinal cumulativo de divergência"
- emerge-de: [[formal-ontology-for-kbs]] ON "wikilinks tipados como relações declaradas; lacuna entre continuants rastreados e occurrents não rastreados"
- análogo-a: [[statistical-arbitrage-pairs-trading]] ON "cointegração como dependência linear; cópula detecta o que cointegração deixa escapar"
- gap-para: bibliometrics (co-citation analysis) — artigo ausente; conexão mais direta pode estar lá
- gap-para: bradford-law-scattering — proxy de dependência entre zonas de conhecimento

## Fontes

- [[copula-dependency-modeling]] — Teorema de Sklar, famílias de cópulas (Clayton/Gumbel/Gaussian), CMI como sinal cumulativo
- [[formal-ontology-for-kbs]] — wikilinks tipados, continuants vs occurrents (BFO), typed relations como dependência declarada
- [Log /ask](../../outputs/logs/sessions/2026-04-12/ask-copula-analogy.md) — sessão que confirmou a conexão ANÁLOGO-A

> ⚠️ QUARENTENA: artigo emergido de /ask cross-domain. Critérios pendentes: tempo (24h), review frio, adversarial.
