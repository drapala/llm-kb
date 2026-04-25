# Rethinking Code Review Workflows with LLM Assistance: An Empirical Study

**Autores:** Fannar Steinn Aðalsteinsson, Björn Borgar Magnússon, Mislav Milicevic, Adam Nirving Davidsson, Chih-Hong Cheng
**Instituição:** WirelessCar Sweden AB + Chalmers University of Technology
**Publicação:** arXiv:2505.16339 [cs.SE]
**Ano:** 2025 (maio)
**URL:** https://arxiv.org/abs/2505.16339
**Tipo:** paper / primary

---

## Metodologia

- Field study + field experiment na WirelessCar Sweden AB
- Duas variações de ferramenta LLM-assisted:
  - **Variation A:** AI-led review upfront (review completo antes do developer abrir o PR)
  - **Variation B:** On-demand interaction (developer consulta AI conforme necessário)
- Ambas usam **RAG com semantic search** para montar contexto relevante
- Developers avaliaram ambas em settings reais

## Desafios identificados no code review tradicional

- Context switching frequente
- Informação contextual insuficiente para o reviewer
- Tempo excessivo em PRs complexos

## Achados principais

### Preferências

- **AI-led reviews (Variation A) são globalmente mais preferidas**
- Mas a preferência é **condicional** na familiaridade do reviewer com o codebase
  - Reviewer familiar com o código: on-demand (B) é mais útil
  - Reviewer menos familiar: upfront AI review (A) reduz o esforço de entender o contexto

### RAG como solução para context assembly

A semântica do RAG resolve o problema de context switching ao pré-montar:
- Definições de funções relevantes
- Histórico de mudanças relacionadas
- Padrões de code review anteriores no projeto

Isso endereça diretamente o achado de SWE-PRBench: em vez de dump de contexto completo, recupera apenas o relevante para aquele diff.

### Preocupações dos developers

- **False positives** continuam sendo problema (alinha com Cihan 2024)
- **Trust issues** — principalmente quando o reviewer conhece o código melhor que o AI

## Implicação para design de ferramentas

O modo mais eficaz depende do perfil do reviewer:
- Junior / não familiar → AI upfront review reduz esforço
- Senior / familiar → On-demand interaction preserva autonomia e evita ruído

## Limitações

- Estudo em uma empresa (WirelessCar) — pode não generalizar
- Número de participantes não reportado claramente
- Sem métricas quantitativas de adoção ou merge rate
