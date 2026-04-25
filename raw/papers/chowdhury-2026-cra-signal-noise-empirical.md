# From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests

**Autores:** Kowshik Chowdhury, Dipayan Banik, K M Ferdous, Shazibul Islam Shamim
**Instituição:** Kennesaw State University + Quanta Technology
**Publicação:** arXiv:2604.03196 [cs.SE] — MSR 2026
**Ano:** 2026 (abril)
**URL:** https://arxiv.org/abs/2604.03196
**Tipo:** paper / primary

---

## Metodologia

- Dataset AIDev: **19.450 PRs** no HuggingFace
- **3.109 PRs únicos** com review activity analisados
- Comparação: human-only vs CRA-only vs mixed reviews
- Análise de **98 PRs fechados CRA-only** (abandonados)
- Signal-to-noise framework via two-tier keyword classification
  - Tier 1 (Critical Signal): runtime errors, crashes, security vulnerabilities, API-breaking changes
  - Tier 2 (Important Signal): architectural problems, performance, maintainability
  - Cohen's Kappa = 0.75 para validação inter-rater

## Achados principais

### Merge rates por tipo de reviewer

| Reviewer Type | Total | Merge Rate | Abandonment |
|--------------|-------|------------|-------------|
| CRA-only | 281 | **45.20%** | **34.88%** |
| Mixed(CRA) | 117 | 63.25% | 14.53% |
| Mixed | 604 | 61.09% | 21.19% |
| Mixed(Human) | 278 | 67.99% | 14.75% |
| Human-only | 1.176 | **68.37%** | 21.60% |

Gap: CRA-only 23.17 pontos percentuais abaixo de human-only. χ²=83.03, p<0.001.

### Signal-to-noise ratio nos PRs abandonados (CRA-only)

| Faixa de signal ratio | PRs (%) | Descrição |
|----------------------|---------|-----------|
| 0-30% | **60.2%** | Predominantemente ruído |
| 31-59% | 14.3% | Mais ruído que sinal |
| 60-79% | 7.1% | Mais sinal que ruído |
| 80-100% | 18.4% | Alta qualidade |

**12 de 13 CRAs (92.31%) têm signal ratio médio abaixo de 60%.**

Copilot: 19.79% signal ratio (pior entre os grandes). GitHub Advanced Security: 27.62%.
Único CRA com 100% signal ratio (semgrep-code-getsentry[bot]) revisou apenas 1 PR.

### Relação entre qualidade e volume de comentários

PRs com high signal (≥0.80) concentram-se em 1-3 comentários — feedback conciso de alta qualidade. PRs com low signal (<0.30) espalhados em 1-8 comentários — volume não prediz qualidade.

## Contraste com claims industriais

| Claim | Fonte | Evidência empírica |
|-------|-------|--------------------|
| "80% dos PRs não precisam de comentários humanos com CRA" | Qodo 2025 | CRA-only merge rate: 45.2% vs human 68.4% |
| "82% de devs usam CRA diariamente" | Greptile | — |

## Implicações práticas

- CRAs devem ser configurados para verificações **específicas e narrow** (security, style) em vez de review geral
- Especialização reduz falsos positivos (semgrep-specific vs genérico)
- Human approval antes do merge permanece necessário
- CRA comments devem **trigger** human review, não substituir

## Ligação com outros papers

- Confirma e quantifica o que Zhong 2026 documentou sobre baixa adoção de sugestões AI
- O signal/noise framework é complementar ao Outdated Rate de BitsAI-CR como métrica de qualidade
- Contraria claims industriais com dados empíricos sólidos (MSR 2026)
