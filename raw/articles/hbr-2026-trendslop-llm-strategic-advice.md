# HBR 2026 — "Researchers Asked LLMs for Strategic Advice. They Got 'Trendslop' in Return"

**Autores:** Angelo Romasanta, Llewellyn D.W. Thomas, Natalia Levina  
**Publicado:** Harvard Business Review, 16 de março de 2026  
**URL:** https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return

## Conceito Central

**"Trendslop"** (definição dos autores): propensão de LLMs em escolher ideias chamativamente populares em vez de soluções fundamentadas em lógica contextual. Em estratégia empresarial: "strategy trendslop" — LLMs recomendam abordagens alinhadas com buzzwords gerenciais contemporâneos, não com análise contextual específica da organização.

## Metodologia

**LLMs testados:** 7 — ChatGPT, Claude, DeepSeek, GPT-5 (via API), Gemini, Grok, Mistral  
**Estrutura:** 7 tensões estratégicas binárias, cada uma com dois polos opostos  
**Simulações para GPT-5:** >15.000 testes de variação de prompt + >15.000 testes de contexto organizacional  
**Medição:** preferência média por polo em 50 execuções por condição, escala 0-100%

**7 tensões estratégicas testadas:**
1. Exploração vs. Exploração (novos mercados vs. eficiência)
2. Centralização vs. Descentralização
3. Curto prazo vs. Longo prazo
4. Competição vs. Colaboração (coopetição)
5. Inovação radical vs. Incremental
6. Diferenciação vs. Comoditização (custo-liderança)
7. Automação vs. Aumento (augmentation)

**Variações de prompt testadas:**
- Ordem de apresentação das opções
- Enquadramento (mudança de perspectiva)
- Demanda por análise de prós e contras
- Manipulação de incentivos

**Variações de contexto organizacional:**
- Multinacionais, startups de tecnologia, setor bancário, saúde, ONGs
- Níveis variáveis de detalhe descritivo

## Resultados

**Vieses consistentes entre todos os 7 modelos:**
- Diferenciação sobre comoditização/custo-liderança: preferência "manifesta", agrupamento apertado entre modelos
- Aumento (augmentation) sobre automação: preferência consistente
- Longo prazo sobre curto prazo: viés "quase universal"

**Efetividade de melhor prompting:**
- Para diferenciação e aumento: redução de <2% nas respostas enviesadas
- Para outras 5 tensões: deslocamento de ~22% da linha de base
- Mudança de ordem de opções apenas: redução de 19%

**Efetividade de contexto organizacional detalhado:**
- Deslocamento médio de apenas 11% da linha de base
- "Às vezes aumentando e às vezes diminuindo o viés" — inconsistente

**Agrupamento entre modelos:** os 7 LLMs exibem preferências similares — não é artefato de um modelo específico.

## Conclusões dos Autores

- LLMs têm "visão de mundo moldada pelo que soa bem no discurso gerencial contemporâneo"
- Recomendação: usar LLMs "para expandir opções, não para fazer escolhas"
- "Julgamento final firmemente nas mãos humanas"
- "Liderança é fundamentalmente sobre fazer escolhas difíceis em condições de incerteza — a IA não pode e não deve ser substituta"

## Limitações Admitidas

- Vieses podem mudar com atualizações de modelo → desafio de monitoramento contínuo
- Sensibilidade à sequência de opções sugere variância aleatória, não julgamento
- Contexto detalhado não consegue desalojar vieses fundamentais
- Não testado com domínios altamente técnicos (apenas tensões estratégicas de gestão geral)
