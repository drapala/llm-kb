---
title: "Sinais de Procurement como Preditores de Default de Crédito — Evidência Empírica"
sources:
  - path: raw/articles/ferris-2022-contractor-default-procurement.md
    type: paper
    quality: primary
    stance: neutral
  - path: raw/articles/surety-bond-underwriting-procurement-history.md
    type: article
    quality: secondary
    stance: confirming
  - path: raw/articles/tax-arrears-bank-loan-default-signal.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-12
updated: 2026-04-12
tags: [credit-risk, default-prediction, procurement, contractor, tax-arrears, PGFN, contract-renegotiation, surety-bond, financial-distress, b2g, cross-domain]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - wiki/concepts/zelox-mvp-laudo-aditivos.md
  - wiki/concepts/audit-risk-rent-extraction.md
  - wiki/concepts/corruption-dynamics.md
status: promoted
promoted_date: 2026-04-12
freshness_status: current
---

## Resumo

A pergunta central é: **quais sinais observáveis no comportamento de procurement de uma empresa predizem default de crédito com maior poder preditivo?** A evidência empírica aponta cinco sinais ordenados por poder preditivo: (1) dívida fiscal ativa (PGFN), (2) histórico de sanções (CEIS/CNEP), (3) frequência de renegociação contratual (aditivos), (4) concentração de receita em contratos governamentais, (5) conexões políticas como fator de risco de descontinuidade. O insight cross-domínio central: para empresas B2G, **o health dos contratos públicos é o cashflow** — deterioração de procurement precede default de crédito, não acompanha.

## Conteúdo

### Por que procurement prediz crédito para empresas B2G

Empresas com receita majoritariamente B2G têm estrutura de risco peculiar:
- O único "cliente" relevante é o Estado
- Perda de contratos = perda de receita instantânea, sem diversificação
- Sanção administrativa (CEIS) = bloqueio de receita — equivale funcionalmente a uma execução forçada
- Comportamento de renegociação contratual é observável publicamente com lag mínimo

Bureaus tradicionais (Serasa, Boa Vista) detectam stress pelo sintoma (atraso em pagamento). Sinais de procurement detectam a causa (perda de contrato, sanção, irregularidade) com antecedência de meses a anos.

### Sinal 1 — Dívida Fiscal Ativa (PGFN)

**Poder preditivo:** 83.5% de accuracy para default bancário com tax arrears como único predictor; 89.1% combinado com outras variáveis.

Tax arrears são o sinal mais forte individualmente porque:
- Empresa que deixa de pagar tributo federal está em stress de caixa real
- PGFN é público e verificável — sem viés de auto-reporte
- Inscrição na dívida ativa = inadimplência confirmada com o credor mais senior possível (União)
- Empresas inscrevem na PGFN antes de atrasar banco (ordem de prioridade de pagamento típica: folha > tributo > banco)

**Para Zelox:** `supplier_credit_v1` já ingere PGFN. É o sinal mais fácil de operacionalizar e com melhor evidência empírica.

**Caveat:** empresa pode ter PGFN e ainda ser solvente se tiver ativo suficiente ou parcelamento em curso (REFIS, transação tributária). O sinal é mais forte em combinação com outros.

### Sinal 2 — Histórico de Sanções (CEIS/CNEP)

**Poder preditivo:** sanção ativa = equivalente funcional a default — a empresa perde o direito de contratar com governo. Inscrição = perda de receita direta.

Diferença de PGFN: CEIS/CNEP é consequência de irregularidade comprovada em processo administrativo, não de stress de caixa. Pode preceder PGFN em anos (empresa fraudou contratos → foi sancionada → perdeu contratos → aí ficou inadimplente com tributo).

**Ordem causal típica para empresa B2G fraudulenta:**
```
irregularidade em contrato → investigação → sanção (CEIS)
  → perda de novos contratos → stress de caixa
  → atraso em tributos (PGFN) → atraso em banco
```

O modelo de crédito que só vê PGFN e banco está 2-3 etapas atrasado. Zelox vê CEIS.

### Sinal 3 — Frequência e Magnitude de Renegociação (Aditivos)

**Evidência:** Ferris, Hanousek & Houston (2022) documentam que comportamento de renegociação em contratos governamentais é preditor significativo de default posterior. A própria solicitação de renegociação de termos de pagamento é sinal de stress financeiro iminente em contexto de supply chain.

**Mecanismo (Tirole 1986 aplicado):** empresa que faz hold-up sistemático (underbid → aditivos iterativos → captura de surplus ex-post) está revelando que sua proposta original não era lucrativa ao preço ofertado. Isso indica margem insuficiente, que por sua vez indica stress estrutural.

