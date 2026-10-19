
#lista de listas pra montar a grade de letras

linha = 8
coluna = 12

grade = [] #criei uma lista vazia

for l in range(linha): 
    nova_linha = []

    for c in range(coluna):
        nova_linha.append(".")

    grade.append(nova_linha)

for l in grade:
    print(" ".join(linha))
