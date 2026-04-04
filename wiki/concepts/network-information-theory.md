---
title: "Network Information Theory (Cover & Thomas Ch. 14)"
sources:
  - path: raw/papers/cover-thomas-elements-information-theory.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [information-theory, multi-terminal, slepian-wolf, multiple-access-channel, broadcast, wyner-ziv, distributed-coding, foundational]
source_quality: high
interpretation_confidence: high
quarantine: false
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
---

## Resumo

Network Information Theory (Cover & Thomas 1991, Ch.14) estende a teoria de Shannon para múltiplos transmissores/receptores. Resultado central: **Slepian-Wolf theorem** — fontes correlacionadas X,Y podem ser separadamente codificadas à soma de taxas H(X,Y), idêntico ao caso com codificação conjunta. Outros resultados: capacity region do Multiple Access Channel (MAC), broadcast channel, relay channel, e **Wyner-Ziv** (rate distortion com side information). Esses são os building blocks do CEO problem (Berger 1996).

## Conteúdo

### O problema de network information theory

Shannon (1948) trata pares fonte-destino únicos. Na prática: múltiplos transmissores competem pelo mesmo canal (MAC), um transmissor serve múltiplos receptores (broadcast), fontes correlacionadas precisam ser comprimidas sem comunicação entre encoders. A teoria de redes generaliza os resultados de Shannon para esses cenários.

Sem solução geral conhecida para redes arbitrárias (Cover & Thomas 1991, §14.10). Os resultados abaixo são para topologias específicas.

### Multiple Access Channel (MAC)

**Configuração**: m transmissores com entradas X₁,...,X_m; um receptor observa Y = f(X₁,...,X_m, Z).

**Capacity region** (Theorem, §14.3):

A capacity region do m-user MAC é o fecho convexo de:

R(S) ≤ I(X(S); Y | X(S^c))   para todo S ⊆ {1,...,m}

para alguma distribuição produto p₁(x₁)···p_m(x_m).

**Caso 2 usuários** (Cover & Thomas 1991, §14.3):

R₁ ≤ I(X₁; Y | X₂)
R₂ ≤ I(X₂; Y | X₁)
R₁ + R₂ ≤ I(X₁,X₂; Y)

**Gaussian MAC** com m usuários, potências P₁,...,P_m e ruído N:

Σ_{i∈S} Rᵢ ≤ C(Σ_{i∈S} Pᵢ / N)   para todo S,   onde C(x) = ½ log(1+x)

**Interpretação**: cada usuário pode transmitir à taxa máxima apenas se os outros não estiverem transmitindo; no geral há tradeoff entre taxas.

### Slepian-Wolf Theorem (§14.4)

**O resultado mais importante de distributed source coding.**

**Configuração**: Fontes correlacionadas (X,Y) i.i.d. ~p(x,y). X disponível em local A, Y em local B. Encoders operam **independentemente** — sem comunicação entre si. Um decoder comum recebe ambas as descrições.

**Pergunta**: quais pares de taxas (R₁, R₂) permitem reconstrução sem erro assintótico?

**Theorem 14.4.1 (Slepian-Wolf)**:

A região de taxas alcançável é:

R₁ ≥ H(X|Y)
R₂ ≥ H(Y|X)
R₁ + R₂ ≥ H(X,Y)

**Resultado surpreendente**: a taxa total mínima é H(X,Y) — a mesma que seria necessária com codificação **conjunta**. Encoders independentes não têm penalidade em relação a encoders que se comunicam, desde que o decoder tenha acesso a ambas as descrições.

**Exemplo numérico** (Cover & Thomas, §14.4.1): Weather in Gotham and Metropolis, correlação 0.89:
- Codificação independente: 200 bits (100 de cada)
- Codificação conjunta (encoder sabe Y): 150 bits
- **Slepian-Wolf**: 150 bits com encoders independentes — mesmo resultado

**Prova (achievability)**: Codebook aleatório para X com 2^{n(H(X|Y)+ε)} codewords. O decoder usa a mensagem de Y como side information para identificar a codeword correta de X — similar ao channel coding theorem mas com Y como "canal de auxílio".

### Broadcast Channel (§14.6)

**Configuração**: Um transmissor X envia para múltiplos receptores Y₁, Y₂ que recebem versões degradadas ou não de X.

**Degraded broadcast channel** (capacity region):

R₁ = I(U; Y₁)
R₂ = I(X; Y₂|U)

para alguma distribuição p(u)p(x|u)p(y₁,y₂|x) — onde U é "cloud center" para usuário de baixa prioridade, e X é refinamento para usuário de alta.

Dual do MAC em termos de capacidade de informação (Cover & Thomas, §14.5).

### Relay Channel (§14.7)

**Configuração**: transmissor X₁ → relay X₁' (que observa Y₁) → receptor Y. O relay ajuda a transmissão.

**Physically degraded relay channel** (Theorem 14.7.1):

C = max_{p(x,x₁)} min{I(X,X₁; Y), I(X; Y₁|X₁)}

O relay aumenta a capacidade mas não indefinidamente — limitado pelo link X→Y₁ ou Y₁→Y.

### Wyner-Ziv: Rate Distortion com Side Information (§14.9)

**Configuração**: Source X, side information Y disponível **apenas** no decoder (não no encoder). O encoder conhece p(x,y) mas não y.

