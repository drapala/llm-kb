# Comprehension Debt: The Hidden Cost of AI-Generated Code

**Autor:** Addy Osmani (Google Chrome Engineer)  
**Publicação:** addyosmani.com / Medium  
**Ano:** Março 2026  
**URL:** https://addyosmani.com/blog/comprehension-debt/  
**Tipo:** article / secondary (ensaio com dados empíricos citados)

---

## Definição

**Comprehension debt:** o gap crescente entre o volume de código que existe no sistema e o volume que qualquer engenheiro humano genuinamente entende.

Diferente de technical debt tradicional:
- Testes passam ✓
- Sintaxe está limpa ✓
- O modelo mental coletivo do sistema se erode silenciosamente ✗

É uma dívida que não aparece nos dashboards de qualidade. É deceptiva porque gera **falsa confiança**.

## Evidência empírica citada: Anthropic RCT

**Estudo:** "How AI Impacts Skill Formation" (Anthropic)  
**N:** 52 engenheiros de software aprendendo uma nova biblioteca

| Grupo | Tempo de conclusão | Score no quiz de compreensão |
|-------|-------------------|-----------------------------|
| Controle (sem AI) | similar | 67% |
| AI-assistido | similar | **50%** |
| **Diferença** | ~mesmo tempo | **-17 pontos percentuais** |

Maior queda: debugging (-maiores quedas). Menores mas significativas: compreensão conceitual e leitura de código.

Insight chave: "passive delegation ('just make it work') impairs skill development far more than active, question-driven use of AI."

## A inversão da dinâmica de review

Historicamente: senior engineers auditavam código mais rápido do que juniors produziam → review era gatilho de qualidade real.

Com AI: junior developers (e não-técnicos) geram código mais rápido do que engenheiros experientes conseguem avaliar criticamente → review vira **gargalo de throughput**, não gatilho de qualidade.

O volume de output de AI inverteu o diferencial de velocidade que tornava code review eficaz.

## Recomendações de Osmani

1. Tratar compreensão como não-negociável — não apenas testes passando
2. Ser explícito sobre intenção antes de gerar código
3. Usar verificação como constraint estrutural, não afterthought
4. Manter modelos mentais em nível de sistema para capturar erros arquiteturais
5. Distinguir "testes passaram" de "entendo por que isso funciona"

"Making code generation cheap doesn't eliminate the comprehension work — it merely defers the bill."

## Limitações como fonte

- Ensaio jornalístico de alto nível (Google Chrome engineer, respeitado), não paper peer-reviewed
- O Anthropic RCT é citado mas sem DOI/link completo — qualidade do estudo não verificada diretamente
- Comprehension debt é termo novo (março 2026) sem definição operacional ainda

## Relação com outros conceitos

Comprehension debt é a manifestação cognitiva do que Mujahid et al. (2026) chamaram de "Limited Understanding" em GIST — o padrão de dívida mais preocupante do ponto de vista sistêmico.
