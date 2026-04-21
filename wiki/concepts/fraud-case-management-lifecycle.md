---
title: "Fraud Case Management — Lifecycle de Investigação como Produto"
sources:
  - path: raw/articles/fraud-case-management-lifecycle.md
    type: article
    quality: secondary
    stance: neutral
created: 2026-04-12
updated: 2026-04-12
tags: [fraud, case-management, investigation, workflow, actimize, palantir, task, decision, outcome, product-design]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
status: promoted
promoted_date: 2026-04-12
freshness_status: current
---

## Resumo

Sistemas de investigação de fraude maduros (NICE Actimize, Palantir AIP, NICE Actimize ActOne) modelam o processo de investigação como um pipeline navegável de objetos: **case → task → decision → action → outcome**. O operador não vê só um score — vê um objeto de trabalho com estado, história auditável e próximo passo prescrito. Esta distinção entre "engine de scoring" e "sistema de investigação como produto" determina se a solução se encaixa no dia a dia operacional de um órgão/equipe ou permanece como ferramenta técnica externa.

## Conteúdo

### O Modelo de Objetos do Case Management

**Case (Caso):** unidade central de trabalho. Agrupa evidências, entidades envolvidas, alertas relacionados e histórico de decisões. Um caso pode ser aberto manualmente ou automaticamente por trigger de risco. Tem status (novo, em investigação, pendente, fechado), prioridade e responsável.

**Task (Tarefa):** unidade atômica de trabalho dentro de um caso. Exemplos: "verificar CNPJ", "solicitar documentação", "revisar contrato". Tasks têm dono, prazo, status e podem ter dependências entre si. A tarefa é o primitivo que viabiliza delegação e rastreamento de progresso.

**Decision (Decisão):** registro formal de julgamento. Exemplos: "suspeito confirmado", "falso positivo", "encaminhar para instância superior". Decisões são imutáveis após registro — criam o trail auditável. Têm autor, timestamp, justificativa e referência às evidências que a embasaram.

**Action (Ação):** operação executada após decisão. Exemplos: "bloquear fornecedor no sistema", "notificar CGU", "emitir laudo", "gerar referral para MPF". Actions podem ser automáticas (disparadas pelo sistema) ou manuais (executadas pelo operador). O registro da ação fecha o loop entre decisão e efeito.

**Outcome (Resultado):** estado final verificado. Exemplos: "fraude confirmada por auditoria", "irregularidade corrigida", "caso arquivado por insuficiência de evidência". O outcome é o sinal de aprendizado — sem ele, o sistema não sabe se suas predições foram corretas.

### Arquitetura de Produto: NICE Actimize

A plataforma ActOne unifica múltiplos sistemas de detecção (AML, fraude em pagamentos, insider threat) numa interface única de investigação. Princípios arquiteturais relevantes:

- **Entity-centric view:** o operador navega por entidade (pessoa, empresa), não por alerta isolado. Alertas são agrupados automaticamente por entidade relacionada.
- **Workflow configurable:** times de compliance configuram stages do workflow sem código. Diferentes tipologias de fraude têm workflows distintos.
- **Regulatory auditability:** toda decisão e ação é logada com metadados suficientes para satisfazer exigências de BACEN, COAF e reguladores equivalentes.
- **Collaborative investigation:** múltiplos analistas podem trabalhar no mesmo caso com visibilidade de quem fez o quê.

### Arquitetura de Produto: Palantir AIP Machinery

Palantir Machinery é o primitivo de orquestração de workflow do AIP. Permite:

- Modelar qualquer processo de negócio como grafo de estados
- Trazer humanos ao loop em pontos específicos (human-in-the-loop gates)
- Supervisionar workflows de AI agents em tempo real
- Auditar cada transição de estado com contexto completo

Para investigação de fraude, isso significa: o sistema pode automatizar tarefas de coleta e análise, mas reservar pontos específicos para julgamento humano (ex: decisão de referral institucional). O Machinery rastreia o tempo em cada estado — dado essencial para medir eficiência operacional.