**Pergunta**: quantos bits por símbolo de X são necessários para alcançar distortion D, dado que o decoder tem Y?

**Theorem 14.9.1 (Rate distortion with side information)**:

R_s(D) = min_{p(w|x), f} [I(X;W) − I(Y;W)]

onde W é variável auxiliar com |𝒲| ≤ |𝒳| + 1, e f: 𝒴 × 𝒲 → 𝒳̂ é o decoder.

**Caso especial D=0 (lossless)**: R_s(0) = H(X|Y) — recupera o Slepian-Wolf theorem.

**Resultado surpreendente**: R_s(D) < R(D) em geral — conhecer Y no decoder permite reduzir a taxa. E **a side information não precisa ser transmitida** — o encoder não precisa conhecê-la, apenas a distribuição conjunta p(x,y).

**Caso Gaussiano** (§14.9, Remark): Para X ~ N(0,σ²), Y correlação ρ com X, squared error D:

R_s(D) = max{0, ½ log(σ²(1−ρ²)/D)}

Comparado com R(D) = ½ log(σ²/D) sem side information — a redução é exatamente ½ log(1/(1−ρ²)).

### General Network Theory e Problemas Abertos (§14.10)

Cover & Thomas (1991) listam como abertos:
1. Capacity region do broadcast channel geral (não degradado)
2. Two-way channel (Bell 1961) — capacity region não conhecida para o caso geral
3. General relay network capacity
4. Multi-terminal rate distortion (inclui CEO problem, introduzido por Berger 1996 após esta edição)

## Interpretação

### Slepian-Wolf como fundação do CEO problem

⚠️ Interpretação nossa — não está nesta forma em Cover & Thomas 1st ed.

O CEO problem (Berger 1996) generaliza Wyner-Ziv para **L observadores paralelos**:
- L agentes observam X₁,...,X_L (versões ruidosas de θ)
- Cada agente codifica independentemente à taxa Rᵢ
- Um CEO reconstrói θ com distortion D

Slepian-Wolf é o caso especial com L=2 e D=0 (lossless). Wyner-Ziv é o caso L=1 com side information. O CEO problem combina ambos: lossy + múltiplos agentes + encoders independentes.

### MAC como coordenação

⚠️ Interpretação nossa.

O MAC formaliza o "uplink" de um sistema multi-agente: múltiplos agentes reportam ao CEO. A capacity region do MAC diz qual combinação de taxas é teoricamente alcançável. Na prática de KB com múltiplos compiladores, o MAC é o modelo de "quanto cada compilador pode contribuir sem degradar a reconstrução total."

## Verificação adversarial

**Claim mais fraco:** Slepian-Wolf assume decoder **comum** para X e Y. Se o decoder não tem acesso a Y, a taxa mínima sobe para H(X). A hipótese de decoder comum é não-trivial em sistemas distribuídos.

**O que o textbook NÃO diz:**
- Não cobre o CEO problem (pós-1991)
- Broadcast channel geral (não degradado) sem solução em 1991
- Não discute overhead de coordenação prático para alinhar codebooks distribuídos

**Simplificações:** A prova do Slepian-Wolf usa codebooks aleatórios — não dá construção eficiente. Implementações práticas (Turbo codes, LDPC) vieram depois.

**Prior work:**
- Slepian & Wolf (1973) — paper original
- Wyner & Ziv (1976) — rate distortion with side information
- Cover & Thomas (1991) é o tratamento textbook unificando esses resultados

## Quality Gate
- [x] Wikilinks tipados: `derivedFrom: [[rate-distortion-theory]]`; `prerequisiteOf: [[team-decision-theory]] ON CEO problem foundations`; `partOf: [[information-theory-shannon]] ON extensão multi-terminal`
- [x] Instance→class: exemplos numéricos identificados como "Gaussian MAC com parâmetros específicos" ou "Bernoulli(½)"; não generalizados
- [x] Meta-KB separado: MAC como modelo de multi-compilador KB em ## Interpretação, não em ## Conteúdo
- [x] Resumo calibrado: "sem solução geral conhecida para redes arbitrárias" preservado

## Níveis epistêmicos

### Descrição (verificado)
- MAC capacity region (Theorem §14.3) — provado no textbook
- Slepian-Wolf theorem (Theorem 14.4.1) — provado no textbook
- Wyner-Ziv (Theorem 14.9.1) — provado no textbook
- Gaussian examples — derivados no textbook
- Broadcast channel capacity region (degraded case) — provado no textbook

### Interpretação (nossa aplicação)
- Slepian-Wolf como fundação do CEO problem — conexão nossa, não está em Cover & Thomas 1st ed.
- MAC como modelo de coordenação multi-compilador — não está no textbook

### Especulação
- (nenhuma)

## Conexões

- derivedFrom: [[rate-distortion-theory]] — Slepian-Wolf e Wyner-Ziv generalizam R(D) para múltiplas fontes
- partOf: [[information-theory-shannon]] ON "extensão multi-terminal da teoria original de Shannon"
- prerequisiteOf: [[team-decision-theory]] ON "CEO problem usa rate distortion multi-terminal; foundations aqui"

## Fontes

- [Cover & Thomas — Elements of Information Theory, Ch. 14](../../raw/papers/cover-thomas-elements-information-theory.md) — MAC capacity region, Slepian-Wolf Theorem 14.4.1, Wyner-Ziv Theorem 14.9.1, broadcast/relay channel
