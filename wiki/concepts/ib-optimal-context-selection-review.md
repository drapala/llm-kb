---
title: "IB-Optimal Context Selection for LLM Code Review"
sources:
  - path: wiki/concepts/attention-dilution-llm-context.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/information-bottleneck.md
    type: synthesis
    quality: primary
created: 2026-04-23
updated: 2026-04-23
tags: [information-bottleneck, code-review, context-selection, llm, rag, compression]
source_quality: medium
interpretation_confidence: low
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: true
quarantine_created: 2026-04-23
quarantine_reason: "Artigo emergido de /ask cross-domain — aguarda confirmação adversarial e review frio"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
provenance: emergence
emergence_trigger:
  pair: [attention-dilution-llm-context, information-bottleneck]
  ask_session: outputs/logs/sessions/2026-04-23/ask-emerge-pairs.md
  connection_type: ANÁLOGO-A
  pearl_level: L2
emerged_on: 2026-04-23
topics: [context-selection, information-theory, code-review, rag, llm-context]
---

## Resumo

O problema de context selection para LLM code review tem formulação ótima via Information Bottleneck: dado o contexto bruto X (diff + codebase) e a variável de relevância Y (issues que reviewers humanos flagrariam), a representação ótima X̃ minimiza I(X̃;X) preservando I(X̃;Y). Attention dilution é a falha deste processo quando |X| excede a capacidade efetiva do LLM. RAG para code review é um algoritmo IB-aproximado — e existe um β-ótimo que maximiza I(X̃;Y)/I(X̃;X), empiricamente próximo de 2K tokens estruturados no dataset de Kumar 2026.

## Conteúdo

### O que attention-dilution-llm-context contribui

No dataset SWE-PRBench (Kumar 2026, 350 PRs), todos os 8 modelos frontier degradam monotonicamente de config_A (diff only) para config_C (full context com AST, import graphs, execution context). O mecanismo hipotético é colapso de Type2_Contextual issues — o tipo que requer compreensão de impacto arquitetural e comportamento esperado, não apenas sintaxe local. Um prompt estruturado de 2.000 tokens supera um prompt de 2.500 tokens com contexto completo: volume sem estrutura degrada, estrutura sem volume preserva sinal.

### O que information-bottleneck contribui

O IB (Tishby et al.) minimiza o funcional `L[p(x̃|x)] = I(X̃;X) − β·I(X̃;Y)`, onde β controla o tradeoff entre compressão e relevância. A medida de distorção não é assumida — emerge da solução como `d(x,x̃) = D_KL[p(y|x) || p(y|x̃)]`. Para β=0: compressão máxima, relevância zero. Para β→∞: contexto completo, atenção diluída. O ponto ótimo na β-curve maximiza informação sobre Y por bit de X̃.

### O que emerge da combinação

(⚠️ nossa interpretação) Attention dilution é movimento para o regime errado na β-curve do IB: β→∞ tenta processar todo o contexto X, mas o LLM não tem capacidade para fazê-lo sem perder sinal. A solução empírica de "prompt estruturado de 2K tokens" é uma aproximação manual do ponto β-ótimo — o menor X̃ que preserva I(X̃;Y) acima de um threshold para code review.

(⚠️ nossa interpretação) RAG para code review (RovoDev, LAURA) implementa IB implicitamente: a embedding similarity usada para recuperar contexto é uma aproximação de `D_KL[p(y|x) || p(y|x̃)]` — a distorção que emerge do IB sem ser assumida. Selecionar top-k passagens ≈ encontrar X̃ que minimiza I(X̃;X) sujeito a I(X̃;Y) > θ. A degradação após k* passagens (documentada em ICLR 2025, "Long-Context LLMs Meet RAG") confirma: existe um k* que é o ponto IB-ótimo para code review, acima do qual I(X̃;X) cresce sem ganho em I(X̃;Y).

## Especulação

- Um context selector treinado explicitamente para maximizar I(X̃;Y) via IB deveria superar tanto diff-only quanto RAG-heurístico
- O β-ótimo varia por tipo de PR (refactoring vs. security fix vs. architecture change) — diferentes "relevâncias Y" exigem diferentes pontos na β-curve
- Modelos maiores com maior capacidade efetiva de atenção têm β-ótimo mais alto (podem processar mais contexto antes de degradar)

## Verificação adversarial

**Pergunta falsificável:** Um context selector que maximiza explicitamente I(X̃;Y) (aprendendo p(y|x) de dados de review humanos) deve superar a heurística de 2K tokens estruturados em detecção de Type2_Contextual issues no benchmark SWE-PRBench.

**Evidência que confirmaria:** Sistema IB-explícito atinge > 31% de detecção de issues humanos com < 2K tokens médios por PR.

**Evidência que refutaria:** A heurística de 2K tokens estruturados já está próxima do IB-ótimo — adições incrementais de estruturação não melhoram detecção. Alternativa: a noção de "relevância Y" para code review é subjetiva demais para IB convergir.

## Conexões

- emerge-de: [[attention-dilution-llm-context]] ON "colapso de I(X̃;Y) quando |X| excede capacidade efetiva"
- emerge-de: [[information-bottleneck]] ON "L[p(x̃|x)] = I(X̃;X) − β·I(X̃;Y) como princípio de compressão ótima"
- partOf: [[llm-automated-code-review]] — explica por que RAG funciona melhor que dump de contexto
- implica-em: [[attention-dilution-llm-context]] — β-ótimo como design target para context selection

## Fontes

- [[attention-dilution-llm-context]] — evidência empírica de degradação e achado 2K > 2.5K
- [[information-bottleneck]] — princípio variacional e β-curve como framework
- [Log /ask 2026-04-23](../../outputs/logs/sessions/2026-04-23/ask-emerge-pairs.md) — sessão que confirmou a conexão

> ⚠️ QUARENTENA: artigo emergido de /ask cross-domain. Critérios pendentes: tempo (24h), review frio, adversarial.
