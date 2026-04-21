# Exploring Irregularities in Brazilian Public Bids: An In-depth Analysis on Small Companies

**Autores:** C. S. Braz, M. T. Dutra, G. P. Oliveira, L. G. L. Costa, M. O. Silva, M. A. Brandão, A. Lacerda, G. L. Pappa (UFMG/IFMG)
**Publicação:** Journal on Interactive Systems, v.15, n.1, pp.349–361, 2024
**URL:** https://journals-sol.sbc.org.br/index.php/jis/article/view/3836
**Grupo:** LAIC — UFMG
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract e ResearchGate.

---

## Tese Central

Detecção de irregularidades em pequenas empresas participantes de licitações públicas em Minas Gerais. Foco em comportamento potencialmente fraudulento via análise exploratória, geoespacial e de redes.

## Metodologia

**Abordagem 1 — Exploratória e geoespacial:**
- Análise de distribuição geográfica de empresas com alertas de irregularidade
- Padrões regionais de concentração de empresas suspeitas

**Abordagem 2 — Análise de redes:**
- Algoritmo Fast Unfolding (Blondel et al. 2008) para detecção de comunidades
- Identifica clusters de pequenas empresas com padrões de irregularidade compartilhados

## Dados

Licitações públicas de Minas Gerais — período e volume não especificados. Foco em empresas de pequeno porte com alertas de irregularidade.

## Resultados

Ambas as abordagens "demonstraram eficácia" — métricas quantitativas não disponíveis no abstract.

## Limitações

- Restrito a Minas Gerais — generalização para outros estados não avaliada
- Pequenas empresas são segmento específico — resultados podem não generalizar
- Features específicas não detalhadas

## Relevância para Zelox

Geolocalização + análise de rede para pequenas empresas é dimensão não explorada no Zelox atual. Municípios com clusters de pequenas empresas suspeitas pode ser feature contextual adicional (ortogonal ao `rede_empresas_score` que foca em CNPJ sobrepostos).
