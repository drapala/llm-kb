---
title: "Sinal CNAE × Objeto — Pré-filtro de Habilitação no Zelox"
sources:
  - path: raw/papers/oliveira-pappa-2022-webmedia-inconsistencies.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/brandao-pappa-2024-plus-pipeline.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-12
updated: 2026-04-12
tags: [zelox, CNAE, procurement-fraud, feature, pre-filter, habilitacao, b2g, signal-design]
source_quality: low
interpretation_confidence: medium
resolved_patches: []
provenance: emergence
emergence_trigger:
  pair: [oliveira-pappa-2022-webmedia-inconsistencies, laic-ufmg-procurement-fraud-detection]
  ask_session: outputs/logs/sessions/2026-04-12/ask-cnae-objeto.md
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-12
status: promoted
promoted_date: 2026-04-12
---

## Resumo

A incompatibilidade entre CNAE do fornecedor e tipo de objeto contratado é um sinal de anomalia de habilitação proposto pelo LAIC/UFMG (Oliveira WebMedia 2022) e incorporado no PLUS pipeline. **Conclusão da análise /ask:** o sinal não deve entrar no `risk_score` como feature contínua — é arquiteturalmente um pré-filtro de triagem, não um componente do score. O mesmo padrão se aplica ao CEIS (sanção formal) e outros sinais binários de desqualificação.

## Conteúdo

### O sinal (Oliveira WebMedia 2022)

Compatibilidade entre a descrição do item licitado e o CNAE (Classificação Nacional de Atividades Econômicas) do licitante. Abordagem hierárquica de decisão:

- **Válido:** CNAE compatível com o objeto — nenhuma anomalia detectada
- **Duvidoso:** compatibilidade parcial — requer análise adicional
- **Inválido:** CNAE incompatível com o objeto — alerta imediato

**Dado público:** CNAE disponível via Receita Federal API (CNPJ). O join é trivial.

**Gargalo técnico:** a tabela de mapeamento CNAE → tipos de objeto compatíveis não é um dado público estruturado. O paper Oliveira 2022 deve incluir essa tabela — não disponível no STUB. Uma alternativa é usar NLP (GovBERT-BR + clustering de itens da LREC 2024) para derivar compatibilidade semanticamente.

### Por que não é uma feature do risk_score

Os 4 sinais Zelox (`aditivo_teto`, `z_score_aditivo`, `rede_empresas_score`, `compliance_rule`) medem **grau de anomalia** numa escala contínua. CNAE × objeto é uma **verificação de elegibilidade** — o licitante deveria estar impedido de participar da licitação.

Combinar os dois tipos no mesmo score dilui cada dimensão:
- Um contrato CNAE-incompatível mas com z_score_aditivo=0 recebe risk_score médio quando deveria receber alerta prioritário
- Um contrato CNAE-compatível mas com z_score alto fica penalizado pela ausência de CNAE flag quando esse não é o problema

O output de Oliveira 2022 (Válido/Duvidoso/Inválido) confirma: o sinal é nativamente uma classificação hierárquica de triagem, não um score contínuo.

### Arquitetura de pré-filtro (padrão genérico)

```
Contrato recebido
  ↓
[Camada de Pré-filtros — sinais binários/categóricos de desqualificação]
  │
  ├─ CNAE × objeto: Inválido?   → ⚠️ ALERTA PRIORITÁRIO (fora do risk_score pipeline)
  │                  Duvidoso?  → entra no pipeline com peso elevado
  │                  Válido?    → entra no pipeline normalmente
  │
  ├─ CEIS check: fornecedor sancionado?
  │              Sim (ativo)    → ⚠️ ALERTA PRIORITÁRIO
  │              Sim (expirado) → entra com flag histórico
  │              Não            → normal
  │
  └─ [outros pré-filtros futuros]
         ↓
[Risk Score Pipeline — sinais contínuos]
  │
  ├─ aditivo_teto
  ├─ z_score_aditivo (→ IQR no próximo ciclo)
  ├─ rede_empresas_score
  └─ compliance_rule
         ↓
[Risk Score consolidado → ledger]
```

