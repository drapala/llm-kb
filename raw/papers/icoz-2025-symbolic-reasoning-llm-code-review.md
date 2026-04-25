# Automated Code Review Using Large Language Models with Symbolic Reasoning

**Autores:** Büşra İçöz, Göksel Biricik
**Instituição:** Yıldız Technical University
**Publicação:** arXiv:2507.18476 [cs.SE, cs.AI]
**Ano:** 2025 (julho)
**URL:** https://arxiv.org/abs/2507.18476
**Tipo:** paper / primary

---

## Metodologia

- Dataset: CodeXGLUE (Python defect detection — snippets classificados como clean/buggy)
- Três modelos testados: CodeBERT, GraphCodeBERT, CodeT5
- Quatro cenários comparados:
  1. Base model (one-shot, sem knowledge map)
  2. Few-shot no base model
  3. Fine-tuned base model
  4. Hybrid (fine-tuned + few-shot + knowledge map)

## Knowledge Map

20 bug patterns e best practices Python incluídos no prompt como "symbolic reasoning":
- Naming anti-patterns (variáveis ambíguas)
- Unreachable code (after return/raise)
- Error handling risks (bare except, wrong exception types)
- Resource leaks (open() sem close())
- Mutable default arguments

## Achados principais

### Performance por configuração (GraphCodeBERT)

| Configuração | Accuracy |
|-------------|----------|
| Base model | 53.9% |
| Few-shot | 64.2% |
| Fine-tuned | 68.7% |
| **Hybrid** | **68.7%** |

GraphCodeBERT consistentemente melhor que CodeBERT e CodeT5.

### Melhoria geral com hybrid approach

- +16% accuracy sobre base LLMs em média
- Supera SYNCHROMESH (LLM + symbolic para code generation) que alcança +12%

### Trade-offs documentados

Precisão vs. recall: modelos com alta precisão (menos falsos positivos) têm recall menor (perdem alguns bugs). Para code review: depende do contexto — false positives são mais custosos que false negatives em termos de developer trust.

## O que "symbolic reasoning" significa aqui

Não é formal verification — é injetar estrutura de conhecimento explícita (knowledge map) no prompt. Similar ao SGCR explicit path, mas mais simples: um único mapa estático em vez de specs dinâmicas por projeto.

## Limitações

- Dataset apenas Python, apenas defect detection — escopo muito narrow
- Knowledge map de 20 padrões é estático e genérico (não project-specific)
- Não testa em PRs reais — apenas em snippets classificados
- GraphCodeBERT é modelo antigo (2021) — comparação com modelos frontier seria mais relevante

## Relação com outros papers

- Confirma que hybrid (LLM + estrutura explícita) > LLM puro — princípio compartilhado com SGCR
- Mas abordagem é muito mais primitiva que SGCR (mapa estático vs specs RAG-retrieved)
- Estabelece baseline para comparação com abordagens mais sofisticadas
