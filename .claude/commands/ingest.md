# /ingest

## Pre-check de contexto

Execute este script bash e leia o resultado:

```bash
SESSION=$(ls -t ~/.claude/projects/-Users-drapala-projects-metaxon/*.jsonl 2>/dev/null | head -1)
python3 -c "
import json
entries = []
try:
    with open('$SESSION') as f:
        for line in f:
            try:
                obj = json.loads(line)
                u = obj.get('message',{}).get('usage',{})
                if u: entries.append(u)
            except: pass
except: pass
if entries:
    u = entries[-1]
    t = u.get('input_tokens',0)+u.get('cache_read_input_tokens',0)+u.get('cache_creation_input_tokens',0)
    print(round(t/200000*100,1))
else:
    print('0')
"
```

Se resultado >= 70%:
  Imprima: `⚠️ Contexto em [N]%. /ingest pode causar auto-compact durante processamento. /dream recomendado primeiro.`
  Não processa automaticamente — aguarda confirmação explícita do usuário.

Se resultado < 70%: silêncio — processa normalmente.

---

## Modo especial: Ontologia Formal

Se a fonte é um paper de ontologia formal (BFO, DOLCE, OWL, Relation Ontology,
ou similar), aplique estas regras EM VEZ do resumo padrão:
- NÃO resuma o paper — extraia primitivos aplicáveis à KB
- Para cada categoria ontológica: dê exemplo de como se aplica a conceitos
  já existentes em wiki/concepts/
- Para cada tipo de relação: mostre como substituiria um wikilink plano existente
- Seção obrigatória: "Perguntas que este framework habilita na KB que antes
  não eram formuláveis"

---

**SPRT chain guard** (verifique antes de processar qualquer fonte):
```bash
yq '.ingest_chain.status' outputs/state/kb-state.yaml
```
- Se `closed` E este ingest é `chain_triggered: true`: **PARE.**
  Reporte: `🚫 SPRT CHAIN CLOSED — chain de ingest encerrada. Este paper deve ser revisado manualmente.`
  Adicione à `ingest_queue_priority` com `auto_trigger: false` e aguarde ingest manual.
- Se `closed` E ingest é manual: reset chain (depth: 0, status: open) e prossiga.
- Se `open`: prossiga normalmente.

---

**Resolução de fonte arxiv** (antes de tudo):
Se a entrada for um arXiv ID (ex: `2401.12345`) ou URL (`https://arxiv.org/abs/XXXX`),
chame `download_paper` (arxiv MCP) para baixar em `raw/papers/` antes de processar.
Se o arquivo já existe em `raw/papers/`: skip do download, prossiga com o arquivo local.

---

Compare raw/ com wiki/_registry.md. Para cada fonte nova:

1. Leia o conteúdo (para PDFs, extraia texto; para imagens, descreva;
   para transcrições de áudio/vídeo, processe o texto transcrito)
2. Identifique conceitos-chave (max 3 por fonte)
3. Para cada conceito:
   - Se artigo existe em wiki/concepts/: ATUALIZE adicionando informação nova
   - Se não existe E o conceito provavelmente será referenciado de outros artigos:
     CRIE seguindo o template (use as heurísticas de granularidade do CLAUDE.md)
   - Se não justifica artigo próprio: mencione como seção em artigo existente mais próximo
4. Classifique a fonte:
   - type: article | paper | repo | note | dataset
   - quality: primary | secondary | tertiary
   - **stance: confirming | challenging | neutral** — a fonte CONFIRMA, DESAFIA,
     ou é NEUTRA em relação às premissas existentes no wiki?

   **Stance auto-classification (P4):** para fontes em inglês com arquivo em raw/,
   execute o classifier como sugestão inicial (requer venv + .env):
   ```bash
   python3 scripts/stance-classify.py --source <path>
   ```
   - Se `needs_human_review: false` e confidence ≥ 0.70: use a stance sugerida
   - Se `needs_human_review: true` ou confidence < 0.70: classifique manualmente
   - O script detecta apenas `challenging_type: content` (contradição direta por dado)
   - Se você identifica conexão analógica/implicação: `stance: challenging, challenging_type: implication`
   - Stance sugerida pode sempre ser overridden: você tem contexto do wiki que o script não tem

   **Quando stance = challenging: defina obrigatoriamente `challenging_type`:**
   - `content` — paper contradiz claim com dado diferente (detectável automaticamente)
   - `implication` — conexão analógica, prática questionável (requer julgamento humano)

