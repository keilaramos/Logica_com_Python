#Exercício 3.8 - Escreva um programa que leia um valor em metros e exiba convertido em milimetros

valor_metros = float(input("Digite o valor em metros: "))
valor_milimetros = valor_metros * 1000
print(f" {valor_metros:6.2f} metros equivale a {valor_milimetros:.2f} em milimetros.")