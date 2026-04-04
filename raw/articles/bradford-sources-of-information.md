---
source: Bradford, S.C. (1934). Sources of information on specific subjects. Engineering: An Illustrated Weekly Journal, 137, 85-86.
author: Samuel Clement Bradford
date: 1934-01-26
type: article
quality: primary
stance: neutral
---

# Bradford — Sources of Information on Specific Subjects (1934)

## Nota de proveniência

⚠️ O original é 2 páginas (Engineering 137:85-86, 1934). PDF não acessível livremente.
O paper foi republicado com introdução de B.C. Brookes em Journal of Information Science 10(4):176-180, 1985.
Conteúdo abaixo derivado de: Wikipedia/Bradford's_law, Bradford (1953) Documentation (livro que elabora a lei), e múltiplas citações acadêmicas verificando a formulação matemática.

---

## A Lei (formulação verbal original)

Bradford observou, ao analisar bibliografias de lubrificação e geofísica aplicada na Science Museum Library, que:

"Se periódicos científicos são ordenados por número decrescente de artigos sobre um dado assunto, podem ser divididos num núcleo de periódicos mais produtivos e em vários grupos ou zonas, cada grupo contendo aproximadamente o mesmo número de artigos que o núcleo."

**Relação entre zonas:**
Se o núcleo tem `p` periódicos, as zonas sucessivas têm aproximadamente `p·n`, `p·n²`, `p·n³`... periódicos, onde `n` é o multiplicador de Bradford (empírico, varia por campo).

**Notação padrão (1:n:n²):**
Núcleo : Zona 1 : Zona 2 = 1 : n : n²

Para artigos uniformemente distribuídos em 3 zonas (1/3 cada):
- Zona core: pequeno conjunto de periódicos produtivos
- Zona 1: ~n× mais periódicos, mesma quantidade de artigos
- Zona 2: ~n²× mais periódicos, mesma quantidade de artigos

## Dados empíricos originais

Bradford analisou dois corpora:
1. **Lubrificação** (campo de sua especialidade como chefe do Science Museum Library)
2. **Geofísica aplicada**

Em ambos, encontrou o padrão de dispersão exponencial: rendimentos decrescentes ao buscar literatura em periódicos periféricos.

## Implicações práticas (articuladas no paper original)

1. Para qualquer campo especializado, existe um núcleo pequeno de periódicos que concentra a maioria da literatura relevante
2. Buscar exaustivamente a literatura "de cauda" tem retorno decrescente previsível
3. Bibliotecas podem otimizar aquisições identificando o núcleo de Bradford

## Conexão com Zipf e Lotka

Bradford (1934) é contemporâneo a Zipf (1935, word frequencies) e posterior a Lotka (1926, author productivity).
Os três descrevem distribuições de lei de potência em fenômenos bibliométricos:
- **Lotka**: produtividade de autores ~ 1/n²
- **Bradford**: dispersão de periódicos ~ zonas logarítmicas
- **Zipf**: frequência de palavras ~ 1/rank

Todos são instâncias da distribuição de Pareto / lei de potência aplicada a sistemas informativos.

## Relação Bradford-Beer (⚠️ nossa interpretação)

A lei de Bradford descreve V(domínio) em termos de cobertura de fontes:
- Zona core = fontes de alto V(compiler) ∩ V(domain)
- Zonas periféricas = fontes onde V(compiler) pode ser insuficiente para processamento fiel
- Implication: para maximizar V(wiki), deve-se cobrir a zona core de cada dimensão do domínio

Esta conexão não está em Bradford — é aplicação da KB.

## O que o paper NÃO diz

- Não propõe explicação causal da lei (é empírica/descritiva)
- Não discute information theory (Shannon é 14 anos posterior)
- Não trata de LLMs nem de qualquer sistema de recuperação automática
- A formulação 1:n:n² é aproximação — Bradford 1934 usa linguagem mais verbal
