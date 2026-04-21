---
title: "Economic Analysis of Debarment — Market Effects (Auriol & Søreide 2017)"
sources:
  - path: raw/papers/auriol-soreide-2017-economic-analysis-debarment.md
    type: paper
    quality: primary
    stance: challenging
    challenging_type: implication
created: 2026-04-08
updated: 2026-04-08
tags: [procurement, debarment, corruption, competition, market-structure, phoenix-firms, b2g, theory]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 2
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-08
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Gate 1 — auto-promote pending"
quarantine_criteria_met:
  gates_passed: []
  gates_failed: [1]
  gate1_reason: "não avaliado ainda — ingest automático via scout"
---

## Resumo

Auriol & Søreide (2017) modelam os efeitos de mercado do debarment em procurement público. Resultado central: eficácia depende do nível de competição — funciona em mercados concentrados com horizonte longo, mas tem efeito anti-competitivo que pode facilitar colusão. O paper explicita o problema de identificação de grupos corporativos como vulnerabilidade estrutural do debarment. IRLE 50:36-49.

⚠️ Stub — baseado em PDF aberto (publicprocurementinternational.com) e TSE working paper. Conteúdo parcialmente verificado.

## Conteúdo

### Modelo

Mercado de procurement com corrupção endógena. Fornecedores escolhem se corrompem dado: probabilidade de detecção p, duração do debarment d, valor esperado de contratos futuros V, e grau de competição no mercado.

### Resultados Teóricos

**1. Mercados competitivos: debarment faz pouca diferença**
Quando há muitos fornecedores alternativos, excluir um não reduz a probabilidade de corrupção significativamente — outros fornecedores ocupam o espaço e a corrupção migra, não cessa.

**2. Mercados concentrados: debarment pode funcionar**
Condição: firmas valorizam contratos futuros (δ alto) E probabilidade de detecção é real. Em municípios menores com poucos fornecedores habilitados, essa condição pode ser atendida.

**3. Efeito anti-competitivo do debarment**
Excluir fornecedores reduz o pool de licitantes elegíveis → facilita colusão tácita entre os restantes → licitações ficam menos competitivas. Este efeito é especialmente danoso quando o debarment atinge *todos* os membros de um cartel simultaneamente.

**4. Targeting seletivo é superior**
Debarment funciona melhor quando aplicado ao ring-leader ou beneficiário específico, não à totalidade dos coludidos. Punir todos os membros ao mesmo tempo destrói a competição remanescente.

**5. Problema de identificação corporativa (o problema phoenix)**
Autores explicitam: "agentes de procurement frequentemente carecem de registro adequado de fornecedores criminosos" e "é difícil determinar quais membros de um grupo são partes da mesma empresa." Este é o mecanismo exato pelo qual phoenix firms evitam o debarment — exploram a incapacidade institucional de identificar continuidade corporativa via mudança de CNPJ.

### Calibração para o Contexto Brasileiro

| Característica | Predição do modelo | Relevância para Zelox |
|----------------|-------------------|----------------------|
| Municípios menores | Baixa competição → debarment pode funcionar | Mercado-alvo correto |
| CEIS sem integração CNPJ/QSA | Incapacidade de identificar grupos → phoenix eficaz | Justifica grafo societário |
| Horizonte longo de contratos (obras) | δ alto → deterrência funciona | Aditivos em obras de longa duração |

## Interpretação

⚠️ Interpretação do compilador.

**Validação do grafo societário como feature não-opcional:**
O modelo prediz que onde a identificação de grupos corporativos é difícil, o debarment é ineficaz — e isso é precisamente a condição nos municípios menores sem capacidade institucional. O Zelox com grafo de sócios resolve exatamente o bottleneck que Auriol & Søreide identificam como falha estrutural do sistema.

**Inversão da prioridade do produto:** Se o laudo por CNPJ é o MVP e o grafo vem depois, o argumento de Auriol & Søreide sugere que o grafo não é feature de expansão — é o que faz o produto funcionar no longo prazo como deterrência. No curto prazo (advocacia, evidência forense), CNPJ basta. Para impacto sistêmico, grafo é necessário.

## Verificação adversarial

**Claim mais fraco:** modelo teórico sem calibração empírica no Brasil. Parâmetros (p, d, δ, V) não são estimados — apenas análise de sensibilidade qualitativa.

**O que o paper NÃO diz:** não mede taxa real de evasão via phoenix; não testa empiricamente em dados brasileiros; não quantifica o tamanho do efeito anti-competitivo do debarment.

**Prior work:** Cerrone et al. (2021) — evidência experimental que confirma o efeito anti-competitivo de debarments curtos.

## Quality Gate
- [x] Wikilinks tipados: validates/relates
- [x] Instance→class: predições são teóricas, não empíricas — calibração ao Brasil é interpretação
- [x] Meta-KB separado: implicações Zelox em Interpretação
- [x] Resumo calibrado: stub parcialmente verificado mencionado

## Conexões

- emerge-para: [[procurement-phoenix-graph-architecture]] ON "problema de identificação corporativa (Auriol & Søreide) = bottleneck que o grafo de sócios resolve"
- extends: [[debarment-evasion-phoenix-firms]] ON "fornece o modelo teórico de quando/por que phoenix evasion é racional e quando debarment falha estruturalmente"
- relates: [[debarment-collusion-experimental]] ON "Cerrone et al. confirma experimentalmente o efeito anti-competitivo que Auriol & Søreide predizem teoricamente"
- relates: [[audit-risk-rent-extraction]] ON "Zamboni & Litschig: auditoria funciona onde accountability local é fraca — mesmo mercado onde Auriol & Søreide dizem debarment pode funcionar"
- relates: [[procurement-manipulation-signals]] ON "grafo societário (Villamil 2024) resolve o problema de identificação corporativa que Auriol & Søreide identificam como falha estrutural"

## Fontes

- [Auriol & Søreide (2017)](../../raw/papers/auriol-soreide-2017-economic-analysis-debarment.md) — IRLE 50:36-49. Modelo teórico de efeitos de mercado do debarment; baixa competição = condição necessária; problema de identificação corporativa = vulnerabilidade estrutural. ⚠️ Parcialmente verificado via PDF aberto.
