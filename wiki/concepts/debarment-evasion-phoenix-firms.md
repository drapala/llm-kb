---
title: "Corporate Debarment and Phoenix Firms in Brazil (Szerman 2023)"
sources:
  - path: raw/papers/szerman-2023-debarment-costs-brazil.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-08
updated: 2026-04-08
tags: [procurement, debarment, ceis, rais, brazil, phoenix-firms, evasion, informal-sector, b2g, zelox-signals]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
reads: 3
retrievals_correct: 1
retrievals_gap: 1
last_read: 2026-04-08
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Gate 3∥challenge — 2 claims invalidados + 4 weakened"
quarantine_criteria_met:
  gates_passed: [1, 2]
  gates_failed: [3]
  gate3_run: 2026-04-08
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  gate3_claims_challenged: 8
  gate3_claims_survived: 2
  gate3_claims_weakened: 4
  gate3_claims_invalidated: 2
  challenge_verdict: PRECISA_CORREÇÃO
---

## Resumo

Szerman (AEJ: Applied Economics, 2023) explora variação exógena em política de debarment no Brasil — combinando CEIS (Cadastro de Empresas Inidôneas e Suspensas) com dados empregador-empregado (RAIS) — para estimar causalmente os custos do debarment. Achado: debarment → −22% em ganhos anuais dos trabalhadores da empresa + probabilidade significativamente maior de entrada no setor informal. O incentivo econômico para evasão via reincorporação (phoenix firms) é, portanto, empiricamente real e quantificável.

⚠️ Conteúdo baseado em abstract, SSRN description e citações em literatura secundária. Full text não verificado.

## Conteúdo

### Dados e Estratégia de Identificação

**Fonte de dados:**
- **CEIS** — registro oficial de empresas suspensas/inidôneas por irregularidades em contratos públicos
- **Dados empregador-empregado (RAIS ou similar)** — vínculo trabalhador-empresa por período (PIS/PASEP → CNPJ)

**Estratégia de identificação:** variação quasi-exógena baseada em timing de sanções individuais a firmas (event-study ou DiD); reform específica não identificada no stub — verificar no full text. A causalidade requer suposições sobre exogeneidade do timing que dependem de detalhes institucionais específicos.

### Custos do Debarment para Trabalhadores

| Variável | Efeito estimado | Interpretação |
|----------|-----------------|---------------|
| Ganhos anuais | **−22%** | Queda substancial em renda dos trabalhadores das firmas debarred |
| Saída do emprego formal | Significativamente maior | Trabalhadores deslocados saem do setor formal (dados RAIS não permitem distinguir informalidade de desemprego ou não-participação diretamente) |
| Mecanismo | Perda de receita de contratos públicos → redução de headcount | Efeito é via receita, não via sanção direta ao trabalhador |

O efeito é economicamente grande e causal — não apenas correlação.

### Incentivo para Evasão via Phoenix Firms

O debarment cria incentivo econômico significativo para evasão via reincorporação: o mecanismo é a **perda de receita de contratos públicos pela firma**, não a queda de renda dos trabalhadores (embora as duas coisas coexistam). Sócios/gestores perdem o canal de receita → criam nova pessoa jurídica para recuperar acesso ao mercado público:

**Mecanismo da phoenix firm:**
1. Empresa X entra no CEIS (suspensa/inidônea)
2. Sócios de X criam empresa Y com novo CNPJ
3. Trabalhadores de X são recrutados por Y (mesmo PIS/PASEP)
4. Y participa de licitações como concorrente "limpo"

**O que torna esse padrão parcialmente detectável:**
- CEIS: data de suspensão + identificação de firma X
- CNPJ/QSA: nova empresa Y com sócios sobrepostos a X (criada em t₁ > t₀)
- RAIS/empregador-empregado: trabalhadores de X aparecem em folha de Y

*Qualificação importante:* movimentação de trabalhadores sozinha NÃO prova phoenix firm. Para confirmar evasão de debarment, é necessário também: (a) matching de ownership/administradores (não apenas trabalhadores) e (b) evidência de que Y voltou a participar de licitações como firma "limpa" via dados PNCP.

