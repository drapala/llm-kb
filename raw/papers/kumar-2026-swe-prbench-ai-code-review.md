# SWE-PRBench: Benchmarking AI Code Review Quality Against Pull Request Feedback

**Autores:** Deepak Kumar (Foundry HQ)
**Publicação:** arXiv:2603.26130 [cs.SE]
**Ano:** 2026 (março)
**URL:** https://arxiv.org/abs/2603.26130
**Tipo:** paper / primary

---

## Metodologia

- **350 pull requests** com ground truth anotado por humanos
- Avaliação com **LLM-as-judge** validado em κ=0.75
- **8 modelos frontier** testados
- Três configurações de contexto (frozen):
  - `config_A` — diff only
  - `config_B` — diff + file content
  - `config_C` — full context (incl. execution context, behaviour mapping, test signatures)
- AST-extracted function context e import graph resolution incluídos em config_C

## Achados principais

### Performance base

| Métrica | Valor |
|---------|-------|
| Detecção de issues humanos (melhor modelo) | **15–31%** |
| Tier gap entre top-4 e demais | top-4: 0.147–0.153; demais: ≤ 0.113 |

AI code review permanece muito abaixo da performance humana apesar de resultados fortes em code generation benchmarks.

### Achado central: atenção diluída por contexto

**Todos os 8 modelos degradam monotonicamente de config_A para config_C.**

Incluindo quando o contexto é enriquecido com:
- AST-extracted function context
- Import graph resolution
- Execution context
- Behaviour mapping
- Test signatures

**Mecanismo dominante:** colapso de detecção de `Type2_Contextual` issues em config_B — issues contextuais são os primeiros a desaparecer com contexto longo.

### Prompt estruturado bate contexto completo

| Configuração | Performance |
|-------------|-------------|
| 2.000-token diff + summary (estruturado) | **SUPERIOR** |
| 2.500-token full context (exec context + behaviour mapping + test signatures) | **INFERIOR** |

Implicação: estrutura do contexto > volume de contexto.

## Taxonomia de issues (implícita)

- `Type1_Direct` — detectável apenas do diff (bugs locais, estilo)
- `Type2_Contextual` — requer compreensão do contexto mais amplo (arquitetura, integração)

Type2_Contextual é onde AI review mais falha — e é exatamente o que mais degrada com mais contexto.

## Implicações práticas

1. Não passar contexto completo para LLM de review — causa atenção diluída
2. Estruturar contexto com sumarização antes de injetar
3. Blast-radius / topologia de codebase como **filtro de routing**, não como contexto injetado diretamente

## Limitações

- Dataset de 350 PRs (pequeno para generalização)
- Pesquisador independente — não peer-reviewed em venue principal
- Modelos testados não especificados individualmente em detalhes
- Config_C pode ter sido mal estruturada (dump de contexto vs. estruturação inteligente)
