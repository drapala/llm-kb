# Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild

**Autores:** Liu et al.  
**Publicação:** arXiv:2603.28592  
**Ano:** Março 2026  
**URL:** https://arxiv.org/abs/2603.28592  
**Tipo:** paper / primary (estudo empírico de larga escala)

---

## Metodologia

- **304.362 commits** verificados como AI-authored
- **6.275 repositórios** GitHub
- **5 AI coding assistants:** GitHub Copilot, Claude, Cursor, Gemini, Devin
- Identificação: commits marcados como gerados por AI (atribuição explícita nos commits)
- Análise estática antes e depois de cada commit para atribuir quais issues o AI introduziu
- Rastreamento longitudinal: cada issue seguida desde o commit introdutor até o HEAD atual do repositório

## Achados quantitativos principais

### Distribuição de tipos de issue (484.606 issues identificadas)
| Tipo | % do total | N |
|------|-----------|---|
| Code smells | 89.1% | ~431.000 |
| Runtime bugs | 5.8% | 28.149 |
| Security issues | 5.1% | 24.607 |

### Taxa de introdução por ferramenta (% de commits com ≥1 issue)
| Tool | Taxa de commits com issue |
|------|--------------------------|
| GitHub Copilot | 17.3% (mínimo) |
| Claude | entre 17–28% |
| Cursor | ~27.6% |
| Gemini | 28.7% (máximo) |
| Devin | entre 17–28% |

Threshold: **>15% de commits de toda ferramenta** introduz ao menos uma issue.

### Persistência (survival rates)
| Tipo | Survival rate |
|------|--------------|
| Overall | **24.2%** — ainda presente no HEAD |
| Security issues | **41.1%** — resolução muito menor |
| Code smells | 22.7% |

Security issues sobrevivem desproporcionalmente — desenvolvedores remediam code smells antes que vulnerabilidades de segurança.

### Crescimento de dívida não resolvida
- Início de 2025: poucas centenas de issues sobreviventes
- Fevereiro 2026: **>110.000 issues surviving**
- Trajetória: crescimento acelerado acompanhou adoção massiva de AI coding tools em 2025

### Top code smell patterns
1. Broad exception handling — 41.723 instâncias
2. Unused variables/parameters — 28.718 instâncias
3. Shadowed outer variables — 20.251 instâncias
4. Access to protected members — 19.835 instâncias

## Conclusão

AI-generated code introduz technical debt de longo prazo em projetos reais. O volume de debt não-resolvido cresce rapidamente com adoção. Security issues são as mais persistentes. A necessidade de quality assurance mais forte em AI-assisted development é evidenciada pelos dados.
