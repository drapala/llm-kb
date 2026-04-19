# Q7 — Bradford scattering aplicado a antipattern mining

**Query**: a quota de 25% challenging aplica? Core-scatter na registry?

## Resposta

### Framework

Bradford 1934: fontes ordenadas por produtividade dividem-se em **core + zonas com razão 1:n:n²**. Cada zona contribui ~1/3 do sinal total, mas exige n× mais fontes para cobrir.

Aplicado a antipattern registry do claude-pipeline (`.pipeline/antipatterns.jsonl`, prompt 11): antipadrões são "fontes" de sinal de falha. **Pergunta**: a distribuição desses sinais segue Bradford?

### O que esperar empiricamente

Em SWE agents, failures típicas concentram-se em pequeno núcleo:
- **Core**: ~5-10 antipadrões cobrem ~33% dos failures (test tautológico, allowed_files sem guard, import de API inexistente, assert True, etc.)
- **Zona 1** (~n=3-5): ~15-30 antipadrões cobrem próximos 33% (mocks que escondem divergência real, off-by-one em list comprehensions, async gather onde threadpool é melhor)
- **Zona 2** (~n²=9-25): ~45-100+ antipadrões cobrem último 33%

Isto informa duas coisas críticas ausentes do prompt 11:
1. **Priorização de mining**: antipadrão que já aparece em 2+ tickets é core (alta produtividade de matching futuro) — esses justificam LLM expensive mining. Antipadrão único é zona 2 — custo de registrar pode exceder valor.
2. **Decay calibrado por zona**: prompt 11 menciona "feedback loop + decay". Decay deveria ser **mais rápido em zona 2** (antipadrões raros envelhecem fast) e **mais lento em core** (antipadrões comuns persistem relevantes).

### Sobre a quota de 25% challenging

A quota 25% é específica do **ingest da KB metaxon** — garante que fontes adversariais não fiquem abafadas por confirmatórias. Bradford é ortogonal ao eixo stance (confirming/challenging). Então a resposta direta:

**25% challenging NÃO se aplica 1:1 a antipattern mining** porque:
- Antipadrão é por definição "sinal de falha" — não tem eixo stance natural.
- O que seria o análogo correto: **diversidade de categoria de falha**, não quota binária.

Mas há um análogo útil: **evitar convergência para zona core monocromática**. Se 80% dos antipadrões minerados são de categoria "test quality", o registry é viesado e perderá novos failures categoricamente novos (supply chain, race condition, etc.). Como o ingest metaxon impõe quota Zone3/Zone2 ≥ 0.8 para diversidade, o registry deveria impor **categoria diversity score**:

> Nenhuma categoria de antipadrão deve ocupar > 40% da registry (ativos).

Isso é Bradford-consistente: força alocação em zonas além do core.

### Adaptação empírica da KB para o pipeline

O [[bradford-law-scattering]] tem observação importante (linhas 100-106):
> "Bradford multiplier empírico desta KB: n ≈ 0.5 — corpus invertido em relação ao Bradford maduro"

Ou seja: KBs jovens/desenvolvendo têm distribuição invertida (zona 2 maior que zona 1). **Antipattern registry jovem do pipeline terá mesma patologia**: maioria dos antipadrões será zona 2 (singular) porque poucos tickets foram rodados. Implicação:
- **Não confiar em core detection cedo** — o aparente "core" nos primeiros 50 tickets pode ser artefato de amostra pequena.
- **Threshold de promoção para active** (prompt 11: "mesmo padrão em 2 tickets") é baixo demais em registry jovem. Subir para 3-4 até registry atingir N=200+.

### Core-scatter no registry: sinal de saúde do pipeline

Bradford multiplier `n` é proxy de maturidade:
- n < 1 (distribuição invertida): registry imaturo, muitos casos singulares
- n ≈ 2-3: registry maduro, poucos casos core dominam
- n > 5: registry sobre-agregado, pouca granularidade (antipadrões genéricos demais)

**Isto muda o prompt 11**: adicionar métrica `bradford_multiplier` ao registry. Expor em dashboard. Disparar alerta se n > 5 (antipadrões genéricos demais) ou se n < 0.5 por mais de N tickets (imaturidade persistente → registry não está aprendendo).

### Circuit breaker análogo no retrieval

[[bradford-law-scattering]] observa: circuit breaker do /ask é Bradford aplicado a retrieval — para quando busca além do core tem retorno decrescente. Aplicado ao `antipattern_retriever.py`:

> Se top-k antipadrões retornados têm `match_score` abaixo de threshold θ, NÃO injete nenhum no planner (é preferível contexto limpo a contexto ruidoso).

Hoje o retriever provavelmente sempre retorna top-k — isso é zona 2 sendo injetada mesmo quando core não cobre. Sinal falso aumenta, planner contamina.

