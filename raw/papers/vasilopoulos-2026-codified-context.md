# Codified Context: Infrastructure for AI Agents in a Complex Codebase

**Autor:** Aristidis Vasilopoulos  
**Publicação:** arXiv  
**arXiv ID:** 2602.20478  
**Ano:** 2026 (submissão: fevereiro 2026)  
**URL:** https://arxiv.org/abs/2602.20478  
**DOI:** https://doi.org/10.48550/arXiv.2602.20478  
**Repositório:** https://github.com/arisvas4/codified-context-infrastructure  
**Tipo:** paper / primary  
**Área:** Software Engineering (cs.SE)  
**Licença:** CC BY 4.0

---

## Problema

LLMs como coding assistants perdem coerência entre sessões: esquecem convenções do projeto, repetem erros conhecidos, e não mantêm estado de decisões arquiteturais anteriores. Em codebases grandes (100K+ LOC), isso é especialmente custoso — o contexto que um desenvolvedor humano mantém implicitamente precisou ser recriado a cada sessão.

## A Infraestrutura de Contexto Codificado

O autor construiu esta infraestrutura enquanto desenvolvia um sistema distribuído em C# de 108.000 linhas ao longo de 283 sessões de desenvolvimento.

### Componente 1: Constituição (Hot Memory)

Documento dinâmico que encoda:
- **Convenções do projeto** — padrões de nomenclatura, estrutura de módulos, convenções de API
- **Retrieval hooks** — ponteiros para onde encontrar informação relevante por tipo de tarefa
- **Protocolos de orquestração** — como os agentes devem coordenar entre si

A constituição é "hot" — sempre carregada no contexto, atualizada frequentemente.

### Componente 2: Workforce de 19 Agentes Especializados

19 agentes com domínios específicos de expertise, distribuídos por tipo de tarefa de desenvolvimento. Cada agente tem:
- Escopo de responsabilidade bem definido
- Acesso seletivo à knowledge base
- Protocolos de handoff para outros agentes

### Componente 3: Knowledge Base de 34 Documentos de Especificação (Cold Memory)

34 documentos de especificação on-demand:
- Carregados apenas quando relevantes para a tarefa atual
- Cobrem arquitetura, decisões de design, APIs internas, e padrões do projeto
- "Cold" — não carregados por padrão, acessados via retrieval hooks da constituição

## Validação

**Escala:** 108.000 linhas de C#, sistema distribuído real.  
**Duração:** 283 sessões de desenvolvimento documentadas.  
**Método:** métricas quantitativas sobre crescimento da infraestrutura + 4 case studies observacionais.

Os case studies demonstram como o contexto codificado previne falhas específicas e mantém consistência entre sessões. Não há grupo controle — comparação implícita com ausência da infraestrutura.

## Conceitos-Chave

**Codified context:** o ato de tornar explícito e persistente o contexto que seria implícito no conhecimento de um desenvolvedor humano sênior — e fazer esse contexto acessível a agentes AI.

**Hot vs. Cold memory:** distinção operacional entre contexto sempre presente (constituição) e contexto on-demand (knowledge base). Análogo a memória de trabalho vs. memória de longo prazo.

**Infrastructure growth:** o sistema não foi projetado de uma vez — cresceu organicamente ao longo das sessões, com documentos adicionados conforme novos padrões emergiam.

## Limitações

- Caso único (N=1 projeto, 1 desenvolvedor) — sem generalização formal
- Linguagem específica (C#) e domínio específico (sistema distribuído) — transferência para outros contextos não avaliada
- Sem comparação controlada com ausência da infraestrutura
- Custo de manutenção da infraestrutura não quantificado
