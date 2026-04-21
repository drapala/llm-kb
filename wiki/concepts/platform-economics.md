---
title: "Platform Economics (Parker, Van Alstyne & Choudary 2016)"
sources:
  - path: raw/articles/parker-van-alstyne-2016-pipelines-platforms.md
    type: article
    quality: secondary
    stance: confirming
created: 2026-04-04
updated: 2026-04-04
tags: [economics, platforms, network-effects, strategy, two-sided-markets, b2g, procurement]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-08
quarantine: false
---

## Resumo

Parker, Van Alstyne & Choudary (2016) contrastam "pipeline businesses" (cadeia linear de valor) com "platform businesses" (ecossistema de producers e consumers). Plataformas ganham via network effects (economias de escala do lado da demanda) em vez de supply-side scale. Três shifts estratégicos — de controle para orquestração, de otimização interna para interação externa, de valor do cliente para valor do ecossistema. Quando plataformas entram em mercados de pipelines, as plataformas quase sempre vencem.

## Conteúdo

### Pipeline vs Plataforma

**Pipeline:** cadeia linear de atividades que transforma inputs em outputs. Recursos são controlados internamente. Value chain model (Porter).

**Plataforma:** ecossistema com 4 tipos de players:
- **Owners:** controlam IP e governança
- **Providers:** interface com usuários
- **Producers:** criam ofertas
- **Consumers:** usam ofertas

Empresas podem ser ambos: handset Apple = pipeline; App Store = plataforma. Quando entram no mesmo mercado, plataformas quase sempre vencem pipelines.

**Evidência:** Nokia et al. detinham 90% dos lucros globais de telefones em 2007. Em 2015, iPhone sozinho = 92% dos lucros globais. Todos os outros incumbentes não lucravam.

### Os 3 Shifts Estratégicos

**1. Resource control → Resource orchestration**
- Pipeline: vantagem via recursos escassos e valiosos (minas, IP, real estate)
- Platform: o ativo difícil de copiar é a *comunidade* e os recursos que seus membros possuem (quartos, carros, ideias)

**2. Internal optimization → External interaction**
- Pipeline: otimiza cadeia de produção
- Platform: facilita interações entre producers e consumers externos; elimina custos variáveis de produção; governa ecossistema
- Shift de "ditating processes" para "persuading participants"

**3. Customer value → Ecosystem value**
- Pipeline: maximiza lifetime value de clientes individuais ao final da cadeia
- Platform: maximiza valor total do ecossistema em processo circular e iterativo
- Às vezes subsidia um tipo de consumer para atrair outro (two-sided market logic)

### Network Effects — Mecanismo Central

**Supply-side economies of scale** (motor da economia industrial):
- Fixed costs altos + marginal costs baixos → firma com maior volume tem menor custo médio → reduce prices → more volume → virtuous loop → monopólios
- Produziu Carnegie Steel, Standard Oil, GE

**Demand-side economies of scale (network effects)** (motor da economia internet):
- Maior "volume" (mais participants) → maior valor médio por transação, porque larger network = better matches + richer data
- Greater scale → more value → more participants → more value → monopolies
- Produziu: Alibaba (75% do e-commerce chinês), Google (82% mobile OS, 94% mobile search), Facebook

Porter's Five Forces não incorpora network effects — trata forças externas como "depletive." Em plataformas, forças externas podem ser "accretive" (adicionam valor).

### Ameaças competitivas

**Dentro do ecossistema:**
- Participants defectam (Zynga tentou migrar players do Facebook para plataforma própria)
- Providers competem diretamente (Netflix extrai valor de telecoms enquanto usa sua infraestrutura)
- Consumers e producers trocam de papel (Uber riders viram drivers; Airbnb travelers viram hosts)

**Do ecossistema externo (3 padrões):**
1. Plataforma estabelecida com superior network effects entra na sua indústria (Google → termostatos → Siemens)
2. Novo player com overlapping customers (Airbnb vs hotéis)
3. Coletor de dados do mesmo tipo entra no seu mercado (saúde: hospitais vs Fitbit vs Walgreens)

### Acesso e Governança

