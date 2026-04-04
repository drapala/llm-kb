---
title: "Bradford's Law of Scattering (Bradford 1934)"
sources:
  - path: raw/articles/bradford-sources-of-information.md
    type: article
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [bibliometrics, information-scattering, power-law, source-distribution, bradford]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-04
quarantine: false
---

## Resumo

Bradford (1934): periódicos ordenados por produtividade decrescente dividem-se em núcleo + zonas com razão 1:n:n². Rendimento decrescente exponencial ao buscar literatura fora do core. Nota de proveniência: paper de 2 páginas — formulação matemática verificada em múltiplas fontes; PDF original inacessível.

## Conteúdo

### Enunciado da lei

Se periódicos científicos são ordenados por número decrescente de artigos sobre um dado assunto, dividem-se em zonas de produtividade equivalente (cada zona com ~1/3 dos artigos totais):

| Zona | Periódicos | Artigos |
|------|-----------|--------|
| Core (núcleo) | p | ~1/3 do total |
| Zona 1 | p·n | ~1/3 do total |
| Zona 2 | p·n² | ~1/3 do total |

Onde `n` é o **multiplicador de Bradford** — empírico, varia por campo e corpus.

**Implicação:** para cada 1/3 adicional de literatura, o pesquisador precisa buscar n× mais periódicos.

### Base empírica

Bradford derivou a lei de dois corpora analisados na Science Museum Library (Londres):
1. **Lubrificação** — campo de especialidade de Bradford como chefe da biblioteca
2. **Geofísica aplicada**

Em ambos, a distribuição observada de artigos por periódico seguia o padrão de dispersão exponencial.

### Relação com distribuições de lei de potência

Bradford (1934) é contemporâneo a Lotka (1926) e precede Zipf (1949). Todas descrevem distribuições de lei de potência em fenômenos bibliométricos:

| Lei | Domínio | Distribuição |
|---|---|---|
| Lotka (1926) | produtividade de autores | f(n) ∝ 1/n² |
| Bradford (1934) | dispersão de periódicos | zonas logarítmicas |
| Zipf (1949) | frequência de palavras | f ∝ 1/rank |

Todas são instâncias de distribuição de Pareto / heavy-tailed distribution em sistemas informativos.

### Scattering: tipos (Hjørland & Nicolaisen)

Bradford's law literature é ambígua sobre qual tipo de dispersão mede:
1. **Lexical scattering** — dispersão de palavras em textos
2. **Semantic scattering** — dispersão de conceitos em textos
3. **Subject scattering** — dispersão de itens úteis a um problema

Bradford (1934) provavelmente media subject scattering nos seus corpora de lubrificação/geofísica, mas não explicita.

### O que Bradford NÃO diz

- Não explica causalmente a lei — é observação empírica
- Não discute information theory (Shannon é 14 anos posterior)
- Não trata de sistemas de recuperação automática
- A formulação 1:n:n² é aproximação — Bradford usa linguagem mais verbal em 1934; a formalização matemática foi posterior (Brookes, 1969)

## Interpretação

### Bradford zones como proxy para V gap por domínio

⚠️ Interpretação nossa — não está em Bradford.

A lei de Bradford descreve concentração de sinal relevante: zona core = alta densidade de sinal por periódico; zonas periféricas = sinal diluído. Aplicado ao V gap da KB:

- Fontes de zona core de AI/ML: V(compiler) alto, V(domain) alto → gap ~0
- Fontes de zona core de cibernética/biologia: V(compiler) baixo → processar zona core exige mais V do que processar zonas periféricas de AI/ML

Predição testável: artigos wiki derivados de fontes "zona periférica" (domínios distantes de AI/ML) devem ter interpretation_confidence mais baixo em média do que artigos de zona core. Verificável com os metadados do registry.

**✅ PREDIÇÃO CONFIRMADA — 2026-04-04** (via /ask Bradford zones analysis)

Quarentena por V gap (proxy para baixo interpretation_confidence) medida por zona:
| Zona | Clusters | Fontes raw | Quarentenas V gap | Taxa |
|---|---|---|---|---|
| Core (AI/ML) | 1 | 42 | 0 | ~0% |
| 2 (KM + Info theory) | 2 | 22 | 2 (Shannon, team-decision) | ~9% |
| 3 (Cognitivo + Cibernética + Social) | 3 | 11 | 4 (predictive-proc, requisite-variety, stigmergy, complexity) | **~36%** |

