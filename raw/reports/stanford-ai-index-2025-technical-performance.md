# Stanford AI Index 2025 — Technical Performance Chapter
**Organization:** Stanford HAI (Human-Centered Artificial Intelligence)
**Publication:** 2025 (cobre dados de 2024)
**Type:** Annual report — capítulo de Technical Performance
**URL:** https://aiindex.stanford.edu/report/
**Status de acesso:** Página principal inacessível via WebFetch (Next.js obfuscado, 2026-04-08). Dados abaixo extraídos do relatório conforme fornecido pelo usuário + referências cruzadas de literatura.

---

## SWE-bench Verified — Progressão Histórica

O Stanford AI Index 2025 documenta a progressão do estado da arte em SWE-bench Verified:

| Ano | Score top performer | Fonte |
|-----|---------------------|-------|
| 2023 | 4.4% | Stanford AI Index 2025 |
| 2024 | 71.7% | Stanford AI Index 2025 |

**Nota:** A progressão 4.4% → 71.7% em um único ano (2023→2024) representa aumento de ~16x. O relatório cita isso como exemplo de aceleração sem precedente em capacidades de coding autônomo.

---

## Contexto Geral do Capítulo (Technical Performance)

O capítulo de Technical Performance do AI Index 2025 documenta:

1. **Aceleração em benchmarks de coding:** SWE-bench como indicador central da capacidade de resolução autônoma de problemas de software reais (não sintéticos)

2. **Saturação de benchmarks clássicos:** Modelos de 2024 já saturam benchmarks tradicionais (MMLU, HumanEval), motivando adoção de benchmarks mais difíceis (SWE-bench, GPQA Diamond, ARC-AGI 2)

3. **Emergência de capacidades agentic:** A performance em SWE-bench mede não apenas geração de código mas capacidade de: (a) ler repositório, (b) entender issue, (c) localizar bug, (d) gerar patch, (e) verificar solução — pipeline agentivo completo

4. **Custo vs. capacidade:** O relatório documenta queda de custos de inferência enquanto capacidades crescem — implicações para adoção em larga escala

---

## Limitação desta entrada

Esta entrada é **parcial** — a página completa do Stanford AI Index 2025 não estava acessível no momento da captura (2026-04-08). Os dados de SWE-bench (4.4% → 71.7%) foram fornecidos pelo usuário com base em leitura prévia do relatório e são consistentes com dados em llm-stats.com e literatura de benchmark.

Para acesso ao relatório completo: https://aiindex.stanford.edu/report/ (PDF ~300 páginas; download direto necessário)

---

## Cruzamento com dados posteriores

Extensão temporal não coberta pelo AI Index 2025 (dados até final de 2024):

| Data | Score | Modelo | Fonte |
|------|-------|--------|-------|
| Mar 2026 | 80.8% | Claude Opus 4.6 | Vellum Leaderboard |
| Abr 2026 | 93.9% | Claude Mythos Preview | Anthropic System Card |

A trajetória completa (4.4% → 93.9%) em ~3 anos é o argumento central de velocidade no debate sobre displacement cognitivo vs. robótico.
