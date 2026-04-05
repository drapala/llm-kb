# /retro

Consolida friction events em padrões observáveis. Só observa e classifica — não propõe.

## Quando rodar

- Quando acumular 10+ friction events desde o último retro
- Mensalmente como manutenção
- Antes de rodar `/propose` pela primeira vez

## Processo

### Passo 1 — Lê friction events

Lê todos os arquivos em `raw/meta/ops/friction-*.md` que ainda não foram incluídos em um retro anterior.
(Verifica `wiki/meta/friction-log.md` para identificar quais já foram consolidados.)

Circuit breaker: se houver > 50 eventos não consolidados, processa em lotes de 20 e reporta parcialmente.

### Passo 2 — Classifica cada evento

Para cada evento, identifica:
- **Surface**: onde no workflow ocorreu
- **Tipo de problema** (escolha exatamente um):
  - `estado-invisível` — o sistema não mostrava em que estado estava
  - `próxima-ação-ausente` — não estava claro o que fazer depois
  - `sequencing` — a ordem correta dependia de memória, não de estrutura
  - `nomenclatura` — nome do comando/arquivo/conceito era ambíguo
  - `excesso-de-opções` — muitas possibilidades sem critério visível
  - `overhead-manual` — passo que devia ser automático ou assistido

**Não infira causa.** Se o evento não encaixa em nenhuma categoria, classifica como `não-classificado` e continua.

### Passo 3 — Identifica padrões

Agrupa eventos por `(surface, tipo-de-problema)`. Um padrão existe quando:
- ≥2 eventos do mesmo tipo na mesma surface, OU
- ≥3 eventos do mesmo tipo em surfaces diferentes (problema sistêmico)

Para cada padrão, verifica se há princípio externo em `raw/meta/ux/` que sustenta a classificação.
Se não houver fonte em `raw/meta/ux/` ainda, registra como "sem sustentação externa — candidato a ingestão".

**Não busca solução.** Só verifica se o padrão está sustentado por evidência externa.

### Passo 4 — Atualiza `wiki/meta/friction-log.md`

Atualiza o arquivo com:

```markdown
# Friction Log

Última consolidação: YYYY-MM-DD
Eventos processados: N (total acumulado: N)

## Padrões ativos

### [surface] × [tipo-de-problema]
- Eventos: N (datas: YYYY-MM-DD, ...)
- Descrição do padrão: [2-3 linhas do que os eventos têm em comum]
- Sustentação externa: [artigo em raw/meta/ux/ ou "pendente — ingerir [tema]"]
- Status: ativo | em-teste | resolvido

...

## Eventos não-classificados
- [lista de eventos que não encaixaram]

## Candidatos a ingestão (UX)
- [temas sem cobertura em raw/meta/ux/ mas com padrão identificado]
```

### Passo 5 — Relatório terminal

```
/retro completo — YYYY-MM-DD

Eventos processados: N
Padrões identificados: N
  - N com sustentação externa
  - N sem sustentação (candidatos a ingestão)
Eventos não-classificados: N

Próximos passos:
  - Se padrão com sustentação: /propose [padrão]
  - Se candidato a ingestão: ingira raw/meta/ux/ sobre [tema]
  - Se muitos não-classificados: revise schema de tags em /friction
```

## O que /retro NÃO faz

- Não propõe mudanças de workflow
- Não modifica nenhum comando
- Não avalia se a mudança seria boa ou ruim
- Não lê kb-state.yaml como base primária (pode ler como contexto auxiliar se relevante)

## kb-state.yaml

### Escreve (ao final)
```yaml
slow_cycle:
  retro:
    last_run: YYYY-MM-DD
    events_processed: N
    patterns_active: N
    patterns_with_evidence: N
```
