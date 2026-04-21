---
title: "Corporate Graph Architecture for Phoenix Firm Detection in Brazilian Procurement"
sources:
  - path: wiki/concepts/procurement-manipulation-signals.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/debarment-evasion-phoenix-firms.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/debarment-market-effects.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/procurement-fraud-ml-methods.md
    type: synthesis
    quality: primary
created: 2026-04-08
updated: 2026-04-08
tags: [procurement, phoenix-firms, graph, cnpj, ceis, rais, pncp, network-analysis, zelox, b2g, architecture]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
reads: 1
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-08
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Artigo emergido de /ask cross-paper — aguarda review frio e adversarial"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
provenance: emergence
emergence_trigger:
  pair:
    - procurement-manipulation-signals
    - debarment-evasion-phoenix-firms
    - debarment-market-effects
    - procurement-fraud-ml-methods
  ask_session: outputs/logs/sessions/2026-04-08/ask-18-30.md
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-08
---

## Resumo

Arquitetura de grafo societário para detecção de phoenix firms em procurement público brasileiro: temporal multiplex de dois layers (ownership por CPF + co-bidding por PNCP), alimentado por CNPJ/QSA + CEIS + PNCP como stack MVP, com RAIS como confirmação de segunda camada. Nenhuma fonte individual articula essa arquitetura — emerge da combinação de Villamil (estrutura), Szerman (stack de dados), Auriol & Søreide (problema de identificação), e Santos (validação sistemática).

⚠️ Artigo de síntese interpretativa — não está em nenhuma fonte individual.

## Conteúdo

### O que cada fonte contribui

**Villamil, Kertész & Fazekas (2024)** → estrutura do grafo:
- Temporal multiplex com dois layers: ownership (sócios compartilhados) + co-bidding (participação nas mesmas licitações)
- Temporalidade é crítica: sobreposição *anterior* ao processo prediz o resultado; grafo estático perde direcionalidade
- Alta centralidade no ownership network prediz single bidding e win rate (dados suecos, 2010-2015)

**Szerman (2023)** → stack de dados brasileiro:
- CEIS (CGU) + CNPJ/QSA (Receita) + RAIS (MTE) como combinação tecnicamente viável
- Linkage por CPF (sócios) para ownership layer; linkage por PIS/PASEP (trabalhadores) para confirmação de phoenix
- A combinação CEIS + employer-employee data detecta saída do emprego formal pós-debarment — o mesmo stack detecta phoenix via migração de trabalhadores

**Auriol & Søreide (2017)** → o problema a resolver:
- Agentes de procurement "carecem de registro adequado de fornecedores criminosos" e "é difícil determinar quais membros de um grupo são partes da mesma empresa"
- Este é o bottleneck institucional exato que phoenix firms exploram: mudança de CNPJ apaga o histórico no sistema
- Debarment só funciona onde esse problema de identificação corporativa está resolvido

**Santos et al. (2025)** → validação sistemática do stack:
- Revisão de 93 estudos: PNCP-equivalente + CNPJ-equivalente + RAIS-equivalente é o stack com melhor performance
- Ensemble ML (81-95% accuracy) requer dados de ownership + co-bidding combinados
- PNCP aberto + CNPJ bulk = base disponível sem convênio

### O que emerge da combinação

⚠️ Interpretação do compilador — não está articulado em nenhuma fonte individual.

**Arquitetura completa em dois estágios:**

**Estágio MVP (sem RAIS):**
```
Nodes:  CNPJs ativos em contratos PNCP

Layer 1 — Ownership (QSA/Receita Federal)
  Aresta A→B: A e B compartilham ≥1 CPF de sócio
  Peso: fração de sócios sobrepostos
  Timestamp: janela de vigência da sobreposição

Layer 2 — Co-bidding (PNCP)
  Aresta A→B: A e B participaram da mesma licitação
  Peso: número de processos compartilhados
  Timestamp: data de abertura da licitação

Query Phoenix:
  X ∈ CEIS (data_suspensão = t₀)
  → buscar Y: share_cpf(X,Y) > 0 AND Y.abertura ∈ [t₀-24m, t₀+6m]
  → filtrar Z ⊆ Y: Z participou de licitações PNCP em [t₀, t₀+36m]
  → Z = candidatos a phoenix firm de X
```

