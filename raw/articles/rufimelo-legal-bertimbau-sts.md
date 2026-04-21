# Legal-BERTimbau-sts-large (rufimelo/Legal-BERTimbau-sts-large)

**Origem:** HuggingFace Model Card — rufimelo  
**URL:** huggingface.co/rufimelo/Legal-BERTimbau-sts-large  
**Tipo:** Modelo fine-tuned open source  
**Type:** STUB — model card; sem paper formal

---

## Hipótese Central

Fine-tuning de BERTimbau-large para Semantic Textual Similarity (STS) em datasets portugueses (ASSIN 1, ASSIN 2) produz embeddings otimizados para busca semântica em domínio legal PT.

---

## Especificações Técnicas

- **Base model:** BERTimbau-large
- **Fine-tuning task:** Semantic Textual Similarity (STS)
- **Datasets de treinamento:** ASSIN 1, ASSIN 2 (portugueses, domínio geral-jurídico)
- **Pooling:** Mean pooling sobre token embeddings (padrão sentence-transformers)
- **Max sequence length:** 128 tokens ⚠️
- **Framework:** sentence-transformers

---

## Evidências

- Disponível diretamente via `sentence-transformers` — integração direta com pipeline existente
- Fine-tuning para STS alinhado com objetivo de retrieval semântico (queries de busca ≠ indexação keyword)
- BERTimbau-large como base garante boa cobertura léxica do PT-BR

---

## Limitação Crítica

**Max sequence length de 128 tokens é proibitivo para atos de DO.**

Atos de licitação típicos têm 300-800 tokens. Com 128 tokens, o modelo processa apenas o início do ato, perdendo objeto do contrato, valor e dados do contratado — as entidades mais importantes para retrieval.

**Opções para contornar:**
1. Usar Legal-BERTimbau-large sem STS fine-tuning (512 tokens) — melhor cobertura, embeddings menos otimizados para busca
2. Usar chunking agressivo + late chunking (se modelo long-context disponível)
3. Usar jina-embeddings-v3 (multilingual, 8K context) como fallback temporário

---

## Applicabilidade Zelox

**ALTA como ponto de partida conceitual, BLOQUEADA na prática por max_seq_length=128.**

A limitação de 128 tokens torna este modelo inadequado para embeddar atos completos. Avaliação necessária: Legal-BERTimbau-large (512 tokens) sem STS fine-tuning vs Legal-BERTimbau-sts-large (128 tokens) com fine-tuning STS — trade-off cobertura × qualidade semântica.

---

## Hipótese a Testar

Legal-BERTimbau-large (512 tokens, sem STS) supera Legal-BERTimbau-sts-large (128 tokens, com STS) em retrieval de atos de DO por cobertura de entidades, mesmo com embeddings semanticamente menos refinados.

---

## Conexões

- Alternativa: LegalBert-pt (1.5M docs, domínio judicial)
- Alternativa: GovBert-BR (silva-pappa-2024-govbert-br.md, domínio governamental)
- Gap: nenhum dos modelos disponíveis foi fine-tunado para STS em textos de licitação/contratação