**Propriedade chave do padrão:** pré-filtros produzem alertas que **precedem** o risk_score, não que **entram** nele. São sinais de elegibilidade — o objeto não deveria ter chegado ao pipeline. O risk_score mede anomalia dentro do conjunto de contratos elegíveis.

### CEIS como pré-filtro (não como feature)

O CEIS (Cadastro Nacional de Empresas Inidôneas e Suspensas) é o exemplo mais claro. Uma empresa sancionada que ganhou um contrato é, por si só, violação formal da Lei 14.133. Isso não precisa ser ponderado no risk_score — é um alerta direto.

Colocar o CEIS como feature contínua no score seria análogo a incluir "o contrato está vencido" como feature de risco: é uma condição binária de inelegibilidade, não um gradiente.

A mesma lógica se aplica a:
- CNPJ baixado/inativo na Receita Federal
- MEI contratado por valor acima do teto legal
- CNAE × objeto (Oliveira 2022)
- Fornecedor com prazo de reabilitação pendente (CEIS expirado mas em período de monitoramento)

### Checklist de implementação (CNAE × objeto)

| Etapa | Dado necessário | Fonte | Status |
|---|---|---|---|
| CNAE do fornecedor | CNPJ + CNAE primário e secundários | Receita Federal API | disponível |
| Tipo de objeto do contrato | categoria PNCP | PNCP API | disponível |
| Tabela de mapeamento CNAE → objeto | classificação manual ou NLP | Oliveira 2022 ou derivado | ❌ pendente |
| Classificador Válido/Duvidoso/Inválido | lógica de compatibilidade | Oliveira 2022 | ❌ pendente (STUB) |

**Bloqueador real:** a tabela de mapeamento. Sem ela, o sinal não é implementável com precisão aceitável. Com NLP (GovBERT-BR), é possível fazer matching semântico de descrição do item × atributos do CNAE — mas requer validação manual.

### Diferença de fase: por que está fora do Zelox V1.1

O Zelox V1.1 opera na fase de **execução contratual** (aditivos, delta_pct). O sinal CNAE × objeto é um sinal da **fase de licitação** (habilitação). A separação de fases não é apenas técnica — é o escopo do produto:

- V1.1 pergunta: "contratos vigentes têm padrão anômalo de execução?"
- CNAE × objeto pergunta: "o fornecedor deveria ter sido habilitado para esse contrato?"

O segundo pode ser o escopo do Zelox V2 (retrospecção de licitações) ou de um produto separado (módulo de due diligence de fornecedores).

## Verificação adversarial

- Oliveira WebMedia 2022 é STUB — sem métricas (precision/recall da classificação CNAE × objeto)
- Tabela de mapeamento CNAE → objeto não está documentada publicamente fora do paper
- CNAEs são auto-declarados e múltiplos: risco de falso positivo se empresa tem CNAE secundário compatível
- Incorporação no PLUS pipeline é evidência indireta de utilidade — mas PLUS também é STUB

## Conexões

- [[laic-ufmg-procurement-fraud-detection]] — fonte do sinal (Oliveira WebMedia 2022 + PLUS pipeline)
- [[zelox-mvp-laudo-aditivos]] — V1.1 foca em execução; CNAE × objeto é habilitação (fora do escopo atual)
- [[circular-ground-truth-ml-systems]] — o anti-padrão de pré-filtro-como-feature é análogo: misturar tipos de sinal degrada o sistema

## Fontes

- [Oliveira & Pappa 2022](../../raw/papers/oliveira-pappa-2022-webmedia-inconsistencies.md) — CNAE × objeto, Válido/Duvidoso/Inválido, WebMedia (STUB)
- [Brandão & Pappa 2024](../../raw/papers/brandao-pappa-2024-plus-pipeline.md) — incorporação do sinal no PLUS pipeline (STUB)
