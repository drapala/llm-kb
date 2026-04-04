---
title: "Binding Attention Regime"
sources:
  - path: wiki/concepts/rational-inattention.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/fast-frugal-heuristics.md
    type: synthesis
    quality: primary
created: 2026-04-04
updated: 2026-04-04
tags: [emergence, information-theory, decision-theory, bounded-rationality, retrieval, ecological-rationality]
source_quality: medium
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: true
quarantine_created: 2026-04-04
quarantine_reason: "Artigo emergido de /ask cross-domain (info-theory × cognitivo) — aguarda confirmação adversarial e review frio"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
provenance: emergence
emergence_trigger:
  pair: [rational-inattention, fast-frugal-heuristics]
  ask_session: outputs/logs/sessions/2026-04-04/ask-rational-inattention-frugal.md
  connection_type: INSTANCIA
  pearl_level: L1
emerged_on: 2026-04-04
---

## Resumo

Sims (2003) e Gigerenzer (décadas de trabalho) fizeram afirmações distintas sobre o mesmo regime: Sims derivou o comportamento ótimo quando a constraint I(X;Y) ≤ C é binding; Gigerenzer documentou empiricamente que heurísticas frugais ganham de modelos complexos nesse mesmo regime. O conceito emergido: **ecological rationality = optimal attention allocation** — a heurística ecologicamente racional é a solução do problema de Sims para C escasso. Take-the-Best é a solução ótima quando C = 1 bit.

## Conteúdo

### O que rational-inattention contribui

Sims (2003): agente com constraint I(X;Y) ≤ C minimiza `E[(Y-X)²]`. Para X Gaussiano, solução: `Var(Y|X) = Var(X)/e^{2C}`. Quando C → 0: Y independente de X (ignore tudo). Quando C = 1 bit: Y responde a exatamente 1 bit de informação sobre X — suficiente para uma comparação binária.

O framework é normativo e contínuo: pressupõe capacidade mensurável em bits e distribuições Gaussianas. Não endereça cues discretos nem estrutura do ambiente.

### O que fast-frugal-heuristics contribui

Gigerenzer: Take-the-Best examina cues em ordem decrescente de validade, escolhe no primeiro cue discriminante, ignora o resto. Funciona melhor em small n, high d, unknown distributions. Mecanismo: bias-variance — frugalidade reduz variância; quando variância domina (small n), menos cues = melhor performance.

O framework é descritivo-empírico: documenta quando a frugalidade funciona, mas não deriva qual é a capacidade ótima de processamento. Não conecta a um formalismo de information theory.

### O que emerge da combinação

⚠️ Interpretação do compilador — não está em nenhuma das duas fontes.

**Regime identification:** O conjunto de condições onde Take-the-Best ganha (small n, high d, Knightian uncertainty, unknown distribution) é o mesmo regime onde a constraint de Sims é binding. O sinal empírico de Gigerenzer ("frugalidade vence") identifica onde a capacidade efetiva é escassa.

**Ecological rationality como optimal attention allocation:** Gigerenzer diz que uma heurística é ecologicamente racional se "adapted to the structure of an environment." Sims diz que o agente ótimo aloca seus C bits onde o sinal tem maior informação. São a mesma afirmação — o alinhamento estrutural da heurística ao ambiente é precisamente o que permite que C escasso produza boas decisões. O agente não precisa resolver o problema de Sims explicitamente; a adaptação ecológica faz isso implicitamente.

**Take-the-Best como solução de Sims:** Se C = 1 bit e há k cues binários ordenados por validade, a solução ótima é usar o cue mais válido como único discriminante — que é exatamente Take-the-Best. C → 0 (ignore tudo) é o limite trivial; C = 1 bit é o limite informativo não-trivial.

**Diagrama de convergência:**

```
Gigerenzer: "small n, high d → heurísticas frugais ganham"
                    ↕ mesmo regime
Sims: "I(X;Y) ≤ C binding → use C bits nos cues mais informativos"
```

### Implicação para retrieval em KBs

⚠️ Aplicação ao design desta KB — nossa interpretação.

A arquitetura 3-camadas do /ask é rational inattention implementada:

| Camada | C efetivo | Análogo Gigerenzer |
|--------|-----------|---------------------|
| Layer 1 (_index.md, ~150 chars) | ~0.1 bits/artigo | Recognition heuristic |
| Layer 2 (5-10 artigos wiki) | moderado | Take-the-Best |
| Circuit breaker (≤10 artigos) | teto de C | Stop rule de Take-the-Best |

