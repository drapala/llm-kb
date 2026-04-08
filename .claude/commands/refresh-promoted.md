# /refresh-promoted

Job de manutenção periódica. Varre artigos promovidos impactados,
aplica patches elegíveis e gera relatório de saúde do corpus.

Rodar: mensalmente, ou quando `article-health.yaml` tiver >= 3 artigos
com `freshness_status: impacted | under_review`.

---

## Fase 1 — Triage de patch-queue.yaml

Leia `outputs/state/patch-queue.yaml`. Para cada patch com `status: pending`:

1. Leia o artigo afetado + o artigo trigger
2. Reavalie materialidade (o artigo afetado pode ter mudado desde o patch foi criado)
3. Classifique:
   - **Aplicar** se ainda material e sem contradição
   - **Dismissar** se artigo afetado já incorporou o conteúdo (patch obsoleto)
   - **Escalar** se detectou contradição que não estava marcada

Para cada patch a aplicar:
- Injete `> [!patch]` no artigo (se ainda não foi injetado)
- Marque `status: ready_for_apply` no patch-queue.yaml

---

## Fase 2 — Processar blocos [!patch] nos artigos

Para cada artigo em `article-health.yaml` com `pending_patch_count > 0`:
1. Leia o artigo
2. Para cada bloco `> [!patch]` com `status: pending`:
   a. Incorpore a correção/adição no corpo do artigo
   b. Mova o patch para `resolved_patches:` no frontmatter:
      ```yaml
      resolved_patches:
        - patch_id: patch-YYYY-MM-DD-NNN
          applied_at: YYYY-MM-DD
          impact_type: claim_refinement
          summary: [o que foi incorporado]
          trigger: wiki/concepts/slug.md
      ```
   c. Remova o bloco `> [!patch]` do corpo
3. Atualize `article-health.yaml`:
   - `freshness_status: current`
   - `pending_patch_count: 0`
4. Atualize patch-queue.yaml: `status: applied`

---

## Fase 3 — Reindexar claims dos artigos atualizados

Para cada artigo que recebeu patch nesta sessão:
Regenere `outputs/index/promoted-claims/{slug}.yaml` com as claims atualizadas.

---

## Fase 4 — Relatório de saúde

Salve `outputs/reports/corpus-health-YYYY-MM-DD.md`:

```markdown
# Corpus Health Report — YYYY-MM-DD

## Artigos promovidos: N total
- current: N
- impacted: N
- under_review: N

## Patches aplicados nesta sessão
- [artigo]: [patch_id] — [impact_type] — [1 linha do que mudou]

## Artigos sob revisão por contradição
- [artigo]: [razão] — ação recomendada: /challenge

## Patches dismissados
- [patch_id]: [razão]
```

---

## Atualização de kb-state.yaml

```yaml
last_updated: YYYY-MM-DD
next_actions:
  # remover entradas de patches aplicados
  # adicionar /challenge para artigos under_review não resolvidos
```

---

## Quando NÃO rodar

- Se `article-health.yaml` não tiver artigos com `impacted` ou `under_review` → NO-OP
- Se contexto > 70% → agendar para próxima sessão
