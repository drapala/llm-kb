---
title: "Zelox como Sistema Neurossimbólico — Mapeamento e Roadmap"
sources:
  - path: raw/papers/delong-2024-neurosymbolic-kg-survey.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/ruckhaus-2025-shacl-owl-kcap.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/wu-2024-gnn-supply-chain-fraud.md
    type: paper
    quality: primary
    stance: neutral
  - path: raw/articles/ajithp-2024-neurosymbolic-compliance.md
    type: article
    quality: secondary
    stance: confirming
  - path: raw/papers/arabian-2025-neurosymbolic-robustness-uq-stub.md
    type: paper
    quality: secondary
    stance: confirming
created: 2026-04-11
updated: 2026-04-11
tags: [zelox, neurosymbolic, delong-taxonomy, compliance, fraud-detection, SHACL, GNN, uncertainty-quantification, architecture]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: emergence
status: quarantined
quarantine_date: 2026-04-11
quarantine_reason: "Gate 3 invalidou: (1) feature_compute rotulado como 'neural' sem componente treinado — scoring determinístico não é neural canônico (OpenAI); (2) 'ambos upgrades requerem ground truth' — logically-informed embeddings podem usar semantic loss sem labels (Gemini); (3) 'JOINs não capturam multi-hop' — CTEs recursivas capturam; vantagem GNN é generalização probabilística (OpenAI). Fixes aplicados: mapeamento qualificado como 'análogo, não canônico'; GNN vantagem = generalização, não impossibilidade JOINs; pré-requisitos de labels qualificados como 'amplificam' não 'são necessários'."
emergence_trigger:
  pair: [neurosymbolic-ai-knowledge-graphs, neurosymbolic-ai-compliance-applications]
  ask_session: outputs/logs/sessions/2026-04-11/ask-00-47.md
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-11
---

## Resumo
(⚠️ Emergence — não está em nenhuma fonte individual.) O Zelox já implementa um sistema neurossimbólico Categoria 2 per DeLong 2024, sem usar o vocabulário formal. Esta análise mapeia cada componente Zelox para a taxonomia NeSy, identifica dois riscos de comunicação (confidence scores como UQ, auditabilidade full-pipeline), e estabelece pré-requisitos para upgrades (OWL, GNN, calibração).

## Conteúdo

### Mapeamento Zelox → DeLong Categoria 2

DeLong 2024 define Categoria 2 como: embeddings aprendidos separadamente, constraints lógicos aplicados no momento de inferência. Zelox instancia este padrão:

| Componente DeLong | Componente Zelox | Nota |
|---|---|---|
| Representação numérica (análogo a embedding) | `feature_compute`: contagens, z-scores, risk scores | Computação determinística — não é embedding aprendido; aproxima Categoria 2, não instancia canonicamente |
| Constraint lógico | `compliance_rule` com operadores (gt, gte, lt, is_true) | Regras da Lei 14.133/2021 codificadas explicitamente |
| KG simbólico | `epistemic.assertion` com (subject, predicate, object, confidence, epistemic_layer) | Triplas + provenance weights |
| Graph traversal | `supply_chain_derive` via SQL JOIN | Travessia simbólica determinística |
| Veredicto | risk_score + flag de compliance | Output combinado neural + simbólico |

O padrão "neural flagga, simbólico decide" (Ajithp 2024, STUB) é estruturalmente análogo ao fluxo:
```
[PNCP data] → [feature_compute] → [risk scores] → [compliance_rule] → [veredicto auditável]
```
Qualificação: `feature_compute` é scoring determinístico baseado em regras (não um modelo treinado). O padrão se aplica por analogia estrutural, não como instância canônica de "componente neural".

### Dois Riscos de Comunicação Identificados

**Risco 1 — Confidence scores apresentados como UQ calibrado:**
Os scores (1.0 world, 0.85 derivado, 0.8 opinion) são **provenance weights** — razoáveis e defensáveis, mas não UQ calibrado no sentido estatístico. Calibração exige validar P(fraude | score = X) = X contra outcomes reais.
- ❌ "confidence = 0.85" (implica probabilidade estatisticamente calibrada)
- ✅ "source_reliability_weight = 0.85" (proveniência: dado derivado, não fonte oficial)

**Risco 2 — Auditabilidade full-pipeline sobrestimada:**
A camada simbólica (compliance_rule) é auditável. Mas o risk score gerado por feature_compute pode não ser interpretável isoladamente — "transação flaggada porque risk_score = 0.73" não explica *qual* padrão gerou esse score sem rastreabilidade adicional.

### Pré-requisitos por Upgrade

| Upgrade | O que adiciona | Pré-requisito |
|---|---|---|
| **SHACL** para validação de dados | Constraint enforcement correto (CWA) | Pode fazer agora |
| **OWL** para hierarquia de Lei | Inferência automática via subsunção (Lei 14.133 Art. X → herda de Y) | Ontologia do domínio modelada; Phase 2 |
| **Description Logic** | Subsunção de regras de compliance | Rule set suficientemente complexo para justificar overhead |
| **GNN** para supply chain | Padrões implícitos e generalizáveis que JOINs determinísticos não aprendem (JOINs cobrem multi-hop explícito, mas não generalização probabilística) | Ground truth ou sinal de supervision (labels ou semantic loss) |
| **Calibrated UQ** | Probabilidades estatisticamente válidas | Audit outcomes como sinal de calibração |