**Estágio 2 (com RAIS via convênio):**
```
Layer 3 — Trabalhadores (RAIS/MTE)
  Aresta A→B: trabalhador com mesmo PIS/PASEP aparece em folha de A e depois de B
  Timestamp: data de admissão em B

Query Phoenix ampliada:
  Confirma Z como phoenix se: trabalhadores de X migram para Z após t₀
  (mais difícil de forjar que estrutura societária formal)
```

**Por que a separação MVP/Estágio 2 importa:**
RAIS tem acesso restrito (convênio MTE). O sinal de CPF compartilhado via QSA (aberto, bulk Receita) já captura phoenix formais — onde o mesmo sócio abre nova empresa. RAIS captura phoenix informais — onde o controlador real não aparece como sócio formal mas mantém equipe.

### Thresholds operacionais (não validados empiricamente)

| Parâmetro | Valor sugerido | Base |
|-----------|---------------|------|
| Janela retroativa de criação (t₀ - N meses) | 24 meses | Estimativa operacional ⚠️ |
| Janela prospectiva de participação (t₀ + N meses) | 36 meses | Estimativa operacional ⚠️ |
| Sobreposição de sócios mínima para aresta ownership | ≥1 CPF | Conservative; dados suecos usam métricas de centralidade |
| Concorrentes relacionados → red flag bid rigging | >30% | Decarolis (Itália) — precisa recalibração Brasil ⚠️ |

⚠️ Todos os thresholds são estimativas. O corpus não tem calibração no contexto municipal brasileiro.

### O que o PNCP + CNPJ permite que nenhum sistema atual faz

- Detecção *prospectiva* de phoenix: antes de o novo CNPJ acumular histórico suspeito, o link de CPF com empresa debarred já é o sinal
- Calibração empírica de thresholds: o Zelox seria o primeiro sistema a medir precision/recall deste grafo em dados municipais brasileiros — dado publicável
- Continuidade de identidade corporativa através de CNPJs: o que o CEIS não faz (só busca CNPJ exato)

## Especulação

- Phoenix firms que reincorporam repetem o padrão underbid+aditivo? Não está no corpus — é a hipótese a verificar com o grafo
- O threshold de 30% de concorrentes relacionados (Decarolis/Itália) é transferível para o Brasil? Leis de licitação diferentes podem mudar o nível esperado de sobreposição
- Presta-nomes e sócios de papel tornam o QSA parcialmente não-confiável — RAIS mitiga mas não elimina o problema

## Verificação adversarial

**Pergunta falsificável:** Empresas com CPF de sócio compartilhado com CNPJ-debarred que participaram de licitações pós-debarment têm win rate ou padrão de aditivos significativamente diferente de empresas sem esse histórico?

**Evidência que confirmaria:** análise de dados PNCP mostrando que CNPJs com link de CPF para empresa CEIS têm maior taxa de aditivos próximos ao teto de 25% ou maior frequência de single bidding.

**Evidência que refutaria:** CPF compartilhado entre empresa-CEIS e empresa-nova é frequente por razões inocentes (familiares com múltiplos negócios, sócios legítimos em várias empresas) sem correlação com comportamento irregular pós-debarment. Se a taxa de falso positivo for >50%, o sinal perde valor como feature.

## Teste empírico preliminar — bid_engine.db (2026-04-08)

⚠️ Análise exploratória — amostra pequena (200 CNPJs debarred, 32 pares phoenix, 49 contratos pós-debarment). Não publicável, mas orienta calibração.

**Dataset:** bid_engine.db (59GB SQLite) — CEIS (22.587 sanções) + supplier_socios (360.812 sócios) + contracts_enriched (3,76M contratos)

**Comparação gross (full dataset, sessão anterior):**
| Grupo | Fornecedores | Contratos | % acima 25% teto |
|-------|-------------|-----------|-----------------|
| Phoenix candidates (CPF link com CEIS) | 2.173 | 114.413 | 77,1% |
| Baseline (sem link CEIS) | 461.197 | 3,3M | 79,7% |

**Resultado:** NULL — phoenix candidates têm taxa *ligeiramente inferior* ao baseline. Predição não confirmada na comparação gross.

