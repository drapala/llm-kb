# Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control

**Authors:** Alireza Rezazadeh, Zichao Li, Ange Lou, Yuying Zhao, Wei Wei, Yujia Bao (Accenture)
**arXiv:** 2505.18279
**Submitted:** May 2025

---

## Abstract

Framework para compartilhamento seguro de memória entre agentes especializados em ambientes multi-usuário. Propõe controles de acesso assimétricos e dinâmicos via grafos bipartidos, arquitetura dual (privado + compartilhado) com provenance imutável, e políticas de leitura/escrita com escopo configurável. Primeiro sistema que formula explicitamente assimetrias de acesso fino-granulares em sistemas multi-agente/multi-usuário.

---

## Formalização central

**Grafos de acesso bipartidos** (time-dependent):
- G_UA(t) ⊆ U × A: permissões usuário→agente no tempo t
- G_AR(t) ⊆ A × R: permissões agente→recurso no tempo t

Derivados:
- A(u,t) = agentes acessíveis ao usuário u em t
- R(a,t) = recursos acessíveis ao agente a em t

**Conjunto de fragmentos acessíveis:**
```
M(u,a,t) := {m ∈ M | A(m) ⊆ A(u,t) ∧ R(m) ⊆ R(a,t)}
```
Fragmento só é visível se TODOS os agentes e recursos que contribuíram para ele estão acessíveis ao principal atual.

---

## Arquitetura dual de memória

**Partição:**
- M^private: fragmentos exclusivos do usuário
- M^shared: fragmentos compartilháveis entre usuários

**Provenance por fragmento (imutável):**
- T(m): timestamp de criação
- U(m): usuário originador
- A(m): agentes contribuintes
- R(m): recursos acessados durante criação

---

## Políticas de leitura e escrita

**Read policy** (πᵘ'ᵃ'ᵗ_read): transforma M(u,a,t) em view filtrada.
- Modo simples: retorna fragmentos admissíveis verbatim
- Modo transformação: LLM redige/anonimiza/parafraseia

**Write policies (dual):**
- write/private: M^private(u,t) → M^private(u,t+1)
- write/shared: M^shared(u,t) → M^shared(u,t+1)

**Escopos de política:**
- Global: uniforme no sistema
- Per-user: regras específicas por usuário
- Per-agent: regras específicas por agente
- Temporal: regras dependentes do tempo

**Implementação:** prompts de sistema instruem LLM a redigir informações específicas do usuário ao escrever em M^shared, enfatizando "informação universal."

---

## Resolução de conflitos

**Provenance validation (read-time, não retroativa):**
Quando agente a em contexto de usuário u solicita memória, fragmentos são incluídos apenas se A(m) ⊆ A(u,t) ∧ R(m) ⊆ R(a,t). Fragmentos cujos agentes/recursos contribuintes saíram das permissões são automaticamente excluídos — sem deleção, apenas inacessibilidade.

**Time-varying enforcement:** memória escrita em t₀ sob uma permissão pode tornar-se inacessível em t₁ se A(m) ou R(m) não estiverem mais em A(u,t₁) ou R(a,t₁). Verificado em read-time, não retroativamente.

---

## Experimentos

### Cenário 1 — Totalmente colaborativo
- Dataset: MultiHop-RAG (609 artigos, 2.556 queries, 6 domínios)
- Setup: 5 usuários, 6 agentes especialistas, acesso exclusivo a 1 recurso cada
- Queries com overlap configurável: 0%, 25%, 50%, 75%
- **Resultado: -61% resource calls com 50% overlap, -59% com 75% overlap**

### Cenário 2 — Colaboração assimétrica
- Dataset: 200 queries sintéticas de negócios (100 fáceis, 100 difíceis)
- 4 usuários por papel (Pesquisador, Analista, Logística, Estratégia), 4 agentes com permissões heterogêneas
- Resultado: colaboração parcial reduz chamadas mesmo com visibilidade restrita

### Cenário 3 — Acesso dinamicamente evolutivo
- Dataset: SciQAG (5 categorias, 100 queries total)
- Acesso: Bernoulli edge addition then revocation em 8 blocos temporais
- Resultado: accuracy rastreia permissões disponíveis; resource usage decresce com reutilização de fragmentos

---

## Implementação

**Stack:**
- Coordinator LLM: seleciona agentes de A(u,t,q)
- Agentes: ferramentas via OpenAI function-calling
- Memory encoder: converte traces conversacionais em fragmentos key-value com provenance
- Memory retrieval: cosine similarity embedding; top-k_user de M^private + top-k_cross de M^shared satisfazendo provenance
- Aggregator LLM: sintetiza resposta final

---

## Relacionados
- MemGPT, MemTree, GraphRAG: single-agent memory — sem controle de acesso
- AutoGen, AgentVerse: multi-agent — sem gestão formal de memória compartilhada
- ABAC (Attribute-Based Access Control): estende com grafos bipartidos time-varying e provenance storage
