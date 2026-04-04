# Modelo Ontológico da KB

Derivado de BFO, DOLCE, OWL 2, Relation Ontology, e Noy 101.
Orientação: DOLCE (cognitiva) com relações RO (formais).

---

## Primitivos (categorias fundamentais)

| Categoria | Definição | Exemplos na KB |
|-----------|----------|---------------|
| **Continuant** | Persiste inteiramente em cada momento | Wiki articles, concepts, raw/ sources |
| **Occurrent** | Desdobra-se no tempo, tem partes temporais | /ask sessions, /review cycles, /ingest runs |
| **Quality** | Propriedade de um continuant | source_quality, interpretation_confidence, stance |
| **Disposition** | Pode ou não se manifestar | Tensões documentadas (podem resolver ou não) |
| **Role** | Função conferida externamente, depende de contexto | Mesmo artigo serve como "referência factual" ou "hipótese especulativa" dependendo do /ask |

**Regra:** artigos wiki são continuants. Commands (/ingest, /review) são occurrents. Não misturar descrição de "o que X é" com "como o processo Y funciona" na mesma seção.

---

## Taxonomia de relações tipadas

| Tipo | Direção | Propriedades | Exemplo |
|------|---------|-------------|---------|
| **partOf** | A → B (A é parte de B) | Transitiva, assimétrica | memory-consolidation partOf agent-memory-architectures |
| **contradicts** | A ↔ B | Simétrica | retrieval-augmented-generation contradicts llm-knowledge-base ON "RAG at small scale" |
| **derivedFrom** | A → B (A derivado de B) | Assimétrica | reflexion-weighted-kg derivedFrom memgpt, reflexion, hipporag |
| **validates** | A → B (A valida B) | Assimétrica | raptor-paper validates _index.md pattern (parcialmente) |
| **supersedes** | A → B (A substitui B) | Assimétrica, temporal | hindsight supersedes reflexion-weighted-kg (parcialmente) |
| **instanceOf** | A → B (A é instância de B) | Assimétrica | this-KB instanceOf kb-architecture-patterns.Pattern1 |
| **complementsAt** | A ↔ B | Simétrica, condicional | QMD complementsAt raptor (não supersede — são alternativos) |

**Formato no artigo wiki:**
```markdown
## Conexões
- partOf: [[agent-memory-architectures]] — consolidation is one memory pattern
- contradicts: [[retrieval-augmented-generation]] ON "need for RAG at small scale"
- derivedFrom: [[memgpt]], [[reflexion]], [[hipporag]] — synthesized from 3 papers
```

---

## Hierarquia de abstração

| Nível | O que contém | Regra |
|-------|-------------|-------|
| **META** | Claims sobre ESTA KB, seus commands, seus processos | Só em ## Interpretação ou ## Aplicação à KB |
| **DOMÍNIO** | Claims sobre o campo (agent memory, retrieval, etc.) | Em ## Conteúdo, com citação raw/ |
| **INSTÂNCIA** | Dados de papers específicos (benchmarks, thresholds) | Sempre qualificados: modelo, dataset, condições |

**Regras de mixing:**
- META claims em ## Conteúdo = VIOLAÇÃO (mover pra Interpretação)
- INSTÂNCIA claims sem qualificador = VIOLAÇÃO (adicionar modelo+dataset)
- DOMÍNIO claims sem citação raw/ = VIOLAÇÃO (adicionar fonte ou mover pra Interpretação)

---

## Regras de consistência (checklist)

Todo artigo novo DEVE passar:

- [ ] **Cada wikilink tem tipo** (partOf, contradicts, derivedFrom, validates, supersedes, instanceOf, complementsAt)
- [ ] **Cada claim numérico tem qualificador** (modelo, dataset, condições)
- [ ] **Zero menções a "nosso KB" / "/ask" / "/ingest" em ## Conteúdo** (só em Interpretação)
- [ ] **Resumo reflete caveats** do corpo (não mais confiante que ## Gaps + ## Especulação)
- [ ] **Continuant vs occurrent consistente** (artigo sobre entidade não descreve processo, e vice-versa)
- [ ] **Relações bidirecionais são simétricas** (se A contradicts B, B contradicts A)
- [ ] **Relações transitivas são consistentes** (se A partOf B partOf C, then A partOf C)

---

## Perguntas habilitadas (não eram formuláveis antes)

1. "O que é parte de X?" — traverse partOf links
2. "O que contradiz X?" — traverse contradicts links (simétricos)
3. "De onde X deriva?" — traverse derivedFrom chain
4. "O que X substitui?" — traverse supersedes links
5. "Quais instâncias de Pattern Y existem?" — traverse instanceOf links
6. "Se eu remover artigo X, o que quebra?" — traverse partOf + derivedFrom dependents
7. "A cadeia A→B→C é transitivamente válida?" — check partOf transitivity

## Perguntas proibidas (malformadas ontologicamente)

1. "X é melhor que Y?" — binário, ignora contexto. Reformular: "Sob quais condições X supera Y?"
2. "X prova Y?" — verificação impossível (Popper). Reformular: "X corrobora Y? O que refutaria?"
3. "Nosso KB faz X?" — meta-claim apresentado como domínio. Reformular separando nível.
