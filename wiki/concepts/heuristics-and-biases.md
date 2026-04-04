---
title: "Heuristics and Biases (Kahneman & Tversky)"
sources:
  - path: raw/papers/kahneman-tversky-1974-heuristics-biases.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [behavioral-economics, heuristics, biases, decision-making, cognitive-shortcuts]
source_quality: high
interpretation_confidence: high
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-04
quarantine: false
---

## Resumo

Kahneman & Tversky (1974): pessoas usam 3 heurísticas cognitivas para julgar probabilidade e prever valores — representatividade, disponibilidade, e ajuste por âncora. Cada heurística gera vieses sistemáticos previsíveis. Nota: heurísticas são atalhos adaptativos (funcionam na maioria dos casos), não defeitos — os vieses são consequências colaterais.

## Conteúdo

### As três heurísticas

**1. Representatividade (Representativeness)**

Probabilidade avaliada pelo grau em que A "parece" pertencer à classe B (similaridade ao estereótipo).

Vieses resultantes:
- **Insensibilidade a prior probabilities (base rates):** Se a descrição de Steve "parece" um bibliotecário, as pessoas ignoram que há muito mais fazendeiros. Testado empiricamente: mesmo com 70% engenheiros vs 30% advogados, os sujeitos ignoraram a taxa base.
- **Insensibilidade ao tamanho da amostra:** Amostras pequenas julgadas tão representativas quanto grandes. "Lei dos grandes números" na pequena amostra = falácia do apostador.
- **Ilusão de validade:** Confiança em predições baseadas em similaridade mesmo quando feedback é ausente ou a validade preditiva é baixa.
- **Regressão à média:** Não intuída espontaneamente. Quando o desempenho é extraordinário, as pessoas não esperam regressão, porque regressão não parece representativa.

**2. Disponibilidade (Availability)**

Probabilidade avaliada pela facilidade com que instâncias vêm à mente.

Vieses resultantes:
- **Facilidade de recuperação:** Palavras com K no início parecem mais frequentes que palavras com K na terceira posição — mas há mais na terceira posição em inglês.
- **Correlação ilusória:** Pares de eventos distinctivos são super-associados porque sua co-ocorrência é imaginável.
- **Efetividade de cenários:** Cenários detalhados parecem mais prováveis do que descrições vagas (mesmo sendo lógicamente menos prováveis).

**3. Ajuste e Ancoragem (Adjustment and Anchoring)**

Estimativas partem de um valor inicial (âncora) e ajustam insuficientemente.

Vieses resultantes:
- **Ancoragem insuficiente:** Produtos de 8×7×6×5×4×3×2×1 estimados em ~2250; 1×2×3×4×5×6×7×8 estimados em ~512 (resposta correta: 40320).
- **Avaliação de eventos conjuntivos e disjuntivos:** Probabilidade conjuntiva (AND) superestimada; disjuntiva (OR) subestimada.
- **Ancoragem em avaliação de distribuições:** Intervalos de confiança de 90% frequentemente capturando apenas 50-70% dos valores verdadeiros — overconfidence sistemática.

### Natureza adaptativa das heurísticas

⚠️ Importante: Kahneman & Tversky apresentam heurísticas como mecanismos cognitivos adaptativos que geralmente funcionam. "In general, these heuristics are quite useful, but sometimes they lead to severe and systematic errors." O framework não é "humanos são irracionais" — é que atalhos cognitivos têm zonas de falha previsíveis.

### Diferença de Gigerenzer

⚠️ Interpretação editorial: Gigerenzer (fast-frugal heuristics) argumenta que heurísticas são racionais no ecossistema certo. K&T (1974) focam nos vieses sem discutir ecologia das heurísticas. Os dois frameworks são complementares: K&T = mapa dos erros; Gigerenzer = mapa do quando-funcionam.

## Verificação adversarial

**Claim mais fraco:** Os experimentos usam cenários de laboratório — a magnitude dos vieses em contextos naturais com stakes reais e feedback pode ser menor.

**O que o paper NÃO diz:** Não propõe que humanos sejam globalmente irracionais; não discute intervenções para reduzir vieses; não trata de vieses coletivos (apenas individuais).

**Simplificações feitas:** 3 heurísticas é uma taxonomia, não uma teoria completa — Kahneman & Tversky reconhecem que há outros mecanismos. A categorização é prescritiva para análise, não neurocientificamente fundamentada.

**Prior work:** Cita Ward Edwards (1968), Paul Meehl (1954) — há literatura anterior sobre julgamentos probabilísticos. O paper formaliza e sistematiza mais do que inicia do zero.

## Conexões

- complementsAt: [[fast-frugal-heuristics]] ON "when heuristics work vs. fail" — Gigerenzer (ecologia das heurísticas) é o lado positivo; K&T (1974) é o lado dos vieses. Não contraditórios: diferentes ênfases
- contradicts: [[fast-frugal-heuristics]] ON "base rate neglect as error" — Gigerenzer argumenta que ignorar base rates pode ser adaptativo em certos ambientes; K&T (1974) trata como erro sistemático
- prerequisiteOf: [[prospect-theory]] — prospect theory pressupõe o framework heurísticas/vieses para motivar os padrões de escolha que descreve
- complementsAt: [[judgment-aggregation]] ON "individual vs collective reasoning failures" — K&T (1974) = falhas individuais; List & Pettit (2002) = falhas coletivas mesmo com indivíduos racionais

## Fontes

- [Kahneman & Tversky — Judgment under Uncertainty](../../raw/papers/kahneman-tversky-1974-heuristics-biases.md) — 3 heurísticas (representatividade, disponibilidade, ancoragem), experimentos e vieses resultantes, Science 1974

## Níveis epistêmicos

### Descrição (verificado)
- 3 heurísticas com nomes e mecanismos — verificado em raw/
- Experimentos com prior probabilities, tamanho de amostra, ancoragem — verificados
- "In general useful but sometimes lead to severe errors" — citação direta

### Interpretação (nossa)
- Comparação com Gigerenzer como complementar, não contraditório

## Quality Gate
- [x] Wikilinks tipados: 4 (complementsAt ×2, contradicts ×1, prerequisiteOf ×1)
- [x] Instance→class: vieses qualificados com contexto experimental específico
- [x] Meta-KB separado: sem referências a /ask ou esta KB
- [x] Resumo calibrado: nota sobre caráter adaptativo incluída
