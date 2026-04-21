# Artificial Intelligence for Software Architecture: Literature Review and the Road Ahead

**Autores:** Alessio Bucaioni (Mälardalen University, Sweden), Martin Weyssow, Junda He, Yunbo Lyu, David Lo (Singapore Management University)  
**Publicação:** arXiv  
**arXiv ID:** 2504.04334  
**Ano:** 2025 (fevereiro 2025)  
**URL:** https://arxiv.org/html/2504.04334v1  
**Tipo:** paper / secondary (systematic literature review)

---

## Tese central

AI aplicada ao nível de **arquitetura de software** (não código) permanece subdesenvolvida. Enquanto AI avança em tarefas de nível de código, o raciocínio arquitetural de alto nível — trade-offs, decisões de design, evolução de sistemas — é ainda domínio humano. O paper mapeia o estado atual e propõe direções.

## Metodologia

- Revisão sistemática seguindo diretrizes Kitchenham
- 4 bases de dados (IEEE Xplore, ACM, SCOPUS, Web of Science)
- 446 estudos iniciais → 35 estudos primários selecionados
- Integração com 17 desafios identificados por practitioners (32 entrevistas)
- Grounded theory para síntese

## 14 Contribuições AI Atuais em Software Architecture

Organizadas em dois clusters:

### Cluster 1 — Design e Decisão (6 tópicos)
1. Geração de candidatos arquiteturais via LLM a partir de requisitos
2. Reconhecimento de padrões arquiteturais via ML
3. Análise de Architecture Decision Records (ADRs)
4. Suporte a tomada de decisão arquitetural
5. Representação de conhecimento arquitetural
6. Geração de decisões de design

### Cluster 2 — Evolução e Adaptação (8 tópicos)
1. Adaptação de componentes ML
2. Architecture recovery / engenharia reversa
3. Otimização de gerenciamento de recursos
4. Estimativa de performance
5. Automação industrial
6. Suporte a refactoring
7. Melhoria de resiliência
8. Quality-of-Service improvements

## 6 Desafios AI-Específicos (AICH) em Arquitetura

| ID | Desafio |
|----|---------|
| AICH1 | Mover além de recomendações únicas para adaptação contínua |
| AICH2 | Garantir rastreabilidade entre código em evolução e documentação |
| AICH3 | Raciocínio contextual além de pattern matching |
| AICH4 | Incorporar expertise de domínio e interpretabilidade |
| AICH5 | Aprender de decisões passadas e refinar métricas dinamicamente |
| AICH6 | Integrar diagnósticos multi-nível com redução de technical debt |

## 6 Direções Futuras Propostas

1. **Monitoramento em tempo real e auto-adaptação** — health arquitetural contínuo com refinamento autônomo
2. **Documentação automatizada e rastreabilidade** — extração dinâmica de conhecimento alinhada com mudanças do sistema
3. **AI context-aware e explicável** — raciocínio domain-specific com justificativas transparentes via RAG e LLMs
4. **Otimização multi-objetivo** — balancear performance, manutenibilidade, segurança, e custo via RL
5. **Diagnósticos multi-nível integrados** — modelos de grafo correlacionando issues entre níveis de abstração
6. **Benchmarks e estudos industriais** — geração de dados sintéticos e integração com workflows reais

## Relevância

O paper documenta o gap entre AI aplicada ao código (madura) e AI aplicada à arquitetura (nascente). É um mapa do que falta, não do que existe. Relevante como ponto de referência para identificar onde sistemas como os descritos por Vandeputte (2025) e Vasilopoulos (2026) se posicionam neste espaço.
