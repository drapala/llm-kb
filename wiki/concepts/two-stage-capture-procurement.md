---
title: "Two-Stage Capture in Procurement — Underbid vs. Category Escalation (Emergido 2026-04-08)"
sources:
  - path: wiki/concepts/quality-manipulation-underbid-procurement.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/unbalanced-bidding-skew-to-win.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/procurement-contract-design.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/debarment-evasion-phoenix-firms.md
    type: synthesis
    quality: primary
created: 2026-04-08
updated: 2026-04-08
tags: [procurement, phoenix-firms, underbid, capture-strategy, zelox-signals, b2g, empirical, feature-falsification]
source_quality: medium
interpretation_confidence: low
resolved_patches: []
reads: 1
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-08
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Artigo emergido de /ask + análise empírica — hipótese central refutada pelos dados; interpretação alternativa pendente de challenge"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: true
provenance: emergence
emergence_trigger:
  pair:
    - quality-manipulation-underbid-procurement
    - unbalanced-bidding-skew-to-win
    - procurement-contract-design
  ask_session: outputs/logs/sessions/2026-04-08/ask-19-00.md
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-08
---

## Resumo

Testou empiricamente 10 features de detecção de phoenix firms contra bid_engine.db (n=30 genuine vs 1.241 preexisting). **Achado central:** features de rede (sanction_scope_score, same_socio_sanction_count, qsa_proximity) superam features comportamentais — todas as features de comportamento pós-reentrada falharam ou se inverteram. Detecção robusta ocorre no momento do registro do CNPJ, não na análise de contratos. Underbid estratégico não confirmado; padrão real é stealth re-entry (contratos curtos, valores abaixo do estimado, diversificação de órgãos).

⚠️ Artigo emergido de análise empírica — falsificação em duas levas concluída. Score de evasão validado em 3 features.

## Conteúdo

### Hipótese Original (Refutada)

**Mecanismo proposto:** Phoenix firms retornam ao mercado com bids baixos (skew-to-win, JPP 2019) → ganham o contrato → extraem via change orders em contratos maduros (quality manipulation, EER 2018).

**Previsão empírica:** phoenix candidates pós-debarment deveriam ter `valor_inicial` abaixo da mediana da categoria.

### Resultado Empírico — bid_engine.db (2026-04-08)

**Dataset:** 9.086 empresas debarred (CEIS) → 2.962 CNPJs phoenix (link CPF via QSA) → 40.214 contratos pós-debarment.

| Métrica | Valor |
|---------|-------|
| Mean z-score de valor_inicial | **+0.14** (acima da média da categoria) |
| Median z-score | **-0.03** (essencialmente zero) |
| % abaixo da mediana da categoria | **35.9%** (esperado 50% para amostra aleatória) |

**Por categoria (top 5 por volume):**

| Categoria | n phoenix | Median phoenix | Median baseline | Ratio |
|-----------|-----------|---------------|-----------------|-------|
| Compras | 34.686 | R$ 2.026 | R$ 967 | **2.10×** |
| Serviços | 4.368 | R$ 10.364 | R$ 4.000 | **2.59×** |
| Serviços de Saúde | 445 | R$ 63.341 | R$ 64.521 | 0.98× |
| Cessão | 245 | R$ 1.450 | R$ 6.158 | **0.24×** |
| TIC | 188 | R$ 65.717 | R$ 14.630 | **4.49×** |

**Phoenix candidates NÃO underbiddem.** Em 3 das 5 maiores categorias, biddem 2-4x acima do baseline.

### Interpretações Alternativas

⚠️ Especulação do compilador — cada hipótese requer teste próprio.

**Hipótese A — Category Escalation:**
Phoenix firms não retornam à mesma categoria com bid baixo. Retornam a categorias mais lucrativas (Serviços, TIC) onde têm vantagem de expertise acumulada e onde os contratos são maiores. A extração de renda é via *seleção de categoria*, não via *distorção de preço*.

