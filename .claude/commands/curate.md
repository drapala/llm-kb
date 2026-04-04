# /curate

Busca fontes adversariais que desafiem premissas do wiki. Olha pra fora.

## Processo

1. **Identificar premissas não desafiadas:**
   Leia wiki/_index.md e identifique os 3-5 claims mais fortes que o wiki
   trata como verdade sem fonte challenging. Priorize claims que:
   - Aparecem em 3+ artigos como fato estabelecido
   - Não têm tensão documentada em [[tension-resolution]]
   - São interpretações (não dados primários verificados)

2. **Formular queries adversariais:**
   Para cada premissa, gere 2-3 search queries que buscariam contra-argumentos:
   - "[premissa] limitations"
   - "[premissa] criticism"
   - "[premissa] alternatives to"
   - "[premissa] fails when"

3. **Web search + triagem:**
   Rode web search com as queries. Para cada resultado:
   - É fonte primary ou secondary? (descartar tertiary: tweets opinativos, blog posts superficiais)
   - Apresenta argumento substantivo ou apenas discorda sem dados?
   - Traz evidência que o wiki não tem?
   Selecione as 2-3 fontes mais fortes.

4. **Salvar em raw/ com stance:challenging:**
   Para cada fonte selecionada, salve em raw/articles/ ou raw/papers/
   com frontmatter incluindo `stance: challenging` e nota sobre qual
   premissa do wiki ela desafia.

5. **NÃO rode /ingest automaticamente.**
   Reporte as fontes salvas e quais premissas desafiam.
   O usuário decide se roda /ingest ou descarta.

## Formato de report (terminal)

- 🎯 Premissas identificadas: [lista com artigos que as sustentam]
- 🔍 Queries geradas: [lista]
- 📄 Fontes encontradas: [lista com título, tipo, qual premissa desafia]
- 💾 Salvas em raw/: [paths]
- ❌ Descartadas: [fontes rejeitadas + motivo]
- 🏷️ Próximo passo: rode `/ingest` pra processar as fontes challenging

## Quando rodar

- Quando /review reportar adversarial gap (ratio confirming:challenging > 5:1)
- Quando /ask reportar gap no wiki
- Periodicamente (sugerido: a cada 10 fontes confirming ingeridas)
