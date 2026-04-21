# Agent READMEs: An Empirical Study of Context Files for Agentic Coding

**Autores:** Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa, Brittany Reid, Kundjanasith Thonglek, Pattara Leelaprute, Arnon Rungsawang, Bundit Manaskasemsak, Bram Adams, Ahmed E. Hassan, Hajimu Iida  
**Publicação:** arXiv  
**arXiv ID:** 2511.12884  
**Ano:** 2025 (submissão: 17 nov 2025)  
**URL:** https://arxiv.org/abs/2511.12884  
**Tipo:** paper / primary (estudo empírico observacional)

---

## Tese central

Context files para agentic coding (CLAUDE.md, AGENTS.md, GEMINI.md, etc.) são artefatos complexos que evoluem como código de configuração — não como documentação estática. Análise de 2.303 arquivos em 1.925 repositórios.

## Dataset

- **2.303 context files** analisados
- **1.925 repositórios**
- Tools representadas: Claude Code, Copilot, Cursor, Gemini, e outros

## Achados sobre conteúdo

| Categoria de requisito | Prevalência |
|------------------------|-------------|
| Build/run commands | **62.3%** |
| Implementation details | **69.9%** |
| Architecture | **67.7%** |
| **Security** | **14.5%** |
| **Performance** | **14.5%** |

Gap central: requisitos funcionais dominam; requisitos não-funcionais (segurança, performance) aparecem em apenas ~14.5% dos context files.

## Achados sobre manutenção

Context files funcionam como **"complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions"** — não como documentação big-bang.

Padrão de manutenção: adições pequenas e frequentes, não rewrites. Isso implica:
- Bootstrap de qualidade é importante (garbage-in, garbage-out ao longo do tempo)
- Sem revisão periódica, acumula debt da mesma forma que código

## Implicações

1. **Gap de non-functional requirements:** se 85% dos context files não mencionam segurança, o agente não tem como priorizar security constraints sem outras formas de enforcement.
2. **Evolução orgânica:** consistent com Vasilopoulos (2602.20478) — infraestrutura de contexto cresce organicamente, não é planejada upfront.
3. **Tooling necessário:** o paper identifica necessidade de ferramentas para garantir que context files incorporem guardrails de segurança e performance.
