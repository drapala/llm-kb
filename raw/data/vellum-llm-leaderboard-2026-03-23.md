# Vellum LLM Leaderboard
**Source:** https://www.vellum.ai/llm-leaderboard
**Last updated:** March 23, 2026
**Captured:** 2026-04-08
**Type:** Live benchmark tracking (não peer-reviewed — dados de leaderboard atualizado continuamente)

---

## Benchmarks selecionados — Top performers (2026-03-23)

### SWE-bench Verified (resolução autônoma de issues de software)

| Rank | Modelo | Score |
|------|--------|-------|
| 1 | Claude Opus 4.6 | 80.8% |
| 2 | GPT-4.1 | ~72% (referência histórica) |

**Nota metodológica:** SWE-bench Verified é subconjunto validado manualmente de SWE-bench; mede resolução autônoma de GitHub issues reais de projetos open-source Python.

### GPQA Diamond (raciocínio científico avançado — PhD-level)

| Rank | Modelo | Score |
|------|--------|-------|
| 1 | Claude Opus 4.6 | 91.3% |

**Nota:** GPQA = Graduate-Level Google-Proof Q&A. Diamond = subconjunto mais difícil. Baseline humana especialista ~70%.

### AIME 2025 (American Invitational Mathematics Examination)

| Rank | Modelo | Score |
|------|--------|-------|
| 1 | Claude Opus 4.6 | 99.8% |

**Nota:** AIME é competição de matemática de nível pré-universitário avançado. 99.8% equivale a praticamente perfeito.

### ARC-AGI 2 (raciocínio abstrato — novo benchmark mais difícil)

| Rank | Modelo | Score |
|------|--------|-------|
| 1 | Claude Opus 4.6 | 68.8% |

**Nota:** ARC-AGI 2 é versão revisada e significativamente mais difícil do ARC-AGI original. Baseline humana ~98%.

---

## Contexto de uso

Leaderboard mantido pela Vellum (empresa de LLM tooling). Dados atualizados continuamente — não é snapshot de paper. Modelos são avaliados com variações de prompt (temperatura, few-shot) que podem diferir de avaliações oficiais dos desenvolvedores.

**Limitação:** Vellum pode ter incentivo comercial para apresentar modelos de forma favorável. Cross-check com avaliações oficiais dos desenvolvedores e benchmarks independentes (Epoch AI, Scale AI HELM) é recomendado.
