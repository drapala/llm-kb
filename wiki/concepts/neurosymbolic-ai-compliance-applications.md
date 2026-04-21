---
title: "Neurosymbolic AI para Compliance e Uncertainty Quantification"
sources:
  - path: raw/articles/ajithp-2024-neurosymbolic-compliance.md
    type: article
    quality: secondary
    stance: confirming
  - path: raw/papers/arabian-2025-neurosymbolic-robustness-uq-stub.md
    type: paper
    quality: secondary
    stance: confirming
  - path: raw/papers/fang-2024-llms-neurosymbolic-reasoners.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-11
updated: 2026-04-11
tags: [neurosymbolic, compliance, uncertainty-quantification, fuzzy-logic, probabilistic-logic, LLMs, knowledge-graphs]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
status: quarantined
quarantine_date: 2026-04-11
quarantine_reason: "Gate 3 invalidou: (1) confidence scores como UQ 'calibrado' — scores heurísticos de proveniência não são UQ calibrado (OpenAI); (2) módulo simbólico como 'apenas tornar explícito' LLM — mechanistic fallacy, módulos determinísticos adicionam capacidade genuinamente nova (Gemini). Fixes aplicados: (1) 'calibrado' → 'proxy de UQ'; (2) argumento Fang qualificado com contra-argumento; auditabilidade full-pipeline qualificada; fuzzy logic vs epistemic uncertainty distinguida."
synthesis_sources:
  - raw/articles/ajithp-2024-neurosymbolic-compliance.md
  - raw/papers/arabian-2025-neurosymbolic-robustness-uq-stub.md
  - raw/papers/fang-2024-llms-neurosymbolic-reasoners.md
---

## Resumo
Três fontes convergem no design de sistemas neurossimbólicos para domínios que requerem raciocínio sobre regras explícitas: Ajithp (2024) descreve o padrão "neural flagga, simbólico decide" para compliance; Arabian Journal (2025) documenta uncertainty quantification via propagação de incerteza neural através de regras lógicas; Fang et al. (AAAI 2024) argumenta que LLMs já fazem raciocínio neurossimbólico implicitamente, com 88% de performance em benchmarks simbólicos.

## Conteúdo

### O Padrão Neurossimbólico para Compliance (Ajithp 2024)

**Arquitetura de dois estágios:**

```
[Dados] → [Componente Neural] → [Flags/Scores] → [Reasoner Simbólico] → [Veredicto de Compliance]
```

**Estágio 1 — Componente Neural:**
- Detecta padrões estatisticamente incomuns (anomaly detection)
- Gera risk scores numéricos
- Captura padrões que regras explícitas não cobrem

**Estágio 2 — Reasoner Simbólico:**
- Recebe flags/scores do componente neural
- Cruza com base de regras de compliance
- Produz veredicto: compliant | non-compliant | requires_review

**Exemplo descrito:**
> Uma regra lógica como "toda transação acima de $10k deve ser reportada *a menos que* critérios X, Y, Z sejam atendidos." O componente neural detecta a transação; o reasoner verifica se os critérios de exceção são válidos.

**Vantagem vs. puramente neural:** a camada simbólica do veredicto é auditável — "não-compliant por violação da regra R3, cláusula C2" é rastreável. Caveat: auditabilidade full-pipeline depende de interpretabilidade do componente neural upstream; o score de anomalia que gerou o flag pode não ser explicável.

**Vantagem vs. puramente simbólico:** regras não capturam tudo. Componente neural flagga padrões emergentes que as regras existentes não cobrem.

### Uncertainty Quantification via Camada Simbólica (Arabian Journal 2025)

Knowledge graphs podem conter fatos com **graus de certeza** — não apenas verdadeiro/falso:
- Arestas ponderadas com score de confiança
- Assertions com proveniência que afeta credibilidade

**Propagação de incerteza:**
A incerteza gerada pelo componente neural (probabilidade de classificação, score de anomalia) propaga-se através das regras lógicas via dois mecanismos. Nota: outputs de redes neurais (softmax, anomaly scores) são frequentemente não-calibrados — propagá-los não garante outputs calibrados sem etapas de calibração explícitas (e.g., temperature scaling).

**Lógica fuzzy:** verdade como valor em [0,1]
- Regra "Se A (0.8) E B (0.7), então C" → C tem confiança = f(0.8, 0.7)
- Permite raciocínio sobre fatos parcialmente verdadeiros (grau de verdade / vagueness)
- Útil em dados ruidosos; nota: fuzzy logic modela vagueness/parcialidade, não incerteza epistêmica probabilística — a distinção é tecnicamente importante

**Lógica probabilística:** probabilidades como cidadãos de primeira classe
- Cada fato tem probabilidade associada
- Inferência propaga distribuições de probabilidade, não apenas verdades binárias

