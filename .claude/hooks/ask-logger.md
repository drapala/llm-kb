# Ask Logger

## Quando ativa

Ao final de TODA sessão /ask, antes de encerrar.

## O que captura

### 1. QUERY
Salve a pergunta exata que foi feita.

### 2. ARTICLES READ
Liste todos os artigos wiki/ lidos durante a sessão. Inclua artigos lidos mas não usados na resposta final — esses são dados de retrieval tão valiosos quanto os usados.

### 3. RAW SOURCES VERIFIED
Liste todos os raw/ consultados para verificação de claims (Layer 3).

### 4. RETRIEVAL GAPS
Após gerar a resposta, pergunte:
"Quais artigos wiki existentes DEVERIAM ter sido consultados para esta query mas não foram? Por quê não foram encontrados?"

Isso é o sinal mais valioso — identifica falhas de retrieval antes que causem erros em sínteses futuras. Um padrão de misses indica que _index.md excedeu a capacidade de seleção.

### 5. CONFIDENCE
HIGH — todos os claims verificados em raw/
MEDIUM — maioria verificada, alguns inferidos
LOW — síntese especulativa, poucos claims verificados

### 6. SYNTHESIS TYPE
| Tipo | O que responde |
|------|---------------|
| ASSOCIATION | o que X e Y têm em comum |
| CONTRADICTION | onde X e Y divergem |
| GAP | o que nenhum resolve |
| MECHANISM | como X causa Y |
| SCALE | em que condições X funciona/falha |
| ABDUCTION | melhor explicação para anomalia Z |
| FRONTIER | limites de aplicabilidade |
| ABSENCE | o que ninguém perguntou |
| FALSIFICATION | o que refutaria este claim |
| SUFFICIENCY | isto é bom o suficiente pra agir? |

## Formato do log

Salve em `outputs/logs/sessions/YYYY-MM-DD/ask-HH-MM.md`

```markdown
# Ask Session Log
date: YYYY-MM-DD HH:MM
query: "[pergunta exata]"
synthesis_type: [tipo]
confidence: high|medium|low

## Articles read
- wiki/concepts/[artigo].md — [usado na resposta / lido mas não usado]

## Raw sources verified
- raw/papers/[paper].md — [claim verificado]

## Retrieval gaps
- [artigo que deveria ter sido lido]: [por que não foi encontrado]

## Response summary
[2-3 linhas do que foi respondido]

## Follow-up flags
- [algo que ficou sem resposta e merece /ask dedicado]
- [claim que deveria ser /challenged]
```
