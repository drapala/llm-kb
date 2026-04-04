# Utility Tracker Hook

## Quando ativa

Ao final de TODA sessão /ask, depois do ask-logger. Roda JUNTO com o ask-logger — não em vez dele.

## O que faz

### Passo 1 — Incrementa reads

Para cada artigo listado em `articles_read` do ask-logger:
- Abra o arquivo wiki/
- Incremente `reads: +1`
- Atualize `last_read: [data da sessão]`

### Passo 2 — Incrementa retrievals_correct

**Se confidence = HIGH:**
- Para cada artigo em articles_read: incremente `retrievals_correct: +1`

**Se confidence = MEDIUM:**
- Para cada artigo que teve claim verificado em raw/: incremente `retrievals_correct: +1`
- Outros artigos lidos mas não verificados: não incrementa

**Se confidence = LOW:**
- Não incrementa `retrievals_correct` em nenhum artigo

### Passo 3 — Incrementa retrievals_gap

Para cada artigo listado em `retrieval_gaps` do ask-logger:
- Abra o arquivo wiki/
- Incremente `retrievals_gap: +1`

NOTA: retrieval_gap incrementa artigos que DEVERIAM ter sido lidos mas não foram. É negative signal — artigo existia mas o retrieval não chegou até ele.

### Passo 4 — Não calcule utility_score

`utility_score = retrievals_correct / reads`

Este cálculo é feito on-demand pelo /scout ou /review. Não armazene — evita drift do número ao longo do tempo.

## Exemplo de execução

Sessão /ask com:
- articles_read: [agent-memory-architectures, self-improving-agents]
- confidence: HIGH
- retrieval_gaps: [formal-ontology-for-kbs]

Resultado:
- agent-memory-architectures: reads 0→1, retrievals_correct 0→1, last_read: 2026-04-04
- self-improving-agents: reads 0→1, retrievals_correct 0→1, last_read: 2026-04-04
- formal-ontology-for-kbs: retrievals_gap 0→1
