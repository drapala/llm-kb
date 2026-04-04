# /prioritize [contexto]

Converte candidatos de conexão do /emerge em fila de trabalho ordenada por valor para um contexto específico.

## Uso

```
/prioritize zelox
/prioritize research
/prioritize zelox outputs/reports/emerge-2026-04-04.md
```

Se o path do emerge-report não for especificado, usa o mais recente em `outputs/reports/emerge-*.md`.

## Input

1. `outputs/reports/emerge-[data].md` — candidatos gerados pelo /emerge
2. `.claude/contexts/[contexto].yaml` — definição do contexto (gate criteria, pesos, janela)

## Passo 1 — Lê insumos

1. Lê o emerge-report especificado (ou mais recente)
2. Lê `.claude/contexts/[contexto].yaml`
3. Extrai: gate_criteria, impacto_weights, janela_atual, backlog_path

## Passo 2 — GATE (elimina antes de rankear)

Para cada candidato do emerge-report, aplica os 3 gates do contexto em sequência. Se **qualquer gate falhar**, move para backlog sem score:

```
GATE [candidato]:
- [ ] Dados disponíveis? [verifica gate_criteria.dados_disponiveis]
      Razão se falhar: [quais dados estão ausentes]
- [ ] Consequência acionável no contexto? [verifica gate_criteria.consequencia_acionavel]
      Razão se falhar: [por que a conexão não gera ação neste contexto]
- [ ] Rota de validação definida? [verifica se custo de verificação é compatível com recursos do contexto]
      Razão se falhar: [o que impede a validação]
→ PASSA / FALHA [gate que falhou]
```

Candidatos que falham no gate → `outputs/reports/backlog-[contexto]-[data].md` com razão registrada.

## Passo 3 — SCORE (só para quem passou o gate)

Para cada candidato que passou o gate, calcula `priority_score`:

```
testabilidade_score:
  L1 = 1.0
  L2 = 0.7  (requer intervenção — mais difícil mas mais robusto)
  L3 = 0.4

custo_score:
  baixo  = 1.0
  médio  = 1.5
  alto   = 2.2

espurio_score:
  baixo  = 1.0
  médio  = 1.6
  alto   = 2.4

impacto_score:
  Calcula usando impacto_weights do contexto (soma ponderada dos fatores do yaml)

janela_score:
  Lê janela_atual do contexto
  Se conexão é urgente para a janela atual: multiplicador > 1.0
  Se conexão é relevante mas não urgente: multiplicador = 1.0
  Se fora da janela: multiplicador < 1.0 (mas não move para backlog — só deprioritiza)

priority_score = (impacto_score × testabilidade_score × janela_score)
                / (custo_score × espurio_score)
```

**Nota:** Score maior = maior prioridade. A divisão por custo e espúrio penaliza candidatos caros e arriscados. A multiplicação por testabilidade penaliza L3 (contrafactual — mais incerto).

## Passo 4 — Output

Gera dois arquivos:

### `outputs/reports/priority-[contexto]-[data].md`

```markdown
---
date: YYYY-MM-DD
context: [contexto]
emerge_source: outputs/reports/emerge-[data].md
---

## Fila de prioridade — [contexto]

| # | Par | Score | Pearl | Espúrio | Custo | Impacto |
|---|-----|-------|-------|---------|-------|---------|
| 1 | A × B | X.XX | L2 | baixo | baixo | alto |
| 2 | C × D | X.XX | L2 | médio | baixo | médio |
...

## Detalhes

### #1: [Artigo A] × [Artigo B] — Score: X.XX

**Gate:** PASSOU (dados: ✓, acionável: ✓, validação: ✓)
**Impacto no contexto:** [descrição específica do impacto no contexto]
**Próximo passo:** [ação concreta — /ask, ingestão, experimento]
**Pergunta /ask:** "[prompt do emerge-report]"

...

## Backlog — gate falhou

### [Artigo A] × [Artigo B]
**Gate falhou:** [qual gate]
**Razão:** [por que]
**Rever quando:** [condição que mudaria o resultado]
```

### `outputs/reports/backlog-[contexto]-[data].md`

Arquivo separado com candidatos que falharam no gate, para revisão futura.

## Passo 5 — Atualiza kb-state.yaml

```yaml
prioritize:
  last_run: YYYY-MM-DD
  context: [contexto]
  emerge_source: outputs/reports/emerge-[data].md
  queue: outputs/reports/priority-[contexto]-[data].md
  top_pair: [par #1 da fila]
```

## Filosofia

O /emerge é **agnóstico de contexto** — ordena por qualidade epistêmica pura (testabilidade, espúrio, custo).
O /prioritize é **context-aware** — injeta valor de negócio/pesquisa sobre os candidatos epistêmicos.

Separação de responsabilidades:
- /emerge: "Quais conexões existem e são verificáveis?"
- /prioritize: "Quais dessas conexões importam para X agora?"

Isso permite reusar o mesmo emerge-report para múltiplos contextos:
```
/prioritize zelox   # prioriza por impacto em feature engineering
/prioritize research  # prioriza por novidade científica
```
