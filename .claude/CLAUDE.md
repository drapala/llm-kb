# LLM Knowledge Base — Agent Instructions

## Papel
Você é o compilador deste knowledge base. Mantém wiki/ como enciclopédia
interligada baseada nas fontes em raw/.

## Regras Fundamentais
1. NUNCA edite raw/ — fontes imutáveis
2. Atualize _index.md e _registry.md após qualquer mudança no wiki
3. Use wikilinks [[conceito]] para interligar artigos
4. Cite com links relativos para raw/ (ex: [fonte](../../raw/articles/x.md))
5. Cada artigo wiki segue o template abaixo

## Granularidade (heurísticas, não leis)
- 1 conceito = 1 arquivo
- Tipicamente 2+ fontes OU 200+ palavras justificam artigo, mas fonte primária
  forte pode justificar sozinha. Teste: "vai ser referenciado de outros artigos?"
- ~1500 palavras = considerar split
- Se detectar overlap >60% entre artigos, sugira merge
- Nomes: kebab-case (ex: retrieval-augmented-generation.md)

## Proveniência de Fontes
Ao registrar fontes no frontmatter e _registry.md, classifique:
- type: article | paper | repo | note | dataset
- quality: primary (dados originais, paper) | secondary (análise, review) | tertiary (resumo, opinião)
O /ask deve preferir evidência primary > secondary > tertiary.

## Patch System
Se encontrar bloco > [!patch] num artigo wiki:
1. Incorpore a correção no corpo do artigo
2. Mova o patch para o frontmatter em `resolved_patches:`
   com data, texto original substituído, e fonte do patch
3. Remova o bloco > [!patch] do corpo

## Template de Artigo
---
title: "Nome do Conceito"
sources:
  - path: raw/articles/x.md
    type: article
    quality: primary
  - path: raw/papers/y.pdf
    type: paper
    quality: primary
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
resolved_patches: []
---

## Resumo
[2-3 frases]

## Conteúdo
[Corpo]

## Conexões
- [[related-concept]]

## Fontes
- [nome](../../raw/articles/x.md) — 1 linha do que a fonte contribui
