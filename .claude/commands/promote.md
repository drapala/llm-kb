# /promote [artigo]

Verifica se artigo em quarentena pode ser promovido.

## Passo 1 — Lê frontmatter
Se `quarantine: false` → "Artigo não está em quarentena."

## Passo 2 — Critério 1 (tempo)
Compara `quarantine_created` com data atual.
Se < 24h → "Critério 1 não satisfeito. Tempo restante: Xh"

## Passo 3 — Critério 2 (review frio)
Busca em `outputs/logs/sessions/` por `review-[artigo]-*.md` com data diferente de `quarantine_created`.
Se não encontra → "Critério 2 não satisfeito. Rode /review em sessão diferente."

## Passo 4 — Critério 3 (um dos três)
Busca evidência de:
- a) `outputs/logs/sessions/challenge-[artigo]-*.md` com verdict ≠ destroyed
- b) `outputs/reports/scout-*.md` sem `subsumes: true` para este artigo
- c) Seção `## Predição falsificável` no artigo com nível Pearl L2+

Se nenhum encontrado → "Critério 3 não satisfeito. Rode /challenge, /scout, ou adicione predição falsificável."

## Passo 5 — Promoção
Se TODOS satisfeitos:
1. `quarantine: true` → `quarantine: false`
2. Adiciona `quarantine_promoted: [data]`
3. Atualiza `quarantine_criteria_met` com detalhes
4. Remove aviso de quarentena do final do artigo
5. Log em `outputs/logs/sessions/YYYY-MM-DD/promote-[artigo]-HH-MM.md`
6. "Artigo promovido. Pode ser linkado por outros artigos."

## Após promoção bem-sucedida

Atualize `outputs/state/kb-state.yaml`:
1. Adicione artigo promovido a `promoted_since_last_emerge`
2. Atualize `last_updated` com data atual
3. Se `promoted_since_last_emerge` tiver >= 3 artigos após a adição:
   imprima "⚠️ /emerge recomendado ([N] artigos promovidos desde último /emerge)"
