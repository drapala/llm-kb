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

## Fase 3 — Regeneração pós-patch

Para cada artigo que recebeu patch nesta sessão, execute em sequência:

**3a — Reindexar claims:**
Regenere `outputs/index/promoted-claims/{slug}.yaml` com as claims atualizadas.
```
python scripts/build-claim-indexes.py --slug <slug> --all
```

**3b — Reconciliar depends_on:**
Verifique se o artigo incorporou nova fonte (trigger do patch).
- Se o patch adicionou evidência de novo raw/ ou wiki/ → adicione à lista `depends_on` em `article-health.yaml`
- Se o patch marcou claim como obsoleta por antiga fonte → remova essa fonte de `depends_on`
- Regra: `depends_on` deve refletir o estado atual do artigo, não o histórico de patches

**3c — Atualizar topics se necessário:**
Se o patch expandiu o escopo temático do artigo, adicione novos topics em `article-health.yaml`.
Topics desatualizados afetam o impact analyzer do /ingest — manter correto é crítico.

---

## Fase 4 — Relatório de saúde + métricas operacionais

Execute o script de métricas e salve resultado:
```
python scripts/patch-metrics.py --save
```

Isso atualiza `outputs/state/patch-metrics.yaml` com:
- `patch_precision_estimate` — ratio applied / (applied + dismissed)
- `under_review_count` — artigos com contradição ativa
- `mean_time_to_resolution_days` — velocidade média de resolução
- `articles_with_repeated_impact` — artigos instáveis (2+ patches)
- `top_sources_of_contradiction` — quais ingestas mais geram contradições
- `high_churn_articles` — artigos com flags de risco ativo

Salve também `outputs/reports/corpus-health-YYYY-MM-DD.md`:

```markdown
# Corpus Health Report — YYYY-MM-DD

## Artigos promovidos: N total
- current: N
- impacted: N
- under_review: N

## Métricas operacionais
- patch_precision: X% (N aplicados, N dismissados)
- mean_time_to_resolution: N dias
- artigos instáveis (2+ patches): [lista ou "nenhum"]

## Patches aplicados nesta sessão
- [artigo]: [patch_id] — [impact_type] — [1 linha do que mudou]

## Artigos sob revisão por contradição
- [artigo]: [razão] — ação recomendada: /challenge

## Patches dismissados
- [patch_id]: [razão]
```

**Sinal de alerta:** Se `patch_precision_estimate < 0.6`, o impact analyzer pode estar gerando patches demais por overlap superficial — considerar elevar threshold de 0.45 para 0.55.

---

## Atualização de kb-state.yaml

```yaml
last_updated: YYYY-MM-DD
next_actions:
  # remover entradas de patches aplicados
  # adicionar /challenge para artigos under_review não resolvidos
```

---

## Fase 5 — Resolução de artigos under_review

Para artigos com `freshness_status: under_review` (contradição detectada):
1. **Não processe** via fases 1-3 — patches escalated requerem julgamento editorial
2. Rode `/challenge [artigo]` para avaliar se a contradição invalida o artigo
3. Após /challenge:
   - Se artigo **weakened mas válido** → incorpore qualificação, set `freshness_status: current`, `epistemic_risk: null`
   - Se artigo **invalidado** → marque para depromote, não processe patches
4. Atualize patch escalado: `status: resolved | dismissed`

---

## Quando NÃO rodar

- Se `article-health.yaml` não tiver artigos com `impacted` ou `under_review` → NO-OP
- Se contexto > 70% → agendar para próxima sessão
