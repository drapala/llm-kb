---
title: "z_score_aditivo — Sinal de Anomalia de Aditivo por Tipo de Objeto"
sources:
  - path: wiki/concepts/procurement-contract-design.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/zelox-mvp-laudo-aditivos.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/two-stage-capture-procurement.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/procurement-variety-gap.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/laic-ufmg-procurement-fraud-detection.md
    type: synthesis
    quality: primary
    stance: challenging
    challenging_type: implication
created: 2026-04-12
updated: 2026-04-12
tags: [zelox, procurement, feature, z-score, aditivo, fraud-detection, bajari-tadelis, b2g, IQR]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - wiki/concepts/procurement-contract-design.md
  - wiki/concepts/zelox-mvp-laudo-aditivos.md
  - wiki/concepts/two-stage-capture-procurement.md
  - wiki/concepts/procurement-variety-gap.md
---

## Resumo

`z_score_aditivo` é o sinal do Zelox que padroniza a taxa de aditivo de um contrato em relação à distribuição de contratos do mesmo tipo de objeto. Captura comportamento anômalo de aditivo que está abaixo do teto legal (25%), onde `aditivo_teto` falha. Backing teórico: Bajari & Tadelis (2001) — contratos de maior complexidade têm taxa de aditivo estruturalmente maior, portanto comparação crua entre tipos é enviesada.

## Conteúdo

### Definição

```
z_score_aditivo = (delta_pct_contrato − μ_delta_pct_tipo) / σ_delta_pct_tipo
```

onde:
- `delta_pct` = `aditivo_acumulado / valor_original_contrato` (taxa bruta de aditivo)
- μ e σ computados por tipo de objeto (categoria PNCP)

Interpretação: z > 0 = o contrato tem taxa de aditivo acima da média da sua categoria; z ≥ 2 = top ~2.5% da distribuição = red flag.

### Por que normalizar por tipo de objeto

Bajari & Tadelis (2001): o tipo de contrato (FP vs C+) determina a taxa estrutural esperada de aditivo. Projetos complexos (obras, TI, infraestrutura) têm alta incerteza de design → aditivos são parcialmente inevitáveis, mesmo sem hold-up. Projetos simples (compras, serviços padronizados) têm baixa incerteza → aditivos são mais anomalous.

A Lei 8.666/93 força FP para todos os projetos, incluindo os complexos. Resultado: taxa de aditivo esperada varia muito por categoria de objeto. Um delta_pct de 20% em obra de engenharia é menos anômalo que 20% em compra de material de expediente.

Comparar delta_pct sem controle de categoria gera falsos positivos (projetos complexos legítimos flagados) e falsos negativos (hold-up em categorias de alto aditivo esperado).

### Relação com `aditivo_teto`

| Sinal | O que detecta | O que perde |
|---|---|---|
| `aditivo_teto` | Violação formal ou aproximação ao limite (Art. 125, Lei 14.133) | Hold-up que para antes do teto; variação por categoria |
| `z_score_aditivo` | Anomalia relativa à categoria — hold-up sub-teto | Violação absoluta do teto; requer distribuição de referência |

Os dois sinais são complementares. `aditivo_teto` é específico e sem custo de calibração; `z_score_aditivo` é sensível e requer dados históricos por categoria.

### Variante por modalidade

Procurement variety gap (ver [[procurement-variety-gap]]): contratos de contratação integrada (Art. 46, inciso V, Lei 14.133) têm error floor estruturalmente menor → o mesmo z_score tem peso maior nessa modalidade.

Variante sugerida: `z_score_aditivo_por_tipo × (1 + modality_premium)`, onde `modality_premium > 0` para contratação integrada e ≈ 0 para regime tradicional.

### Status empírico

`two-stage-capture-procurement.md` valida que o "z-score de delta_pct" permanece como feature válida mesmo após a hipótese de underbid+aditivo ter sido refutada empiricamente nos dados de empresas phoenix. A feature identifica anomalia de aditivo em contratos maduros de qualquer fornecedor — não depende do mecanismo específico de two-stage capture.

Validação indireta: `extreme_additive_tail` (versão binária, cauda extrema da mesma distribuição) é usada como monitor de fase 2 no Risk Score v0 (`score_extracao_v0`).

### Custo de computo

Requer distribuição de referência por categoria → precisa de histórico PNCP por tipo de objeto. Este é o principal custo de atenção em relação a `aditivo_teto` (que é aritmética pura). Em regime de C escasso (ver [[zelox-attention-feature-ranking]]), `aditivo_teto` deve ser consultado primeiro.

