# Evaluating Domain-adapted Language Models for Governmental Text Classification Tasks in Portuguese

**Autores:** Mariana O. Silva, Gabriel P. Oliveira, Lucas G. L. Costa, Gisele L. Pappa (UFMG)
**Publicação:** Anais do XXXIX Simpósio Brasileiro de Bancos de Dados (SBBD 2024)
**DOI:** 10.5753/sbbd.2024.240508
**URL:** https://sol.sbc.org.br/index.php/sbbd/article/view/30697
**Grupo:** LAIC — UFMG
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract do portal SBC.

---

## Tese Central

Domain-adaptive pre-training (DAPT) melhora modelos de linguagem para tarefas de classificação governamental. Principais fatores: **dataset do domínio alvo**, composição linguística do modelo base, e tamanho do dataset.

## Metodologia

- DAPT aplicado sobre BERTimbau e LaBSE
- Tarefas de classificação de texto governamental em português
- Avaliação sistemática de 3 fatores: dataset alvo, composição linguística, tamanho

## Resultados

- Seleção adequada do dataset alvo e estratégia de pré-treino melhora "notavelmente" o desempenho
- Modelos derivados de BERTimbau e LaBSE com DAPT superam modelos genéricos
- (métricas quantitativas específicas não disponíveis no abstract)

## Relação com outros papers

Paper complementar ao GovBERT-BR (BRACIS 2024): aquele apresenta o modelo; este avalia sistematicamente os fatores que determinam a eficácia do DAPT. Juntos formam a base NLP do pipeline LAIC.

## Relevância para Zelox

Confirma que especialização de domínio é necessária para classificação de texto governamental — modelos genéricos (GPT-4, etc.) podem ter desempenho inferior a modelos DAPT menores para tarefas específicas do SICOM/PNCP. Relevante para decisão de infraestrutura NLP se Zelox incorporar classificação de texto.
