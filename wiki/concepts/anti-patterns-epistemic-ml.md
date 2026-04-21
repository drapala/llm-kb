---
title: "Anti-padrões Epistêmicos em Sistemas ML de Detecção de Fraude"
sources:
  - path: raw/papers/schmitz-2025-gmm-semisupervised-licitacoes.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/morais-2024-fraud-prediction-random-forest.md
    type: paper
    quality: primary
    stance: confirming
  - path: wiki/concepts/audit-deterrence-corruption.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/corruption-dynamics.md
    type: synthesis
    quality: primary
    stance: confirming
created: 2026-04-12
updated: 2026-04-12
tags: [ml-systems, anti-patterns, fraud-detection, zelox, epistemics, ground-truth, goodhart, threshold, audit-trails, proxy]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - wiki/concepts/circular-ground-truth-ml-systems.md
  - wiki/concepts/audit-deterrence-corruption.md
  - wiki/concepts/corruption-dynamics.md
  - wiki/concepts/z-score-aditivo.md
  - raw/papers/morais-2024-fraud-prediction-random-forest.md
status: promoted
promoted_date: 2026-04-12
---

## Resumo

Cinco anti-padrões recorrentes em sistemas ML de detecção de fraude em procurement. Cada um tem um mecanismo específico de degradação, backing no corpus, e mitigação. O mais urgente para o Zelox em fase de produto público é o **Threshold Gaming** (#5). Artigo de referência — cada anti-padrão tem instância Zelox concreta.

## Conteúdo

---

### Anti-padrão 1 — Circularidade de Ground Truth

**Mecanismo:** Labels geradas pelo sistema A são usadas como ground truth para treinar sistema B que substitui A. B aprende o que A já sabia — não o que A perdia. Ver artigo detalhado: [[circular-ground-truth-ml-systems]].

**Instância Zelox:** usar os 3 L2 predictions do ledger (gerados por `z_score_aditivo`) como âncoras para GMM semi-supervisionado.

**Teste de diagnóstico:** se B, treinado com labels de A, concordaria com A em >90% dos casos positivos, a substituição é circular.

**Mitigação:** ground truth exclusivamente externo ao sistema — acórdãos TCU com número de contrato, auditoria CGU, operações judiciais. Ver [[tcu-acordaos-ground-truth-pipeline]].

**Urgência Zelox:** bloqueador para qualquer modelo supervisionado/semi-supervisionado.

---

### Anti-padrão 2 — Goodhart's Law aplicada a Sinais de Fraude

**Mecanismo:** quando um sinal de fraude torna-se público e documentado, agentes fraudulentos adaptam comportamento para passar no sinal. A medida deixa de rastrear o fenômeno — rastreia quem não sabe que está sendo medido.

> *"When a measure becomes a target, it ceases to be a good measure."* — Goodhart (1975)

**Backing no corpus:** Niehaus & Sukhtankar 2013 ([[corruption-dynamics]]) — enforcement mais forte → mais corrupção no curto prazo porque agentes racionais adaptam estratégia. Corrupção é elástica à metodologia de detecção, não ao nível de enforcement bruto.

**Instâncias Zelox:**
- `rede_empresas_score`: fornecedores conectados que sabem do sinal usam CNPJs distintos com sócios intermediários (1 grau de separação)
- `compliance_rule` baseada em Art. 125 Lei 14.133: limite de 25% é público — agentes informados param em 24.9%
- Qualquer sinal publicado em documentação técnica ou relatório de auditoria

**Mitigação:**
- Ensemble de sinais: custo de passar em todos simultaneamente é mais alto que passar em um
- Sinais comportamentais de processo (como a licitação foi conduzida) vs. sinais de resultado (valor final)
- Rotação de thresholds ou thresholds ocultos na camada de decision (não expor threshold numérico no relatório público)
- Sinal de Niehaus: medir *padrão de adaptação* como sinal — cluster de contratos em 24-24.9% é evidência do agente tentando passar no sinal, o que é mais forte do que um contrato em 26%

---

### Anti-padrão 3 — Proxy Drift

**Mecanismo:** o proxy usado para medir fraude desacopla gradualmente do fenômeno real à medida que o comportamento fraudulento evolui, as regras mudam, ou o proxy é influenciado por fatores não-fraude.

**Backing no corpus:** Morais/UFU 2024 ([[morais-2024-fraud-prediction-random-forest]]) usa multas como proxy de fraude. Variação sazonal extrema (F1: 0.96 em janeiro → 0.54 em novembro) indica que o proxy é instável — não fraude, mas o processo administrativo de multas (mais lento em fim de ano fiscal).

**Instâncias Zelox:**
- `aditivo_teto` como proxy de hold-up: válido para Obras/Engenharia; inválido para Serviços (Q3=100% por renovações anuais acumuladas — o campo `valor_global` não mede aditivo de Art. 125)
- `z_score_aditivo` calculado sobre `valor_acumulado`: mediu execução orçamentária (empenhos), não aditivos contratuais — drift de campo, não de conceito
- Multas como proxy de fraude (Morais): multas refletem capacidade de enforcement, não prevalência de fraude

**Mitigação:**
- Monitorar distribuição do proxy ao longo do tempo — drift de Q3 ou σ sem mudança no fenômeno real indica proxy instável
- Usar proxy no nível do dado mais próximo ao fenômeno (termos aditivos via `/termos` > `valor_global` - `valor_inicial`)
- Múltiplos proxies ortogonais — se todos driftam na mesma direção, suspeitar de mudança real; se só um drifa, trocar o proxy

---

### Anti-padrão 4 — Seleção de Confirmação em Audit Trails

**Mecanismo:** audit trails registram o que foi investigado e verificado, não o que aconteceu. Modelos treinados em audit trails aprendem "o que é detectável dada a capacidade de enforcement atual" — não "o que é fraudulento". A distribuição de fraudes detectadas é enviesada para os tipos de fraude mais fáceis de detectar.

**Backing no corpus:** Olken 2007 ([[audit-deterrence-corruption]]) — em aldeias com auditoria garantida, o nível de corrupção que *sobrevive* é o mais difícil de detectar, não o mais raro. O audit trail de aldeias auditadas superestima a fraude "detectável" e subestima a fraude "sofisticada".

LAIC/UFMG usa audit trails como sinais de fraude. A abordagem é válida para detecção, mas os modelos aprendem os padrões das fraudes que já foram suficientemente óbvias para gerar trilha — não fraudes que evitam deixar trilha.

**Instância Zelox:**
- As 19 trilhas de auditagem (Oliveira BraSNAM 2023) refletem o que a metodologia LAIC consegue registrar via dados públicos PNCP/CNPJ
- Fraudes que envolvem um único fornecedor habilitado sem rede societária visível, com aditivo abaixo de 25%, CNAE compatível e sem historico de multas são **invisíveis ao Zelox V1.1**
- Isso não invalida os sinais — mas calibra as expectativas: o Zelox detecta fraudes que deixam trilha nos dados públicos

**Mitigação:**
- Não usar precision/recall em dados históricos de audit como proxy de performance real — esses dados têm selection bias para fraudes detectáveis
- Manter articulação explícita do que o sistema *não detecta* (ver seção de escopo do Zelox)
- Complementar audit trails com sinais de mercado (anomalias de preço) que não dependem de investigação prévia

---

### Anti-padrão 5 — Threshold Gaming ⚡ URGENTE para Zelox produto

**Mecanismo:** agentes racionais com conhecimento dos thresholds de detecção adaptam comportamento para ficar marginalmente abaixo do limite. O comportamento de hold-up (extrair valor máximo sem disparar alerta) torna-se o padrão de agentes informados. O threshold conhecido deixa de ser sinal e passa a ser **coordenador de comportamento fraudulento**.

**Backing no corpus:**
- Threshold de aditivo de 25% (Art. 125, Lei 14.133) é público por definição legal — qualquer fornecedor informado sabe
- Fracionamento de compras abaixo dos limites de dispensa de licitação é documentado em acórdãos TCU como padrão sistemático
- Goodhart: o threshold publicado coordena comportamento ao redor de 24.9% tanto quanto coordena comportamento legítimo

**Instâncias Zelox:**
- `aditivo_teto`: contratos que param em 24-24.9% são **mais suspeitos** que contratos em 26% — o excesso de 26% pode ser erro ou emergência técnica; a acumulação em 24.9% é comportamento deliberado
- Limites de dispensa de licitação (R$50k para obras, R$17.6k para outros): fracionamento sistemático em contratos de R$49.9k do mesmo fornecedor ao mesmo órgão
- Score threshold público: se o Zelox publicar "contratos com score > 0.7 são investigados", fornecedores sofisticados calibrarão para score = 0.68

**Mitigação — sinal de clustering sub-threshold:**

```python
# Detectar hold-up comportamental via clustering próximo ao teto
def threshold_gaming_score(contratos_fornecedor, teto=0.25, janela=0.01):
    """
    Retorna fração de contratos que terminam em [teto-janela, teto].
    Score > 0.3 = evidência de threshold gaming sistemático.
    """
    proximos_teto = [
        c for c in contratos_fornecedor
        if (teto - janela) <= c.delta_pct < teto
    ]
    return len(proximos_teto) / len(contratos_fornecedor) if contratos_fornecedor else 0
```

O sinal detecta o *padrão comportamental* (evitar o threshold), não a violação do threshold. Uma empresa que sistematicamente termina contratos em 24-24.9% ao longo de múltiplos órgãos é mais suspeita que uma empresa que violou o teto uma vez.

**Variantes:**
- Fracionamento temporal: múltiplos contratos ao mesmo órgão em sequência, cada um abaixo do limite de dispensa
- Score gaming: se o threshold do Zelox for público, monitorar fornecedores que progressivamente reduzem seu delta_pct ao longo do tempo (sinal de aprendizado adaptativo)

**Princípio de design:** thresholds de detecção nunca devem ser documentados em relatórios públicos com precisão numérica. "Acima do padrão da categoria" é mais robusto que "acima de 25%".

---

## Mapa de Urgência para o Zelox

| Anti-padrão | Urgência | Quando se torna crítico | Mitigação ativa no Zelox V1.1 |
|---|---|---|---|
| 1. Circular ground truth | Alta | Ao implementar qualquer modelo treinado | TCU pipeline pendente |
| 2. Goodhart / sinal público | **Crítica** | Ao publicar documentação técnica | ❌ não implementada |
| 3. Proxy drift | Média | Monitoramento contínuo | Parcial (campo `/termos` corrigido) |
| 4. Audit trail selection bias | Baixa | Ao reportar métricas de performance | ❌ não documentada |
| 5. Threshold gaming | **Crítica** | Ao virar produto público | ❌ não implementada — próximo item de código |

Anti-padrões 2 e 5 são instâncias do mesmo mecanismo (Goodhart) em níveis diferentes — um no sinal, outro no threshold.

**Próxima ação de código (AP-5):** implementar `cluster_subteto_score` em `pncp_supplier_contracts.py` como feature adicional em `ContractRecord`. Requer histórico agregado por fornecedor + categoria — não computável por contrato individual, mas computável ao nível do laudo (todos os contratos de um CNPJ). Candidato para `enrich_zscores()` como segunda passagem após a normalização.

## Conexões

- [[circular-ground-truth-ml-systems]] — artigo detalhado do anti-padrão 1
- [[tcu-acordaos-ground-truth-pipeline]] — mitigação do anti-padrão 1
- [[corruption-dynamics]] — Niehaus & Sukhtankar: backing teórico para anti-padrões 2 e 5
- [[audit-deterrence-corruption]] — Olken: backing para anti-padrão 4
- [[z-score-aditivo]] — instâncias dos anti-padrões 3 e 5 (proxy drift do campo; threshold gaming 24.9%)
- [[procurement-fraud-ml-methods]] — Santos 2025: variação sazonal do proxy (anti-padrão 3)

## Fontes

- [[circular-ground-truth-ml-systems]] — anti-padrão 1, detalhado
- [[corruption-dynamics]] — Niehaus & Sukhtankar 2013: elasticidade da corrupção ao enforcement
- [[audit-deterrence-corruption]] — Olken 2007: RCT audit deterrence; selection bias
- [Morais/UFU 2024](../../raw/papers/morais-2024-fraud-prediction-random-forest.md) — proxy drift via variação sazonal de F1
- [[z-score-aditivo]] — calibração empírica: instâncias dos anti-padrões 3 e 5
