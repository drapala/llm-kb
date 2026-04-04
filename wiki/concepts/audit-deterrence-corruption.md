---
title: "Audit Deterrence and Corruption (Olken 2007)"
sources:
  - path: raw/papers/olken-2007-monitoring-corruption.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-04
updated: 2026-04-04
tags: [corruption, audit, deterrence, randomized-experiment, indonesia, b2g, monitoring]
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

Olken (2007) usa experimento de campo aleatorizado em 608 aldeias indonésias para identificar causalmente o efeito de auditorias sobre corrupção em construção de estradas. Resultado: aumento da probabilidade de auditoria (4% → 100%) reduz "gastos faltantes" (proxy de corrupção) em ≈8pp sobre média de 24%. Monitoramento comunitário (assembleias de aldeia) não tem efeito significativo. JPE 2007.

⚠️ Stub — full text não lido. Conteúdo baseado em descrições secundárias.

## Conteúdo

### Design do Experimento

**Intervenção:** 608 aldeias em Indonésia construindo estradas foram aleatoriamente atribuídas a:
1. **Auditoria garantida:** probabilidade de auditoria governamental aumentada de 4% → 100%
2. **Monitoramento comunitário:** assembleias de aldeia + engenheiros externos convidados
3. **Controle:** sem mudança (probabilidade de 4% de auditoria)

**Medida de corrupção:** "Missing expenditures" = diferença entre gastos reportados e estimativa independente de engenheiro do custo real do projeto. Média na linha de base: ≈24% do custo total do projeto.

### Resultados Principais

**Auditorias governamentais:** Reduziram gastos faltantes em ≈8 pp (do 24% de linha de base). Efeito grande, estatisticamente significativo, e robusto.

**Monitoramento comunitário:** Nenhum efeito significativo sobre corrupção. Participação da comunidade aumentou, mas não traduziu em redução de irregularidades.

**Efeito não-linear:** O efeito ocorre principalmente pela mudança de probabilidade "baixa" para "certa" de auditoria — não é a intensidade da auditoria que importa, é a certeza de que haverá auditoria.

### Por que Auditorias Funcionam e Monitoramento Comunitário Não

**Especificidade técnica:** Auditores governamentais com expertise técnica conseguem verificar espessura de pavimento, qualidade de materiais, e quantidade de insumos — especificações que membros da comunidade não conseguem aferir sem treinamento.

**O que é detectável em auditorias:** Formas mais facilmente mensuráveis de corrupção (quantidade de materiais, extensão de obra) respondem mais fortemente. Formas mais difusas (preços de mão-de-obra) respondem menos.

**Implicação:** Complexidade técnica do procurement → monitoramento comunitário insuficiente → auditoria técnica especializada é necessária e eficaz.

### Mecanismo: Deterrência ex-ante

A auditoria não apenas *detecta* corrupção depois do fato — ela *previne* antes. Contratistas que sabem que serão auditados reduzem a fraude *antecipadamente*. Este é o canal de deterrência (vs. o canal de detecção de Ferraz & Finan 2008).

| Mecanismo | Paper | Canal |
|-----------|-------|-------|
| Detecção | Ferraz & Finan (2008) | Punição eleitoral após descoberta |
| Deterrência | Olken (2007) | Mudança de comportamento *antes* da fraude |

Ambos os canais são empiricamente documentados e complementares.

## Interpretação

⚠️ Interpretação do compilador.

**Validação fundamental do Zelox:** Se um sistema de risk scoring aumenta a probabilidade percebida de auditoria pelos fornecedores — mesmo sem auditorias adicionais efetivas — o Olken mecanismo prediz redução de fraude. Zelox opera como "auditoria virtual" que sinaliza vigilância.

**Magnitude esperada:** Olken encontra ≈8pp de redução em contexto onde auditorias passam de 4% para 100%. O efeito de um risk score é provavelmente menor (não há auditoria garantida), mas a direção é a mesma.

**Sinais detectáveis:** Os sinais mais robustos para um risk score são análogos ao que é detectável em auditorias técnicas: quantidades de materiais vs. escopo (superfaturamento), número de fornecedores habilitados vs. selecionados (ausência de competição), presença vs. ausência de documentação (phantom firms).

## Quality Gate
- [x] Wikilinks tipados: validates/relaciona
- [x] Instance→class: "8pp" é específico ao contexto Indonesia Olken 2007
- [x] Meta-KB separado: Zelox em Interpretação
- [x] Resumo calibrado: ⚠️ stub mencionado

## Conexões

- validates: [[corruption-audits-brazil]] ON "evidência causal de deterrência; complementa detecção de F&F pelo lado preventivo"
- relaciona: [[electoral-accountability-corruption]] ON "ambos identificam mecanismos complementares: deterrência (Olken) + punição eleitoral (F&F 2011)"
- relaciona: [[market-for-lemons]] ON "auditoria técnica resolve assimetria de informação sobre qualidade que o mercado sozinho não resolve"

## Fontes

- [Olken (2007)](../../raw/papers/olken-2007-monitoring-corruption.md) — JPE 115(2), 200-249. RCT em 608 aldeias indonésias, -8pp gastos faltantes via auditoria garantida, monitoramento comunitário ineficaz. ⚠️ Stub — texto completo não lido.
