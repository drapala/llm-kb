# Logs de Occurrents

Este diretório contém o registro de processos da KB — o que acontece quando a KB é usada, não o que a KB sabe.

## Estrutura

```
outputs/logs/sessions/YYYY-MM-DD/
  ask-HH-MM.md                    — sessões /ask
  review-[artigo]-HH-MM.md        — sessões /review
  ingest-[source]-HH-MM.md        — sessões /ingest
  challenge-[artigo]-HH-MM.md     — sessões /challenge
```

## Por que isso importa

Sem registro de occurrents:
- Não sabemos quais artigos são mais consultados
- Não sabemos onde o retrieval falha
- Não sabemos se respostas foram corretas
- Não podemos implementar learning-from-experience

Este diretório é o pré-requisito de RWKG e qualquer mecanismo similar.

## Schema

Ver `wiki/meta/process-log.md` para o schema formal de cada tipo de log.
