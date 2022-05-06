# Exercício 6.2 - Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.


# lista1 = [1,3,5,7,9]
# lista2 = [2,4,6,8,10]
# lista3 = lista1 + lista2

# print (f"A terceira lista é: {lista3}")

primeira = []
segunda = []
while True:
    entrada_valores1 = int(input("Digite um valor para a primeira lista (0 para terminar): "))
    if entrada_valores1 == 0:
        break
    primeira.append(entrada_valores1)#parâmetro(variável de caráter secundário cuja finalidade é especificar os objetos de um conjunto)
while True:
    entrada_valores2 = int(input("Digite um valor para a segunda lista (0 para terminar): "))
    if entrada_valores2 == 0:
        break
    segunda.append(entrada_valores2)
terceira = primeira[:]  # Copia os elementos da primeira lista
terceira.extend(segunda) # e extend os elementos da segunda lista
x = 0
while x < len(terceira):
    print(f"Terceira lista: Índice {x} - Elemento {terceira[x]}")
    x = x + 1