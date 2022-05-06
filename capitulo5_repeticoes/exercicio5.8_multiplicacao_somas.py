# Exercício5.8_ Multiplicação com somas sucessivas
# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender
# a multiplicação de dois números como somas sucessivas de um deles.
# Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

p = int(input("Primeiro número: "))
s = int(input("Segundo número: "))
x = 1
resultado = 0
while x <= s:
    resultado = resultado + p # 0+5 / 5+5/10+5
    x = x + 1
print(f"{p} x {s} = {resultado}")