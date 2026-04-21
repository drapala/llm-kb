---
title: "Espectro de Estruturas de Conhecimento e o Problema McOntology"
sources:
  - path: raw/blogs/knowledge-graph-guys-what-is-ontology.md
    type: article
    quality: secondary
    stance: confirming
created: 2026-04-12
updated: 2026-04-12
tags: [ontology, knowledge-graph, schema, taxonomy, epistemics, mconto, meta-kb, structured-knowledge, inference, axioms]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
---

## Resumo

Quatro níveis de estrutura de conhecimento — lista, schema, taxonomia, ontologia — diferem em capacidade inferencial, não apenas em complexidade. O "McOntology problem" (Tony Seale, The Knowledge Graph Guys): quando uma estrutura inferior é chamada de ontologia, as decisões arquiteturais que seguem são inválidas — e a ferramenta é culpada pelo fracasso da rotulagem errada.

## Conteúdo

### O espectro

| Nível | O que define | Capacidade | Assumption |
|---|---|---|---|
| **Lista** | Enumeração flat | Lookup | — |
| **Schema** | Forma dos dados: campos, tipos, restrições | Validação | Closed World |
| **Taxonomia** | Hierarquia + classificação, relações is-a | Classificação | Closed World |
| **Ontologia** | Axiomas + description logics | Validação + **Inferência** | Open World |

A distinção crítica é entre schema e ontologia:

**Closed World Assumption (schema):** o que não está declarado explicitamente não existe. Válido para validação de dados estruturados, inútil para domínios incompletos ou evolutivos.

**Open World Assumption (ontologia):** a ausência de uma declaração não implica falsidade. O sistema trabalha com informação parcial e deriva novos fatos via axiomas.

### Inferência como propriedade definidora

Em um schema, propriedades descrevem campos — a estrutura determina o que existe. Em uma ontologia, propriedades flutuam livremente e **inferem tipo**:

> "If it walks like a duck and quacks like a duck, it's a duck."

A afirmação "tem valorAcrescido > 0" pode inferir `tipoDocumento = TermoAditivo` sem declaração explícita — desde que o axioma esteja formalizado em description logic.

Herança lógica: "Médico é um tipo de Pessoa; Pessoa é um tipo de Animal." Um sistema com esses axiomas deriva que médicos têm taxa respiratória sem ser dito explicitamente. Um schema com as mesmas tabelas não deriva nada — só valida.

### McOntology (Seale)

O padrão de degradação terminológica observado por Tony Seale (The Knowledge Graph Guys, LinkedIn, ~2026):

> Ontologia dilui para buzzword. Taxonomia é chamada de ontologia. Schema é chamado de ontologia. JSON com labels é chamado de ontologia. A palavra passa a significar tudo — e portanto nada.

Análogo ao que aconteceu com "Agile": o termo se popularizou, o rigor que o tornava útil foi descartado, e as falhas passaram a ser atribuídas à ferramenta em vez de ao uso degradado dela.

**Consequência prática:** um sistema construído sobre uma "ontologia" que é na verdade um schema não terá capacidade inferencial. Quando falhar por esse motivo, o diagnóstico errado será "ontologias não funcionam" — não "usamos o nível errado de estrutura".

### Mínimo viável, não máximo formal

A implicação prática não é "toda estrutura precisa ser OWL com description logics completas". É:

1. **Nomear corretamente o que você tem** — um YAML com tags é um schema, não uma ontologia.
2. **Escolher o nível mínimo que entrega a capacidade que o sistema precisa**.
3. **Não atribuir a uma estrutura capacidades que ela não tem** — um schema não faz inferência, independente de como é chamado.

Se o sistema precisa de validação: schema é suficiente. Se precisa de classificação hierárquica: taxonomia. Se precisa de inferência a partir de informação parcial: ontologia com axiomas.

## Interpretação

⚠️ Interpretação do compilador.

### Aplicação ao llm-kb

O `ontology/core.py` do metaxon é descrito como "ontologia" no CLAUDE.md e nos artigos de meta-KB. Checklist honesto:

| Critério | Status |
|---|---|
| Hierarquia de classes (is-a) | ✅ `KnowledgeArtifact → Claim`, etc. |
| Campos tipados e restrições | ✅ dataclasses com mode='before' |
| Open World Assumption | ❌ Python dataclasses são closed world |
| Axiomas formais | ❌ não há description logics |
| Capacidade inferencial | ❌ não deriva novos fatos |

**Veredito:** `ontology/core.py` é um **schema com hierarquia de tipos** — ou seja, uma taxonomia sofisticada. Não é uma ontologia no sentido técnico de Seale/W3C. Isso não é necessariamente um problema — se o sistema não precisa de inferência, um schema é suficiente e mais fácil de manter. O problema seria assumir capacidade inferencial que não existe.

A pergunta relevante: **o metaxon precisa de inferência?** Se a resposta for "não — só validação e classificação", `core.py` está no nível certo e o nome é o único problema (McOntology em sentido benign). Se a resposta for "sim — derivar relações entre artigos a partir de axiomas", há um gap de capacidade real.

## Conexões

- [[meta-ontology-metaxon]] ON "core.py como 'ontologia' — checklist McOntology sugere que é schema+hierarquia, não ontologia inferencial"
- [[formal-ontology-for-kbs]] ON "gaps estruturais: wikilinks não tipados, sem hierarchy formal — instâncias do problema McOntology"
- [[upper-ontology-for-kbs]] ON "BFO/DOLCE como upper ontology real — confrontar com o que core.py efetivamente implementa"
- [[anti-patterns-epistemic-ml]] ON "McOntology é instância do mesmo mecanismo: nome errado → decisões arquiteturais inválidas → falha atribuída à ferramenta"

## Fontes

- [What is an Ontology? — The Knowledge Graph Guys](https://www.knowledge-graph-guys.com/blog/what-is-an-ontology) — schema vs ontologia; Open/Closed World; description logics; duck example
- Tony Seale, LinkedIn post ~2026 — McOntology problem; dilution pattern; analogia com Agile ⚠️ não acessível diretamente, referenciado via Marques da Silva (2026)