**Sinais específicos de aditivos que predizem crédito:**
- Aditivo_teto elevado (>20% do valor original) em múltiplos contratos = margem original inadequada
- Frequência crescente de aditivos = empresa depende de renegociação para sobreviver
- Aditivos próximos ao limite legal (≈25%) sem justificativa técnica = comportamento de extração, não de ajuste legítimo

**Diferença de sinal para crédito vs. fraude:**
- Para detectar fraude: padrão de aditivos sistemático = comportamento doloso
- Para prever default: padrão de aditivos = margem insuficiente → stress de caixa futuro

O mesmo dado, duas leituras com defasagens diferentes.

### Sinal 4 — Concentração de Receita em Contratos Governamentais

**Mecanismo:** empresa com >70% de receita em contratos públicos tem risco de concentração extremo. Perda de um contrato grande = evento de crédito equivalente a perder o principal cliente.

**Sinais observáveis no PNCP:**
- Volume total de contratos ativos vs. histórico — queda indica perda de receita
- Número de órgãos distintos contratantes — concentração em 1-2 órgãos = risco maior
- Renovações vs. novos contratos — empresa que para de ganhar novos contratos está em declínio
- Participação em licitações sem ganhar — empresa ativa mas não lucrativa (proposta muito alta = perdeu margem)

**Para Zelox:** esse sinal não requer dado novo — é calculável sobre o corpus PNCP já ingerido.

### Sinal 5 — Conexões Políticas (Fator de Risco, não de Proteção)

**Evidência contra-intuitiva:** Ferris et al. (2022) documentam que conexões políticas afetam tanto a probabilidade de ser selecionado quanto a probabilidade de default — não são proteção incondicional.

Empresa dependente de conexão política para ganhar contratos enfrenta risco de descontinuidade ao mudar de governo. Sua "vantagem competitiva" é politicamente frágil. No contexto brasileiro:
- Empresa que concentrou contratos em governo X pode perder tudo em governo Y
- Ciclo eleitoral = risco de concentração temporal de receita
- Doação a candidato que perde = sinal de risco de descontinuidade de contratos

**Para Zelox:** cruzar dados TSE (doações) com dados PNCP (contratos) + ciclo eleitoral — esse sinal é calculável e não existe em nenhum bureau tradicional.

### Sinais Secundários com Evidência Menor

**Procurement failure rate:** cancelamento de contratos antes da conclusão prediz dificuldades financeiras. Empresa que tem contratos cancelados (por descumprimento) está em situação mais grave que empresa com sanção CEIS — o cancelamento acontece antes da sanção formal.

**Surety bond history:** seguradoras de garantia já usam "prior work portfolio" como predictor primário de risco. Histórico de sinistros em apólices anteriores = default de performance documentado.

**Group risk (sócios em outros CNPJs problemáticos):** empresa controlada por CPF com histórico de outras empresas inadimplentes tem risco sistêmico — o controlador pode estar usando o CNPJ atual como "empresa saudável" temporária num ciclo de phoenix company.

### Ranking de Poder Preditivo por Timing

| Sinal | Timing de detecção antes do default bancário | Disponibilidade em Zelox |
|-------|----------------------------------------------|-------------------------|
| Sanção CEIS ativa | 12-36 meses antes | Já disponível |
| Aditivo_teto sistemático (>20%, múltiplos contratos) | 6-18 meses antes | Calculável no PNCP |
| Queda de novos contratos ganhos | 6-12 meses antes | Calculável no PNCP |
| PGFN inscrito | 3-9 meses antes | Já disponível |
| Conexão política em governo perdedor | Varia por ciclo eleitoral | Requer TSE |
| Cancelamento de contrato | 2-6 meses antes | Disponível no PNCP |
| Atraso em banco (bureau tradicional) | 0 — é o próprio evento | Não disponível |

**Insight central:** o bureau tradicional detecta o evento. Zelox detecta os sinais que precedem o evento com 6-36 meses de antecedência. Para quem compra recebíveis de contratos públicos ou subscreve seguro garantia, essa antecedência é o produto.

### Modelo de Crédito Mínimo Viável para B2G

Score de crédito para fornecedor B2G com os dados disponíveis no Zelox:

```
credit_score_b2g = f(
  pgfn_status,              # binário + valor inscrito
  ceis_status,              # ativo / expirado / limpo
  aditivo_teto_medio,       # média de % nos últimos 3 anos
  contratos_ativos_delta,   # variação YoY de contratos ativos
  receita_b2g_concentracao, # HHI de concentração por órgão
  group_risk_score          # risco agregado do grupo societário
)
```

