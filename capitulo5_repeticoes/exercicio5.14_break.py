# Exercício5.14 Lendo números inteiros do teclado e parando quando zero é entrado
# Escreva um programa que leia números inteiros do teclado. O programa deve ler os 
# números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade 
# de números digitados, assim como a soma e a média aritmética.

soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print(f"Média: {soma/quantidade:10.2f}")
