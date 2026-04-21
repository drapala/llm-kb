# The Evolution of Technical Debt from DevOps to Generative AI: A Multivocal Literature Review

**Autores:** Sergio Moreschini, Elvira-Maria Arvanitou, Elisavet-Persefoni Kanidou, Nikolaos Nikolaidis, Ruoyu Su, Apostolos Ampatzoglou, Alexander Chatzigeorgiou, Valentina Lenarduzzi  
**Publicação:** Journal of Systems and Software (JSS), Vol. 231  
**Ano:** Janeiro 2026  
**DOI:** https://www.sciencedirect.com/science/article/pii/S0164121225002687  
**Tipo:** paper / secondary (multivocal literature review — combina fontes peer-reviewed e grey literature)

---

## Metodologia

- **61 fontes primárias** analisadas (combinação de literatura acadêmica e fontes da indústria)
- Multivocal literature review (MLR): inclui sistematicamente grey literature (blogs, reports, white papers) além de papers acadêmicos
- Foco: como Technical Debt Management (TDM) precisa se adaptar no contexto de AI-enhanced development

## Novos tipos de dívida identificados

### Prompt Debt
Dívida acumulada em prompts mal-estruturados, inconsistentes ou não-versionados usados para interagir com LLMs. Características:
- Prompts ad-hoc sem controle de versão
- Inconsistência entre prompts em diferentes partes do sistema
- Ausência de testes de prompt
- Degradação silenciosa de comportamento quando modelo muda

### Explainability Debt
Dívida acumulada na incapacidade de explicar por que componentes AI tomam determinadas decisões. Inclui:
- Modelos sem documentação de decisão
- Ausência de interpretabilidade para reguladores ou usuários
- Dependência de comportamentos emergentes não-documentados

### AI Technical Debt (ATD) — framework expandido
O paper mapeia como dívidas já conhecidas (de Sculley et al. 2015) se manifestam diferentemente com GenAI:
- Data debt → agora inclui dívida em dados de treinamento de prompts
- Infrastructure debt → inclui dependência em APIs de LLM externas
- Governance debt → compliance e explicabilidade de decisões AI

## Conclusão principal

TDM precisa se adaptar especificamente para GenAI: as ferramentas e métricas de technical debt desenvolvidas para código convencional são insuficientes para capturar as formas emergentes de dívida introduzidas por AI. "Prompt debt" e "explainability debt" têm little formal support nas ferramentas existentes.

## Limitações

- MLR inclui grey literature — qualidade heterogênea das 61 fontes
- Conceitos de "prompt debt" e "explainability debt" são emergentes e ainda sem operacionalização empírica robusta
