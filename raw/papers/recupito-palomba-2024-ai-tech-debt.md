# Technical Debt in AI-Enabled Systems: On the Prevalence, Severity, Impact, and Management Strategies for Code and Architecture

**Autores:** Gilberto Recupito, Fabiano Pecorelli, Gemma Catolino, Valentina Lenarduzzi, Davide Taibi, Dario Di Nucci, Fabio Palomba  
**Publicação:** Journal of Systems and Software (JSS), Vol. 216  
**Ano:** 2024  
**DOI:** https://www.sciencedirect.com/science/article/pii/S0164121224001961  
**Tipo:** paper / secondary (survey com practitioners)

---

## Metodologia

- **53 AI developers** (practitioners)
- Survey sobre características de AI Technical Debt (AITD): prevalência percebida, severidade, impacto, estratégias de gerenciamento
- Foco em dívida de código e arquitetura em sistemas AI-enabled

## Achados principais

### Paradoxo prevalência/severidade
| Dimensão | Avaliação dos practitioners |
|----------|----------------------------|
| Prevalência percebida | **Baixa** |
| Severidade percebida | **Alta** |

Interpretação: AITD não ocorre frequentemente, mas quando ocorre tem impacto severo.

### Impacto nas dimensões de qualidade
AITD impacta especialmente:
1. **Understandability** — sistemas AI são difíceis de entender e auditar
2. **Security** — componentes AI introduzem riscos de segurança não tradicionais

### Estratégias de gerenciamento atuais (emergentes, ad-hoc)
- Manual review — revisão humana de componentes AI
- Ad-hoc refactoring — correção reativa, não sistemática
- Ausência de ferramentas especializadas — practitioners usam ferramentas tradicionais de code quality inadequadas para AI-specific debt

## Taxonomia de AITD implícita no paper

1. **Model debt** — modelos desatualizados, não-monitorizados
2. **Data debt** — qualidade de dados de treino, data drift
3. **Infrastructure debt** — dependências frágeis em frameworks ML
4. **Process debt** — ausência de MLOps, CI/CD para modelos
5. **Architecture debt** — integração de AI sem separação limpa de concerns

## Relação com Sculley et al. (2015)

Recupito & Palomba atualizam e especializam o framework de Sculley para o contexto de AI-enabled systems (sistemas que *usam* AI, não apenas sistemas de ML). A fronteira é relevante: sistemas que chamam APIs de LLM têm formas de dívida não cobertas pelo framework de 2015.
