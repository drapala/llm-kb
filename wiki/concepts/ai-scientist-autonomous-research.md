---
title: "AI Scientist — Fully Automated Scientific Discovery"
sources:
  - path: raw/papers/lu-2024-ai-scientist-autonomous-research.md
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/chen-2026-aiscientist-long-horizon-ml-engineering.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-04
updated: 2026-04-14
tags: [autoresearch, autonomous-agents, scientific-discovery, failure-modes, multi-agent]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
reads: 1
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-14
quarantine: false
provenance: source
---

## Resumo

Dois papers progressivos. **Lu et al. (2024)**: primeiro sistema end-to-end de descoberta científica (hipótese→experimento→paper), custo <$15/paper, failure modes mapeados para os três pilares do [[autoresearch-reliability-triad]]. **Chen et al. (2026)**: AiScientist, sistema de ML research engineering de longa duração, adiciona File-as-Bus workspace (thin control over thick state): PaperBench 33.73 (+11.15 pts sobre melhor baseline), MLE-Bench Lite 81.82% Any Medal%. Ablação: remover File-as-Bus custa −31.82 Any Medal%.

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

## AiScientist 2026 — Chen et al.

### Distinção em relação a Lu 2024

Lu et al. (2024) opera em modo ideação: gera hipóteses novas, testa em domínios templateados (NanoGPT, Grokking), escreve paper novo.  
Chen et al. (2026) opera em modo replicação/otimização: dado um paper existente, reproduz seus resultados from-scratch num ambiente Docker, ou otimiza uma solução ML em tarefa de competição.

O setting de Chen 2026 é mais exigente em continuidade de estado: múltiplas rodadas de implement→run→debug ao longo de 24h, onde decisões de implementação em round 3 dependem de logs de falha de round 1.

### File-as-Bus — mecanismo central

Ver [[file-as-bus-workspace]] para descrição completa do protocolo.

Resumo: agentes coordenam via artefatos em disco (não handoffs conversacionais). Orchestrator mantém workspace map compacto. Especialistas re-ancoram no workspace atual a cada invocação — contexto privado é re-inicializado, continuidade é pelo workspace.

### Resultados Chen 2026

| Benchmark | AiScientist | Melhor baseline | Δ |
|-----------|------------|----------------|---|
| PaperBench avg | 33.73 | 22.37 (IterAgent GLM-5) | +11.15 |
| MLE-Bench Lite Any Medal% | 81.82% | 77.27% (LoongFlow) | +4.55 |
| Custo/tarefa | $12.20 | $54.90 (IterAgent) | −$42.70 |

**Ablação File-as-Bus:** −6.41 PaperBench, −31.82 MLE-Bench Lite Any Medal%. Perda concentrada em refinamento tardio (Silver/Gold/Any Medal), não em setup inicial.

### Stopping Criterion em Chen 2026

Time budget de 24h por tarefa. Não usa SPRT nem critério de convergência baseado em evidência — mesma limitação de Lu 2024. O loop evidência-driven (diagnose → patch) é adaptativo mas sem stopping principled. Timeout permanece o único critério explícito.

## Conexões

- adversarial-para: [[autoresearch-reliability-triad]] ON "AI Scientist (Lu 2024) satisfaz Pilar 1 mas viola Pilares 2 e 3; AiScientist (Chen 2026) fortalece Pilar 1 via File-as-Bus mas mantém timeout como único stopping criterion"
- instanceOf: [[autonomous-research-agents]] ON "primeiro sistema end-to-end (Lu 2024); primeiro com durable state continuity em escala (Chen 2026)"
- instanceOf: [[self-improving-agents]] ON "código como oracle externo — AI Scientist é implementação em escala de produção do mesmo princípio"
- contrasts: [[sequential-hypothesis-testing]] ON "AI Scientist usa timeout como stopping criterion — SPRT seria o substituto principled"
- partOf: [[file-as-bus-workspace]] ON "AiScientist 2026 é o sistema que instancia o protocolo File-as-Bus"

## Fontes

- [Lu et al. 2024 — AI Scientist](../../raw/papers/lu-2024-ai-scientist-autonomous-research.md) — pipeline, failure modes, métricas, safety constraints
- [Chen et al. 2026 — AiScientist](../../raw/papers/chen-2026-aiscientist-long-horizon-ml-engineering.md) — File-as-Bus, hierarquia, benchmarks PaperBench/MLE-Bench, ablações
