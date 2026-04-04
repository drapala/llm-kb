---
title: "Corruption Audits and Electoral Accountability (Ferraz & Finan 2008)"
sources:
  - path: raw/papers/ferraz-finan-2008-exposing-corrupt-politicians.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [corruption, procurement, brazil, b2g, accountability, information-asymmetry, electoral, empirical]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: null
quarantine: false
---

## Resumo

Ferraz & Finan (2008) usam auditoria aleatória de municípios brasileiros pelo CGU (programa Lula, 2003) para identificar causalmente o efeito de divulgar corrupção sobre accountability eleitoral. Resultado: a divulgação de auditorias pré-eleição reduziu a probabilidade de reeleição de prefeitos corruptos em até 17-28 pontos percentuais, efeito amplificado por rádio local. Os eleitores atualizam suas crenças bayesianamente quando recebem a informação. QJE 2008.

## Conteúdo

### Contexto institucional: Programa CGU

Em maio de 2003, o governo Lula iniciou programa de auditoria aleatória de gastos municipais de verbas federais. A Controladoria Geral da União (CGU) sorteia municípios mensalmente (junto à loteria nacional, para transparência), audita 2001-2003, e divulga resultados publicamente à mídia.

**Escala:** O programa seleciona amostras de municípios com menos de 450.000 habitantes (≈92% dos 5.500 municípios brasileiros; ≈73% da população total). Auditores: contratados por concurso público, salários competitivos, extenso treinamento, sempre acompanhados por supervisor. As 13 primeiras loterias produziram relatórios para 669 municípios.

**Definição de corrupção operacionalizada:**
- *Procurement irregular:* ausência de chamada pública, mínimo de licitantes não atingido, evidência de fraude (propostas de firmas inexistentes)
- *Desvio de recursos públicos:* qualquer gasto sem comprovação de compra ou provisão
- *Superfaturamento:* compra de bens/serviços acima do preço de mercado

### Dados e amostra

373 municípios com prefeitos de primeiro mandato elegíveis à reeleição (dos 669 com relatórios disponíveis até julho 2005).

**Grupo de tratamento:** 205 municípios auditados *antes* das eleições de outubro 2004.
**Grupo de controle:** 168 municípios auditados *depois* das eleições.

**Estatísticas descritivas de corrupção:**
- 73% dos municípios na amostra tinham ao menos 1 incidente de corrupção reportado
- Média: 1,74 violações por município
- Distribuição balanceada entre tratamento e controle (diferença não significativa a 10%)

**Características municipais:** Renda per capita média R$204/mês (≈US$81, abaixo do salário mínimo de R$240); 38% da população em áreas rurais; 21% do adultos analfabetos; rádio AM presente em 27% dos municípios; 79% dos domicílios possuem rádio.

**Exemplos concretos de corrupção dos relatórios:**
- São Francisco do Conde (BA): firma Mazda contratada sem licitação para construção de estrada de 9 km, estimativa R$1M; recibos pagos R$5M; firma sem experiência em construção, subcontratou por R$1,8M. Overprice: >R$3M. A firma posteriormente deu um apartamento de R$600k ao prefeito e sua família.
- Capelinha (MG): Ministério da Saúde transferiu R$321.700 para programa de saúde básica; governo municipal usou recibos falsos de R$166k de compra de medicamentos; mercadorias nunca encontradas em estoque.

### Estratégia empírica

Modelo reduzido de forma:
```
E_ms = α + β·A_ms + X_ms·γ + v_s + ε_ms
```
Onde `A_ms` = indicador para auditoria pré-eleição. `β` captura o efeito médio causal da política. Porque a seleção é aleatória, `β` é estimativa não-viesada.

Para capturar heterogeneidade por nível de corrupção e presença de mídia:
```
E_ms = α + β₀C_ms + β₁A_ms + β₂(A_ms × C_ms) + X_ms·γ + v_s + ε_ms
```
`β₂` captura o efeito causal condicional ao nível de corrupção.

### Resultados principais

**Efeito médio (Tabela II):** Não significativo — a auditoria reduziu probabilidade de reeleição em apenas 3,6pp (SE=0,053), não distinguível de zero. O programa não teve efeito médio detectável.

**Por nível de corrupção (Tabela III, Figura III):**

Municípios auditados pré-eleição mostram sharp downward-sloping relationship entre reeleição e corrupção; controles mostram relação plana (≈40% em todos os níveis).

| Violações | Efeito em Pr(reeleição) | Significância |
|-----------|------------------------|---------------|
| 0 violações | +17pp (incumbente recompensado) | — |
| 1 violação | −4,6pp | p=.45 |
| 2 violações | −17,7pp | F(1,348)=4,93; p=.03 |
| 3+ violações | Ainda maior | — |

