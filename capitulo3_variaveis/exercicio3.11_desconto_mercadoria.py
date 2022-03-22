#Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria
# e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

#Entrada dos dados
preco_mercadoria = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

#Cálculo
desconto = preco_mercadoria * percentual_desconto / 100
preco_pagar = preco_mercadoria - desconto

#Exibição para o usuário
print(f"O valor do desconto será: R${desconto:5.2f}")
print(f"O preço a pagar será: R${preco_pagar:5.2f}")