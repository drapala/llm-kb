---
title: "AI Technical Debt — Taxonomy and Conceptual Framework"
sources:
  - path: raw/papers/sculley-2015-hidden-tech-debt-ml.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/recupito-palomba-2024-ai-tech-debt.md
    type: paper
    quality: secondary
    stance: confirming
  - path: raw/papers/moreschini-2026-evolution-tech-debt-genai.md
    type: paper
    quality: secondary
    stance: confirming
created: 2026-04-11
updated: 2026-04-11
tags: [technical-debt, taxonomy, ml-systems, prompt-debt, explainability-debt, sculley, moreschini]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
quarantine: true
quarantine_reason: "Gate 3 invalidou: (1) citação 'organism not a component' não encontrada no raw/ do Sculley 2015 — possivelmente fabricada; (2) 'toda literatura posterior usa este vocabulário' — universalização falsa; (3) modelos flagaram Moreschini 2026 como 'data impossível' (falso positivo dado que estamos em 2026-04-11, mas outros claims do artigo precisam revisão). Fixes necessários."
quarantine_date: 2026-04-11
synthesis_sources:
  - raw/papers/sculley-2015-hidden-tech-debt-ml.md
  - raw/papers/recupito-palomba-2024-ai-tech-debt.md
  - raw/papers/moreschini-2026-evolution-tech-debt-genai.md
---

## Resumo
Sculley et al. (Google/NeurIPS 2015) cunhou o vocabulário fundacional: glue code, pipeline jungles, undeclared consumers — dívidas de ML invisíveis a métricas tradicionais. Recupito & Palomba (JSS 2024) atualizaram para AI-enabled systems, documentando paradoxo practitioners: baixa prevalência percebida, alta severidade percebida, impacto principal em understandability e security. Moreschini et al. (JSS 2026) expandiu para GenAI, cunhando "prompt debt" (prompts não-versionados e inconsistentes) e "explainability debt" (incapacidade de explicar decisões de componentes AI).

## Conteúdo

### Sculley et al. 2015 — O framework fundacional

Paper de engenheiros do Google que identificou formas de dívida em sistemas ML invisíveis a ferramentas de qualidade convencionais.

**As formas principais:**

| Forma de dívida | Descrição |
|-----------------|-----------|
| **Entanglement (CACE)** | Changing Anything Changes Everything — qualquer mudança em features ou thresholds altera o sistema inteiro |
| **Hidden Feedback Loops** | Modelo influencia o mundo → muda dados de retreino → loop não-monitorado |
| **Undeclared Consumers** | Outros sistemas dependem do output do modelo sem declaração formal |
| **Unstable Data Dependencies** | Features de outras equipes que podem mudar sem aviso |
| **Configuration Debt** | Hiperparâmetros e thresholds raramente versionados ou testados |
| **Glue Code** | Sistema ML em produção tipicamente tem ML como pequena fração; a maior parte é wrappers e adaptadores (⚠️ proporção 5%/95% é anedotal em Sculley, não estatística da indústria) |
| **Pipeline Jungles** | Preprocessing steps ad-hoc que ninguém entende completamente |
| **Dead Experimental Codepaths** | Experimentos passados como código condicional nunca removido |

**Status:** paper fundacional — a maioria da literatura posterior de AI technical debt referencia este vocabulário (glue code, pipeline jungles, undeclared consumers, CACE). (⚠️ literatura subsequente também usa taxonomias próprias — MLOps debt, governance debt — não derivadas diretamente de Sculley.)

### Recupito & Palomba 2024 — AI-Enabled Systems

Survey com 53 AI developers sobre AI Technical Debt (AITD) em sistemas que *usam* AI (não apenas sistemas de ML puro).

**Paradoxo dos practitioners:**
- Prevalência percebida: **baixa**
- Severidade percebida: **alta**

AITD não ocorre frequentemente, mas quando ocorre tem impacto severo — especialmente em **understandability** e **security**.

