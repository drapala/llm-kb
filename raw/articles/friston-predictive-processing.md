---
source: Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience, 11(2), 127-138.
author: Karl Friston
date: 2010-01-01
type: article
quality: primary
stance: neutral
---

# Friston — Predictive Processing / Free Energy Principle

## Fonte primária

Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience, 11(2), 127-138.

Nota: o Free Energy Principle é um framework extenso com muitos papers. O 2010 Nature Reviews é o overview mais citado. Para formalismos: Friston (2009) "The free-energy principle: a rough guide to the brain."

## Conceito central

O cérebro é uma máquina de predição que minimiza "free energy" — um upper bound na surpresa (negative log-likelihood) de inputs sensoriais dado um modelo generativo do mundo.

**Percepção** = inferência sobre causas dos inputs sensoriais (inverter o modelo generativo).
**Ação** = modificação do mundo para confirmar predições (reduzir prediction error via mudança de inputs).
**Aprendizado** = atualização do modelo generativo para melhor prever inputs futuros.

## Formulação

F = surprise + complexity = -log p(sensory data | model)

Minimizar F é equivalente a:
1. Maximizar evidence para o modelo do mundo (model evidence)
2. Minimizar surpresa dos inputs sensoriais
3. Minimizar prediction error

O sistema age para minimizar prediction error de duas formas:
1. **Atualizar o modelo** (perceptual inference / learning) — mudar crenças para se ajustar aos dados
2. **Mudar o ambiente** (active inference / action) — mudar dados para se ajustar às crenças

## Active Inference

Extensão de predictive processing para agentes embodied:
- Agentes não apenas percebem — AGEM para confirmar predições
- Comportamento = minimização de free energy via ação
- Unifica percepção, ação e aprendizado num único princípio variacional
- Preferências (goals) são encoded como prior beliefs sobre estados futuros esperados

## Hierarchical Predictive Processing

O cérebro é hierárquico:
- Cada nível prediz a atividade do nível abaixo
- Prediction errors propagam UPWARD (bottom-up)
- Predictions propagam DOWNWARD (top-down)
- Atenção = modulação da precisão (gain) dos prediction errors

[verificar: a hierarquia de predictive processing é de Rao & Ballard (1999), formalizada por Friston em termos de free energy]

## Aplicações documentadas

- **Neurociência:** modelo de percepção visual, auditiva, proprioceptiva. Ilusões ópticas = priors override sensory evidence.
- **Psiquiatria:** delírio = priors muito rígidos; ansiedade = prediction error precision muito alta; depressão = learned helplessness via free energy landscape. [verificar — estas aplicações são de Clark (2013), Stephan et al. (2016)]
- **Robotics:** agentes que aprendem por active inference (Tschantz et al., 2020)
- **LLMs:** [verificar] área emergente 2024-2026. Alguns pesquisadores modelam LLMs como implementações implícitas de predictive processing (next token prediction = minimização de surprise). Controverso.

## O que Friston NÃO afirma

- **Não é teoria exclusiva do cérebro** — é princípio variacional geral aplicável a qualquer sistema que mantém integridade contra perturbações (Friston: "any system that resists the second law of thermodynamics")
- **Não é falsificável trivialmente** — o framework é suficientemente geral para acomodar muitos comportamentos post-hoc. Crítica: se explica tudo, não prediz nada específico. [verificar — Friston respondeu a esta crítica em Friston (2012) "A Free Energy Principle for Biological Systems"]
- **Free energy não é energia física** — é uma medida de estatística variacional (variational free energy), bound on surprise

## Limitações e controvérsias

1. **Crítica de tautologia:** "Todo sistema que persiste minimiza free energy" é verdade por definição? Ou é predição empírica? Debate ativo. [verificar — Andrews (2021) "The Math is not the Territory"]
2. **Implementação computacional complexa** — active inference agents requerem modelo generativo explícito, que é difícil de especificar para domínios complexos
3. **Relação com RL:** Active inference pode ser reformulada como RL com prior preferences (KL control). Controvérsia: é mais geral que RL ou é RL com terminologia diferente? [verificar — Millidge, Tschantz & Buckley (2021) "Whence the Expected Free Energy?"]
4. **Precision weighting:** O mecanismo de atenção (modular precisão dos prediction errors) é central mas sub-especificado — como o sistema DECIDE quais prediction errors são importantes?

> [editorial — não é de Friston]
> Conexão com anomalia verbal/self-assessment:
> Reflexion com testes = sistema minimiza prediction error
> via feedback externo (atualiza modelo generativo).
> Self-assessment sem ground truth = sistema tenta minimizar
> prediction error SEM dados externos — minimiza contra
> suas próprias predições → loop fechado → converge para
> estado de menor surpresa = confirmar o que já acredita.
>
> "LLM como amplificador" (nossa teoria) vs
> "LLM como prediction error minimizer" (Friston):
> Friston é mais geral — "amplificação" é caso especial
> onde o feedback externo é o prediction error signal.
> Com feedback: prediction error drives update → improvement.
> Sem feedback: system converges to minimum surprise state
> = maximum self-consistency = self-enhancement bias.
>
> Ashby connection: V(regulator) maps to model evidence.
> Low V(regulator) = poor generative model = high free energy
> = high surprise = poor regulation.
> Increasing V(regulator) = improving generative model.
>
> Predição: Friston prediz que self-assessment sem ground
> truth converge para o estado de MENOR SURPRESA para o
> modelo — que é confirmar o que já acredita.
> Isso é mais preciso que "amplifica vieses" — especifica
> O QUE é amplificado (o state of least surprise).
> Status: L1 (analogia). Não testado formalmente para LLM KBs.
