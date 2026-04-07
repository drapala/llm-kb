---
title: "Single Brain — Phase 1 Design"
sources:
  - path: raw/papers/yu-2026-multi-agent-memory-architecture.md
    type: paper
    quality: primary
    stance: neutral
  - path: raw/papers/rezazadeh-2025-collaborative-memory-access-control.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-05
updated: 2026-04-05
tags: [single-brain, world-model, design, lancedb, phase1, multi-agent]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
provenance: emergence
emergence_trigger:
  pair: [single-brain-data-ontology, multi-agent-memory-consistency]
  ask_session: outputs/logs/sessions/2026-04-05/ask-12-34.md
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-05
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-05
quarantine: true
quarantine_created: 2026-04-05
quarantine_reason: "artigo de design emergido — decisões arquiteturais precisam de 24h + review frio"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: "L2 predição: 4 namespaces Hindsight vs. flat index reduz conflitos de schema durante migração Phase 1→3"
---

## Resumo

Síntese de design para Phase 1 do Single Brain baseada em três artigos ingeridos em 2026-04-05. Decisões desbloqueadas: schema LanceDB com 4 namespaces (Hindsight), provenance desde Dia 1, coexistência gradual com grep/markdown. Caveat crítico: João é o único "agente" agora por limitação de sistema (Claude Code session-based), mas o plano é múltiplos agentes especializados em paralelo (Phase 3). O design de Phase 1 deve ser multi-agent-ready sem implementar complexidade desnecessária.

## Conteúdo

### Contexto: o que "agente único" significa agora

**Situação atual (Phase 1):** João opera como agente único via Claude Code em sessões sequenciais. Não há concorrência — cada sessão é linear, sem escrita paralela no world model.

**Situação planejada (Phase 3):** múltiplos agentes especializados operando em paralelo, cada um com função específica (ex: agente KB, agente Zelox, agente carreira, agente PP, agente AG). Esses agentes escreverão no world model concorrentemente.

**Implicação de design:** Phase 1 pode usar arquitetura simples (sem protocolo de consistência) porque não há concorrência. Mas o schema de dados deve ser multi-agent-ready desde o início — retrofit de provenance e namespaces em Phase 3 é custoso.

### Schema LanceDB — 4 namespaces Hindsight

Baseado em [[single-brain-data-ontology]] (⚠️ quarantined):

```
LanceDB (embedded, local)
├── world/        ← fatos externos verificáveis
│     wiki promovidos, PNCP contratos, dados de mercado
│     update: append-only + expiry (bi-temporal)
│     writer: somente fontes externas verificadas
│
├── experience/   ← log imutável de ações do sistema
│     sessões Claude Code, ingest logs, outputs de ferramentas
│     update: append-only, nunca modificado
│     writer: somente o agente que executou a ação
│
├── opinion/      ← claims com confiança c∈[0,1]
│     artigos em quarentena, hipóteses emergidas, risk scores Zelox
│     update: confidence decay + update por nova evidência
│     writer: qualquer agente, com provenance obrigatória
│
└── observation/  ← sínteses compiladas
      artigos wiki promovidos, relatórios consolidados
      update: rebuild periódico (derivado das outras redes)
      writer: processo de consolidação (/dream, /promote)
```

**Por que 4 namespaces e não flat?**

Sem separação, agente de Zelox (escreve opinion/risk scores) contamina o mesmo espaço que agente de KB (lê observation/fatos). Em Phase 3 com múltiplos agentes paralelos, isso é authority bias cascade em nível de DB — o failure mode mais silencioso de [[autonomous-kb-failure-modes]] escalado para infraestrutura.

### Provenance desde Dia 1

Baseado em [[collaborative-memory-access-control]]: fragmentos sem provenance não podem ser auditados ou filtrados por permissão depois.

Schema mínimo por fragmento em Phase 1:

```python
fragment = {
    "id": "sha256(content + source_path)",  # ID estável para updates incrementais
    "content": "...",
    "embedding": [...],
    "network": "world | experience | opinion | observation",
    "provenance": {
        "created": "2026-04-05",
        "source": "wiki/concepts/agent-memory-architectures.md",
        "agent": "claude-code-session",  # Phase 3: nome do agente específico
        "session": "YYYY-MM-DD/HH-MM"
    }
}
```

**Custo em Phase 1:** zero — apenas campos adicionais no schema.
**Custo de retrofit em Phase 3 sem isso:** reconstruir todo o índice + perder rastreabilidade histórica.

### Coexistência com grep/markdown (transição gradual)

Phase 1 não substitui o sistema atual — adiciona LanceDB como camada paralela.

```
/ask atual:
  Layer 1: _index.md (grep) → artigos candidatos
  Layer 2: wiki/concepts/*.md (leitura direta)
  Layer 3: raw/ (verificação pontual)

/ask com LanceDB (Phase 1+):
  Layer 0: LanceDB semantic search → candidatos por similaridade
  Layer 1: _index.md (grep) → refinamento por keywords
  Layer 2: wiki/concepts/*.md (leitura direta)
  Layer 3: raw/ (verificação pontual)
```