### Escopo de aplicação (restrição empírica)

Com base na calibração de 2026-04-12 (bid_engine.db, ~2.1M contratos):

- **`valor_global - valor_inicial`** é o campo correto para fallback (não `valor_acumulado`)
- **Filtro obrigatório:** `tipo_contrato = 'Contrato (termo inicial)'`
- **Fonte primária (todos os categorias):** `/termos` endpoint → `Σ(valorAcrescido)` para `tipoTermoContratoNome == 'Termo Aditivo'`
  - Representa aditivo realizado independente de `valor_global` pré-autorizado
  - Contratos sem termos: `aditivo_termos_ratio = None` (sem penalidade — fallback aplicado)
- **Fallback (apenas Obras e Serviços de Engenharia):** `valor_global - valor_inicial`
  - Compras e Serviços: `valor_global` frequentemente registra teto pré-autorizado (ARP, renovação anual) → não usar como fallback
- Implementado em `scripts/zelox/pncp_supplier_contracts.py` via `_ZSCORE_ELIGIBLE_TIPOS`, `_ZSCORE_CATEGORIAS_SEM_TERMOS` e `_effective_ratio()`

## Interpretação

⚠️ Interpretação do compilador — a fórmula de z_score_aditivo não está em nenhuma fonte raw/; é design de feature derivado do corpus teórico.

O backing mais forte é estrutural (Bajari-Tadelis justifica por que a normalização é necessária), não empírico (não temos precision/recall para z_score_aditivo em dados PNCP brasileiros). A feature faz sentido teórico mas carece de calibração de threshold. z ≥ 2 como red flag é heurística razoável para Gaussianas, mas a distribuição de delta_pct por categoria pode ser não-Gaussiana (cauda pesada à direita).

### Calibração empírica — bid_engine.db (2026-04-12)

Análise em ~2.1M contratos PNCP (bid_engine.db), filtrado a aditivo_pct ∈ [0, 500%]:

| Categoria | thresh z≥2 | thresh IQR 1.5× | flags_teto25 | flags_z2 | flags_IQR | IQR÷z2 |
|---|---|---|---|---|---|---|
| Obras | **109%** | 51.8% | 86 | 9 | 37 | **4.1×** |
| Serviços de Saúde | 192% | 51.5% | 91 | 14 | 57 | 4.1× |
| Compras | 371% | 456% | 1600 | 171 | 48 | 0.28× |
| Serviços | 325% | 250% | 1730 | 207 | 319 | 1.5× |

**Causa raiz identificada (2026-04-12) — dois problemas independentes:**

1. **Campo errado:** análise inicial usou `valor_acumulado - valor_inicial`. O campo correto para aditivos realizados é `valor_global - valor_inicial`. `valor_acumulado` em Empenhos acumula pagamentos iterativos, não aditivos contratuais.

2. **Serviços com `valor_global ≈ 2× valor_inicial`:** Q3=100% é estrutural — contratos de serviço registram `valor_global` como teto pré-autorizado para renovações anuais, não como aditivo realizado. Vigência anual + valor_global = 2× é padrão de administração pública brasileira. `valor_global - valor_inicial` para Serviços não mede aditivo de Art. 125.

**Escopo válido do z_score_aditivo:** somente `tipo_contrato = 'Contrato (termo inicial)'` + `categoria IN ('Obras', 'Serviços de Engenharia')`. Demais categorias têm semântica de `valor_global` incompatível com aditivo do Art. 125.

Filtrando para `tipo_contrato = 'Contrato (termo inicial)'`, campo `valor_global`:

| Categoria | n | Q1/p50/Q3 | thresh z≥2 | thresh IQR | flag_25 | flag_z2 | flag_IQR | IQR÷z2 |
|---|---|---|---|---|---|---|---|---|
| Compras | 665 | 5.5/19.3/27.6 | 153% | **60.7%** | 186 | 38 | 138 | **3.6×** |
| Obras | 428 | 6.4/13.7/24.2 | 74.5% | 50.9% | 74 | 27 | 28 | 1.0× |
| Serviços de Saúde | 343 | 6.7/20.0/25.0 | 102% | 52.5% | 78 | 23 | 43 | 1.9× |
| Serviços | 2328 | 5.5/24.1/100.0 | 187% | 242% | 985 | 172 | 45 | 0.26× |