4.5. **Bradford hard gate** (imediato após classificar stance):
   Se stance = `challenging`, execute:
   ```bash
   bash scripts/bradford-gate.sh --stance challenging
   ```
   - Exit 0: prossiga normalmente
   - Exit 1: **PARE.** Não crie artigo, não registre no _registry.md.
     Reporte: `🚫 BRADFORD GATE: quota de fontes challenging excedida. Fonte não ingerida.`
     A fonte pode ser salva em `raw/` para ingestão futura, mas não é processada agora.
     Informe qual ratio atual e quanto falta para a quota reabrir.

5. Verifique: algum artigo existente agora tem overlap >60% com outro? Se sim, sugira merge
6. Processe quaisquer blocos > [!patch] encontrados nos artigos tocados
7. Ao criar/atualizar artigos, atribua no frontmatter:
   - **source_quality: high|medium|low** — baseado em fontes:
     high = 2+ fontes primary concordam, medium = 1 primary ou 2+ secondary,
     low = apenas tertiary
   - **interpretation_confidence: high|medium|low** — auto-avaliação da síntese:
     high = claim factual direto das fontes, medium = síntese moderada,
     low = interpretação novel ou cross-paper insight
   - Quando source_quality e interpretation_confidence divergem, flag com ⚠️
     no report pra revisão humana
8. **Adversarial quota:** após processar, conte fontes no _registry.md por stance.
   Se as últimas 5+ fontes são todas "confirming", reporte:
   "⚠️ Adversarial gap: últimas N fontes são confirming. Considere buscar
   fonte challenging. Rode /curate pra discovery automático."
9. **Ingest threshold** (quando wiki > 40 artigos): exigir que fonte nova
   contribua conceito não coberto OU contradiga claim existente.
   Quando wiki > 80 artigos: exigir sub-índices antes de continuar crescendo.
10. **Verificação adversarial** (antes de finalizar cada artigo):
    Para cada artigo criado ou significativamente atualizado, responda:
    a. **Claim mais fraco:** qual afirmação seria mais fácil de refutar?
    b. **O que o paper NÃO diz:** 2-3 coisas que o resumo poderia sugerir
       mas a fonte não afirma
    c. **Simplificações feitas:** onde o artigo perdeu nuance importante?
    d. **Prior work:** a fonte cita trabalhos anteriores no mesmo terreno?
    Salve como seção `## Verificação adversarial` no artigo wiki gerado.
    Se o claim mais fraco é uma ESPECULAÇÃO não marcada, mova pra
    ## Interpretação antes de publicar.
