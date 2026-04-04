# /ask

## Pre-check de contexto

Execute este script bash e leia o resultado:

```bash
SESSION=$(ls -t ~/.claude/projects/-Users-drapala-projects-llm-kb/*.jsonl 2>/dev/null | head -1)
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

O usuário faz uma pergunta. Para responder, siga as 3 camadas de retrieval:

Layer 1 — Orientação:
1. Leia wiki/_index.md inteiro (~150 chars por artigo, leve)
2. Identifique os 5-10 artigos mais relevantes pelos ponteiros

Layer 2 — Profundidade:
3. Leia esses artigos em wiki/concepts/
4. Trate o wiki como HINT, não como verdade
4b. **Quarantine check:** Se um artigo selecionado tem `quarantine: true`,
    leia-o MAS prefixe TODOS os claims dele com "⚠️ artigo em quarentena —
    claims especulativos." Não ignore — informação especulativa é útil se
    rotulada. Não trate como igual a artigos promovidos.
5. **Circuit breaker:** Se nenhum dos 5-10 artigos candidatos for relevante
   para a pergunta, PARE e reporte como gap. Não tente ler raw/ inteiro
   como fallback — isso é desperdício de contexto, não verificação.

Layer 3 — Verificação:
6. Para claims importantes: vá à fonte original em raw/ para verificar.
   Se wiki contradiz raw/, raw/ vence.
7. Sintetize resposta

Formato obrigatório:
- **Resposta** — direto ao ponto
- **Fontes wiki** — [[wikilinks]] dos artigos usados
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
| `articles_with_recent_gaps` cresceu | `💡 /emerge — novos gaps identificados. /emerge pode sugerir /ask nos pares certos.` |
| Artigo quarentenado foi central na resposta | `💡 /promote ou /challenge — [artigo] em quarentena foi decisivo. Considere promover.` |
