# TSR Oficial do Brasil — AA40 (2025, 2026)

**Fonte:** AA40 — Aposente aos 40 (aposenteaos40.org)
**Publicações:**
- 2025: "A primeira taxa segura de retirada (TSR) oficial do Brasil" (jan/2025)
- 2026: "2026: Atualização anual da taxa segura de retirada no Brasil" (jan/2026)
**Tipo:** análise quantitativa com dados históricos (não-acadêmica, mas metodologia replicável)

## Contexto

A AA40 é a principal comunidade FIRE (Financial Independence, Retire Early) do Brasil. Esta análise representa o primeiro cálculo sistemático da TSR (Taxa Segura de Retirada) com dados históricos completos do Plano Real.

## Metodologia

- Simulação de declaração de FIRE em janeiro de 1995 com R$ 1 milhão
- Saques anuais, reajustados pelo IPCA
- Horizonte: 30 anos
- Índices usados: IBOVESPA (renda variável), CDI/Selic (renda fixa)
- TSR SafeMax = maior taxa que não zerou o portfólio em nenhum período testado
- PWR (Perpetual Withdrawal Rate) = taxa que preserva o capital real

## Dados Históricos Utilizados

- Período base: 1995–2024 (30 anos completos do Plano Real)
- Atualização 2026: adiciona janela 1996–2025, mantém TSR pelo pior período

### Retornos históricos médios (1995–2024):
- IBOVESPA: -10,36% ao ano (em USD real — em BRL nominal é positivo, mas em termos reais ajustados é adverso em certos períodos)
- IPCA (inflação): +4,83% ao ano
- Selic média: 10,8% ao ano

### 2025 (dados para atualização 2026):
- IBOVESPA: +33,95%
- CDI/Selic médio: 14,5%
- IPCA: 4,26%

## Resultados — TSR SafeMax por Alocação

| Alocação | TSR 2024 (29 anos) | TSR 2025 (30 anos) | TSR 2026 (mantida) |
|----------|-------------------|-------------------|-------------------|
| 100% Ibovespa | 7,16% | 7,29% | 7,29% |
| 50% Ibov / 50% Selic | 8,30% | **8,48%** | **8,48%** |
| 100% Selic/CDI | 9,21% | 9,34% | 9,34% |
| Poupança (ref.) | 5,17% | — | — |

## PWR — Perpetual Withdrawal Rate (capital preservado)

| Alocação | PWR |
|----------|-----|
| 50% Ibov / 50% Selic | **6,93%** |

## Simulação Monte Carlo (adicionada em 2026)

Com 95% de probabilidade de sucesso:
- TSR máxima segura: **3,69% a 4,5%** (dependendo das premissas)
- Cenário mediano: crescimento expressivo do patrimônio na maioria dos cenários

## Interpretação dos Autores

- O TSR de 8,48% NÃO deve ser usado diretamente no planejamento — é dado histórico de um único ciclo
- A regra dos 4% americana é segura para o Brasil (está bem abaixo do TSR histórico)
- Monte Carlo a 95% de sucesso converge para 3,69-4,5%, mais próximo do conservadorismo americano
- Diversificação geográfica (ativos internacionais) é recomendada além da carteira doméstica

## Limitações Declaradas

- Apenas um ciclo histórico de 30 anos disponível (vs. 109 anos dos EUA no estudo de Pfau)
- Período 1995-2004 inclui juros reais excepcionalmente altos — dificilmente repetíveis
- Selic de dois dígitos é anomalia estrutural em declínio secular
- Imposto de renda não completamente incorporado
- Risco-país e instabilidade fiscal não capturados pelo histórico
