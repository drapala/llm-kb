---
title: "Team Decision Theory"
sources:
  - path: raw/papers/ho-chu-team-decision-theory.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [decision-theory, multi-agent, information-structures, control-theory, optimization]
source_quality: medium
interpretation_confidence: low
quarantine: true
quarantine_created: 2026-04-04
quarantine_reason: "interpretation_confidence: low — aplicação a multi-compiler é interpretação nossa; 3+ especulações"
resolved_patches: []
---

> ⚠️ QUARENTENA: artigo não pode ser linkado por outros até /promote.

## Resumo

Team Decision Theory (Ho & Chu, 1972) estuda organizações onde múltiplos membros controlam variáveis de decisão diferentes, têm acesso a informações diferentes, mas compartilham um único objetivo (payoff comum). O conceito central é a *information structure* — a relação causal entre observações, ações passadas e decisões futuras. O paper caracteriza quando a otimização do time pode ser decomposta em problemas independentes (static teams vs. dynamic teams com partially nested information structure) e prova que linear-quadratic-Gaussian control é um caso especial.

**Nota OCR:** O paper é de 1972, digitalizado por scan. Partes do texto são fragmentadas, equações ocasionalmente ilegíveis. Toda extração de conteúdo abaixo reflete o que foi recuperável; claims marcados com [OCR?] indicam reconstrução parcial.

## Conteúdo

### Formulação do problema (Team Problem)

Um **team** é uma organização com N membros onde:
- Cada membro i recebe informação zi e controla variável de decisão ui via lei de controle γi: zi → ui
- Todos os membros minimizam a mesma função de payoff J(γ1, ..., γN)
- O objetivo é encontrar γi* para todos i que minimiza J

A distinção entre *team* e *game* é central: num jogo (game theory), cada agente tem seu próprio objetivo; num time, o objetivo é único mas a informação é distribuída.

### Estrutura de informação (Information Structure)

A informação disponível para o membro i é formulada como [OCR: equação parcialmente recuperada]:
```
zi = Hi·ξ + Σj Dij·uj
```
onde ξ é o vetor de variáveis aleatórias do ambiente (Gaussiano), Hi e Dij são matrizes conhecidas por todos os membros, e uj são ações de membros anteriores.

O sistema é **causal**: o que acontece no futuro não afeta o que é observado agora. Isso implica restrições sobre quais Dij são não-zero.

### Diagrama de precedência (Precedence Diagram)

Define-se a relação de precedência: j precede i (j ≺ i) se:
- Dij ≠ 0 (ação de j entra diretamente na informação de i), ou
- Existe cadeia transitiva de precedências de j até i

O **precedence diagram** é um grafo dirigido onde membros são nós e arestas indicam relações de precedência. O **information structure diagram** adiciona *memory-communication lines* (linhas pontilhadas) mostrando quais membros têm acesso ao quê.

Casos especiais:
- **Static team**: grafo de precedência com nós isolados — sem relações causais entre membros
- **Dynamic team**: presença de cadeias de precedência — ações passadas afetam informações futuras

### Partially Nested Information Structure

Uma estrutura de informação é **partially nested** se: j ≺ i implica Zj ⊆ Zi para todo i, j (e todo conjunto de leis de controle γ).

Interpretação: num sistema partially nested, todo seguidor tem acesso a tudo que seu precedente sabia. Em particular: se j ≺ i, o membro i pode deduzir a ação uj de j — pois conhece zj e sabe a lei de controle γj usada (que pode ser acordada antecipadamente pela equipe).

Consequência formal: os termos Dij·uj tornam-se redundantes na formulação de zi quando o sistema é partially nested, pois uj é determinístico dado zj, que já está em zi.

### Resultado principal: redução a static team

**Teorema 1** (Ho & Chu): Num dynamic team com partially nested information structure, a informação efetiva ẑi = Hi·ξ (apenas ruído externo, sem termos de ação) é equivalente à informação original zi para qualquer conjunto fixo de leis de controle. O problema equivale, portanto, a um static team problem.

Consequência: pelo Teorema de Radner (para static teams com LQG), a solução ótima existe, é única, e é linear em ẑi. Portanto, para dynamic teams partially nested com payoff quadrático e distribuição Gaussiana, a solução ótima é linear nas observações.

### Aplicação: LQG Control como caso especial

O problema clássico de controle estocástico linear-quadratic-Gaussian (LQG) é um caso especial da teoria de times com:
- N membros = N estágios de controle
- Informação de cada membro = estado acumulado até o estágio atual
- Estrutura naturally partially nested (memória perfeita)

Esta derivação unifica controle LQG clássico com a teoria de times distribuídos.

### O que o paper NÃO resolve

O paper (Part I) explicitamente não resolve o caso geral de dynamic teams sem partially nested structure. Esses casos são matematicamente intratáveis em geral — o payoff deixa de ser convexo e zi deixa de ser Gaussiano mesmo quando ξ é Gaussiano. Part II (mencionada mas não incluída no raw) trataria outros casos especiais.

