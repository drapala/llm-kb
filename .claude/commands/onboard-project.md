# /onboard-project

## Propósito
Integra um novo projeto ao METAXON de forma que /ask sessions sobre domínios
relacionados leiam o estado real do código antes de sugerir mudanças.

## Input esperado
O usuário passa:
```
/onboard-project <nome> <caminho> [clusters]
```
Exemplos:
```
/onboard-project advantage-group ~/projects/advantage-group econ-poli,strategy
/onboard-project proofpoint ~/projects/proofpoint agents,ai-tech-debt
```

Se o usuário não passar argumentos, pergunte:
1. Nome do projeto (slug kebab-case, ex: `advantage-group`)
2. Caminho absoluto do projeto
3. Quais clusters do KB são adjacentes? (liste os disponíveis: `econ-poli`, `strategy`, `ai-tech-debt`, `agents`, `meta-kb`, `retrieval`, `lateral`, `neurosymbolic`, `info-theory`, `ai-labor`)
4. Quais arquivos-chave mudam quando features são adicionadas? (ex: `src/ag/models/risk.py`)

---

## Passos de execução

### Passo 1 — Inspecionar o projeto

```bash
ls <caminho>/
```

Identifique:
- A linguagem principal (Python/TS/Go/...)
- Se tem Makefile
- Se tem `.claude/settings.json`
- Os arquivos que definem features/sinais/scores (o equivalente de `supplier_risk_check_v1.py`)

### Passo 2 — Criar `contexts/<projeto>.yaml`

Salve em `llm-kb/.claude/contexts/<projeto>.yaml`:

```yaml
# <Projeto> Context — [descrição em 1 linha]
# Usado por /ask quando a sessão toca clusters [lista de clusters]

name: <projeto>
description: "[descrição para /prioritize]"

# ─── GATE CRITERIA ───────────────────────────────────────────────────────────

gate_criteria:

  dados_disponiveis:
    description: "Quais dados/APIs este projeto tem acesso?"
    sources_available:
      - [liste aqui o que o usuário informou]
    fail_condition: "A conexão requer dados não listados acima"

  consequencia_acionavel:
    description: "O que insights do KB podem gerar neste projeto?"
    acceptable_actions:
      - [liste aqui as ações típicas: novo sinal, ajuste de peso, nova feature, etc.]
    fail_condition: "Conexão é teoricamente interessante mas não mapeia para nenhuma ação implementável"

  rota_de_validacao:
    description: "Existe rota clara para testar nos dados do projeto?"
    acceptable_routes:
      - [liste aqui: análise estatística, backtesting, A/B test, etc.]
    fail_condition: "Validação requer dados institucionais não acessíveis"

# ─── IMPACTO WEIGHTS ─────────────────────────────────────────────────────────

impacto_weights:
  feature_utility:
    description: "O quanto o insight melhora algo implementável?"
    weight: 0.40
  validability:
    description: "O quanto é fácil testar com dados disponíveis?"
    weight: 0.35
  signal_robustness:
    description: "Resistência a degradação / gaming / drift?"
    weight: 0.25

# ─── JANELA ATUAL ────────────────────────────────────────────────────────────

janela_atual:
  description: "[versão/fase atual]"
  current_scope: "V1.0"

# ─── IMPLEMENTATION STATE ────────────────────────────────────────────────────
# Atualizado por: cd <caminho> && make context
# Snapshot completo em: raw/notes/<projeto>-codebase-snapshot.md

implementation_state:
  deployed_features: []   # preencher após gen-context.py rodar
  pending_features: []
  key_files: {}

# ─── OUTPUT PATHS ────────────────────────────────────────────────────────────

output:
  priority_report: "outputs/reports/priority-<projeto>-{date}.md"
  backlog: "outputs/reports/backlog-<projeto>-{date}.md"
```

### Passo 3 — Criar `scripts/gen-context.py` no projeto

Leia a estrutura do projeto identificada no Passo 1.
Crie `<caminho>/scripts/gen-context.py` adaptado ao projeto.

O script deve:
- Importar os arquivos-chave via `pathlib.Path`
- Usar `ast.parse()` para extrair constantes e funções relevantes
- Escrever `llm-kb/raw/notes/<projeto>-codebase-snapshot.md`
- Seguir o mesmo padrão do zelox: seções "Features Implementadas", "Features Pendentes", "Arquitetura"

**Template mínimo** (adaptar ao stack do projeto):

