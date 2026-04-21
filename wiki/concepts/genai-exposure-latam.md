---
title: "GenAI Employment Exposure in Latin America (ILO/World Bank 2024)"
sources:
  - path: raw/papers/gmyrek-winkler-2024-buffer-bottleneck-genai-latam.md
    type: paper
    quality: secondary
    stance: neutral
    note: "nota derivada — PDF inacessível; dados de press releases + WorldBank summary"
created: 2026-04-08
updated: 2026-04-08
tags: [labor-economics, ai, latam, brazil, informal-sector, digital-divide, genai, automation]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
---

## Resumo

Gmyrek, Winkler & Garganta (ILO WP121 / World Bank WP10863, julho 2024) medem a exposição ao GenAI em 18 países da América Latina e Caribe, ajustando pelo acesso real à tecnologia digital no trabalho. Achado central: 26–38% dos empregos na ALC estão expostos a GenAI (vs. 60% em economias avançadas). A lacuna se explica principalmente pelo setor informal e pelo digital divide. O digital divide funciona como **bottleneck para ganhos de produtividade** — ~17 milhões de empregos poderiam se beneficiar mas não têm acesso digital para capturar esses ganhos.

## Conteúdo

### Exposição ao GenAI na ALC

| Categoria | % empregos ALC |
|-----------|---------------|
| Expostos a GenAI (total) | 26–38% |
| Com potencial de aumento de produtividade | 8–14% |
| Com risco de automação completa | 2–5% |
| Bloqueados por digital divide | ~17 milhões |

Economias avançadas: ~60% de exposição. Diferença ALC explicada pelo setor informal + digital divide.

### Quem Tem Maior Exposição

- Trabalhadores urbanos, ensino superior, setor formal, renda mais alta
- Trabalhadores mais jovens
- Setores: finanças, seguros, administração pública
- Padrão consistente com Eloundou (2024): gradiente salarial invertido vs. automação industrial

### Dados Brasil por Grupo de Renda

| Grupo | Potencial de benefício GenAI | Acesso digital no trabalho |
|-------|------------------------------|---------------------------|
| Em situação de pobreza | 8,5% | ~40% |
| Não-pobres | 14% | ~60% |

### Mecanismo: Bottleneck, não Buffer

**Achado central:** para ganhos de produtividade, o digital divide é bottleneck (bloqueia augmentação), não buffer (proteção).

Dois grupos de trabalhadores afetados de formas opostas:

| Grupo | Digital access | Exposição | Resultado |
|-------|---------------|-----------|-----------|
| Formal, renda alta, urbano | Alto | Alto | Risco de automação + potencial de augmentação |
| Informal, baixa renda, rural | Baixo | Baixo | Perde ganhos de produtividade; protegido de automação por non-adoption |

"Quase metade dos empregos que poderiam melhorar produtividade com GenAI (~17M) são bloqueados por lacunas de acesso digital e infraestrutura."

**Distinção de mecanismos:**
O informal não é "buffer de absorção pós-deslocamento" (mecanismo Brambilla para robôs físicos). O informal tem **menor exposição** porque firmas informais têm menor propensão a adotar GenAI — é um barrier to adoption, não um absorber of displaced workers. São mecanismos distintos que operam em momentos diferentes da cadeia de impacto.

### Metodologia

- 18 países ALC; classificação ISCO-08 4-digit
- Dados: SEDLAC (harmonized household surveys)
- Ajuste digital: probabilidade de uso de tecnologia digital no trabalho
- Fonte digital: modelo preditivo baseado em PIAAC (4 países) extrapolado para 18 países
- Três categorias: automation potential | augmentation potential | big unknown

### Limitações

- Análise de exposição técnica, não deslocamento realizado
- "Big unknown" é categoria relevante — impacto depende de evolução tecnológica
- Dados extrapolados de 4 países para 18 via modelo preditivo
- Nota derivada de press releases (não do paper completo) — pode faltar detalhes por país

## Verificação adversarial

**Fragilidade principal:** source_quality:medium porque esta nota foi construída sem acesso ao PDF completo — dados de press releases institucionais. Dados de Brasil são agregados (poverty/non-poverty), não por setor ISCO específico.

**O que o estudo NÃO diz:**
1. Não prevê deslocamento real — apenas exposição técnica ajustada por digital access
2. Não modela criação de novos empregos
3. Brasil-specific não está isolado no abstract público — dados são inferidos

## Interpretação

(⚠️ Zone 3 — domínio lateral. Interpretação intencionalmente vazia no ingest. Conexões com a KB emergem no /ask.)

## Conexões

## Fontes
- [Gmyrek, Winkler, Garganta (2024)](../../raw/papers/gmyrek-winkler-2024-buffer-bottleneck-genai-latam.md) — ILO WP121 / World Bank WP10863; 18 países ALC; buffer vs. bottleneck; digital divide adjustment
