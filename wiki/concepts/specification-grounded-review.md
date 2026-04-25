---
title: "Specification-Grounded LLM Review"
sources:
  - path: raw/papers/wang-2025-sgcr-specification-grounded-review.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/icoz-2025-symbolic-reasoning-llm-code-review.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-23
updated: 2026-04-23
tags: [code-review, llm, specification, grounding, dual-pathway, rag, software-engineering]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
reads: 0
retrievals_correct: 0
retrievals_gap: 0
freshness_status: current
quarantine: false
quarantine_promoted: 2026-04-23
quarantine_criteria_met:
  auto_promote: true
  gates_passed: [1, 2, 4]
  gate3_skipped: staleness
  newest_source_yyyymm: "2025-12"
  challenge_verdict: PUBLICÁVEL
topics: [code-review, specification-grounding, llm-review, context-control, software-quality]
depends_on:
  - raw/papers/wang-2025-sgcr-specification-grounded-review.md
synthesis_sources:
  - raw/papers/wang-2025-sgcr-specification-grounded-review.md
  - raw/papers/icoz-2025-symbolic-reasoning-llm-code-review.md
---

## Resumo

Specification-grounding ancora LLMs de code review em regras explícitas e verificáveis do projeto — substituindo dependência de conhecimento implícito pré-treinado por constraints determinísticos. SGCR (Wang et al. 2025, HiThink Research) demonstrou 42% de adoption rate vs. 22% baseline (+90.9% relativo) via dual-pathway: explicit path (ensemble contra specs) + implicit path (heurística livre → verificação contra specs via RAG). A abordagem resolve os problemas centrais de LLMs genéricos em code review: falta de contexto de domínio, estochasticidade e falta de controlabilidade.

## Conteúdo

### O problema que specification-grounding resolve

LLMs genéricos em code review falham por quatro razões identificadas por Wang et al. 2025:

1. **Falta de contexto de domínio** — LLMs treinados em open-source não conhecem business logic, APIs proprietárias ou convenções arquiteturais do projeto
2. **Estochasticidade** — mesmo prompt produz feedback diferente em runs distintos (erode credibilidade)
3. **Controlabilidade pobre** — LLMs fixam em questões triviais de estilo enquanto ignoram bugs críticos de performance ou segurança
4. **Falta de explainability** — developers não entendem por que uma sugestão foi gerada → não confiam → não adotam

Specification-grounding resolve os quatro: injeta domínio via specs, estabiliza via ensemble, controla prioridade via metadados de severidade nas specs, explica linkando cada sugestão à regra que a originou.

### Arquitetura SGCR: Dual-Pathway

**Path 1 — Explicit Specification Injection:**

```
Specs humanas → Ensemble N LLMs (paralelo) → Aggregator LLM → R_explicit
```

- N instâncias independentes revisam o código contra as specs
- Aggregator sintetiza, resolve conflitos, prioriza por severidade
- Para specs longas: divide em chunks → processa em paralelo → sintetiza (resolve [[attention-dilution-llm-context]])
- Determinístico: cada sugestão tem regra específica como âncora

**Path 2 — Implicit Specification Discovery:**

```
Código → Proposer LLM (sem specs) → Q_hypo → Embedding → Vector DB de specs → Verifier ensemble → R_implicit
```

- Proposer analisa sem constraints → captura issues que o olhar direto nas specs perderia
- Para cada hipótese: busca semântica nas specs recupera regras relacionadas
- Verifier confirma/rejeita cada hipótese contra as specs recuperadas
- Preserva capacidade heurística do LLM, mas filtra alucinações via grounding

**Agregação final:** De-duplicação + priorização por severidade + opcionalmente gera code patches guiados pelas specs.

### Ablação de componentes

| Configuração | Adoption Rate |
|-------------|---------------|
| SGCR Full (explicit + implicit) | **42%** |
| Explicit-Only | 37% |
| Implicit-Only | 29% |
| Baseline LLM (sem specs) | 22% |

Explicit path é o principal driver (+15 pp sobre baseline). Implicit path adiciona 5 pp como "safety net" — captura issues que o checklist explícito perderia.

### Versão simplificada: Knowledge Map

İçöz & Biricik (2025) implementam o princípio de forma mais simples: um mapa estático de 20 bug patterns Python injetado no prompt como "symbolic reasoning". Sem RAG, sem ensemble, sem specs por projeto. Resultado: +16% accuracy vs. base LLM.

