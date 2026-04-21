---
title: "Pipeline de Ground Truth via Acórdãos TCU — Projeto"
sources: []
created: 2026-04-12
updated: 2026-04-12
tags: [zelox, ground-truth, tcu, scraping, procurement-fraud, ml-systems, b2g]
source_quality: low
interpretation_confidence: high
resolved_patches: []
provenance: emergence
emergence_trigger:
  pair: [circular-ground-truth-ml-systems, z-score-aditivo]
  ask_session: outputs/logs/sessions/2026-04-12/ask-gmm-zscore.md
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-12
status: promoted
promoted_date: 2026-04-12
freshness_status: current
---

## Resumo

Proposta de pipeline para extrair ground truth de nível contrato a partir de acórdãos públicos do TCU. Acórdãos TCU que citam irregularidades em contratos específicos são a fonte de labels independentes mais acessível para o Zelox. O desbloqueador para qualquer modelo supervisionado/semi-supervisionado no contexto de procurement fraud brasileiro.

## Conteúdo

### Por que acórdãos TCU

O TCU (Tribunal de Contas da União) publica acórdãos que frequentemente:
- Identificam contratos específicos com irregularidades confirmadas
- Citam superfaturamento, aditivos irregulares, inexigibilidade indevida
- Incluem número de processo de licitação (muitas vezes o número PNCP ou equivalente)
- São documentos públicos — sem restrição de acesso

Diferente de auditoria CGU (interna, acesso restrito) e operações policiais (viés de seleção + amostras pequenas), acórdãos TCU são:
- Públicos (portal.tcu.gov.br)
- Decisões formais com número de contrato explícito
- Sistematicamente anotados (tipo de irregularidade, órgão, valor)
- Independentes do Zelox — eliminam a circularidade de ground truth

### Estrutura dos acórdãos TCU (razoavelmente consistente)

Campos extraíveis de forma semi-estruturada:
```
Acórdão N/ANO — Plenário/1ª/2ª Câmara
Órgão: [nome do órgão auditado]
Processo: [número do processo TCU]
Contrato: [número do contrato ou licitação] ← chave para join PNCP
Irregularidade: [tipo — superfaturamento, sobrepreço, inexigibilidade...]
Valor: [R$ montante irregularidade identificada]
Deliberação: [multa, devolução, recomendação]
```

### Design do pipeline

```
[Portal TCU — Pesquisa de Jurisprudência]
  → Busca: "aditivo" AND "superfaturamento" AND data_range
  → Busca: "sobrepreço" AND "contrato" AND data_range
  → Resultado: lista de acórdãos (PDF/HTML)

[Extração]
  → Parser HTML/PDF dos acórdãos
  → Extração: número do contrato, órgão, tipo de irregularidade, valor
  → NLP: identificar referências a contratos PNCP (regex + GovBERT-BR)

[Join PNCP]
  → Cruzar número de contrato TCU → PNCP via:
    (a) número do processo de licitação
    (b) CNPJ do fornecedor + período + valor (fuzzy match fallback)
  → Output: tabela (cnpj_fornecedor, id_contrato_pncp, tipo_irregularidade, acordao_tcu_id)

[Ground truth labels]
  → fraud_label = True para contratos identificados por TCU
  → fraud_type = {superfaturamento, aditivo_irregular, sobrepreco, outros}
  → confidence = {confirmed (deliberação), suspected (recomendação)}
```

### Estimativa de escala

O TCU publica ~1.500 acórdãos/mês (Plenário + Câmaras). Filtrando por termos de procurement:
- "aditivo" + "irregularidade": estimativa ~200-400 acórdãos/ano com contrato identificável
- "sobrepreço" + "contrato": estimativa ~100-200/ano
- Join PNCP bem-sucedido: ~50-70% dos casos (contratos pré-PNCP ou sem número explícito perdem join)

**Estimativa de yield:** 100-200 contratos rotulados/ano com join PNCP bem-sucedido. Em 2-3 anos de acórdãos históricos: 300-600 contratos — suficiente para GMM semi-supervisionado e possivelmente supervised RF.

### Bloqueadores técnicos

1. **Formato dos acórdãos:** mistura de PDF scanned + HTML + texto. Scanned PDFs requerem OCR — ruído de propagação. Priorizar acórdãos pós-2015 (digitais nativos).

2. **Identificação do número do contrato:** nem todo acórdão cita o número PNCP explicitamente. Fallback: CNPJ + período + valor (fuzzy match com margem de ±10%).

3. **Registro histórico PNCP:** PNCP tem cobertura crescente. Contratos pré-2020 têm cobertura parcial. Join Zelox limitado ao universo PNCP.

4. **Escopo geográfico:** TCU fiscaliza contratos federais. Contratos municipais são competência dos TCEs estaduais (26 tribunais, sem API unificada). Priorizar TCU para V1 do pipeline.

### Implementação estimada

| Etapa | Esforço | Bloqueador |
|---|---|---|
| Scraper HTML portal TCU | ~1 semana | nenhum |
| Parser estruturado de acórdãos | ~1-2 semanas | variabilidade de formato |
| Join PNCP por número de contrato | ~3 dias | cobertura histórica PNCP |
| Join fuzzy (CNPJ + valor + período) | ~1 semana | definição de threshold |
| Validação manual de sample | ~2-3 dias | precisa de revisão humana |

**Total estimado: 4-6 semanas** para V1 com ~100 contratos rotulados.

### Impacto no roadmap Zelox

Com ground truth externo disponível:
- Calibração empírica do threshold IQR com precision/recall real
- Bootstrap do GMM semi-supervisionado (Schmitz 2025) com labels independentes
- Validação dos 3 L2 predictions do ledger: são falsos positivos ou corretos?
- Treinamento de Random Forest multi-feature (benchmark contra Morais/UFU 2024, F1=80%)

## Conexões

- [[circular-ground-truth-ml-systems]] — este pipeline é o desbloqueador do anti-padrão de circularidade
- [[z-score-aditivo]] — o pipeline fornece os labels para calibração empírica do threshold IQR
- [[laic-ufmg-procurement-fraud-detection]] — LAIC usa ground truth de Operação Licitante Fantasma; TCU acórdãos são alternativa sistematizada sem viés de operação policial

## Fontes

Artigo emergido de análise /ask — sem fontes raw/ primárias. Baseado em conhecimento do domínio (portal TCU público) + gap identificado na sessão de 2026-04-12.
