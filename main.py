#Comandos para eu lembrar de atualizar projeto
#git status
#git diff
#git add main.py
#git commit -m "Adiciona letra na primeira posição da grade"
#git push

#lista de listas pra montar a grade de letras

linha = 8
coluna = 12

grade = [] #criei uma lista vazia

#Se eu quero primeira linha, primeira coluna, entao quero grade[0][0] = Q

for l in range(linha): 
    nova_linha = []

    for c in range(coluna):
        nova_linha.append(".")
        
    grade.append(nova_linha)


#adicionando uma palavra
palavra = "SUPERAI"
#Essa palavra deve ser alocada na linha 0, mas começando a partir da coluna 2
linhaPalavra = 0
colunaInicialPalavra = 2

if(colunaInicialPalavra +len (palavra) <= coluna):

    for indice, letra in enumerate(palavra):
        grade[linhaPalavra][colunaInicialPalavra+indice] = letra
else:
    print("Essa palavra não cabe na posição desejada")

for l in grade:
    print(" ".join(l))
