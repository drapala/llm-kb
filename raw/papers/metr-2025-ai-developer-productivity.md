# Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity

**Autores:** METR (Model Evaluation & Threat Research)  
**Publicação:** arXiv:2507.09089; METR Blog  
**Ano:** 2025 (publicado julho 2025)  
**URL:** https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/  
**Tipo:** paper / primary (RCT)

---

## Metodologia

**Desenho:** Randomized Controlled Trial (within-subject)
- **16 desenvolvedores experientes** de projetos open-source grandes
- Repositórios: média de 22k+ stars, 1M+ linhas de código, contribuidores de múltiplos anos
- **246 tarefas reais** de issues reais dos repos (bug fixes, features, refactors)
- Cada issue randomicamente atribuída a condição: **AI permitido** vs. **AI proibido**
- Condição AI: qualquer ferramenta escolhida pelo dev (predominantemente Cursor Pro + Claude 3.5/3.7 Sonnet)
- Tempo reportado pelo próprio desenvolvedor; screens gravadas

## Achados principais

### O paradoxo
| Métrica | Valor |
|---------|-------|
| Previsão dos devs (antes): redução de tempo com AI | -24% (mais rápido) |
| Estimativa dos devs (depois): redução de tempo com AI | -20% (mais rápido) |
| **Resultado real medido** | **+19% mais lento com AI** |
| Gap percepção vs. realidade | **39 pontos percentuais** |

Desenvolvedores sentiram que eram mais rápidos. Eram mais lentos.

### Contexto crítico: os repos eram codebases maduras e complexas
O efeito negativo foi documentado em codebases com ≥1M linhas e colaboradores experientes — não em projetos verdes ou tarefas isoladas.

## Atualização de fevereiro 2026 (METR)

METR publicou atualização do design experimental após descobrir que **30–50% dos desenvolvedores convidados recusaram participar** sem acesso a AI. Novo cohort:
- 800+ tarefas, 57 desenvolvedores
- Resultado: **-4% slowdown** (CI: -15% a +9%)
- Conclusão revisada de METR: "AI provavelmente provê benefícios de produtividade em early 2026"

## Interpretação

O resultado de -19% não é universalmente generalizável:
1. Contexto específico: codebases maduras e complexas onde AI tem mais dificuldade com contexto
2. Ferramentas usadas eram frontier de meados 2025 (Claude 3.5/3.7) — não agentic AI
3. O update de 2026 com cohort maior sugere que o efeito pode ser menor ou positivo com ferramentas mais recentes

O dado mais robusto do estudo é o **gap de 39 pontos entre percepção e realidade** — independente do sinal do efeito real.

## Relevância para comprehension debt

O paradoxo percepção/realidade do METR é um mecanismo de entrada para comprehension debt: desenvolvedores que se sentem mais produtivos com AI têm menos incentivo a questionar o que realmente entenderam.
