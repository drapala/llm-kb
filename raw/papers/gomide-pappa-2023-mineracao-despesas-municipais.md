# Mineração de Dados sobre Despesas Públicas de Municípios Mineiros para Gerar Alertas de Fraudes

**Autores:** Larissa D. Gomide, Guilherme Bezerra dos Santos, Lucas L. Costa, Michele A. Brandão, Anisio Lacerda, Gisele L. Pappa (UFMG/IFMG)
**Publicação:** XXXVIII SBBD 2023, Short Article, pp. 378–383
**DOI:** 10.5753/sbbd.2023.232788
**URL:** https://sol.sbc.org.br/index.php/sbbd/article/view/25547
**Grupo:** LAIC — UFMG
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract do portal SBC.

---

## Tese Central

Comparação de despesas entre municípios mineiros para identificar fraudes orçamentais municipais. Clustering de municípios por tamanho de população e microrregião + ranking de despesas para detectar anomalias.

## Metodologia

- Clustering de municípios: por população e microrregião geográfica
- Ranking de despesas dentro de cada cluster
- Detecção de anomalias: despesas fora do range esperado para o grupo de pares
- (abordagem de "peer comparison" — municípios similares como baseline)

## Resultados

Não disponíveis no abstract — short article (5 páginas).

## Relevância para Zelox

**Alta relevância metodológica:**
- A abordagem de peer comparison (municípios similares como grupo de controle) é análoga ao IQR do Silva/Pappa 2024 mas aplicada a **nível de município** ao invés de item
- Zelox poderia usar benchmark de municípios similares para contextualizar o risk_score: um `delta_pct` de +30% pode ser normal em município com baixa competitividade e anômalo em capital
- Clustering geográfico + ranking é implementável com dados SICONFI/STN que são públicos
- Autores incluem Gomide e Bezerra (nomes que aparecem em co-autoria do silva-pappa-2024 overpricing) — confirma integração com pipeline LAIC

## Conexão com outros papers

Complementa Braz/Pappa 2024 (small companies, geoespacial): aquele foca em empresas suspeitas geograficamente concentradas; este foca em municípios com despesas anômalas. Juntos formam uma visão geográfica dupla: quem fornece (empresas) e quem compra (municípios).
