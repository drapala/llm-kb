# Collusion risk in corporate networks

**Authors:** Villamil, Kertész, Fazekas
**Year:** 2024
**Journal:** Scientific Reports, Volume 14 (Nature Publishing Group)
**URL:** https://www.nature.com/articles/s41598-024-53625-9
**Type:** Empirical paper — network analysis
**Data:** Swedish procurement, 2010-2015
**Note:** Conteúdo baseado em abstract e descrição da busca — full text não verificado.

## Abstract / Key Findings

Usa temporal multiplex networks construídas a partir de:
1. **Ownership ties** — quem são os sócios de cada empresa (registro societário)
2. **Co-bidding ties** — quais empresas submeteram propostas no mesmo processo licitatório

Combinação dos dois layers cria rede temporal onde é possível identificar clusters de empresas que (a) têm relacionamento societário E (b) biddam no mesmo mercado.

## Resultados principais

### Métricas de collusão identificadas
- **Single bidding:** mercados com empresas mais centrais no grafo de ownership têm maior incidência de processos com apenas 1 licitante
- **Missing bidders:** empresas conectadas ao vencedor sistematicamente "deixam de aparecer" em certos processos (bid rigging coordinado)
- **Win rate de empresas centrais:** empresas com alta centralidade em ownership network ganham contratos significativamente mais frequentemente, controlando por outras características

### Metodologia
- Temporal multiplex: 2010-2015 (5 anos de dados)
- Dados de registro societário (análogo ao CNPJ brasileiro) + dados de licitações (análogo ao PNCP)
- Network centrality metrics como preditores de win rate
- Controlling for: tamanho da empresa, setor, histórico de contratos

### Achados de validação
- Markets mais conectados via ownership links → higher single bidding + missing bidders
- Efeito é estatisticamente significativo e economicamente relevante
- Replicação de Decarolis et al.: confirma que relacionamento societário é o mecanismo, não apenas a politcal connection

## Relevância para KB

- **CONFIRMA** claim em `procurement-manipulation-signals`: "empresas com sócios sobrepostos que submetem propostas no mesmo processo = sinal de bid rigging"
- **REFINA**: o claim era baseado em Decarolis (Itália); agora tem confirmação independente com metodologia de rede em outro país (Suécia)
- **ADICIONA**: método de detecção via temporal multiplex — não apenas sobreposição estática de sócios, mas evolução dinâmica do relacionamento
- **Aplicação direta ao Brasil:** PNCP (licitações) + CNPJ (registro societário) = exatamente os dois layers usados por Villamil et al. para construir a rede
