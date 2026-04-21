# Neurosymbolic AI for Reasoning over Knowledge Graphs: A Survey

**Autores:** Lauren Nicole DeLong, Ramon Fernández Mir, Jacques D. Fleuriot (University of Edinburgh, AI and its Applications Institute)  
**Publicação:** IEEE Transactions on Neural Networks and Learning Systems (TNNLS)  
**DOI:** 10.1109/TNNLS.2024.3420218  
**arXiv ID:** 2302.07200  
**Ano:** 2024 (v1: fev 2023; publicado TNNLS: mai 2024)  
**URL:** https://arxiv.org/abs/2302.07200  
**Tipo:** paper / primary (survey fundacional)

---

## Tese central

Sistemas de raciocínio em knowledge graphs são mais robustos quando combinam raciocínio simbólico com deep learning — o ponto cego de abordagens puramente simbólicas (completude, escalabilidade) e puramente neurais (interpretabilidade, integração de conhecimento especialista). O paper propõe taxonomia de 3 categorias para classificar abordagens neurossimbólicas em KGs.

## Taxonomia de 3 Categorias

### 1. Logically-Informed Embedding Approaches
Métodos de embedding moldados por constraints lógicas. O processo de geração de embeddings incorpora informação lógica — seja como regularização, como loss term, ou como estrutura do espaço de embedding.

Exemplos: embeddings de entidades e relações treinados com penalidade por violação de regras lógicas conhecidas.

### 2. Embedding Approaches with Logical Constraints
Representações numéricas (embeddings) augmentadas com regras lógicas no momento de inferência ou treinamento. Diferente da categoria 1: o embedding é aprendido primeiro, depois constraints lógicos são aplicados para filtrar, reranquear, ou validar outputs.

### 3. Rule Learning Approaches
Sistemas que descobrem regras simbólicas a partir de dados. Em vez de receber regras como input, aprendem padrões regularidades no KG e as codificam como regras lógicas. Mais interpretável; mais generalista.

## Gap Endereçado

O survey endereça o gap entre:
- Abordagens tradicionais baseadas em regras (interpretável, mas incompleto e não-escalável)
- Abordagens baseadas em embedding (alta performance, mas caixa-preta)

Neurossimbólico combina os dois: mantém interpretabilidade de componentes simbólicos e capacidade de aprendizado de componentes neurais.

## Recursos

- Repositório GitHub: NeSymGraphs (código de modelos surveyed)
- 21 páginas, 6 figuras, 2 tabelas
- 3 versões no arXiv (última: maio 2024)
