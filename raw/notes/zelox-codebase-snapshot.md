---
title: "Zelox Codebase Snapshot"
sources:
  - path: raw/notes/zelox-codebase-snapshot.md
    type: note
    quality: primary
    stance: confirming
created: 2026-04-12
updated: 2026-04-12
tags: [zelox, codebase, implementation-state, feature-engineering]
source_quality: high
interpretation_confidence: high
provenance: source
status: promoted
---

## Propósito

Snapshot do estado de implementação do Zelox gerado por `scripts/gen-context.py`.
Use este artigo em /ask sessions sobre feature engineering para distinguir
o que está implementado do que está no backlog.

> Gerado em: 2026-04-12
> Para atualizar: `cd ~/projects/zelox && python scripts/gen-context.py`

---

## Features Implementadas (V1.1)

### Feature Keys Ativos

```python
SANCTION_FEATURE_KEYS = ('sanction_ceis_count', 'sanction_cnep_count', 'sanction_cepim_count')
FEATURE_KEYS = (*SANCTION_FEATURE_KEYS, 'has_public_contract', 'shareholder_count')
```

### Lógica de Risk Score (current)

Arquivo: `src/zelox/packets/supplier_risk_check_v1.py`

```python
    recommended_attention = "low"
    if factual_flags["is_listed_in_sanctions_registry"]:
        recommended_attention = "high"
    elif factual_flags["has_public_contract_observation"]:
        recommended_attention = "medium"
```

**Interpretação:** Risk score V1.1 é heurístico — 3 tiers baseados em presença/ausência
de sanções e contratos públicos. Sem z-score, sem IQR, sem rede. Esses sinais estão
no backlog, não no código.

---

## Features Pendentes (Backlog)

| Feature | Status | Bloqueio |
|---------|--------|----------|
| `z_score_aditivo_por_tipo` | ❌ não implementado | ADR-001 escrito, aguarda migração IQR |
| `aditivo_teto` | ❌ não implementado | Depende de z_score_aditivo migration |
| `rede_empresas_score` | ❌ não implementado | Sem ETA |
| `flag_prefeito_ultimo_mandato` | ❌ não implementado | Depende de dados TSE |
| `threshold_gaming_score` | ❌ não implementado | AP-5, urgente quando produto público |
| `iqr_score_aditivo` (substitui z_score) | ❌ não implementado | ADR-001 aceito |

**Sinais de pré-filtro (não features do score):**
| Pré-filtro | Status |
|------------|--------|
| CEIS como pré-filtro prioritário | 🟡 formalização pendente (está no score hoje) |
| CNAE × objeto como habilitação | ❌ bloqueado (tabela de mapeamento não pública) |

---

## Arquitetura de Loaders

| Loader | Propósito | Estado |
|--------|-----------|--------|
| `ceis_cnep_cepim.py` | Sanções CEIS/CNEP/CEPIM → raw → staging | ✅ em produção |
| `pncp_contracts.py` | Contratos PNCP → raw → staging | ✅ em produção |
| `pncp_contract_updates.py` | Atualizações de contratos PNCP | ✅ em produção |
| `feature_compute.py` | Computa features → `risk.feature_vector` | ✅ em produção |

**Invariante de design:** loaders não emitem claims de risco. Risco é packet-only.
Separação: `loaders/` ingesta → `packets/` interpreta.

---

## DB Tables Relevantes

| Tabela | Propósito |
|--------|-----------|
| `risk.feature_vector` | Feature values por empresa (`feature_key`, `value_numeric`, `value_boolean`, `stale`) |
| `pncp.contracts_staging` | Contratos PNCP normalizados (sem score) |
| `sanctions.ceis_staging` / `cnep_staging` / `cepim_staging` | Sanções normalizadas |

---

## Pacotes de Resposta

| Pacote | Propósito | Audience |
|--------|-----------|----------|
| `supplier_risk_check_v1` | Risk check com sanções + contratos | internal / institutional |
| `supplier_credit_v1` | Avaliação de crédito | internal |
| `supplier_esg_v1` | Avaliação ESG | internal |
| `supplier_factual` | Dados factuais RFB + sanções + PNCP | base para todos |

---

## O que o /ask pode sugerir com segurança

- Implementações novas na camada `loaders/` usando `FeatureDefinition` + `register_strategy()`
- Novos `feature_key` strings para `risk.feature_vector`
- Expansão de `FEATURE_KEYS` em `supplier_risk_check_v1.py`
- Lógica de `recommended_attention` baseada em múltiplos sinais (hoje só sanctions/has_public_contract)
- `enrich_zscores()` pattern: segunda passagem após normalização para features que precisam de histórico agregado

**Não sugerir sem verificar:**
- `pncp_supplier_contracts.py` — não existe em `src/zelox/` (referenciado no KB mas não localizado)
- Qualquer função que busque `z_score_aditivo` — não existe ainda

---

## Referências

- `BACKLOG.md` — itens pendentes com prioridade e origem KB
- `docs/spec-driven/adrs/001-zscore-to-iqr-aditivo.md` — decisão de migrar para IQR
- [[anti-patterns-epistemic-ml]] — 5 anti-padrões com instâncias Zelox
- [[z-score-aditivo]] — calibração empírica do z_score existente
- [[zelox-mvp-laudo-aditivos]] — primeiro caso de uso pagável
