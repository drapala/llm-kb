# The Employee Costs of Corporate Debarment in Public Procurement

**Authors:** Christiane Szerman
**Year:** 2023
**Journal:** American Economic Journal: Applied Economics, Volume 15, Issue 1
**SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3488424
**Type:** Empirical paper — causal identification
**Data:** Brazil — CEIS (debarment records) + employer-employee administrative data (RAIS)
**Note:** Conteúdo baseado em abstract, SSRN description, e citações em literatura secundária. Full text não verificado.

## Abstract / Key Findings

Explora mudança de política no Brasil que impôs penalidades de debarment mais rígidas para empresas corruptas. Combina:
- **CEIS** (Cadastro de Empresas Inidôneas e Suspensas) — registro de empresas com contratos rescindidos por irregularidades
- **Dados empregador-empregado** (RAIS ou similar) — vincula trabalhadores às empresas debarred

## Resultados principais

### Impacto econômico do debarment
- **−22% em ganhos anuais** dos trabalhadores de empresas debarred
- Probabilidade significativamente maior de entrada no **setor informal** após debarment
- Efeitos concentrados em trabalhadores das empresas que perderam contratos governamentais

### Mecanismo
- Debarment → perda de receitas de contratos públicos → firma reduz headcount
- Trabalhadores deslocados: probabilidade maior de informalidade (vs. trabalhadores de firmas similares não-debarred)
- Efeito é CAUSAL (não apenas correlação) — exploração de variação exógena na política

### Implicação para evasão (phoenix firms)
- Penalidade econômica do debarment é substancial (−22% earnings dos trabalhadores, mais informalidade)
- Isso cria **incentivo econômico significativo para evasão** via re-incorporação (phoenix firms)
- Trabalhadores da firma original são preservados → recrutá-los na nova firma é relativamente simples
- RAIS linkage é o mecanismo de detecção: mesmos trabalhadores (PIS/PASEP) em nova empresa = indício de phoenix

### Dados utilizados
- CEIS: data de entrada, tipo de irregularidade, firma identificada
- Employer-employee data (RAIS/RAIS-like): PIS/PASEP do trabalhador + CNPJ do empregador, por ano

## Relevância para KB

- **PREENCHE GAP** identificado em /ask sobre "Combinação 3: CEIS + CNPJ + RAIS → phoenix firms"
- **CONFIRMA** que o incentivo para evasão via phoenix firm é empiricamente real e economicamente significativo
- **METODOLOGIA DIRETA**: o paper usa exatamente a combinação CEIS + RAIS para rastrear impactos → demonstra que o linkage é tecnicamente viável
- **ADICIONA**: a variável de trabalhadores (PIS/PASEP) como identificador de phoenix firms é validada neste contexto
- **Implicação para Zelox**: monitorar CEIS + CNPJ + RAIS não é apenas teórico — é a mesma combinação usada em paper AEJ de alta qualidade
