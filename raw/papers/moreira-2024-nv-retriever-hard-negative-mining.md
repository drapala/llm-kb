# NV-Retriever: Improving text embedding models with effective hard-negative mining

**ArXiv:** 2407.15831  
**Publicado:** 22 July 2024  
**URL:** https://arxiv.org/abs/2407.15831  
**Autores:** Gabriel de Souza P. Moreira, Radek Osmulski, Mengyao Xu, Ronay Ak, Benedikt Schifferer, Even Oldridge — NVIDIA

---

## Abstract

Text embedding models have been popular for information retrieval applications such as semantic search and RAG. Those models are Transformer models fine-tuned with contrastive learning objectives. One challenging aspect is the selection of high quality hard-negative passages for contrastive learning. We introduce a family of positive-aware mining methods that use the positive relevance score as an anchor for effective false negative removal, leading to faster training and more accurate retrieval models. NV-Retriever-v1 scored 60.9 on MTEB Retrieval (BEIR) benchmark, placed 1st when published (July 2024).

---

## Conceito Central: Hard Negative Mining

No treinamento contrastivo de embedding models:
- **Positivos:** par (query, documento relevante)
- **Negatives aleatórios:** documentos irrelevantes — fáceis demais; pouco sinal de aprendizado
- **Hard negatives:** documentos semanticamente similares mas não relevantes — forçam o modelo a discriminar melhor

### O Problema: False Negatives

Hard negatives de alta qualidade às vezes SÃO relevantes (falsos negativos). Incluí-los como negativos degrada o modelo — o modelo aprende a se afastar de documentos relevantes.

### Solução: Positive-Aware Mining

NV-Retriever usa o **relevance score do positivo** como âncora:
- Um candidato a negative só é aceito se seu score é significativamente menor que o score do positivo
- Remove false negatives antes do treinamento
- Resultado: treinamento mais rápido, modelos mais precisos

---

## Resultados

- **NV-Retriever-v1:** MTEB Retrieval (BEIR) = **60.9** — 1º lugar quando publicado em Julho 2024
- Ablation study mostra que positive-aware mining supera standard hard-negative mining em todas as configurações testadas
- Funciona com diferentes teacher models e base models

---

## Relevância para Zelox

Para fine-tuning de embeddings em corpus de DOs/licitações:

1. **False negative problem é crítico em domínio jurídico:** dois extratos de contrato similares podem ambos ser relevantes para a mesma query → se tratados como negatives, degradam o modelo
2. **Positive-aware mining** é a abordagem correta para corpus com documentos semanticamente próximos (DOs têm muitos atos boilerplate)
3. **Custo:** requer teacher model para score os candidatos — overhead comparado a random negatives

---

## Limitações

- Avaliado em BEIR (inglês) — transferência para PT-BR/domínio administrativo não testada
- Requer teacher model para scoring de candidatos (custo adicional de inference)
- NV-Retriever-v1 específico; metodologia de mining é mais geral