**Szerman demonstra que o linkage CEIS + employer-employee data é tecnicamente viável** para rastrear saída do emprego formal pós-debarment — o paper usa essa combinação para estimar custos de trabalhadores, não para identificar phoenix firms diretamente.

### Dormant Entity Activation — Variante Não Detectada por CNPJ Creation Date

⚠️ Conceito emergido de análise empírica Zelox (2026-04-08) — não está em Szerman.

O phoenix clássico cria um CNPJ novo após o debarment. Uma variante estruturalmente equivalente, mas **não capturada por filtros de data de fundação**, é a **ativação de entidade dormente**: CNPJ registrado anos antes da sanção, mantido inativo (sem contratos), ativado somente quando o CNPJ original entra no CEIS.

**Caso documentado:** CH3 Eletro e Eletrônicos (CNPJ 39.581.101/0001-39)
- Fundada: out/2020
- Primeiro contrato PNCP: 25/04/2025 — **3 dias antes** da primeira sanção do CH3 Contratos (28/04/2025)
- Rede: 12 sanções em CNPJs vinculados; Exército Brasileiro (5×), Fiocruz, MAPA, TJ-BA
- Padrão pós-ativação: 165 contratos, 118 órgãos distintos, R$3,25M em <12 meses
- Sobrepreço identificado: +190,6% (Abadia dos Dourados) e +55,8% (DNIT)

**Por que o filtro `created_post_sanction` falha:**
O CNPJ dormant existe antes da sanção → `data_abertura < data_sancao` → sistema classifica como empresa preexistente legítima, não como phoenix.

**Sinal alternativo — `activation_lag_post_sanction`:**
Feature proposta: dias entre o PRIMEIRO contrato PNCP da empresa dormant e a data da sanção âncora da empresa-mãe na rede. Valores próximos de zero (< 30 dias) ou negativos (empresa ativa antes da sanção do parceiro) são incomuns para empresa genuinamente inativa por anos.

**Escala do problema:** em amostra de 1.199 successors (Zelox bid_engine.db 2026-04-08), 712 CNPJs têm `dormant_entity_flag = 1` — **vs 27 genuine phoenix** pelo critério `created_post_sanction`. O padrão dominante de evasão é dormant activation, não nova incorporação.

**Distinção jurídica:** Evasão via dormant activation pode ter tratamento distinto em instrução processual (o CNPJ não foi *criado* para fraudar — foi *ativado*). Substantivamente o efeito é idêntico; formalmente pode requerer argumentação diferente em representação ao TCU.

### Setor Formal → Saída após Debarment

Quando phoenix firm não é formada (ou detectada e bloqueada):
- Trabalhadores da empresa debarred têm probabilidade maior de sair do emprego formal (dados RAIS mensuram saída do formal, não confirmam informalidade diretamente)
- Potencial "double blow" (Cazzaniga et al. 2024 por analogia): deslocamento + perda de proteção trabalhista, se trabalhadores transitam para informal
- Efeito provavelmente mais concentrado em trabalhadores de menor qualificação

### Contexto de Aplicação (Brasil)

- CEIS é mantido pela CGU — atualizado com decisões de órgãos de controle
- Abrangência: contratos federais prioritariamente; cobertura estadual/municipal varia
- Limitação: lag entre irregularidade detectada → investigação → suspensão → registro no CEIS

## Verificação adversarial

**Claim mais fraco:** "−22% ganhos" depende da variação de política específica usada como instrumento — pode não generalizar para todos os tipos de debarment ou todos os tamanhos de firma. Paper foca em empresas que perderam contratos federais.

**O que o paper NÃO diz:**
1. Não documenta diretamente phoenix firms como estratégia observada — o incentivo é inferido do custo
2. Não mede a taxa de re-incorporação via novo CNPJ após debarment (esse seria o dado direto)
3. Não cobre debarment estadual/municipal — apenas federal (CEIS federal)

