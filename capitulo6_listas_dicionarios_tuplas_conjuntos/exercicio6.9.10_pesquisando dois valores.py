# Exercício 6.9 - pesquisando dois valores

L =     [15, 7, 27, 39]
#posição.[0, 1, 2, 3 ]
p = int(input("Digite o primeiro valor a procurar: ")) 
v = int(input("Digite o seguendo valor a procurar: "))
x = 0
while x < len(L):
    if L[x] == p:
        break 
    elif L[x] == v:
        break 
    x += 1 #incrementa
if x < len(L):
    if p == L[x]:
        print(f"{p} achado primeiro na posição {x}")
    else: 
        print(f"{p} não encontrado")
    if v == L[x]:
        print(f"{v} achado primeiro na posição {x}")
    else: 
        print(f"{v} não encontrado") 