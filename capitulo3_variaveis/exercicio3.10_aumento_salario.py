#Exercício 3.10 - Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem do aumento. 
#Exiba o valor do aumento e do novo salário.

#Entrada de dados
salario = float(input("Digite o valor do salário: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento do salário: "))

#Cálculo
porcentagem = porcentagem_aumento / 100
aumento = salario * porcentagem
novo_salario = salario + aumento

#Exibição para o usuário
print(f"O valor do aumento será: R${aumento:5.2f}")
print(f"O novo salário será: R${novo_salario:5.2f}")