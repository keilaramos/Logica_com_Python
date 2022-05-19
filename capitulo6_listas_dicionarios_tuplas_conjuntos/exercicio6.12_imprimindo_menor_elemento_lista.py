# Exercício 6.12 - Imprima o menor elemento da lista.

L = [8, 7, 3, 4]
minimo = L[-1]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)