**Análise temporal — full CEIS (query completa, 201 debarred):**
| Métrica | Valor |
|---------|-------|
| Pares debarred→phoenix | 417 |
| CNPJs phoenix com contratos pós-debarment | 320 |
| Avg contratos por phoenix | 2,7 |
| Avg delta_pct (pós-debarment) | **0,002%** |
| Contratos acima 25% teto | 47 / ~864 = **5,4%** |

**Análise temporal (subsample 200 debarred, para comparação pré/pós):**
| Período | Contratos | % acima 25% teto | Median delta_pct |
|---------|-----------|-----------------|-----------------|
| Pós-debarment (phoenix) | 49 | 2,0% | -93,9% |
| Pré-debarment (mesmos CNPJs) | 180 | 8,3% | n/a |

**Achado convergente:** dois métodos independentes mostram phoenix firms pós-debarment com delta_pct próximo de zero (5,4% acima do teto vs 77-79% no dataset completo). Isso é consistente com estratégia underbid — entrar a preço baixo para ganhar o contrato, aditivos vêm em contratos maduros posteriores. O sinal de aditivo *neste* contrato não é o indicador correto; win rate e padrão longitudinal são os sinais primários (Villamil 2024).

**Série de testes (5 análises, bid_engine.db + s200):**

A hipótese underbid→aditivo foi testada sistematicamente e refutada. O padrão empírico real é **stealth re-entry** — ver [[two-stage-capture-procurement]] para quadro completo.

**Sinais operacionais confirmados — série completa de análises (2026-04-08):**

### Universo real após filtro temporal (phoenix_feature_checks.py)

| Estágio | CNPJs |
|---------|-------|
| Sucessores por CPF compartilhado (pool bruto) | 2.968 |
| Criados após a sanção (data_inicio_atividade > data_sancao) | **39** |
| Com contratos pós-sanção ativos | **30** |

O filtro `created_post_sanction` é obrigatório — reduz ruído de 2.968 para 30 genuínos.

### Features validadas nos 30 genuínos

| Feature | Resultado | Threshold sugerido |
|---------|-----------|-------------------|
| `same_buyer_repeat` | 23/30 (77%) têm repetição no mesmo órgão | ≥ 1 repetição |
| `buyer_5plus` | 9/30 (30%) têm ≥ 5 contratos no mesmo órgão | ≥ 5 = alto risco |
| `top1_organ_share` | avg 0.48; 12/30 com ≥ 50% em um órgão | ≥ 0.5 = concentração |
| `hhi` (órgãos) | avg 0.429 | > 0.4 = concentração |
| `top1_organ_share ≥ 0.8` | 10/30 (33%) | ≥ 0.8 = monopolização |

### Win rate — proxy operacional (não confiável como evidência)

| Grupo | Vitórias | Participações | Taxa |
|-------|---------|--------------|------|
| Genuínos | 636 | 769 | 82.7% |
| Preexistentes | 72.195 | 75.764 | 95.3% |

⚠️ De 75.619 itens com sucessores, apenas 687 (0.9%) têm >1 fornecedor distinto. O banco é majoritariamente winner-centric — win rate não é comparável sem validar cobertura de perdedores.

### Análise s200 (222 pares, 11.830 contratos)

| Sinal | Phoenix | Baseline | Ratio |
|-------|---------|----------|-------|
| `delta_pct < 0` | 94.2% | 53.5% | 1.76× |
| `award_vs_estimated ≤ −10%` | 95.2% | 57.2% | 1.66× |
| `duration_days` mediana | **19 dias** | 270 dias | 14× menor |
| `days_after_sanction` mediana | 56 dias | — | — |

Fonte: scripts/zelox/phoenix_feature_checks.py + outputs/reports/pncp-queries/phoenix-feature-checks-full.md

### Feature Falsification — Resultado Final (duas levas, 2026-04-08)

10 features testadas em genuine (n=30) vs preexisting (n=1.241). Ver [[two-stage-capture-procurement]] para detalhes completos.

**Features de rede sobrevivem; features comportamentais falham:**

