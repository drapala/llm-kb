# /emerge

Descobre conexões latentes entre artigos que ainda não se citam mas têm estrutura causal análoga.
Ativado quando Bradford Zone3/Zone2 ≈ 1.0 (pausa de ingestão).

## Quando rodar

- Após Bradford Zone3/Zone2 cruzar 0.9
- Antes de qualquer nova ingestão lateral
- Após /promote de hub importante

## Passo 1 — Mapeamento de artigos sem conexão cross-cluster

Leia `wiki/_index.md` para listar todos os artigos. Classifique cada um por cluster:

- **core-ai-ml**: context-management, memory-consolidation, multi-agent-orchestration, autonomous-research-agents, hybrid-search, raptor-vs-flat-retrieval, agent-memory-architectures, self-improving-agents, tension-resolution, llm-as-judge, reflexion-weighted-knowledge-graphs, immune-inspired-credit-assignment, groupthink-and-cascades, autonomous-kb-failure-modes, curation-anti-bias, question-taxonomy, retrieval-augmented-generation, llm-knowledge-base, kb-architecture-patterns, obsidian-agent-workflow
- **meta-kb**: epistemic-maintenance, variety-gap-analysis, bibliometrics, bradford-law-scattering, formal-ontology-for-kbs
- **info-theory**: information-theory-shannon, information-bottleneck, partial-information-decomposition, rate-distortion-theory, network-information-theory, ceo-problem, rational-inattention, pac-bayes-bounds
- **cognitivo**: heuristics-and-biases, prospect-theory, fast-frugal-heuristics, episodic-semantic-memory, complementary-learning-systems, predictive-processing
- **sistemas**: requisite-variety, viable-system-model-beer, complexity-emergence, complexity-stability-tradeoff, stigmergic-coordination, resource-competition-coexistence
- **epistemológico**: falsificationism-demarcation, scientific-research-programmes, causal-reasoning-pearl, judgment-aggregation, social-choice-aggregation, zipf-law-power-laws, team-decision-theory

Para cada par de artigos de **clusters diferentes** que **não se citam** (verificar seção `## Conexões` de cada um):

Pergunta: "Estes dois artigos têm estrutura causal análoga?"
Critério: mesma relação causa→efeito em domínios diferentes.
**Não é similaridade temática — é isomorfismo estrutural.**

Leia artigos em lotes de 10. Não tente ler todos de uma vez. Circuit breaker: se ≥15 pares sem isomorfismo detectado consecutivamente, pare e reporte o que encontrou até aqui.

## Passo 2 — Gera candidatos de conexão

Para cada par com isomorfismo detectado, gera:

```
CONEXÃO CANDIDATA:
- Artigo A: [nome] — mecanismo: [X causa Y via Z]
- Artigo B: [nome] — mecanismo: [análogo em domínio diferente]
- Tipo de relação: ANÁLOGO-A | INSTANCIA | EMERGE-DE
- Nível Pearl: L1 (associação) | L2 (intervenção) | L3 (contrafactual)
- Pergunta falsificável que testaria a conexão: [pergunta]
- Valor de ingerir fonte que conecta os dois: [alto/médio/baixo + justificativa]
```

## Passo 3 — Prioriza por ROI

Ordena candidatos por:
1. Nível Pearl mais alto (L2 > L1)
2. Artigos com `provenance: emergence` já existente (conexão já emergiu uma vez — mais fértil)
3. Conexão que habilitaria promoção de artigo em quarentena (verifica frontmatter `quarantine: true`)

## Passo 4 — Gera /ask recomendados

Para os top 3 candidatos, gera o /ask que exploraria a conexão sem ingestão nova:

```
"[Artigo A] propõe [mecanismo X]. [Artigo B] propõe [mecanismo análogo Y].
O que emerge da combinação que nenhum dos dois articula individualmente?"
```

## Passo 5 — Salva

Salva em `outputs/reports/emerge-YYYY-MM-DD.md`:

```markdown
---
date: YYYY-MM-DD
---

## Resumo
- N pares analisados
- N conexões candidatas encontradas
- N artigos com provenance: emergence no corpus atual

## Top 3 Candidatos

### 1. [Artigo A] × [Artigo B]
[conteúdo estruturado conforme Passo 2]

/ask recomendado:
> "[prompt gerado]"

### 2. ...

### 3. ...

## Artigos em quarentena desbloqueáveis
[lista artigos quarentena que seriam promovidos se conexão for confirmada]

## Estado do grafo
[N artigos por cluster, N conexões cross-cluster existentes vs. candidatas]
```

## O que NÃO faz

- Não cria wikilinks automaticamente
- Não modifica artigos
- Não ingere fontes
- Apenas mapeia e sugere — humano decide o que conectar

## Filosofia

Conexões cross-domain emergem no /ask, não no /ingest.
O /emerge é o catalisador: encontra onde o /ask deveria ser rodado a seguir.
O ponto de equilíbrio Bradford é exatamente quando você tem fontes suficientes
de domínios diferentes para que conexões não-óbvias existam — mas ainda não
foram descobertas porque o /ask não foi rodado nos pares certos.

## Após /emerge completar

Atualize `outputs/state/kb-state.yaml`:
1. `promoted_since_last_emerge: []` ← reset
2. `emerge_top_pairs: [novos pares encontrados]` ← lista dos top 3 pares identificados
3. `last_updated` com data atual
