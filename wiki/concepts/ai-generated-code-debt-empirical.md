---
title: "AI-Generated Code Technical Debt — Empirical Evidence"
sources:
  - path: raw/papers/liu-2026-debt-behind-ai-boom.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/articles/ox-security-2025-army-of-juniors.md
    type: article
    quality: primary
    stance: confirming
  - path: raw/papers/mujahid-2026-todo-fix-gemini.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/huang-2026-more-code-less-reuse.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/watanabe-2025-agentic-coding-prs.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-11
updated: 2026-04-11
tags: [technical-debt, ai-generated-code, code-quality, empirical, security, code-smells]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
status: promoted
promoted_date: 2026-04-11
freshness_status: current
synthesis_sources:
  - raw/papers/liu-2026-debt-behind-ai-boom.md
  - raw/articles/ox-security-2025-army-of-juniors.md
  - raw/papers/mujahid-2026-todo-fix-gemini.md
  - raw/papers/huang-2026-more-code-less-reuse.md
  - raw/papers/watanabe-2025-agentic-coding-prs.md
---

## Resumo
Cinco estudos empíricos (2025–2026) convergem: AI coding assistants introduzem technical debt mensurável em código de produção. Liu et al. (2026) documentou 484K issues em 304K commits de 5 ferramentas — 24.2% ainda presentes no HEAD dos repositórios, com security issues sobrevivendo a 41.1%. Mujahid et al. (2026) identificou o padrão GIST: desenvolvedores explicitamente admitem dívida em comentários ligados a AI. Huang et al. (2026) documentou que AI agents produzem Type-4 clones — duplicação semântica invisível a ferramentas tradicionais. Watanabe et al. (2025) mostrou que 45.1% dos PRs de Claude Code requerem revisão humana substancial.

## Conteúdo

### Escala e persistência da dívida (Liu et al. 2026)

Dataset: 304.362 commits verificados como AI-authored, 6.275 repos, 5 ferramentas (Copilot, Claude, Cursor, Gemini, Devin).

**Distribuição de tipos de issue (484.606 total):**
| Tipo | % | N |
|------|---|---|
| Code smells | 89.1% | ~431K |
| Runtime bugs | 5.8% | 28.149 |
| Security issues | 5.1% | 24.607 |

**Taxa de introdução por ferramenta (commits com ≥1 issue):**
| Tool | Taxa |
|------|------|
| GitHub Copilot | 17.3% (mínimo) |
| Cursor | ~27.6% |
| Gemini | 28.7% (máximo) |

No dataset estudado (5 ferramentas, 6.275 repos): >15% de commits de **toda** ferramenta introduz ao menos uma issue — resultado do estudo, não generalização universal.

**Survival rates (persistência no HEAD):**
| Tipo | Survival |
|------|---------|
| Overall | **24.2%** |
| Security issues | **41.1%** — maior taxa de persistência no dataset (possivelmente mais difíceis de corrigir ou menos visíveis) |
| Code smells | 22.7% |

**Trajetória de crescimento:** de centenas de issues surviving no início de 2025 para >110.000 em fevereiro 2026 — dívida acumulando com a adoção.

**Top patterns de code smell:**
1. Broad exception handling (41.723)
2. Unused variables/parameters (28.718)
3. Shadowed outer variables (20.251)

### Dívida auto-admitida ligada a AI: GIST (Mujahid et al. 2026)

De 6.540 comentários de código que referenciam LLMs em repos Python/JS (nov 2022–jul 2025): **81 (1.24%)** admitem dívida explicitamente — denominados GIST (GenAI-Induced Self-Admitted Technical Debt).

**Três padrões:**
1. **Postponed Testing** — testes adiados de código AI-gerado
2. **Incomplete Adaptation** — código gerado não adaptado ao contexto específico
3. **Limited Understanding** — desenvolvedor admite não entender o código AI produziu

O dado de 1.24% é lower bound — captura apenas dívida explicitamente admitida em comentários.

### Duplicação semântica: Type-4 clones (Huang et al. 2026)