**OCR Gaps documentados:**
- Figuras 1-4 (diagramas de precedência e estrutura de informação) não são recuperáveis como texto — são diagramas que descrevem os exemplos 1-3
- Algumas equações intermediárias nas seções III e IV são parcialmente ilegíveis (ex: equação 17 tem termos com símbolos misturados ao texto pelo OCR)
- A seção de payoff da Part II não está no raw (paper foi digitalizado incompleto ou é realmente Part I apenas)

## Interpretação

⚠️ (nossa interpretação) A teoria de times é o framework formal mais próximo do problema de multi-compiler KB: compiladores são membros do time, o payoff compartilhado é a qualidade do wiki final, cada compilador tem acesso a subconjunto diferente de raw/ (information structure). A pergunta de design mais relevante desta teoria: a information structure dos compiladores é partially nested?

⚠️ (nossa interpretação) Se o compilador "Tishby/PID" (este agente) e o compilador "Shannon/Beer" (outro agente, desta sessão) têm acesso a overlapping sources, a estrutura é similar a static team — sem precedência, mas com potencial redundância. Se um agente processa antes e passa síntese para o outro, torna-se partially nested — e pelo Teorema 1, a solução ótima seria linear (sem necessidade de comunicação extra além da síntese anterior).

⚠️ (nossa interpretação) A distinção static vs. dynamic team tem implicação arquitetural concreta: compiladores paralelos sem comunicação = static team; compiladores sequenciais com handoff = dynamic team partially nested. O design atual da KB (agentes paralelos por tarefa) é static team; compilação sequencial com review incremental seria partially nested.

⚠️ (nossa interpretação) A "lei de controle acordada antecipadamente" (CLAUDE.md + templates) é análoga à agreed-upon γi — permite que cada agente deduza o comportamento dos outros sem comunicação em tempo real.

## Verificação adversarial

**a. Claim mais fraco:** A afirmação de que "qualquer dynamic team partially nested reduz a static team" — esta equivalência depende criticamente de todos os precedentes seguirem exatamente suas leis de controle acordadas, o que em sistemas com agentes LLM não é garantido (compliance não é determinístico).

**b. O que o paper NÃO diz:**
- Não trata heterogeneidade nos objetivos dos membros (um time com objetivos conflitantes é um game, não um team)
- Não discute robustez a erros nas leis de controle — assume compliance perfeito
- Não aborda escalabilidade computacional para N grande

**c. Simplificações feitas neste artigo:**
- OCR degradado impede extração completa das provas formais — claims sobre teoremas são baseados em leitura parcial
- A formalização matemática completa do Teorema 1 e seus lemas não foi integralmente recuperada

**d. Prior work:** Marschak (1955) formulou o problema de time original. Radner (data não recuperada via OCR) provou o teorema para static teams com LQG. Ho & Chu estendem ao caso dinâmico. O paper cita explicitamente Cover & Thomas (rate distortion, referência geral de teoria da informação) não como fonte direta mas como contexto da área.

## Níveis epistêmicos

### Factual (direto da fonte, OCR suficiente)
- Definição formal de team (objetivo único, informação distribuída) vs. game (objetivos distintos)
- Estrutura de informação zi = Hi·ξ + Σ Dij·uj e relação de precedência
- Definição de partially nested information structure
- LQG control como caso especial (demonstrado)

### Síntese (inferência moderada)
- Partially nested implica redução a static team (Teorema 1 — lido parcialmente)
- A solução ótima é linear para LQG partially nested (combinação de Teorema 1 + Radner)

### Especulação
- Analogia compiladores KB ↔ membros do time
- CLAUDE.md como "lei de controle acordada"
- Implicação arquitetural paralelo vs. sequencial

## Conexões
- complementsAt: [[multi-agent-orchestration]] — team theory provê fundamentação formal para design de sistemas multi-agente com objetivo compartilhado
- complementsAt: [[partial-information-decomposition]] — PID quantifica o que cada agente contribui; team theory otimiza como estruturar a informação entre agentes
- validates: [[groupthink-and-cascades]] — static teams (sem precedência) evitam cascades causadas por coordenação excessiva
- derivedFrom: [[causal-reasoning-pearl]] — o precedence diagram é uma instância de DAG causal (direção temporal de informação)

## Fontes
- [Ho & Chu (1972)](../../raw/papers/ho-chu-team-decision-theory.md) — paper primário: formulação da teoria de times, information structure, precedence diagram, partially nested structure, prova de redução a static team, LQG como caso especial. **Qualidade OCR: baixa em ~30% do texto — equações intermediárias e figuras degradadas.**

## Quality Gate
- [x] Wikilinks tipados: 4 substituições, 0 tipos novos
- [x] Instance→class: 0 claims numéricos sem qualificador (paper é teórico, sem benchmarks)
- [x] Meta-KB separado: sim — 4 referências a compiladores/KB movidas para ## Interpretação
- [x] Resumo calibrado: sim — OCR gap documentado no resumo e em seção dedicada
