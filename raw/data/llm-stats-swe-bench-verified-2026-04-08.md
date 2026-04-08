# llm-stats.com — SWE-bench Verified Leaderboard
**Source:** https://llm-stats.com/benchmarks/swe-bench-verified
**Captured:** 2026-04-08
**Type:** Live leaderboard agregado (agrega avaliações de múltiplos benchmarks públicos)

---

## Distribuição geral (2026-04-08)

- **Total de modelos avaliados:** 80
- **Score médio:** 62.7%
- **Score mínimo (GPT-4o mini):** 8.7%

## Top rankings

| Rank | Modelo | Score SWE-bench Verified |
|------|--------|--------------------------|
| 1 | Claude Opus 4.5 | 80.9% |
| 2 | Claude Opus 4.6 | 80.8% |

**Nota:** A diferença entre rank 1 e rank 2 (0.1 pp) é estatisticamente insignificante — dentro da margem de variação por prompt/run. Ambos são efetivamente empatados.

## Distribuição de scores

- Top quartil (Q4): ≥ ~70%
- Score médio: 62.7%
- Bottom quartil (Q1): ≤ ~40%
- Cauda inferior: GPT-4o mini 8.7%

A distribuição sugere consolidação do estado da arte entre ~70-80%, com cauda longa de modelos menores muito abaixo da fronteira.

---

## Contexto histórico (SWE-bench Verified — progressão temporal)

Dados de progressão fornecidos pelo usuário + Stanford AI Index 2025:

| Ano | Score SWE-bench Verified | Nota |
|-----|--------------------------|------|
| 2023 | 4.4% | Primeiros modelos avaliados (Stanford AI Index 2025) |
| 2024 | 71.7% | Top performer final de 2024 (Stanford AI Index 2025) |
| 2026-03 | 80.8% | Claude Opus 4.6 (Vellum, Anthropic) |
| 2026-04 | 93.9% | Claude Mythos Preview (Anthropic System Card) |

**Velocidade de progressão:** de 4.4% a 93.9% em ~3 anos. Para referência, a penetração de robótica industrial no Brasil passou de ~5.000 para ~10.000 unidades em uma década (2008–2018, Stemmler 2022).

---

## Notas metodológicas sobre SWE-bench Verified

- **Tarefa:** resolver GitHub issues reais de projetos open-source Python (Django, Flask, NumPy, etc.)
- **Verified:** subconjunto validado manualmente por testadores humanos para garantir soluções corretas são de fato corretas
- **Avaliação:** modelo recebe o issue + contexto do repositório; gera patch; patch é testado por suite de testes automatizada
- **Limitação estrutural:** performance pode variar por configuração de scaffolding (agente simples vs loop de reflexão); scores não são diretamente comparáveis entre avaliações com arquiteturas diferentes
- **Limitação de generalização:** GitHub issues = código aberto, Python-heavy, projetos com boas suites de testes. Performance em código proprietário / sem testes pode diferir.

---

## Fonte

llm-stats.com é agregador independente. Não é paper peer-reviewed. Cross-check com relatórios dos desenvolvedores e Epoch AI recomendado para uso em argumentos sobre capacidades.
