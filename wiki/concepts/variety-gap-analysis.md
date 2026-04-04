---
title: "Variety Gap Analysis (Esta KB)"
sources:
  - path: raw/articles/ashby-requisite-variety.md
    type: article
    quality: primary
created: 2026-04-04
updated: 2026-04-04
tags: [meta-kb, variety, gap-analysis, ashby, original-insight]
source_quality: medium
interpretation_confidence: low
resolved_patches:
  - date: 2026-04-04
    patch: "Beer/VSM gap preenchido (viable-system-model-beer.md). Shannon parcialmente preenchido (quarentena). Também ingeridos: information-bottleneck, partial-information-decomposition, team-decision-theory, bibliometrics, bradford-law-scattering."
  - date: 2026-04-04
    patch: "Ingestão lateral: 12 papers seminais em 6 domínios Zone 3. Gaps cognitiva, ecologia, linguística, filosofia, neurociência agora ~0. Predição Ashby C (lateral > same-domain) recebeu suporte empírico parcial. Bradford Zone3/Zone2 subiu de 0.5 → 1.05."
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-04
---

## Resumo

⚠️ Aplicação especulativa de Ashby à própria KB. V(compiler) = 1 LLM fixo. Gap alto nas dimensões laterais (cibernética, biologia, complexidade, cognitiva). Gaps mais críticos: Shannon ausente (V(LLM) inoperacionalizável em bits) e Beer/VSM ausente (multi-regulator coordination não modelada). Os 4 artigos quarentados são exatamente os de maior distância do domínio AI/ML — evidência de que V(R) é mais fraco onde a cobertura mais importa.

## Conteúdo

### Framework aplicado

V(O) ≥ V(D) / V(R) — para compilação perfeita V(O) = 1 → exige V(R) ≥ V(D).

| Variable | Nesta KB |
|----------|---------|
| V(D) | Variedade do domínio que a KB pretende cobrir |
| V(R) | 1 LLM + processo + fontes ingeridas |
| V(O) | Fidelidade de compilação (alvo: 1) |

### Gap por dimensão

| Dimensão | V(Domínio) | V(Compilador) | Gap | Atualização |
|---|---|---|---|---|
| AI/ML técnico | Alto | Alto | ~0 | — |
| Metodologia de avaliação | Médio | Médio | Pequeno | — |
| Teoria de controle / cibernética | Médio | Médio-baixo | **Médio** | Ashby promovido |
| Ciência cognitiva (Friston) | Médio | Baixo | Baixo | Friston promovido + Tulving/McClelland ingeridos |
| Complexidade / emergência | Médio | Baixo | Baixo | Waldrop promovido + May (formal) ingerido |
| Psicologia social (Janis) | Médio | Médio | Médio | — |
| Bounded rationality (K&T, Gigerenzer) | Médio | Médio | ~0 | K&T ×2 ingeridos |
| Social choice (Arrow, Black) | Alto | Baixo | ~0 | Arrow + Black ingeridos |
| Ecologia de comunidades | Alto | Baixo | ~0 | May + Tilman ingeridos |
| Linguística computacional | Alto | Baixo | Baixo | Ferrer-i-Cancho + Piantadosi ingeridos |
| Filosofia da ciência | Médio | Médio | ~0 | Popper + Lakatos ingeridos |
| Neurociência cognitiva | Alto | Baixo | ~0 | Tulving + McClelland ingeridos |
| Biologia / sistemas imunes | Médio | Baixo | **Alto** | — |
| Teoria da organização (Beer/VSM) | Médio | Médio | Pequeno | Beer ingerido |
| Filosofia / ontologia formal | Médio | Médio | Pequeno | — |
| Teoria da informação (Shannon) | Médio | Baixo | **Médio** | Shannon ingerido mas em quarentena |
| Stigmergia / coordenação | Médio | Baixo | Baixo | Grassé promovido |

### Compressão como proxy de V gap

64 fontes → 27 artigos = 58% compressão. Por construção V(wiki) < V(raw). ⚠️ Predição D (Ashby quarentena): error floor ≈ V(raw) − V(wiki) mensurável por diversidade de embeddings — não testado.

### O floor irreducível atual

V(R) é um único LLM. ⚠️ Processo adicional (9 comandos, 6 hooks) opera dentro de V(R) fixo — não reduz o floor. O único fix é aumentar V(R): múltiplos compiladores ou fontes de domínios com V(compiler) não saturado.

## Interpretação

### Sinal mais limpo desta análise

Os 4 artigos quarentados (Ashby, Stigmergy, Complexity, Friston) são 100% de domínios laterais ao AI/ML. Isso é evidência, não coincidência: o compilador tem V mais alto no domínio AI/ML → interpreta fontes AI/ML com alta fidelidade → fontes laterais geram mais especulação → entram em quarentena. A quarentena é o sinal de V insuficiente no mapa.

### Por que Shannon é o gap mais crítico

Sem formalismo de teoria da informação, V(LLM) não tem unidade de medida. A Predição D (error floor mensurável) permanece não operacionalizável. Shannon (1948) forneceria:
- Definição formal de entropia H = -Σ p log p
- V(sistema) operacionalizável como entropia da distribuição de estados
- Base para medir V(raw) vs V(wiki) empiricamente

### Por que Beer é o segundo gap crítico

Ashby modela 1 regulador. KB com múltiplos compiladores (Predição A) precisa de teoria de multi-regulator coordination — que é exatamente o que Beer formaliza no VSM (Viable System Model). Sem Beer, a Predição A não tem framework para design.

## Gaps identificados (estado atual 2026-04-04)

1. **Shannon / Teoria da Informação** — V(LLM) inoperacionalizável sem entropia formal (Shannon em quarentena)
2. **Biologia / sistemas imunes** — único domínio Zone 3 sem cobertura após ingestão lateral
3. **Evidência empírica de degradação** — nenhum estudo mede timelines reais de KB degradation
4. **Prescrições Janis faltando** — devil's advocate + método Delphi documentados como ausentes em [[groupthink-and-cascades]]
5. **Predições A–E do Ashby não testadas** — Predição C tem suporte empírico parcial; A, B, D, E pendentes

### Gaps fechados desde criação deste artigo
- ~~Beer/VSM~~ → viable-system-model-beer.md ✅
- ~~Social choice~~ → social-choice-aggregation.md ✅
- ~~Ecologia~~ → complexity-stability-tradeoff.md + resource-competition-coexistence.md ✅
- ~~Neurociência cognitiva~~ → episodic-semantic-memory.md + complementary-learning-systems.md ✅
- ~~Filosofia da ciência~~ → falsificationism-demarcation.md + scientific-research-programmes.md ✅
- ~~Bounded rationality~~ → heuristics-and-biases.md + prospect-theory.md ✅

## Conexões

- ⚠️ aplicação especulativa de: [[requisite-variety]] — lei formal verificada, aplicação à KB especulativa
- explicado por: [[autonomous-kb-failure-modes]] — failure modes são sintomas do V gap
- refina: [[curation-anti-bias]] — bias de corpus (73% AI/ML) é consequência de V(compiler) topology, não escolha consciente

## Fontes

- [Ashby — Requisite Variety](../../raw/articles/ashby-requisite-variety.md) — lei formal e error floor
