# BitsAI-CR: Automated Code Review via LLM in Practice

**Autores:** Tao Sun, Jian Xu, Yuanpeng Li, Zhao Yan, Ge Zhang, Lintao Xie, Lu Geng, Zheng Wang, Yueyan Chen, Qin Lin, Wenbo Duan, Kaixin Sui
**Instituição:** ByteDance
**Publicação:** arXiv:2501.15134 [cs.SE]
**Ano:** 2025 (janeiro)
**URL:** https://arxiv.org/abs/2501.15134
**Tipo:** paper / primary

---

## Metodologia

- Deployment em produção na ByteDance
- **12.000+ Weekly Active Users (WAU)**
- Foco em Go (linguagem predominante na ByteDance)
- Métrica central inovadora: **Outdated Rate** — percentual de comentários automatizados que se tornam "desatualizados" (developer modifica o código após o comentário, sinalizando adoção ou resolução implícita)

## Arquitetura do Sistema

### Two-stage pipeline

**Stage 1 — RuleChecker:**
- Detecção inicial de issues baseada em taxonomia de review rules
- Alta cobertura, menor precisão

**Stage 2 — ReviewFilter:**
- Verificação de precisão das issues detectadas pelo Stage 1
- Filtra falsos positivos antes de enviar ao developer
- Aumenta precisão de ~X% para 75%

### Mecanismos de melhoria contínua

**Data Flywheel:**
- Feedback estruturado dos developers alimenta retreinamento
- Métricas de avaliação automatizadas permitem otimização em escala
- Outdated Rate como proxy de adoção real (não requer label manual)

**Taxonomy of Review Rules:**
- Conjunto estruturado de regras categorizadas por tipo de problema
- Base para o RuleChecker

## Achados principais

### Performance

| Métrica | Valor |
|---------|-------|
| Precisão geral | **75.0%** |
| Outdated Rate (Go) | **26.7%** |
| Weekly Active Users | **12.000+** |

### Outdated Rate como métrica

Inovação metodológica: em vez de medir se o developer explicitamente "resolveu" o comentário, mede se o código mudou após o comentário — proxy de impacto real, automatizável sem custo de anotação manual.

Outdated Rate de 26.7% para Go significa: 26.7% dos comentários gerados levaram a mudança de código (estimativa de adoção real).

## Interpretação dos dados (autores)

O sistema demonstra viabilidade de automated code review em escala industrial com alta precisão. A arquitetura two-stage (detect + filter) é chave para atingir 75% de precisão sem sacrificar cobertura. O data flywheel permite melhoria contínua sem annotation manual intensiva.

## Limitações

- Resultados específicos para ByteDance (Go predominante, escala muito grande)
- Outdated Rate é proxy — não captura casos onde developer rejeita conscientemente o comentário e não muda o código
- Taxonomia de rules não divulgada completamente (proprietary)
- Não compara com revisores humanos diretamente
