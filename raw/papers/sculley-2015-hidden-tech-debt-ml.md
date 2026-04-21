# Hidden Technical Debt in Machine Learning Systems

**Autores:** D. Sculley, Gary Holt, Daniel Golovin, Eugene Davydov, Todd Phillips, Dietmar Ebner, Vinay Chaudhary, Michael Young, Jean-Francois Crespo, Dan Dennison  
**Publicação:** Advances in Neural Information Processing Systems (NeurIPS), Vol. 28  
**Ano:** 2015  
**URL:** https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html  
**Tipo:** paper / primary (paper fundacional — Google)

---

## Tese central

Código de ML em produção é rodeado de "glue code" e dívidas escondidas que são invisíveis a métricas tradicionais. A proporção de código real de ML num sistema ML típico é frequentemente pequena; a maioria do código é infraestrutura ao redor.

## As formas de dívida identificadas

### 1. Entanglement (Changing Anything Changes Everything — CACE)
Mudar qualquer feature de input, threshold, ou hiperparâmetro pode alterar o comportamento de todo o sistema. Isolamento é difícil. Debugging é difícil.

### 2. Hidden Feedback Loops
Modelos que influenciam o mundo ao redor mudam os dados com os quais serão retreinados. Loop de feedback fechado não-intencional e frequentemente não-monitorado.

### 3. Undeclared Consumers
Outros sistemas consomem outputs do modelo sem declaração formal de dependência. Mudanças no modelo quebram silenciosamente outros sistemas.

### 4. Data Dependencies
Dependências em dados externos são mais frágeis que dependências de código:
- **Unstable data dependencies:** features de outras equipes que podem mudar
- **Underutilized data dependencies:** features que contribuem pouco mas aumentam complexidade

### 5. Configuration Debt
Sistemas ML têm enormes espaços de configuração (hiperparâmetros, thresholds, feature flags). Configurações mudam frequentemente e raramente são versionadas, testadas ou revisadas.

### 6. Glue Code
Sistemas ML em produção são frequentemente 5% ML e 95% "glue code" — wrappers, adaptadores, conversores — que não é testado com rigor equivalente ao código de negócio.

### 7. Pipeline Jungles
Acumulação de preprocessing steps ad-hoc que ninguém entende completamente. Frequentemente resultado de experimentação não-limpa.

### 8. Dead Experimental Codepaths
Experimentos passados deixam código condicional que nunca é ativado. Acumula complexidade sem valor.

### 9. Abstraction Debt
Abstrações inadequadas para ML: falta de tipos fortes para tensors, lack de invariants verificáveis, interfaces frágeis.

### 10. ML-Specific Anti-Patterns
- **Plain-Old-Data type smell:** features com nomes genéricos sem semântica
- **Multiple Language smell:** usar linguagens diferentes para treino e serviço
- **Prototype smell:** código de prototipagem que entra em produção

## Por que é "hidden"

Technical debt em ML é escondida porque:
1. Métricas de qualidade tradicionais (testes, linting) não capturam acoplamento semântico
2. Modelo pode funcionar bem localmente mas ter dívida sistêmica
3. Degradação é frequentemente gradual e não-óbvia até um ponto de ruptura

## Status como fonte fundacional

Este paper cunhou o vocabulário ("glue code", "pipeline jungles", "undeclared consumers") que toda a literatura posterior de AI technical debt usa. É a referência obrigatória de qualquer taxonomia de dívida em sistemas de ML.

## Relevância para GenAI (2025+)

Todos os problemas de Sculley se aplicam com intensidade amplificada em sistemas que usam LLMs:
- Undeclared consumers: outros sistemas dependendo de outputs de LLM via API
- Configuration debt: gestão de prompts como configuração não-versionada (→ "prompt debt" de Moreschini)
- Pipeline jungles: chains de prompts e RAG pipelines ad-hoc
- Hidden feedback loops: outputs de LLM usados para retreinar ou avaliar LLMs
