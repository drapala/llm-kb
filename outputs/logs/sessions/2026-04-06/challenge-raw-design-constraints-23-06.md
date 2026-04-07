---
date: 2026-04-06
article: raw-design-constraints
claims_challenged: 3
claims_survived: 1
claims_weakened: 2
claims_invalidated: 0
prior_work_found: 3
verdict: PRECISA_CORREÇÃO
---

# Challenge: raw-design-constraints

**Artigo:** wiki/concepts/raw-design-constraints.md  
**Status:** quarantine: true | pearl_level: L2 | interpretation_confidence: low  
**Chain depth:** 0

---

## Active triggers (pré-challenge)

- `⚠️ quarantine_rate 18% > 15% — priorizar /challenge + /promote` (lint 2026-04-06)

---

## Claims

**CLAIM 1:** "Se /review passa a operar majoritariamente sobre wiki/ em vez de raw/, o mecanismo de regularização desaparece — a função de raw/ é ser o 'dado real' que ancora as sínteses do compilador."

- **Evidência mais fraca:** Cadeia de dois saltos — paper Keisha et al. (2025) → knowledge-collapse-llm.md (marcado ⚠️ em Interpretação naquele artigo) → raw-design-constraints.md (NÃO marcado ⚠️ na seção ## Conteúdo). O claim factual subjacente (25% real data = regularizer) é sólido; a implicação para KB design é inferência analógica.
- **Prior work:** Confirmado indiretamente por arXiv:2410.02825 (Ingest-And-Ground — RAG corrige colapso de LLMs pré-treinados recursivamente) e arXiv:2510.24476 (RAG como método primário de mitigação de alucinação). Nenhum paper estuda diretamente KB curatorial (human-mediated) vs. sintético neste sentido.
- **Cenário de falha:** Em um KB onde /review usa wiki/ mas o revisor humano independentemente valida claims contra conhecimento externo, o mecanismo de colapso descrito por Keisha et al. não se aplica diretamente — Keisha et al. estudam treinamento de gradiente descendente em LLMs, não curadoria humana de artigos wiki. A analogia é válida como heurística de design, não como lei mecanística.
- **Citação raw verificada:** O claim "25% de dados reais = regularizer" é rastreável a `raw/papers/knowledge-collapse-recursive-synthetic-training.md` via knowledge-collapse-llm.md. A implicação para raw/ NÃO tem citação raw direta — é síntese analógica.
- **VEREDICTO: PRECISA REVISÃO** — "Implicação para raw/:" em ## Conteúdo deve ser marcada `(⚠️ nossa interpretação)`.

---

**CLAIM 2:** "Se raw/ acumula predominantemente fontes de um único cluster (ex: AI/ML/agentic systems), /review opera como 'focused learning' — aprende bem um cluster, potencialmente degradando integração com outros."

- **Evidência mais fraca:** McClelland et al. (1995) estudam catastrophic interference em redes neurais com backpropagation. Um KB é um conjunto de arquivos de texto — não há pesos compartilhados nem gradientes. O mecanismo de interferência catastrófica não opera diretamente no KB; operaria no LLM que consome os artigos durante /review ou /ask.
- **Prior work:** Nenhum paper encontrado que conecte especificamente topical diversity de corpora de KB com degradação de integração cross-domain em retrieval. Surveys de RAG (arXiv:2506.00054, arXiv:2503.10677) não abordam este ponto.
- **Cenário de falha:** KB com raw/ exclusivamente de AI/ML mas com fontes primárias de alta qualidade pode continuar respondendo corretamente a perguntas cross-domain por raciocínio — o LLM tem conhecimento paramétrico. A degradação prevista (integração cross-domain reduzida) é plausível mas não demonstrada empiricamente para KBs curatoriais.
- **Citação raw verificada:** O claim "interleaved learning > blocked learning" é rastreável a `raw/papers/mcclelland-1995-complementary-learning-systems.md`. A implicação para raw/ NÃO tem citação raw direta.
- **VEREDICTO: PRECISA REVISÃO** — "Implicação para raw/:" em ## Conteúdo deve ser marcada `(⚠️ nossa interpretação)`.

---

**CLAIM 3:** "O failure mode composto — violar os dois constraints simultaneamente — é o mais perigoso e o menos visível: raw/ acumulando sínteses do mesmo cluster."

- **Evidência mais fraca:** Claim puramente sintético — nenhum paper estuda falha composta de KB design com estes dois parâmetros. Está corretamente marcado `(⚠️ interpretação do compilador)` no artigo.
- **Prior work:** PoisonedRAG (arXiv:2402.07867) estuda ataques externos ao KB — mostra que KB pode degradar silenciosamente por injeção de conteúdo malicioso, o que refina o claim de "invisibilidade" (degradação silenciosa é um padrão documentado).
- **Cenário de falha:** O argumento "mais perigoso e menos visível" assume que as duas degradações são aditivas e os sinais não se amplificam mutuamente. Se as duas violações produzissem sinais de alarme mais fortes em conjunto (falhas mais flagrantes e detectáveis), o claim se inverteria.
- **Citação raw verificada:** Não aplicável — claim corretamente posicionado em seção ⚠️ marcada.
- **VEREDICTO: SÓLIDO** — apropriadamente marcado como interpretação, com cenário de falha documentado na seção `## Verificação adversarial` do próprio artigo.

---

## Verificação estrutural

- [x] `## Interpretação` separada de `## Conteúdo`? **PARCIALMENTE** — artigo usa `## Especulação` (template antigo). Conteúdo e Especulação estão separados, mas template atual usa `## Interpretação`.
- [x] Claims interpretativos na seção certa? **PARCIALMENTE** — duas implicações analógicas estão em `## Conteúdo` sem marcador ⚠️. O parágrafo de síntese na subseção "O que emerge da combinação" SIM está marcado.
- [x] Fontes listam wiki/*.md não raw/ papers? **OBSERVADO** — artigo cita wiki/concepts/ como sources, não raw/papers/. As fontes wiki são rastreáveis aos papers primários. Irônico para artigo sobre source primacy, mas não fatal.

---

## CLASSIFICAÇÃO GERAL: PRECISA CORREÇÃO

**Motivo:** Core insights são válidos e valiosos. Dois paragráfos de "Implicação para raw/:" em ## Conteúdo precisam ser marcados com `(⚠️ nossa interpretação)` — são analogias, não claims factuais das fontes. O artigo já sinaliza `interpretation_confidence: low` no frontmatter, mas o corpo deve ser consistente com isso.

**AÇÃO RECOMENDADA:** Aplicar marcadores ⚠️ nos dois parágrafos de implicação em ## Conteúdo. Não remover conteúdo — apenas explicitar o status epistêmico já declarado no frontmatter.

---

## PRIOR WORK (web search)

1. **Ingest-And-Ground: Dispelling Hallucinations from Continually-Pretrained LLMs with RAG** — [arXiv:2410.02825](https://arxiv.org/abs/2410.02825) — afeta Claim 1 — **REFINA**: RAG grounding é suficiente para mitigar degradação por treinamento sintético recursivo, o que refina (mas não invalida) o claim de source primacy — o mecanismo de correção é ativo, não apenas preventivo.

2. **Mitigating Hallucination in LLMs: Survey on RAG, Reasoning, and Agentic Systems** — [arXiv:2510.24476](https://arxiv.org/abs/2510.24476) — afeta Claim 1 — **CONFIRMA**: RAG (= source primacy ativa) é o método primário de mitigação de alucinação, confirmando a importância de fontes externas vs. sínteses internas.

3. **PoisonedRAG: Knowledge Corruption Attacks to RAG** — [arXiv:2402.07867](https://arxiv.org/abs/2402.07867) — afeta Claim 3 — **REFINA**: degradação silenciosa de KB é documentada em contexto de ataque (injeção de conteúdo). Generaliza o claim de "menos visível" para múltiplos vetores, não apenas auto-contaminação.

**CHAIN CONTROL (SPRT):**
- Chain depth atual: 0
- Nenhum prior work INVALIDA claim central
- Resultado: **CHAIN_IGNORED** — nenhum auto-ingest disparado

---

## Ações disparadas

- `💡 post-challenge hook: critérios 2+3 satisfeitos → /auto-promote raw-design-constraints`
  - quarantine: true ✓
  - verdict ≠ RISCO_ALTO ✓
  - ## Verificação adversarial presente com pearl_level: L2 ✓
- `📥 Queue — Ingest-And-Ground (arXiv:2410.02825)` — REFINA Claim 1. Auto-trigger: false.