LanceDB adiciona Layer 0, não substitui as outras. Migração completa só quando o índice tiver acurácia validada empiricamente (teste: /ask com e sem Layer 0, mede recall).

### Bloqueios restantes

**Bloqueio 1 — Chunking do Obsidian vault** ✅ RESOLVIDO
`MarkdownNodeParser` (LlamaIndex) parseia markdown raw splitando por headers e preservando hierarquia. Para hierarquia pai/filho: `HierarchicalNodeParser`. Metadados relevantes (`doc_type`, `network`, `provenance`) como metadata filters. Uma linha de código, não problema de pesquisa.

```python
from llama_index.core.node_parser import MarkdownNodeParser
nodes = MarkdownNodeParser().get_nodes_from_documents(documents)
```

**Bloqueio 2 — Atualização incremental do índice** ✅ RESOLVIDO
GraphAnchor (ingerido 2026-04-05) é ephemeral e per-query — não resolve manutenção de índice persistente. Mas a solução é mais simples: ID estável (`sha256(source_path)`) + `delete_by_id` + `reinsert` — nativo no LanceDB. Não é problema de pesquisa, é decisão de implementação. O `id` já está no schema de provenance.

**Bloqueio 3 — Embedding model**
BGE-M3 é correto para PNCP (300M vetores, H100, português jurídico). Para Phase 1 (KB pessoal, ~10k chunks, macOS):
- `text-embedding-3-small` via API: simples, $0.02/1M tokens, sem setup local
- `nomic-embed-text` (768 dims): local via Ollama, zero custo, boa qualidade multilingual
- Decisão: `nomic-embed-text` para Phase 1 (evita dependência de API + alinha com filosofia local-first do Single Brain)

### O que GraphAnchor e HetaRAG desbloqueiam

**GraphAnchor (2601.16462):** não resolve Bloqueio 2 (ephemeral, per-query). Contribuição real: padrão de /ask iterativo com sufficiency judgment — relevante para /ask multi-hop no KB, não para manutenção de índice.

**HetaRAG (2509.21336):** mais relevante para Phase 2+ (multi-modal, múltiplas fontes). Phase 1 é só markdown — pode esperar.

### Predição L2

"Implementar Phase 1 com 4 namespaces Hindsight vs. flat index produzirá menos conflitos de schema durante a migração Phase 1→3 (introdução de múltiplos agentes)." Falsificador: se a migração Phase 1→3 requer o mesmo esforço de retrofit independente do schema inicial, a separação ontológica não teve valor arquitetural.

## Interpretação

Este artigo é design decision, não descrição de sistema existente. As recomendações são derivadas de três papers, mas a aplicação específica ao metaxon/Single Brain é nossa síntese — não validada empiricamente.

O caveat mais importante: Phase 1 pode ser implementada com simplicidade porque João é o único agente agora. Mas toda decisão de schema deve ser testada mentalmente contra o cenário "5 agentes escrevendo simultaneamente no mesmo namespace" — se causa problema nesse cenário, precisa ser redesenhada antes de Phase 1 crystallize.

## Gaps que este artigo deixa abertos

1. Chunking strategy para markdown com wikilinks — empírico, não coberto por papers
2. Cold start protocol — ordem de ingestão dos 83 artigos + vault
3. Benchmark de embedding models para português técnico em escala pequena

## Conexões

- derivedFrom: [[single-brain-data-ontology]] — 4 namespaces Hindsight como schema LanceDB
- derivedFrom: [[multi-agent-memory-consistency]] — "Phase 1 pode ser simples" porque agente único = sem update-time ordering
- derivedFrom: [[collaborative-memory-access-control]] — provenance schema desde Dia 1
- validates: [[complementary-learning-systems]] — LanceDB como hipocampo (ingest rápido); wiki/grep como neocórtex (slow, consolidated)
- blocked_by: [[autonomous-kb-failure-modes]] — promote pendente; authority bias cascade é o failure mode que a separação de namespaces previne

## Fontes

- [Yu et al. 2026](../../raw/papers/yu-2026-multi-agent-memory-architecture.md) — "Phase 1 pode ser simples" porque agente único sem concorrência
- [Rezazadeh et al. 2025](../../raw/papers/rezazadeh-2025-collaborative-memory-access-control.md) — provenance schema mínimo por fragmento

## Quality Gate
- [x] Wikilinks tipados: 5 (derivedFrom ×3, validates, blocked_by)
- [x] Instance→class: recomendações qualificadas como "não validado empiricamente"
- [x] Meta-KB separado: aplicação ao Single Brain em Interpretação
- [x] Resumo calibrado: "síntese de design" explícito, não "decisão arquitetural validada"
