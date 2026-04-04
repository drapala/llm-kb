---
title: "Partial Information Decomposition"
sources:
  - path: raw/papers/wibral-partial-information-decomposition.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [information-theory, multi-agent, ensemble-methods, neural-coding]
source_quality: medium
interpretation_confidence: medium
quarantine: false
resolved_patches: []
---

## Resumo

Partial Information Decomposition (PID) estende a teoria da informação de Shannon para sistemas com múltiplas entradas, decompondo a informação total que um conjunto de inputs {X1, X2} fornece sobre um output Y em quatro componentes não-sobrepostos: informação única de X1, informação única de X2, informação compartilhada (redundante) entre X1 e X2, e informação sinérgica (que só existe na combinação). O PI-diagram visualiza estas quatro componentes como regiões distintas.

## Conteúdo

### Motivação

Shannon's information theory clássica trata canais com uma entrada e uma saída. Em sistemas com múltiplas entradas — como circuitos neurais corticais, processadores lógicos (NAND requer duas entradas), ou agentes com fontes diversas de informação — a mutual information I(Y:X1,X2) não responde como as diferentes entradas contribuem para o output. Wibral et al. (2017) aplicam PID para especificar funções-objetivo de processadores neurais, mas o framework é domain-independent.

### A decomposição PID

Para um output Y e dois inputs X1, X2, a mutual information total I(Y:X1,X2) decompõe-se como:

```
I(Y:X1,X2) = Iunq(Y:X1\X2) + Iunq(Y:X2\X1) + Ishd(Y:X1;X2) + Isyn(Y:X1;X2)
```

Onde:

**Informação única** Iunq(Y:X1\X2): informação que X1 tem sobre Y que não pode ser obtida de X2. Análogo ao que um agente contribui exclusivamente, não disponível em nenhuma outra fonte.

**Informação compartilhada (redundante)** Ishd(Y:X1;X2): informação que X1 tem sobre Y que também pode ser obtida de X2 — e vice-versa. Surge por dois mecanismos distintos: (a) *source redundancy*: X1 e X2 têm mutual information entre si; (b) *mechanistic redundancy*: o mecanismo que gera Y cria redundância mesmo com inputs independentes (ex: operação AND sobre variáveis independentes gera 0.311 bits de shared information).

**Informação sinérgica** Isyn(Y:X1;X2): informação sobre Y que só existe ao observar X1 e X2 conjuntamente — não obtível de nenhum deles separadamente. O XOR é o exemplo canônico: nenhuma entrada individualmente diz nada sobre o output, mas a combinação determina-o completamente.

### O PI-diagram

O PI-diagram (Williams e Beer, 2010) é a representação gráfica das quatro componentes PID como regiões não-sobrepostas. Permite visualizar qual componente domina num sistema e como goal functions neurais se mapeiam nas regiões.

### Relações com mutual information clássica

As componentes PID se relacionam com termos clássicos por:
```
I(Y:X1) = Iunq(Y:X1\X2) + Ishd(Y:X1;X2)
I(Y:X1|X2) = Iunq(Y:X1\X2) + Isyn(Y:X1;X2)
```

Estas relações permitem expressar goal functions neurais clássicas em linguagem PID.

### Goal functions neurais via PID

Wibral et al. propõem uma goal function genérica G como combinação linear ponderada:
```
G = Γ0·Iunq(Y:X1\X2) + Γ1·Iunq(Y:X2\X1) + Γ2·Ishd + Γ3·Isyn + Γ4·H(Y|X1,X2)
```

Funções específicas são instâncias com pesos particulares:
- **Infomax** (Linsker): maximiza I(Y:X1) = Iunq + Ishd, sem preferência por nenhum
- **Coherent infomax**: maximiza Ishd e Iunq(Y:X1\X2), minimiza Isyn entre drive e contexto
- **Predictive coding**: envolve maximizar informação sobre X1(t) usando X2(t)=predictor; requer synergy via XOR no circuito de detecção de erro

### Limitação computacional do framework

O sistema de equações PID é subdeterminado: com dois inputs e um output há 3 equações independentes mas 4 termos PID. É necessário definir axiomaticamente ao menos um termo. Os sistemas axiomáticos de Bertschinger et al. (2014) e Griffiths & Koch (2014) têm maior aceitação e resultados próximos entre si.

### O que F (Kay-Phillips) não pode representar

A goal function F do coherent infomax, definida em termos de informação clássica, não cobre todo o espaço de G definido via PID. O subespaço não representável é unidimensional: {Γ = α·[-1,-1,1,1,0]ᵀ}. Em particular, **é impossível** usando F maximizar simultaneamente Isyn e Ishd enquanto minimiza as duas únicas — e vice-versa.

