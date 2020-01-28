arquivo = open('arquivoTeste.txt', 'w')### parametro 'w' é para escrever no arquivo, porém ele sobrescreve, 'a' altera o arquivo sem substituir as informações

txt = '''
Arquivo de teste... 
abc
dsad
dsdadsafaf
fdasfdfdsfsdf
'''

arquivo.write(txt)
arquivo.close

arquivo = open('arquivoTeste.txt', 'r')

leia = arquivo.read()
arquivo.close

print(leia)

arquivo = open('arquivoTeste.txt', 'r')

txt = arquivo.readlines() # le uma linha de cada vez... cada linha tem um indice de acordo com a ordem do arquivo

for i in txt:
    print(i)
arquivo.close()