**Trade-offs de abertura:**
- Open architecture: producers podem criar → mais valor, mais inovação
- Open governance: outros moldam regras de recompensa → mais engajamento
- Sem reward sharing: ability to engage mas sem incentivo
- Sem open architecture: incentivo mas sem ability

**Permissionless innovation:** Rovio criou Angry Birds no iOS sem aprovação, com garantia de que Apple não roubaria seu IP → hit que gerou valor enorme para toda a plataforma.

**Problema oposto:** Chatroulette — sem regras de acesso → "naked hairy man problem" → usuários vestidos abandonaram → colapso. Solução: filtros de usuário.

Uber e Airbnb: rate participants, segment insurance. Twitter/Facebook: anti-stalking tools. App Store/Google Play: filtram apps baixa qualidade.

### Inversão da Firma (Platform Inversion)

Plataformas invertem funções organizacionais para fora:
- **Marketing:** consumidores propagam mensagens (Warby Parker: fotos de óculos nas redes)
- **IT:** suporta redes externas (Threadless: clientes colaboram no design)
- **HR:** talento externo (SAP: rede de desenvolvedores aberta a parceiros e clientes de parceiros)
- **Finance:** distributed ledgers (IBM, Intel, JPMorgan: blockchain para ledgers compartilhados)
- **Operations:** "not-even-mine" inventory (Airbnb, Uber, YouTube)

### Métricas de Plataforma

| Métrica | O que monitora |
|---------|---------------|
| Interaction failure | Falhas de match (ex: "no cars available" no Lyft) |
| Engagement | Daily/monthly user ratio (Facebook); repeat visits |
| Match quality | Click/read patterns (Google search) |
| Negative network effects | Congestion, misbehavior, spam |

Feedback loops negativos: falha de match → passengers quit → higher driver downtime → drivers quit → even lower availability.

**Valuation:** Em 2016, private equity valuou Uber (fundado 2009) acima da GM (fundada 1908) — investidores olham além de financeiras tradicionais.

### Liderança em Plataformas

Controle interno ≠ orquestração de ecossistema. Rupert Murdoch comprou Myspace e gerenciou top-down como jornal — focou em controlar operação interna em vez de nutrir ecossistema → comunidade evaporou.

## Interpretação

⚠️ Interpretação do compilador — não está explicitamente no artigo nesta forma.

**B2G como pipeline que precisa de plataforma:** O mercado de compras públicas brasileiro é um pipeline clássico — cada compra é uma transação linear entre governo e fornecedor. A assimetria de informação (Akerlof) persiste porque o governo não tem os mecanismos de network effects e feedback loops que plataformas privadas têm. Um sistema de risk scoring é análogo a criar uma "reputation layer" para esse mercado — tentando introduzir a função de match quality e negative network effects em um contexto pipeline.

**Network effects em licitação:** Fornecedores com histórico em PNCP são análogos a producers em plataforma — sua reputação (qualidade de entregas anteriores) deveria ser visível para compradores futuros. Hoje esse dado existe mas não está integrado.

## Verificação adversarial

**Limitações do artigo:**
- Artigo HBR (não peer-reviewed) — normativo/prescritivo, não empírico
- Exemplos selecionados ex-post para confirmar tese (viés de confirmação)
- Não quantifica "quase sempre vencem" — afirmação qualitativa sem benchmarking sistemático

**O que o artigo NÃO diz:**
- Não deriva quando especificamente pipeline deve virar plataforma
- Não modela formalmente as condições de network effects
- Não discute plataformas que falharam (seleção de survivors)

## Conexões

- [[market-for-lemons]] ON "assimetria de informação é o problema que plataformas resolvem via ratings e reputação"
- [[network-information-theory]] ON "network effects como demand-side economies of scale"
- [[information-asymmetry-b2g]] ON "B2G como pipeline sem feedback loops de qualidade"

## Fontes

- [Parker, Van Alstyne & Choudary (2016)](../../raw/articles/parker-van-alstyne-2016-pipelines-platforms.md) — HBR April 2016. Conceitos de pipeline/plataforma, 3 shifts, network effects, acesso/governança, métricas, casos (iPhone, Airbnb, Chatroulette).
