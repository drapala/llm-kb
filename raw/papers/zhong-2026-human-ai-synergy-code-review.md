# Human-AI Synergy in Agentic Code Review

**Autores:** Suzhen Zhong, Shayan Noei, Ying Zou, Bram Adams
**Instituição:** Queen's University, Kingston, CA
**Publicação:** arXiv:2603.15911 [cs.SE]
**Ano:** 2026 (março)
**URL:** https://arxiv.org/abs/2603.15911
**Tipo:** paper / primary

---

## Metodologia

- **278.790 conversações** de code review analisadas
- **300 projetos open-source** no GitHub
- Comparação entre feedback de reviewers humanos e agentes AI
- Análise de: padrões de colaboração, taxa de adoção de sugestões, impacto na qualidade do código

## Achados principais

### Diferenças de conteúdo no feedback

| Dimensão | Agentes AI | Revisores Humanos |
|----------|-----------|-------------------|
| Foco principal | >95% em code improvement + defect detection | Inclui understanding, testing, knowledge transfer |
| Comprimento dos comentários | Significativamente mais longos | Mais concisos |
| Cobertura contextual | Técnica (sintaxe, bugs) | Técnica + organizacional + pedagógica |

### Taxa de adoção de sugestões

| Tipo de reviewer | Taxa de adoção |
|-----------------|----------------|
| Agentes AI | **16.6%** |
| Revisores humanos | **56.5%** |

Motivos de rejeição de sugestões AI:
- Incorretas (maior causa)
- Abordadas através de fixes alternativos pelos desenvolvedores

### Impacto das sugestões adotadas na qualidade do código

Quando adotadas, sugestões de agentes AI produzem:
- **Maior aumento de complexidade** do código
- **Maior aumento de tamanho** do código
— comparado com sugestões de revisores humanos adotadas

### Comportamento humano ao revisar código gerado por AI

- Revisores humanos trocam **11.8% mais rounds** ao revisar código gerado por AI vs. código escrito por humanos
- Sinal de maior esforço de supervisão necessário para código AI-gerado

## Interpretação dos dados (autores)

"AI agents can scale defect screening, human oversight remains critical for ensuring suggestion quality and providing contextual feedback that AI agents lack."

A baixa taxa de adoção (16.6%) não significa apenas que as sugestões são ruins — parte reflete que desenvolvedores resolvem o problema de outra forma. Mas >50% das sugestões rejeitadas são classificadas como incorretas ou redundantes.

## Limitações

- Dataset limitado a projetos open-source no GitHub (não representa ambientes corporativos fechados)
- Agentes AI analisados não especificados individualmente (mix de ferramentas)
- Não controla por tipo/complexidade de mudança nos PRs
