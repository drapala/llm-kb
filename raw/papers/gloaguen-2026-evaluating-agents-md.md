# Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

**Autores:** Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev  
**Publicação:** arXiv  
**arXiv ID:** 2602.11988  
**Ano:** 2026 (submissão: 12 fev 2026)  
**URL:** https://arxiv.org/abs/2602.11988  
**Tipo:** paper / primary (⚠️ challenging — contradiz narrativa de que context files são sempre benéficos)

---

## Tese central

Context files (AGENTS.md e similares) reduzem taxa de sucesso de agentes de coding quando comparados à ausência de contexto de repositório. Ambos os tipos — gerado por LLM e escrito por humano — tendem a piorar performance. A prática é "fortemente encorajada por developers de agents" mas sem validação empírica.

## Metodologia

- Dois settings: SWE-bench tasks com AGENTS.md LLM-generated, e issues reais de repositórios com AGENTS.md human-committed
- Múltiplos coding agents e LLMs avaliados
- Métricas: task success rate, inference cost, agent behavior (exploration patterns)

## Resultados

| Resultado | Valor |
|-----------|-------|
| AGENTS.md LLM-generated | Reduz taxa de sucesso vs. sem contexto |
| AGENTS.md human-written | Também tende a reduzir (efeito menor) |
| Inference cost | **+20%** com context files |
| Agent behavior | Mais exploração (mais testing e file traversal) |

## Mecanismo identificado

Agentes respeitam as instruções do context file — mas instruções desnecessárias ou excessivamente especificadas tornam as tarefas mais difíceis. O problema não é que o agente ignora o contexto; é que contexto mal especificado gera overhead sem benefício.

**Recomendação central:** human-written context files devem "descrever apenas requisitos mínimos", não documentação abrangente.

## Limitações

- Dois settings distintos — generalização limitada
- "Human-written" inclui contexto comprometido por developers mas não necessariamente de alta qualidade

## Relação com outras fontes

Contradiz Lulla et al. (2601.20404) em termos de task success (enquanto Lulla encontra eficiência, ETH Zürich encontra menos sucesso). Complementa Agent READMEs (2511.12884): o gap de non-functional requirements (14.5%) pode explicar por que mesmo context files humanos frequentemente não ajudam.

## Implicação de design

Menos é mais: context file deve conter constraints mínimas obrigatórias, não tudo que o agente "deveria saber." O overhead de +20% de inference cost por contexto mal calibrado é mensurável.