**Achados com dados limpos:**
- **Filtro obrigatório:** `tipo_contrato = 'Contrato (termo inicial)'` — Empenhos não medem aditivos, medem execução orçamentária.
- **Compras (limpo):** IQR ganha 3.6× sobre z2. Threshold IQR=60.7% é razoável; z2=153% é inutilizável.
- **Obras:** IQR e z2 convergem (1.0×), mas `aditivo_teto` continua dominante (74 flags vs 28). Q3=24.2% já está no limite legal — IQR é complemento, não substituto.
- **Serviços:** Q3=100% indica contratos plurianuais com renovação anual acumulando em valor_acumulado. ⚠️ Requer investigação separada — não é aditivo de Art. 125.
- **Conclusão:** o problema não era z-score vs IQR — era Empenho vs Contrato. Com dados limpos, IQR é preferível para Compras e Serviços de Saúde; para Obras, `aditivo_teto` é suficiente.

### IQR como alternativa mais robusta (LAIC/UFMG)

Silva & Pappa (2024) usam IQR — não z-score — para detecção de anomalia de preço em procurement:

```
Anomalia = preço fora de [Q1 − 1.5×IQR, Q3 + 1.5×IQR]
```

Em distribuição Gaussiana, esse threshold corresponde a **z ≈ 2.7**, não z ≈ 2. Mais importante: IQR é **resistente a outliers** porque usa quartis, não média e desvio padrão. Distribuições de delta_pct têm cauda direita pesada (projetos com aditivo de 50%+ por razão técnica legítima) — esses outliers inflam σ e tornam o z-score permissivo.

Implementação robusta (⚠️ nossa interpretação — não está em Silva 2024 aplicada a aditivos):

```python
Q1 = delta_pct_categoria.quantile(0.25)
Q3 = delta_pct_categoria.quantile(0.75)
IQR = Q3 - Q1

flag_anomalia = delta_pct_contrato > (Q3 + 1.5 * IQR)
iqr_score = max(0, (delta_pct_contrato - Q3) / IQR)  # >1.5 = flag
```

Vantagem adicional: "acima do limite da caixa" é mais defensável ao TCU do que "2 desvios padrões".

## Verificação adversarial

**O que este artigo NÃO diz:**
- Silva 2024 é STUB — não confirmado se o IQR foi aplicado a aditivos especificamente ou apenas a preços unitários de itens
- Não compara precisão IQR vs z-score em dados PNCP + ground truth CGU/TCU
- Threshold 1.5× (Tukey 1977) não foi calibrado para delta_pct de procurement brasileiro
- A distribuição de referência via `/termos` ainda não foi calibrada empiricamente — requer histórico de contratos com termos publicados no PNCP

**Gap resolvido (2026-04-12):** expansão do sinal para Compras e Serviços via `/termos` → `valorAcrescido`. Validado logicamente (mock): `_effective_ratio` prioriza `aditivo_termos_ratio` e ignora `valor_global` inflado. Validação empírica em fornecedor com Termos Aditivos reais pendente.

**Risco do z-score:** Outliers estruturais (projetos com aditivo de 50%+ por razão técnica legítima) inflam σ → threshold z ≥ 2 torna-se muito permissivo nessas categorias. IQR é mais robusto nesse regime.

## Conexões

- complementsAt: [[zelox-mvp-laudo-aditivos]] ON "`aditivo_teto` = threshold absoluto; `z_score_aditivo` = anomalia relativa — cobrem mecanismos diferentes"
- derivedFrom: [[procurement-contract-design]] ON "Bajari-Tadelis: taxa de aditivo varia por complexidade do projeto → normalização por tipo é necessária"
- relaciona: [[zelox-attention-feature-ranking]] ON "ranking Sims/Matějka coloca `z_score_aditivo` no slot intermediário (C médio); custo de computo é o fator"
- relaciona: [[procurement-variety-gap]] ON "modality_premium: integrada tem error floor menor → mesmo z tem peso maior"
- relaciona: [[two-stage-capture-procurement]] ON "z-score de delta_pct permanece válido como feature de contratos maduros independente de hipótese de two-stage capture"

## Fontes

- [[procurement-contract-design]] — Bajari & Tadelis (2001): FP vs C+, taxa de aditivo varia por complexidade
- [[zelox-mvp-laudo-aditivos]] — delta_pct = aditivo_acumulado/valor_original; contexto PNCP
- [[two-stage-capture-procurement]] — "z-score de delta_pct" como feature residual validada (bid_engine.db 2026-04-08)
- [[laic-ufmg-procurement-fraud-detection]] — Silva & Pappa (2024): IQR como alternativa mais robusta; threshold 1.5× ≈ z 2.7 em Gaussiana
- [[procurement-variety-gap]] — modality_premium para contratação integrada
