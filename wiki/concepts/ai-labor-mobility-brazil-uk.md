---
title: "AI Exposure and Occupational Mobility: Brazil vs. UK (IMF WP 2024/116)"
sources:
  - path: raw/papers/cazzaniga-pizzinelli-2024-ai-labor-brazil-uk-imf.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-08
updated: 2026-04-08
tags: [labor-economics, ai, brazil, uk, occupational-mobility, informality, pnad, inequality]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Gate 3∥challenge — 1 claim invalidado + 4 weakened"
quarantine_criteria_met:
  gates_passed: [1, 2]
  gates_failed: [3]
  gate3_run: 2026-04-08
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  gate3_claims_challenged: 9
  gate3_claims_survived: 4
  gate3_claims_weakened: 4
  gate3_claims_invalidated: 1
  challenge_verdict: PRECISA_CORREÇÃO
---

## Resumo

Cazzaniga, Pizzinelli, Rockall & Tavares (IMF WP/24/116, junho 2024) documentam transições ocupacionais históricas de trabalhadores no Brasil (PNAD Contínua) e no UK (LFS) por categoria de exposição à AI. Achado central: trabalhadores com ensino superior transitam de ocupações HELC (risco) para HEHC (complementaridade) em ambos os países com frequência similar — padrão de mobilidade "para cima". Trabalhadores sem ensino superior no Brasil têm risco muito maior de mobilidade descendente para LE (baixa exposição, menor salário). Informalidade como "double blow" (deslocamento + informalidade) é condicional ao desemprego — não à simples mudança ocupacional.

## Conteúdo

### Framework de Três Categorias Ocupacionais

| Categoria | Definição | Resultado esperado com AI |
|-----------|-----------|---------------------------|
| HEHC | Alta exposição + alta complementaridade | Aumento de produtividade, salário cresce |
| HELC | Alta exposição + baixa complementaridade | Risco de substituição por AI |
| LE | Baixa exposição | Baixo impacto direto |

### Composição do Emprego por País

| País | HEHC | HELC | LE (aprox.) |
|------|------|------|-------------|
| UK | 35% | 30% | 35% |
| Brasil | 19% | 21% | 60% |

Brasil: menor share em categorias expostas — reflexo de maior informalidade e intensidade cognitiva média menor.

### Trabalhadores com Ensino Superior: Brasil ≈ UK

- Ambos os países: mobilidade "para cima" — HELC → HEHC ao longo da carreira
- Transições HELC→HEHC associadas a aumento de salário
- Concentradas nas 20s e 30s
- Retenção emprego: 98% UK vs. 96.3% Brasil (quarter-a-quarter)
- **Implicação:** impacto de AI no alto qualificado pode ser similar entre economias avançadas e emergentes

### Jovens com Ensino Superior: Stepping-Stone Risk

- Empregos HELC servem como degrau de carreira para HEHC
- Se AI eliminar HELC jobs de entrada → disruption de início de carreira para jovens qualificados
- Este grupo tem simultaneamente a maior oportunidade (crescimento em HEHC) e o maior risco (entrada bloqueada)

### Trabalhadores sem Ensino Superior: Brasil ≠ UK

- Brasil: muito maior risco de mobilidade descendente para LE após deslocamento de HELC
- Non-college workers Brasil: praticamente **nenhum crescimento de salário ao longo da carreira**
- Retenção Brasil non-college: 89.6% (vs. 97.7% UK) — maior risco idiossincrático
- Retorno à experiência mais baixo para não-qualificados em LE — desvantagem se perpetua

### Informalidade como "Double Blow" — Condicional ao Desemprego

**Achado crítico (seção sobre informalidade, Brasil):**

- Mudança de ocupação para trabalhadores formais: **raramente** implica em passagem para informalidade quando ocorre *via novo emprego direto*
- Quando ocorre *via spell de desemprego*: trabalhadores em LE têm alta probabilidade de entrar na informalidade

```
Deslocamento por AI
       ↓
Via emprego direto → novo emprego formal (sem double blow)
Via desemprego → LE workers → alta prob. de informalidade
                → double blow: perda de renda + perda de proteção trabalhista
```

