# /ask

O usuário faz uma pergunta. Para responder, siga as 3 camadas de retrieval:

Layer 1 — Orientação:
1. Leia wiki/_index.md inteiro (~150 chars por artigo, leve)
2. Identifique os 5-10 artigos mais relevantes pelos ponteiros

Layer 2 — Profundidade:
3. Leia esses artigos em wiki/concepts/
4. Trate o wiki como HINT, não como verdade

Layer 3 — Verificação:
5. Para claims importantes: vá à fonte original em raw/ para verificar.
   Se wiki contradiz raw/, raw/ vence.
6. Sintetize resposta

Formato obrigatório:
- **Resposta** — direto ao ponto
- **Fontes wiki** — [[wikilinks]] dos artigos usados
- **Fontes raw verificadas** — links para raw/ quando claims foram checados na origem
- **Confiança** — alta/média/baixa baseada na cobertura E verificação
- **Gaps** — o que o wiki não cobre e que fonte o usuário deveria adicionar

Se a resposta depender de claim não verificável em raw/ (só existe no wiki
sem fonte clara), sinalize com ⚠️.
