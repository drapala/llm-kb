---
source: Ashby, W.R. (1956). An Introduction to Cybernetics. Chapman & Hall, London.
author: W. Ross Ashby
date: 1956-01-01
type: article
quality: primary
stance: challenging
---

# Ashby — Law of Requisite Variety (1956)

## Fonte primária

Ashby, W.R. (1956). An Introduction to Cybernetics. Chapman & Hall. London.
Capítulos relevantes: 11 (Requisite Variety), 12 (The Error-Controlled Regulator).

Texto integral disponível em: http://pespmc1.vub.ac.be/books/IntroCyb.pdf

## A Lei

**Formulação original:** "Only variety can destroy variety." (Chapter 11, Section 11/5)

**Formulação operacional:** A variedade nos outcomes (O) de um sistema regulado não pode ser reduzida abaixo de:

V(O) ≥ V(D) / V(R)

onde:
- V(D) = variety das disturbances (perturbações do ambiente)
- V(R) = variety do regulador (respostas disponíveis)
- V(O) = variety dos outcomes (o que queremos minimizar)

**Implicação:** Para manter V(O) = 1 (outcome constante, controle perfeito), é necessário V(R) ≥ V(D). Se V(R) < V(D), alguns distúrbios passam sem regulação → error floor.

**Equivalente informacional:** "The variety of the regulator must be at least as great as the variety of the disturbances if the outcomes are to be kept within some desired subset."

## Exemplos de Ashby

1. **Termostato:** V(D) = muitas temperaturas ambientes possíveis. V(R) = on/off (2 estados). Resultado: controla temperatura dentro de uma faixa, não exatamente. Se V(D) incluir falha de aquecimento, V(R) = 2 é insuficiente.

2. **Jogador de xadrez:** V(D) = todos os movimentos possíveis do oponente. V(R) = todos os movimentos disponíveis para o jogador. Para vencer: V(R) deve cobrir (ou superar em qualidade) V(D). [verificar na fonte — Ashby usa exemplos de jogos mas a formulação exata do xadrez pode ser de Beer, não de Ashby]

3. **Sistema nervoso como regulador:** O cérebro tem ~10^10 neurônios com múltiplos estados cada → V(R) enorme. Necessário porque V(D) do ambiente é enorme. "The brain is not a luxury but a necessity." [verificar na fonte — citação pode ser paráfrase, não literal]

## Distinções importantes

- **Variedade ≠ complexidade.** Variedade é o NÚMERO de estados distintos que um sistema pode assumir. Um sistema complexo pode ter baixa variedade (se converge para poucos estados) e um sistema simples pode ter alta variedade (se tem muitos estados possíveis).

- **Controle ≠ redução de variedade no sistema.** Controle = ABSORÇÃO de variedade das perturbações pelo regulador, de modo que a variedade nos OUTCOMES (variáveis essenciais) seja mantida baixa. O regulador ABSORVE variedade, não a elimina.

- **Regulador ≠ controlador ativo.** Um regulador pode ser passivo (filtro que bloqueia distúrbios) ou ativo (controlador que compensa). A lei se aplica a ambos.

- **Essential variables:** As variáveis que DEVEM ser mantidas dentro de limites para o sistema sobreviver (em organismos: temperatura, pH, glucose). O regulador protege as essential variables das perturbações.

## Aplicações documentadas

- **Viable System Model** (Stafford Beer, 1972): modelo de gestão organizacional baseado em requisite variety. Cada nível da organização deve ter variedade suficiente para regular o nível abaixo.

- **Segunda cibernética** (Heinz von Foerster): sistemas auto-referentes onde o observador é parte do sistema regulado. Variedade do observador limita o que pode ser observado.

- **Engenharia de controle:** Design de controladores robustos. O princípio de Conant-Ashby (1970): "Every good regulator of a system must be a model of that system."

- **Management cybernetics:** A lei é usada para argumentar que hierarquias organizacionais existem para AMPLIFICAR variedade (cada nível agrega variedade dos subordinados) e ATENUAR variedade (cada nível filtra para o nível superior).

## O que Ashby NÃO afirma

- **NÃO diz que mais complexidade = melhor controle.** Diz que mais VARIEDADE no regulador = melhor controle. Um regulador complexo com poucos estados efetivos tem variedade baixa.

- **NÃO resolve como MEDIR variedade em sistemas simbólicos.** Ashby trabalhava com máquinas de estados discretos. Variedade em linguagem natural ou em "perspectivas de um LLM" não é trivialmente definível. [verificar na fonte — Ashby pode ter discutido measurement challenges no cap. 7]

- **NÃO especifica como AUMENTAR variedade do regulador.** A lei diz que variedade é necessária, não como obtê-la. Beer (1972) propôs amplificação via hierarquia. Von Foerster propôs self-organization. A questão "como aumentar V(R)?" é aberta.

- **NÃO assume que todos os estados são igualmente prováveis.** A formulação básica usa cardinalidade (contagem de estados). A formulação com informação de Shannon (H = -Σp log p) pesa estados por probabilidade, mas Ashby frequentemente usa a versão mais simples. [verificar na fonte — capítulo 7 discute relação com information theory]

## Limitações reconhecidas

1. **Medir variedade em sistemas linguísticos é não-trivial.** Ashby trabalhava com autômatos de estados finitos. "Variedade de um LLM" não tem definição consensual.

2. **Condição necessária, não suficiente.** V(R) ≥ V(D) é necessário para controle, mas não garante controle — o regulador também precisa ter a ESTRUTURA certa (saber qual resposta dar a qual distúrbio).

3. **Estático vs dinâmico.** A lei na forma mais simples assume snapshot estático. Sistemas que aprendem (como LLMs) mudam V(R) ao longo do tempo — a lei original não modela essa dinâmica explicitamente.

## Conceitos relacionados no livro

- **Homeostasis** (cap. 5-6): manutenção de essential variables dentro de limites
- **Essential variables**: o que o regulador DEVE proteger
- **Black box methodology** (cap. 6): como estudar um sistema sem conhecer sua estrutura interna — inferir comportamento de input-output
- **Ultrastability** (cap. 7): sistemas que mudam sua ESTRUTURA quando essential variables saem dos limites — self-organization via parameter change

> [editorial — não é de Ashby]
> Aplicação potencial à KB: se o compilador (1 LLM) tem variedade fixa
> V(compilador), e o corpus tem V(corpus) >> V(compilador), a lei prediz
> error floor irreducível. Mais process (commands, hooks, reviews) não
> aumenta V(compilador) — opera dentro do mesmo V. A única forma de
> aumentar V(regulador): múltiplos modelos, múltiplas perspectivas,
> adversarial externo. Esta é INTERPRETAÇÃO nossa — não está em Ashby.
> Status: L0 (aplicação a LLM KBs não verificada em nenhuma fonte).
