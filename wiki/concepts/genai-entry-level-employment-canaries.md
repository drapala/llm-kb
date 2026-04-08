---
title: "GenAI and Entry-Level Employment: Six Facts (Brynjolfsson et al., 2025)"
sources:
  - path: raw/papers/brynjolfsson-chen-2025-canaries-coal-mine-ai-employment.pdf
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-08
updated: 2026-04-08
tags: [labor-economics, ai, employment, entry-level, young-workers, usa, adp, canaries]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
quarantine: true
quarantine_created: 2026-04-08
quarantine_reason: "Gate 3∥challenge — 1 claim invalidado + 5 weakened (2 invalidações por model staleness — overridden)"
quarantine_criteria_met:
  gates_passed: [1, 2]
  gates_failed: [3]
  gate3_run: 2026-04-08
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  gate3_claims_challenged: 9
  gate3_claims_survived: 1
  gate3_claims_weakened: 5
  gate3_claims_invalidated: 3
  gate3_staleness_overrides: 2
  challenge_verdict: PRECISA_CORREÇÃO
---

## Resumo

Brynjolfsson, Chandar & Chen (Stanford/NBER, nov 2025) documentam seis fatos sobre efeitos empíricos da GenAI no mercado de trabalho americano usando dados de payroll da ADP (3,5–5M trabalhadores/mês, jan 2021–set 2025). Achado central: trabalhadores de início de carreira (22–25 anos) em ocupações AI-exposed sofreram declínio de –16% no emprego relativo (controlando choques firm-level), enquanto trabalhadores experientes nas mesmas ocupações permaneceram estáveis. Ajuste ocorre via quantidade de emprego, não via salários.

## Conteúdo

### Dataset

- **Fonte:** ADP, maior processadora de payroll dos EUA; ~25M trabalhadores em sua plataforma
- **Amostra analítica:** 3,5–5M trabalhadores/mês com earnings positivos, tempo integral, abaixo de 70 anos
- **Período:** jan 2021–set 2025 (conjunto consistente de firmas com dados em todos os meses)
- **Cobertura:** ~7.000 títulos padronizados; mapeados para SOC 2010 via ADP Research
- **Exposição a AI:** Eloundou et al. (2024) + Anthropic Economic Index (Handa et al., 2025) para automative vs augmentative

### Os Seis Fatos

**Fato 1 — Declínio de –16% relativo para jovens em ocupações AI-exposed**
- Trabalhadores 22–25 anos: –16% emprego relativo nas ocupações de maior exposição vs menor exposição (controlando firm-time effects)
- –6% absoluto de emprego (late 2022 → set 2025) para o quintil mais exposto nessa faixa etária
- Trabalhadores mais velhos nas mesmas ocupações: +6–9% no mesmo período
- Em ocupações de baixa exposição (ex: auxiliares de enfermagem): jovens e velhos com crescimento similar

**Fato 2 — Estagnação geral do emprego jovem desde late 2022**
- Emprego total continua crescendo; emprego de trabalhadores jovens estagnado desde late 2022
- Padrão inicia em late 2022/early 2023 — coincide com proliferação de ChatGPT (lançado nov 2022)
- Índice de exposição AI *não* previa quedas de emprego jovem em períodos anteriores (incluindo COVID-19)

**Fato 3 — Declínio concentrado em usos AUTOMATIVOS de AI, não AUMENTATIVOS**
- AI que automatiza tarefas → associada a queda de emprego jovem
- AI que aumenta trabalhadores → associada a *crescimento* de emprego jovem
- Classificação via Anthropic Economic Index: proporção de queries Claude que são "automative" vs "augmentative" por ocupação

**Fato 4 — Efeito persiste após controlar firm-time effects**
- –15 log-points de emprego relativo: quintil mais exposto vs menos exposto (22–25 anos)
- Efeito não explicado por choques industriais ou de firma que correlacionem com AI exposure e age sorting

**Fato 5 — Ajuste via emprego, não salários (wage stickiness)**
- Pouca diferença em tendências de salário anual por faixa etária ou quintil de exposição
- AI tem efeito maior sobre emprego do que sobre salários, pelo menos inicialmente
- "AI may boost wages for as many workers as it hurts"

**Fato 6 — Robusto a tech firms e ocupações teleworkable**
- Não explicado por: ocupações de tecnologia, remotabilidade, queda em college-education COVID-19
- Para non-college workers: experiência protege menos → divergência de emprego por AI exposure estende-se até os 40 anos

### Mecanismo Hipotético