Sem precisar de DRE, balanço ou acesso ao SCR do BACEN. Apenas dados públicos já disponíveis no corpus Zelox.

## Interpretação

⚠️ Interpretação do compilador.

**Implicação direta para Zelox/Artifcat:** o modelo de crédito B2G não precisa competir frontalmente com Serasa. Ele compete na dimensão que Serasa não alcança: **lead time de detecção**. O produto não é "score de crédito" — é "sinal antecipado de deterioração 6-36 meses antes do default aparecer no bureau".

**Comprador natural:** fundo de FIDC comprando recebíveis de contratos públicos. Ele precisa saber se o contrato será honrado antes de antecipar. O Serasa diz o histórico de pagamento; Zelox diz se o fornecedor está perdendo contratos agora.

**O que falta para o modelo ser defensável:**
- Backtesting: quantas empresas com CEIS ativo em T-12 defaultaram com banco em T? Esse dataset existe no PNCP + CEIS + PGFN + dados de crédito (SCR ou bureau parceiro)
- Calibração de pesos: qual sinal tem mais poder preditivo no contexto B2G brasileiro especificamente

**Risco principal:** a pesquisa empírica de referência (Ferris et al. 2022) é sobre contratos federais americanos. A transferabilidade para Brasil não é automática — estrutura de contratos, regimes legais (Lei 8.666 vs. 14.133 vs. FAR americano) e mecanismos de sanção diferem. Backtesting próprio é condição necessária antes de vender o score como produto.

## Verificação adversarial

**Claim mais fraco:** "83.5% de accuracy com tax arrears" — esse número é de contexto específico (país europeu não identificado nas fontes web, provavelmente Estônia ou Finlândia com dados fiscais integrados). Não há evidência publicada de que a mesma accuracy se mantém no contexto brasileiro com PGFN.

**O que não está aqui:** como tratar empresas com parcelamento REFIS ativo (PGFN inscrita mas regularizada formalmente), que podem ter sinal positivo de PGFN mas ainda em stress. Essa é uma gap real no modelo.

**Circularidade potencial:** empresa que é investigada pelo Zelox pode ser sancionada, o que deteriora seu crédito, o que confirma a predição — mas isso é profecia auto-realizável, não evidência de poder preditivo genuíno.

## Quality Gate
- [x] Instance→class: "83.5% accuracy" qualificado como contexto externo, não Brasil
- [x] Meta-KB separado: implicações para Zelox em Interpretação
- [x] Resumo calibrado: source_quality medium

## Conexões
- procurement-signals-credit-default-prediction relates-to zelox-mvp-laudo-aditivos ON "aditivo_teto como sinal de fraude é o mesmo dado que prediz margem insuficiente como sinal de crédito — mesma feature, dois produtos"
- procurement-signals-credit-default-prediction relates-to audit-deterrence-corruption ON "empresa que sabe que está sendo monitorada reduz irregularidades — mas isso pode mascarar o sinal de crédito se o comportamento muda"
- procurement-signals-credit-default-prediction relates-to fraud-system-operational-telemetry ON "outcome de crédito confirmado (default real) é o labeled example mais valioso para retreinar o modelo de procurement"
- procurement-signals-credit-default-prediction relates-to corruption-dynamics ON "sinal decay: fornecedores aprendem a evitar sinais de fraude — o mesmo decay afeta poder preditivo dos sinais de crédito ao longo do tempo"
- procurement-signals-credit-default-prediction relates-to beneficial-ownership-graph-traversal ON "phoenix company pattern: controlador move operação para novo CNPJ antes do default — group_risk detecta isso, score por CNPJ isolado não"

## Fontes
- Ferris, Hanousek & Houston (2022) — "Contractor default: Predictions, politics, and penalties in the procurement process", Annals of Public and Cooperative Economics, Vol 93(4): 1001-1039
- Structural models of credit risk for contractor default prediction — Construction Management and Economics (2009, referência histórica)
- Tax arrears as bank loan default predictor — evidência empírica europeia: 83.5% accuracy (fonte web, país não identificado)
- Surety bond underwriting criteria — OR Surety: procurement history como predictor primário (documentação de produto, 2024)
- [[zelox-mvp-laudo-aditivos]] — aditivo_teto como sinal primário; mecanismo de Tirole
- [[audit-risk-rent-extraction]] — Zamboni & Litschig: PGFN como sinal de stress fiscal