### Por que "Case como Produto" é Diferente de "Score como Output"

| Dimensão | Score Engine | Case Management Product |
|----------|-------------|------------------------|
| Output primário | Score numérico | Objeto navegável com estado |
| Interface | API / dashboard analítico | Fila de trabalho + histórico |
| Rastreabilidade | Log técnico | Audit trail regulatório |
| Aprendizado | Retreino periódico | Feedback contínuo por outcome |
| Encaixe operacional | Ferramenta técnica externa | Parte do processo diário |
| Dado proprietário gerado | Predições | Decisões humanas + overrides + outcomes |

O dado mais valioso gerado por um case management system não é o score — são as **decisões humanas, overrides e outcomes**. Esses dados são exclusivos do produto e não podem ser replicados por concorrentes que apenas têm acesso às mesmas fontes públicas.

### Primitivos de UI/UX para Investigação Fraud

Interfaces de investigação madura tipicamente expõem:

1. **Investigation Queue:** fila priorizada de casos aguardando ação. Filtros por risco, prazo, tipo, responsável.
2. **Case Timeline:** linha do tempo de todos os eventos do caso (alertas, evidências adicionadas, decisões, ações tomadas).
3. **Entity Graph View:** visualização das relações entre entidades envolvidas no caso (useful para fraud rings e group risk).
4. **Evidence Panel:** documentos, dados, flags organizados por relevância.
5. **Decision Panel:** formulário estruturado para registrar decisão com justificativa e referência a evidências.
6. **Action Dispatcher:** interface para disparar ações downstream (notificações, bloqueios, laudos).
7. **Outcome Tracker:** painel para registrar resultado final quando disponível (fecha o loop de aprendizado).

## Interpretação

⚠️ Interpretação do compilador.

**Implicação direta para Zelox:** A superfície atual (loader → packet factual → risk check → job dispatch) implementa a camada de detecção mas não a camada de investigação. Para virar produto institucional, o próximo passo não é melhorar o score — é construir os objetos Case, Task, Decision, Action, Outcome como cidadãos de primeira classe da aplicação, com estado navegável e audit trail. Sem isso, o Zelox permanece uma engine que precisa de outro produto à frente para ser operável por um analista de compliance.

**O moat de dados está nos outcomes:** sistemas que registram sistematicamente o que aconteceu depois da decisão (foi auditado? irregularidade confirmada? fornecedor corrigiu o comportamento?) acumulam um dataset que concorrentes com acesso às mesmas fontes públicas não conseguem replicar.

## Verificação adversarial

**Claim mais fraco:** os primitivos listados (Case, Task, Decision, Action, Outcome) são amplamente documentados em literatura de ITSM/SIEM, mas a aplicação específica a fraud investigation em contexto B2G brasileiro não tem referência primária aqui — é extrapolação de padrões de produto observados em contexto financeiro privado (NICE Actimize) para contexto público.

**O que não está aqui:** como esses primitivos se mapeiam especificamente para os workflows do COAF, CGU, AGU e TCU. A regulação brasileira pode exigir campos ou fluxos não cobertos pelos produtos estrangeiros.

## Quality Gate
- [x] Instance→class: primitivos de produto são padrões observados, não afirmações causais
- [x] Meta-KB separado: sem autoreferência no Conteúdo
- [x] Resumo calibrado: source_quality medium (síntese de documentação de produto + literatura)

## Conexões
- fraud-case-management-lifecycle relates-to audit-risk-rent-extraction ON "o dado proprietário gerado por case management (outcomes confirmados) é o mesmo que valida o mecanismo de deterrência de Zamboni & Litschig"
- fraud-case-management-lifecycle relates-to gnn-fraud-detection-supply-chain ON "GNN detecta padrão de grupo; case management é onde o operador age sobre o padrão detectado"

## Fontes
- NICE Actimize — Enterprise Fraud Management Platform (documentação de produto, 2025)
- Palantir AIP — Machinery workflow orchestration (documentação de produto, 2025)
- FraudNet — Top Fraud Case Management Software Solutions (survey, 2025)
