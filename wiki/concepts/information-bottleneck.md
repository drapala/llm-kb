---
title: "Information Bottleneck"
sources:
  - path: raw/papers/tishby-information-bottleneck.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [information-theory, compression, learning, variational-principles]
source_quality: medium
interpretation_confidence: medium
quarantine: false
resolved_patches: []
provenance: source
---

## Resumo

O Information Bottleneck (IB) é um princípio variacional que formaliza a extração de informação relevante: dada uma variável de entrada X e uma variável de relevância Y, encontra a representação comprimida X̃ de X que minimiza I(X;X̃) (compressão máxima) sujeita a preservar I(X̃;Y) (relevância máxima). O parâmetro β controla o tradeoff entre compressão e preservação de relevância ao longo de uma família de curvas no plano (IX, IY).

## Conteúdo

### Problema motivador

Shannon's rate distortion theory caracteriza o tradeoff entre taxa de compressão R e distorção D, mas requer uma função de distorção d(x, x̃) definida a priori. Em muitos domínios práticos — reconhecimento de fala, processamento de linguagem natural, bioinformática, codificação neural — a função de distorção correta não é conhecida e sua escolha arbitrária equivale a seleção arbitrária de features. O IB resolve este problema substituindo a função de distorção pelo sinal de relevância Y, cujo acesso ao conjunto de dados é assumido (via distribuição conjunta p(x, y)).

### Princípio variacional

O IB minimiza o funcional:

```
L[p(x̃|x)] = I(X̃; X) − β · I(X̃; Y)
```

onde β é o multiplicador de Lagrange que controla o tradeoff. A interpretação:
- β = 0: compressão máxima, tudo mapeado a um único ponto — I(X̃;Y) = 0
- β → ∞: quantização arbitrariamente detalhada, I(X̃;Y) → I(X;Y)
- β intermediário: representações com grau variável de detalhe relevante

### Solução self-consistent

A solução ótima satisfaz equações iterativas envolvendo três distribuições — p(x̃|x), p(x̃), p(y|x̃) — que convergem alternando iterações análogas ao algoritmo Blahut-Arimoto. A medida de distorção que emerge naturalmente da solução é a divergência KL entre distribuições condicionais:

```
d(x, x̃) = D_KL[p(y|x) || p(y|x̃)]
```

Esta distorção não é assumida; ela emerge do princípio variacional.

### Estrutura das soluções e β-curve

Para cada valor de β, existem valores correspondentes de IX ≡ I(X, X̃) e IY ≡ I(X̃, Y) para cada cardinalidade de X̃. As soluções traçam curvas convexas no "plano de informação" (IX, IY), analogas às curvas rate-distortion. A relação:

```
δI(X̃, Y) / δI(X, X̃) = β⁻¹ > 0
```

sugere uma abordagem de annealing determinístico: aumentando β, move-se ao longo das curvas convexas no plano de informação, separando-se (bifurcando) em transições de fase de segunda ordem a valores críticos de β.

### Relação com rate distortion theory

O IB generaliza rate distortion theory com duas diferenças-chave:
1. A função de distorção emerge do problema, não é especificada externamente
2. A otimização inclui tanto o particionamento de X quanto a otimização dos representantes x̃, enquanto rate distortion trata esses como problemas separados

### Aplicações reportadas no paper

Tishby, Pereira e Bialek mencionam aplicações a: clustering semântico de palavras em inglês (Pereira, Tishby, Lee 1993), classificação de documentos (Slonim e Tishby 1999), codificação neural, e análise espectral.

## Interpretação

⚠️ (nossa interpretação) A analogia entre IB e compilação de KB é direta: raw/ corresponde a X (sinal de entrada), a relevância Y corresponde às queries futuras esperadas (o que os usuários vão perguntar), e X̃ corresponde a wiki/ (representação comprimida). Compilar bem = maximizar I(X̃; Y) (preservar o que importa responder) enquanto minimiza I(X̃; X) (não duplicar raw/, não criar redundância desnecessária). O parâmetro β seria o "nível de detalhe" do wiki — artigos muito concisos (β baixo) ou muito detalhados (β alto).