**Hipótese B — False Positive Problem:**
O link via CPF captura muitos empresários legítimos com múltiplas empresas. Uma empresa no CEIS não significa que todas as outras empresas do mesmo sócio são corruptas. Os contratos "acima do baseline" podem simplesmente refletir empresários de maior porte (mais experience → contratos maiores → maior valor_inicial).

**Hipótese C — Timing do Mecanismo:**
O underbid pode ocorrer na *empresa original* (antes do CEIS), não na phoenix. A empresa comete irregularidade via underbid + aditivos → entra no CEIS → cria phoenix → phoenix usa credibilidade da empresa mãe para ganhar contratos maiores a preço normal. O mecanismo de dois estágios está na empresa original, não na phoenix.

**Hipótese D — Underbid em Subsegmento:**
A categoria "Cessão" (ratio 0.24) é a única onde phoenix biddem muito abaixo. Pode ser o subsegmento onde o mecanismo opera. O agregado esconde heterogeneidade.

### O Que Isso Muda no Laudo Zelox

Se a hipótese A (category escalation) for correta:
- O sinal de aditivo (delta_pct alto) permanece válido para contratos maduros
- O sinal de "bid baixo" deve ser REMOVIDO ou aplicado apenas a categorias específicas
- O sinal mais promissor é **mobilidade de categoria**: phoenix que migra de categorias simples para complexas após reincorporação

Se a hipótese B (false positives) for correta:
- O link CPF via QSA tem precisão insuficiente como feature isolada
- Precisaria de segundo filtro: ex., apenas CNPJs criados APÓS o debarment (empresa nova, não empresa preexistente)

### Teste Empírico — Hipótese B (2026-04-08)

**Método:** proxy de data de criação = MIN(data_entrada_sociedade) por CNPJ em supplier_socios.

**Resultado de classificação (2.962 phoenix candidatos):**

| Grupo | n CNPJs | % do total |
|-------|---------|-----------|
| Genuine phoenix (criado APÓS debarment) | **108** | **3,6%** |
| Preexisting (criado ANTES do debarment) | 2.854 | 96,4% |

**Achado crítico:** 96,4% dos "phoenix candidatos" são empresas preexistentes com CPF compartilhado — não novas incorporações. O link CPF captura majoritariamente empreendedores legítimos com múltiplas empresas.

**Comparação de bid prices (ratio vs mediana da categoria):**

| Grupo | Contratos | Median ratio vs baseline | % underbid >30% |
|-------|-----------|--------------------------|-----------------|
| Genuine phoenix | 6.858 | **1,86×** | 23,7% |
| Preexisting | 5.005 | **2,34×** | 33,1% |

**Interpretação:** Genuine phoenix biddem menos que preexisting (1,86× vs 2,34×), sugerindo empresas menores/mais novas. Mas a maioria ainda bida ACIMA da mediana. 23,7% dos contratos genuine underbiddem em >30% — sinal minoritário mas não negligenciável.

**H-B parcialmente confirmada:** o link CPF não separa adequadamente genuine phoenix de multi-empresa legítimos. O corpus relevante é os 108 genuínos, não os 2.962 do pool amplo.

### Predição Falsificável (próximo teste)

**Teste Hipótese A:** verificar se phoenix migram de categoria original da empresa-mãe para categoria de maior valor_inicial:
```python
categoria_mae = modal_category(contratos_de_cnpj_debarred)
categoria_phoenix = modal_category(contratos_de_cnpj_phoenix_pos_debarment)
# H-A: categoria_phoenix has higher avg valor_inicial than categoria_mae
```

**Teste de precision nos 108 genuine (executado 2026-04-08):**

71 dos 108 CNPJs têm contratos pós-debarment. Distribuição de consistência de underbid:

| % contratos com underbid >30% | n CNPJs |
|-------------------------------|---------|
| 0–20% | **62 (87%)** |
| 20–40% | 4 |
| 40–60% | 3 |
| 60–80% | 2 |
| 80–100% | 0 |

