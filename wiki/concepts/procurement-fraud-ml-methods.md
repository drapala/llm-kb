---
title: "ML Methods for Procurement Fraud Detection — Systematic Review (Santos et al. 2025)"
sources:
  - path: raw/papers/santos-2025-ml-procurement-fraud-detection.md
    type: paper
    quality: secondary
    stance: confirming
created: 2026-04-08
updated: 2026-04-08
tags: [procurement, fraud-detection, machine-learning, collusion, bid-rigging, ensemble, systematic-review, b2g]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-08
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Gate 3∥challenge — 4 claims weakened"
quarantine_criteria_met:
  gates_passed: [1, 2]
  gates_failed: [3]
  gate3_run: 2026-04-08
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  gate3_claims_challenged: 9
  gate3_claims_survived: 5
  gate3_claims_weakened: 4
  gate3_claims_invalidated: 0
  challenge_verdict: PRECISA_CORREÇÃO
---

## Resumo

Santos, Santos, Castro & Carvalho (EPJ Data Science 2025) revisam sistematicamente 93 estudos peer-reviewed sobre detecção de fraude em procurement usando métodos data-driven (filtrados de 6.000+). Achado central: ensemble methods (Extra Trees, Random Forest, AdaBoost) atingem 81-95% accuracy para detecção de colusão/bid rigging. Statistical analysis domina detecção de favoritism. A combinação de dados de licitações + ownership/registro societário + emprego é a que produz melhores resultados.

⚠️ Conteúdo baseado em abstract e descrição secundária — full text não verificado. Classificado como source_quality:high por ser systematic review de 93 estudos primários.

## Conteúdo

### Escopo da Revisão

- **93 estudos** peer-reviewed incluídos (de 6.000+ inicialmente screened)
- Critério: uso de métodos data-driven (ML, estatística, redes) para detectar fraude em procurement público
- Cobre: collusion/bid rigging, favoritism, superfaturamento, phantom deliveries

### Tipos de Fraude e Metodologias

**Detecção de colusão/bid rigging (maioria dos estudos):**
- Ensemble methods dominam: Extra Trees, Random Forest, AdaBoost — accuracy **81-95%** (range reportado nos melhores estudos; variação por dataset e definição de colusão)
- Network analysis: ownership + co-bidding graphs (ver Villamil et al. 2024)
- Statistical screening: distribuição de preços, bid spread, coeficientes de variação

**Detecção de favoritism (31,18% dos estudos):**
- Statistical analysis é dominante — relação entre conexões políticas e resultados
- ML tem menor penetração: menos dados rotulados disponíveis

**Outros tipos:** superfaturamento (price benchmarking), phantom deliveries (dados de execução), bid suppression

### Dados Utilizados (em ordem de frequência)

1. **Procurement bidding data** — resultados, preços, participantes (PNCP equivalente)
2. **Ownership/company registration** — sócios, endereços (CNPJ equivalente)
3. **Employment data** — vínculo trabalhador-empresa (RAIS equivalente) — menos comum, crescente
4. **Graph databases** — redes de fornecedores construídas sobre os dados acima

### Desafios Metodológicos

**Escassez de ground truth:** cartéis são difíceis de confirmar em dados observacionais.
- Abordagem predominante: usar casos conhecidos de cartéis como positive labels (viés: só estudamos mercados com cartéis confirmados)
- Abordagens emergentes ainda experimentais: synthetic data generation, transfer learning — úteis conceitualmente mas codificam suposições que podem não se aplicar a outros contextos de procurement
- GNN (Graph Neural Networks) mostram transferência cross-country em estudo específico (Gomes et al. 2024), mas cross-country transferability em procurement é historicamente pobre por diferenças em regras legais, formatos de licitação e ontologias de dados entre países

**Limites de generalização:**
- Accuracy 81-95% é reportada em datasets com colusão confirmada — performance em dados não-rotulados é menor
- Regras de licitação variam por país → sinais específicos (ex: regra de média italiana) não são universais
- Brasil: Lei 8.666/14.133 tem mecanismos distintos da "average-bid" italiana

### Resultado cross-estudo

| Tipo de fraude | Melhor método | Accuracy range | Principal fonte de dados |
|----------------|---------------|----------------|--------------------------|
| Collusion/bid rigging | Ensemble ML | 81-95%* | Bidding data + ownership |
| Favoritism | Statistical | N/D | Political connections + contract data |
| Superfaturamento | Price benchmarking | N/D | Procurement prices + market reference |

