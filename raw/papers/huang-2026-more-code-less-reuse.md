# More Code, Less Reuse: Investigating Code Quality and Reviewer Sentiment towards AI-generated Pull Requests

**Autores:** Haoming Huang et al.  
**Publicação:** arXiv:2601.21276  
**Ano:** Janeiro 2026  
**URL:** https://arxiv.org/abs/2601.21276  
**Tipo:** paper / primary

---

## Metodologia

- Análise de PRs gerados por LLM agents vs. PRs humanos no GitHub
- Duas perspectivas: **qualidade interna do código** e **percepção externa de reviewers**
- Métricas tradicionais: LOC (Lines of Code), Cyclomatic Complexity
- **Nova métrica proposta:** Max Redundancy Score (MRS) — mede redundância semântica

## Achado central: Type-4 clones

LLM agents tipicamente não geram clones textuais idênticos (Type-1/Type-2). Geram **Type-4 clones**: código redundante com inconsistências textuais mas semântica similar — duplicação que ferramentas tradicionais de detecção de clones (baseadas em similaridade textual) não capturam.

> "LLM models typically do not generate textually identical code clones; instead, they tend to produce more Type-4 clones — redundant code that exhibits textual inconsistencies but shares similar semantic meaning."

## Resultado principal

- LLM Agents frequentemente **desconsideram oportunidades de reuso** de código existente
- Resultado: **maior nível de redundância** comparado a desenvolvedores humanos
- Métricas tradicionais (pass rate, LOC) **não capturam** este problema — código passa nos testes mas aumenta a carga de manutenção

## Implicação para manutenção

Métricas existentes medem correctness mas não long-term maintainability. O MRS proposto pelo paper tenta preencher esse gap.

Reviewers de PR percebem negativamente o excesso de código sem reuso — o sentimento negativo em code reviews de AI-generated PRs está correlacionado com esta característica.

## Conexão com outros estudos

Este paper é citado diretamente no "Debt Behind the AI Boom" (Liu et al. 2026) como evidência do problema de duplicação semântica introduzida por AI tools.