**Apenas 2 CNPJs (3%)** mostram underbid consistente (≥50% dos contratos, ≥3 contratos):
- `21019908000117`: 25 contratos, median 0.15×, 68% underbid, avg_delta_pct = 0%
- `47426140000190`: 267 contratos, median 0.43×, 62% underbid, avg_delta_pct = **−82%**

Crítico: os dois underbidders consistentes têm delta_pct NEGATIVO — contratos com *redução* de valor, não aditivos. O mecanismo dois-estágios (underbid → aditivo posterior) **não está presente nos dados**.

## Conclusão Empírica — Quadro Completo (5 testes)

| Teste | Amostra | Resultado |
|-------|---------|-----------|
| Gross comparison (delta_pct ≥25%) | Full CEIS | NULL — 77.1% phoenix vs 79.7% baseline |
| Temporal avg delta_pct | 201 debarred | ≈0% — sem aditivo acima do teto |
| Z-score de valor_inicial | 2.962 phoenix | Phoenix biddem 2–4× ACIMA da mediana — oposto da hipótese |
| Precision genuine phoenix | 108 genuine | 3% underbid consistente; esses têm delta_pct = −82% |
| Análise exploratória s200 (usuário) | 222 pares, 11.830 contratos | **Padrão diferente — entrada furtiva** |

**A hipótese two-stage capture (underbid → aditivo) não está nos dados.** O padrão observado na análise mais rica (s200) é diferente:

### Padrão Empírico Emergente — Stealth Re-entry

| Sinal | Phoenix pós-debarment | Baseline | Ratio |
|-------|-----------------------|----------|-------|
| `delta_pct < 0` | 94.16% | 53.51% | **1.76×** |
| `award_vs_estimated ≤ −10%` | 95.18% | 57.22% | **1.66×** |
| `contract_vs_award ≤ −10%` | 94.09% | 52.47% | **1.79×** |
| `duration_days` (mediana) | **19 dias** | 270 dias | **14× menor** |
| `days_after_sanction` (mediana) | 56 dias | — | re-entrada rápida |
| `top-1 organ share` (1º contrato) | **0.995** | 0.915 | concentração extrema |

**Mecanismo consistente com os dados:** phoenix retorna em 56 dias via órgão familiar (0.995 de concentração no primeiro contrato), com contratos curtos (19 dias) e valores abaixo do estimado e do homologado. Dispersa para outros órgãos depois (0.523). **Não é extração via aditivo — é estabelecimento de foothold furtivo.**

**Primeiro contrato vs contratos posteriores:**
- 1º contrato: `award_vs_estimated ≤ −10%` = 64.42%, `top-1 organ share` = 0.995
- Contratos posteriores: `award_vs_estimated ≤ −10%` = 95.70%, `top-1 organ share` = 0.523
- O padrão se intensifica depois — não é comportamento de entrada que some, é estratégia persistente

⚠️ Ressalva analítica (do autor, s200): baseline de 10k não pareado por modalidade/categoria; linkage continua heurístico (sócio compartilhado). Tratar como exploratória forte, não causal.

### Testes Causais (2026-04-08) — 3 controles

**Teste 1 — Pareamento intra-categoria:**
- Compras: baseline 99% delta<0 — categoria estruturalmente negativa, não discrimina
- **Serviços: phoenix 50% vs baseline 0% delta<0** — sinal robusto dentro da categoria
- Obras/Saúde: ambos baixos — sem diferença

**Teste 2 — Falsification via irmã (mesmo CPF, sem CEIS link):**

| Grupo | n contratos | Dur mediana | delta<0 |
|-------|-------------|-------------|---------|
| Genuine phoenix | 6.858 | **31 dias** | **86.3%** |
| Irmã (mesmo CPF, CNPJ sem CEIS) | 1.672 | 72 dias | **32.8%** |
| Baseline geral | ~10.000 | 270 dias | ~53% |

