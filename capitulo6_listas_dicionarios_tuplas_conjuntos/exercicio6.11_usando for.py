L = [2,3,4,7]
k = int(input("Digite um número a pesquisar:"))
for i in L:
    if i == k:
        print("Elemento encontrado!")
        break #1
else: #2
    print("Elemento não encontrado!")
