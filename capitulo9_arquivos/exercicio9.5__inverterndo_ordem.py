#Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A primeira linha deve conter o maior número; e a última, o menor.

pares = open("pares.txt","r")
saida = open("pares_invertidos.txt","w")

l = pares.readlines()
l.reverse()
for li in l:
    saida.write(li)

pares.close()
saida.close()

# Alternativa usando with:
#
##with open("pares.txt","r") as pares, open("pares_invertido.txt","w") as saída:
##    L = pares.readlines()
##    L.reverse()
##    for l in L:
##        saída.write(l)