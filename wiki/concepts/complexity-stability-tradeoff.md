---
title: "Complexity-Stability Tradeoff (May 1972)"
sources:
  - path: raw/papers/may-1972-large-complex-system-stability.md
    type: paper
    quality: primary
    stance: challenging
created: 2026-04-04
updated: 2026-04-04
tags: [ecology, complexity, stability, random-matrix, connectance, network-theory]
source_quality: high
interpretation_confidence: high
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-04
quarantine: false
provenance: source
---

## Resumo

May (1972): usando teoria de matrizes aleatórias, demonstra que sistemas complexos (alto n, C, σ) são instáveis além de um limiar crítico. Resultado contraintuitivo: complexidade não implica estabilidade — implica o oposto. Estabilidade requer que aσ²C < 1 (onde a = número de espécies, C = conectância, σ = força de interação). Resultado geral: aplica-se a qualquer sistema com variáveis interagindo aleatoriamente.

## Conteúdo

### O modelo

Sistema com n variáveis (populações de espécies em ecologia) descritas por equações diferenciais. Estabilidade do equilíbrio analisada pela matriz de interação A:

**dx/dt = Ax**

Onde:
- A = B - I (B = matriz aleatória de interações, I = matriz identidade)
- Diagonal a_ii = -1 (cada espécie estável isoladamente)
- Elementos off-diagonal a_ij: com probabilidade C (connectance) amostrado de distribuição com média 0 e variância σ²; com probabilidade 1-C, zero

### O resultado principal

Para n grande, usando a lei do semi-círculo de Wigner para matrizes aleatórias:

**Sistema QUASE-CERTAMENTE estável se:** σ√(nC) < 1
**Sistema QUASE-CERTAMENTE instável se:** σ√(nC) > 1

**Transição é abrupta** — "very sharp for n >> 1". A largura da zona de transição escala com n^(-1/2).

### Implicações qualitativas

1. **Tradeoff complexidade-estabilidade:** Aumentar n (mais espécies), C (mais links), ou σ (interações mais fortes) diminui a estabilidade. São substitutos: σ²C é o "produto de complexidade" que importa.

2. **Espécies com muitas interações devem ter interações fracas:** "Species which interact with many others (large C) should do so weakly (small σ), and conversely those which interact strongly should do so with but a few species." — padrão observado empiricamente por Margalef.

3. **Estrutura em blocos aumenta estabilidade:** 12-species community com 15% connectance tem probabilidade ≈ 0 de ser estável. Mesmas espécies reorganizadas em três blocos de 4 com 45% connectance interna: probabilidade 35% de estabilidade. Modularidade emergindo como propriedade necessária.

### Relação com Gardner & Ashby (1970)

May estende o resultado numérico de Gardner & Ashby (computacional, n=4,7,10) para prova analítica no limite n→∞. Confirma a transição abrupta conjecturada por Gardner & Ashby, com escalonamento explícito.

### Generalidade

"The formal development of the problem is a general one, and thus applies to the wide range of contexts" além de ecologia. O resultado é sobre matrizes aleatórias interagindo — qualquer sistema que possa ser modelado assim está sujeito ao mesmo tradeoff.

## Verificação adversarial

**Claim mais fraco:** O modelo assume interações ALEATÓRIAS e simétricas — ecossistemas reais têm estrutura (coevolução, hierarquias tróficas, reciprocidade), que pode aumentar estabilidade além das predições.

**O que o paper NÃO diz:** Não modela dinâmica temporal (apenas estabilidade local do equilíbrio); não discute como comunidades reais escapam do tradeoff via estrutura; não trata de coevolução. May (1973) em "Stability and Complexity" expande esses pontos.

**Simplificações:** 2 páginas — resultado de alta densidade. A prova completa via Wigner semi-circle law não está aqui, apenas citada. O resultado foi contestado empiricamente: ecossistemas reais mostram mais estabilidade do que o modelo prediz, sugerindo que estrutura não-aleatória importa.

**Prior work:** Lotka-Volterra (1925-26) para pares; Elton (1958) argumentou empiricamente que diversidade promove estabilidade (oposto ao resultado de May); May contradiz Elton diretamente.

## Conexões

- emerge-para: [[modular-escape-principle]] ON "modularidade como escape de σ√(nC) > 1 — isomorfismo com escapes de Judgment Aggregation e Bradford"
- contradicts: [[complexity-emergence]] ON "edge of chaos narrative" — Waldrop (1992) popularizou a ideia de que complexidade → riqueza funcional; May (1972) mostra que complexidade aleatória → instabilidade. A tensão é real: sistemas biológicos reais contornam o tradeoff via estrutura não-aleatória
- complementsAt: [[requisite-variety]] ON "variety and complexity" — Ashby: mais variedade no regulador melhora controle; May: mais variedade (conectância) no sistema regulado piora estabilidade. Domínios diferentes mas tensão conceitual
- complementsAt: [[resource-competition-coexistence]] ON "ecology of structured competition" — May (1972) = instabilidade de redes aleatórias; Tilman (1994) = como estrutura competitiva permite coexistência estável

## Fontes

- [May — Will a Large Complex System be Stable?](../../raw/papers/may-1972-large-complex-system-stability.md) — prova analítica σ√(nC) < 1, transição abrupta, implicação de modularidade, Nature 1972

## Níveis epistêmicos

### Descrição (verificado)
- Condição σ√(nC) < 1 para estabilidade (quase-certeza)
- Transição abrupta como n → ∞
- Tradeoff C-σ: interações fortes devem ser poucas
- Estrutura em blocos aumenta estabilidade (exemplo Gardner & Ashby)

### Interpretação (nossa)
- Generalização além de ecologia para sistemas com matrizes de interação aleatórias

## Quality Gate
- [x] Wikilinks tipados: 3 (contradicts, complementsAt ×2)
- [x] Instance→class: σ√(nC) < 1 é resultado matemático geral, não empiricamente calibrado para ecossistemas específicos
- [x] Meta-KB separado: sem referências a esta KB
- [x] Resumo calibrado: menciona o caráter contraintuitivo e a limitação de interações aleatórias