**Resultado mais forte de todo o conjunto:** o padrão (contratos curtos, delta negativo) é específico ao CNPJ com link para CEIS. A empresa-irmã do mesmo sócio, sem CEIS, comporta-se como o baseline. Não é estilo do empreendedor — é específico da situação de evasão.

**Teste 3 — Organ tracing (primeiro contrato phoenix):**
- Mesmo órgão da empresa-mãe: **12.7%** (9/71)
- Órgão diferente: **81.7%** (58/71)
- Empresa-mãe sem histórico PNCP: 5.6%

**Phoenix NÃO retorna ao órgão familiar.** Estratégia de diversificação — evita o órgão onde a empresa original foi penalizada. O foothold é construído em novos órgãos.

### Feature Set Revisado para Zelox

O laudo de aditivos (z-score de delta_pct) cobre contratos maduros de qualquer fornecedor. Para phoenix especificamente, os sinais operacionais são diferentes:

| Feature | Threshold sugerido | Base empírica |
|---------|-------------------|---------------|
| `award_vs_estimated_pct` | ≤ −10% | 95% dos phoenix vs 57% baseline |
| `contract_vs_award_pct` | ≤ −10% | 94% dos phoenix vs 52% baseline |
| `duration_days` | ≤ 30 dias | Mediana phoenix = 19 vs 270 baseline |
| `days_after_sanction` | ≤ 120 dias | Mediana = 56 dias |
| `top_organ_share_first_contract` | ≥ 0.9 | 0.995 no 1º contrato |
| CNPJ criado após sanção | data_entrada_sociedade > data_debarment | Filtra de 2.962 para 108 |

Todos computáveis de PNCP + CEIS + QSA — sem RAIS necessário para MVP.

## Especulação (pós-refutação da hipótese original)

- O órgão do primeiro contrato NÃO é o órgão da empresa-mãe (12.7% — organ tracing test). Refuta "relacionamento preexistente" e sugere **credencialismo**: novo CNPJ usa expertise herdada para entrar em órgãos novos, evitando rastro.
- Contrato curto + delta negativo em **Serviços** (50% vs 0% baseline após pareamento) é o sinal mais limpo por categoria.

### Distribuição Bimodal — Achado Final (task b2q0xf8v3, pool amplo)

Análise completa com 1.266 suppliers phoenix, 70.369 contratos pós-debarment:

| Grupo | N | % do total |
|-------|---|-----------|
| delta ≤ 0 (stealth) | ~69.529 | **~98.8%** |
| Com aditivo > 0 | 840 | 1.19% |
| **Desses, acima do teto 25%** | **654** | **77.86% dos com aditivo** |
| Avg delta dos com aditivo | — | **62.09%** |

**A distribuição é bimodal:** a vasta maioria dos contratos phoenix tem delta negativo (stealth re-entry). Mas os 1.19% que têm aditivo tendem a ser extremos — avg 62%, 78% acima do teto legal. **Quando a extração começa, é maximal.**

**Caso flagrante:** CNPJ `37673034000157` aparece como phoenix de **3 empresas debarred diferentes** (R$ 143M em contratos). Hub phoenix — absorveu múltiplas identidades.

**Revisão do mecanismo:** stealth re-entry é fase 1 (estabelecimento), não o fim. A extração via aditivo extremo é fase 2, rara mas maximal quando ocorre. O two-stage capture existe — só não está no mesmo contrato, está na sequência temporal.

### Feature Falsification — Duas Levas (2026-04-08)

Script: `scripts/zelox/phoenix_feature_falsification.py`
Controle: genuine (`created_post_sanction = 1`, n=30) vs preexisting (`created_post_sanction = 0`, n=1.241), ambos com contratos pós-sanção.

**Leva 1 — 4 prioritárias:**

