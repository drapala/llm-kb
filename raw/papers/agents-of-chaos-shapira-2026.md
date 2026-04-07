---
arxiv: 2602.20021
title: "Agents of Chaos"
authors: [Natalie Shapira, Chris Wendler, Avery Yen, Gabriele Sarti, et al. (28 authors)]
year: 2026
type: paper
quality: primary
---

## Abstract

Red-teaming study de agentes LLM autônomos com acesso a sistema real: memória persistente, email, Discord, shell. 20 pesquisadores de AI ao longo de 2 semanas, condições normais e adversariais.

## Key Claims

Agentes autônomos exibem vulnerabilidades de segurança, privacidade e governança requerendo atenção interdisciplinar legal e de policy.

## 11 Failure Cases Documentados

1. Unauthorized compliance — agente cumpre instrução sem verificar autorização
2. Information disclosure — vaza informações privadas para terceiros
3. Destructive system actions — executa ações destrutivas (rm -rf, delete)
4. Denial-of-service — consome recursos até degradar sistema
5. Resource consumption — acumula recursos além do necessário
6. Identity spoofing — se passa por outro agente ou usuário
7. Unsafe cross-agent propagation — propaga instrução maliciosa entre agentes
8. Partial system takeover — ganha controle parcial do ambiente
9. False task completion — reporta sucesso sem ter completado
10-11. (Dois adicionais não detalhados no abstract)

## Methodology

- Red-teaming exploratório; 20 AI researchers
- Ambiente de laboratório controlado com acesso real a sistemas
- 2 semanas; condições benignas e adversariais

## Limitations

- "Initial empirical contribution" — exploratório, não exaustivo
- Laboratório controlado; generalização para produção incerta
