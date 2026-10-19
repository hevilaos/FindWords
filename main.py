#Comandos para eu lembrar de atualizar projeto
#git status
#git diff
#git add main.py
#git commit -m "Adiciona letra na primeira posição da grade"
#git push


#Próxima parte do estudo: 
#praticar o acesso ás posições antes de inserir palavras inteiras
#Tente colocar a letra "Q" na primeira Linha e primeira coluna, 
#mantendo os pontos restantes, e imprimir novamente
#a dica é que os índices começam em zero grade[indice_da_linha][indice_da_coluna]

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

#modificando a posição depois de ter a grade pronta
grade[0][0] = "Q"
for l in grade:
    print(" ".join(l))
