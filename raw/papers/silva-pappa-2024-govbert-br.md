# GovBERT-BR: A BERT-Based Language Model for Brazilian Portuguese Governmental Data

**Autores:** Mariana O. Silva, Gabriel P. Oliveira, Lucas G. L. Costa, Gisele L. Pappa (UFMG)
**Publicação:** Brazilian Conference on Intelligent Systems (BRACIS 2024), Springer LNCS, ISBN 978-3-031-79032-4, pp. 19–32
**DOI:** 10.1007/978-3-031-79032-4_2
**Grupo:** LAIC — UFMG
**Tipo:** paper / primary
**Status:** STUB — conteúdo baseado em abstract e metadados Springer.

---

## Tese Central

GovBERT-BR: modelo de linguagem pré-treinado especificamente para **português brasileiro governamental** (domínios legal e administrativo). Supera modelos existentes em tarefas de classificação de documentos e textos curtos do setor público brasileiro.

## Metodologia

- Base: BERTimbau + pré-treinamento adaptativo de domínio (DAPT)
- Corpus: textos governamentais brasileiros — legal e administrativo
- Tarefas avaliadas: classificação de documentos e textos curtos
- Métricas: desempenho vs. BERTimbau base; convergência durante fine-tuning

## Resultados

- Supera modelos existentes em classificação de documentos governamentais
- Convergência mais rápida durante fine-tuning vs. modelos genéricos
- (métricas quantitativas completas não disponíveis no abstract)

## Relevância para Zelox

**Ferramenta prática de alto valor:**
- Classificação de tipo de objeto de contrato (serviço/obra/compra) é tarefa de classificação de texto curto — domínio exato para o qual GovBERT-BR é otimizado
- Normalização de descrições de itens (problema central do LAIC) pode usar GovBERT-BR como encoder ao invés de TF-IDF/bag-of-words
- Se Zelox evoluir para feature extraction via NLP (ex: detectar inconsistências entre objeto do contrato e CNAE do fornecedor), GovBERT-BR é o modelo de referência para português governamental
- Disponibilidade: checar HuggingFace hub (grupo UFMG publica modelos publicamente)

## Conexão com outros papers do grupo

Fundação linguística para toda a stack NLP do LAIC. GovBERT-BR é o encoder que suporta:
- Classificação de documentos (PLUS pipeline — Brandão 2024)
- Avaliação de modelos DAPT (Silva/Pappa SBBD 2024)
- Potencialmente: agrupamento de itens (Brum/Pappa LREC 2024)
