# /ingest

Compare raw/ com wiki/_registry.md. Para cada fonte nova:

1. Leia o conteúdo (para PDFs, extraia texto; para imagens, descreva)
2. Identifique conceitos-chave (max 3 por fonte)
3. Para cada conceito:
   - Se artigo existe em wiki/concepts/: ATUALIZE adicionando informação nova
   - Se não existe E o conceito provavelmente será referenciado de outros artigos:
     CRIE seguindo o template (use as heurísticas de granularidade do CLAUDE.md)
   - Se não justifica artigo próprio: mencione como seção em artigo existente mais próximo
4. Classifique a fonte: type (article/paper/repo/note/dataset) e quality (primary/secondary/tertiary)
5. Verifique: algum artigo existente agora tem overlap >60% com outro? Se sim, sugira merge
6. Adicione entrada no _registry.md:
   - path | data processamento | type | quality | conceitos extraídos | status (processed)
7. Atualize _index.md (1 linha por artigo: título + resumo curto)
8. Processe quaisquer blocos > [!patch] encontrados nos artigos tocados

Reporte: X fontes processadas, Y artigos criados, Z atualizados, W patches resolvidos.
Se encontrar fontes com problemas (vazio, ilegível, duplicata exata): reporte sem processar.
