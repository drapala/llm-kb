# llm-kb

LLMs confirmam melhor do que descobrem. Um KB operado por LLM sem intervenção humana converge semanticamente em ~30 dias: artigos homogeneizam, erros cristalizam por validação circular, nuance some. O sistema parece saudável em todas as métricas automáticas. A qualidade erode nos claims, não nos arquivos.

Este KB foi construído para tornar essa degradação visível — e estruturalmente difícil de esconder.

---

## O que é

Fontes brutas entram em `raw/`. Um agente LLM compila artigos interligados em `wiki/`. `/ask` responde com retrieval em 3 camadas e citação de fonte verificável.

```
raw/ (imutável) → /ingest → wiki/ → /ask → outputs/
```

O padrão foi descrito por praticantes em 2026 (Karpathy, Elvis). Evidência de qualidade em escala é limitada a relatos anedóticos. Riscos documentados: conteúdo revisado por LLM piora performance de RAG ([Wikipedia study](wiki/concepts/autonomous-kb-failure-modes.md)); autoconsumo recursivo destrói diversidade ([Model Collapse, Nature 2024](wiki/concepts/autonomous-kb-failure-modes.md)).

---

## O que é diferente

A maioria dos PKMs com LLM resolve o problema de manutenção. Este resolve também o problema epistêmico — que é diferente e mais difícil.

**Proveniência de claims.** Cada afirmação no wiki é rastreável a um arquivo em `raw/`. Sínteses cross-paper são marcadas explicitamente como `[interpretação]`. Quando você lê um artigo seis meses depois, sabe o que vem de fonte e o que vem do compilador.

**Quarentena na criação.** Artigos especulativos começam isolados — não podem ser linkados até critérios de promoção serem satisfeitos: 24h de resfriamento, review em sessão diferente, validação adversarial ou predição falsificável. Inspirado em Janis (1972): "second-chance meeting antes de cristalizar no grafo."

**Cota adversarial.** 1 em 5 fontes ingeridas deve desafiar os claims existentes, não confirmá-los. O viés de curadoria opera em 3 camadas (seleção, interpretação, avaliação) — a cota é estrutural, não opcional.

**Provenance tracking.** Cada artigo é classificado como `source` (resume 1 fonte), `synthesis` (combina 2+ fontes), ou `emergence` (propõe conceito ausente em qualquer fonte individual). Artigos `emergence` são o output genuíno do sistema como ferramenta de pensamento — não compilação.

---

## Estado atual

```
91 fontes  |  53 artigos  |  6 em quarentena
provenance: 28 source · 11 synthesis · 13 emergence
stance:     29% challenging  (threshold mínimo: 20%)
Bradford Zone3/Zone2: 1.05  (pausa de ingestão lateral)
```

**13 artigos com `provenance: emergence`** (25%). Esses artigos não existem em nenhuma fonte — emergiram de conexões cross-domain descobertas via `/ask`. É o número que mede o que o sistema produziu além de compilar.

O inventário completo está em [`outputs/reports/emergence-inventory.md`](outputs/reports/emergence-inventory.md).

---

## Pipeline

```
/ingest   → processa raw/, cria/atualiza artigos wiki
/ask      → retrieval 3 camadas + Q&A com citação verificável
/challenge → avaliação adversarial de claims de um artigo
/promote  → move artigo de quarentena para o grafo
/emerge   → mapeia conexões latentes cross-cluster
/synthesize → cria artigo emergence a partir de /ask confirmado
/draft-post → rascunho de post com check anti-paramétrico
/lint-epistemic → audita saúde epistêmica (stance ratio, quarantine rate, hub health)
/self-report → snapshot estrutural do sistema via frontmatter e logs
```

Coordenação entre commands via [`outputs/state/kb-state.yaml`](outputs/state/kb-state.yaml) — cada command deixa sinais para o próximo sem comunicação direta (stigmergy).

---

## O que o sistema sabe que não sabe

Artigos em quarentena ativa:

| Artigo | Razão | Bloqueio |
|--------|-------|---------|
| `autonomous-kb-failure-modes` | síntese especulativa | bloqueia migração do cluster meta-kb (15 citações) |
| `reflexion-weighted-knowledge-graphs` | subsumido parcialmente por papers externos? | precisa de /scout |
| `raptor-vs-flat-retrieval` | falta predição L2 formal | critério 3 pendente |
| `epistemic-maintenance` | 3 claims sem fonte | critérios todos pendentes |
| `team-decision-theory` | OCR ~30% degradado | precisa de fonte melhor |
| `kb-architecture-patterns` | 0/26 claims sobreviveram ao /challenge | caso especial — não promovível no estado atual |

---

## Aviso

> **Lei de Ashby:** apenas variedade destrói variedade. V(compilador) < V(domínio) → floor de erro irredutível. Adicionar mais processo (16 passos no `/ingest`, 13 commands, 6 hooks) não aumenta V(regulator). O que aumenta é usar a KB para problemas reais — não refiná-la indefinidamente.

Este KB foi refinado por 2 sessões longas e nunca usado para um problema real. Isso está documentado como falha.

---

## Estrutura de arquivos

```
raw/
  articles/   fontes tipo artigo/blog
  papers/     papers acadêmicos
wiki/
  concepts/   1 artigo = 1 conceito
  _index.md   ponteiros (~150 chars/linha)
  _registry.md registro de fontes com stance e data
outputs/
  state/      kb-state.yaml — sinal de coordenação entre commands
  reports/    relatórios gerados (emergence inventory, lint, scout)
  logs/       log de sessões por command
  inbox/      itens pendentes de revisão humana
.claude/
  commands/   /ingest /ask /challenge /promote /emerge /synthesize ...
  hooks/      session-start (executa checks automáticos ao abrir)
  CLAUDE.md   instruções do agente compilador
```

---

## Uso

```bash
# Adiciona fonte
cp paper.pdf raw/papers/
claude /ingest raw/papers/paper.pdf

# Pergunta
claude /ask "o que a literatura diz sobre catastrophic forgetting em agentes?"

# Auditoria epistêmica
claude /lint-epistemic

# Descobre conexões latentes
claude /emerge
```

O `session-start` hook roda automaticamente ao abrir o projeto e reporta artigos prontos para promoção, inbox pendente, e sinais do kb-state.

---

## Princípios

- `raw/` é imutável — fontes nunca são editadas
- Wiki é hint, não verdade — se contradiz `raw/`, `raw/` vence
- Index é ponteiro — conhecimento vive nos artigos, não no índice
- Se é derivável, não persista
- Síntese sem marca é suposição não documentada
- Artigo que não sobrevive a um `/challenge` não deveria estar no grafo
