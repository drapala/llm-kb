# Automated Code Review In Practice

**Autores:** Umut Cihan, Vahid Haratian, Arda İçöz, Mert Kaan Gül, Ömercan Devran, Emircan Furkan Bayendur, Baykal Mehmet Uçar, Eray Tüzün
**Instituição:** Bilkent University + Beko (Türkiye)
**Publicação:** arXiv:2412.18531 [cs.SE]
**Ano:** 2024 (dezembro)
**URL:** https://arxiv.org/abs/2412.18531
**Tipo:** paper / primary

---

## Metodologia

- **238 practitioners** em **10 projetos industriais** (empresa Beko)
- Ferramenta adotada: **Qodo PR Agent** (open-source)
- Análise focada em **3 projetos** com **4.335 pull requests**
  - 1.568 PRs com automated review
  - 2.767 PRs sem automated review (controle)
- Coleta de dados:
  1. Análise quantitativa de PR data (comment labels: resolved/unresolved)
  2. Surveys por PR individual (experiência do desenvolvedor)
  3. Survey geral com 22 practitioners (opinião ampla sobre automated review)

## Achados principais

### Taxa de resolução de comentários automatizados

- **73.8%** dos comentários automatizados foram marcados como "resolved"
- Variação significativa entre projetos

### Impacto no tempo de fechamento de PRs

| Condição | Tempo médio de fechamento |
|----------|--------------------------|
| Sem automated review | **5h 52min** |
| Com automated review | **8h 20min** |
| **Aumento** | **+2h 28min (+42%)** |

Nota: tendências variaram por projeto — em alguns, o tempo não aumentou.

### Percepção dos practitioners

- Maioria: **melhoria minor em qualidade** de código
- Benefícios reportados: melhor detecção de bugs, maior consciência de qualidade, promoção de best practices
- Problemas reportados: **faulty reviews**, **unnecessary corrections**, **irrelevant comments**

### Utilidade por tipo de problema

Ferramenta mais útil para:
- Detecção de bugs simples e padronizados
- Verificação de best practices conhecidas

Ferramenta menos útil para:
- Contexto arquitetural e decisões de design
- Julgamento sobre comportamento esperado

## Interpretação dos dados (autores)

A alta taxa de resolução (73.8%) não implica alta qualidade — developers podem marcar como "resolved" sem realmente aplicar a sugestão. O aumento no tempo de fechamento (+42%) sugere overhead cognitivo: developers precisam avaliar, aceitar ou rejeitar cada comentário automatizado, adicionando carga ao processo.

## Limitações

- Ambiente industrial único (Beko) — pode não generalizar
- Qodo PR Agent é uma ferramenta específica; outras ferramentas podem ter comportamento diferente
- Survey bias: developers que respondem podem ter opiniões mais fortes (positivas ou negativas)
- Período de estudo não especificado (curva de aprendizado pode afetar resultados iniciais)
