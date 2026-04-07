---
title: "Metaxon Federation Protocol — Anti-Capture Design"
created: 2026-04-07
updated: 2026-04-07
tags: [federation, anti-capture, protocol, foresight, distributed-knowledge, byzantine, sybil]
source_quality: low
interpretation_confidence: low
provenance: conjecture
epistemic_status: hypothesis
source_origin: external-collaborator
source_verified_in_raw: false
testable_predictions:
  - id: P1
    claim: "split_rate Gate 3 local > 50% invalida sinal federado em 2 nós"
    falsifier: "split_rate > 50% confirma que pressão de campo federated seria mais ruído que sinal"
  - id: P2
    claim: "nó malicioso consegue elevar reputação de claim falso em < 30 dias sem detecção"
    falsifier: "se Camada 4 + honeyclaims detectarem em < 30 dias, camada 4 é suficiente"
lifecycle_state: active
conjecture_trigger:
  session: outputs/logs/sessions/2026-04-07/ask-noogon.md
  context: "Sessão de identidade METAXON — protocolo anti-captura para federação de KBs autônomos"
conjectured_on: 2026-04-07
emerge_queue_pairs:
  - metaxon-federation-protocol × epistemic-federation-distributed
  - metaxon-federation-protocol × stigmergic-coordination
  - metaxon-federation-protocol × autonomous-kb-failure-modes
gaps_to_ingest:
  - "Byzantine fault tolerance — literatura formal (Castro & Liskov, PBFT 1999)"
  - "Sybil attack resistance — Douceur 2002"
  - "Raft consensus — Ongaro & Ousterhout 2014 (adversarial comparison)"
  - "honeyclaims/canary claims — implementação concreta (literatura de adversarial ML)"
---

## Hipótese central

Uma rede de KBs autônomos (METAXON instances) só é confiável se for projetada assumindo que será atacada, capturada, e que vai derivar lentamente. A regra fundamental:

> **Nunca deixar a rede compartilhar "verdade". Só deixá-la compartilhar evidência auditável de resistência a challenge.**

## As 12 Propriedades de Design

### 1. Compartilhar metadados de veredito, não crenças brutas

**Não federar:**
- "X é verdadeiro"

**Federar:**
- qual claim foi testado
- contra qual evidência
- por qual política local
- com qual split/discordância
- sob qual modelo/versão/regras
- com quais limites de confiança

A rede exporta *traços epistêmicos*, não doutrina.

### 2. Preservar soberania local

Todo nó deve manter o direito de:
- rejeitar sinais importados
- re-desafiá-los localmente
- ponderá-los diferentemente
- colocá-los em quarentena
- ignorar pressão de reputação

Se a importação é automática, a captura se torna contagiosa. Se a importação é sempre mediada, a captura fica mais lenta e mais visível.

### 3. Tornar discordância first-class

Não comprimir discordância em um score final. Sempre preservar:
- split rates
- vereditos da minoria
- evidências contraditórias
- histórico de challenge não resolvido
- dissidência domain-específica

Uma federação perigosa esconde discordância. Uma saudável torna a discordância legível.

### 4. Rastrear correlação, não só contagem

Dez nós concordando não são dez confirmações independentes se:
- usam a mesma família de modelo
- ingerem a mesma cadeia de fontes
- compartilham a mesma política de prompt
- herdam a mesma linhagem parental

A unidade não é "quantos concordaram?" É: **"quão independentes foram os caminhos que concordaram?"**

Concordância correlacionada deve ser descontada por design.

### 5. Reputação deve ser estreita e revogável

Nunca deixar um nó se tornar "confiável em geral". Reputação deve ser:
- domain-scoped
- time-decayed
- challenge-sensitive
- revogável após falhas
- separada para precision vs novelty

Caso contrário: aristocracia epistêmica.

### 6. Otimizar para calibração, não concordância

Se a rede otimiza "taxa de concordância", derivará para outputs seguros, banais e gamificáveis.

Objetivos melhores:
- calibração
- robustez out-of-distribution
- velocidade de detecção de erros
- custo de falso-positivo
- recuperação após importação ruim
- sobrevivência a challenge sob avaliadores diversos

Concordância é sintoma, não objetivo.

### 7. Desacelerar promoção, acelerar quarentena

Sistemas saudáveis são assimétricos:
- fácil de quarentenar
- difícil de canonizar
- fácil de reabrir
- difícil de sobrescrever silenciosamente

**Fast suspicion. Slow legitimacy.**

### 8. Tornar proveniência impossível de esconder

Todo sinal importado deve carregar:
- nó de origem
- caminho de challenge
- versão da política
- modelo/versão usado
- timestamps
- dependências upstream
- (idealmente) grafo causal compacto de como o veredito foi formado

