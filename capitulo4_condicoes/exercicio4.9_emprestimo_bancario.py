# Exercício4.9_Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valorda prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação
# como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

# Entradas do usuário
valor_casa = float(input("Informe o valor da casa a comprar: "))
salario = float(input("Informe o seu salário: "))
quantidade_anos = int(input("Informe a quantidade de anos a pagar: "))

# Cálculando os valores e colocando em variáveis
quantidade_anos = quantidade_anos * 12
valor_prestação = valor_casa / quantidade_anos
porcentagem = salario * (30/100)

# Usando a condicional
if valor_prestação <= porcentagem:
    print(f"Parabéns! O emprestivo está aprovado com parcela de: R$ {valor_prestação:6.2f} ")
else:
    print(f"Infelizmente o valor da prestação ficou acima de 30% do seu salário: R$ {valor_prestação:6.2f} ")