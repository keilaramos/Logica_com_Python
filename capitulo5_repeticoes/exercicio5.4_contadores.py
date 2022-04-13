#*****Contadores********************************
#São variáveis ultilizadas para contar o número
# de ocorrência de um determinado evento como no 
# exercício abaixo onde x aparece na 5ª vez como contador.

# Exercício 5.5 - Modifique o programa anterior para imprimir de 1 até o 
# número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

fim = int(input("Digite o último número a imprimir:"))
#x = 1 #1
x = 0
while x <= fim:#3 usando a estrutura de repetição enquanto
    if x % 2 == 0:
        print(x)
    #print(x)#4
    x = x + 1
    #x = x + 2 #5 contador em ação!

