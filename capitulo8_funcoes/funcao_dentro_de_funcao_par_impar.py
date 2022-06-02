# def épar(x):
# 		return x % 2 == 0
# def par_ou_ímpar(x):
#     impar = "Ímpar"
#     par = "Par"
#     if épar(x):
#         return par
#     else:
#         return impar
# print(par_ou_ímpar(7))
# print(par_ou_ímpar(14))


A = 5
def muda_e_imprime( ):
    global A
    A = 7
    print(f"A dentro da função: {A}")
print(f" A antes de mudar: {A}")
muda_e_imprime()
print(f"A depois de mudar: {A}")