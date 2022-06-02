# def imprime_maior(mensagem, *numeros):
#     maior = None
#     for e in numeros:
#         if maior is None or maior < e:  
#             maior = e
#     print(mensagem, maior) 
# imprime_maior("Maior:", 5, 4, 3, 1)
# imprime_maior("Max:", *[1, 7, 9])

# # def epar(x):
# #     return x % 2 == 0
# # print(epar(2))
# # print(epar(3))
# # print(epar(10))

L = [10, 20, 25, 30]
def soma(L):
    total = 0
    for e in L:
        total += e
    return total
def media(L):
    return soma(L) / len(L)
print(soma(L) / len(L))



