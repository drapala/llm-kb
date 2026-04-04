---
created: 2026-04-04
type: ambiguous-classification-log
---

# Provenance Ambiguous Cases

Casos onde a classificação de provenance não foi óbvia.
Regra aplicada: conservadora (source > synthesis > emergence).

---

## causal-reasoning-pearl.md

**Classificado como:** `source`

**Tensão:** O artigo contém uma tabela de classificação de corpus por nível causal (L1/L2/L3) aplicada a textos específicos desta KB (NLP applications, social sciences, medicine, etc.). Essa tabela não existe em nenhuma fonte raw/ — é uma aplicação interpretativa de Pearl ao domínio de KBs.

**Por que não `emergence`:** A tabela é uma *aplicação ilustrativa* do framework de Pearl, não um conceito novo. Qualquer leitor de Pearl poderia produzi-la. O conceito central (níveis causais de Pearl) vem 100% de uma fonte raw/ primária.

**Decisão final:** source — o conteúdo factual domina; a tabela é interpretação menor que não justifica reclassificação.

**Alternativa considerada:** `emergence` com `pair: [causal-reasoning-pearl, kb-architecture-patterns]` e `connection_type: INSTANCIA`. Rejeitada pela regra conservadora.

---

## stigmergic-coordination.md

**Classificado como:** `emergence`

**Tensão:** O artigo descreve fielmente Grassé (1959) no conteúdo factual. Mas a aplicação de stigmergy a wikis LLM e multi-agent orchestration é totalmente ausente de Grassé — não existe na fonte raw/.

**Por que não `source`:** A seção de conexões e interpretações aplica o conceito de forma que a fonte não suporta. O artigo propõe um conceito ausente em qualquer fonte individual.

**Decisão final:** emergence — par [formal-ontology-for-kbs, multi-agent-orchestration].

---

## variety-gap-analysis.md

**Classificado como:** `emergence`

**Tensão:** Usa Ashby's Law of Requisite Variety como fundamento, mas o objeto de análise (esta KB) não existe em Ashby. Todo o "gap analysis" é aplicação nova.

**Por que não `synthesis`:** Não combina múltiplas fontes raw/ — usa uma fonte + aplica ao objeto KB. Isso é emergence, não synthesis.

**Decisão final:** emergence — par [requisite-variety, autonomous-kb-failure-modes].
