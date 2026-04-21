# Overpricing Analysis in Brazilian Public Bidding Items

**Autores:** M. O. Silva, L. G. L. Costa, L. D. Gomide, G. Bezerra, G. P. Oliveira, M. A. Brandão, A. Lacerda, G. L. Pappa (UFMG/IFMG)
**Publicação:** Journal on Interactive Systems, v.15, n.1, pp.130–142, 2024
**DOI:** 10.5753/jis.2024.3831
**URL:** https://journals-sol.sbc.org.br/index.php/jis/article/view/3831
**Acesso:** Open access — PDF disponível diretamente na SBC
**Grupo:** LAIC — UFMG
**Tipo:** paper / primary
**Status:** VERIFICADO — paper completo obtido e lido.

---

## Tese Central

Detecção de sobrepreços em **preços unitários de itens** de licitações públicas brasileiras via padronização textual + IQR. O problema central: itens com a mesma função são descritos de formas radicalmente diferentes nos editais, tornando a comparação de preços direta impossível sem normalização prévia.

## Problema e Motivação

Superfaturamento (overpricing) em licitações públicas é sinal direto de irregularidade. A detecção é difícil porque:
- Descrições de itens são heterogêneas (mesmo item, 50 formas de descrever)
- Não há base de preços de referência consolidada
- Volume de licitações torna revisão manual inviável

## Metodologia

### Etapa 1 — Padronização de descrições de itens

3 estratégias de agrupamento textual testadas:
- **Words:** normalização por palavras-chave (melhor resultado: R² = 95% vs. preços ANP)
- Estratégias alternativas com desempenho inferior

### Etapa 2 — Dois níveis de detecção de anomalia de preço

Após agrupar itens similares, aplicam IQR em duas camadas:

**Nível 1 — Overpricing:**
- Threshold: preço unitário > Q3 + 1.5×IQR do grupo
- Flags preços moderadamente acima da faixa normal

**Nível 2 — Anomalia:**
- Threshold mais restritivo (múltiplo maior do IQR)
- Flags preços dramaticamente acima do esperado
- Os dois níveis permitem priorização: anomalias para investigação imediata, overpricing para monitoramento

### Validação empírica

- Estratégia "Words" validada contra preços reais da **ANP (Agência Nacional do Petróleo)**
- R² = 95% — agrupamento textual reproduz clusters de preços reais
- Validação empírica real, não apenas argumento estatístico (Tukey 1977)

## Limitações Explicitadas pelos Autores

- **"Not a definitive solution, requiring continuous monitoring"** — o paper reconhece explicitamente que a detecção é heurística e requer revisão contínua
- Padronização textual é difícil com descrições muito heterogêneas
- IQR é instável para itens com poucos registros no grupo
- Não trata aditivos contratuais em nenhum momento

## O que este paper NÃO cobre

- Aditivos contratuais (delta_pct, hold-up) — completamente fora do escopo
- Redes de empresas ou bid-rigging
- Análise temporal de variação de preços ao longo do contrato
- Municípios específicos ou análise regional

## Relevância para Zelox

**Analogia válida, mas domínio diferente:**
- O IQR do LAIC é aplicado a **preços unitários de itens** na fase de licitação
- O `z_score_aditivo_por_tipo` do Zelox é aplicado a **delta_pct de aditivos** na fase de execução
- São momentos distintos do ciclo de vida do contrato — a lógica estatística é análoga, o objeto de medição é diferente

**O que o Zelox pode adaptar:**
- Dois níveis de threshold (overpricing + anomalia) para o risk score — em vez de um único z-score, criar dois tiers
- Validação de agrupamento por tipo de objeto via R² contra preços de referência externos (ANP → equivalente para contratos de obra/serviço)
- A ressalva "continuous monitoring" se aplica diretamente ao Zelox: compliance_rules precisam de revisão periódica
