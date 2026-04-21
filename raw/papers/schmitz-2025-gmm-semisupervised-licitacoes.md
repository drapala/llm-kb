# Detecção de fraudes em licitações públicas: uma abordagem semissupervisionada de agrupamento com Modelos de Mistura Gaussiana

**Autor:** Fernando Augusto Schmitz
**Orientador:** Jônata Tyska Carvalho
**Publicação:** Dissertação de Mestrado — PPGCC, CTC, Universidade Federal de Santa Catarina (UFSC), Florianópolis, 67 p., 2025
**URL:** https://repositorio.ufsc.br/handle/123456789/267575
**Grupo:** UFSC — grupo diferente do LAIC/UFMG
**Tipo:** paper / primary (dissertação de mestrado)
**Status:** STUB — conteúdo baseado em resumo do repositório UFSC.

---

## Tese Central

Metodologia **semi-supervisionada** com Gaussian Mixture Models (GMM) para detecção de fraude em licitações públicas, endereçando o problema de **escassez de dados rotulados** (casos confirmados de fraude).

## Problema Central

Fraude em licitações é difícil de detectar via ML supervisionado porque:
1. Dados rotulados escassos (poucos casos confirmados)
2. Irregularidades são dinâmicas e heterogêneas
3. Alta dimensionalidade dos dados

## Metodologia

- GMM para clustering semi-supervisionado
- Usa grandes volumes de dados públicos (não rotulados)
- Semi-supervisão: aproveita os poucos casos rotulados disponíveis como âncoras

## Resultados

Não disponíveis no resumo.

## Relevância para Zelox

**Alta relevância metodológica — endereça o problema fundamental:**
- O Zelox enfrenta exatamente o mesmo problema: ausência de ground truth (CGU/TCU) sistematizado
- GMM semi-supervisionado é alternativa ao z-score heurístico atual: em vez de threshold manual, o modelo aprende a distribuição dos normais e sinaliza desvios
- Semi-supervisão permite usar os poucos casos confirmados como guia sem exigir dataset completo rotulado
- Contrasta com MultiFraud (Wu 2024) que requer dados totalmente rotulados

## Conexão com outros papers

Complementa o debate sobre ground truth documentado em `laic-ufmg-procurement-fraud-detection.md`. A dissertação UFSC representa uma solução alternativa: ao invés de contornar a ausência de labels (LAIC usa heurísticas), usa os poucos labels disponíveis como supervisão fraca (semi-supervised). Comparação direta com abordagem LAIC seria valiosa.
