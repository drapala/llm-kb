# Meta: Padrões de Uso do /ask

type: note
quality: secondary
date: 2026-04-06
author: drapala

---

## Anti-pattern: Loop Epistêmico Circular
Usar /ask para descobrir como melhorar o próprio sistema
antes de ter corpus sobre o domínio da melhoria.

Sintoma: query sobre X → KB sem corpus de X → 
resposta paramétrica do LLM → parece fundamentada mas não é

Regra: se o corpus sobre o domínio da query é ausente,
/ask retorna gap, não resposta.

## Padrão Correto: Ask com Âncoras
Em vez de: /ask "como faço X?"
Usar:       /ask "dado que preciso de X, 
                  quais conceitos relacionados 
                  estão ausentes no corpus?"

## Padrão: Gap Mapping
/ask pode ser usado para mapear o perímetro do conhecimento
existente — mas só detecta unknown knowns, não unknown unknowns.

Para unknown unknowns, o fluxo correto é:
1. Pesquisa externa (web, papers)
2. Ingestão do corpus relevante
3. /ask fundamentado no novo corpus