### Zelox como NeSy Categoria 2 — Implicações do Roadmap

DeLong descreve o upgrade natural de Categoria 2:
- → Categoria 1: treinar `feature_compute` com penalidade por violação de compliance_rules (logically-informed embeddings) — pode usar semantic loss (sem labels), mas outcomes reais amplificam a qualidade do treinamento
- → Categoria 3: aprender regras de compliance dos dados (rule learning) — beneficia de labeled data + volume suficiente de padrões; pode começar semi-supervisionado

O acumulador principal continua sendo as decisões de auditoria do CGU/TCU — não como pré-requisito universal, mas como o sinal de calibração mais valioso disponível.

## Interpretação

(⚠️ Emergence — síntese cross-paper sem fonte individual.)

O insight central desta análise: Zelox não está *construindo para* NeSy — Zelox *já é* NeSy Categoria 2. A consequência prática é que o roadmap de upgrades está mapeado na literatura acadêmica e tem pré-requisitos concretos, não abstratos.

A renomeação `confidence → source_reliability_weight` é a única ação de custo zero antes de ter clientes. Todas as outras formalizações dependem de dados que só existem após operação real.

## Predição falsificável

1. **Se Zelox implementar SHACL para data validation**, o número de assertions inválidas detectadas em batch aumentará vs. detecção via compliance_rule puro — porque SHACL opera com CWA e flaggará ausências que OWL ignoraria. Verificável ao migrar uma validation rule de compliance_rule para SHACL shape.

2. **Se Zelox coletar 100+ contratos com outcomes confirmados (CGU/TCU)** e calibrar os provenance weights empiricamente, os scores calibrados divergirão dos heurísticos (1.0/0.85/0.8) para pelo menos um tipo de fonte — ou os heurísticos são acidentalmente bem calibrados (falsificável: calibração empírica ≠ heurísticos atuais em algum quartil).

3. **Se Zelox treinar GNN em supply chain com os contratos existentes sem ground truth**, a AUC do modelo em detecção de fraude não superará um baseline de anomaly detection não-supervisionado (z-score nos features) — porque GNN sem labels aprende topologia, não fraude. Falsificável ao tentar treinar MultiFraud sem labels.

## Verificação adversarial

**Claims mais fracos:**
- "Zelox já é NeSy Categoria 2" — a taxonomia DeLong descreve sistemas com *componentes neurais aprendidos*; `feature_compute` do Zelox é computação determinística sem treino, o que se aproxima de Categoria 2 mas não é uma instância canônica.
- Mapeamento é feito pelo compilador do KB a partir de descrição textual dos componentes Zelox — não há auditoria direta do código.

**O que os papers não dizem:** (1) DeLong não discute sistemas com "embeddings determinísticos" (não-treinados); (2) nenhum paper sobre upgrade path de Categoria 2 → 1 com custo/benefício quantificado; (3) o timing ótimo para introduzir OWL em sistemas de compliance real não está documentado na literatura.

## Quality Gate
- [x] Wikilinks tipados: sem wikilinks externos necessários — artigo de aplicação
- [x] Instance→class: "Zelox já é NeSy Categoria 2" marcado como ⚠️ interpretação do compilador; mapeamento baseado em descrição textual
- [x] Meta-KB separado: análise de design Zelox na seção Conteúdo é aplicação direta das fontes, não meta-KB; sem referências ao processo do KB
- [x] Resumo calibrado: source_quality medium (STUB papers + primary DeLong); marcado como emergence

## Conexões
- neurosymbolic-ai-knowledge-graphs derivedFrom zelox-neurosymbolic-architecture-mapping (taxonomia DeLong aplicada ao Zelox)
- neurosymbolic-ai-compliance-applications partOf zelox-neurosymbolic-architecture-mapping (padrão compliance aplicado)
- shacl-owl-knowledge-graphs partOf zelox-neurosymbolic-architecture-mapping (SHACL como próximo passo concreto)
- gnn-fraud-detection-supply-chain partOf zelox-neurosymbolic-architecture-mapping (GNN como upgrade path supply_chain_derive)

## Fontes
- [DeLong et al. 2024](../../raw/papers/delong-2024-neurosymbolic-kg-survey.md) — taxonomia 3 categorias; Categoria 2 como mapeamento do Zelox
- [Ruckhaus et al. 2025](../../raw/papers/ruckhaus-2025-shacl-owl-kcap.md) — distinção SHACL/OWL; quando usar cada um (STUB)
- [Wu et al. 2024](../../raw/papers/wu-2024-gnn-supply-chain-fraud.md) — MultiFraud GNN; pré-requisito de ground truth (STUB)
- [Ajithp 2024](../../raw/articles/ajithp-2024-neurosymbolic-compliance.md) — "neural flags, simbólico decide" (STUB)
- [Arabian Journal 2025](../../raw/papers/arabian-2025-neurosymbolic-robustness-uq-stub.md) — UQ proxy via propagação de weights (STUB)
