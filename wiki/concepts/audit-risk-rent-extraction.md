---
title: "Audit Risk and Rent Extraction in Brazilian Procurement (Zamboni & Litschig 2018)"
sources:
  - path: raw/papers/zamboni-litschig-2018-audit-risk-rent-extraction.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-04
updated: 2026-04-04
tags: [corruption, audit, procurement, brazil, b2g, rent-extraction, empirical, zelox-validation]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 3
retrievals_correct: 3
retrievals_gap: 0
last_read: 2026-04-08
quarantine: false
---

## Resumo

Zamboni & Litschig (2018) exploram a aleatorização do programa CGU brasileiro para estimar o efeito de risco de auditoria sobre irregularidades em procurement municipal. Resultado: maior probabilidade de auditoria → ≈15-20% menos irregularidades de procurement. Efeito concentrado em municípios com accountabilidade local *fraca* — auditoria top-down e accountability local são substitutos. JDE 2018. **Paper mais diretamente relevante para validação do Zelox**.

⚠️ Stub — full text não lido. Conteúdo baseado em descrições secundárias.

## Conteúdo

### Distinção de Ferraz & Finan (2008)

| Aspecto | Ferraz & Finan (2008) | Zamboni & Litschig (2018) |
|---------|----------------------|--------------------------|
| Outcome | Resultado eleitoral do prefeito | Irregularidades de procurement |
| Mecanismo | Punição de eleitores | Deterrência de burocratas/fornecedores |
| Unidade | Município × eleição | Contrato × município |
| Pergunta | Revelação pune? | Risco de auditoria deterrência? |

Zamboni & Litschig usam a mesma variação (aleatorização CGU) mas têm o outcome diretamente relevante para detecção de fraude em procurement — não o outcome político.

### Resultados Principais

**Efeito principal:** Doubling da probabilidade de auditoria → redução de ≈15-20% em irregularidades de procurement.

**Heterogeneidade por accountability local:**
- Municípios com accountability local *forte* (civil society, educação, imprensa): efeito da auditoria *menor*
- Municípios com accountability local *fraca*: efeito da auditoria *maior*

**Implicação:** Auditoria top-down e accountability local são substitutos, não complementos. Onde há pouco controle local, a auditoria externa tem maior impacto marginal.

### Tipos de Irregularidades Detectadas

Codificação similar a Ferraz & Finan (2008):
1. **Procurement sem competição:** contrato sem chamada pública adequada
2. **Superfaturamento:** preços substancialmente acima da referência de mercado
3. **Phantom firms:** pagamentos a entidades inexistentes
4. **Bid rigging:** evidência de colusão entre licitantes

Essas categorias mapeiam diretamente para sinais detectáveis em dados de PNCP.

### Implications para Mercados com Fraca Accountability

Municípios com baixa density institucional (pouca mídia local, baixa educação, baixa competição política) têm:
- Mais corrupção em procurement (sem controle local)
- Maior impacto marginal de auditoria/monitoramento externo
- **Maior valor marginal de um sistema como Zelox**

## Interpretação

⚠️ Interpretação do compilador.

**Validação mais direta do Zelox:** Este paper estima causalmente que risco de auditoria reduz irregularidades de procurement em ≈15-20% no contexto brasileiro. Zelox opera precisamente como um mecanismo de risco de auditoria percebido → a magnitude de Zamboni & Litschig é a expectativa de referência para o impacto do Zelox.

**Segmentação de valor:** O efeito é maior em municípios com fraca accountability local. Zelox deveria priorizar:
- Municípios menores (menos imprensa, menos competição política)
- Mercados concentrados (poucas opções de fornecedor)
- Regiões com menor densidade institucional

**Calibração do modelo:** Se o Zelox consegue dobrar a probabilidade *percebida* de detecção (em vez da probabilidade real de auditoria CGU), o efeito esperado em irregularidades é análogo ao de Zamboni & Litschig — na faixa de 10-20% de redução.

## Quality Gate
- [x] Wikilinks tipados: validates/relaciona
- [x] Instance→class: "15-20%" específico ao contexto CGU Brasil Zamboni & Litschig
- [x] Meta-KB separado: Zelox em Interpretação
- [x] Resumo calibrado: ⚠️ stub mencionado; "mais diretamente relevante" justificado

## Conexões

- validates: [[corruption-audits-brazil]] ON "efeito de risco de auditoria especificamente sobre irregularidades em procurement (vs. outcome eleitoral)"
- extends: [[audit-deterrence-corruption]] ON "replica mecanismo de Olken no contexto específico de procurement municipal brasileiro"
- relaciona: [[electoral-accountability-corruption]] ON "substitutabilidade: accountability local forte reduz valor marginal de auditoria externa"

## Fontes

- [Zamboni & Litschig (2018)](../../raw/papers/zamboni-litschig-2018-audit-risk-rent-extraction.md) — JDE 134, 133-149. CGU Brasil, -15-20% irregularidades, substitutabilidade auditoria/accountability local. ⚠️ Stub — texto completo não lido.
