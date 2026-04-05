---
updated: 2026-04-05
version: 1.0
---

# System Map

Estado operacional atual da KB. Atualizado manualmente após mudanças de workflow promovidas.
Não é aspiracional — descreve como a KB funciona hoje, não como deveria funcionar.

## Comandos ativos e quando são usados

| Comando | Gatilho | Frequência real |
|---------|---------|-----------------|
| `/ingest` | Fontes novas em raw/ | Por sessão |
| `/ask` | Pergunta sobre domínio | Por sessão |
| `/review [artigo]` | Artigo desatualizado ou suspeito | Semanal |
| `/challenge [artigo]` | Antes de publicar síntese | Antes de cada /draft-post |
| `/promote [artigo]` | Critérios de quarentena satisfeitos | Conforme necessário |
| `/scout` | Após 10+ ingestões | Mensal |
| `/emerge` | Após 3+ promoções | Mensal |
| `/dream` | Final de sessão produtiva | Por sessão quando relevante |
| `/lint-epistemic` | Manutenção geral | Mensal |
| `/friction` | Evento de atrito observado | Sempre que ocorrer |
| `/retro` | 10+ friction events acumulados | Mensal |

## Fluxo principal

```
raw/  →  /ingest  →  wiki/concepts/  →  /ask
                          ↓
                   /challenge (antes de publicar)
                          ↓
              quarentena  →  /promote  →  wiki ativo
```

## Estado de coordenação

`outputs/state/kb-state.yaml` coordena entre sessões via triggers.
Disciplina atual: manual — comandos atualizam o estado ao final de cada execução.

## Pontos de intervenção manual conhecidos

- `kb-state.yaml` requer edição manual após promoções e ingestões
- Cluster list em `/emerge` requer atualização manual conforme a KB cresce
- Friction events requerem captura ativa do operador (não são automáticos)

## Meta-camada (V1 — ativa)

```
raw/meta/ops/  →  /friction  →  /retro  →  wiki/meta/friction-log.md
raw/meta/ux/   ↗
```

V2 (não implementada ainda): `/propose` → `wiki/meta/hypotheses/`
V3 (não implementada ainda): `/promote-change` → `wiki/meta/promoted-changes/`