Interpretation: eleitores têm prior médio de ≈1 violação. Quem revelou menos do que esperado é recompensado; quem revelou mais é punido.

**Efeito da mídia local — Rádio AM (Tabela VI, Figura IV):**

| Condição | Efeito em Pr(reeleição) |
|----------|------------------------|
| 3 violações, sem rádio | −3,7pp |
| 3 violações, 1 rádio AM | −16,1pp (F(1,324)=2,81; p=.09) |
| 3 violações, rádio (excluindo outliers) | −29pp |
| 0 violações, com rádio | +17pp (incumbente honesto recompensado) |

O rádio amplifica o efeito do audit em ambas as direções: pune os corruptos mais severamente E recompensa os honestos mais fortemente. Resultado robusto a controles demográficos, institucionais, e à medida alternativa de penetração de rádio (% domicílios com rádio).

**Robustez (Tabela V):**
- Não há evidência de manipulação das auditorias por afiliação política (coeficiente −0,155, SE=0,256 para mesmo partido do governador)
- Placebo: auditorias não afetam resultados eleitorais de 2000 (estimativas próximas a zero)
- Resultados robustos a controle para nível de corrupção da eleição anterior

### Mecanismo identificado

Eleitores atualizam bayesianamente: corrupção revelada só altera voto quando *supera* o prior do eleitor. A disseminação via rádio é crítica: municípios sem rádio têm ponto de crossover em ≈0 violações (qualquer revelação pune o incumbente); com rádio, o prior é de ≈1 violação, refletindo melhor informação de base.

### Natureza da corrupção em procurement municipal

Esquemas típicos combinam três elementos:
1. **Fraude em procurement:** beneficiar empresa amiga com insider information sobre valor do projeto; impor restrições que limitam competidores (ex: Caculé/BA: esporte complex exigiu R$100k de capital mínimo — só uma firma qualificou, a que pagou propina)
2. **Desvio de recursos:** despesas sem comprovação (phantom firms, recibos falsos)
3. **Superfaturamento:** notas acima do preço de mercado

Esses elementos são complementares (não excludentes) — por isso somam num único índice.

## Interpretação

⚠️ Interpretação do compilador — não está em Ferraz & Finan nesta forma.

**Implicação para Risk Score de procurement:** O paper documenta empiricamente que *violações em procurement são detectáveis e mensuráveis* via auditoria — e que eleitores respondem a elas. Para um sistema de risk scoring:

1. As formas de corrupção documentadas (ausência de licitação, firmas inexistentes, superfaturamento) são exatamente os padrões identificáveis em dados de PNCP/CGU
2. O threshold de 2-3 violações como sinal confiável é análogo ao threshold de confiança em modelos de anomalia
3. O efeito não-linear (0 violações → recompensa; 2+ → punição) sugere que o prior de "corrupção esperada" é informativamente um baseline — desvios do baseline são o sinal, não o nível absoluto

**B2G:** Municípios com auditorias CGU reveladas são cases de ground truth de corrupção em procurement público. Os padrões documentados (contratos sem licitação, additive contracts, phantom firms) mapeiam diretamente para sinais detectáveis em dados de compras públicas.

## Verificação adversarial

**Ameaças à identificação:**
1. Auditorias pré-eleição mais intensas? → Autores mostram balanceamento da distribuição de corrupção entre grupos
2. Prefeitos corruptos pré-eleição alteram estratégia de campanha? → O timing (meses antes, não dias) torna improvável
3. Rádio captura educação/população? → Robusto a interações com densidade, literacy, urbanização

**O que o paper NÃO diz:**
- Não fornece evidência de que auditorias *previnem* corrupção futura (só impacto eleitoral)
- Não modela procurement em nível de contrato (unidade = município)
- A medida de corrupção é contagem de violações, não valor monetário desviado

## Conexões

- [[market-for-lemons]] ON "assimetria de informação entre governo-comprador e fornecedor; auditorias como mecanismo de sinalização"
- [[information-asymmetry-b2g]] ON "evidência empírica de formas de corrupção em procurement municipal brasileiro"
- [[autonomous-kb-failure-modes]] ON "exemplo de sistema (político) que funciona melhor com informação externa (auditoria) do que com auto-avaliação"

## Fontes

- [Ferraz & Finan (2008)](../../raw/papers/ferraz-finan-2008-exposing-corrupt-politicians.pdf) — Quarterly Journal of Economics, Vol. 123, No. 2, pp. 703-745. Modelo empírico, Tabelas II-VI, definição de corrupção, dados CGU, mecanismo bayesiano.
