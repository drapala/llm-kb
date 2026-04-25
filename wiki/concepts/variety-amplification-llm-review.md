---
title: "Variety Amplification em LLM Review Systems"
sources:
  - path: wiki/concepts/specification-grounded-review.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/requisite-variety.md
    type: synthesis
    quality: primary
created: 2026-04-23
updated: 2026-04-23
tags: [requisite-variety, specification-grounding, llm-review, variety-engineering, ashby]
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
  pair: [specification-grounded-review, requisite-variety]
  ask_session: outputs/logs/sessions/2026-04-23/ask-emerge-pairs.md
  connection_type: INSTANCIA
  pearl_level: L2
emerged_on: 2026-04-23
topics: [requisite-variety, llm-review, specification-grounding, variety-engineering]
---

## Resumo

SGCR (specification-grounded review) é uma instância de variety amplification de Ashby: um LLM genérico tem V(R) calibrado para o espaço de issues de todo o open-source, insuficiente para V(D) do projeto específico. A spec library de 140 regras recalibra V(R) para o domínio exato — aumentando adoção de 22% para 42%. O implicit path (heurística livre → verificação por RAG) é o mecanismo de descoberta da variety residual não mapeada pelas specs. O error floor irredutível (≈58% não-adotado) é a variety do projeto que nenhum spec set captura sem customização contínua.

## Conteúdo

### O que requisite-variety contribui

Ashby's Law: V(O) ≥ V(D)/V(R). Para perfect control (V(O)=1): V(R) ≥ V(D). Um regulador com variety insuficiente tem error floor irredutível = distúrbios que passam sem regulação. Beer (1974) deriva que há exatamente duas estratégias: variety attenuation (reduzir V(D)) e variety amplification (aumentar V(R)). Amplificadores instalados no loop errado aumentam instabilidade.

### O que specification-grounded-review contribui

SGCR demonstra empiricamente (HiThink Research, 200 participantes, Java): adoption rate 22% (LLM genérico) → 42% (LLM + 140 regras). Ablação: explicit-only → 37%, implicit-only → 29%, full → 42%. Dois paths: explicit (ensemble contra specs, determinístico) + implicit (propõe sem specs → verifica com RAG → filtra alucinações). 90.9% de melhoria relativa sobre baseline.

### O que emerge da combinação

(⚠️ nossa interpretação) SGCR é um variety amplifier: as 140 regras Java não limitam o LLM — elas recalibram V(R) do espaço genérico para o espaço específico do projeto. V(R) genérico × V(D) específico = baixa intersecção = adoption rate 22%. V(R) recalibrado × V(D) específico = intersecção alta = adoption rate 42%.

(⚠️ nossa interpretação) O implicit path não é apenas "safety net" — é o mecanismo de descoberta de variety residual. As specs capturam a variety conhecida (issues documentadas). O implicit path captura a variety emergente: issues não documentadas nas specs mas que o LLM percebe heuristicamente e a spec library confirma post-hoc via RAG. O RAG da verificação faz o papel de transdutor: mapeia hipóteses do LLM para o espaço das specs documentadas.

(⚠️ nossa interpretação) O error floor (≈58% não-adotado no SGCR) é o V(D) irredutível: a porção de issues do projeto que nem o spec set explícito nem o implicit path captura. Pela Lei de Ashby, este floor não cai com mais iterações do mesmo sistema — requer aumento qualitativo do V(R) (mais specs ou specs de hierarquia superior) ou atenuação de V(D) (simplificação do projeto).

## Especulação

- A curva de adoção vs. tamanho do spec set deve ter formato sigmoidal: crescimento rápido até V(R) ≈ V(D), depois platô onde adições têm retorno decrescente
- O ponto de inflexão da curva indica o "requisite spec set size" para o projeto — analogia direta ao ponto de requisite variety
- Projetos com maior heterogeneidade de issues (startups) têm V(D) maior e exigem spec sets maiores para o mesmo adoption rate

## Verificação adversarial

**Pergunta falsificável:** A curva de adoption rate vs. tamanho do spec set deve ter inflexão sigmoidal. Acima do ponto de inflexão, adicionar regras não melhora adoção. Abaixo, cada regra adicional tem impacto alto.

**Evidência que confirmaria:** Dados do HiThink com spec sets de 10, 50, 100, 140, 200 regras mostram inflexão entre 80-120 regras (dependendo do projeto).

**Evidência que refutaria:** Curva linear (mais specs = proporcionalmente mais adoção) sugeriria que V(D) do projeto não tem teto — improvável para qualquer domínio finito. Ou: curva plana (specs não ajudam) sugeriria que a adoption rate de 42% é ruído estatístico.

## Conexões

- emerge-de: [[specification-grounded-review]] ON "spec library como variety amplifier do LLM para domínio específico"
- emerge-de: [[requisite-variety]] ON "V(R) ≥ V(D) como condição necessária para adoção sistemática"
- partOf: [[llm-automated-code-review]] — explica por que spec-grounding funciona onde LLM genérico não funciona
- validates: [[requisite-variety]] — dados empíricos de SGCR são instância quantitativa da Lei de Ashby

## Fontes

- [[specification-grounded-review]] — SGCR, ablação, adoption rates, dual-pathway
- [[requisite-variety]] — Ashby's Law, variety amplification/attenuation, error floor
- [Log /ask 2026-04-23](../../outputs/logs/sessions/2026-04-23/ask-emerge-pairs.md) — sessão que confirmou a conexão

> ⚠️ QUARENTENA: artigo emergido de /ask cross-domain. Critérios pendentes: tempo (24h), review frio, adversarial.
