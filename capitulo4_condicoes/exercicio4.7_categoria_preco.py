# Estruturas aninhadas 
# Escreva um programa que solicite a categoria de um produto e de acordo com a categoria
# digitada mostre o preço respectivo do produto.

categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
        preço = 10
else: 
    if categoria == 2:
        preço = 18
    else: 
        if categoria == 3:
            preço = 23
        else: 
            if categoria == 4:
                preço = 26
            else: 
                if categoria == 5:
                    preço = 31
                else: 
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preço = 0
print(f"O preço do produto é: R${preço:6.2f}")


# if categoria ==1:
#     preço = 10
# elif categoria == 2:
#     preço = 18
# elif categoria == 3:
#     preço = 23
# elif categoria == 4:
#     preço = 26
# elif categoria == 5:
#     preço = 31
# else:
#     print("Categoria inválida, digite um valor entre 1 e 5!")
#     preço = 0
# print(f"O preço do produto é: R${preço:6.2f}")