**Estratégias de gestão atuais:** ad-hoc. Manual review e refactoring reativo. Sem ferramentas especializadas.

**Taxonomia implícita no paper:**
1. Model debt — modelos desatualizados ou não-monitorados
2. Data debt — qualidade de dados de treino, data drift
3. Infrastructure debt — dependências frágeis em frameworks ML
4. Process debt — ausência de MLOps, CI/CD para modelos
5. Architecture debt — integração de AI sem separação de concerns

### Moreschini et al. 2026 — GenAI Extensions

Multivocal review de 61 fontes (peer-reviewed + grey literature). Identificou formas de dívida específicas de sistemas que usam LLMs.

**Prompt Debt** — nova categoria:
- Prompts ad-hoc sem controle de versão
- Inconsistência entre prompts em diferentes partes do sistema
- Ausência de testes de prompt
- Degradação silenciosa quando o modelo muda

**Explainability Debt** — nova categoria:
- Incapacidade de explicar decisões de componentes AI a reguladores, auditores, ou usuários
- Dependência de comportamentos emergentes não-documentados
- Risco crescente com regulações de AI (EU AI Act)

**Extensões do framework de Sculley para GenAI:**
| Sculley (ML, 2015) | Moreschini (GenAI, 2026) |
|--------------------|-------------------------|
| Configuration debt | Prompt debt |
| Undeclared consumers | Dependências implícitas de APIs de LLM |
| Pipeline jungles | Chains de prompts e RAG pipelines ad-hoc |
| Hidden feedback loops | Outputs de LLM usados para avaliar ou retreinar LLMs |

### A evolução do conceito

```
Sculley 2015           Recupito 2024          Moreschini 2026
(ML Systems)     →    (AI-Enabled Systems) →  (GenAI Systems)
glue code             understandability       prompt debt
pipeline jungles      security impact         explainability debt
undeclared consumers  ad-hoc management       prompt versioning gap
```

Cada camada adiciona formas novas sem invalidar as anteriores — acumulação de tipos de dívida conforme AI se torna mais central nos sistemas.

## Verificação adversarial

**Claim mais fraco:** "prompt debt" é conceito emergente sem operacionalização robusta — como medir se um prompt está em "dívida" não tem consenso na literatura em 2026.

**O que os papers não dizem:** (1) Recupito & Palomba não quantificam o custo real da AITD em projetos reais; (2) Moreschini é MLR — qualidade heterogênea das 61 fontes; (3) Sculley descreve sistemas ML de 2015 — generalizações para LLMs de 2025 são inferências, não dados.

**Simplificações:** a taxonomia de Sculley foi construída para sistemas ML closed-source do Google — contexto muito diferente de sistemas que consomem APIs de LLM externas.

## Quality Gate
- [x] Wikilinks tipados: sem wikilinks externos necessários
- [x] Instance→class: claims por paper claramente atribuídos com fonte e contexto
- [x] Meta-KB separado: nenhuma referência a design da KB
- [x] Resumo calibrado: inclui que "prompt debt" é emergente sem operacionalização

## Conexões
- ai-generated-code-debt-empirical validates ai-technical-debt-taxonomy (dados empíricos 2025-26 instanciam categorias do framework)
- ai-productivity-paradox partOf ai-technical-debt-taxonomy (comprehension debt como nova categoria pós-Sculley)

## Fontes
- [Sculley et al. 2015](../../raw/papers/sculley-2015-hidden-tech-debt-ml.md) — glue code, pipeline jungles, undeclared consumers, CACE
- [Recupito & Palomba 2024](../../raw/papers/recupito-palomba-2024-ai-tech-debt.md) — paradoxo prevalência/severidade, understandability, security, ad-hoc management
- [Moreschini et al. 2026](../../raw/papers/moreschini-2026-evolution-tech-debt-genai.md) — prompt debt, explainability debt, evolução do framework