**Isto muda o prompt 11 e 19**: threshold mínimo de match_score; se nenhum antipadrão passa, não injete — reporte "no antipattern match" ao planner.

### Refinamento epistêmico crucial

A KB tem achado importante (linha 106):
> "Zona 3 tem quarentena alta quando /ingest extrapola; tem quarentena baixa quando descreve o campo nos seus próprios termos."

Tradução ao pipeline: **antipattern mining falha quando o miner extrapola** (infere antipadrão a partir de um único failure genérico). Tem sucesso quando **registra fielmente o padrão concreto observado em múltiplos tickets**.

**Isto muda o prompt 11**: o miner (Haiku por default) tem tendência à síntese prematura. Adicionar check: antipadrão só vira active se tiver `concrete_evidence_count >= 2` (instâncias específicas, não inferência).

### Conexão com Q4 (tree search)

Best-of-N sampling (Q4) gera múltiplas trajetórias — algumas com failures novos. Bradford-consistente: rodar best-of-N em N=3 gera **mais evidência para zonas 1-2** porque failures raras têm chance maior de aparecer com sampling diverso. Isso é mecanismo natural de **enrichment do registry sem aumentar ticket count**.

### Sobre a quota challenging revisitada

Há um caso onde 25% challenging **é relevante**: o **antipattern ↔ heuristic positive duality** (lessons são positive patterns, antipatterns são negative). Se o registry positivo e negativo não mantêm proporção balanceada, o planner recebe contexto enviesado:
- 90% positive lessons, 10% antipatterns → planner otimista, perde cautela
- 90% antipatterns, 10% lessons → planner excessivamente cauteloso

**Isto muda o prompt 16** (loadable skills, unifica lessons+antipatterns+skills): manter quota de **pelo menos 20% antipattern** no retrieval context, mesmo que matching score das lessons seja maior. Análogo ao Bradford forçando diversity de zonas.

## Fontes wiki
- `[L0]` [[bradford-law-scattering]] — lei 1:n:n², scattering types, evidência empírica em bibliometrics
- `[L1]` [[bibliometrics]] — contexto Lotka-Bradford-Zipf
- `[L1]` [[curation-anti-bias]] — source diversity como contra-ponto

## Fontes raw
- `raw/articles/bradford-sources-of-information.md` via wiki

## Confiança
**Média.** Framework Bradford transfere estruturalmente mas falta validação empírica: precisa registry com ≥200 antipadrões para verificar se n converge para 2-3. Claims sobre categoria diversity e threshold são extrapolação principiada mas não testadas.

## Gaps
- Literatura sobre **failure taxonomy em SWE agents** não indexada. Seria útil referência empírica de distribuição de failure modes.
- MAST taxonomy (arXiv 2503.13657) já está na ingest_queue_priority — **deve ser priorizada**, traz 14 failure modes em 1600+ traces (dados de Bradford-teste).

## Mudanças no roadmap
- **Prompt 11** (antipattern registry): (a) métrica `bradford_multiplier` + alerta; (b) categoria diversity score (nenhuma categoria > 40%); (c) promoção para active exige `concrete_evidence_count >= 2` (não inferência); (d) threshold mínimo de match_score no retriever (silent se nenhum passa).
- **Prompt 16** (unified skills): quota de 20% antipattern no retrieval context cross-registry.
- **Prompt 19** (RAG): threshold mínimo genérico para todos os retrievers (antipattern, lesson, skill) — retorno silencioso se core não cobre.
- **Prompt 6** (eval): métrica de **registry bradford health** longitudinal.

## Sugestão de ingestão (já na fila — priorizar)
- MAST taxonomy Why Do Multi-Agent LLM Systems Fail? (arXiv 2503.13657) — 14 failure modes, 1600+ traces, direct evidence para distribuição Bradford de failures.

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Instrumentar Bradford no registry aumenta utilidade de retrieval e reduz ruído contextual.

**Experiment**
- Implementar `bradford_multiplier`, `category_diversity_score` e `match_score_threshold`.
- Rodar 4 semanas em produção controlada e comparar contra baseline histórico.
- Medir: `retrieval_useful_rate`, `planner_overload_events`, `false_positive_antipattern_hits`.

**Success Metric**
- `retrieval_useful_rate` +20% ou melhor.
- `planner_overload_events` -25% ou melhor.
- Nenhuma categoria >40% por mais de 2 janelas consecutivas.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| Lei de Bradford (1:n:n^2) | Measured (bibliometrics) | Teoria/observação consolidada. |
| "n ~2-3 indica maturidade no registry" | Projected | Heurística operacional para este domínio. |
| "threshold de match melhora planner quality" | Projected | Requer telemetria longitudinal local. |
