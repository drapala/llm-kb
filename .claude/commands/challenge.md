# /challenge [artigo]

Avaliação adversarial de um artigo wiki antes de usá-lo como fonte ou publicar.

## Processo

1. **Leia o artigo** indicado pelo usuário (wiki/concepts/nome.md)

2. **Identifique os 3 claims mais fortes** — as afirmações centrais que o artigo faz.

3. **Para cada claim, avalie:**

   a. **Evidência mais fraca:** qual a fonte mais frágil que suporta este claim?
      Se depende de uma única fonte tertiary (tweet, opinião), flag.

   b. **Prior work:** existe trabalho anterior que já cobre isso?
      Verificar nos raw/ sources disponíveis. Se não souber, escrever
      "não verificado — buscar antes de publicar."

   c. **Cenário de falha:** descreva um cenário concreto e plausível onde
      este claim não se sustenta. Se não conseguir imaginar um, o claim
      pode estar excessivamente vago.

   d. **Citação raw verificada:** o claim tem citação rastreável em raw/?
      Se não, marcar como INTERPRETAÇÃO ou ESPECULAÇÃO.

4. **Classifique cada claim:**
   - **SÓLIDO** — 2+ fontes primary concordam, cenário de falha é edge case
   - **PRECISA REVISÃO** — 1 fonte ou interpretação não marcada
   - **ESPECULAÇÃO NÃO MARCADA** — apresentado como fato sem evidência empírica

5. **Verifique seção ## Interpretação:**
   - Existe? Está separada de ## Conteúdo?
   - Claims interpretativos estão na seção certa?

6. **Web search por prior work:**
   Para cada claim central, busque:
   - "[conceito central] agent memory 2024 2025 2026 arxiv"
   - "[conceito central] limitations OR criticism"
   - "[conceito central] benchmark OR evaluation"
   Liste os 3-5 papers mais relevantes que a KB NÃO contém.
   Para cada um: título, URL, qual claim do artigo afeta.
   Se encontrar paper que invalida um claim, marcar como RISCO ALTO.

## Formato de report

```
ARTIGO: [nome]

CLAIM 1: "[texto do claim]"
  Evidência: [fonte mais fraca]
  Prior work: [existe? onde?]
  Cenário de falha: [descrição]
  Citação raw: [confirmada / não encontrada]
  VEREDICTO: SÓLIDO / PRECISA REVISÃO / ESPECULAÇÃO NÃO MARCADA

CLAIM 2: ...

CLAIM 3: ...

CLASSIFICAÇÃO GERAL: PUBLICÁVEL / PRECISA CORREÇÃO / RISCO ALTO
AÇÃO RECOMENDADA: [o que fazer antes de usar como fonte]

PRIOR WORK (web search):
  1. [Título] — URL — afeta claim N — INVALIDA/REFINA/CONFIRMA
  2. ...
```

## Quando rodar

- Antes de citar um artigo de síntese em outputs/ (reports, LinkedIn posts)
- Antes de usar um artigo como base pra novo artigo
- Quando interpretation_confidence é medium ou low
- Quando /review flagga over-synthesis

## Log de occurrent

Salve resultado em `outputs/logs/sessions/YYYY-MM-DD/challenge-[artigo]-HH-MM.md`
segundo schema em `wiki/meta/process-log.md`.
Campos: claims_challenged, claims_survived, claims_weakened, claims_invalidated,
prior_work_found, verdict.