11. **Impact propagation para artigos promovidos** (após verificação adversarial):

    Artigos promovidos são nós dependentes do corpus, não arquivos estáticos.
    Este step detecta impacto material do novo artigo sobre promovidos e gera patches.

    **11a — Identificar candidatos afetados:**
    Leia `outputs/state/article-health.yaml`.
    Para cada artigo promovido com `freshness_status != under_review`:
    - Verifique sobreposição de topics com o novo artigo
    - Verifique se o novo artigo está em `depends_on` de algum promovido (trigger forte)
    - Verifique sobreposição semântica com claims em `outputs/index/promoted-claims/{slug}.yaml` (se existir)

    Candidatos = artigos com qualquer sobreposição de topics OU depends_on match.

    **11b — Score de materialidade por candidato:**
    Para cada candidato, compute score (0–1):
    ```
    score = topical_overlap (0-0.3)
          + claim_overlap (0-0.3)       # novo artigo toca claims existentes?
          + evidence_novelty (0-0.2)    # nova evidência primária onde só havia secundária?
          + contradiction_weight (0-0.1) # novo artigo contradiz alguma claim?
          + depends_on_bonus (0.1)       # trigger forte: novo artigo está em depends_on
    ```
    Thresholds: < 0.45 = skip | 0.45–0.70 = queue (review) | > 0.70 = patch candidate

    **11c — Classificar impact_type para candidatos acima do threshold:**
    - `new_support` — novo suporte para claim já existente
    - `claim_refinement` — claim continua válida mas precisa qualificação ou nuance
    - `claim_contradiction` — novo material enfraquece ou contradiz claim existente
    - `scope_expansion` — artigo promovido estava correto mas incompleto em escopo
    - `bridge_creation` — nova conexão interpretativa importante entre dois blocos
    - `obsolete_framing` — framing central ficou datado

    **11d — Gerar patch candidate e decidir ação (3 saídas explícitas):**

    *Saída 1 — Auto-apply* (score > 0.85 E impact_type ∈ {new_support, claim_refinement, scope_expansion}):
    Injete `> [!patch]` diretamente no artigo afetado:
    ```
    > [!patch]
    > id: patch-YYYY-MM-DD-NNN
    > status: pending
    > trigger: ingest/[slug-do-novo-artigo]
    > impact_type: [tipo]
    > materiality: high
    > affected_claims: [c001, c002, ...]
    > summary: [1-2 frases sobre o que muda]
    > action: [o que o editor deve fazer: incorporar, qualificar, etc.]
    > sources:
    >   - wiki/concepts/[novo-artigo].md
    > created_at: YYYY-MM-DD
    ```

    *Saída 2 — Queue for review* (0.45 ≤ score ≤ 0.85 OU impact_type ∈ {bridge_creation, obsolete_framing}):
    Adicione a `outputs/state/patch-queue.yaml` (não injete no artigo):
    ```yaml
    - patch_id: patch-YYYY-MM-DD-NNN
      article_slug: [slug]
      trigger_slug: [novo-artigo]
      status: pending
      impact_type: [tipo]
      materiality: high|medium
      auto_apply_eligible: false
      summary: [descrição breve]
      created_at: YYYY-MM-DD
    ```
    Adicione entrada em `next_actions` de `kb-state.yaml`:
    `"[patch-id]: review patch em [artigo] (impact: [tipo])"`

    *Saída 3 — Mark under_review* (impact_type = claim_contradiction, qualquer score acima de 0.45):
    Não injete patch no artigo. Atualize diretamente o status do artigo:
    ```yaml
    freshness_status: under_review
    epistemic_risk: high          # novo campo
    pending_patch_count: [N+1]
    last_impact_at: YYYY-MM-DD
    ```
    Adicione a `patch-queue.yaml` com `status: escalated` (não pending):
    ```yaml
    - patch_id: patch-YYYY-MM-DD-NNN
      article_slug: [slug]
      trigger_slug: [novo-artigo]
      status: escalated
      impact_type: claim_contradiction
      materiality: [score]
      auto_apply_eligible: false
      affected_claims: [c001, c002, ...]
      summary: [o que contradiz e como]
      created_at: YYYY-MM-DD
    ```
    Adicione entrada em `next_actions`:
    `"CONTRADIÇÃO: /challenge [artigo] (trigger: [novo-artigo])"`

    **11e — Atualizar article-health.yaml:**
    Para cada artigo que recebeu patch (saídas 1 ou 2):
    ```yaml
    freshness_status: impacted
    pending_patch_count: [N+1]
    last_impact_at: YYYY-MM-DD
    ```
    Para saída 3 (claim_contradiction):
    ```yaml
    freshness_status: under_review
    epistemic_risk: high
    pending_patch_count: [N+1]
    last_impact_at: YYYY-MM-DD
    ```
    Quando contradição for resolvida via /challenge e artigo atualizado:
    `epistemic_risk: null  # ou remover o campo`

    **11f — Salvar relatório:**
    `outputs/reports/impact-[novo-artigo-slug].md` com lista de candidatos,
    scores, decisões (skip/queue/patch) e razões.

    **Regra de omissão:** se nenhum candidato passa 0.45, step 11 é NO-OP silencioso.
    Não crie relatório vazio. Não gaste tokens verificando artigos sem sobreposição.