Progressão: Knowledge Map (estático, genérico) → SGCR (dinâmico, project-specific via RAG). O princípio compartilhado é que estrutura explícita de conhecimento injeta estabilidade e controlabilidade que o modelo implícito não tem.

### Requisitos operacionais

- **Spec library**: coleção curada de regras específicas do projeto (HiThink: 140 regras Java)
- **Vector DB**: para busca semântica de specs no implicit path
- **Ensemble de LLMs**: para estabilidade (pode ser substituído por temperatura baixa em modelos maiores)
- **Overhead de manutenção**: specs precisam ser atualizadas quando o projeto evolui (principal queixa dos developers no estudo)

### Comparação com abordagens alternativas

| Abordagem | Mecanismo central | Adoption/Precision | Escalabilidade |
|-----------|------------------|--------------------|---------------|
| SGCR | Spec-grounding + dual-path | 42% adoption | Alta (manutenção de specs) |
| BitsAI-CR | Two-stage filter + rules taxonomy | 75% precision | Alta (data flywheel) |
| RovoDev | RAG para contexto mínimo | 38.7% code resolution | Alta (sem fine-tuning) |
| LAURA | RAG + exemplar retrieval | 42.2% helpful | Média (precisa de histórico de reviews) |
| Generic LLM | Conhecimento implícito | 16-22% adoption | Alta (zero-setup) |

## Interpretação

(⚠️ nossa interpretação) Specification-grounding e [[agentic-codebase-enforcement-patterns]] são estratégias complementares: enforcement via hooks garante invariantes de processo (nunca editar raw/, registry atualizado), enquanto spec-grounding garante qualidade de review em código. A distinção é que hooks são determinísticos por construção, enquanto SGCR usa specs para aproximar determinismo em outputs LLM.

(⚠️ nossa interpretação) O overhead de manutenção de specs é o principal tradeoff contra abordagens RAG-only (RovoDev). Para projetos com documentação de regras existente (ADRs, coding standards, security policies), o custo é baixo — as specs já existem e só precisam ser formatadas. Para projetos sem documentação, o custo inicial é alto.

## Conexões

- partOf: [[llm-automated-code-review]] — uma das abordagens que funciona industrialmente
- validates: [[attention-dilution-llm-context]] — chunk-based processing do explicit path resolve attention dilution documentada por Kumar 2026
- complementa: [[agentic-codebase-enforcement-patterns]] — abordagem complementar de enforcement
- partOf: [[codified-context-codebase-agents]] — specs são uma forma de codified context para agents
- emerge-para: [[variety-amplification-llm-review]] ON "spec library como variety amplifier do LLM para domínio específico"
- emerge-para: [[vsm-blast-radius-routing-calibration]] ON "blast-radius como roteador de qual camada de review ativar"

## Fontes

- [Wang 2025 SGCR](../../raw/papers/wang-2025-sgcr-specification-grounded-review.md) — 140 regras Java, 42% vs 22%, dual-pathway completo, ablação
- [İçöz 2025](../../raw/papers/icoz-2025-symbolic-reasoning-llm-code-review.md) — versão simplificada: knowledge map estático, +16% accuracy

## Verificação adversarial

**Claim mais fraco:** "Specification-grounding resolve os quatro problemas de LLMs genéricos." — Testado apenas em HiThink Research (Java, 140 regras, 200 participantes). Generalização para outros stacks ou projetos sem documentação existente não está demonstrada.

**O que os papers NÃO dizem:**
- SGCR não compara contra static analysis tools (SonarQube, PMD) — que detectam apenas ~16% dos issues humanos mas são completamente determinísticos
- İçöz 2025 testa em dataset laboratorial (CodeXGLUE), não em PRs reais

**Simplificações feitas:** O implicit path é chamado de "unconstrained" mas o proposer ainda tem o código fonte como contexto — não é realmente sem constraints, apenas sem specs explícitas.

**Prior work:** Bacchelli & Bird 2013 (Modern Code Review), McIntosh et al. 2016 (impacto de code review em software quality), Singh et al. 2017 (static analysis reduz review effort).

## Quality Gate

- [x] Wikilinks tipados: 4 relações (partOf x3, validates)
- [x] Instance→class: claims com fonte, dataset e limitações
- [x] Meta-KB separado: sem referências a comandos internos
- [x] Resumo calibrado: menciona "HiThink Research" especificamente, não generaliza
