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
- **b2g-economics**: market-for-lemons, corruption-audits-brazil, platform-economics, jobs-to-be-done, procurement-renegotiation, incentive-theory-procurement, electoral-accountability-corruption, audit-deterrence-corruption, corruption-dynamics, audit-risk-rent-extraction, procurement-contract-design, procurement-manipulation-signals, procurement-variety-gap

Para cada par de artigos de **clusters diferentes** que **não se citam** (verificar seção `## Conexões` de cada um):

Pergunta: "Estes dois artigos têm estrutura causal análoga?"
Critério: mesma relação causa→efeito em domínios diferentes.
**Não é similaridade temática — é isomorfismo estrutural.**

Leia artigos em lotes de 10. Não tente ler todos de uma vez. Circuit breaker: se ≥15 pares sem isomorfismo detectado consecutivamente, pare e reporte o que encontrou até aqui.

## Passo 2 — Gera candidatos de conexão

Para cada par com isomorfismo detectado, gera um bloco estruturado:

```
CONEXÃO CANDIDATA:
- Artigo A: [nome] — mecanismo: [X causa Y via Z]
- Artigo B: [nome] — mecanismo: [análogo em domínio diferente]
- Tipo de relação: ANÁLOGO-A | INSTANCIA | EMERGE-DE
- Pearl level: L1 | L2 | L3
- Pergunta falsificável: [a pergunta que testaria a conexão]
- Espúrio check: baixo | médio | alto
  Razão: [por que a conexão pode ser aparente, não real — confounding, superficial similarity, etc.]
- Custo de verificação: baixo | médio | alto
  Razão: [o que seria necessário para confirmar — /ask interno, dados externos, paper novo, experimento]
- Pergunta /ask recomendada:
  "[Artigo A] propõe [mecanismo X]. [Artigo B] propõe [mecanismo análogo Y].
  O que emerge da combinação que nenhum dos dois articula individualmente?"
```

### Critérios de espúrio check

**Baixo risco de espúrio:** mecanismo A e mecanismo B são estruturalmente idênticos com variáveis mapeáveis 1:1, domínios independentes, conexão não-óbvia.

**Médio risco:** similaridade plausível mas mecanismos têm assimetrias importantes; ou os domínios não são tão independentes quanto parecem.

**Alto risco:** conexão baseada em metáfora superficial; variáveis não mapeiam limpamente; ou ambos os artigos poderiam citar um terceiro artigo que os conecta (conexão não-emergente).

### Critérios de custo de verificação

**Baixo:** um /ask cross-domain resolve (sem dados externos, sem ingestão nova).

**Médio:** requer ingestão de 1-2 fontes adicionais OU análise de dados existentes.

**Alto:** requer dados externos não disponíveis atualmente, experimento, ou paper que ainda não existe no raw/.

## Passo 2b — Oracle externo (cross-model validation)

Para cada par candidato gerado no Passo 2, chama o oracle externo antes de ordenar:

```bash
python3 scripts/cross-model-challenge.py --mode auto << 'EOF'
{
  "article_a": {
    "title": "[título]",
    "summary": "[resumo 2-3 frases]",
    "mechanism": "[X causa Y via Z]"
  },
  "article_b": {
    "title": "[título]",
    "summary": "[resumo 2-3 frases]",
    "mechanism": "[mecanismo análogo]"
  },
  "proposed_connection": "[descrição da conexão proposta]",
  "connection_type": "ANÁLOGO-A | INSTANCIA | EMERGE-DE",
  "pearl_level": "L1 | L2 | L3"
}
EOF
```

**Resultado do oracle:**
- `score >= 7` (GENUINE) → par avança para Passo 3
- `score < 7` (SUPERFICIAL) → par vai para `outputs/reports/emerge-rejected-YYYY-MM-DD.md`
  com reasoning do oracle. Não entra em `emerge_top_pairs`.

**Se o script falhar** (sem chave de API, sem internet):
- Registra aviso: "Oracle indisponível — todos os pares avançam sem validação externa"
- Adiciona flag `oracle_validated: false` em cada par
- Continua para Passo 3

**Propósito:** o oracle externo é o Pilar 1 do autoresearch-reliability-triad aplicado ao /emerge.
Sem ele, o mesmo sistema que escreveu os artigos está avaliando a qualidade das conexões entre eles.
GPT-4o e Gemini têm viés diferente do Claude — concordância entre modelos é sinal mais forte que
concordância interna.

## Passo 3 — Ordena candidatos

Ordena apenas pares que passaram no oracle externo (ou todos se oracle indisponível),
por prioridade de verificação (não por impacto contextual — isso é tarefa do /prioritize):

1. **Pearl level mais alto** (L2 > L1 > L3)
2. **Espúrio mais baixo** (baixo antes de alto)
3. **Custo mais baixo** (baixo antes de alto)
4. Desempate: artigos com `provenance: emergence` já existente (conexão já emergiu uma vez — mais fértil)

## Passo 4 — Identifica quarentenas desbloqueáveis

Verifica artigos com `quarantine: true`. Para cada um: a conexão identificada seria uma nova instância do claim quarentenado? Se sim, lista como "desbloqueável se conexão confirmada."

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

## Candidatos (ordenados por prioridade de verificação)

### 1. [Artigo A] × [Artigo B]
[bloco estruturado do Passo 2]

### 2. ...

## Artigos em quarentena desbloqueáveis
[lista artigos quarentena que seriam promovidos se conexão confirmada]

## Estado do grafo
[N artigos por cluster, N conexões cross-cluster existentes vs. candidatas]
```

## O que NÃO faz

- Não avalia impacto contextual (Zelox, research, produto) — isso é /prioritize
- Não cria wikilinks automaticamente
- Não modifica artigos
- Não ingere fontes
- Apenas mapeia e ordena por verificabilidade — humano decide o que conectar

## Filosofia

Conexões cross-domain emergem no /ask, não no /ingest.
O /emerge é o catalisador: encontra onde o /ask deveria ser rodado a seguir.
A ordenação é por custo de verificação e qualidade epistêmica — sem contexto externo.
Contexto (Zelox, research) é injetado pelo /prioritize sobre o output do /emerge.

## Após /emerge completar

Atualize `outputs/state/kb-state.yaml`:
1. `emerge_queue: []` ← reset
2. `emerge_top_pairs: [novos pares encontrados]` ← lista dos top pares identificados
3. `last_updated` com data atual