12. **ONTOLOGICAL QUALITY GATE** (antes de salvar o artigo final):

    **CHECK 1 — WIKILINKS TIPADOS**
    Para cada [[wikilink]] no artigo, substitua por relação tipada:
    `[conceito] [TIPO] [[artigo]]`
    Tipos: partOf, contradicts, derivedFrom, validates, supersedes.
    Se o tipo não existe em wiki/meta/ontology.md, proponha em
    outputs/inbox/ontology-proposals.md e use o mais próximo com ⚠️.
    Wikilinks planos são proibidos no artigo final.

    **CHECK 2 — INSTANCE→CLASS ESCALATION**
    Para cada claim numérico/estatístico: de qual paper? qual dataset?
    está apresentado como verdade geral ou dado pontual?
    ❌ "self-enhancement bias causa 16.1% de erro"
    ✅ "self-enhancement bias causa até 16.1% de erro em Qwen2 (CALM benchmark)"

    **CHECK 3 — META-KB SEPARATION**
    Referências a /ask, /ingest, /challenge, /scout, /review, "nosso KB",
    "nossa arquitetura" NUNCA pertencem a ## Conteúdo.
    Mova para ## Aplicação à KB ou ## Interpretação.

    **CHECK 4 — RESUMO CALIBRADO**
    O resumo (_index.md, ~150 chars) não pode ser mais confiante que o corpo.
    Se o corpo tem gaps, especulações, ou caveats significativos, o resumo
    deve refletir.
    ❌ "HippoRAG + Reflexion + MemGPT = adaptive retrieval"
    ✅ "Síntese especulativa: feedback de falha poderia modificar topologia — não implementado"

    Salve no final do artigo:
    ```
    ## Quality Gate
    - [ ] Wikilinks tipados: [N substituições, N tipos novos]
    - [ ] Instance→class: [N claims verificados, N qualificados]
    - [ ] Meta-KB separado: [sim/não — N referências movidas]
    - [ ] Resumo calibrado: [sim/não — alterado/mantido]
    ```

13. **Auto-Promote** (após Quality Gate):
    Invoque `/auto-promote [artigo]` imediatamente.
    O comando executa 4 gates automáticos e decide: promover ou quarentenar com razão específica.
    Não defina `quarantine:` manualmente — o /auto-promote define.
    Se o artigo for quarentenado, adicione ao final:
      `> ⚠️ QUARENTENA: [motivo do gate]. Revisão humana necessária.`

14. **Quarantine cross-check:** Após gerar artigo novo, verifique:
    "Algum artigo em quarentena tem claims que este novo paper confirma?"
    Se sim: atualize `quarantine_criteria_met` do artigo em quarentena
    e notifique via `outputs/inbox/quarantine-update-[artigo].md`.

15. DEPOIS de todos os artigos escritos/atualizados, atualize:
    - _registry.md: path | data | type | quality | stance | conceitos | status
    - _index.md: 1 ponteiro por artigo (~150 chars: título + contexto mínimo)
    Ordem importa: artigo primeiro → índice depois. Nunca o contrário.

