---
title: "Zelox — Ranking de Features por Valor Informacional (Rational Inattention)"
sources:
  - path: wiki/concepts/rational-inattention-discrete.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/rational-inattention.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/zelox-mvp-laudo-aditivos.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/procurement-manipulation-signals.md
    type: synthesis
    quality: primary
    stance: confirming
created: 2026-04-12
updated: 2026-04-12
tags: [zelox, rational-inattention, feature-selection, procurement, audit, information-theory, emergence]
source_quality: medium
interpretation_confidence: low
resolved_patches: []
provenance: emergence
emergence_trigger:
  pair: [rational-inattention-discrete, zelox-mvp-laudo-aditivos]
  ask_session: outputs/logs/sessions/2026-04-12/ask-zelox-attention.md
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-12
---

## Resumo

Aplicação do framework de rational inattention (Sims 2003, Matějka & McKay 2011) ao problema de priorização de features no Zelox: auditor com capacidade limitada C deve alocar atenção entre `aditivo_teto`, `z_score_aditivo` e `rede_empresas_score`. A feature ótima é aquela com maior I(sinal; irregular) / custo_bits. O ranking depende do regime de C: escasso → `aditivo_teto` domina; abundante → `rede_empresas_score` reverte para primeiro.

## Conteúdo

### Framework

Sims (2003): I(X; Y) ≤ C. Auditor minimiza E[(Y − X)²], onde Y = decisão de investigar, X = irregularidade real.

Matějka & McKay (2011): regra ótima de priorização é logit:

```
P(investigar contrato i) ∝ e^{q_i / λ}
```

onde:
- q_i = valor esperado de detecção de irregularidade no contrato i
- λ = custo marginal de 1 bit de atenção do auditor

Feature com maior **I(sinal; irregular) / custo_bits** domina em regime C escasso.

### Análise das três features Zelox

| Feature | I(sinal; irregular) | Custo cognitivo (bits) | Valor/bit | Irregularidade detectada |
|---|---|---|---|---|
| `aditivo_teto` | Alto e específico | Mínimo — aritmética pura, threshold legal fixo 25% (Art. 125, Lei 14.133) | **Máximo** | Hold-up serial em direção ao teto |
| `z_score_aditivo` | Médio — padrão comportamental | Moderado — exige distribuição de referência + contexto setorial | Médio | Hold-up sub-teto, comportamento anômalo sem violação formal |
| `rede_empresas_score` | Muito alto para colusão sistêmica | Alto — exige grafo societário + análise de centralidade | **Baixo em C escasso; alto em C alto** | Bid rigging, single bidding, missing bidders |

### Ranking por regime de C

**Regime binding (C escasso — auditor sobrecarregado):**

Sequência lexicográfica ótima: `aditivo_teto → z_score_aditivo → rede_empresas_score`

1. `aditivo_teto`: threshold legal objetivo, ~0 bits de julgamento, interpreta sem expertise técnica, admissível no TCU sem ML.
2. `z_score_aditivo`: captura CNPJs que fazem hold-up iterativo mas param antes do teto — falsos negativos do sinal anterior. Custo maior (normalização por setor/porte).
3. `rede_empresas_score`: detecta bid rigging sistêmico mas exige grafo completo — só entra após os dois anteriores.

**Regime não-binding (C alto — auditor especializado):**

`rede_empresas_score` reverte para primeiro. Detecta mecanismos (colusão sistêmica) que os outros sinais nunca capturam independentemente de thresholds. Villamil, Kertész & Fazekas (2024): centralidade histórica em grafo de ownership prediz single bidding e result de licitação.

### Implicação para design do Risk Score

O modelo Sims/Matějka prediz que pesos fixos no Risk Score são subótimos. A ponderação ótima varia com λ efetivo do usuário:

| Perfil de usuário | λ efetivo | Feature dominante | Racional |
|---|---|---|---|
| Escritório de advocacia (busca evidência rápida para TCU) | Alto (C baixo) | `aditivo_teto` | Interpreta sem ML, admissível como evidência documental |
| Gestor de controle interno (portfólio de contratos) | Médio | `aditivo_teto` + `z_score_aditivo` | Triagem rápida + escalamento por anomalia |
| CGU / TCU (investigação proativa) | Baixo (C alto) | `rede_empresas_score` | Colusão sistêmica não detectável pelos outros sinais |

## Interpretação

⚠️ Interpretação do compilador — mapeamento feature → I(sinal; irregular) não está em nenhuma fonte; é inferência estrutural do framework Sims/Matějka aplicado ao contexto Zelox.

O resultado mais não-óbvio: **`rede_empresas_score` não é sempre o sinal mais valioso**. Em regime de C escasso, seu custo cognitivo supera seu valor informacional marginal — o auditor deve priorizar sinais mais baratos primeiro. Isso contradiz a intuição de que sinal mais sofisticado = sinal mais útil.

A implicação prática para o Zelox: o Risk Score deveria ter **modo λ** — perfil de usuário determina o vetor de pesos, não um único score universal.

## Verificação adversarial

**O que este artigo NÃO diz:**
- Não estima I(sinal; irregular) empiricamente — não há dados calibrados no corpus
- Não deriva λ para nenhum perfil de usuário — é raciocínio estrutural
- Não confirma que `z_score_aditivo` supera `rede_empresas_score` em C médio — o ranking intermediário é mais incerto

**Risco de over-synthesis:** A aplicação do logit de Matějka & McKay ao problema de priorização de auditoria é por analogia (o paper trata escolha de consumidores, não de auditores). A estrutura matemática se aplica, mas os parâmetros precisam calibração empírica.

**Falsificador:** Se dados de auditoria brasileiros mostrarem que `rede_empresas_score` tem maior precision/recall do que `aditivo_teto` em auditorias com restrição de tempo, o ranking de C escasso estaria errado.

## Conexões

- emerge-de: [[rational-inattention-discrete]] ON "logit como regra ótima de priorização; λ = custo de atenção por bit"
- emerge-de: [[zelox-mvp-laudo-aditivos]] ON "`aditivo_teto` como sinal de mínimo custo cognitivo; threshold legal elimina julgamento discricionário"
- relaciona: [[procurement-manipulation-signals]] ON "`rede_empresas_score` fundamentado em Villamil et al. 2024; Decarolis et al. para bid rigging"
- relaciona: [[rational-inattention]] ON "framework Sims; I(X;Y)≤C constraint base"
- relaciona: [[binding-attention-regime]] ON "⚠️ quarentenado — regime C escasso como contexto de aplicação"

## Fontes

- [[rational-inattention-discrete]] — Matějka & McKay (2011): logit = solução ótima; λ = shadow price de atenção
- [[rational-inattention]] — Sims (2003): I(X;Y)≤C; Var(Y|X)=σ²/e^{2C}
- [[zelox-mvp-laudo-aditivos]] — `aditivo_teto`, mecanismo hold-up de Tirole, threshold Art. 125
- [[procurement-manipulation-signals]] — `rede_empresas_score`, Villamil et al. 2024 (grafos temporais), Decarolis et al. 2020 (bid rigging)
