# LegalBert-pt — 1.5M Documentos Legais Brasileiros

**Autores:** Silveira et al.  
**Publicado:** 2023  
**URL:** researchgate.net/publication/374645610  
**Type:** STUB — sem arxiv; baseado em análise de literatura

---

## Hipótese Central

Modelo BERT treinado em 1.5M documentos do ordenamento jurídico brasileiro supera BERTimbau e modelos multilíngues em tarefas de NLP legal brasileiro.

---

## Evidências

- Corpus: 1.5M documentos legais — **maior corpus jurídico PT-BR publicado** até 2023
- Supera BERTimbau em classificação de textos legais
- Domínio de treinamento: judicial (acórdãos, petições, decisões)
- Arquitetura: BERT base com fine-tuning em corpus jurídico BR

---

## Limitações / Falsificadores

- Domínio judicial ≠ domínio administrativo/procurement — vocabulário de DO é mais próximo de edital/portaria do que de acórdão/petição
- 512 token limit padrão BERT — atos longos precisam chunking
- Domínio de treinamento focado em textos judiciais, não em documentos de licitação/contratação pública

---

## Applicabilidade Zelox

**MÉDIA para embeddings gerais, ALTA como backbone para fine-tuning de NER em entidades de DO.**

Para embeddings de busca semântica, Legal-BERTimbau-sts-large pode ser superior (específico para STS). Para fine-tuning de um NER de entidades de licitação (CNPJ, valor, modalidade, objeto), LegalBert-pt é o melhor ponto de partida disponível — o domínio jurídico geral é mais próximo do domínio de licitação do que BERTimbau-base.

---

## Conexões

- Complementa: Legal-BERTimbau-sts-large (Rufimelo) para busca semântica
- Baseline para: fine-tuning de NER em entidades de DO brasileiro
- Relaciona com: GovBert-BR (silva-pappa-2024-govbert-br.md) — alternativa específica para documentos governamentais
