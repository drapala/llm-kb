---
title: "Collaborative Memory and Access Control"
sources:
  - path: raw/papers/rezazadeh-2025-collaborative-memory-access-control.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-05
updated: 2026-04-05
tags: [multi-agent, memory, access-control, world-model, single-brain, provenance]
source_quality: high
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-05
quarantine: false
---

## Resumo

Rezazadeh et al. (Accenture, 2025): primeiro sistema que formaliza compartilhamento de memória entre agentes em ambientes multi-usuário/multi-agente com controles de acesso assimétricos e time-varying. Grafos bipartidos G_UA(t) e G_AR(t) codificam permissões. Memória dual (privada + compartilhada) com provenance imutável por fragmento. Conflitos resolvidos via provenance validation em read-time. Resultado empírico: -61% chamadas de recurso com 50% overlap de queries entre usuários.

## Conteúdo

### Formalização

**Grafos de acesso bipartidos (time-dependent):**
- G_UA(t) ⊆ U × A: quais usuários podem invocar quais agentes em t
- G_AR(t) ⊆ A × R: quais agentes acessam quais recursos em t

**Fragmento acessível a usuário u via agente a em t:**
```
M(u,a,t) := {m ∈ M | A(m) ⊆ A(u,t) ∧ R(m) ⊆ R(a,t)}
```
Fragmento visível apenas se TODOS os agentes e recursos que o criaram estão nas permissões atuais do principal.

### Arquitetura dual de memória

| Tipo | Conteúdo | Quem acessa |
|------|----------|-------------|
| M^private | Fragmentos exclusivos do usuário | Só o usuário originador |
| M^shared | Fragmentos compartilháveis | Qualquer usuário com permissão |

**Provenance imutável por fragmento:**
- T(m): timestamp de criação
- U(m): usuário originador
- A(m): conjunto de agentes contribuintes
- R(m): recursos acessados na criação

### Políticas de leitura e escrita

**Read policy:** transforma M(u,a,t) em view filtrada. Modo simples (verbatim) ou transformação (LLM redige/anonimiza informações específicas do usuário).

**Write policies (duas, independentes):**
- write/private: controla o que persiste em M^private
- write/shared: controla o que persiste em M^shared — LLM remove informações específicas do usuário, mantém "informação universal"

**Escopos:** global, per-user, per-agent, temporal.

### Resolução de conflitos e temporalidade

**Provenance validation (read-time, não retroativa):**
Memória escrita em t₀ sob permissões P₀ pode tornar-se inacessível em t₁ se P₁ não inclui A(m) ou R(m). O fragmento não é deletado — apenas excluído da view M(u,a,t₁). Permissões futuras podem restaurar o acesso.

Isso resolve conflitos por exclusão de provenance, não por merge de conteúdo — fragmentos conflitantes de diferentes usuários não colidem porque ficam em M^private separados ou, se compartilhados, passaram pela transformação write/shared que remove especificidades.

### Resultados

| Cenário | Dataset | Resultado chave |
|---------|---------|-----------------|
| Colaboração total | MultiHop-RAG, 5 usuários, 6 agentes | -61% resource calls com 50% overlap |
| Assimétrico | 200 queries sintéticas, 4 papéis | Redução mesmo com visibilidade restrita |
| Dinâmico | SciQAG, 8 blocos temporais | Accuracy rastreia permissões; reutilização de fragmentos reduz chamadas |

### Stack de implementação

Coordinator LLM → seleciona agentes de A(u,t,q) → agentes executam ferramentas → memory encoder gera fragmentos key-value com provenance → retrieval por cosine similarity (top-k_user de M^private + top-k_cross de M^shared com provenance check) → Aggregator LLM sintetiza resposta.

## Interpretação

### Conexão com Single Brain (⚠️ nossa síntese)

Este paper resolve o **read-time conflict resolution** com granularidade maior do que Hindsight. Enquanto Hindsight separa por tipo epistêmico (World/Experience/Opinion/Observation), Collaborative Memory separa por origem e permissão.

**Mapeamento para Single Brain:**

| Conceito Collaborative Memory | Single Brain equivalent |
|-------------------------------|------------------------|
| M^private | Dados específicos do contexto (PP, AG, Zelox — isolados) |
| M^shared | World model compartilhado entre agentes especializados |
| Provenance T(m), U(m), A(m), R(m) | Rastreabilidade de cada claim no world model |
| G_UA(t) + G_AR(t) | Permissões: qual agente lê qual parte do world model |
| Write/shared com transformação | Processo de destilação de Experience → Observation em Hindsight |

**O que resolve além de Hindsight:** Hindsight define o que armazenar em cada rede (ontologia). Collaborative Memory define quem pode acessar o quê e quando (controle de acesso). São complementares, não substitutos.

**O que NÃO resolve:** update-time ordering — o problema de quando writes concorrentes de múltiplos agentes se tornam visíveis uns para os outros. Collaborative Memory resolve visibilidade via permissões, mas não sequenciamento de writes concorrentes. Esse gap permanece em [[multi-agent-memory-consistency]].

### Limitação importante

O sistema usa LLM para write/shared transformation ("redija informações específicas do usuário"). Isso introduz variabilidade — LLMs podem redagir de forma inconsistente ou incompleta. O paper não mede a qualidade da transformação isoladamente, só o efeito sistêmico.

## Verificação adversarial

**Claim mais fraco:** "-61% resource calls" — medido em MultiHop-RAG com 5 usuários e 6 agentes especialistas com overlap de domínio. Este cenário é favorável para colaboração (queries com domínios compartilhados). Em cenários com baixo overlap ou alta assimetria de informação, a redução pode ser próxima de zero.

**O que o paper NÃO diz:**
1. Não mede latência da provenance validation em escala (100M+ fragmentos)
2. Não mede qualidade da transformação write/shared isoladamente
3. Não testa adversarially — um agente tentando acessar fragmentos fora de suas permissões via engenharia de prompt

**Simplificações feitas:**
- O paper usa datasets relativamente pequenos (≤2.556 queries). Comportamento em escala do world model do Single Brain (300M vetores PNCP) não validado.

**Prior work:**
- ABAC (Attribute-Based Access Control) — formalismo de segurança que o paper estende
- MemGPT, AutoGen — citados como trabalhos sem controle de acesso formal

## Conexões

- validates: [[single-brain-data-ontology]] — provenance tracking (T/U/A/R por fragmento) formaliza rastreabilidade da rede Experience (ℬ) de Hindsight; write/shared policy mapeia para processo de destilação Experience→Observation
- complements: [[multi-agent-memory-consistency]] — resolve read-time conflict via provenance; não resolve update-time ordering (gap explícito)
- partOf: [[agent-memory-architectures]] — instância de controle de acesso em arquiteturas de memória multi-agente
- contradicts: [[multi-agent-orchestration]] ON "coordinator centraliza conhecimento" — M^private preserva conhecimento isolado mesmo em sistema multi-agente; compartilhamento é opt-in via write/shared policy

## Fontes

- [Rezazadeh et al. 2025](../../raw/papers/rezazadeh-2025-collaborative-memory-access-control.md) — grafos bipartidos G_UA/G_AR, dual memory, provenance imutável, -61% resource calls

## Quality Gate
- [x] Wikilinks tipados: 4 (validates, complements, partOf, contradicts)
- [x] Instance→class: -61% qualificado como "cenário MultiHop-RAG, 5 usuários, 6 agentes, 50% overlap"
- [x] Meta-KB separado: Single Brain mapping em Interpretação
- [x] Resumo calibrado: "primeiro sistema que formaliza" qualificado como claim dos próprios autores
