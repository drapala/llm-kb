# /ask

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
  Imprima: `⚠️ Contexto em [N]%. /dream recomendado antes de continuar. Prosseguir mesmo assim? (s/n)`
  - Se resposta for "s" ou "sim": processa normalmente
  - Se resposta for "n" ou "não": encerra e aguarda /dream
  - Se não houver resposta explícita: processa normalmente com aviso no topo da resposta

Se resultado < 70%: silêncio — processa normalmente.

---

## Leader Impartiality Check (Janis, 1972)
Antes de processar, verifique: a pergunta pressupõe uma resposta?
- "Como o RWKG funciona?" → pressupõe que funciona. Reformular: "O RWKG funciona? Sob quais condições?"
- "Quais melhorias aplicar?" → pressupõe que melhorias são necessárias. Reformular: "A KB precisa de melhorias neste ponto?"
Se a pergunta é direcional, sugira reformulação aberta antes de processar.

---

## Corpus Sufficiency Check (anti-loop epistêmico)

Antes de rodar Layer 0, avalie: **existe corpus em raw/ sobre o domínio da query?**

**Anti-pattern — Loop Epistêmico Circular:**
query sobre X → KB sem corpus de X → resposta paramétrica do LLM → parece fundamentada mas não é.
Se o corpus sobre o domínio da query é ausente, /ask retorna gap, não resposta.

**Sinal de risco:** Layer 0 retorna scores < 0.02 E Layer 1 não identifica nenhum artigo candidato.
Nesse caso: **PARE**, reporte o gap, e **execute `/scout` automaticamente** focado no domínio da query antes de qualquer síntese. Não fabrique resposta com conhecimento paramétrico.

**Auto-scout ao detectar gap:**
Quando gap é confirmado (scores < 0.02 + nenhum artigo candidato):
1. Identifique o domínio do gap (ex: "contractor offshoring Brazil", "AI occupation mobility")
2. Execute `/scout` com contexto: "scout focado em: [domínio do gap]"
3. Reporte os candidatos encontrados ao usuário
4. Pergunte: "Quer que eu ingira os top candidatos agora?"
Só então sintetize resposta parcial com o que existe (marcado com confiança BAIXA e gap explícito).

**Padrão correto — Ask com Âncoras:**
Se o usuário perguntou "como faço X?", reformule internamente como:
"Dado que o usuário precisa de X, quais conceitos relacionados estão ausentes no corpus?"
Responda o gap, não a pergunta direta.

**Padrão — Gap Mapping:**
/ask detecta *unknown knowns* (o que existe mas não está indexado) — não *unknown unknowns*.
Se a query exige unknown unknowns, o fluxo correto é:
1. /scout automático (disparado acima)
2. Ingestão do corpus relevante via /ingest
3. /ask fundamentado no novo corpus

---

O usuário faz uma pergunta. Para responder, siga as 4 camadas de retrieval:

Layer 0 — Vector Search (PRIMEIRO, antes de ler qualquer arquivo):
Chame o MCP tool `kb_search` com a query do usuário:
```
kb_search(query="<pergunta do usuário>", limit=5)
```
Se o MCP tool não estiver disponível, use o fallback:
```bash
source .venv/bin/activate && python -c "
import sys, json; sys.path.insert(0, '.')
from api.core import search
results = search('<query>', limit=5)
print(json.dumps([{'title': r['title'], 'source': r['source'].split('/')[-1], 'score': round(r['score'],4)} for r in results], indent=2))
"
```
Resultado: lista rankeada de artigos candidatos. Estes são os candidatos **primários** para Layer 2.
- Se nenhum resultado com score relevante: indício de gap — anote e continue com Layer 1.
- Não leia os artigos ainda — Layer 0 só identifica, Layer 2 lê.

Layer 1 — Orientação global:
1. Leia wiki/_index.md inteiro (~150 chars por artigo, leve)
2. Verifique se Layer 0 perdeu algum artigo obviamente relevante
3. Adicione no máximo 2 suplementos ao conjunto de candidatos
   (Layer 0 já fez o trabalho pesado — Layer 1 é checagem, não candidatura)

