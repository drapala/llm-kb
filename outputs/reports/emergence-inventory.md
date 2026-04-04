---
created: 2026-04-04
type: inventory-report
scope: wiki/concepts/*.md
total_articles: 52
---

# Provenance Inventory — wiki/concepts/

**Retrofit executado em:** 2026-04-04
**Escopo:** todos os 52 artigos em `wiki/concepts/` (excluindo `_index*.md`)

## Resumo Executivo

| Provenance | Count | % |
|---|---|---|
| source | 28 | 54% |
| synthesis | 11 | 21% |
| emergence | 13 | 25% |
| **Total** | **52** | **100%** |

**Emergências por connection_type:**
- EMERGE-DE: 10
- ANÁLOGO-A: 2
- INSTANCIA: 1

**Emergências por pearl_level:**
- L2: 12
- L1: 1

---

## Artigos: source (28)

| Artigo | Nota |
|---|---|
| autonomous-research-agents | 1 fonte raw/ principal |
| bibliometrics | 1 fonte raw/ principal |
| bradford-law-scattering | 1 fonte raw/ principal |
| causal-reasoning-pearl | 1 fonte; tabela de corpus é interpretação menor (ver ambiguous.md) |
| ceo-problem | 1 fonte raw/ principal |
| complementary-learning-systems | 1 fonte raw/ principal |
| complexity-emergence | 1 fonte jornalística; conceitos de Waldrop/Santa Fe |
| complexity-stability-tradeoff | 1 fonte raw/ principal (May 1972) |
| episodic-semantic-memory | 1 fonte raw/ principal (Tulving 2002) |
| epistemic-maintenance | 1 fonte raw/ principal (quarentinado) |
| falsificationism-demarcation | 2 fontes concordantes sobre Popper |
| heuristics-and-biases | 1 fonte raw/ principal |
| hybrid-search | 1 fonte raw/ principal |
| information-bottleneck | 1 fonte raw/ principal |
| information-theory-shannon | 1 fonte raw/ principal (Shannon 1948; quarentinado) |
| judgment-aggregation | 1 fonte raw/ principal |
| memory-consolidation | 1 fonte raw/ principal |
| network-information-theory | 1 fonte raw/ principal |
| obsidian-agent-workflow | 1 fonte raw/ principal |
| pac-bayes-bounds | 1 fonte raw/ principal |
| partial-information-decomposition | 1 fonte raw/ principal |
| prospect-theory | 1 fonte raw/ principal (K&T 1979) |
| rate-distortion-theory | 1 fonte raw/ principal |
| rational-inattention | 1 fonte raw/ principal |
| resource-competition-coexistence | 1 fonte raw/ principal (Tilman 1994) |
| scientific-research-programmes | 2 fontes concordantes sobre Lakatos |
| team-decision-theory | 1 fonte raw/ principal |
| viable-system-model-beer | 1 fonte raw/ principal |

---

## Artigos: synthesis (11)

| Artigo | Fontes wiki combinadas |
|---|---|
| agent-memory-architectures | context-management, tension-resolution, memory-consolidation, hybrid-search, retrieval-augmented-generation, self-improving-agents, raptor-vs-flat-retrieval |
| context-management | memory-consolidation, hybrid-search, raptor-vs-flat-retrieval, kb-architecture-patterns, agent-memory-architectures |
| llm-as-judge | self-improving-agents, kb-architecture-patterns, context-management, memory-consolidation, tension-resolution |
| llm-knowledge-base | retrieval-augmented-generation, hybrid-search, memory-consolidation, autonomous-research-agents, kb-architecture-patterns, obsidian-agent-workflow, autonomous-kb-failure-modes |
| multi-agent-orchestration | autonomous-research-agents, context-management, memory-consolidation |
| question-taxonomy | tension-resolution, curation-anti-bias, autonomous-kb-failure-modes, llm-as-judge, kb-architecture-patterns, reflexion-weighted-knowledge-graphs |
| retrieval-augmented-generation | llm-knowledge-base, hybrid-search, context-management, raptor-vs-flat-retrieval, kb-architecture-patterns |
| self-improving-agents | memory-consolidation, kb-architecture-patterns, autonomous-research-agents, context-management, llm-as-judge, agent-memory-architectures, multi-agent-orchestration |
| social-choice-aggregation | judgment-aggregation, prospect-theory |
| tension-resolution | self-improving-agents, llm-as-judge, kb-architecture-patterns, memory-consolidation |
| zipf-law-power-laws | bradford-law-scattering, information-theory-shannon, rational-inattention |

---

## Artigos: emergence (13)

| Artigo | Par originador | connection_type | pearl_level |
|---|---|---|---|
| autonomous-kb-failure-modes | llm-as-judge + self-improving-agents | EMERGE-DE | L2 |
| curation-anti-bias | llm-as-judge + autonomous-kb-failure-modes | EMERGE-DE | L2 |
| fast-frugal-heuristics | self-improving-agents + autonomous-kb-failure-modes | ANÁLOGO-A | L2 |
| formal-ontology-for-kbs | question-taxonomy + kb-architecture-patterns | EMERGE-DE | L2 |
| groupthink-and-cascades | autonomous-kb-failure-modes + curation-anti-bias | INSTANCIA | L2 |
| immune-inspired-credit-assignment | reflexion-weighted-knowledge-graphs + causal-reasoning-pearl | ANÁLOGO-A | L1 |
| kb-architecture-patterns | llm-knowledge-base + context-management | EMERGE-DE | L2 |
| predictive-processing | self-improving-agents + llm-as-judge | EMERGE-DE | L2 |
| raptor-vs-flat-retrieval | retrieval-augmented-generation + context-management | EMERGE-DE | L2 |
| reflexion-weighted-knowledge-graphs | agent-memory-architectures + self-improving-agents | EMERGE-DE | L2 |
| requisite-variety | autonomous-kb-failure-modes + curation-anti-bias | EMERGE-DE | L2 |
| stigmergic-coordination | formal-ontology-for-kbs + multi-agent-orchestration | EMERGE-DE | L2 |
| variety-gap-analysis | requisite-variety + autonomous-kb-failure-modes | EMERGE-DE | L2 |

---

## Hubs de emergência (artigos que originam mais emergências)

| Artigo | Quantas emergências originadas |
|---|---|
| autonomous-kb-failure-modes | 4 (curation-anti-bias, fast-frugal-heuristics, groupthink-and-cascades, requisite-variety, variety-gap-analysis) |
| self-improving-agents | 4 (autonomous-kb-failure-modes, fast-frugal-heuristics, predictive-processing, reflexion-weighted-knowledge-graphs) |
| llm-as-judge | 3 (autonomous-kb-failure-modes, curation-anti-bias, predictive-processing) |
| context-management | 2 (kb-architecture-patterns, raptor-vs-flat-retrieval) |
| curation-anti-bias | 2 (groupthink-and-cascades, requisite-variety) |

---

## Casos ambíguos

Ver: `outputs/inbox/provenance-ambiguous.md`

- **causal-reasoning-pearl** — classificado source (conservador); tabela de corpus contém interpretação emergente menor
- **stigmergic-coordination** — classificado emergence; Grassé descrito fielmente, mas aplicação a wikis LLM é totalmente nova
- **variety-gap-analysis** — classificado emergence; usa Ashby mas o objeto (esta KB) não existe na fonte

---

## Observações estruturais

1. **25% de emergência é sinal saudável.** Indica que /ask está gerando conexões genuínas, não apenas sumarizando fontes.
2. **EMERGE-DE domina (77% das emergências).** Padrão esperado: novos conceitos emergem de interseção de dois conceitos existentes. ANÁLOGO-A (analogias laterais) e INSTANCIA são raros mas válidos.
3. **L2 domina (92% das emergências).** Intervenção/mecanismo. Só 1 emergência ficou em L1 (associação): immune-inspired-credit-assignment, classificado conservadoramente por ser altamente especulativo.
4. **Cluster de failure modes é o mais fértil.** autonomous-kb-failure-modes + curation-anti-bias + self-improving-agents geraram 6 dos 13 artigos de emergência. Isso é o núcleo intelectual desta KB.
5. **Zone 3 ingerida como source pura.** Todos os 12 papers Zone 3 (ecologia, linguística, filosofia, neurociência) foram classificados source — certo pelo design: /ingest descreve o campo, /ask gera conexões.
