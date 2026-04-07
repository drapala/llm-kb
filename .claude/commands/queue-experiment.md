# /queue-experiment

Enfileira uma fonte do live para entrar no experimento metaxon-benchmark.
A fonte será processada pelo orchestrator às 23:55 e ingerida nos dois braços (full e vanilla).

## Argumento
$ARGUMENTS — URL, caminho de arquivo raw/, ou descrição da fonte

## O que fazer

1. Determinar o tipo de entrada:
   - Se for URL → adicionar em `/Users/drapala/projects/metaxon-benchmark/experiment-hub/inbox/queued_urls.txt`
   - Se for arquivo local → copiar para `/Users/drapala/projects/metaxon-benchmark/experiment-hub/inbox/dropbox/`

2. Para URL:
   - Verificar se já existe em `queued_urls.txt` (não duplicar)
   - Adicionar linha no formato: `<url>  # enfileirado em YYYY-MM-DD por joao`
   - Confirmar adição

3. Para arquivo local (raw/):
   - Copiar o arquivo para `experiment-hub/inbox/dropbox/`
   - Preservar o nome original
   - Confirmar cópia

4. Reportar:
   ```
   ✓ Enfileirado para o experimento: <fonte>
   Tipo: url | arquivo
   Próximo processamento: 23:55 hoje (ou amanhã se já passou)
   Braços afetados: full + vanilla (simétrico)
   
   Nota: esta fonte também precisa ser ingerida no live separadamente se quiser no wiki principal.
   ```

## Regras

- NÃO modificar batches já congelados em `experiment-hub/batches/`
- NÃO editar diretamente `metaxon-exp-full/` ou `metaxon-exp-vanilla/`
- NÃO enfileirar se a motivação for beneficiar um braço específico
- Toda entrada vai para os dois braços — sem exceções