Layer 2 — Profundidade:
4. Leia os artigos de Layer 0 + suplementos de Layer 1 em wiki/concepts/
5. Trate o wiki como HINT, não como verdade
5b. **Quarantine check:** Se um artigo selecionado tem `quarantine: true`,
    leia-o MAS prefixe TODOS os claims dele com "⚠️ artigo em quarentena —
    claims especulativos." Não ignore — informação especulativa é útil se
    rotulada. Não trate como igual a artigos promovidos.
6. **Circuit breaker:** Se nenhum dos candidatos for relevante para a pergunta,
   PARE e reporte como gap. Não tente ler raw/ inteiro como fallback.

Layer 3 — Verificação:
7. Para claims importantes: vá à fonte original em raw/ para verificar.
   Se wiki contradiz raw/, raw/ vence.
8. Sintetize resposta

Formato obrigatório:
- **Resposta** — direto ao ponto
- **Fontes wiki** — [[wikilinks]] dos artigos usados (marque com `[L0]` os vindos do vector search, `[L1]` os adicionados pelo _index.md)
- **Fontes raw verificadas** — links para raw/ quando claims foram checados na origem
- **Confiança** — alta/média/baixa baseada na cobertura E verificação
- **Gaps** — o que o wiki não cobre e que fonte o usuário deveria adicionar

Se a resposta depender de claim não verificável em raw/ (só existe no wiki
sem fonte clara), sinalize com ⚠️.

## Sugestão de arquivamento

Se a resposta contém taxonomia original, síntese canônica, ou insight
reutilizável que não existe em nenhum artigo wiki, sugira ao final:
"Esta resposta contém [descrição]. Quer que eu arquive as partes
canônicas no wiki?"

## Log de occurrent

Ao final de TODA sessão /ask, salve log seguindo
`.claude/hooks/ask-logger.md` em:
`outputs/logs/sessions/YYYY-MM-DD/ask-HH-MM.md`

Campos obrigatórios: query, articles_read, confidence, synthesis_type.
Retrieval gaps é o campo mais valioso — identifica falhas de retrieval.
Ver `wiki/meta/process-log.md` para schema completo.

## Utility tracking

Após salvar o log, execute utility-tracker:
- Incrementa `reads` nos artigos lidos
- Incrementa `retrievals_correct` se confidence HIGH/MEDIUM (verificados)
- Incrementa `retrievals_gap` nos artigos identificados como gap
- Atualiza `last_read` com data da sessão
Ver `.claude/hooks/utility-tracker.md` para instruções completas.

---

## Pipeline — kb-state.yaml

### Lê (início)
- `slow_cycle.emerge.top_pairs` — se não vazio, considere iniciar o /ask com um dos pares sugeridos (são os pares com maior potencial de conexão latente)
- `active_triggers` — imprima qualquer trigger de `priority: high` ao usuário antes de processar a query

### Escreve (final)
Se a resposta identificou gaps (artigos mencionados como "o wiki não cobre X"):
```yaml
ask:
  articles_with_recent_gaps:
    - [artigo-que-seria-útil-mas-não-existe-ou-estava-ausente]
  last_session: YYYY-MM-DD/ask-HH-MM.md
```

Se usou um par de `emerge_top_pairs` e confirmou a conexão:
```yaml
synthesize:
  pending_from_ask:
    - pair: [artigo-A, artigo-B]
      ask_session: outputs/logs/sessions/YYYY-MM-DD/ask-HH-MM.md
      connection_type: ANÁLOGO-A | INSTANCIA | EMERGE-DE
```

### Gatilhos — verifique ao final

| Condição | Gatilho |
|----------|---------|
| Conexão cross-cluster confirmada nesta sessão | `💡 /synthesize — conexão [A]×[B] confirmada. Rode /synthesize para criar artigo.` |
| `articles_with_recent_gaps` cresceu | **AUTO-SCOUT:** invoque `/scout` imediatamente, focado no domínio do gap. Passe o gap como contexto: "scout focado em: [domínio do gap identificado]". Não sugira — execute. Após /scout, reporte candidatos ao usuário e pergunte se quer /ingest. |
| Artigo quarentenado foi central na resposta | `💡 /promote ou /challenge — [artigo] em quarentena foi decisivo. Considere promover.` |
