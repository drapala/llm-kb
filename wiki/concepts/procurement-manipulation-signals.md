---
title: "Procurement Manipulation and Bid Rigging (Decarolis et al. 2020)"
sources:
  - path: raw/papers/decarolis-2020-procurement-manipulation.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-04
updated: 2026-04-04
tags: [corruption, procurement, bid-rigging, italy, b2g, manipulation, political-connections, zelox-signals]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: false
---

## Resumo

Decarolis, Fisman, Pinotti & Vannutelli (2020) documentam manipulação sistemática em licitações públicas italianas usando dados que ligam resultados de procurement a conexões políticas de empresas. Empresas conectadas vencem 20-30% mais frequentemente e pagam preços 4-8% maiores. Dois canais de manipulação: bid rigging com colusão e exploração da regra de exclusão por desvio de média. Review of Economic Studies 2020.

⚠️ Stub — full text não lido. Conteúdo baseado em abstract e descrição da NBER WP.

## Conteúdo

### Setting e Dados

**Contexto:** Licitações públicas italianas, 2000-2016. Itália usa "average-bid" auctions — propostas que desviam muito da média de preços são excluídas automaticamente. Esta regra cria um canal de manipulação específico.

**Identificação:** Conexões políticas medidas via sócios/diretores compartilhados entre empresas e funcionários públicos. Eleições criam variação temporal no valor das conexões (empresas conectadas ao partido perdedor perdem a vantagem pós-eleição).

### Resultados Principais

**Magnitude da vantagem de empresas conectadas:**
- Vencem 20-30% mais frequentemente que empresas não-conectadas
- Pagam preços 4-8% maiores que vencedoras não-conectadas comparáveis
- O prêmio cresce com a força da conexão política

**Evidência de causalidade:** Pós-eleição, empresas conectadas ao partido perdedor perdem a vantagem — mostra que conexões são instrumentos ativos, não proxies de qualidade de empresa.

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
| Empresa vencedora com preço sistematicamente acima dos concorrentes | Canal 1+2 | Sim (comparação com referência) |
| Mesmo fornecedor vencendo >50% de contratos por categoria/município | Concentração | Sim (histórico de winners) |

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
- relates: [[audit-risk-rent-extraction]] ON "Zamboni & Litschig documenta redução de irregularidades via auditoria; Decarolis documenta quais irregularidades existem"

## Fontes

- [Decarolis et al. (2020)](../../raw/papers/decarolis-2020-procurement-manipulation.md) — RES 87(6), 2465-2502. Licitações italianas 2000-2016, +20-30% win rate empresas conectadas, +4-8% preços, bid rigging + exploração de regra de média. ⚠️ Stub — texto completo não lido.