```python
#!/usr/bin/env python3
"""gen-context.py — <Projeto> codebase snapshot para METAXON"""
from __future__ import annotations
import ast
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
LLM_KB_ROOT = PROJECT_ROOT.parent / "llm-kb"
OUTPUT = LLM_KB_ROOT / "raw/notes/<projeto>-codebase-snapshot.md"

KEY_MODULES = {
    # "rel/path/to/key_file.py": "descrição do que contém",
}

def build_snapshot() -> str:
    today = date.today().isoformat()
    # ... extrair info dos KEY_MODULES ...
    # retornar markdown com frontmatter
    pass

if __name__ == "__main__":
    OUTPUT.write_text(build_snapshot())
    print(f"Snapshot: {OUTPUT}")
```

### Passo 4 — Adicionar `make context` ao Makefile do projeto

Se o projeto tem Makefile:
```makefile
context:
	uv run python scripts/gen-context.py
```

Se não tem Makefile, criar um mínimo com apenas este target.

### Passo 5 — Hook determinístico (Claude Code)

Criar `<caminho>/.claude/settings.json`:

```json
{
    "hooks": {
        "PostToolUse": [
            {
                "matcher": "Edit|Write",
                "hooks": [
                    {
                        "type": "command",
                        "command": "<caminho>/bin/hooks/post-write-context.sh"
                    }
                ]
            }
        ]
    }
}
```

Criar `<caminho>/bin/hooks/post-write-context.sh`:

```bash
#!/usr/bin/env bash
# auto-regenera snapshot METAXON quando arquivos-chave mudam
KEY_MODULES=(
    # "rel/path/to/key_file.py"  ← preencher com os arquivos do Passo 1
)

FILE_PATH=$(python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('file_path', ''))
except Exception:
    print('')
" 2>/dev/null)

[ -z "$FILE_PATH" ] && exit 0

for MODULE in "${KEY_MODULES[@]}"; do
    if [[ "$FILE_PATH" == *"$MODULE"* ]]; then
        make -C "<caminho>" context 2>/dev/null
        echo "[<projeto>-context] snapshot regenerado: $MODULE" >&2
        exit 0
    fi
done
```

```bash
chmod +x <caminho>/bin/hooks/post-write-context.sh
```

### Passo 6 — Registrar clusters em `ask.md`

Abra `.claude/commands/ask.md` e localize a seção **Gatilhos**.

Adicione linha na tabela de Gatilhos:

```
| **Sessão <Projeto>-adjacent** E resposta contém conclusão de design | **TRADUÇÃO METAXON→<PROJETO>:** pergunte ao final: "Esta conclusão precisa de ADR ou item de backlog no <Projeto>? (ADR: mudança de design com alternativas; backlog: implementação pendente)" — e execute se sim. |
```

Adicione seção "Clusters <Projeto>-adjacent" análoga à seção Zelox existente:

```markdown
**Clusters <Projeto>-adjacent** (condição da última linha):
A sessão é <Projeto>-adjacent se ≥1 artigo lido pertence a qualquer um destes índices:
- `_index-<cluster1>.md`
- `_index-<cluster2>.md`
```

Adicione ao bloco "Pipeline — Contexto de Projeto" em `ask.md`:

```markdown
Se a sessão é **<Projeto>-adjacent** (≥1 artigo lido pertence a `_index-<cluster>.md`):
**Antes de processar a query**, leia:
1. `.claude/contexts/<projeto>.yaml` — seção `implementation_state`
2. `raw/notes/<projeto>-codebase-snapshot.md`
```

### Passo 7 — Rodar e verificar

```bash
cd <caminho> && make context
```

Verifique que `llm-kb/raw/notes/<projeto>-codebase-snapshot.md` foi criado.

---

## Checklist de conclusão

- [ ] `llm-kb/.claude/contexts/<projeto>.yaml` criado
- [ ] `<caminho>/scripts/gen-context.py` criado e funcional
- [ ] `make context` adicionado ao Makefile
- [ ] `.claude/settings.json` criado no projeto
- [ ] `bin/hooks/post-write-context.sh` criado e executável
- [ ] Clusters adicionados em `ask.md` Gatilhos + Pipeline seção
- [ ] `make context` rodou com sucesso (snapshot gerado)

---

## O que NÃO faz
- Não cria artigos wiki sobre o projeto (isso é /ingest)
- Não define os gate_criteria automaticamente — você precisa de input do usuário
- Não commita nada
- Não modifica o projeto target além de criar scripts/

## Após concluir

Rode `/ask` sobre um tópico do KB adjacente ao projeto novo e verifique que o
snapshot é lido automaticamente. Se o /ask não mencionar features implementadas
vs. pendentes, a integração está incompleta.
