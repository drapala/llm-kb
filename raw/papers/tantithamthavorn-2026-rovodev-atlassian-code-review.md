# RovoDev Code Reviewer: Large-Scale Online Evaluation of LLM-based Code Review at Atlassian

**Autores:** Kla Tantithamthavorn, Yaotian Zou, Andy Wong, Michael Gupta, Zhe Wang, Mike Buller, Ryan Jiang, Matthew Watson, Minwoo Jeong, Kun Chen, Ming Wu
**Instituição:** Monash University + Atlassian
**Publicação:** arXiv:2601.01129 [cs.SE, cs.AI, cs.CL, cs.LG]
**Ano:** 2026 (janeiro)
**URL:** https://arxiv.org/abs/2601.01129
**Tipo:** paper / primary

---

## Metodologia

- Deployment em produção na **Atlassian** (Bitbucket)
- Avaliação por **1 ano** (offline + online + user feedback)
- Sem fine-tuning — apenas prompting e RAG
- Design question central: "como projetar review-guided, context-aware, quality-checked code review sem fine-tuning?"

## Arquitetura: RovoDev

- **Review-guided:** estrutura o review segundo padrões observados em code reviews históricos
- **Context-aware:** RAG para montar contexto relevante para o diff específico
- **Quality-checked:** filtering de comentários de baixa qualidade antes de enviar ao developer

Abordagem sem fine-tuning é deliberada: permite atualizar o modelo base sem custo de retreinamento.

## Achados principais

### Métricas de impacto

| Métrica | Valor |
|---------|-------|
| Code resolution rate | **38.70%** (comentários que levaram a mudança de código) |
| PR cycle time | **−30.8%** |
| Human-written comments | **−35.6%** |

### Interpretação dos números

- Code resolution 38.70%: quase 2× a taxa de adoção de CRAs típicos (16.6% de Zhong 2026)
- Redução de PR cycle time contraria Cihan 2024 (+42%) — diferença provavelmente na qualidade do filtering de comentários
- Redução de comentários humanos sugere que devs confiam nas sugestões e não precisam adicionar as próprias

## O que diferencia RovoDev das ferramentas genéricas

1. **Context assembly via RAG** — não injeta contexto completo, recupera o relevante
2. **Quality gate antes do output** — filtra antes de mostrar (similar ao ReviewFilter do BitsAI-CR)
3. **Review-guided structure** — formato do output espelha como humans revisam, não apenas lista de issues

## Ligação com atenção diluída (SWE-PRBench)

RovoDev confirma a hipótese de SWE-PRBench via arquitetura: não injeta contexto bruto — usa RAG para selecionar contexto mínimo relevante. Resultado: melhor performance do que abordagens com contexto completo.

## Limitações

- Resultados específicos para Atlassian/Bitbucket
- Sem fine-tuning pode limitar performance em codebases muito específicos
- 1-year period pode incluir efeitos de novelty bias nos primeiros meses
- Métricas de "resolution" e "cycle time" podem ser confundidas por mudanças de processo paralelas
