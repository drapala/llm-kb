---
title: "Procurement Manipulation and Bid Rigging (Decarolis et al. 2020)"
sources:
  - path: raw/papers/decarolis-2020-procurement-manipulation.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/villamil-kertesz-fazekas-2024-collusion-corporate-networks.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-04
updated: 2026-04-08
tags: [corruption, procurement, bid-rigging, italy, sweden, b2g, manipulation, political-connections, network-analysis, zelox-signals]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 3
retrievals_correct: 3
retrievals_gap: 0
last_read: 2026-04-12
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Gate 3∥challenge — 1 claim invalidado (sinal preço vs referência) + 5 weakened após update Villamil 2024"
quarantine_criteria_met:
  gates_passed: [1, 2]
  gates_failed: [3]
  gate3_run: 2026-04-08
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  gate3_claims_challenged: 8
  gate3_claims_survived: 2
  gate3_claims_weakened: 5
  gate3_claims_invalidated: 1
  challenge_verdict: PRECISA_CORREÇÃO
---

## Resumo

Decarolis, Fisman, Pinotti & Vannutelli (2020) documentam manipulação sistemática em licitações públicas italianas usando dados que ligam resultados de procurement a conexões políticas de empresas. Empresas conectadas vencem 20-30% mais frequentemente e pagam preços 4-8% maiores. Dois canais de manipulação: bid rigging com colusão e exploração da regra de exclusão por desvio de média. Review of Economic Studies 2020.

⚠️ Stub — full text não lido. Conteúdo baseado em abstract e descrição da NBER WP.

## Conteúdo

### Setting e Dados

**Contexto:** Licitações públicas italianas, 2000-2016. Itália usa "average-bid" auctions — propostas que desviam muito da média de preços são excluídas automaticamente. Esta regra cria um canal de manipulação específico.

**Identificação:** Conexões políticas medidas via sócios/diretores compartilhados entre empresas e funcionários públicos. Eleições criam variação temporal no valor das conexões (empresas conectadas ao partido perdedor perdem a vantagem pós-eleição).

### Resultados Principais

**Magnitude da vantagem de empresas conectadas (Decarolis et al. 2020, Itália):**
- Vencem **20-30% mais frequentemente** que empresas não-conectadas (magnitude relativa; específico ao contexto italiano)
- Preços **4-8% maiores** que vencedoras não-conectadas comparáveis (potencialmente conflation de prêmio de conexão política + markup de cartel — os dois mecanismos coexistem no paper)
- O prêmio cresce com a força da conexão política

**Evidência de causalidade:** Pós-eleição, empresas conectadas ao partido perdedor perdem a vantagem — resultado *consistente com* conexões como instrumentos ativos (não prova definitiva; alternativa: outros fatores que mudam com eleições). Gemini confirma como identificação DiD padrão na literatura.

### Os Dois Canais de Manipulação

**Canal 1 — Bid Rigging:**
Empresas conectadas + parceiras coludentes coordenam propostas para excluir competição:
- Parceiras submetem propostas perdedoras (falsas) para criar aparência de competição
- Propostas coordenadas para garantir que o vencedor desejado fique dentro da faixa de aceitação

**Canal 2 — Exploração da Regra de Média:**
Coordenando múltiplas propostas, as empresas conectadas *deslocam* o ponto de referência (a média) para excluir concorrentes de baixo custo e honestos. Um grupo grande de empresas coludentes submete propostas que concentram a média em torno do preço-alvo delas.

### Classificação dos Sinais Detectáveis

| Sinal | Fonte | Detectável em dados? |
|-------|-------|---------------------|
| Empresas com sócios sobrepostos submetendo propostas | Bid rigging | Sim (dados de CNPJ) |
| Preços agrupados próximos à média de exclusão | Exploração de regra | Sim (distribuição de lances) |
| Empresa vencedora com preço sistematicamente acima de referência de mercado (SINAPI, pesquisa de preços) — não acima dos concorrentes (que em menor-preço seriam eliminados) | Canal 1+2 | Sim (comparação com referência de mercado) |
| Mesmo fornecedor vencendo >50% de contratos por categoria/município | Concentração | Sim (histórico de winners) |

### Confirmação Cross-Country: Temporal Multiplex Networks (Villamil, Kertész & Fazekas 2024)

Evidência independente com dados suecos (2010-2015) usando redes temporais multiplex:

**Dois layers combinados:**
- **Ownership layer:** grafo de sócios compartilhados entre empresas (análogo CNPJ)
- **Co-bidding layer:** grafo de empresas que submetem propostas no mesmo processo (análogo PNCP)

**Achados (Scientific Reports, 2024):**
- Mercados com empresas mais centrais no ownership network → maior incidência de **single bidding** (apenas 1 licitante) e **missing bidders** (concorrentes esperados que não aparecem)
- Empresas com alta centralidade em ownership network vencem contratos significativamente mais frequentemente, controlando por características da firma
- O efeito é temporal: relacionamentos de ownership *anteriores* ao processo licitatório predizem o resultado do processo

