#Comandos para eu lembrar de atualizar projeto
#git status
#git diff
#git add main.py
#git commit -m "Adiciona letra na primeira posição da grade"
#git push


#Próxima parte do estudo: 
#inserir uma palavra na horizontal
#palavra que vou inserir: "SUPERAI" (na realidade seria super AI, mas na minha estrutura imagino que se uma 
#dica leva a duas palavras, essa expressão virá junta)

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
grade[0][2] = "S"
grade[0][3] = "U"
grade[0][4] = "P"
grade[0][5] = "E"
grade[0][6] = "R"
grade[0][7] = "A"
grade[0][8] = "I"

for l in grade:
    print(" ".join(l))
