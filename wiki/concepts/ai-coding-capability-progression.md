---
title: "Progressão de Capacidades de Coding Autônomo em LLMs (SWE-bench 2023–2026)"
sources:
  - path: raw/reports/stanford-ai-index-2025-technical-performance.md
    type: report
    quality: secondary
    stance: neutral
  - path: raw/data/vellum-llm-leaderboard-2026-03-23.md
    type: dataset
    quality: secondary
    stance: neutral
  - path: raw/data/llm-stats-swe-bench-verified-2026-04-08.md
    type: dataset
    quality: secondary
    stance: neutral
created: 2026-04-08
updated: 2026-04-08
tags: [ai-capabilities, swe-bench, coding, benchmarks, velocity, labor-economics, frontier-models]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - raw/reports/stanford-ai-index-2025-technical-performance.md
  - raw/data/vellum-llm-leaderboard-2026-03-23.md
  - raw/data/llm-stats-swe-bench-verified-2026-04-08.md
quarantine: false
quarantine_promoted: 2026-04-08
quarantine_criteria_met:
  auto_promote: false
  promoted_after_corrections: true
  gates_passed: [1, 2, 3, 4]
  gate3_run: 2026-04-08
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  gate3_claims_challenged: 9
  gate3_claims_survived: 3
  gate3_claims_weakened: 3
  gate3_claims_invalidated: 3
  gate3_staleness_overrides: 1
  gate3_effective_invalidated: 2
  challenge_verdict: CORRIGIDO_PROMOVIDO
---

## Resumo

SWE-bench Verified mede resolução autônoma de GitHub issues reais. A progressão do state-of-the-art: 4.4% (2023) → 71.7% (2024, Stanford AI Index) → 80.8% (Claude Opus 4.6, mar/2026) → 93.9% (Claude Mythos Preview, abr/2026). Velocidade sem paralelo histórico em automação: a mesma trajectória levou décadas na robótica industrial. Em 2026-04-08, 80 modelos avaliados com score médio de 62.7% — progressão não restrita ao topo da fronteira.

## Conteúdo

### SWE-bench Verified — Definição e Metodologia

**O que mede:** capacidade de LLM de resolver GitHub issues reais de projetos open-source Python (Django, Flask, NumPy, scikit-learn, etc.) de forma autônoma.

**Pipeline de avaliação:**
1. Modelo recebe o issue textual + contexto do repositório
2. Gera patch de código
3. Patch é avaliado pela suite de testes automatizada do projeto
4. Score = % de issues corretamente resolvidos (testes passam)

**"Verified":** subconjunto validado manualmente por testadores humanos para garantir que soluções corretas são de fato corretas (elimina falsos positivos na suite de testes).

**Benchmark não-sintético:** ao contrário de HumanEval ou MBPP, SWE-bench usa bugs e features reais de produção, não exercícios criados para avaliação. Isso confere maior validade ecológica do que exercícios sintéticos — mas performance ainda é afetada por design de harness, quantidade de contexto de repositório fornecida, e qualidade da suite de testes de cada projeto.

---

### Progressão Temporal do State-of-the-Art

| Data | Score | Modelo/Contexto | Fonte |
|------|-------|-----------------|-------|
| 2023 | **4.4%** | Top performer do período | Stanford AI Index 2025 |
| 2024 (final) | **71.7%** | Top performer do período | Stanford AI Index 2025 |
| Mar/2026 | **80.8%** | Claude Opus 4.6 | Vellum Leaderboard (2026-03-23) |
| Abr/2026 | **93.9%** | Claude Mythos Preview | Anthropic System Card (2026-04-07) ¹ |

¹ Dado fornecido pelo usuário com base em leitura do System Card; não verificado diretamente no documento ingested (acesso parcial ao PDF).

**Velocidade de progressão:**
- 2023→2024: +67.3 pp em ~12 meses (~16x) — comparação entre top performers de cada ano; scaffolding potencialmente distinto; indicador direcional, não progressão de arquitetura única
- 2024→Mar/2026: +9.1 pp em ~16 meses (modelos publicamente disponíveis)
- 2024→Abr/2026: +22.2 pp em ~16 meses (incluindo Mythos Preview, modelo de acesso restrito)
- Trajetória completa (3 anos): de 4.4% a 80.8% (modelos disponíveis) / 93.9% (incluindo Mythos restrito)

---

### Distribuição de Campo (Além da Fronteira)

Dados llm-stats.com (2026-04-08, 80 modelos avaliados):

- **Score médio do campo:** 62.7%
- **Top performers:** Claude Opus 4.5 (80.9%), Claude Opus 4.6 (80.8%)
- **Cauda inferior:** GPT-4o mini (8.7%)
- **Observação:** a progressão não é apenas da fronteira — o campo inteiro avançou. Score médio de 62.7% em leaderboard selecionado não permite inferir que modelos de custo intermediário resolvem a maioria dos issues de coding no mundo real — SWE-bench cobre slice estreito de Python OSS com boas suites de testes; capacidade geral em código proprietário, sem testes, ou de baixa qualidade pode ser significativamente menor.

---

### Benchmarks Complementares (Vellum, 2026-03-23)

| Benchmark | Claude Opus 4.6 | Baseline humana |
|-----------|----------------|-----------------|
| GPQA Diamond | 91.3% | ~70% (especialistas) |
| AIME 2025 | 99.8% | ~2–5% (estudantes top) |
| SWE-bench Verified | 80.8% | n.d. |
| ARC-AGI 2 | 68.8% | ~98% |

**Nota:** GPQA Diamond supera especialistas humanos. AIME praticamente saturado. ARC-AGI 2 ainda abaixo de humanos — sugere raciocínio abstrato visual como área de limitação persistente.

