# On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents

**Autores:** Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude  
**Publicação:** arXiv  
**arXiv ID:** 2601.20404  
**Ano:** 2026 (submissão: 28 jan 2026; revisado: 30 mar 2026)  
**URL:** https://arxiv.org/abs/2601.20404  
**Tipo:** paper / primary

---

## Tese central

AGENTS.md — arquivo de configuração de nível de repositório para coding agents como Codex e Claude Code — reduz tempo de execução e consumo de tokens sem comprometer taxa de conclusão de tarefas.

## Metodologia

- 10 repositórios
- 124 pull requests
- Condições: com e sem AGENTS.md
- Métricas: wall-clock runtime, output token consumption, task completion rate

## Resultados

| Métrica | Efeito com AGENTS.md |
|---------|---------------------|
| Runtime | **-28.64%** (mediana) |
| Output tokens | **-16.58%** |
| Task completion | Comparável (não degradou) |

## Mecanismo

AGENTS.md fornece instruções a nível de repositório — convenções, comandos de build, padrões do projeto. O agente usa esse contexto para evitar exploração desnecessária do codebase, o que reduz tanto o tempo quanto os tokens consumidos.

## Limitações

- Apenas 10 repositórios e 124 PRs — amostra pequena
- Paper de 5 páginas — contribuição preliminar
- Não decompõe quais seções do AGENTS.md têm maior impacto
- Não separa efeito de redução de exploração vs. redução de erros

## Relação com outras fontes

Contrasta com Gloaguen et al. (2602.11988 — ETH Zürich): este paper encontra ganho de eficiência, enquanto o ETH encontra redução de taxa de sucesso. A diferença pode ser de métrica (eficiência vs. sucesso) ou de qualidade/tamanho do AGENTS.md analisado.