15.5. **Stub-wiki queue** — para cada fonte registrada com status `stub-wiki`:

    Compute `completion_priority` para o(s) conceito(s) da fonte:
    ```bash
    python3 - <<'EOF'
    import re, sys
    from pathlib import Path
    from collections import Counter

    concept_slugs = sys.argv[1:]  # slugs dos concepts da fonte stub-wiki
    wiki_dir = Path("wiki/concepts")
    in_degree = Counter()
    reads_map = {}
    for f in wiki_dir.glob("*.md"):
        if f.stem.startswith("_"): continue
        text = f.read_text()
        for link in re.findall(r'\[\[([^\]|#]+)', text):
            in_degree[link.strip().lower().replace(' ', '-')] += 1
        m = re.search(r'^reads:\s*(\d+)', text, re.MULTILINE)
        reads_map[f.stem] = int(m.group(1)) if m else 0

    for slug in concept_slugs:
        deg = in_degree.get(slug, 0)
        reads = reads_map.get(slug, 0)
        print(f"{slug}  in_degree={deg}  reads={reads}  priority={deg*2+reads}")
    EOF
    ```
    Passe os slugs dos concepts como argv (ex: `python3 - procurement-renegotiation incentive-theory-procurement`).

    Adicione cada conceito a `stub_completion_queue` em `outputs/state/kb-state.yaml`:
    ```yaml
    stub_completion_queue:
      updated: YYYY-MM-DD
      entries:
        - stem: concept-slug
          source: raw/papers/fonte.md   # fonte raw/ que gerou o stub
          in_degree: N
          reads: N
          completion_priority: N
          option_b_eligible: true|false  # false se in_degree >= 5 ou sem fontes raw/
          ineligibility_reason: null | "in_degree=N >= 5"
    ```
    Se o conceito já está na fila: atualize `in_degree`, `reads`, `completion_priority`.
    Não duplicar entradas — use o stem como chave.

16. **Log de occurrent:** Salve log da sessão em
    `outputs/logs/sessions/YYYY-MM-DD/ingest-[source-slug]-HH-MM.md`
    segundo schema em `wiki/meta/process-log.md`.

Reporte: X fontes processadas, Y artigos criados, Z atualizados, W patches resolvidos.
Se encontrar fontes com problemas (vazio, ilegível, duplicata exata): reporte sem processar.

## Após processar (antes do log de occurrent)

**SPRT chain update** (se este ingest foi `chain_triggered: true`):
```yaml
ingest_chain:
  depth: [depth + 1]
  status: closed          # SEMPRE closed após auto-ingest de INVALIDA
  last_challenge: YYYY-MM-DD
```
Se este ingest foi manual (chain_triggered: false ou ausente):
```yaml
ingest_chain:
  depth: 0
  status: open
  origin_article: null
```

Atualize `outputs/state/kb-state.yaml`:
1. `ingest_count_since_last_lint += 1`
2. `sessions_since_last_dream += 1`
3. `last_updated` com data atual
4. Atualize `readiness_signal`:
   - Recalcule `stance_status` com base no total atual de fontes por stance no _registry.md
   - Se stance challenging < 20%: `can_ingest: true`, `warning: "stance baixo — busque fonte challenging"`
   - Se stance challenging 20-25%: `can_ingest: true`, `warning: null` (ou "marginal" se próximo de 25%)
   - Se stance challenging > 25%: `can_ingest: true`, `stance_status: "saudável"`
   - Atualize `next_ingest_candidates` com os itens do topo de `ingest_queue_priority` e `ingest_queue_autoresearch`
5. Atualize `next_actions`:
   - Se artigo entrou em quarentena por Gate 1/2: adicione `/review [artigo]` (humano necessário)
   - Se artigo entrou em quarentena por Gate 3 (weakened): adicione `/challenge [artigo]` para humano decidir se correção é menor
   - Se artigo foi auto-promoted: nenhuma entrada de promoção necessária
   - Se `ingest_count_since_last_lint >= 5`: adicione `/lint-epistemic`
   - Remova da fila `ingest_queue_priority` o item que acabou de ser ingerido
