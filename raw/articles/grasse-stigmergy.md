---
source: Grassé, P.P. (1959). La reconstruction du nid et les coordinations interindividuelles. Insectes Sociaux, 6(1), 41-80.
author: Pierre-Paul Grassé
date: 1959-01-01
type: article
quality: primary
stance: neutral
---

# Grassé — Stigmergy (1959)

## Fonte primária

Grassé, P.P. (1959). La reconstruction du nid et les coordinations interindividuelles chez Bellicositermes natalensis et Cubitermes sp. La théorie de la Stigmergie: Essai d'interprétation du comportement des termites constructeurs. Insectes Sociaux, 6(1), 41-80.

## Conceito central

Coordenação indireta de comportamento via modificações no ambiente — não via comunicação direta entre agentes. O ambiente modificado serve como memória externa e como sinal para próximas ações.

Etimologia: stigma (marca) + ergon (trabalho) = "o trabalho guia o trabalho."

## Mecanismo original (térmitas)

Grassé observou que térmitas construtoras coordenam a construção do ninho sem comunicação direta entre si. O mecanismo:

1. Uma térmita deposita uma bolota de terra com feromônio num local
2. O depósito (modificação do ambiente) ATRAI outras térmitas
3. Outras térmitas depositam mais material no mesmo local
4. A estrutura crescente guia mais deposições
5. Emergem pilares, arcos, câmaras — sem plano central

O PRODUTO do trabalho guia o PRÓXIMO trabalho. Nenhuma térmita "sabe" o plano do ninho. O plano emerge da interação entre agentes e ambiente modificado.

## Tipos de stigmergy

**Sematectônica:** modificação FÍSICA do ambiente que guia comportamento.
- Térmitas: depósitos de terra atraem mais depósitos
- Construção de pilares: quando dois pilares ficam próximos, térmitas começam a conectá-los (arco emerge)

**Baseada em marcas (sign-based):** sinais deixados no ambiente sem modificação física permanente.
- Formigas: feromônios em trilhas. Trail decays → path optimizes over time.
- Intensidade do sinal = qualidade do recurso (mais feromônio = caminho mais usado = recurso melhor)

## Extensões documentadas

- **Wikipedia:** edições anteriores guiam edições futuras. O artigo modificado É o sinal para o próximo editor. Nenhum coordenador central.
- **Open source:** commits guiam próximos commits. O estado do código é o sinal.
- **Mercados:** preços passados guiam decisões futuras (Adam Smith's "invisible hand" é stigmergy econômica). [verificar — esta interpretação é de Heylighen, 2016, não de Grassé]
- **Ant Colony Optimization** (Dorigo, 1992): algoritmo de otimização inspirado em stigmergy. Agentes artificiais depositam "feromônios" em grafos. Caminhos melhores acumulam mais feromônio.

## O que Grassé NÃO afirma

- Não requer consciência nos agentes — térmitas não "sabem" o que fazem
- Não requer comunicação direta — coordenação é VIA AMBIENTE
- Não requer coordenador central — plano emerge da interação
- Não requer que agentes sejam idênticos — diferentes agentes podem responder ao mesmo sinal de formas diferentes

## Limitações

- Assume que ambiente PRESERVA sinais — em ambientes instáveis, sinais decaem antes de serem lidos. [verificar — Grassé discute decay de feromônios?]
- Não especifica como agentes INTERPRETAM sinais — a semântica do sinal é implícita na resposta do agente, não explícita
- Em sistemas com muitos tipos de sinal (alta V de sinais), agentes podem não distinguir entre eles — "noise" stigmérgico [verificar — esta limitação é de Theraulaz & Bonabeau (1999), não de Grassé]

> [editorial — não é de Grassé]
> A KB como sistema stigmérgico:
> - /ingest = agente modifica ambiente (wiki)
> - Wikilinks tipados = feromônios diferenciados (sinais tipados)
> - /ask = agente lê ambiente modificado e age
> - /review = agente re-modifica baseado em leitura
> Predição: a qualidade dos "feromônios" (tipos de wikilink)
> determina a qualidade da coordenação entre sessões.
> Wikilinks planos = feromônios sem tipo = coordenação fraca.
> Wikilinks tipados = feromônios diferenciados = coordenação forte.
> Status: analogia L1. Não testada formalmente.
