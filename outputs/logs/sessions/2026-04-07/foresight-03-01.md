---
session_id: 2026-04-07-03-01
type: foresight
---

## Hipótese capturada

Federação Epistêmica Distribuída

## Campos

hypothesis: >
  Uma rede de organismos de conhecimento autônomos que co-evoluem via
  perturbações verificadas pode constituir a primeira infraestrutura
  epistêmica distribuída — pressão de campo emerge de verificações
  independentes, sem autoridade central.

testable_prediction: >
  Gate 3 split_rate < 30% valida viabilidade de sinal; split_rate > 50%
  falsifica o mecanismo. Teste formal requer segundo clone com corpus ≥30% sobreposto.

epistemic_status: hypothesis

premises:
  - autopoiese de instâncias individuais funciona sem coordenação central
  - gate verdicts são o primitivo transferível (não claims em prosa)
  - decay natural é computável via sessions_since_verification
  - gap aggregation é derivável de /ask failures distribuídos

architectural_consequences:
  - protocolo de federação: formato canônico de gate verdicts
  - DisturbanceEvent como primitivo com federation_origin
  - decay function: claim_pressure = base_score × exp(-λ × sessions)
  - gap aggregation como novo primitivo de /ask federated
  - epistemic_status comparável entre instâncias (normalização por approval_rate)

horizon: persistent

## Arquivo criado

wiki/strategy/epistemic-federation-distributed.md

## emerge_queue

Adicionado par:
  [strategy/epistemic-federation-distributed] × [concepts/stigmergic-coordination]
  stability: stable (stigmergic-coordination promovido)
  connection: campo federated = estigmergia de gate verdicts

Não elegível por serem conjectures:
  × structural-coupling-maturana (L0, sem raw/, quarentena)
  × viable-system-model-beer (verificar quarantine status — não adicionado por precaução)
