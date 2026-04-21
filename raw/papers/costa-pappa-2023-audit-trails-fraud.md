# Identification of Suspected Fraud Bids Through Audit Trails

**Autores:** L. Costa, C. Bacha, G. P. Oliveira, M. O. Silva, M. C. Teixeira, M. A. Brandão, A. Lacerda, G. L. Pappa (UFMG/IFMG)
**Publicação:** iSys — Journal of Information Systems (SBC), Vol. 16, Issue 1, 2023
**URL:** https://journals-sol.sbc.org.br/index.php/isys/article/view/3013
**Grupo:** LAIC — UFMG
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract e web search.

---

## Tese Central

Detecção de fraudes em licitações via análise de audit trails (trilhas de auditoria) e social network analysis para identificar padrões suspeitos de conluio entre empresas participantes.

## Metodologia

**Features/Signals:**
- Histórico de participação de empresas em editais
- Co-bidding patterns: empresas que participam conjuntamente em múltiplos processos
- Análise de coesão e exclusividade de grupos de licitantes
- Indicadores de cartel baseados em comportamento coletivo

**Algoritmos:**
- Social network analysis dos co-bidding patterns
- Clustering de licitações por atributos
- Classificadores para identificar comportamentos consistentes com bid-rigging

**Saída:** Ranking de lances suspeitos para priorização de auditores

## Dados

Licitações públicas brasileiras com histórico de participantes, preços e histórico de transações.

## Resultados

- Audit trails efetivas em selecionar informações relevantes de grande volume de dados
- Suporta detecção de cartéis via padrões de co-bidding

## Limitações

- Volume massivo de dados exige processamento eficiente
- Número reduzido de especialistas limita validação manual
- Dependência de qualidade dos dados de trilha
