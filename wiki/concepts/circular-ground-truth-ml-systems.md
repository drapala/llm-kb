---
title: "Circularidade de Ground Truth em Sistemas ML — Anti-padrão de Auto-Referência"
sources:
  - path: raw/papers/schmitz-2025-gmm-semisupervised-licitacoes.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-12
updated: 2026-04-12
tags: [ml-systems, ground-truth, evaluation, bias, zelox, model-validation, anti-pattern]
source_quality: low
interpretation_confidence: high
resolved_patches: []
provenance: emergence
emergence_trigger:
  pair: [schmitz-2025-gmm-semisupervised-licitacoes, z-score-aditivo]
  ask_session: outputs/logs/sessions/2026-04-12/ask-gmm-zscore.md
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-12
status: promoted
promoted_date: 2026-04-12
---

## Resumo

Labels gerados pelo sistema A não podem servir como ground truth para treinar o sistema B que substitui A. B herda os vieses de A sem oportunidade de falsificação — o resultado é uma versão mais cara de A, não um modelo independente. Princípio geral de design de sistemas ML; instância concreta identificada no Zelox durante análise de substituição de z_score_aditivo por GMM semi-supervisionado.

## Conteúdo

### O Anti-padrão

```
Sistema A (heurística/modelo atual)
  → flags conjunto F de casos como "fraude"
  → F usado como ground truth para treinar Sistema B (substituto)
  → B aprende padrão de F
  → B detecta casos parecidos com F
  → B ≈ A mais caro
```

A circularidade não é óbvia porque B pode ter arquitetura diferente de A. O problema não é a arquitetura — é a **fonte das labels**. Labels derivadas de A codificam os critérios de A. B aprende o quê A já sabia, não o quê A não sabia.

### Instância Zelox (2026-04-12)

O `z_score_aditivo` (sistema A) produz flags de contratos com delta_pct alto. Os 3 L2 predictions no ledger do Zelox são saídas desse sistema. Usar esses predictions como âncoras para treinar um GMM semi-supervisionado (sistema B) produziria um GMM que detecta contratos com z_score alto — exatamente o que z_score já faz.

**Teste de circularidade:** se B fosse treinado com labels de A, você esperaria que B concordasse com A em ~100% dos casos positivos. Se concordância > 90%, a substituição é circular.

### Condição para ground truth válido

Ground truth é válido para substituição de sistema quando é **independente do sistema sendo substituído**:

| Fonte de labels | Independente? | Adequado para substituição? |
|---|---|---|
| Flags do sistema atual | Não | Circular — invalida a substituição |
| Acórdãos TCU com número de contrato | Sim | Válido — decisão externa ao modelo |
| Notícias de escândalo (sem contrato ID) | Parcialmente | Nível errado — entidade, não contrato |
| Auditoria CGU sistematizada | Sim | Válido — mas acesso restrito |
| Operações policiais (ex: Licitante Fantasma) | Sim | Válido, mas viés de seleção (só casos confirmados) |

### Relação com outros anti-padrões

**Goodhart's Law:** quando a métrica torna-se o alvo, deixa de ser boa métrica. Aqui: quando os flags do modelo tornam-se os labels, o novo modelo aprende a replicar os flags — não a detectar o fenômeno real.

**Autoresearch anti-cascade:** na literatura de confiabilidade de autoavaliação em LLMs (autoresearch-reliability-triad), o anti-cascade structure exige que o sinal de avaliação seja logicamente independente do modelo avaliado. O mesmo princípio se aplica a sistemas ML que usam suas próprias saídas como supervisão.

**Causal level collapse:** labels geradas por A são L1 (correlacionais — "A flagou X"). Ground truth válido requer L2 (interventional — "removendo o fenômeno, o label muda"). Usar flags de A como labels trata L1 como L2.

### Quando o anti-padrão é aceitável

Em dois casos limitados:

1. **Bootstrapping iterativo com validação externa:** A gera candidates → humano valida subset → subset validado é o ground truth. A nunca é a fonte final.

2. **Ensemble diversity:** A e B são diferentes por design (ex: A = regra + B = unsupervised), e o objetivo é detectar o que um dos dois perde. Nesse caso, concordância de A e B é evidência de robustez, não de circularidade.

### Bloqueador Zelox

O anti-padrão circular é o bloqueador fundamental para qualquer modelo supervisionado/semi-supervisionado no Zelox. Não é volume de cases (problema solucionável). É a fonte das labels.

O desbloqueador é ground truth externo ao Zelox: acórdãos TCU com referência a contratos específicos. Ver `tcu-acordaos-ground-truth-pipeline.md`.

## Conexões

- [[anti-patterns-epistemic-ml]] — taxonomia: este artigo é o Anti-padrão #1 de uma família de 5
- [[z-score-aditivo]] — instância: L2 predictions do ledger são circulares como ground truth para GMM substituto
- [[autoresearch-reliability-triad]] — princípio análogo: sinal de avaliação deve ser logicamente independente do modelo avaliado
- [[tcu-acordaos-ground-truth-pipeline]] — desbloqueador: ground truth externo via acórdãos TCU

## Fontes

- `/ask` session 2026-04-12 — identificação do anti-padrão durante análise GMM × z_score_aditivo
- [Schmitz UFSC 2025](../../raw/papers/schmitz-2025-gmm-semisupervised-licitacoes.md) — metodologia GMM semi-supervisionado que motivou a análise
