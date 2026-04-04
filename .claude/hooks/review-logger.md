# Review Logger

## Quando ativa

Ao final de TODA sessão /review que modifica um artigo wiki.

## O que captura

### 1. TRIGGER
Por que o review foi disparado:
| Trigger | Causa |
|---------|-------|
| MANUAL | Usuário pediu explicitamente |
| CHALLENGE-FLAG | /challenge marcou como needs-revision |
| INGEST-CONFLICT | Novo paper contradiz claim existente |
| AUDIT | Auditoria periódica (epistêmica, ontológica) |
| ONTOLOGY-VIOLATION | Quality gate detectou problema |

### 2. CHANGES
Para cada mudança no artigo:
- **Tipo**: factual / epistemic / ontological / structural
- **Before**: claim exato anterior
- **After**: claim corrigido
- **Reason**: por que mudou (nova evidência / erro detectado / qualificação necessária / confusão ontológica)

### 3. PROPAGATION CHECK
Após modificar um artigo, verifique:
"Quais outros artigos citam este via wikilink? A mudança invalida ou qualifica algum claim nesses artigos?"

Se sim: adicione em `outputs/inbox/propagation-review.md` com formato:
`[artigo afetado] — [claim impactado] — [urgência: high/medium/low]`

### 4. NET EPISTEMIC CHANGE
A KB ficou mais ou menos confiante sobre este domínio após o review? Em que direção o conhecimento foi corrigido? (mais preciso? mais cauteloso? mais abrangente? mais restrito?)

## Formato do log

Salve em `outputs/logs/sessions/YYYY-MM-DD/review-[artigo]-HH-MM.md`

```markdown
# Review Session Log
date: YYYY-MM-DD HH:MM
article: wiki/concepts/[artigo].md
trigger: [tipo]

## Changes
### Change 1
type: [factual|epistemic|ontological|structural]
before: "[claim anterior]"
after: "[claim corrigido]"
reason: "[por que mudou]"

## Propagation check
- [artigo afetado]: [claim impactado] — [urgência]

## Net epistemic change
[direção da correção]
```
