---
title: "Two-Sigma Problem"
sources:
  - path: raw/papers/bloom-1984-two-sigma-problem.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/articles/nintil-bloom-sigma-systematic-review.md
    type: article
    quality: secondary
    stance: challenging
    challenging_type: content
created: 2026-04-11
updated: 2026-04-11
tags: [educational-psychology, tutoring, mastery-learning, effect-size, empirical]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
quarantine: true
quarantine_created: 2026-04-11
quarantine_reason: "Gate 3 — claims_invalidated: descrição dos estudos como não-randomizados estava incorreta (corrigida no corpo; verificação humana necessária)"
provenance: synthesis
synthesis_sources:
  - raw/papers/bloom-1984-two-sigma-problem.md
  - raw/articles/nintil-bloom-sigma-systematic-review.md
---

## Resumo
Bloom (1984) reportou que alunos com tutoria 1:1 combinada com mastery learning performaram 2 desvios padrão acima de alunos em instrução convencional de sala de aula. Revisões sistemáticas posteriores confirmam que tutoria produz efeito real (d≈0.79), mas não replicam o 2 sigma em condições generalizadas — o efeito original é atribuído parcialmente a confounds metodológicos.

## Conteúdo

### O achado original (Bloom 1984)

Bloom reportou três condições comparadas em dois estudos de dissertação (Anania 1982; Burke 1984), conduzidos na Universidade de Chicago com estudantes de séries 4, 5 e 8:

| Condição | Resultado relativo |
|----------|--------------------|
| Conventional (sala de aula, ~30 alunos) | baseline (50º percentil) |
| Mastery Learning (instrução em grupo com ciclos de correção) | +1 sigma (84º percentil) |
| Tutoring 1:1 (mastery learning individual) | +2 sigma (98º percentil) |

Disciplinas testadas: Probabilidade e Cartografia. N total ≈ 222 alunos em escolas paroquiais de Chicago.

"The average tutored student was above 98% of the students in the control class." (Bloom, 1984)

O "problema" nomeado por Bloom: encontrar métodos de instrução em grupo com eficácia equivalente à tutoria 1:1, dado que tutoria universal é inviável economicamente.

### Evidência replicatória (meta-análises posteriores)

Efeitos para **mastery learning** (revisão Kulik, Kulik & Bangert-Drowns 1990; Ricón/Nintil systematic review):

| Contexto | Effect size (d) |
|----------|----------------|
| Geral | 0.40–0.52 |
| Estudantes desfavorecidos | 0.61 |
| Testes construídos pelo experimentador | ~0.50 |
| Testes padronizados | ~0.08 (negligível) |
| Khan Academy RCT | ~0.06 |

Efeitos para **tutoria** (Hattie 2009 meta-meta-análise, >800 estudos):

| Contexto | Effect size (d) |
|----------|----------------|
| Média geral (Hattie 2009) | 0.79 |
| Software tutoring de alta qualidade | comparável a tutores humanos |
| DARPA Digital Tutor (contexto militar, IT) | 1.97–3.18 |

O d=0.79 de Hattie para tutoria é substancial, mas inferior ao 2.0 reportado por Bloom. O DARPA Digital Tutor atingiu d>1.97 em contexto altamente específico (adultos militares motivados, domínio técnico bem-delimitado).

### Critiques metodológicas ao estudo original

Identificadas por Slavin e Ricón/Nintil:

1. **Confound de padrão de mastery:** grupo de tutoria exigia 90% de domínio; sala de aula exigia 80% — o efeito pode ser de padrão, não de formato de instrução
2. **Viés de teste:** testes construídos pelo experimentador inflam efeitos; em testes padronizados, ganhos são próximos de zero para mastery learning
3. **Confound de tempo:** mastery learning requer mais tempo de instrução; controlando tempo, efeitos caem
4. **Amostras pequenas e não-representativas:** escolas paroquiais específicas de Chicago; os estudos usaram pareamento entre condições, mas o contexto é estreito e o N é insuficiente para generalização
5. **Publication bias:** literatura subjacente favorece resultados positivos
6. **Fade-out:** ganhos não se sustentam no longo prazo em estudos de follow-up

### Mecanismos subjacentes (o que a evidência suporta)

A revisão de Ricón conclui que os mecanismos centrais são: exposição repetida, testes frequentes, feedback direcionado e remediação — não algo específico do framework de mastery learning per se. Efeitos de d=0.3–0.5 representam melhorias reais, mas não as transformações sugeridas por Bloom.

## Verificação adversarial

**Claim mais fraco:** o 2 sigma é apresentado como efeito de tutoria, mas pode ser em grande parte efeito de padrão de mastery diferente entre condições.

**O que Bloom não diz:** (1) não afirma que o efeito é replicável em condições de implementação típica; (2) não controla por tempo de instrução; (3) não reporta resultados de longo prazo.

**Simplificações feitas:** o artigo trata o 2 sigma como finding central, mas revisões posteriores sugerem que é limite superior em condições ideais controladas, não efeito típico.

**Prior work:** Carroll (1963) — Model of School Learning; Bloom (1968) — Learning for Mastery. Bloom 1984 é síntese, não experimento original do próprio Bloom.

## Quality Gate
- [x] Wikilinks tipados: nenhum wikilink necessário neste artigo (conceito isolado no primeiro ingest)
- [x] Instance→class: efeitos qualificados com autor, ano e contexto
- [x] Meta-KB separado: nenhuma referência a /ask ou design da KB
- [x] Resumo calibrado: reflete a tensão entre claim original e replicações

## Conexões
- aristocratic-tutoring-history partOf two-sigma-problem (contexto histórico do mesmo fenômeno)

> ⚠️ QUARENTENA: Gate 3 — claim "estudos não-randomizados" invalidado (corrigido no corpo; verificação humana necessária antes de citar)

## Fontes
- [Bloom 1984](../../raw/papers/bloom-1984-two-sigma-problem.md) — paper original, claim de 2 sigma, três condições comparadas
- [Ricón/Nintil systematic review](../../raw/articles/nintil-bloom-sigma-systematic-review.md) — efeitos das meta-análises, critiques metodológicas, mecanismos subjacentes