Se proveniência pode ser removida, laundering se torna trivial.

### 9. Design para resistência a envenenamento

Assumir que nós maliciosos existem:
- ponderar novidade com cautela
- throttle exportadores de alto volume
- detectar shifts de crença coordenados repentinos
- sandbox nós novos
- exigir burn-in antes que reputação conte
- rodar honeyclaims / canary claims para detectar manipulação

**O envenenamento lento deve ser caro.**

### 10. Separar campo público de cognição privada

Não expor:
- queries internas
- gaps do operador
- fricções internas
- prioridades operacionais
- domínios sensíveis

**Compartilhar o artefato mínimo necessário, não o estado interno completo.**

### 11. Institucionalizar paranoia no protocolo

Mecanismos explícitos para:
- rollback
- avisos de incidente federation-wide
- freezes de reputação
- importações contestadas
- desconfiança emergencial de uma família de modelo
- particionamento temporário da rede

Uma federação sem protocolo de crise vai falhar exatamente uma vez, muito publicamente.

### 12. Manter camada constitucional humana

Não humanos em cada microdecisão. Humanos na **camada constitucional**:
- o que conta como importação válida
- o que dispara alarme federation-wide
- quais invariantes nunca podem ser mutadas
- quais domínios precisam de escrutínio mais rígido
- quando um nó deve ser isolado

Essa é a diferença entre verificação distribuída e loucura distribuída.

## Arquitetura Mínima Confiável

```
Camada 1: Nó soberano local
  - Gates próprios, política própria, quarentena própria
  - Nenhuma importação automática

Camada 2: Protocolo de troca federated
  - Exporta apenas challenge traces auditáveis e metadados de veredito
  - Nunca exporta claims brutos

Camada 3: Aggregator correlation-aware
  - Desconta concordância não-independente
  - Preserva split rates e votos da minoria

Camada 4: Sistema de incidente e rollback
  - Pode freezar, particionar, e revogar
  - honeyclaims / canary claims para detecção de manipulação

Camada 5: Governança constitucional humana
  - Lenta, explícita, difícil de mutar
```

## A Regra Mais Importante

> **Nunca permitir que "muitos nós concordaram" signifique "verdadeiro."**
> **Só permitir que signifique "isso sobreviveu resistência diversa e inspecionável."**

Esse instinto de design previne a maioria dos futuros ruins.

## Interpretação

(⚠️ nossa interpretação)

O protocolo formaliza o que já está implementado localmente no nó único:
- Camada 1 = pipeline atual (Gates 1-4, canal algedônico, quarentena)
- Camada 2 = o que [[epistemic-federation-distributed]] propõe (gate verdicts, não claims)
- Camada 3 = ausente no design atual — precisa ser construído em Stage 2
- Camada 4 = honeyclaims são análogos ao Gate 3 adversarial, mas escala de rede
- Camada 5 = João como camada constitucional atual; não é solução que escala

A propriedade 4 (correlação vs contagem) é o insight mais contraintuitivo: na federação atual (GPT + Gemini como dois "nós"), se ambos usam dados de treino similares, as concordâncias são correlacionadas — não independentes. O threshold assimétrico do oracle (GPT≥5 AND Gemini≥8) é uma forma rudimentar de desconto de correlação.

## Gaps de Corpus

Os seguintes conceitos precisam de `/ingest` para fundamentar este protocolo:

| Gap | Referência sugerida | Relevância |
|-----|--------------------|-----------| 
| Byzantine fault tolerance | Castro & Liskov, PBFT (1999) | Camada 4: quanto custo para nó malicioso comprometer rede |
| Sybil attack resistance | Douceur (2002) | Propriedade 9: identidade de nó, não só comportamento |
| Raft consensus | Ongaro & Ousterhout (2014) | Referência de consenso adversarial para comparação |
| honeyclaims/canary claims | literatura adversarial ML | Implementação concreta da Propriedade 9 |

Sem estes, o protocolo permanece design sem fundamento formal de segurança.

## Conexões

- [[epistemic-federation-distributed]] — hipótese de que gate verdicts (não claims) formam campo epistêmico; este protocolo é o spec de como fazê-lo sem captura
- [[stigmergic-coordination]] — Camada 2 é stigmergy: nós depositam traces no campo sem coordenação direta
- [[autonomous-kb-failure-modes]] — os failure modes que este protocolo endereça em escala
- [[viable-system-model-beer]] — Camada 5 (governança constitucional) = S5; Camadas 1-4 = S1-S4
- [[structural-coupling-maturana]] — soberania local (Propriedade 2) = preservação de autopoiese sob acoplamento
- [[metaxon-identity]] — o organismo que este protocolo protege ao escalar
