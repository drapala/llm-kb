---
title: "Claude Code: Architecture Analysis (Design Space)"
sources:
  - path: raw/papers/liu-2026-claude-code-design-space.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-18
updated: 2026-04-18
tags: [agents, claude-code, harness, architecture, design-space, extensibility]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
reads: 1
last_read: 2026-04-18
retrievals_correct: 1
provenance: source
freshness_status: current
quarantine: false
quarantine_promoted: 2026-04-18
quarantine_criteria_met:
  auto_promote: true
  gates_passed: [1, 2, 3, 4]
  gate3_skipped: staleness
  challenge_verdict: PUBLICÁVEL
topics: [harness-engineering, agentic-coding, extensibility, context-management, permission-system]
depends_on: []
---

## Resumo

Liu et al. (2026) analisam o código TypeScript open-source do Claude Code (v2.1.88) e identificam **5 valores → 13 design principles → escolhas de implementação específicas**. O núcleo é um while-loop simples; a maior parte do código vive nos sistemas ao redor desse loop. Comparado com OpenClaw, as mesmas perguntas de design recorrentes produzem respostas arquiteturais distintas por contexto de deployment.

## Conteúdo

### 5 Valores Humanos que Motivam a Arquitetura

1. **Human decision authority** — modelo propõe, humano aprova ações de alto risco
2. **Safety and security** — classificação ML por ação + 7 modos de permissão graduados
3. **Reliable execution** — harness determinístico em torno de modelo não-determinístico
4. **Capability amplification** — ferramentas, MCP, mecanismos de extensibilidade
5. **Contextual adaptability** — hooks, skills, recuperação de sessão

### Core: While-Loop + Harness Denso

```
while(true) {
  call_model()
  run_tools()
}
```

A lógica é trivial. A complexidade está no harness:

**Permission System (7 modos)**
- Graduated trust: algumas ações sempre permitidas, algumas sempre requerem aprovação, a maioria é context-dependent
- ML-based classifier por ação (separado dos modos explícitos)

**Context Management (5-Layer Compaction Pipeline)**
- Layer 1: acumulação raw de contexto
- Layer 2: compressão de tool outputs
- Layer 3: sumarização de conversa
- Layer 4: compressão de sessão longa
- Layer 5: memória cross-sessão (append-oriented session storage — nunca sobrescreve)

**4 Mecanismos de Extensibilidade**
- **MCP**: ferramentas/servidores externos
- **Plugins**: extensões first-party
- **Skills**: workflows reutilizáveis
- **Hooks**: automação event-triggered

**Delegation**
- Subagent dispatch mechanism
- Worktree isolation: cada subagente em worktree git separada

### Comparação Claude Code vs OpenClaw

| Pergunta de Design | Claude Code | OpenClaw |
|---|---|---|
| Modelo de segurança | Classificação ML por ação | Controle de acesso perimetral |
| Modelo de execução | Single CLI while-loop | Runtime embeddado em gateway |
| Extensibilidade | Extensions de context-window (MCP, hooks) | Registro de capability gateway-wide |
| Composição | Pode ser hospedado pelo OpenClaw via ACP | Gateway multi-canal |

### 6 Direções Abertas para Sistemas Futuros

1. **Preservação da capacidade humana** — sistemas atuais têm mecanismos limitados para manter compreensão humana de longo prazo
2. **Coerência de codebase** — agentes podem quebrar padrões arquiteturais sem mecanismo de enforcement
3. **Integração no pipeline de desenvolvimento** — CI/CD, code review, merge: agentes operam fora desses loops de feedback
4. **Evolução do modelo de permissão** — 7 modos são estáticos; calibração dinâmica de confiança
5. **Padrões de coordenação multi-agente** — sem protocolos padronizados para composição CC ↔ OpenClaw
6. **Metodologia de avaliação** — SWE-bench insuficiente para medir efeitos de longo prazo em manutenibilidade

## Verificação adversarial

**Claim mais fraco:** a derivação "valores → princípios → implementação" é interpretativa — os autores inferem os valores a partir do código, não a partir de documentação interna da Anthropic. Pode haver discrepância entre intenção declarada e arquitetura real.

**O que o paper NÃO diz:**
1. Não mede eficácia empírica de cada mecanismo (apenas descreve)
2. Não analisa versões anteriores — pode ser snapshot temporário
3. Não verifica se 7 modos de permissão são suficientes para enterprise use cases

**Simplificações feitas:** a comparação CC vs OpenClaw é qualitativa; não há benchmark de performance entre as arquiteturas.

**Prior work:** SWE-bench, Claude Code documentation oficial, OpenClaw source code.

## Interpretação

(⚠️ nossa interpretação) A finding de que "codebase coherence e pipeline integration são problemas abertos" é relevante para design de qualquer pipeline Jira→PR: o agente pode gerar código que passa testes mas viola invariantes arquiteturais. O harness precisa de enforcement de coerência, não apenas de permissões.

(⚠️ nossa interpretação) O ML-based classifier por ação (separado dos 7 modos explícitos) é o mecanismo que permite que o mesmo comando tenha decisões de permissão diferentes em contextos diferentes — é adaptive enforcement, não static enforcement.

## Conexões

- validates: [[codified-context-codebase-agents]] ON "4 extensibility mechanisms (MCP/plugins/skills/hooks) confirmados empiricamente via análise de source code"
- partOf: [[natural-language-agent-harness]] ON "Claude Code é instância concreta do NLAH pattern — harness NL executável com runtime IHR"
- refines: [[agentic-codebase-enforcement-patterns]] ON "permission system com ML classifier por ação é enforcement layer mais granular que hook/CLAUDE.md/linter tabela existente"

## Fontes

- [Liu et al. 2026 — Dive into Claude Code (arXiv 2604.14228)](../../raw/papers/liu-2026-claude-code-design-space.md) — análise completa da source code

## Quality Gate

- [x] Wikilinks tipados: 3 (validates, partOf, refines)
- [x] Instance→class: versão específica v2.1.88 declarada; comparação com OpenClaw é qualitativa
- [x] Meta-KB separado: sem referências a /ask ou /ingest no Conteúdo
- [x] Resumo calibrado: limitações (interpretativo, não empírico) documentadas em Verificação adversarial