**Predição derivada (falsificável):** O trigger de migração do _index.md não é um número fixo de artigos — é quando a Layer 1 perde poder discriminante (C efetivo cai abaixo do threshold necessário para identificar artigos relevantes com 150 chars). Atualmente (54 artigos): ok. Estimativa de degradação: 150-200 artigos com 150 chars cada (~22-30K tokens no Layer 1), quando o recall de artigos relevantes em Layer 1 cair abaixo de 80%.

## Correção pós-ingestão (Matějka & McKay 2011)

A solução ótima de rational inattention para escolhas discretas é o **multinomial logit** (Theorem 3), não Take-the-Best. Take-the-Best é uma aproximação válida do logit quando `|q_best - q_second| >> λ` — regime de dominância clara onde o logit concentra prob ≈ 1 na melhor opção. Gigerenzer's ecological rationality identifica exatamente os ambientes onde essa aproximação é boa.

Portanto, a formulação original "Take-the-Best = solução de Sims quando C = 1 bit" está imprecisa. A relação correta: **logit = solução exata; Take-the-Best = caso-limite com dominância estrutural**. A conexão entre Gigerenzer e Sims/Matějka-McKay é real, mas mais sutil.

**Impacto no pearl_level:** O logit de Matějka-McKay eleva a fundamentação de L1 para L2 para a parte central (logit = rational inattention discreta), mas a conexão específica com Take-the-Best permanece L1 (regime de dominância não é derivado formalmente, apenas identificado).

## Especulação

- A formalização de Take-the-Best como logit em regime de dominância ainda requer derivação formal não feita neste artigo.
- Se a derivação formal estiver correta, Take-the-Best não é apenas uma observação empírica — é uma lei: o agente com C = 1 bit e k cues DEVE usar o melhor cue único. Isso elevaria Gigerenzer de descritivo para normativo.
- Implicação para KB: o número ótimo de artigos a ler no Layer 2 é diretamente calculável dado C efetivo do retrieval engine e a distribuição de relevância dos artigos. Hoje chutamos 5-10; isso poderia ser derivado.

## Verificação adversarial

**Pergunta falsificável:** Em KBs de diferentes tamanhos, o recall de artigos relevantes em Layer 1 (usando _index.md com ~150 chars/artigo) degrada de forma consistente com o limite de C efetivo? Se sim, quando a KB crescer para 150+ artigos, o Layer 1 precisará de mais bits/artigo para manter recall.

**Evidência que confirmaria:**
- Matějka & McKay (2015) deriva que a solução de rational inattention discreta é logit com temperature proporcional a C — e Take-the-Best emerge como C → 1 bit nesse framework
- Métricas do utility-tracker mostram que `retrievals_gap` aumenta conforme o índice cresce sem migração

**Evidência que refutaria:**
- Sims é Gaussiano contínuo; cues de Take-the-Best são binários discretos — o mapeamento pode quebrar na formalização
- Gigerenzer: ecological rationality depende de QUAL ambiente, não só de C escasso — sem o alinhamento certo, C = 1 bit produz resultado pior, não Take-the-Best

**Risco de over-synthesis:** A convergência é observada via analogia estrutural (L1). Elevar para L2 (intervenção: "use C = 1 bit para determinar número ótimo de cues") requer derivação formal ausente.

## Conexões

- emerge-de: [[rational-inattention]] ON "constraint I(X;Y)≤C → comportamento ótimo quando C=1 bit"
- emerge-de: [[fast-frugal-heuristics]] ON "Take-the-Best = 1 cue = C=1 bit; ecological rationality = optimal allocation"
- relaciona: [[information-bottleneck]] ON "⚠️ IB também opera em tradeoff bits-vs-relevância; binding regime pode ser formalizado via IB"
- relaciona: [[retrieval-augmented-generation]] ON "⚠️ circuit breaker do /ask é implementação de Take-the-Best para retrieval"

## Fontes

- [[rational-inattention]] — Sims (2003): formalização de I(X;Y)≤C e solução ótima Gaussiana
- [[fast-frugal-heuristics]] — Gigerenzer: Take-the-Best, less-is-more, ecological rationality
- [Log /ask](../../outputs/logs/sessions/2026-04-04/ask-rational-inattention-frugal.md) — sessão que descobriu a convergência de regime

**Gap explícito:** Matějka & McKay (2015) — "Rational Inattention to Discrete Choices: A New Foundation for the Multinomial Logit Model." Formaliza rational inattention para cues binários/discretos. Necessário para elevar L1 → L2.

> ⚠️ QUARENTENA: artigo emergido de /ask cross-domain (Sims × Gigerenzer). Critérios pendentes: tempo (24h), review frio, adversarial ou Matějka & McKay (2015) como L2 prediction.
