# How Do Developers Use Code Suggestions in Pull Request Reviews?

**Autores:** Abir Bouraffa, Yen Dieu Pham, Walid Maalej
**Instituição:** University of Hamburg
**Publicação:** arXiv:2502.04835 [cs.SE]
**Ano:** 2025 (fevereiro)
**URL:** https://arxiv.org/abs/2502.04835
**Tipo:** paper / primary

---

## Metodologia

- **46 projetos GitHub** engineered (não toy projects)
- Análise de pull requests com uso da GitHub suggestion feature
- Open coding para identificar tipos de sugestões
- Survey com contributors dos projetos estudados
- Métricas: merge rate, resolution time, code complexity

## Achados principais

### Taxonomia de sugestões (4 tipos)

| Tipo | Frequência |
|------|-----------|
| Improvements | Mais frequente |
| Code style | Segundo |
| Fixes | Terceiro |
| Documentation | Menos frequente |

### Impacto das sugestões no PR

| Impacto | Resultado |
|---------|-----------|
| Merge rate | **Aumenta positivamente** |
| Resolution time | **Aumenta significativamente** |
| Code complexity | **Sem redução** |

Sugestões melhoram a chance de merge mas custam tempo. E não reduzem complexidade — implicação: sugestões melhoram surface quality, não arquitetura.

### Fatores sociais

- Sugestões são mais utilizadas por reviewers quando o submitter é **newcomer**
- Developers buscam sugestões principalmente para: rastrear rationale e buscar exemplos de código
- Sugestões têm valor como knowledge sharing tool, não apenas correção técnica

## Ligação com outros papers

- Explica parcialmente por que Zhong 2026 encontra adoção maior de sugestões humanas (56.5%) vs AI (16.6%): sugestões humanas carregam contexto social e educational value que AI não captura
- "Improvements being most frequent" alinha com o achado de Zhong de que AI foca em code improvement (>95%)
- O aumento de resolution time sem redução de complexity sugere que sugestões adicionam overhead sem ganho arquitetural — similar ao que Zhong reporta sobre AI suggestions aumentando code complexity quando adotadas

## Limitações

- GitHub suggestion feature é específica — pode não generalizar para outros mecanismos de review
- Projetos "engineered" podem ter dinâmicas diferentes de projetos acadêmicos ou corporativos fechados