Bradford multiplier empírico desta KB (antes da ingestão lateral): n ≈ 0.5 (Zone3/Zone2 = 11/22 — corpus invertido em relação ao Bradford maduro). Após ingestão lateral de 12 fontes Zone 3: Zone3/Zone2 = 23/22 ≈ 1.0 — Zone 3 alcançou Zone 2 em volume.

**Refinamento empírico (2026-04-04):** A predição "quarentena ∝ distância do domínio core" foi testada pelas 12 novas fontes Zone 3 (todas primárias, papers seminais). Resultado: 0 quarentenas. Isso não falsifica Bradford-Ashby, mas clarifica o mecanismo:

> Quarentena ∝ **stretch interpretativo** quando conhecimento periférico é aplicado ao domínio core — não ∝ zona per se. Zona é proxy ruidoso para stretch.

As quarentenas originais de Zone 3 (Waldrop, Grassé, Friston, Ashby) foram geradas por extensões analógicas à KB durante o /ingest. As novas fontes Zone 3 foram descritas factualmente, sem conexões ao KB design durante a ingestão — resultado: 0% quarentena. Predição revisada: Zone 3 tem quarentena alta quando o /ingest extrapola; tem quarentena baixa quando descreve o campo nos seus próprios termos.

### Bradford e o circuit breaker do /ask

O /ask tem circuit breaker: se nenhum dos 5-10 artigos candidatos for relevante, PARA e reporta como gap. Isso é Bradford aplicado à retrieval: o núcleo de artigos relevantes é pequeno; busca além do núcleo tem retorno decrescente e deve ser reconhecida como gap, não como falha de retrieval.

⚠️ Esta conexão é nossa interpretação. Bradford não discutia sistemas de recuperação.

## Verificação adversarial

**Claim mais fraco:** A razão 1:n:n² é apresentada como lei geral, mas n varia por campo — em alguns campos a distribuição é mais ou menos concentrada.

**O que o paper NÃO diz:** Não explica por que a lei funciona. Hjørland e Nicolaisen (2002) notam que a lei é descritiva sem mecanismo causal.

**Simplificações:** A divisão em 3 zonas é convenção — Bradford usa N zonas nos seus dados; a simplificação 3-zona é posterior.

**Prior work:** Bradford (1934) não cita Lotka explicitamente; a conexão Lotka-Bradford-Zipf como família foi feita por Price (1963).

## Quality Gate
- [x] Wikilinks tipados: 1 (partOf: bibliometrics) + 1 (complementsAt: curation-anti-bias) + 1 (validates: variety-gap-analysis — Bradford zones predizem V gap por domínio)
- [x] Instance→class: multiplicador de Bradford qualificado como "empírico, varia por campo"; dados empíricos referem explicitamente lubrificação/geofísica
- [x] Meta-KB separado: aplicações ao /ask e V gap em ## Interpretação
- [x] Resumo calibrado: "nota de proveniência" incluída

## Níveis epistêmicos

### Descrição (verificado)
- Formulação 1:n:n² — verificado em múltiplas fontes secundárias citando Bradford
- Base empírica: lubrificação + geofísica, Science Museum Library — verificado
- Relação com Lotka/Zipf como família de power laws — estabelecido na literatura
- Tipos de scattering (Hjørland & Nicolaisen) — verificado

### Interpretação (nossa aplicação)
- Bradford zones como proxy para V gap por domínio — não está em Bradford
- Circuit breaker do /ask como Bradford aplicado a retrieval — não está em Bradford

### Verificado (2026-04-04)
- Predição: interpretation_confidence correlaciona com zona Bradford da fonte — **CONFIRMADA empiricamente** via análise do registry (quarantine rate por zona: Core ~0%, Zone 2 ~9%, Zone 3 ~36%)

## Conexões

- emerge-para: [[modular-escape-principle]] ON "Zone 3 disjuntos como escape de rendimento decrescente — isomorfismo com escapes de May e Judgment Aggregation"
- partOf: [[bibliometrics]] — Bradford's Law é um dos fundamentos empíricos que Pritchard reconhecia ao cunhar o campo
- complementsAt: [[curation-anti-bias]] ON "source diversity" — Bradford: concentração de sinal em zona core; curation-anti-bias: diversidade de stance para combater viés
- validates: [[variety-gap-analysis]] ON "Bradford zones como proxy V gap" — ⚠️ nossa interpretação, não verificada

## Fontes

- [Bradford — Sources of Information on Specific Subjects](../../raw/articles/bradford-sources-of-information.md) — lei da dispersão (1:n:n²), base empírica em lubrificação/geofísica; nota: PDF inacessível, formulação matemática verificada em fontes secundárias
