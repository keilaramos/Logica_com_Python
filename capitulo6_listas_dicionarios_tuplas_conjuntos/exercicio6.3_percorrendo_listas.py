# Exercício 6.3 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
primeira = []
segunda = []
while True:
    entrada = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if entrada == 0:
        break
    primeira.append(entrada)
while True:
    entrada = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if entrada == 0:
        break
    segunda.append(entrada)
terceira = []
# Aqui vamos criar uma outra lista, com os elementos da primeira
# e da segunda. Vamos pesquisar os valores a inserir na terceira
# lista. Se não existirem, adicionaremos à terceira. Caso contrário,
# não copiaremos, evitando assim os repetidos.
duas_listas = primeira[:]
duas_listas.extend(segunda)
x = 0
while x < len(duas_listas):
    y = 0
    while y < len(terceira):
        if duas_listas[x] == terceira[y]:
            break
        y = y + 1
    if y == len(terceira):
        terceira.append(duas_listas[x])
    x = x + 1
x = 0
while x < len(terceira):
    print(f"{x}: A terceira lista contém: {terceira[x]}")
    x = x + 1
