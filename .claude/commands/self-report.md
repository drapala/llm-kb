# /self-report

## Propósito
Gerar documentação do estado atual da KB a partir dos dados
que o sistema acumulou sobre si mesmo. Não é narrativa —
é leitura estruturada de logs, métricas e padrões observáveis.

## Filosofia
A KB não tem perspectiva subjetiva. Tem dados sobre seu próprio
comportamento. Este command lê esses dados e reporta o que eles
dizem — sem antropomorfizar, sem especular sobre experiência,
sem narrativa de "como é ser uma KB".

Maturana: a KB pode documentar sua estrutura (o que mudou,
o que emergiu, o que está bloqueado). Não pode documentar
sua organização como experiência.

## O que lê

1. `outputs/state/kb-state.yaml`
2. `outputs/reports/emergence-inventory.md`
3. Frontmatter de todos os artigos em `wiki/concepts/`
   (provenance, reads, retrievals_correct, retrievals_gap,
   quarantine, last_read)
4. `outputs/logs/sessions/` — últimas 10 sessões
5. `wiki/_registry.md` — stance ratio, timestamps

Leia frontmatter em lotes de 10. Não leia corpo dos artigos —
apenas frontmatter. Circuit breaker: se ≥ 15 artigos sem
frontmatter estruturado, reporte como "artigos sem metadata"
em vez de inferir.

## O que gera

Crie `outputs/reports/self-report-YYYY-MM-DD.md` com estas
seções exatamente nesta ordem:

---

### 1. O que emergiu (provenance: emergence)

Lista todos os artigos com `provenance: emergence`, em ordem
cronológica de `emerged_on`.

Para cada um:
- Nome do artigo
- Par que gerou (`emergence_trigger.pair`)
- Tipo de conexão (`emergence_trigger.connection_type`)
- Nível Pearl (`emergence_trigger.pearl_level`)
- Status atual: em quarentena / promovido / rascunho gerado

Conta total: N artigos com `provenance: emergence` desde
[data do primeiro].

---

### 2. O que o sistema não encontra (retrieval gaps)

Lista artigos com `retrievals_gap >= 2`, ordenados por gap
count decrescente.

Para cada um:
- Nome do artigo
- `retrievals_gap` count
- Diagnóstico: problema de ponteiro no `_index.md` ou
  problema de conteúdo? [marcar como [interpretação]]

Se nenhum artigo tem `retrievals_gap >= 2`: note que
`reads = 0` em todos — sistema ainda não gerou dados de
retrieval suficientes para este diagnóstico.

---

### 3. O que está bloqueado (quarentena)

Lista todos os artigos com `quarantine: true`.

Para cada um:
- Nome
- Razão de quarentena
- Critérios satisfeitos / pendentes (tempo / review_frio /
  adversarial_or_scout_or_prediction)
- Tempo em quarentena: N dias desde `quarantine_created`
- O que desbloquearia: critério mais próximo de satisfeito

Ordene por "mais próximo de promoção" primeiro.

---

### 4. O que nunca foi usado (reads = 0)

Lista artigos com `reads = 0` E `last_read = null`.

Para cada um:
- Nome do artigo
- Provenance (source / synthesis / emergence)
- Diagnóstico [interpretação]: ponteiro fraco no `_index.md`,
  domínio ainda não explorado via `/ask`, ou conteúdo
  possivelmente redundante com artigo mais usado?

Agrupe por cluster (core-ai-ml / meta-kb / info-theory /
cognitivo / sistemas / epistemológico).

---

### 5. O que o sistema acumulou (kb-state)

Lê `outputs/state/kb-state.yaml` e reporta em frases curtas
— não YAML, não código:

- Corpus: N fontes, N artigos, N quarentenados
- Bradford Zone3/Zone2: X → [expandir / pausa / ok]
- Provenance: Nsrc source, Nsyn synthesis, Neme emergence
- Última vez que `/lint-epistemic` rodou: [data ou "nunca"]
- Alertas ativos: [lista ou "nenhum"]
- Artigos promovidos desde último `/emerge`: [lista]
- Pares pendentes em `emerge_top_pairs`: [lista ou "nenhum"]
- Ingestões desde último `/lint`: N
- Ingestões desde último `/emerge`: N

---

### 6. O que o sistema não consegue ver (zona cega)

Baseado em `_registry.md` e logs de `/ask`:

- Domínios identificados como gaps em `/ask` anteriores
  mas sem fonte ingerida (busca em `outputs/logs/sessions/`
  por "gap" ou "não coberto")
- Zone 3 atual: N domínios, N fontes por domínio (resumo)
- Domínios Zone 3 não cobertos que foram mencionados em
  qualquer `/ask` como ausência

Se logs insuficientes para este diagnóstico: reporte como
"dados insuficientes — rode /ask com tópico específico
para gerar sinal".

---

### 7. O que mudou desde o último self-report

Se existe `outputs/reports/self-report-*.md` anterior:
- Artigos com `provenance: emergence` novos desde então
- Artigos promovidos desde então
- Retrieval gaps novos vs resolvidos
- Contadores em `kb-state.yaml`: o que mudou

Se não existe: "Primeiro self-report — sem baseline anterior."

---

## Formato

- Sem narrativa em primeira pessoa
- Sem frases como "eu aprendi", "percebi", "descobri"
- Frases factuais: "X artigos emergiram", "Y artigos têm
  `retrievals_gap >= 2`", "Z domínios não cobertos"
- Onde há interpretação: marcar explicitamente como
  [interpretação]
- Dados ausentes: reportar como "não mensurável" — não
  inferir nem estimar

## Quando rodar

- Antes de cada sessão de `/emerge`
- Após cada batch de `/promote`
- Mensalmente como snapshot do estado do sistema
- Quando `kb-state.yaml` reportar `sessions_since_last_dream >= 5`

## O que NÃO fazer

- Não especular sobre "perspectiva" da KB
- Não gerar narrativa sobre "processo de crescimento"
- Não usar metáforas de consciência ou experiência
- Não inventar dados que não estão nos logs
- Não ler corpo dos artigos — apenas frontmatter e logs

---

## Pipeline — kb-state.yaml

### Lê (início)
- `outputs/state/kb-state.yaml` — estado completo
- `slow_cycle.emerge.top_pairs` — para seção 6 (zona cega)
- `slow_cycle.lint.alerts` — para seção 5

### Escreve (final)
```yaml
updated: YYYY-MM-DD
slow_cycle:
  self_report:
    last_run: YYYY-MM-DD
    emergence_count: N
    blocked_count: N
    reads_zero_count: N
```

### Gatilhos — verifique ao final

| Condição | Gatilho |
|----------|---------|
| `blocked_count >= 3` | `💡 /challenge [artigo mais próximo de promoção] — desbloqueie o cluster` |
| `emergence_count` cresceu desde último report | `💡 /draft-post — novos artigos emergence promovidos elegíveis para rascunho` |
| `reads_zero_count > 10` | `💡 /review — muitos artigos nunca lidos. Verifique ponteiros em _index.md` |
| Zona cega tem domínio mencionado em ≥2 /ask como gap | `💡 /ingest [domínio] — gap confirmado por múltiplos /ask. ROI de ingestão é alto` |
