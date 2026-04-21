# Detection of fraud in public procurement using data-driven methods: a systematic mapping study

**Authors:** Everton Schneider dos Santos, Matheus Machado dos Santos, Márcio Castro, Jônata Tyska Carvalho
**Year:** 2025
**Journal:** EPJ Data Science, Volume 14, Article 52 (Springer Nature)
**URL:** https://link.springer.com/article/10.1140/epjds/s13688-025-00569-3
**Type:** Systematic review
**Note:** Conteúdo baseado em abstract e descrição da busca — full text não verificado.

## Abstract / Key Findings

Revisão sistemática de 93 estudos peer-reviewed sobre detecção de fraude em procurement público usando métodos data-driven (filtrados de 6.000+ candidatos iniciais).

## Resultados principais

### Tipos de fraude estudados
- **Colusão/bid rigging:** categoria mais estudada (maioria dos 93 papers)
- **Favoritism:** 31.18% dos estudos — menor atenção que colusão
- Outros: superfaturamento, fraude em habilitação, phantom deliveries

### Metodologias dominantes

**Para detecção de colusão:**
- Ensemble methods (Extra Trees, Random Forest, AdaBoost): 81-95% accuracy
- Network analysis (ownership + co-bidding graphs)
- Statistical screening (distribuição de preços, bid spread, coefficients of variation)

**Para detecção de favoritism:**
- Statistical analysis é dominante (mais simples, menos dados necessários)
- Machine learning tem menor penetração nessa categoria

### Dados utilizados
- Procurement bidding data (resultados de licitações, preços, participantes)
- Ownership/company registration data (análogo ao CNPJ)
- Employment data (análogo ao RAIS) — menos comum mas crescente
- Supplier networks + graph databases

### Achados metodológicos
- Modelos ensemble superam modelos single em todos os datasets testados
- Principal challenge: ground truth escasso — cartéis são difíceis de confirmar
- Solução emergente: usar casos conhecidos de cartéis + synthetic data + transfer learning

### Contexto geográfico dos estudos
- Múltiplos países; Brasil presente mas não dominante
- Dados de auditoria como ground truth (análogo à CGU brasileira) são o padrão

## Relevância para KB

- **REFINA** `procurement-manipulation-signals`: confirma que os sinais listados (sobreposição de CNPJ, concentração de winners) são os mais validados na literatura
- **REFINA** `audit-risk-rent-extraction`: adiciona metodologia ML específica para os tipos de irregularidades identificados por Zamboni & Litschig
- Preenche gap de "metodologia de detecção" que o corpus tinha apenas em forma teórica (Decarolis identificou sinais; este paper sistematiza como detectá-los computacionalmente)
