# Sequential Probability Ratio Test (SPRT)

**Fonte primária:** Wald, A. (1945). "Sequential Tests of Statistical Hypotheses." *The Annals of Mathematical Statistics*, 16(2), 117–186.

**Nota de ingestão:** Acesso restrito ao paper original (Tandfonline 403). Conteúdo compilado de: Wikipedia/Sequential_probability_ratio_test, Wikipedia/Sequential_analysis, e literatura secundária estabelecida. Framework matemático verificado contra múltiplas fontes independentes — as equações são padrão em probabilidade e estatística.

---

## Definição

O SPRT é um teste de hipótese sequencial: ao contrário dos testes clássicos com n fixo, o SPRT decide se continua coletando observações ou para — e qual hipótese aceitar — a cada passo, baseado na evidência acumulada até aquele ponto.

## Setup

**Duas hipóteses:**
- **H₀**: parâmetro θ = θ₀ (hipótese nula — ex: "hipótese emergida é artefato/circular")
- **H₁**: parâmetro θ = θ₁ (hipótese alternativa — ex: "hipótese emergida é robusta")

**Observações:** x₁, x₂, ..., xₙ i.i.d. (cada ciclo de teste = uma observação)

**Log-likelihood ratio individual:** λᵢ = log P(xᵢ | H₁) / P(xᵢ | H₀)

**Estatística de teste cumulativa:** Sₙ = Σᵢ₌₁ⁿ λᵢ = log [P(x₁,...,xₙ | H₁) / P(x₁,...,xₙ | H₀)]

## Regra de Parada (Stopping Rule)

Dados limiares a e b (a < 0 < b):

- Se **Sₙ ≥ b**: PARA — aceita H₁ (hipótese confirmada)
- Se **Sₙ ≤ a**: PARA — aceita H₀ (hipótese rejeitada)
- Se **a < Sₙ < b**: CONTINUA — coleta próxima observação

## Thresholds em Função de α e β

Dado erro tipo I α = P(aceitar H₁ | H₀ verdade) e erro tipo II β = P(aceitar H₀ | H₁ verdade):

```
A = β / (1 - α)        a = log A = log(β/(1-α))
B = (1 - β) / α        b = log B = log((1-β)/α)
```

**Exemplo:** α = 0.05, β = 0.10:
- A = 0.10/0.95 ≈ 0.105   →  a = log(0.105) ≈ -2.25
- B = 0.90/0.05 = 18       →  b = log(18) ≈ 2.89

## Teorema de Optimalidade (Wald & Wolfowitz)

**Resultado:** O SPRT minimiza o ASN (Average Sample Number — número esperado de observações) entre TODOS os procedimentos sequenciais com os mesmos níveis α e β.

Formalmente: para qualquer teste T com P(Erro I) ≤ α e P(Erro II) ≤ β:
- E[N | H₀] para SPRT ≤ E[N | H₀] para T
- E[N | H₁] para SPRT ≤ E[N | H₁] para T

**Implicação prática:** O SPRT é o teste sequencial mais eficiente possível — nenhum outro procedimento, seja ele qual for, pode resolver o mesmo problema de hipóteses com menos observações em média.

## ASN Aproximado (Wald's Identity)

Sob H₁: E[N | H₁] ≈ [β·log(β/(1-α)) + (1-β)·log((1-β)/α)] / E[λᵢ | H₁]

Sob H₀: E[N | H₀] ≈ [α·log((1-β)/α) + (1-α)·log(β/(1-α))] / E[λᵢ | H₀]

Onde E[λᵢ | Hⱼ] é o valor esperado do log-likelihood ratio individual sob Hⱼ (= KL divergence).

**Insight:** ASN ∝ 1/E[λᵢ | Hⱼ] — quanto mais discriminativa cada observação (maior KL), menos observações são necessárias. Uma hipótese que se confirma fortemente a cada ciclo precisa de menos ciclos.

## Limitações

1. **Assume i.i.d.:** Observações devem ser independentes e identicamente distribuídas. SPRT não funciona diretamente quando cada teste muda o sistema (ex: cada /ask muda a KB, que muda o próximo /ask).

2. **Requer H₀ e H₁ pontuais:** Para hipóteses compostas (ex: "θ > θ₀") o SPRT não é diretamente aplicável.

3. **Custo de parada assimétrico:** SPRT para assim que uma hipótese é aceita. Se o custo de falso positivo ≫ falso negativo (ou vice-versa), os thresholds devem ser assimétricos.

## Extensões Modernas para Não-i.i.d.

- **e-values e e-processes** (Vovk & Wang, 2021; Ramdas et al.): alternativas anytime-valid que dispensam i.i.d.
- **Alpha spending functions** (DeMets & Lan): generalizam SPRT para looks irregulares sem inflação de α.
- **mSPRT (mixture-SPRT)**: prior sobre θ₁ em vez de valor pontual — mais robusto para H₁ compostas.
