# Army of Juniors: The AI Code Security Crisis

**Autor:** Ox Security  
**Publicação:** Ox Security Whitepaper  
**Ano:** Outubro 2025  
**URL:** https://www.ox.security/resource-category/whitepapers-and-reports/army-of-juniors/  
**Tipo:** article / primary (indústria, dados empíricos próprios — não peer-reviewed)

---

## Metodologia

- **300+ repositórios open-source** analisados
- Identificação de **10 anti-patterns** que violam boas práticas de engenharia de software
- Foco em segurança e arquitetura, não apenas bugs individuais

## Os 10 Anti-Patterns identificados

O relatório cobre um espectro de "Comments Everywhere" a "Return of Monoliths":
1. **Comentários excessivos** — AI comenta tudo, criando ruído que mascara compreensão real
2. **Retorno de monolitos** — AI gera código monolítico em vez de seguir arquitetura modular existente
3. **Ausência de reuso** — duplicação em vez de reutilização de código existente
4. **Falta de tratamento de erro contextual** — erros genéricos, não adaptados ao sistema
5. **Hardcoding de valores** — constantes e credenciais sem parametrização
6. **Dependências desnecessárias** — introdução de bibliotecas sem necessidade real
7. **Lógica excessivamente complexa** — soluções over-engineered para problemas simples
8. **Violação de convenções do projeto** — desrespeito a padrões existentes no codebase
9. **Ausência de tratamento de edge cases** — código "caminho feliz" sem robustez
10. **Acoplamento excessivo** — código que cria dependências desnecessárias entre módulos

## Achado central: "insecure by dumbness"

O problema não é que AI escreva código com mais vulnerabilidades por linha do que humanos. O problema é:
- Usuários não-técnicos deployam aplicações construídas com AI tools em velocidade sem precedente
- Code review humano não consegue escalar para acompanhar o volume de output gerado
- Sistemas vulneráveis chegam à produção mais rápido, não mais devagar

A metáfora: AI age como developer júnior talentoso — rápido, funcional em casos simples, mas sem julgamento arquitetural e sem consciência de segurança sistêmica.

## Implicação operacional

O relatório recomenda:
- Embutir conhecimento de segurança diretamente nos workflows de AI (instruction sets)
- Enforcing de constraints arquiteturais nos prompts
- Guardrails automatizados integrados ao ambiente de desenvolvimento

## Limitações como fonte

- Industry whitepaper, não peer-reviewed
- Metodologia de seleção dos 300 repositórios não completamente detalhada
- Potencial conflito de interesse (Ox Security vende produto de segurança)
- Os 10 anti-patterns são tipologia qualitativa, não métricas quantitativas
