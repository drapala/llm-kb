# "TODO: Fix the Mess Gemini Created": Towards Understanding GenAI-Induced Self-Admitted Technical Debt

**Autores:** Abdullah Al Mujahid, Mia Mohammad Imran  
**Publicação:** arXiv:2601.07786  
**Ano:** Janeiro 2026  
**URL:** https://arxiv.org/abs/2601.07786  
**Tipo:** paper / primary

---

## Metodologia

- **6.540 comentários de código** que referenciam LLMs extraídos de repositórios GitHub públicos (Python e JavaScript)
- Período: Novembro 2022 – Julho 2025
- LLMs mencionados: ChatGPT, Copilot, Claude, Gemini
- Critério de inclusão: comentário menciona uso de AI E admite technical debt (SATD — Self-Admitted Technical Debt)
- **81 comentários** classificados como GIST (GenAI-Induced Self-admitted Technical Debt)

## O conceito GIST

**GenAI-Induced Self-Admitted Technical Debt (GIST):** situações onde desenvolvedores incorporam código gerado por AI enquanto expressam explicitamente incerteza sobre seu comportamento ou correção em comentários no próprio código.

Exemplo canônico do título: `// TODO: Fix the mess Gemini created` — desenvolvedor admite dívida, cita o causador.

## Os 3 padrões de GIST encontrados

1. **Postponed Testing** — testes adiados de código gerado por AI
   - Desenvolvedor aceita o código funcionalmente mas não escreve testes ainda
   - Admite explicitamente no comentário que validação está pendente

2. **Incomplete Adaptation** — adaptação incompleta da solução gerada
   - AI produziu solução genérica; adaptação ao contexto específico ficou pendente
   - Código foi commitado com a dívida de adaptação aberta

3. **Limited Understanding** — compreensão limitada do código gerado
   - Desenvolvedor não entende completamente o que o código AI faz
   - Admite isso explicitamente em comentário, frequentemente com TODO

## Achado principal

AI assistance afeta **quando** e **por que** o technical debt emerge:
- *Quando:* dívida emerge mais cedo no ciclo de desenvolvimento (código é commitado antes de estar maduro)
- *Por que:* a dívida está ligada à relação desenvolvedor-código gerado por AI, não apenas a pressão de prazo

## Contexto quantitativo

81/6.540 = 1.24% dos comentários que mencionam AI também admitem dívida. 
Nota: este é lower bound — não captura dívida não-admitida (o iceberg não visível).

## Relevância cruzada

O padrão "Limited Understanding" é o predecessor direto do "comprehension debt" de Osmani (2026) — um conceito popularizado depois que este paper documentou o fenômeno em dados reais.