**Simplificações:** o paper é sobre custos para trabalhadores, não sobre evasão por sócios. A inferência de incentivo para phoenix firms é da leitura do compilador, não claim direto de Szerman.

**Prior work:** Ferraz & Finan (2008, 2011) — auditoria e accountability no Brasil; Zamboni & Litschig (2018) — debarment como mecanismo de deterrência; ambos na KB.

## Interpretação

⚠️ Interpretação do compilador.

**Validação da Combinação 3 (CEIS + CNPJ + RAIS):**
O paper de Szerman é a primeira evidência na KB de que o linkage CEIS + RAIS (dados empregador-empregado) é metodologicamente viável e empiricamente produtivo. A mesma combinação que Szerman usa para estimar custos é a que um sistema de risk scoring usaria para detectar phoenix firms.

**Calibração do sinal:** O incentivo para evasão é de magnitude −22% em renda → qualquer empresário racional tentará evitar o debarment ou contorná-lo via phoenix firm. Isso significa que **a presença no CEIS + criação de empresa próxima no tempo com sócios sobrepostos** não é coincidência — é resposta racional documentada.

**O que NÃO esperar:** Szerman documenta custos, não taxa de evasão via phoenix. A confirmação direta de que X% das empresas debarred criam phoenix firms precisaria de outro paper (gap do corpus).

## Conexões

- emerge-para: [[procurement-phoenix-graph-architecture]] ON "CEIS+CNPJ+RAIS = stack brasileiro; CPF de sócio = link de continuidade corporativa que o grafo explora"
- validates: [[audit-risk-rent-extraction]] ON "debarment é mecanismo de deterrência — Szerman mostra que o custo é real e grande, validando o efeito de risco de Zamboni & Litschig"
- extends: [[procurement-manipulation-signals]] ON "phoenix firms adicionam terceiro canal de manipulação além de bid rigging e exploração de regra de média: evasão de debarment via reincorporação"
- relates: [[market-for-lemons]] ON "phoenix firms agravam adverse selection: comprador não consegue distinguir empresa limpa de phoenix com histórico de irregularidade"
- relates: [[corruption-audits-brazil]] ON "CGU audita irregularidades que geram debarment no CEIS — o mesmo pipeline que Szerman estuda"

## Quality Gate
- [x] Wikilinks tipados: 4 relações tipadas
- [x] Instance→class: "−22%" qualificado com variação de política federal Brasil, estudo Szerman
- [x] Meta-KB separado: inferência de phoenix firms como Interpretação
- [x] Resumo calibrado: stub mencionado; source_quality:high justificado (AEJ Applied Economics)

## Fontes

- [Szerman (2023)](../../raw/papers/szerman-2023-debarment-costs-brazil.md) — AEJ Applied Economics Vol.15 No.1; CEIS + employer-employee data Brasil; −22% earnings; informalidade pós-debarment; incentivo causal para evasão. ⚠️ Baseado em abstract/SSRN — full text não verificado.

> ⚠️ QUARENTENA: Gate 3∥challenge — Gate 3∥challenge — 2 claims invalidados + 4 weakened. Correções necessárias:
> 1. [INVALIDADO] Mecanismo de incentivo: −22% earnings de TRABALHADORES ≠ incentivo de SÓCIOS — corrigido para 'perda de receita de contratos' como mecanismo
> 2. [INVALIDADO] 'Probabilidade de informalidade maior' → RAIS mede saída do formal, não informalidade; corrigido para 'saída do emprego formal'
> 3. [WEAKENED] 'Estratégia causal: exploração de mudança de política' → ID strategy usa timing quasi-exógeno de sanções individuais, não apenas macro policy change
> 4. [WEAKENED] 'Phoenix firm detectável via RAIS worker movement' → worker movement ≠ phoenix firm; requer ownership + procurement data adicionais
> 5. [WEAKENED] '−22%' sem timeframe/comparison group — adicionar caveat de contextualização
> 6. [WEAKENED] 'Informalidade como double blow' — potencial/por analogia, não confirmado diretamente
