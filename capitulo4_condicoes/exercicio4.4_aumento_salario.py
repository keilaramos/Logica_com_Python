#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a la
# R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais de 15%. Para

salario = float(input("Informe o seu salário: "))
if salario > 1250:
    aumento = salario * (10/100)
    print(f"Com esse salário o aumento será de: {aumento:6.2f}")
if salario <= 1250:
    aumento = salario * (15/100)
    print(f"Com esse salário o aumento será de: {aumento:6.2f}")
    