# llm-kb

Knowledge base pessoal compilada por LLM. Fontes brutas entram em `raw/`, o agente sintetiza artigos interligados em `wiki/`, e `/ask` responde com citação de fonte e verificação.

## Estrutura

```
raw/           → fontes imutáveis (artigos, papers, notas)
wiki/          → enciclopédia compilada pelo agente
  concepts/    → 1 conceito = 1 arquivo
  _index.md    → ponteiros (~150 chars/linha)
  _registry.md → registro de fontes processadas
outputs/       → relatórios e artefatos derivados
```

## Uso

```bash
# 1. Adicione fontes em raw/articles/ ou raw/papers/
# 2. Processe
claude /ingest

# 3. Pergunte
claude /ask "como RAG se compara a long context?"
```

## Comandos

| Comando | O que faz |
|---------|-----------|
| `/ingest` | Processa fontes novas → cria/atualiza artigos wiki |
| `/ask` | Responde perguntas com retrieval em 3 camadas + citação |

## Princípios

- **raw/ é imutável** — fontes nunca são editadas
- **Wiki é hint, não verdade** — se contradiz raw/, raw/ vence
- **Index = ponteiros** — conhecimento vive nos artigos, não no índice
- **Se é derivável, não persista** — não armazene o que pode ser recalculado
- **1 conceito = 1 arquivo** — granularidade por conceito, não por fonte
