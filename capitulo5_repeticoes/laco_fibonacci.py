# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

#Usando o for para achar pelo número de termos q deseja

termos = int(input('Digite o número de termos Fibonatti: '))
anterior, proximo = 1, 1
ultimo_k = 0

for i in range(termos):
    print(anterior, end=', ')
    ultimo_k = anterior
    anterior = proximo
    proximo = ultimo_k + anterior

print('Fim')


# n = int(input("Digite o n−ésimo termo da serie "))
# cont = 0
# inicial = 0
# final = 1

# print(inicial)
# print(final)
# while cont <= n - 1:
#     inicial = final + inicial
#     print(inicial)
#     final = inicial + final
#     print(final)
#     cont += 1
# print("Fim")

# abaixo segue modelo para achar somente um valor pela sua posição

# n = int(input("Que termo deseja encontrar: "))
# ultimo=1
# penultimo=1

# if (n==1) or (n==2):
#     print("1")
# else:
#     for count in range(2,n):
#         termo = ultimo + penultimo
#         penultimo = ultimo
#         ultimo = termo
#         count += 1
#     print(termo)

