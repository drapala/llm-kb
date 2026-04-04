---
title: "Social Choice Aggregation: Arrow (1950) & Black (1948)"
sources:
  - path: raw/papers/arrow-1950-difficulty-social-welfare.md
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/black-1948-group-decision-making.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [social-choice, impossibility, arrow, voting, single-peaked, median-voter, aggregation]
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

Arrow (1950): nenhuma função de bem-estar social satisfaz simultaneamente Unanimidade, Não-Ditadura, e Independência de Alternativas Irrelevantes → a única função possível é uma ditadura. Black (1948): sob single-peaked preferences (preferências com único máximo), a maioria é transitiva e o eleitor mediano vence — escape route para o teorema de Arrow. Complementa List & Pettit (2002) que opera no espaço de julgamentos lógicos, não preferências ordinais.

## Conteúdo

### Arrow (1950): A Difficulty in the Concept of Social Welfare

**O problema:** Em democracias capitalistas, decisões sociais são tomadas por voto ou pelo mercado. Arrow pergunta: é possível construir uma função de bem-estar social (SWF) que agregue preferências individuais em preferências sociais de forma razoável?

**Condições (Arrow's impossibility theorem):**

| Condição | Definição |
|---|---|
| **Unanimidade (Pareto)** | Se todos preferem x a y, a SWF deve preferir x a y |
| **Independência de Alternativas Irrelevantes (IIA)** | A ordenação social de x vs y depende apenas das ordenações individuais de x vs y — não de alternativas irrelevantes z |
| **Não-Ditadura** | Não existe indivíduo i tal que, sempre que i prefere x a y, a sociedade prefere x a y independentemente dos outros |
| **Domínio Irrestrito** | A SWF deve funcionar para qualquer perfil de preferências individuais |
| **Transitividade** | A ordenação social produzida deve ser transitiva (racional) |

**Teorema:** Nenhuma SWF satisfaz todas essas condições simultaneamente para 3+ alternativas. A única função que satisfaz Unanimidade, IIA e Transitividade é uma **ditadura**.

**Consequência:** O voto majoritário pode gerar ciclos (Paradoxo de Condorcet). Exemplo com 3 eleitores e 3 alternativas: A > B > C (eleitor 1), B > C > A (eleitor 2), C > A > B (eleitor 3) → maioria prefere A a B, B a C, C a A — intransitivo.

**O que Arrow NÃO diz:** Não afirma que democracia é impossível — afirma que uma noção específica de agregação racional de preferências ordinais é impossível. Diferentes formulações (preferências intensas, votação por aprovação, etc.) têm propriedades diferentes.

### Black (1948): Single-Peaked Preferences e o Eleitor Mediano

**O problema de Black:** Quando a votação majoritária é consistente (transitiva)?

**Condição suficiente:** Se as preferências de todos os membros do comitê são **single-peaked** em relação a alguma ordenação linear das alternativas, então:
1. A votação majoritária produz ordenação transitiva
2. Existe um **eleitor mediano** cuja preferência de topo vence qualquer outra alternativa em votação majoritária binária

**Single-peaked:** A curva de preferência de cada eleitor tem exatamente um máximo local. Intuitivo em decisões de política pública: posições num espectro esquerda-direita; intensidade de um imposto; tamanho de um bem público.

**Exemplo (Black):** 3 alternativas {a₁, a₂, a₃} numa linha. Se o eleitor A prefere a₂ > a₃ > a₁ e o eleitor B prefere a₃ > a₂ > a₁ e o eleitor C prefere a₁ > a₂ > a₃ — todas são single-peaked. O eleitor mediano (cujo pico está no meio da distribuição) vence.

**Teorema do Eleitor Mediano:** Com single-peaked preferences numa dimensão:
- A alternativa preferida pelo eleitor mediano é o **Condorcet winner** — vence qualquer outra em confronto direto
- É estável: nenhuma coalização pode derrotá-la por maioria

**Limitações:**
- Requer que as preferências sejam unidimensionais (ou "unidimensionalmente alinhadas" no sentido de List & Pettit)
- Preferências multidimensionais em geral não são single-peaked → Arrow se aplica
- Em dimensões múltiplas, não existe geralmente um equilíbrio de Condorcet (teorema de McKelvey 1976)

### Relação Arrow ↔ Black

Arrow e Black são diretamente complementares:
- Arrow: impossibilidade **geral** de agregação racional
- Black: condição suficiente para **escapar** da impossibilidade

A condição de single-peaked preferences de Black é exatamente o "unidimensional alignment" que List & Pettit (2002) generalizam para o espaço de julgamentos.

### Relação com List & Pettit (2002)

List & Pettit operam em preferências lógicas (julgamentos sobre proposições), não preferências ordinais sobre alternativas. Mas a estrutura é análoga:
- Arrow: impossibilidade para preferências → List & Pettit: impossibilidade para julgamentos (Theorem 1)
- Black: single-peaked preferences → List & Pettit: unidimensional alignment (Theorem 2)

Os dois pares de resultados são instâncias do mesmo problema meta-matemático: quando é que a agregação por maioria é lógicamente consistente?

## Verificação adversarial

**Claim mais fraco:** O Teorema de Arrow depende da condição IIA, que é controversa — vários autores argumentam que IIA é normativa demais e pode ser relaxada. Sen (1970) mostrou que mesmo relaxar para "quasi-transitivity" não resolve completamente.

**O que os papers NÃO dizem:** Arrow não diz que todas as formas de democracia falham — apenas a forma que pressupõe SWF com essas 4 condições. Black não diz que preferências reais são single-peaked — é uma condição estrutural.

**Simplificações:** O Arrow de 1950 é a versão simplificada; o livro "Social Choice and Individual Values" (1951) tem o resultado completo com provas mais rigorosas. O teorema aqui descrito é a versão que entrou para o uso padrão.

**Prior work:** Condorcet (1785) identificou o paradoxo do votante circular. Black cita Condorcet explicitamente. Arrow (1950) é essencialmente a formalização moderna do insight de Condorcet.

## Conexões

- contradicts: [[judgment-aggregation]] ON "impossibility structure" — Arrow (1950) é o predecessor direto de List & Pettit (2002); ambos mostram impossibilidade de agregação com condições análogas, mas em domínios diferentes (preferências vs. julgamentos)
- validates: [[judgment-aggregation]] ON "unidimensional alignment as escape route" — Theorem 2 de List & Pettit generaliza o resultado de Black para o domínio de julgamentos
- complementsAt: [[prospect-theory]] ON "individual rationality baseline" — Prospect Theory mostra que mesmo as preferências individuais divergem do modelo racional que Arrow assume

## Fontes

- [Arrow — A Difficulty in the Concept of Social Welfare](../../raw/papers/arrow-1950-difficulty-social-welfare.md) — teorema da impossibilidade, condições (unanimidade, IIA, não-ditadura, transitividade), paradoxo de Condorcet como motivação
- [Black — On the Rationale of Group Decision-Making](../../raw/papers/black-1948-group-decision-making.md) — single-peaked preferences, teorema do eleitor mediano, condição para transitividade da votação majoritária

## Níveis epistêmicos

### Descrição (verificado)
- Teorema de Arrow: 4 condições + impossibilidade → ditadura
- Paradoxo de Condorcet com 3 eleitores e 3 alternativas
- Single-peaked preferences de Black + teorema do eleitor mediano

### Interpretação (nossa)
- Relação estrutural Arrow ↔ Black ↔ List & Pettit como instâncias do mesmo problema

## Quality Gate
- [x] Wikilinks tipados: 3 (contradicts, validates, complementsAt)
- [x] Instance→class: teorema qualificado como resultado de Arrow (1950), não lei universal
- [x] Meta-KB separado: sem referências a esta KB
- [x] Resumo calibrado: escopo limitado (preferências ordinais, não todo conceito de democracia)