**Confidence scores como proxy de UQ:**
Sistemas que usam scores de confiança diferenciados por fonte (1.0 para fonte oficial, 0.85 para derivado, 0.8 para opinião) propagam esses pesos via camada simbólica. Caveat: scores heurísticos de proveniência não são UQ calibrado — calibração requer validação empírica contra outcomes observados. O que esses sistemas fazem é UQ proxy, não UQ calibrado.

### LLMs como Reasoners Neurossimbólicos Implícitos (Fang et al. AAAI 2024)

**Argumento central:** LLMs já fazem raciocínio neurossimbólico sem que isso seja design explícito. O pre-training em linguagem natural que codifica lógica, regras, e inferências faz o LLM aprender esses padrões implicitamente.

**Evidência empírica (arXiv 2401.09334):**
- ~88% de performance em benchmarks de raciocínio simbólico (matemático, navegação, sorting, common-sense)
- LLM + módulo simbólico explícito melhora substancialmente vs. LLM puro

**Implicação de design (argumento de Fang):**
Fang argumenta que adicionar um módulo simbólico a um LLM explicita raciocínio que o LLM já faz implicitamente. Contra-argumento: módulos simbólicos (SAT solvers, intérpretes lógicos) fornecem computação deterministicamente correta que difere fundamentalmente da geração probabilística de tokens — podem adicionar capacidade genuinamente nova. A interpretação mais defensável é que o módulo simbólico tanto explicita quanto estende as capacidades do LLM.

**Limitação importante:** os 88% foram obtidos em text-based games — ambiente artificial. Generalização para sistemas de produção com regras complexas e dados reais não está demonstrada.

### Convergência dos Três Patterns

| Dimensão | Componente Neural | Componente Simbólico | Output |
|----------|-----------------|---------------------|--------|
| Compliance | Detecta padrões, flags anomalias | Regras de compliance, exceções | Veredicto auditável |
| UQ | Score de confiança por predição | Propagação via lógica fuzzy/probabilística | Output com incerteza calibrada |
| LLMs + NeSy | Raciocínio implícito em linguagem | Módulo simbólico explicitado | Raciocínio verificável |

## Interpretação

(⚠️ Síntese interpretativa — não está em nenhuma fonte individual.)

O padrão neurossimbólico para compliance endereça precisamente o gap identificado em [[ai-generated-code-debt-empirical]] na dimensão de security: se o componente neural (LLM) gera código sem enforcement simbólico explícito, ele produz sistemas que chegam à produção sem verificação de regras. A arquitetura "neural flagga, simbólico decide" é o padrão de enforcement que evitaria isso.

Confidence scores diferenciados por fonte (valores típicos: 1.0 oficial, 0.85 derivado, 0.8 opinião) são uma implementação de uncertainty quantification — a camada simbólica do sistema propaga esses scores como lógica fuzzy.

## Verificação adversarial

**Claims mais fracos:** (1) Ajithp 2024 é blog post (STUB) — não peer-reviewed; (2) Arabian Journal 2025 é STUB não verificado independentemente; (3) Fang et al. 88% é em text-based games — benchmark artificial, não sistemas de produção.

**O que os papers não dizem:** (1) Ajithp não quantifica melhoria de recall/precision vs. puramente simbólico; (2) Arabian Journal não avalia qual mecanismo (fuzzy vs. probabilístico) é mais adequado para quais domínios; (3) Fang não demonstra que o "módulo simbólico" é o que produz melhoria vs. apenas melhor prompting.

## Quality Gate
- [x] Wikilinks tipados: [[ai-generated-code-debt-empirical]] em Interpretação, marcado como ⚠️
- [x] Instance→class: 88% qualificado com Fang 2024, text-based games; confidence scores como exemplo típico, não número específico
- [x] Meta-KB separado: conexão com code debt isolada na Interpretação com marcação
- [x] Resumo calibrado: inclui que Ajithp e Arabian são STUB e 88% é benchmark artificial

## Conexões
- neurosymbolic-ai-knowledge-graphs partOf neurosymbolic-ai-compliance-applications (taxonomia base para aplicação em compliance)

## Fontes
- [Ajithp 2024](../../raw/articles/ajithp-2024-neurosymbolic-compliance.md) — padrão "neural flagga, simbólico decide", compliance flow (STUB)
- [Arabian Journal 2025](../../raw/papers/arabian-2025-neurosymbolic-robustness-uq-stub.md) — UQ via fuzzy/probabilistic logic, confidence scores (STUB)
- [Fang et al. AAAI 2024](../../raw/papers/fang-2024-llms-neurosymbolic-reasoners.md) — LLMs como NeSy implícitos, 88% benchmark simbólico
