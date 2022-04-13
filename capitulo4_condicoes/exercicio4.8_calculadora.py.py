# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular a soma (+), subritração(-), multiplicação (*) e divisão(/).
# Exiba o resultado da operação solicitada.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


operacao = float(input("Digite a operação que deseja: 1 para soma, 2 para subritração, 3 para multiplicação e 4 para divisão: "))
soma = (numero1 + numero2)
subritracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

if operacao == 1:
    print(f"O resultado é: {soma:6.2f}")
elif operacao == 2:
    print(f"O resultado é: {subritracao:6.2f}")
elif operacao == 3:
    print(f"O resultado é: {multiplicacao:6.2f}")
elif operacao == 4:
    print(f"O resultado é: {divisao:6.2f}")
else:
    print(f"Comando inexistente!")