AI substitui *conhecimento codificável* (book-learning, conhecimento digital corporativo) — a principal contribuição de trabalhadores de início de carreira. Conhecimento tácito, acumulado com experiência e não digitalizado, é protegido.

**Implicação:** firmas **reduzem contratações junior em vez de demitir incumbentes** (ajuste de menor fricção). Menos incentivos a treinar junior workers que podem mudar de empresa (Becker 1994).

Esta combinação explica: queda de emprego de jovens + estabilidade de salários + estabilidade de emprego de sêniors.

### Contexto do Campo

- AI capabilities jump: SWE-Bench 4.4% → 71.7% (2023–2024)
- LLM adoption at work: 46% trabalhadores EUA idade 18+ (jun/jul 2025, Hartley et al.)
- Confirmação independente com LinkedIn data: Hosseini & Lichtinger (2025), Klein Teeselink (2025) — resultados similares para EUA e UK
- Contraste: Humlum & Vestergaard (2025) — efeitos mínimos na Dinamarca (diferenças em instituições do mercado de trabalho?)

## Verificação Adversarial

**Claim mais fraco:** causalidade AI→employment decline. O paper controla firm-time effects, mas não pode descartar outros choques contemporâneos específicos a ocupações AI-exposed e idades 22–25 (ex: interesse rate shock afetando setores com muitos júniors tech).

**O que o paper NÃO diz:**
1. Não documenta declínio de salários — apenas de emprego
2. Não cobre mercados de trabalho fora dos EUA (ADP = EUA)
3. Não mede criação de novas ocupações por AI

**Simplificações:** exposure index (Eloundou 2024) é técnico, não medição de adoção observada. ADP overrepresenta empresas do Nordeste e manufatura/serviços vs QCEW.

**Prior work relacionado:** Eloundou et al. (2024), Acemoglu & Restrepo (2022), Frey & Osborne (2017), Acemoglu & Autor (2011).

## Interpretação

(⚠️ Zone 3 — domínio lateral. Interpretação intencionalmente vazia no ingest. Conexões com a KB emergem no /ask.)

## Conexões

## Fontes
- [Brynjolfsson, Chandar, Chen (2025)](../../raw/papers/brynjolfsson-chen-2025-canaries-coal-mine-ai-employment.pdf) — ADP payroll data; –16% emprego relativo 22–25 anos AI-exposed; automative vs augmentative distinction

## Quality Gate
- [x] Wikilinks tipados: nenhum — Zone 3, conexões emergem no /ask
- [x] Instance→class: –16% relativo = ADP data, controlling firm-time effects, 22–25 EUA; –6% absoluto = quintil mais exposto late 2022-set 2025
- [x] Meta-KB separado: nenhuma referência ao metaxon no Conteúdo
- [x] Resumo calibrado: source_quality:high — ADP primary data, Stanford working paper; interpretation_confidence:high — claims factuais diretos

> ⚠️ QUARENTENA: Gate 3∥challenge — 1 claim invalidado + 5 weakened. Correções necessárias antes de /promote:
> 1. [INVALIDADO] "O índice de exposição à AI não previa quedas de emprego jovem em períodos anteriores" → qualificar: "dentro da janela analítica (jan 2021–late 2022, pré-GenAI); o período COVID-19 (2020) não está coberto pelos dados"
> 2. [WEAKENED] "–16% emprego relativo" → adicionar: "associação observacional controlando firm-time effects; não causal (possíveis confounders: choques de taxa de juros correlacionados com setores tech + idade)"
> 3. [WEAKENED] "automative vs augmentative distinction" → qualificar: "classificação via Anthropic Economic Index (proporção de queries Claude por ocupação) — proxy de uso, não medição direta de intent de automação"
> 4. [WEAKENED] "O padrão começa em late 2022/early 2023" → manter mas adicionar: "temporalidade sugestiva, não causal; coincide também com alta de juros que afetou setores tech desproporcionalmente"
> 5. [WEAKENED] "após controlar firm-time effects" → adicionar: "absorve choques firm-month comuns; não elimina mudanças de composição dentro da firma (ex: shrinkage de equipes júnior por decisão estratégica)"
> 6. [WEAKENED] "SWE-Bench 4.4% → 71.7%" → adicionar: "(provavelmente SWE-bench Lite, versão reduzida; benchmark completo tem scores menores)"
> 7. [STALENESS OVERRIDE] "Período: jan 2021–set 2025" e "46% LLM adoption (jun/jul 2025)" → dados reais do paper (nov 2025); invalidações por model staleness, não por erro factual