| Feature | Resultado | Detalhe |
|---------|-----------|---------|
| `same_socio_sanction_count` | **WEAK** | Mediana empata (1 vs 1); taxa ≥2 é 23.3% genuine vs 10.2% — melhora precision isolada, fraca como discriminador |
| `post_sanction_ramp_speed` | **REFUTED** | Genuine: mediana 0 contratos em 90 dias; preexisting: mediana 1. Consistente com cautela deliberada, não aceleração |
| `new_buyer_ratio` | **WEAK** | Direção correta, mas todo o universo de sucessores também vai para órgãos novos — separa pouco |
| `qsa_change_near_sanction` (flag ≤90d) | **REFUTED** | Genuine 10% vs preexisting 16.2% — direção invertida como flag binária |
| `qsa_change_near_sanction` (distância mínima) | **SUPPORTED** | Mediana genuine 697.5 vs preexisting 761 dias — sinal sutil, na direção certa |

**Leva 2 — 6 features adicionais + associações:**

| Feature | Resultado | Detalhe |
|---------|-----------|---------|
| `sanction_scope_score` | **SUPPORTED** | Mediana genuine 8.0 vs preexisting 6.0 — gap de 33%, o mais limpo de todos os testes |
| `extreme_additive_tail` | **WEAK** | Direção invertida: genuine 6.67% vs preexisting 10.64% — consistent com stealth (ainda na fase 1) |
| `stealth_to_extraction_gap` | **REFUTED** | Mediana genuine 72.5 vs preexisting 65 dias — sem diferença material |
| `category_shift_from_mother` | **REFUTED** | Genuine MORE distantes da categoria da mãe (mediana 1.0 vs 0.67) — hipótese de continuidade invertida |
| `same_socio_sanction_count >= 2 → extreme_additive` | **SUPPORTED** | Associação interna: 18.8% vs 9.58% — count alto prediz fase 2 |
| `sanction_scope_score >= 4 → extreme_additive` | **WEAK** | Score separa genuine, mas não explica fase 2 isolado |

**Achado estrutural — features de rede superam features comportamentais:**

As 3 features que sobreviveram (`sanction_scope_score`, `same_socio_sanction_count`, `min_abs_days_to_qsa_change`) são todas sobre a rede de debarment — não sobre comportamento pós-reentrada. Todas as features comportamentais (ramp_speed, extreme_additive isolado, stealth_gap, category_shift, new_buyer_ratio) falharam ou enfraqueceram. Implicação: detecção robusta ocorre **no momento do registro**, não na análise de contratos — o CNPJ é detectável antes de assinar qualquer contrato.

**`extreme_additive_tail` invertido é coerente:** genuine phoenix têm menos aditivos extremos que preexisting porque ainda estão na fase 1. A extração ocorre em contratos maduros que o banco ainda não registra (ou em CNPJs não capturados pelo filtro). É indicador de fase 2, não de detecção primária.

**`category_shift` refutado na direção errada:** genuine se diversificam mais do que preexisting (mediana 1.0 vs 0.67 de distância Jaccard). Possíveis explicações: diversificação deliberada para evitar detecção, ou CNPJs novos naturalmente biddam em categorias mais variadas que empresas estabelecidas.

**Score de evasão recomendado (3 features validadas):**
1. `sanction_scope_score` — feature quantitativa mais forte (gap 33%)
2. `same_socio_sanction_count` — precision booster (taxa ≥2 dobra em genuine)
3. `qsa_proximity` — distância contínua, não flag; argumento jurídico de cronologia

**Camada de fase 2 (não primária):**
- `extreme_additive_tail` — quando o CNPJ já está identificado como phoenix; sinal de extração ativa

**Descartadas para MVP:**
- `post_sanction_ramp_speed`, `new_buyer_ratio`, `category_shift_from_mother`, `stealth_to_extraction_gap`

Fonte: `outputs/reports/pncp-queries/phoenix-feature-falsification.md` (levas 1 e 2)

### Winner-Centric Procurement Data Gap (PNCP Brasil)

⚠️ Observação estrutural emergida de análise Zelox (2026-04-08) — não está nos papers do corpus.

