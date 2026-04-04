---
title: "CEO Problem (Berger 1996; Courtade & Weissman 2014)"
sources:
  - path: raw/papers/courtade-ceo-problem.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [information-theory, multi-terminal, rate-distortion, distributed-coding, ceo, multi-agent]
source_quality: high
interpretation_confidence: high
quarantine: false
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
provenance: source
---

## Resumo

O CEO problem (Berger, Zhang & Viswanathan 1996; Courtade & Weissman 2014) formaliza a reconstrução de uma fonte X por um CEO que recebe relatórios comprimidos de L agentes independentes, cada um observando uma versão ruidosa de X. Sob logarithmic loss, Courtade & Weissman provam que o Berger-Tung inner bound é tight — primeira caracterização exata da rate distortion region para fontes finitas gerais. Aplicações: machine learning multi-view, coordenação de agentes com comunicação limitada.

## Conteúdo

### Configuração formal (2-encoder, §3, Courtade & Weissman 2014)

**Fonte e observações**:
- X: fonte com distribuição p(x), alfabeto finito
- Y₁, Y₂: observações dos agentes, com distribuição condicional p(y₁|x), p(y₂|x)
- Estrutura Markov: Y₁ ↔ X ↔ Y₂ (as observações são condicionalmente independentes dado X)

**Codificação independente**:
- Encoder 1: g₁: Y₁ⁿ → {1,...,M₁} a taxa R₁ ≥ (1/n)log M₁
- Encoder 2: g₂: Y₂ⁿ → {1,...,M₂} a taxa R₂ ≥ (1/n)log M₂
- Os encoders operam **sem comunicação entre si**

**Decoder central (CEO)**:
- ψ: {1,...,M₁} × {1,...,M₂} → X̂ⁿ
- Objetivo: minimizar Ed(Xⁿ, X̂ⁿ) ≤ D

**Logarithmic loss distortion**:
d(x, q) = log(1/q(x))

onde q é a estimativa do decoder (distribuição sobre X). A distortion esperada é a entropia condicional H(X|Û₁,Û₂) — "quanto incerteza resta sobre X após os relatórios".

### Inner bound: Berger-Tung (Proposition 1)

A region RDᵢ_CEO é alcançável se existe distribuição conjunta p(x)p(y₁|x)p(y₂|x)p(u₁|y₁,q)p(u₂|y₂,q)p(q) satisfazendo:

```
R₁ ≥ I(Y₁; U₁ | U₂, Q)
R₂ ≥ I(Y₂; U₂ | U₁, Q)
R₁ + R₂ ≥ I(U₁,U₂; Y₁,Y₂ | Q)
D ≥ H(X | U₁, U₂, Q)
```

onde U₁, U₂ são variáveis auxiliares (quantizações de Y₁, Y₂), Q é time-sharing.

**Mecanismo (quantize-and-bin)**: cada encoder quantiza sua observação Yᵢ → Uᵢ, depois usa Slepian-Wolf coding para transmitir Uᵢ ao CEO. O CEO combina U₁, U₂ para estimar X.

### Converse: Theorem 2 (Courtade & Weissman 2014)

**Resultado principal**: Para qualquer código com (R₁, R₂, D) estritamente alcançável:

```
∑_{i∈A} Rᵢ ≥ I(X; U_A | U_{Aᶜ}, Q) + H(X | U₁, U₂, Q)
         = H(X | U_{Aᶜ}, Q) - D    para todo A ⊆ {1,2}
```

**Corolário**: RDᵢ_CEO = RD_CEO (inner bound é tight).

Esta é a primeira caracterização completa da rate distortion region para fontes finitas arbitrárias sob distortion não trivial. Para Gaussiano quadrático, conhecida desde Viswanath et al. (2008).

### Por que logarithmic loss é especial?

Para distortion geral, o CEO problem permanece em aberto (open problem desde Berger 1996). Logarithmic loss funciona porque:
- d(x, q) = log(1/q(x)) implica distortion ótima Ed(X, q̂) = H(X|U₁,U₂,Q) — entropia condicional
- Esta forma de entropia permite o converse usando a desigualdade de Fano generalizada
- Berger-Tung é tight porque a distortion já é uma mutual information expression

### m-encoder generalização

Para m agentes (§3, Courtade & Weissman): a região satisfaz para todo S ⊆ {1,...,m}:

```
∑_{i∈S} Rᵢ ≥ H(X | U_{Sᶜ}, Q) - D
```

Caso especial m=1: recupera rate distortion clássico R(D) = I(Y; U) com H(X|U) = D.

### Aplicações

**Machine learning** (§3.4, Courtade & Weissman):
- Xⱼ = classe do objeto j, Y₁ⱼ, Y₂ⱼ = atributos observáveis por dois classificadores
- Log loss = cross-entropy de classificação
- CEO = ensemble que combina as estimativas soft de cada classificador
- Rate region determina quando comunicação adicional melhora a classificação