⚠️ (nossa interpretação) O threshold do protocolo /ingest (>40 artigos, exigir contribuição nova) é análogo a operar com β baixo — compressão alta, preservando apenas informação genuinamente nova.

⚠️ (nossa interpretação) A bifurcação por transições de fase em β crítico é análoga à criação de novos artigos wiki quando um conceito atinge complexidade suficiente para justificar split.

## Verificação adversarial

**a. Claim mais fraco:** A afirmação de que o método "contém como casos especiais" predição, filtragem e aprendizado — mencionada no paper mas não demonstrada neste texto (referência a trabalho em preparação [1]).

**b. O que o paper NÃO diz:**
- Não prova que o IB é computacionalmente tratável em escala (convergência é provada mas não complexidade prática)
- Não discute como obter uma amostra suficiente de p(x,y) — explicitamente deixado como problema futuro (footnote 1)
- Não demonstra as aplicações mencionadas — estão em papers separados

**c. Simplificações feitas:**
- O paper assume distribuições finitas; extensão a espaços contínuos requer trabalho adicional
- A convergência é para mínimos locais (análogo ao EM); unicidade não é garantida

**d. Prior work:** O paper cita Shannon/Kolmogorov rate distortion (Cover & Thomas 1991), Csiszár & Tusnády (algoritmo BA, 1984), Blahut (1972), e trabalho próprio anterior em preparação.

## Níveis epistêmicos

### Factual (direto da fonte)
- Equações (15), (16), (28) e algoritmo iterativo (31) são resultados formais com provas
- β controla tradeoff: β=0 colapsa tudo a um ponto, β→∞ maximiza detalhe
- A medida de distorção natural é D_KL[p(y|x)||p(y|x̃)]
- Convergência do algoritmo iterativo é provada (Teorema 5)

### Síntese (inferência moderada)
- IB generaliza rate distortion theory ao substituir distorção por relevância via Y
- A estrutura bifurcante (transições de segunda ordem) cria hierarquia de quantizações relevantes

### Especulação
- Analogia com compilação de KB
- β como "nível de detalhe" de artigos wiki
- Bifurcação como justificativa para splits de artigos

## Conexões
- derivedFrom: [[information-theory-shannon]] — IB é extensão de rate distortion theory de Shannon/Kolmogorov; mutual information I(X;X̃) e I(X̃;Y) são definidas pela teoria de Shannon
- derivedFrom: [[rate-distortion-theory]] — IB Lagrangian L = I(X̃;X) − βI(X̃;Y) é um problema de rate distortion com relevância como distortion (⚠️ nossa interpretação)
- complementsAt: [[complexity-emergence]] — ambos tratam compressão e estrutura emergente, em níveis diferentes
- validates: [[curation-anti-bias]] — princípio IB formaliza por que curação deve preservar relevância, não apenas volume
- partOf: [[requisite-variety]] — compressão com preservação de variedade relevante é instância do princípio de Beer

## Fontes
- [Tishby, Pereira, Bialek (2000)](../../raw/papers/tishby-information-bottleneck.md) — paper primário: formalização do princípio IB, solução variacional, algoritmo iterativo, estrutura das soluções

## Quality Gate
- [x] Wikilinks tipados: 4 substituições, 0 tipos novos — artigo Shannon existe em information-theory-shannon.md
- [x] Instance→class: 0 claims numéricos sem qualificador (β=0 e β→∞ são limites matemáticos formais, não medições empíricas)
- [x] Meta-KB separado: sim — 3 referências a KB/compilação movidas para ## Interpretação
- [x] Resumo calibrado: mantido — resumo factual, caveats em ## Verificação adversarial
