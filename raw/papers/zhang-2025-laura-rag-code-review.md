# LAURA: Enhancing Code Review Generation with Context-Enriched Retrieval-Augmented LLM

**Autores:** Yuxin Zhang, Yuxia Zhang, Zeyu Sun, Yanjie Jiang, Hui Liu
**Publicação:** arXiv:2512.01356 [cs.SE]
**Ano:** 2025 (dezembro)
**URL:** https://arxiv.org/abs/2512.01356
**Tipo:** paper / primary

---

## Metodologia

- Framework: GPT-4o e DeepSeek v3 com RAG + exemplar retrieval + context augmentation
- Construção de high-quality dataset (datasets existentes têm muito ruído)
- Avaliação: % de comentários "completely correct or at least helpful"

## Arquitetura LAURA

### Três componentes

1. **Review exemplar retrieval** — recupera exemplos de reviews de alta qualidade de PRs históricos similares
2. **Context augmentation** — aumenta o contexto do diff com informações relevantes do codebase
3. **Systematic guidance** — fornece orientação estruturada ao LLM sobre como conduzir o review

### Dataset de alta qualidade

Problema central: datasets existentes de code review são ruidosos — treinamento em dados ruins produz modelos ruins. LAURA constrói dataset curado.

## Achados principais

| Modelo | Performance (correct ou helpful) |
|--------|----------------------------------|
| LAURA + GPT-4o | **42.2%** |
| LAURA + DeepSeek v3 | **40.4%** |
| SOTA baselines | Significativamente inferior |

### Contribuição de cada componente (ablação)

Todos os três componentes (exemplar retrieval + context augmentation + systematic guidance) contribuem positivamente — nenhum é dispensável.

### Insight sobre dados

O problema com abordagens existentes não é só o modelo — é a qualidade dos dados de treinamento/retrieval. Reviews de baixa qualidade no contexto contaminam o output.

## Ligação com outros papers

- Exemplar retrieval resolve parcialmente o problema de atenção diluída (SWE-PRBench): em vez de contexto bruto do codebase, recupera reviews históricos de alta qualidade semanticamente similares
- Alinha com RovoDev (RAG para context assembly) e SGCR (quality filtering antes do output)
- A curação de dataset é o mesmo insight de Bouraffa 2025 sobre qualidade dos dados de treinamento

## Limitações

- Avaliação subjetiva ("at least helpful") dificulta comparação rigorosa
- Dataset curado pode não generalizar além dos projetos avaliados
- Não testa em ambiente de produção real (laboratorial)
