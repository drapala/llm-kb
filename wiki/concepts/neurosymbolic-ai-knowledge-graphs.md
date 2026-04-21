---
title: "Neurosymbolic AI para Raciocínio em Knowledge Graphs — Taxonomia e Fundamentos"
sources:
  - path: raw/papers/delong-2024-neurosymbolic-kg-survey.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/herron-2025-owl-neurosymbolic-stub.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/acm-2024-neural-symbolic-kg-reasoning-stub.md
    type: paper
    quality: secondary
    stance: confirming
  - path: raw/papers/hitzler-sarker-2023-compendium-neurosymbolic.md
    type: paper
    quality: secondary
    stance: confirming
  - path: raw/papers/colelough-2025-neurosymbolic-systematic-review.md
    type: paper
    quality: secondary
    stance: confirming
created: 2026-04-11
updated: 2026-04-11
tags: [neurosymbolic, knowledge-graphs, OWL, reasoning, taxonomy, embeddings, rule-learning]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
status: quarantined
quarantine_date: 2026-04-11
quarantine_reason: "Gate 3 invalidou: AMIE classificado como NeSy mas é método puramente simbólico (Gemini). Fixes aplicados: AMIE removido dos exemplos NeSy; OWL 'enforça' → 'verifica'; semântica open-world explicitada; distribuição Colelough qualificada como bibliométrica não-intencional."
synthesis_sources:
  - raw/papers/delong-2024-neurosymbolic-kg-survey.md
  - raw/papers/herron-2025-owl-neurosymbolic-stub.md
  - raw/papers/colelough-2025-neurosymbolic-systematic-review.md
---

## Resumo
DeLong et al. (IEEE TNNLS 2024, arXiv 2302.07200) estabelece a taxonomia fundacional: 3 categorias de sistemas neurossimbólicos para KGs — logically-informed embeddings, embeddings com logical constraints, e rule learning. Herron et al. (2025) especifica como OWL ontologies governam KGs com semânticas de inferência formais. Colelough et al. (2025, 167/1.428 papers) documenta o estado da arte: learning/inference domina (63%), explainability e meta-cognition são os gaps principais (28% e 5%).

## Conteúdo

### O que é Neurosymbolic AI

Neurosymbolic AI (NeSy) combina dois paradigmas complementares:
- **Simbólico:** regras lógicas, ontologias, raciocínio formal — interpretável, verificável, mas brittle com dados incompletos/ruidosos
- **Neural:** redes neurais, embeddings, aprendizado estatístico — robusto, escalável, mas caixa-preta

O ponto cego de cada abordagem:
| Abordagem | Vantagem | Limitação |
|-----------|----------|-----------|
| Simbólica pura (clássica) | Interpretável, auditável, garantias lógicas | Difícil de escalar, knowledge engineering manual custoso; abordagens clássicas não lidam com incerteza (note: frameworks probabilísticos simbólicos como ProbLog e MLNs estendem isso) |
| Neural pura | Escalável, aprende de dados, robusta a ruído | Inexplicável, não enforcement de regras, sem garantias |
| **Neurossimbólica** | Interpretabilidade + performance + conhecimento especialista | Mais complexidade de design |

### Taxonomia DeLong 2024 — As 3 Categorias

**Categoria 1: Logically-Informed Embedding Approaches**

O processo de geração de embeddings incorpora informação lógica. Exemplos:
- Embeddings de entidades treinados com penalidade por violação de regras lógicas conhecidas
- Espaços de embedding onde relações lógicas (transitiva, simétrica) são preservadas geometricamente
- Loss functions que incluem termo de consistência lógica

**Categoria 2: Embedding Approaches with Logical Constraints**

Embeddings aprendidos separadamente, depois constraints lógicos aplicados no momento de inferência:
- Embedding modelo prediz score para tripla (entidade1, relação, entidade2)
- Reasoner simbólico filtra ou reranqueia outputs por consistência com regras conhecidas
- Dois componentes trainados independentemente, combinados no deployment

**Categoria 3: Rule Learning Approaches**

Sistemas que descobrem regras simbólicas a partir de padrões nos dados do KG:
- Aprende regras como "se A→B e B→C, então A→C" a partir de exemplos
- Mais interpretável (regras são legíveis por humano)
- Mais generalista (não depende de regras pré-definidas)
- Exemplos neurossimbólicos: Neural-LP, RNNLogic (nota: AMIE é método puramente simbólico de rule mining, não NeSy)

