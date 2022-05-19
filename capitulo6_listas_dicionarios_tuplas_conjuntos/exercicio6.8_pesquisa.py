# Exercício 6.8 - sequencial

L =     [15, 7, 27, 39]
#posição.[0, 1, 2, 3 ]
p = int(input("Digite o valor a procurar: ")) 
x = 0
while x < len(L):
    if L[x] == p:
        break 
    x += 1 #incrementa
if x < len(L):
    print(f"{p} achado na posição {x}")
else: 
    print(f"{p} não encontrado") 
        

    
   
    