## Interpretação

⚠️ (nossa interpretação) A decomposição PID é diretamente aplicável ao diagnóstico de ensembles de compiladores: dado um output wiki (Y) e dois compiladores-agente (X1, X2), PID quantifica quanto cada agente contribui unicamente (Iunq), quanto suas contribuições se sobrepõem redundantemente (Ishd), e se há informação sinérgica que só existe na combinação dos dois (Isyn). Um ensemble bem projetado maximizaria Iunq de cada agente e Isyn do conjunto, minimizando Ishd (redundância desnecessária).

⚠️ (nossa interpretação) A distinção entre *source redundancy* e *mechanistic redundancy* tem implicação arquitetural: dois compiladores com contextos sobrepostos (mesmo acesso a raw/) terão Ishd alta por source redundancy mesmo com estratégias diferentes. Separação de contexto é necessária para reduzir redundância estruturalmente.

⚠️ (nossa interpretação) A synergy (XOR canônico) corresponderia a artigos wiki que só podem ser gerados por múltiplos compiladores em combinação — synthesis articles que nenhum compilador individual produziria. Artigos como reflexion-weighted-knowledge-graphs são candidatos a essa categoria.

## Verificação adversarial

**a. Claim mais fraco:** A afirmação de que o framework PID é "domain-independent" — o paper é motivado por neurociência e as aplicações são todas em processamento neural. A generalização a outros domínios é implícita, não demonstrada.

**b. O que o paper NÃO diz:**
- Não propõe um algoritmo eficiente para calcular PID em escala — o problema computacional permanece em aberto para casos gerais
- Não prova que Isyn e Ishd são sempre não-negativos; a positividade é um requisito axiomático, não uma garantia
- Não avalia empiricamente as goal functions propostas além da análise matemática

**c. Simplificações feitas:**
- O paper limita PID a dois inputs; extensão a N inputs é mencionada como trabalho futuro
- A equivalência entre os sistemas axiomáticos de Bertschinger/Griffiths/Harder é aproximada, não exata

**d. Prior work:** Williams e Beer (2010) introduziram o PI-diagram original. Bertschinger et al. (2014), Griffiths e Koch (2014), e Harder et al. (2013) propuseram os sistemas axiomáticos. Kay e Phillips propuseram a goal function F para coherent infomax.

## Níveis epistêmicos

### Factual (direto da fonte)
- Equação de decomposição (3) e relações com informação clássica (4), (5) são resultados matemáticos
- O subespaço não representável por F (equação 17) é resultado analítico
- A AND operation em variáveis binárias independentes gera 0.311 bits de shared information (Bertschinger et al. 2014, referenciado em Wibral et al.)
- O sistema PID é subdeterminado (3 equações, 4 incógnitas)

### Síntese (inferência moderada)
- Coherent infomax é uma instância de G com pesos específicos — isto é demonstrado matematicamente no paper
- A limitação de F em representar certas goal functions G decorre da álgebra

### Especulação
- Aplicação a ensembles de compiladores de KB
- Source vs mechanistic redundancy como critério arquitetural para multi-agent design
- Synergy como categoria de artigos que exigem múltiplos agentes

## Conexões
- derivedFrom: [[information-theory-shannon]] — PID estende mutual information de Shannon (H, I(X;Y)) para o caso de múltiplas entradas com contribuições separadas
- complementsAt: [[information-bottleneck]] — IB trata compressão de uma variável; PID trata contribuições de múltiplas variáveis ao mesmo target
- validates: [[multi-agent-orchestration]] — PID fornece métrica formal para avaliar contribuição única vs redundante de agentes num ensemble
- partOf: [[complexity-emergence]] — synergy é uma das formas de emergência: o todo fornece mais informação que a soma das partes

## Fontes
- [Wibral et al. (2017)](../../raw/papers/wibral-partial-information-decomposition.md) — paper primário: framework PID completo, relações com goal functions neurais (infomax, coherent infomax, predictive coding), prova de limitação de F, PI-diagram

## Quality Gate
- [x] Wikilinks tipados: 4 substituições, 0 tipos novos — artigo Shannon existe em information-theory-shannon.md
- [x] Instance→class: 1 claim qualificado — "0.311 bits" qualificado com fonte (Bertschinger et al. via Wibral)
- [x] Meta-KB separado: sim — 3 referências a compiladores/KB movidas para ## Interpretação
- [x] Resumo calibrado: mantido — limitação computacional e restrição a 2 inputs refletidas
