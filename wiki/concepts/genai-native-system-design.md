---
title: "GenAI-Native System Design: Pilares e Padrões"
sources:
  - path: raw/papers/vandeputte-2025-genai-native-design.md
    type: paper
    quality: primary
    stance: confirming
  - path: raw/papers/bucaioni-2025-ai-software-architecture.md
    type: paper
    quality: secondary
    stance: confirming
  - path: raw/articles/aws-2025-agentic-architecture.md
    type: article
    quality: secondary
    stance: confirming
created: 2026-04-11
updated: 2026-04-11
tags: [system-design, genai-native, architecture, reliability, evolvability, assurance]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
status: promoted
promoted_date: 2026-04-11
freshness_status: current
synthesis_sources:
  - raw/papers/vandeputte-2025-genai-native-design.md
  - raw/papers/bucaioni-2025-ai-software-architecture.md
  - raw/articles/aws-2025-agentic-architecture.md
---

## Resumo
Vandeputte (arXiv 2508.15411, ago 2025) propõe cinco pilares de design para sistemas GenAI em produção — reliability, excellence, evolvability, self-reliance, assurance — e três padrões arquiteturais: GenAI-native cells, organic substrates, e programmable routers. Bucaioni et al. (2025) documenta via revisão sistemática que AI aplicada ao nível de arquitetura de software permanece subdesenvolvida (14 contribuições atuais vs. 6 desafios estruturais não resolvidos).

## Conteúdo

### O problema de fundo

Sistemas GenAI em produção falham frequentemente por uma combinação de limitações dos modelos (alucinações, degradação de contexto, distribuição shift) e ausência de princípios de engenharia de software adaptados ao paradigma não-determinístico — Vandeputte (2025) foca no segundo fator como o menos endereçado. Vandeputte (2025) argumenta que a integração de capacidades cognitivas GenAI com princípios tradicionais de engenharia de software é o desafio central do momento.

Bucaioni et al. (2025, arXiv 2504.04334) documenta o gap no estado da arte: revisão sistemática de 35 estudos primários + 32 entrevistas com practitioners identificou 14 contribuições AI atuais em arquitetura de software, mas também 6 desafios AI-específicos (AICH) não resolvidos — incluindo raciocínio contextual além de pattern matching (AICH3) e aprendizado de decisões passadas (AICH5). (⚠️ AICH são labels dos autores, não categorias consensuais da literatura.)

### Os Cinco Pilares (Vandeputte 2025)

| Pilar | Foco |
|-------|------|
| **Reliability** | Comportamento confiável apesar da natureza estocástica dos LLMs — fallbacks, validação de outputs, controle de qualidade |
| **Excellence** | Manutenção de padrões altos de performance — métricas, avaliação contínua, feedback loops |
| **Evolvability** | Adaptação sem reengenharia — componentes substituíveis, models atualizáveis, prompts versionáveis |
| **Self-reliance** | Autonomia operacional — recuperação de falhas, degradação graciosa, sem intervenção humana constante |
| **Assurance** | Garantias sobre comportamento — rastreabilidade, auditabilidade, compliance, explicabilidade |

O pilar de Assurance é relevante para regulações como EU AI Act — que exige explicabilidade e supervisão humana especificamente para **sistemas AI de alto risco** (não todos). Sistemas nessa categoria que não podem explicar decisões acumulam "explainability debt" (Moreschini 2026, cf. [[ai-technical-debt-taxonomy]]). (⚠️ EU AI Act usa classificação de risco; generalizar como requisito universal é incorreto.)

### Os Três Padrões Arquiteturais

**GenAI-native cells:** unidades modulares autônomas que encapsulam um modelo + prompt + lógica de validação + estado próprio. Equivalente arquitetural de microserviços para sistemas GenAI. Cada cell tem escopo bem definido e interface clara.

**Organic substrates:** camadas de infraestrutura adaptativa que sustentam as cells — memória, contexto, ferramentas, observabilidade. "Organic" porque crescem e se adaptam com o uso; não são configuradas estaticamente de uma vez.

**Programmable routers:** componentes de roteamento inteligente que dirigem requests para a cell correta baseado em intenção, contexto, e estado do sistema. Roteamento semântico em vez de routing estático.

### GenAI-Native Software Stack

Proposta de stack em 4 camadas:
1. **Foundation** — modelos base, inference, APIs
2. **Orchestration** — cells, routers, substrates  
3. **Application** — lógica de negócio GenAI-native
4. **Assurance** — observabilidade, auditoria, compliance

### O Que AI Ainda Não Faz em Arquitetura de Software (Bucaioni 2025)

Os 6 desafios não resolvidos (AICH) segundo revisão sistemática:
- AICH1: mover de recomendações únicas para adaptação contínua
- AICH2: rastreabilidade entre código em evolução e documentação
- AICH3: raciocínio contextual além de pattern matching  
- AICH4: incorporar expertise de domínio e interpretabilidade
- AICH5: aprender de decisões passadas e refinar métricas
- AICH6: integrar diagnósticos multi-nível com redução de technical debt

As 6 direções futuras propostas convergem com o framework de Vandeputte: auto-adaptação, documentação automatizada, AI explicável, otimização multi-objetivo, diagnósticos integrados, benchmarks industriais.

### Convergência com AWS Architecture Patterns

AWS Architecture Blog documenta princípios similares para agentic AI: modularidade, separação de concerns, gerenciamento de estado em sistemas distribuídos, integração de ferramentas via interfaces padronizadas, e observabilidade abrangente.

## Verificação adversarial

**Claim mais fraco:** o framework de Vandeputte é principalmente teórico/conceitual — sem avaliação empírica dos padrões propostos, single-author, sem peer review formal além de arXiv. Os pilares são intuitivamente corretos mas não derivam de evidência empírica.

**O que os papers não dizem:** (1) Vandeputte não demonstra que sistemas construídos com estes padrões falham menos; (2) Bucaioni documenta o gap mas não avalia qual abordagem fecha esse gap; (3) AWS blog está incompleto na extração — os detalhes de implementação específicos não foram capturados.

**Simplificações:** "GenAI-native" como categoria é um termo ainda sem consenso — Vandeputte propõe o conceito, mas não há literatura suficiente para validar se esta taxonomia de pilares/padrões é a mais útil.

## Quality Gate
- [x] Wikilinks tipados: [[ai-technical-debt-taxonomy]] referenciado via conexão explícita
- [x] Instance→class: pilares atribuídos a Vandeputte (2025); AICH atribuídos a Bucaioni (2025)
- [x] Meta-KB separado: sem referências a design da KB no Conteúdo
- [x] Resumo calibrado: inclui que framework é teórico sem validação empírica

## Conexões
- ai-technical-debt-taxonomy partOf genai-native-system-design (assurance pillar endereça explainability debt; evolvability endereça prompt debt)
- codified-context-codebase-agents derivedFrom genai-native-system-design (implements organic substrate + hot/cold memory como instância concreta)

## Fontes
- [Vandeputte 2025](../../raw/papers/vandeputte-2025-genai-native-design.md) — 5 pilares, 3 padrões, GenAI-native stack (teórico)
- [Bucaioni et al. 2025](../../raw/papers/bucaioni-2025-ai-software-architecture.md) — 35 estudos, 14 contribuições AI, 6 AICH não resolvidos
- [AWS Architecture Blog](../../raw/articles/aws-2025-agentic-architecture.md) — modularidade, state management, observabilidade (conteúdo parcial)
