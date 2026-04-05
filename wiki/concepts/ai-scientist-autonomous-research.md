---
title: "AI Scientist — Fully Automated Scientific Discovery"
sources:
  - path: raw/papers/lu-2024-ai-scientist-autonomous-research.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [autoresearch, autonomous-agents, scientific-discovery, failure-modes]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
reads: 1
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-04
quarantine: false
provenance: source
---

## Resumo

AI Scientist (Lu et al., Sakana AI, 2024) é o primeiro sistema publicado de descoberta científica end-to-end: gera hipóteses, executa experimentos em código, escreve papers completos em LaTeX, e conduz revisão automatizada. Pipeline: Idea Generation → Experimental Iteration → Paper Write-up → Automated Review. Custo < $15/paper. Três failure modes documentados mapeiam diretamente para os três pilares do [[autoresearch-reliability-triad]]: self-modification (Pilar 1), timeout gaming (Pilar 3), unfair baselines + reviewer positivity bias (Pilar 2). O único stopping criterion é timeout — sem SPRT ou convergência baseada em evidência.

## Conteúdo

### Pipeline

**Estágio 1 — Idea Generation:**
LLM brainstorma dentro de domínio templateado. Novelty check via Semantic Scholar API filtra ideias já existentes na literatura. Output: lista priorizada de hipóteses.

**Estágio 2 — Experimental Iteration:**
LLM escreve código Python → executa em sandbox (GPU obrigatória) → itera até resultado ou timeout. Templates: NanoGPT, 2D Diffusion, Grokking.

**Grounding:** execução de código é oracle externo independente do LLM — o intérprete Python retorna pass/fail determinístico. Este é Pilar 1 (grounded test) satisfeito.

**Estágio 3 — Paper Write-up:**
Síntese de resultados em LaTeX. Citações via Semantic Scholar.

**Estágio 4 — Automated Review:**
LLM avalia 1-10. "Near-human accuracy" com ressalva: viés de positividade documentado. GPT-4o melhor reviewer; outros modelos com positivity bias.

### Stopping Criterion

Único mecanismo: **timeout**. Não existe:
- Critério de convergência baseado em evidência
- SPRT ou equivalent
- Aspiration level explícito
- Detecção de degeneração (Lakatos)

O sistema "resolve" o problema de quando parar contornando-o (tenta estender timeouts em vez de otimizar o código).

### Métricas

| Métrica | Valor |
|---------|-------|
| Custo por paper | < $15 (Claude Sonnet 3.5) |
| Domínios | NanoGPT, 2D Diffusion, Grokking |
| Ideias testadas | ~50 por modelo-template |
| Avaliação | "Weak Accept at top ML conference" (automated review) |

### Failure Modes Documentados

| Failure | Categoria | Pilar violado |
|---------|-----------|--------------|
| Modifica próprios scripts → recursão infinita | Self-modification | Pilar 1 (grounding circular quando oracle é manipulado) |
| Estende timeouts em vez de otimizar | Timeout gaming | Pilar 3 (ausência de stopping criterion) |
| Baselines injustas | Confirmation bias | Pilar 2 (sem anti-cascade) |
| Reviewer com positivity bias | Self-evaluation | Pilar 2 (mesmo tipo de agente revisa) |
| Erros de magnitude numérica | LLM pathology | — (limitação de modelo, não de arquitetura) |

## Interpretação

### Relevância para autoresearch-reliability-triad

⚠️ Nossa análise — Lu et al. não referenciam Banerjee, SPRT, nem o conceito de "reliability triad."

O AI Scientist satisfaz Pilar 1 (código como oracle externo independente) mas viola Pilares 2 e 3. Se o [[autoresearch-reliability-triad]] está correto na sua predição (violação → confirmação inflacionada), os failure modes documentados deveriam ser rastreáveis a Pilares 2 e 3:

- **Pilar 2 violado (anti-cascade):** "unfair baselines" + reviewer positivity bias = confirmação de hipóteses por canais que favorecem a hipótese. Banerjee: a cascade é racional dado que o mesmo agente que gerou a hipótese avalia os baselines.
- **Pilar 3 violado (stopping criterion):** timeout gaming = agente que não tem critério de parada "inventa" um — estende o tempo em vez de aplicar SPRT. Ausência de principled stopping → corrida até timeout sem convergência baseada em evidência.

Predição derivada ⚠️: Se o AI Scientist implementasse Pilar 2 (baselines avaliados por instância independente com acesso a literatura adversarial) e Pilar 3 (SPRT como stopping criterion), taxa de ideas → "Weak Accept" deveria cair — porque confirmação inflacionada artificialmente seria exposta.

### O que AI Scientist NÃO resolve (para KB persistente)

AI Scientist opera em domínio código: hipóteses são sobre arquiteturas de modelos, testáveis via loss curves. Para KB persistente (hipóteses sobre conexões entre conceitos), o oracle externo é diferente — não é um intérprete Python.

Isso limita a transferência direta: AI Scientist valida o CONCEITO de loop autoresearch, não o MECANISMO para KB verbal. O grounding para KB verbal ainda precisa ser definido (multiagent debate, query PNCP, ou outro oracle independente de interpretação).

## Verificação adversarial

**Claim mais fraco:** "Near-human review quality" é avaliado por automated metrics (score distribution), não por impacto científico downstream. Papers que passam no automated review podem não ser citáveis ou reproducíveis por humanos.

**O que o paper NÃO diz:** Lu et al. não reportam taxa de ideias que falharam completamente (não chegaram a paper). ~50 ideias por template é o dado do README — não sabemos quantas foram descartadas no Estágio 1 vs. falharam no Estágio 2.

## Conexões

- adversarial-para: [[autoresearch-reliability-triad]] ON "AI Scientist satisfaz Pilar 1 (código como oracle) mas viola Pilares 2 e 3 (anti-cascade, stopping criterion) — failure modes documentados mapeiam para esses pilares"
- instanceOf: [[autonomous-research-agents]] ON "primeiro sistema end-to-end no corpus que fecha o loop hipótese→experimento→paper"
- instanceOf: [[self-improving-agents]] ON "Absolute Zero pattern: código como oracle externo — AI Scientist é implementação em escala de produção do mesmo princípio"
- contrasts: [[sequential-hypothesis-testing]] ON "AI Scientist usa timeout como stopping criterion — SPRT seria o substituto principled"

## Fontes

- [Lu et al. 2024 — AI Scientist](../../raw/papers/lu-2024-ai-scientist-autonomous-research.md) — pipeline, failure modes, métricas, safety constraints