**Implicação metodológica:** o `rede_empresas_score` não precisa verificar apenas sobreposição estática de sócios no momento da licitação — a centralidade histórica no grafo de ownership é *sugestiva* de risco de colusão. Isso é *consistente com* usar grafos societários longitudinais (dados suecos; alta centralidade pode ter explicações alternativas além de colusão). Não generaliza automaticamente para o contexto legal brasileiro.

*Qualificação: dados suecos — regras de licitação diferentes do Brasil. Mecanismo de rede se generaliza, mas thresholds específicos precisam calibração com dados PNCP brasileiros.*

## Interpretação

⚠️ Interpretação do compilador.

**Paper mais diretamente relevante para feature engineering do Zelox:**

**Sinal "rede de empresas":** Decarolis et al. identificam que bid rigging requer coordenação entre empresas. Empresas com sócios, endereços ou registros CNPJ sobrepostos que submetem propostas no mesmo processo licitatório são o sinal mais direto de colusão.

**Contexto brasileiro:** Brasil usa formato diferente (menor preço vence na Lei 8.666, sem regra de exclusão por média). Mas os canais de manipulação análogos existem:
- "Concorrentes" controlados pelo mesmo grupo de ownership submetem propostas perdedoras
- Coordenação de preços entre empresas relacionadas
- Não-qualificação técnica estratégica de concorrentes genuínos

**Validação cruzada:** Decarolis et al. usam conexões políticas como ground truth de corrupção. Para o Zelox, os dados de auditoria CGU (Ferraz & Finan) podem servir como ground truth análogo — validar se os sinais de rede de empresas predizem achados reais de irregularidades.

**Feature prioritária:** `rede_empresas_score` = fração de concorrentes no processo que compartilham sócios/endereço/telefone com o vencedor. Threshold > 30% concorrentes relacionados ao vencedor = red flag de bid rigging.

## Quality Gate
- [x] Wikilinks tipados: validates/relaciona
- [x] Instance→class: "20-30%" e "4-8%" — específicos ao contexto Decarolis et al. Itália 2000-2016
- [x] Meta-KB separado: Zelox feature engineering em Interpretação
- [x] Resumo calibrado: ⚠️ stub mencionado

## Conexões

- validates: [[corruption-audits-brazil]] ON "identificação de bid rigging como canal de corrupção em procurement; CGU audita os mesmos tipos de irregularidade"
- relates: [[procurement-renegotiation]] ON "aditivos (hold-up) e bid rigging são duas estratégias de extração — Tirole modela a primeira, Decarolis a segunda"
- relates: [[market-for-lemons]] ON "bid rigging agrava adverse selection: compradores não conseguem distinguir proposta genuína de colusiva"
- emerge-para: [[procurement-phoenix-graph-architecture]] ON "temporal multiplex ownership+co-bidding (Villamil 2024) = estrutura empiricamente validada que ancora a arquitetura de detecção de phoenix"
- relates: [[audit-risk-rent-extraction]] ON "Zamboni & Litschig documenta redução de irregularidades via auditoria; Decarolis documenta quais irregularidades existem"

## Fontes

- [Decarolis et al. (2020)](../../raw/papers/decarolis-2020-procurement-manipulation.md) — RES 87(6), 2465-2502. Licitações italianas 2000-2016, +20-30% win rate empresas conectadas, +4-8% preços, bid rigging + exploração de regra de média. ⚠️ Stub — texto completo não lido.
- [Villamil, Kertész & Fazekas (2024)](../../raw/papers/villamil-kertesz-fazekas-2024-collusion-corporate-networks.md) — Scientific Reports Vol.14. Dados suecos 2010-2015. Temporal multiplex (ownership + co-bidding): centralidade no ownership network prediz single bidding e win rate. Confirmação cross-country independente. ⚠️ Baseado em abstract/descrição secundária.

> ⚠️ QUARENTENA: Gate 3∥challenge — 1 invalidado + 5 weakened. Correções aplicadas (verificar):
> 1. [INVALIDADO] 'Preço acima dos concorrentes' → corrigido para 'preço acima de referência de mercado' (SINAPI, pesquisa de preços)
> 2. [WEAKENED] Magnitudes 20-30%/4-8% qualificadas — podem conflate connection premium + cartel markup
> 3. [WEAKENED] 'Mostra que conexões são instrumentos ativos' → 'consistente com'
> 4. [WEAKENED] Centralidade de rede como proxy de colusão → 'sugestiva', não definitiva
> 5. [WEAKENED] Generalização cross-country dos achados suecos → qualificada
> 6. [WEAKENED] '20-30%' sem spec de modelo/fonte → contexto Decarolis Itália adicionado