No estudo de Huang et al., AI agents geraram predominantemente **Type-4 clones**: código semanticamente redundante com variações textuais — em contraste com clones Type-1/2 (textuais), que eram menos frequentes neste contexto. Métricas tradicionais (LOC, complexidade ciclomática) não capturam redundância semântica.

Novo métrico proposto: **Max Redundancy Score (MRS)** — mede redundância semântica.

Reviewers de PR percebem negativamente o excesso de código sem reuso — correlação entre MRS alto e sentimento negativo em code reviews.

### Qualidade de PRs agentic (Watanabe et al. 2025)

567 PRs de Claude Code em 157 projetos open-source:
| Resultado | %|
|-----------|--|
| Mergeados | **83.8%** |
| Mergeados sem modificação | **54.9%** dos mergeados |
| Mergeados após revisão humana | **45.1%** dos mergeados |

Supervisão mais necessária em: bug fixes, documentação, aderência a padrões locais de projeto.

### Os 10 anti-patterns de AI code (Ox Security 2025)

Análise qualitativa de 300+ repos:
1. Comentários excessivos (ruído, não sinal)
2. Retorno de monolitos (ignora arquitetura modular existente)
3. Ausência de reuso (duplicação em vez de reutilização)
4. Tratamento de erro genérico (não adaptado ao sistema)
5. Hardcoding de valores
6. Dependências desnecessárias
7. Over-engineering de soluções simples
8. Violação de convenções do projeto
9. Ausência de edge cases
10. Acoplamento excessivo

Achado central (Ox Security, análise qualitativa): AI code não teria mais vulnerabilidades por linha — o problema é "insecure by dumbness": sistemas vulneráveis chegam à produção com velocidade que code review não consegue acompanhar. (⚠️ afirmação baseada em análise qualitativa de repos; literatura sobre densidade de vulnerabilidades por linha ainda é heterogênea.)

## Verificação adversarial

**Claim mais fraco:** a survival rate de 24.2% (Liu) pode refletir que issues sobrevivem porque são irrelevantes para os maintainers, não necessariamente porque são "dívida" no sentido de custo futuro.

**O que os papers não dizem:** (1) Liu não demonstra que issues AI-introduzidas causam mais bugs em produção que issues humanas; (2) Watanabe não compara a 83.8% de merge rate de PRs humanos no mesmo contexto; (3) Ox Security não quantifica severidade individual dos anti-patterns.

**Simplificações:** os 5 estudos medem proxies de qualidade (issues estáticas, merge rates, comentários) — não medem o que realmente importa: custo de manutenção a longo prazo.

## Quality Gate
- [x] Wikilinks tipados: sem wikilinks externos necessários neste artigo
- [x] Instance→class: todos os números qualificados com fonte, N da amostra, e ferramenta específica
- [x] Meta-KB separado: nenhuma referência a design da KB
- [x] Resumo calibrado: inclui que survival rate pode não implicar custo futuro

## Conexões
- ai-technical-debt-taxonomy partOf ai-generated-code-debt-empirical (framework conceitual para interpretar estes dados)
- ai-productivity-paradox derivedFrom ai-generated-code-debt-empirical (a velocidade que gera debt é o mesmo mecanismo que cria a ilusão de produtividade)

## Fontes
- [Liu et al. 2026](../../raw/papers/liu-2026-debt-behind-ai-boom.md) — 304K commits, 5 tools, survival rates, growth trajectory
- [Ox Security 2025](../../raw/articles/ox-security-2025-army-of-juniors.md) — 300 repos, 10 anti-patterns, "insecure by dumbness"
- [Mujahid et al. 2026](../../raw/papers/mujahid-2026-todo-fix-gemini.md) — GIST concept, 81/6540 comments, 3 debt patterns
- [Huang et al. 2026](../../raw/papers/huang-2026-more-code-less-reuse.md) — Type-4 clones, Max Redundancy Score, reviewer sentiment
- [Watanabe et al. 2025](../../raw/papers/watanabe-2025-agentic-coding-prs.md) — 567 Claude Code PRs, 83.8% merge rate, task distribution
