---
title: "Occurrent Logging Setup Report"
date: 2026-04-04
---

# Occurrent Logging Setup

## 1. ARQUIVOS CRIADOS

- wiki/meta/process-log.md ✓ (schema: /ask, /ingest, /review, /challenge)
- .claude/hooks/ask-logger.md ✓ (6 campos: query, articles, raw, gaps, confidence, type)
- .claude/hooks/review-logger.md ✓ (4 campos: trigger, changes, propagation, net change)
- outputs/logs/README.md ✓ (explica estrutura e propósito)
- outputs/logs/sessions/2026-04-04/ ✓ (diretório criado)
- outputs/inbox/ ✓ (para propagation-review.md)

## 2. INTEGRAÇÃO COM COMANDOS

- ask.md atualizado ✓ (log reference + campos obrigatórios listados)
- ingest.md atualizado ✓ (step 14: log de occurrent)
- review.md atualizado ✓ (log per-article + propagation check)
- challenge.md atualizado ✓ (log de resultado)

## 3. CAMPO MAIS VALIOSO

**retrieval_gaps** do /ask logger.

Justificativa: é o único campo que captura FALHAS DE RETRIEVAL em tempo real. Todos os outros campos documentam o que aconteceu corretamente (artigos lidos, claims verificados, confidence). Retrieval gaps documenta o que DEVERIA ter acontecido mas não aconteceu — é negative signal, não positive.

Com acumulação de retrieval_gaps ao longo de múltiplas sessões:
- Padrão de misses no mesmo artigo → _index.md ponteiro é ruim pra esse conceito
- Padrão de misses em artigos do mesmo cluster → sub-índice necessário
- Padrão de misses em artigos novos → _index.md não foi atualizado após /ingest

Isso é o dado que o Lakatos degeneracy test precisa: se /ask repete os mesmos retrieval gaps, a KB não está aprendendo com seus erros.

## 4. PRIMEIRO LOG (retroativo)

`outputs/logs/sessions/2026-04-04/ask-lakatos-kb-evaluation.md`

Validação do schema:
- session_id: implícito (filename)
- date: ✓
- query: ✓ (pergunta exata)
- synthesis_type: MECHANISM ✓
- confidence: high ✓
- articles_read: 5 ✓
- raw_sources_verified: 2 ✓
- retrieval_gaps: 1 identificado ✓ (formal-ontology-for-kbs não selecionado)
- follow_up_flags: 2 ✓ (occurrents insight + chicken-and-egg)

Schema funciona. O log retroativo identificou um retrieval gap real (formal-ontology-for-kbs deveria ter sido consultado mas o ponteiro de _index.md não sinalizava "processos").