---

### Saturação de Benchmarks e Dinâmica de Corrida

- Benchmarks clássicos (MMLU, HumanEval) já saturados por modelos de 2024
- SWE-bench Verified começa a ser saturado na fronteira (80–94%)
- Criação de benchmarks mais difíceis: ARC-AGI 2, BIG-Bench Hard, LiveCodeBench
- Padrão histórico: saturação → novo benchmark mais difícil → nova rodada de progresso

**Implicação metodológica:** scores absolutos de benchmarks têm vida útil limitada. Velocidade de progressão e generalização a tarefas não-benchmark são os indicadores mais duradouros.

---

### Comparação de Velocidade: Cognitiva vs. Robótica

(⚠️ nossa interpretação — síntese cross-domain)

| Tecnologia | Trajetória | Período |
|------------|-----------|---------|
| Robótica industrial (Brasil) | ~5.000 → ~10.000 unidades | 2008–2018 (10 anos, Stemmler 2022) |
| LLMs coding (SWE-bench) | 4.4% → 93.9% | 2023–2026 (~3 anos) |

A robótica industrial levou uma década para dobrar a penetração no Brasil — e mesmo assim com penetração baixa (<3% das firmas em 2018). LLMs foram de incipiente a quase-saturação no benchmark de coding em 3 anos.

**Por que isso importa para displacement:** modelos como Cazzaniga (IMF WP/24/116) assumem gradualidade suficiente para que trabalhadores transitem de HELC para HEHC ao longo da carreira. A comparação entre as trajetórias sugere que a automação cognitiva avança em benchmark muito mais rápido do que a penetração robótica industrial avançou no Brasil — porém as métricas são incomensuráveis (benchmark improvement ≠ diffusion speed real no mercado de trabalho). O argumento qualitativo permanece: se a velocidade de adoção em produção acompanhar mesmo parcialmente a velocidade de benchmark, a janela de transição pode ser insuficiente.

## Verificação Adversarial

**Claim mais fraco:** a comparação de velocidade cognitiva vs. robótica é análoga, não direta. SWE-bench mede performance em benchmark; adoção de ferramentas de coding AI em produção (GitHub Copilot enterprise, Cursor) ainda tem fricção de adoção, treinamento, e governança que desacelera o impacto real.

**O que os dados NÃO dizem:**
1. Não medem performance em código proprietário, sem testes, ou em repositórios de baixa qualidade — SWE-bench é Python open-source com boa cobertura de testes
2. Não distinguem entre "LLM resolve issue de forma autônoma" e "desenvolvedor usa LLM para resolver issue mais rápido" — o benchmark é o primeiro, o mundo real é mistura dos dois
3. Não documentam qual share de tasks de trabalho real corresponde ao tipo de issue avaliado em SWE-bench

**Simplificações:**
- "Saturação a 93.9%" é verdade para Claude Mythos Preview em condições controladas de benchmark; performance em ambientes reais de desenvolvimento pode ser 20–40 pp menor
- Vellum e llm-stats são leaderboards comerciais, não avaliações independentes — podem ter viés de seleção de modelos

**Prior work:**
- SWE-bench original: Jimenez et al. (2023) — paper de introdução do benchmark
- SWE-bench Verified: OpenAI/scale.ai validation subset
- Goldman Sachs (Briggs/Kodnani 2023): ~25% do trabalho global exposto a LLMs — metodologia diferente (análise de tarefas, não benchmark de performance)

## Interpretação

(⚠️ nossa interpretação — conexão ao debate de labor displacement)

A trajetória 4.4% → 93.9% em 3 anos é o argumento de velocidade ausente dos modelos de labor displacement. Cazzaniga (2024) e Brynjolfsson et al. (2025) pressupõem, implicitamente, que trabalhadores têm tempo para transitar entre zonas de exposição. Mas a velocidade de SWE-bench sugere que a janela de transição pode ser mais curta do que o tempo de experiência necessário para acumular conhecimento tácito (tipicamente 5–10 anos para ir de HELC para HEHC).

Isso cria o "duplo problema de velocidade":
1. LLMs substituem o trabalho de entrada (HELC) antes que jovens qualificados acumulem experiência
2. A velocidade de melhoria é rápida o suficiente para que trabalhadores em transição vejam o goalpost mover antes de chegar

Esta conexão é síntese — nenhum dos papers individuais faz esta ligação explicitamente.

## Conexões

## Fontes
- [Stanford AI Index 2025 — Technical Performance](../../raw/reports/stanford-ai-index-2025-technical-performance.md) — SWE-bench 4.4%→71.7%; aceleração de benchmarks; saturação de clássicos; acesso parcial
- [Vellum LLM Leaderboard (2026-03-23)](../../raw/data/vellum-llm-leaderboard-2026-03-23.md) — Claude Opus 4.6: 80.8% SWE-bench, 91.3% GPQA Diamond, 99.8% AIME 2025, 68.8% ARC-AGI 2
- [llm-stats.com SWE-bench Verified (2026-04-08)](../../raw/data/llm-stats-swe-bench-verified-2026-04-08.md) — 80 modelos; score médio 62.7%; distribuição de campo; progressão histórica

## Quality Gate
- [x] Wikilinks tipados: nenhum — Zone 3 (cross-domain; conexões emergem via /ask)
- [x] Instance→class: todos os scores qualificados com modelo, data e fonte específica
- [x] Meta-KB separado: conexões ao debate de labor displacement em Interpretação, não em Conteúdo
- [x] Resumo calibrado: source_quality:medium — 3 fontes secundárias (leaderboards + relatório anual); sem paper primary de benchmark; interpretation_confidence:medium — velocidade é síntese cross-domain
