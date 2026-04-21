# On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub

**Autores:** Miku Watanabe et al.  
**Publicação:** arXiv:2509.14745  
**Ano:** 2025 (atualizado fevereiro 2026)  
**URL:** https://arxiv.org/abs/2509.14745  
**Tipo:** paper / primary

---

## Metodologia

- **567 pull requests** identificados como gerados por Claude Code no GitHub
- **157 projetos open-source** diversos
- Análise de: taxa de merge, modificações requeridas antes do merge, distribuição de tipos de tarefa

## Achados principais

### Taxa de aceitação
| Métrica | Valor |
|---------|-------|
| PRs aceitos e mergeados | **83.8%** |
| PRs mergeados sem modificação adicional | **54.9%** dos mergeados |
| PRs mergeados após revisão humana | **45.1%** dos mergeados |

### Distribuição de tarefas
Desenvolvedores usam Claude Code predominantemente para:
1. **Refactoring** — reorganização de código existente
2. **Documentation** — geração e atualização de docs
3. **Testing** — escrita de testes

### Onde a supervisão humana é mais necessária
- Bug fixes — agente não capta contexto de comportamento esperado
- Documentação — não segue padrões específicos do projeto
- Aderência a padrões do projeto — julgamento arquitetural local

## Interpretação dos dados

Alta taxa de merge (83.8%) pode refletir:
(a) qualidade genuína dos PRs do Claude Code, OU
(b) seleção de tarefas — desenvolvedores usam o agente para tarefas onde sabem que o resultado será adequado

O fato de que 45.1% dos mergeados requererem revisão humana sugere que o agente produz código funcionalmente correto mas frequentemente sem aderência a padrões locais do projeto.

## Limitações

- Amostra limitada a 567 PRs com atribuição explícita a Claude Code
- Claude Code foi lançado em fevereiro 2025 — dataset estreito
- Projetos que usam Claude Code podem não ser representativos de projetos típicos