## Verificação adversarial

**Claim mais fraco:** "81-95% accuracy*" — este range é de estudos com datasets onde colusão confirmada existe (viés de seleção: estudamos mercados onde sabemos que houve cartel). Comparabilidade cross-estudo é fraca: accuracy varia com balanceamento de classes, sampling case-control, e leakage. Em dados não-rotulados brasileiros, a performance real seria consideravelmente menor. O 31,18% para favoritism é um percentual de Santos et al. 2025 — não verificado em full text (stub).

**O que a revisão NÃO diz:**
1. Não especifica qual feature é mais preditiva para o contexto brasileiro (PNCP + CNPJ)
2. Não avalia modelos em dados de procurement aberto em tempo real — a maioria usa dados históricos
3. Não cobre a dimensão de "inexigibilidade" ou personalíssimo — que é o modelo de contratação diferente de licitação aberta

**Simplificações:** "93 estudos" inclui países e contextos muito diferentes. A generalização para o Brasil especificamente requer adaptar os sinais às regras da Lei 14.133.

**Prior work:** Decarolis et al. (2020), Olken (2007), Zamboni & Litschig (2018) — todos presentes na KB.

## Interpretação

⚠️ Interpretação do compilador.

**O que muda para um sistema de risk scoring brasileiro:**
A revisão confirma que os sinais de propriedade/rede (CNPJ + co-bidding) são os mais validados para collusion detection — não apenas teorizados em Decarolis. A combinação PNCP + CNPJ + grafos societários tem suporte sistemático de 93 estudos.

**Limitação crítica para o contexto B2G analytics:**
Nenhum dos 93 estudos revisados cobre especificamente a detecção de **underbidding intencional seguido de aditivo** (o mecanismo central do procurement-variety-gap). Este é um gap do campo que o procurement-variety-gap identificou a partir de teoria. A literatura empírica de ML ainda não modelou esse padrão.

## Conexões

- emerge-para: [[procurement-phoenix-graph-architecture]] ON "PNCP+CNPJ+RAIS validado como melhor stack em 93 estudos — âncora empírica da arquitetura"
- validates: [[procurement-manipulation-signals]] ON "ensemble ML (81-95% accuracy) confirma que ownership + co-bidding são os sinais mais detectáveis; sistematiza evidência de 93 estudos"
- validates: [[audit-risk-rent-extraction]] ON "tipos de irregularidades de Zamboni & Litschig (bid rigging, phantom firms, superfaturamento) são os mesmos targets dos 93 estudos"
- extends: [[procurement-variety-gap]] ON "lacuna identificada: nenhum dos 93 estudos modela underbidding + aditivo como padrão de fraude — gap do campo"

## Quality Gate
- [x] Wikilinks tipados: 3 relações tipadas
- [x] Instance→class: "81-95%" qualificado como range de melhores estudos com ground truth confirmado
- [x] Meta-KB separado: aplicação a risk scoring em Interpretação
- [x] Resumo calibrado: ⚠️ stub + source_quality:high justificada (revisão de 93 estudos primários)

## Fontes

- [Santos et al. (2025)](../../raw/papers/santos-2025-ml-procurement-fraud-detection.md) — EPJ Data Science Vol.14; revisão sistemática 93 estudos; ensemble 81-95% accuracy; collusion + favoritism; dados PNCP/CNPJ/RAIS equivalentes. ⚠️ Baseado em abstract/descrição secundária.

> ⚠️ QUARENTENA: Gate 3∥challenge — Gate 3∥challenge — 4 claims weakened. Correções necessárias:
> 1. [WEAKENED] '81-95% accuracy' como resumo cross-study → comparabilidade cross-estudo é fraca (balanceamento, sampling, leakage variam); aplicado parcialmente no corpo
> 2. [WEAKENED] '31,18% favoritism' → percentual não verificado em full text (stub); mencionar como 'Santos et al. reportam'
> 3. [WEAKENED] 'synthetic data + transfer learning' como 'solução emergente' → corrigido para 'abordagens ainda experimentais'
> 4. [WEAKENED] 'GNN cross-country promissor' → corrigido com caveat sobre barriers práticos; cross-country transfer histórico é pobre em procurement
