---
title: "Modelos BERT Legal PT-BR"
sources:
  - path: raw/articles/silveira-2023-legalbert-pt.md
    type: article
    quality: secondary
    stance: confirming
  - path: raw/articles/rufimelo-legal-bertimbau-sts.md
    type: note
    quality: secondary
    stance: confirming
  - path: raw/papers/garcia-2024-roberta-lex-pt.md
    type: paper
    quality: primary
    stance: challenging
    challenging_type: content
created: 2026-04-13
updated: 2026-04-14
tags: [nlp, embedding, bert, roberta, legal, ptbr, zelox, ner, portulexbenchmark]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: synthesis
synthesis_sources: []
---

## Resumo

**[ATUALIZADO 2026-04-14]** RoBERTaLexPT (Garcia et al., PROPOR 2024) supera LegalBert-pt em todas as tarefas do PortuLex benchmark — novo modelo de referência para PT jurídico. LegalBert-pt (Silveira et al. 2023) permanece relevante como baseline; Legal-BERTimbau-sts-large bloqueado por limite de 128 tokens. Nenhum modelo foi avaliado em textos de licitação/contratação pública (domínio de DO Seção III).

## Conteúdo

### LegalBert-pt (Silveira et al. 2023)

- Corpus: 1.5M documentos legais brasileiros — maior corpus jurídico PT-BR publicado até 2023
- Arquitetura: BERT base + fine-tuning no corpus jurídico BR
- Domínio: judicial (acórdãos, petições, decisões)
- Supera BERTimbau-base e multilíngues em classificação de textos legais

**Limitação de domínio:** corpus judicial ≠ corpus administrativo/procurement. Vocabulário de DO (portaria, extrato, pregão) é mais próximo de edital do que de acórdão. Fine-tuning adicional em corpus de DOs/PNCP necessário para aplicação Zelox.

### Legal-BERTimbau-sts-large (rufimelo)

- Base: BERTimbau-large
- Fine-tuning: STS em ASSIN 1 + ASSIN 2 (PT-BR, domínio geral-jurídico)
- Framework: sentence-transformers (mean pooling)
- **Max sequence length: 128 tokens** ⚠️

**Limitação crítica:** atos de licitação têm 300-800 tokens. Com 128 tokens, o modelo processa apenas o início do ato, perdendo objeto do contrato, valor e dados do contratado.

### RoBERTaLexPT (Garcia et al., PROPOR 2024)

- **Corpus:** LegalPT — até 125GiB de textos legais PT + CrawlPT (geral)
- **Inovação:** primeiro corpus jurídico PT com deduplicação explícita — prior corpora tinham alta taxa de duplicação
- **Arquitetura:** RoBERTa base (512 tokens max)
- **Benchmark:** PortuLex — 4 tarefas legais PT anotadas por especialistas (LeNER-Br, UlyssesNER-Br, RRI, FGV-STF)
- **Resultado:** supera LegalBert-pt, BERTikal, JurisBERT e modelos multilíngues maiores em todas as tarefas PortuLex
- **Disponível:** github.com/eduagarcia/roberta-legal-portuguese

**Implicação direta:** LegalBert-pt deixa de ser o modelo de referência — RoBERTaLexPT é o novo baseline para NER e classificação em textos jurídicos PT-BR.

**Limitação:** mesmo domínio judicial; DOs municipais provavelmente sub-representados no LegalPT. Max 512 tokens (sem cobertura de atos longos sem chunking).

### Mapa de Decisão para Zelox (Atualizado)

| Tarefa | Modelo recomendado |
|--------|-------------------|
| NER em entidades de DO (CNPJ, valor, modalidade) | **RoBERTaLexPT** como base de fine-tuning (supera LegalBert-pt) |
| Embedding semântico para retrieval | RoBERTaLexPT (512 tok) ou jina-embeddings-v3 (8K tok) |
| STS/retrieval otimizado | Legal-BERTimbau-sts-large bloqueado (128 tok) — NÃO usar para atos completos |

**Hipótese a testar (H10 atualizada):** RoBERTaLexPT (512 tok, legal, deduplicated) supera LegalBert-pt e Legal-BERTimbau-sts-large (128 tok) em retrieval de atos completos.

### Gap Identificado (Persiste)

Nenhum modelo avaliado em textos de licitação/contratação pública (DO Seção III). O PortuLex cobre jurisprudência e legislação. Alternativas de curto prazo:
1. RoBERTaLexPT com fine-tuning em corpus PNCP/DOs — melhor backbone disponível
2. Jina-embeddings-v3 (multilingual, 8K context) — para atos longos
3. Hard-negative mining (NV-Retriever) para fine-tuning de qualidade

## Interpretação

(⚠️ nossa interpretação) RoBERTaLexPT substitui LegalBert-pt como backbone de referência. Para NER de entidades B2G (CNPJ-contratante vs CNPJ-contratado, valor-contrato vs valor-aditivo), RoBERTaLexPT é o melhor ponto de partida — corpus maior, deduplicated, supera LegalBert-pt em PortuLex. Porém: avaliação em DO Seção III (contratos/licitações) ainda inexistente.

(⚠️ nossa interpretação) Verificação adversarial: os 128 tokens do Legal-BERTimbau-sts-large não são contornáveis por chunking agressivo — chunking de ato perde precisamente as entidades relacionais (contratante + contratado no mesmo ato). Late chunking não resolve porque o modelo base não processa além de 128 tokens.

## Conexões

- partOf: [[diario-oficial-segmentation-strategies]] — modelos para boundary detection e NER em DOs
- partOf: [[blended-rag-three-way-retrieval]] — tier dense do three-way retrieval depende de modelo de embedding adequado
- partOf: [[late-chunking-contextual-embeddings]] — late chunking requer modelo com contexto longo (jina-v3 ou equivalente)

## Fontes

- [LegalBert-pt (Silveira et al. 2023)](../../raw/articles/silveira-2023-legalbert-pt.md) — 1.5M docs judiciais BR, supera BERTimbau em classificação legal
- [Legal-BERTimbau-sts-large (rufimelo)](../../raw/articles/rufimelo-legal-bertimbau-sts.md) — STS fine-tuned, 128 tokens máximo, bloqueado para atos completos