**Horse racing com side information** (§3, Courtade & Weissman):
- CEO faz decisões de investimento (apostas) com outcomes Xⁿ
- Y₁, Y₂ = relatórios de analistas independentes a taxas limitadas
- Log loss = doubling rate da riqueza

## Interpretação

### CEO problem como caso geral da família

⚠️ Conexões nossas — explícitas no paper de Courtade como motivação, mas não apresentadas como "família KB".

| Modelo | Configuração | Distortion | Solução |
|--------|-------------|------------|---------|
| Rate distortion (Shannon 1959) | 1 encoder, 1 decoder | geral | R(D) = min I(Y;U) |
| Wyner-Ziv (1976) | 1 encoder, decoder com side info | geral | R_s(D) = min [I(Y;W) - I(Z;W)] |
| Slepian-Wolf (1973) | 2 encoders, lossless | Hamming D=0 | R₁+R₂ ≥ H(Y₁,Y₂) |
| CEO problem (Berger 1996) | L encoders independentes | geral | **open** |
| CEO + log loss (Courtade 2014) | L encoders independentes | log loss | **solved** |

### Conexão com multi-agent KB

⚠️ Interpretação nossa — não está em Courtade.

Se a KB usa múltiplos LLMs como compiladores:
- X = conhecimento "verdadeiro" a capturar
- Yᵢ = perspectiva ruidosa do compilador i (V(compiler_i) < V(domain))
- Rᵢ = taxa de informação do compilador i (tokens de output)
- D = distortion residual do wiki compilado

O CEO problem diz que a rate region ótima requer coordenação implícita via quantize-and-bin — os compiladores não precisam se comunicar entre si, mas a arquitetura de aggregation (CEO decoder) deve ser projetada para extrair a informação complementar de cada compilador.

## Verificação adversarial

**Claim mais fraco:** O resultado é restrito a logarithmic loss — para Hamming distortion geral, o CEO problem ainda está em aberto. Não existe solução geral para distortion arbitrária.

**O que o paper NÃO diz:**
- Não resolve o CEO problem para squared error distortion (só o caso Gaussiano foi resolvido antes)
- Não discute como implementar o Berger-Tung em sistemas práticos (codebooks, delay)
- Não trata de CEO problem com mais de 2 encoders em detalhes (m-encoder é generalização direta)

**Simplificações:** O modelo assume Markov: Y₁ ↔ X ↔ Y₂. Se as observações são correlacionadas diretamente (não apenas via X), o modelo muda.

**Prior work citado:**
- Berger, Zhang, Viswanathan (1996) — paper original do CEO problem (paywalled)
- Wagner, Tavildar, Viswanath (2008) — solução para Gaussian quadratic CEO
- Slepian & Wolf (1973), Wyner & Ziv (1976) — fundamentos

## Quality Gate
- [x] Wikilinks tipados: `derivedFrom: [[rate-distortion-theory]]`; `derivedFrom: [[network-information-theory]] ON Slepian-Wolf como building block`; `prerequisiteOf: [[team-decision-theory]] ON multi-agent information processing`
- [x] Instance→class: resultado de Courtade 2014 é sob log loss específico; generalização para Hamming explicitamente marcada como open
- [x] Meta-KB separado: conexão com multi-compiler KB em ## Interpretação, não em ## Conteúdo
- [x] Resumo calibrado: "primeira caracterização exata" qualificado com "fontes finitas gerais sob log loss"

## Níveis epistêmicos

### Descrição (verificado)
- Configuração formal: Markov chain Y₁↔X↔Y₂, encoders independentes — do paper
- Berger-Tung inner bound — Proposition 1 no paper
- Theorem 2 (converse) — provado no paper
- Tight sob log loss: primeiro resultado geral (Courtade, 2014)
- m-encoder generalização — Corolário do paper

### Interpretação (nossa aplicação)
- Tabela família de modelos — conexão nossa, motivada pelo paper
- Conexão com multi-compiler KB — não está no paper

### Especulação
- (nenhuma)

## Conexões

- derivedFrom: [[rate-distortion-theory]] — CEO generaliza R(D) para L encoders independentes
- derivedFrom: [[network-information-theory]] ON "Slepian-Wolf (lossless) é caso especial D=0 do CEO"
- complementsAt: [[team-decision-theory]] ON "CEO = framework de informação para o problema que Ho & Chu modela como decisão"
- complementsAt: [[partial-information-decomposition]] ON "PID diagnóstica unique/shared/synergistic de dois compiladores; CEO determina a taxa ótima para recuperá-las"

## Fontes

- [Courtade & Weissman (2014) — Multiterminal Source Coding under Logarithmic Loss](../../raw/papers/courtade-ceo-problem.md) — CEO problem definition, Berger-Tung inner bound, Theorem 2 (converse), tight result for log loss, applications to ML
