---
title: "Agent Context Files — Evidência Empírica (AGENTS.md, CLAUDE.md, READMEs)"
sources:
  - path: raw/papers/lulla-2026-agents-md-impact.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/gloaguen-2026-evaluating-agents-md.md
    type: paper
    quality: primary
    stance: challenging
    challenging_type: content
  - path: raw/papers/chatlatanagulchai-2025-agent-readmes.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-11
updated: 2026-04-11
tags: [context-files, agents-md, claude-md, coding-agents, empirical, enforcement]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
quarantine: true
quarantine_reason: "Gate 3: (1) reconciliação eficiência/eficácia como single-factor oversimplification — Lulla e Gloaguen medem coisas diferentes em contextos diferentes, não necessariamente o mesmo fenômeno; (2) claims numéricos específicos (-28.6%, +20%) tratados como generalizáveis de amostras pequenas. Fixes aplicados; re-promoção requer verificação adicional das claims de reconciliação."
quarantine_date: 2026-04-11
synthesis_sources:
  - raw/papers/lulla-2026-agents-md-impact.md
  - raw/papers/gloaguen-2026-evaluating-agents-md.md
  - raw/papers/chatlatanagulchai-2025-agent-readmes.md
---

## Resumo
Três estudos empíricos (2025–2026) sobre context files para coding agents revelam uma tensão: Lulla et al. (2026) mostra -28.6% runtime e -16.6% tokens com AGENTS.md; Gloaguen et al. (2026, ETH) mostra que ambos os tipos de context file (LLM-generated e human-written) tendem a reduzir taxa de sucesso e aumentar custo de inference em +20%. Chatlatanagulchai et al. (2025) documenta o estado atual em 2.303 context files: functional requirements dominam (62-70%), non-functional (segurança, performance) presentes em apenas 14.5%.

## Conteúdo

### O Paradoxo dos Context Files

Os estudos divergem em resultado mas convergem na causa raiz:

| Estudo | N | Métrica | Resultado |
|--------|---|---------|-----------|
| Lulla et al. 2026 (2601.20404) | 10 repos, 124 PRs | Runtime, tokens | **-28.6% runtime, -16.6% tokens** |
| Gloaguen et al. 2026 (2602.11988) | SWE-bench + repos reais | Task success, inference cost | **Menos sucesso, +20% custo** |

A aparente contradição se resolve pela métrica: Lulla mede **eficiência** (velocidade, tokens); Gloaguen mede **eficácia** (tasks concluídas corretamente). Um agente que executa mais rápido mas acerta menos — cenário consistente com ambos os resultados.

### Por Que Context Files Falham em Sucesso (Gloaguen 2026)

Mecanismo identificado: agentes **respeitam** as instruções dos context files — o problema é quando as instruções são excessivas ou mal calibradas.

- Instruções desnecessárias tornam tarefas mais difíceis
- Ambos os tipos (LLM-generated e human-written) tendem a piorar vs. sem contexto
- Recomendação central: **"descrever apenas requisitos mínimos"**

O overlap com o paper de Lulla: AGENTS.md bem calibrado (mínimo, focado) pode produzir ganhos de eficiência sem penalidade de sucesso. O tamanho e qualidade do context file importam mais do que sua presença.

### O Que Está em Context Files na Prática (Chatlatanagulchai 2025)

Análise de 2.303 context files em 1.925 repositórios:

| Requisito | Prevalência |
|-----------|-------------|
| Implementation details | **69.9%** |
| Architecture | **67.7%** |
| Build/run commands | **62.3%** |
| Security | **14.5%** |
| Performance | **14.5%** |

**Achado sobre manutenção:** context files evoluem como código de configuração — "frequent, small additions" ao longo do tempo. Não são documentação estática, mas também não são código com testes.

### O Gap de Non-Functional Requirements

85% dos context files não especificam security, 85% não especificam performance. Isso explica dois fenômenos:

1. **Ox Security 2025 "insecure by dumbness"** (cf. [[ai-generated-code-debt-empirical]]): se o context file não menciona segurança, o agente não tem orientação específica do projeto sobre prioridade de segurança — depende apenas dos defaults de alinhamento do modelo base, que são genéricos e não específicos ao contexto do projeto.
2. **Gloaguen "requisitos desnecessários" degradam**: o que está nos context files é majoritariamente functional — e functional overspecification piora o agente mais do que ausência de non-functional.

### Implicações de Design

**Regra de ouro sugerida pelos três estudos** (⚠️ heurística derivada de evidências heterogêneas, não regra universalmente validada):

> Evidência sugere que context files são mais eficazes quando contêm: (1) constraints de boundary explícitos, (2) non-functional mínimos ausentes no codebase (security, performance), e (3) comandos operacionais. Gloaguen 2026 documenta que especificação funcional excessiva aumenta custo em +20% e reduz sucesso — o que sugere que o problema não é "functional context" em si, mas "functional context desnecessário ou mal calibrado."

Isso é o inverso do que developers intuitivamente fazem (Chatlatanagulchai: implementation details em 70% dos files).

## Verificação adversarial

**Claim mais fraco:** a reconciliação "eficiência vs. eficácia" entre Lulla e Gloaguen é interpretação plausível mas não testada diretamente — os dois estudos usam metodologias diferentes em contextos diferentes.

**O que os papers não dizem:** (1) qual seção específica do AGENTS.md produz o ganho de -28% de Lulla; (2) se o threshold de "mínimo" de Gloaguen é quantificável; (3) se o gap de non-functional em Chatlatanagulchai é intencional (não relevante para o projeto) ou por desconhecimento.

**Simplificações:** "AGENTS.md LLM-generated degrada" e "human-written também degrada" de Gloaguen pode não generalizar para context files bem projetados por humans com experiência em prompt engineering.

## Quality Gate
- [x] Wikilinks tipados: [[ai-generated-code-debt-empirical]] via gap de non-functional requirements
- [x] Instance→class: -28.6% qualificado como Lulla 2026, 10 repos; -20% custo qualificado como Gloaguen 2026
- [x] Meta-KB separado: sem referências a design da KB no Conteúdo
- [x] Resumo calibrado: tensão entre os estudos explicitada no resumo

## Conexões
- codified-context-codebase-agents validates agent-context-files-evidence (constituição como instância de context file bem calibrado — minimal, growing organically)
- ai-generated-code-debt-empirical partOf agent-context-files-evidence (gap de security em context files → "insecure by dumbness" em escala)

## Fontes
- [Lulla et al. 2026](../../raw/papers/lulla-2026-agents-md-impact.md) — -28.6% runtime, -16.6% tokens, 10 repos, 124 PRs
- [Gloaguen et al. 2026](../../raw/papers/gloaguen-2026-evaluating-agents-md.md) — LLM-generated e human-written degradam task success, +20% inference cost
- [Chatlatanagulchai et al. 2025](../../raw/papers/chatlatanagulchai-2025-agent-readmes.md) — 2.303 context files, functional 62-70%, non-functional 14.5%
