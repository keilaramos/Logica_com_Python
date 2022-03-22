# **Interpolação de String (str)**
# substituir as posições fixas e demarcadas na string por valores de variáveis.
# Usa-se o f ou F de format antes das aspas e coloque entre chaves o valor a ser chamado.

# Exercício 3.4 - Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
# Considerando que paga imposto pessoas que recebem mais que R$ 1.900,00.


salario = int(input("digite o salário: "))
print(salario)
imposto = True

if salario > 1900 and salario < 2800:
    valor1 = salario * (7/100)
    print(F"você pagara imposto? {imposto} e no valor de R$ {valor1}")
elif salario > 2800 and salario < 3700:
    valor2 = salario * (15/100)
    print(f"você pagara imposto? {imposto} e no valor de R$ {valor2}")
elif salario > 3700 and salario < 4600:
    valor3 = salario * (22.5/100)
    print(f"você pagara imposto? {imposto} e no valor de R$ {valor3}")
    
elif salario >= 4600:
    valor4 = salario * (27.5/100)
    print(f"você pagara imposto? {imposto} e no valor de R$ {valor4}")
else: 
    print(f"você pagara imposto? {not imposto}")