with open('words1.txt') as arquivo1:
    conteudoArquivo1 = arquivo1.read().splitlines()

with open('words2.txt') as arquivo2:
    conteudoArquivo2 = arquivo2.read().splitlines()

for n in conteudoArquivo1:
    if n in conteudoArquivo2:
        print(n)