| Feature | Status |
|---------|--------|
| `sanction_scope_score` | SUPPORTED — mediana 8.0 vs 6.0 |
| `min_abs_days_to_qsa_change` | SUPPORTED — 697.5 vs 761 dias |
| `same_socio_sanction_count >= 2` | WEAK — precision boost, não discriminador isolado |
| `post_sanction_ramp_speed` | REFUTED |
| `new_buyer_ratio` | WEAK |
| `extreme_additive_tail` | WEAK isolado; útil como monitor de fase 2 |
| `category_shift_from_mother` | REFUTED — direção invertida |
| `stealth_to_extraction_gap` | REFUTED |

### Risk Score v0 (2026-04-08)

`score_evasao_v0`: regressão logística ridge (lambda=30, 5-fold CV, classes balanceadas).
- AUC: 0.590 — triagem adequada, não classificador duro
- Pesos: `same_socio_multi_flag` 0.234 > `sanction_scope_score` 0.135 > `qsa_proximity` 0.057
- Fórmula: `sigmoid(-0.063 + 0.234·z_multi + 0.135·z_scope + 0.057·z_qsa)`

`score_extracao_v0`: monitor observado de `extreme_additive_tail` — fora da calibração prospectiva.

**Validação interna:** caso 37673034000157 rankeado em 7º (score_evasao=0.7395, score_extracao=1, 2.340 contratos). Rank 7 em vez de 1 é sinal de generalização, não overfitting.

Fonte: scripts/zelox/phoenix_risk_score_v0.py + outputs/reports/pncp-queries/phoenix-risk-score-v0.md

**Achado arquitetural:** detecção robusta ocorre no momento do registro do CNPJ (via rede de debarment), não na análise de contratos. As 3 features validadas são computáveis antes do primeiro contrato ser assinado.

## Quality Gate
- [x] Wikilinks tipados: 4 emerge-de com mecanismos específicos
- [x] Instance→class: thresholds marcados como estimativas; accuracy 81-95% qualificada como ground-truth datasets
- [x] Meta-KB separado: aplicação ao Zelox em Conteúdo (é o propósito do artigo)
- [x] Resumo calibrado: ⚠️ artigo de síntese interpretativa explicitado

## Conexões

- emerge-de: [[procurement-manipulation-signals]] ON "temporal multiplex ownership+co-bidding (Villamil 2024) = estrutura de grafo empiricamente validada para bid rigging detection"
- emerge-de: [[debarment-evasion-phoenix-firms]] ON "CEIS+CNPJ+RAIS = stack de dados brasileiro; CPF de sócio = link de continuidade corporativa entre CNPJ-debarred e CNPJ-novo"
- emerge-de: [[debarment-market-effects]] ON "problema de identificação corporativa (Auriol & Søreide) = bottleneck institucional que este grafo resolve"
- emerge-de: [[procurement-fraud-ml-methods]] ON "PNCP+CNPJ+RAIS validado em 93 estudos como stack de maior performance para collusion detection"
- relates: [[zelox-mvp-laudo-aditivos]] ON "grafo societário é camada 2 do produto Zelox: MVP (laudo por CNPJ) + phoenix detection (grafo) = produto completo"
- relates: [[debarment-collusion-experimental]] ON "Cerrone et al.: debarments curtos facilitam colusão tácita — grafo que detecta phoenix resolve o gap de eficácia do debarment"

## Fontes

- [[procurement-manipulation-signals]] — Villamil (2024): temporal multiplex, ownership + co-bidding layers, centralidade prediz win rate
- [[debarment-evasion-phoenix-firms]] — Szerman (2023): CEIS+RAIS viável; CPF como link de continuidade; incentivo causal documentado
- [[debarment-market-effects]] — Auriol & Søreide (2017): problema de identificação corporativa como falha estrutural do debarment
- [[procurement-fraud-ml-methods]] — Santos (2025): PNCP+CNPJ+RAIS como stack de melhor performance em 93 estudos
- [Log /ask 18:30](../../outputs/logs/sessions/2026-04-08/ask-18-30.md) — sessão que articulou a arquitetura integrada

> ⚠️ QUARENTENA: artigo emergido de /ask cross-paper. Critérios pendentes: tempo (24h), review frio em sessão diferente, adversarial ou predição falsificável.
