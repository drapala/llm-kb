# Ranqueamento de Licitações Públicas a partir de Alertas de Fraude

**Autores:** Gabriel P. Oliveira, Bárbara M. A. Mendes, Camila S. Braz, Lucas L. Costa, Mariana O. Silva, Michele A. Brandão, Anísio Lacerda, Gisele L. Pappa (UFMG/IFMG)
**Publicação:** BraSNAM 2023 (12th Brazilian Workshop on Social Network Analysis and Mining)
**URL:** https://sol.sbc.org.br/index.php/brasnam/article/view/24782
**Grupo:** LAIC — UFMG
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract e web search. PDF pode ser acesso aberto via URL.

---

## Tese Central

Modelar alertas de fraude como rede social para ranquear licitações públicas suspeitas. Combina múltiplos sinais de detecção em estratégia integrada de priorização.

## Metodologia

**19 trilhas de auditagem como sinais:**
- Cada trilha representa um tipo de alerta de irregularidade
- Modeladas como grafo social: nós = licitações, arestas = alertas em comum

**Ranqueamento:**
- Agrega múltiplos alertas via estrutura de rede
- Prioriza licitações com maior densidade de alertas interconectados

## Dados

Licitações públicas brasileiras — fonte específica não confirmada.

## Resultados

Identificação de licitações suspeitas via ranqueamento baseado em padrões de alertas conectados.

## Limitações

Detalhes de métricas e dataset não acessíveis sem PDF completo.

## Relevância para Zelox

19 trilhas de auditagem é a especificação mais próxima de um "feature set" para detecção de fraude em licitações brasileiras publicada pelo grupo LAIC. Direto comparável aos sinais do Risk Score Zelox.