### OWL como Camada de Governança (Herron 2025)

OWL (Web Ontology Language) adiciona uma camada de semantics formal ao KG:

**O que OWL especifica:**
- Axiomas de domínio/range de propriedades, class membership (sob semântica open-world)
- Disjointness e cardinality constraints para inferência lógica
- Class subsumption e property chains para derivar novo conhecimento

Nota: OWL usa open-world assumption — domain/range são axiomas inferenciais, não validação de dados. Para constraint enforcement em sentido de banco de dados, SHACL é a tecnologia adequada.

**Reasoners OWL** (Pellet, HermiT, FaCT++):
1. Inferem novo conhecimento implícito no KG
2. Verificam consistência lógica (não enforçam como um banco de dados — checam post-hoc)
3. Detectam contradições na base de conhecimento

**Inferência como predição:** com design de ontologia adequado, o reasoner não apenas valida conhecimento existente — pode prever o que deveria ser verdade dado o modelo de domínio.

### Estado do Campo (Colelough 2025, PRISMA, N=167/1428)

| Área de pesquisa | % dos papers |
|-----------------|-------------|
| Learning and inference | **63%** |
| Knowledge representation | **44%** |
| Logic and reasoning | **35%** |
| Explainability and trustworthiness | **28%** |
| Meta-Cognition | **5%** |

**Distribuição observada em Colelough 2025:** learning/inference domina (63%), enquanto explainability (28%) e meta-cognition (5%) têm menor representação neste corpus. Nota: explainability é frequentemente citada como motivação fundacional para sistemas NeSy (a lacuna do black-box neural). A proporção menor pode refletir dificuldade de publicação nesta área, não desinteresse do campo. (⚠️ interpretação do compilador: os dados mostram distribuição bibliométrica, não intenção do campo).

### Hitzler & Sarker 2023 — O Compendium

Livro-texto de referência do campo. Cobre:
- Definições e taxonomias canônicas
- Integração de description logics (DLs) com redes neurais
- Knowledge representation híbrida
- Aplicações em compliance, medicina, robótica

## Verificação adversarial

**Claims mais fracos:** (1) A taxonomia de 3 categorias de DeLong é uma proposta — não é a única possível; outras surveys usam taxonomias diferentes; (2) Herron 2025 é STUB baseado em descrição do usuário — não verificado independentemente; (3) a ideia de "inferência como predição" de Herron é interessante mas requer design cuidadoso de ontologia — não é automático.

**O que os papers não dizem:** (1) DeLong não quantifica diferença de performance entre as 3 categorias em benchmarks específicos; (2) Colelough não decompõe quais domínios de aplicação são mais representados; (3) OWL reasoners têm problemas de escalabilidade em KGs grandes que os papers não discutem extensamente.

## Quality Gate
- [x] Wikilinks tipados: sem wikilinks externos necessários neste artigo
- [x] Instance→class: taxonomia atribuída a DeLong 2024; % atribuídos a Colelough 2025 (167/1428)
- [x] Meta-KB separado: sem referências a design da KB no Conteúdo
- [x] Resumo calibrado: inclui que Herron e ACM são STUB

## Conexões
- agent-memory-architectures partOf neurosymbolic-ai-knowledge-graphs (KG como memória externa estruturada por ontologia)

## Fontes
- [DeLong et al. 2024](../../raw/papers/delong-2024-neurosymbolic-kg-survey.md) — taxonomia 3 categorias, IEEE TNNLS, arXiv 2302.07200
- [Herron et al. 2025](../../raw/papers/herron-2025-owl-neurosymbolic-stub.md) — OWL governance, inference semantics, inferência como predição (STUB)
- [ACM TKDD 2024](../../raw/papers/acm-2024-neural-symbolic-kg-reasoning-stub.md) — KG completion, link prediction (STUB)
- [Hitzler & Sarker 2023](../../raw/papers/hitzler-sarker-2023-compendium-neurosymbolic.md) — livro-texto fundacional (STUB)
- [Colelough et al. 2025](../../raw/papers/colelough-2025-neurosymbolic-systematic-review.md) — 167/1428, PRISMA, estado do campo