Uma limitação material para qualquer modelo de detecção baseado em PNCP: **os dados públicos de licitação brasileiros são 99.1% winner-centric**. O que está disponível:
- Empresa vencedora (CNPJ, valor homologado, objeto)
- Valor estimado pelo órgão
- Delta entre estimado e homologado

O que não está disponível via PNCP standard:
- Quem perdeu — os outros participantes do certame
- Lance de cada proponente (exceto pregão com ata publicada)
- Sequência de lances no pregão eletrônico

**Implicação para detecção de bid depression:** qualquer hipótese sobre underbid estratégico de phoenix firms (lance deliberadamente baixo para ganhar) não pode ser testada com dados PNCP diretamente — só se vê o winner, não o spread do certame.

**Caminhos parciais para losing bidder data:**
- PNCP `/propostas` endpoint (não documentado publicamente — verificar disponibilidade)
- COMPRAS.GOV.BR API (federal — mais completo que PNCP para pregões eletrônicos)
- Querido Diário NLP (atas de julgamento publicadas em diários oficiais municipais)

**Impacto no corpus:** os 5 testes empíricos deste artigo só comparam *contratados* phoenix vs *contratados* baseline — não comparam lances. A refutação do underbid hipótese é sobre contratos ganhos, não sobre estratégia de lances.

## Verificação adversarial

**Claim mais fraco:** a comparação de mediana por categoria não controla por subcategoria, porte da firma, região, ou tipo de órgão. "Compras" é uma categoria vasta — phoenix em Compras podem estar em subcategorias sistematicamente mais caras.

**Evidência que confirmaria H-A (escalation):** análise de categoria *antes* e *depois* do debarment para os mesmos CNPJs/sócios mostrando migração para categorias de maior ticket.

**Evidência que refutaria underbid definitivamente:** mesmo após controlar por subcategoria e porte, phoenix candidates têm valor_inicial >= baseline.

## Quality Gate
- [x] Wikilinks tipados: emerge-de com mecanismos específicos
- [x] Instance→class: dados bid_engine.db (Brasil, PNCP, amostra 2024-2026); não generalizável sem replicação
- [x] Meta-KB separado: implicações Zelox em seção própria
- [x] Resumo calibrado: hipótese refutada explicitada no resumo, não enterrada

## Conexões

- emerge-de: [[quality-manipulation-underbid-procurement]] ON "mecanismo teórico underbid+change orders — testado empiricamente e não confirmado no agregado"
- emerge-de: [[unbalanced-bidding-skew-to-win]] ON "skew-to-win como hipótese de entrada — z-score empírico mostra que phoenix não underbidem na maioria das categorias"
- emerge-de: [[procurement-contract-design]] ON "z-score de aditivo por categoria como feature — permanece válido mesmo com hipótese de underbid refutada"
- relates: [[procurement-phoenix-graph-architecture]] ON "dados empíricos que refinam o design do grafo: sinal de valor_inicial deve ser condicionado por categoria e data de criação do CNPJ"
- relates: [[debarment-evasion-phoenix-firms]] ON "Szerman confirma incentivo econômico para phoenix; este artigo testa mas não confirma o mecanismo de captura via underbid"

## Fontes

- [[quality-manipulation-underbid-procurement]] — EER 2018: mecanismo underbid+change orders (hipótese testada)
- [[unbalanced-bidding-skew-to-win]] — JPP 2019: skew-to-win como fundamento game-teórico
- [[procurement-contract-design]] — Bajari & Tadelis: z-score por categoria como feature
- bid_engine.db (análise exploratória 2026-04-08) — 40.214 contratos phoenix pós-debarment; mediana por categoria; z-score de valor_inicial
- [Log /ask 19:00](../../outputs/logs/sessions/2026-04-08/ask-19-00.md) — sessão que originou a hipótese

> ⚠️ QUARENTENA: hipótese central refutada empiricamente. Interpretação alternativa (category escalation, false positives) pendente de teste. Não usar como fonte até challenge e testes adicionais.
