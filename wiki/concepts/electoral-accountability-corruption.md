---
title: "Electoral Accountability and Corruption (Ferraz & Finan 2011)"
sources:
  - path: raw/papers/ferraz-finan-2011-electoral-accountability-corruption.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [corruption, procurement, brazil, b2g, accountability, term-limits, electoral, empirical]
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

Ferraz & Finan (2011) usam variação em limites de mandato para identificar o efeito de incentivos eleitorais sobre corrupção em municípios brasileiros. Prefeitos em último mandato (sem incentivo de reeleição) têm ≈20% mais violações de corrupção do que prefeitos de primeiro mandato. O efeito é amplificado por rádio local. Accountability eleitoral = mecanismo de disciplina pelo lado da oferta (políticos se comportam melhor quando ameaçados). AER 2011.

⚠️ Stub — full text não lido. Conteúdo baseado em descrições secundárias.

## Conteúdo

### Contraste com Ferraz & Finan (2008)

Os dois papers identificam os dois lados do mecanismo de accountability:

| Paper | Pergunta | Variação | Resultado |
|-------|----------|----------|-----------|
| F&F (2008) | Revelar corrupção pune incumbente? | Timing da auditoria | Sim: -7 a -29pp reeleição |
| F&F (2011) | Ameaça de revelação reduz corrupção? | Limites de mandato | Sim: +20% corrupção no último mandato |

(2008) opera pelo lado da demanda: eleitores punem quando informados. (2011) opera pelo lado da oferta: políticos se comportam melhor quando têm incentivo de carreira.

### Identificação

**Variação exógena:** Constituição brasileira limita prefeitos a dois mandatos consecutivos. Prefeitos em segundo mandato não podem se reeleger → nenhum incentivo eleitoral de curto prazo.

**Comparação:** Municípios com prefeitos de primeiro mandato (elegível à reeleição) vs. prefeitos de último mandato (não elegível). A comparação é válida assumindo que os dois grupos são similares exceto pelo incentivo eleitoral.

**Medida de corrupção:** Mesma codificação de irregularidades do F&F (2008) — dados CGU, procurement fraud + desvio de recursos + superfaturamento.

### Resultados Principais

**Efeito do último mandato:** Municípios com prefeitos em último mandato têm aproximadamente 0,35 violações a mais (≈20% do média da amostra) do que municípios com prefeitos de primeiro mandato.

**Amplificação por rádio:** O efeito de disciplina eleitoral (primeiro mandato → menos corrupção) é mais forte em municípios com rádio AM local. Sem mídia, a ameaça eleitoral é fraca porque a informação sobre corrupção não chega aos eleitores.

**Mecanismo inferido:** A ameaça de punição eleitoral induz disciplina. Quando essa ameaça é removida (último mandato), corrupção aumenta — evidência de que os políticos sabem que estão sendo observados e respondem ao incentivo.

### Implicações Temporais

**Ciclo de corrupção dentro do mandato:** A teoria prediz mais corrupção no final do mandato (quando reeleição está garantida ou impossível) e no início (antes de construir reputação). A evidência empírica é consistente com corrupção crescendo no último mandato.

**Previsão para último ano de mandato:** Prefeitos em último ano de segundo mandato têm:
- Nenhum incentivo eleitoral
- Nenhuma perspectiva de carreira pós-mandato dependente de reputação municipal
- Incentivo máximo para extrair recursos antes de sair

## Interpretação

⚠️ Interpretação do compilador.

**Implicação para risco sistêmico em procurement:** O paper prediz que a corrupção em procurement é *estruturalmente maior* em municípios com prefeitos de último mandato. Este é um feature de risco municipal (não de fornecedor) que um sistema como Zelox deveria incorporar.

**Indicador contextual para Risk Score:**
- Prefeito em segundo mandato + próximo do fim = elevação automática de risco de base
- Combinado com fornecedor com histórico de irregularidades = risco composto muito mais alto

**Sinais a monitorar:** Volume de licitações, contratos e aditivos nos últimos 12 meses do mandato de prefeitos em segundo mandato — deve ser maior que nos primeiros 12 meses do mesmo mandato.

## Quality Gate
- [x] Wikilinks tipados: extends/relaciona
- [x] Instance→class: "0.35 violações a mais" — específico ao sample F&F (AER 2011)
- [x] Meta-KB separado: Zelox em Interpretação
- [x] Resumo calibrado: ⚠️ stub mencionado

## Conexões

- extends: [[corruption-audits-brazil]] ON "mesmo programa CGU, mesma medida de corrupção — complementa pelo lado da oferta (incentivos políticos)"
- relaciona: [[market-for-lemons]] ON "prefeitos no último mandato = compradores com horizonte truncado → degradação de qualidade"
- relaciona: [[procurement-renegotiation]] ON "hold-up piora quando comprador não tem incentivo de longo prazo (último mandato)"

## Fontes

- [Ferraz & Finan (2011)](../../raw/papers/ferraz-finan-2011-electoral-accountability-corruption.md) — AER 101(4), 1274-1311. Limites de mandato, +20% corrupção no último mandato, amplificação por rádio. ⚠️ Stub — texto completo não lido.