Implicação: se AI disrupção for gradual e mercado de trabalho absorver sem desemprego intermediário, o double blow é menos provável. Se criação de desemprego friccional for grande, double blow é risco real para trabalhadores não-qualificados brasileiros.

### Exercício Contrafactual (Partial Equilibrium)

- Cenário: AI desloca HELC workers para desemprego
- Brasil: efeito mais negativo sobre lifetime earnings do que no UK (qualquer nível educacional)
- Razão: salários relativos HELC são mais altos no Brasil do que no UK → perda absoluta maior
- Ganho em HEHC: concentrado em altamente educados; mais no UK do que no Brasil

## Verificação adversarial

**Claim mais fraco:** "padrões históricos de transição valerão com AI" — o paper usa transições pré-AI como proxy para capacidade de adaptação, mas reconhece explicitamente que transformação estrutural profunda pode mudar padrões.

**O que o paper NÃO diz:**
1. Não prevê que o Brasil terá melhor ou pior desempenho que o UK — apenas documenta estruturas de transição
2. Não modela criação de novas ocupações por AI
3. Partial equilibrium: não captura efeitos de preço (salários de equilíbrio podem subir em HEHC, reduzindo pressão descendente em HELC)

**Simplificações:** exercício contrafactual é ilustrativo — "wide range of potential outcomes" é reconhecida pelos autores.

**Prior work:** Pizzinelli et al. (2023) fornece o mapeamento de AI exposure por ocupação. Eloundou et al. (2023), Webb (2020), Felten et al. (2023) são trabalhos de exposição estática que este paper complementa com dinâmica.

## Interpretação

(⚠️ Zone 3 — domínio lateral. Interpretação intencionalmente vazia no ingest. Conexões com a KB emergem no /ask.)

## Conexões

## Fontes
- [Cazzaniga, Pizzinelli, Rockall, Tavares (2024)](../../raw/papers/cazzaniga-pizzinelli-2024-ai-labor-brazil-uk-imf.pdf) — IMF WP/24/116; PNAD Contínua + LFS; Brasil vs. UK; HEHC/HELC/LE transitions; double blow condicional

## Quality Gate
- [x] Wikilinks tipados: nenhum — Zone 3, conexões emergem no /ask
- [x] Instance→class: 19%/21% HELC/HEHC Brasil qualificados como dados de composição de emprego via Pizzinelli mapping; não projeção
- [x] Meta-KB separado: nenhuma referência ao metaxon no Conteúdo
- [x] Resumo calibrado: source_quality:high — paper peer-reviewed IMF Research Dept., dados PNAD Contínua primários

> ⚠️ QUARENTENA: Gate 3∥challenge — 1 claim invalidado + 4 weakened. Correções necessárias antes de /promote:
> 1. [INVALIDADO] "Non-college workers Brasil: praticamente nenhum crescimento de salário ao longo da carreira" → overstates: há algum crescimento nos primeiros 5-10 anos de carreira; trocar por "crescimento salarial muito menor que no UK; perfil plano após a fase inicial"
> 2. [WEAKENED] "Retenção emprego: 98% UK vs. 96.3% Brasil (quarter-a-quarter)" → especificar: são dados de college workers mantendo emprego; período e definição de retenção ausentes
> 3. [WEAKENED] "Exercício contrafactual: efeito mais negativo no Brasil (qualquer nível educacional)" → trocar por "mais negativo em média, com assunção de que HELC wages relativas mais altas no Brasil — resultado dependente de modelo"
> 4. [WEAKENED] "UK 35%/30%, Brasil 19%/21% HEHC/HELC" → adicionar: "metodologia-sensitivo; baseado em Pizzinelli et al. (2023) mapping — percentuais variam com framework de exposição"
> 5. [/challenge] "transitam com frequência similar" → trocar por "padrão de transição HELC→HEHC presente em ambos os países"
> 6. [/challenge] Coluna LE na tabela: valores 35%/60% são derivados aritméticos → adicionar "(calculado)"
