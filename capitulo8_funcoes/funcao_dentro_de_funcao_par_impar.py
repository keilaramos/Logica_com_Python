def épar(x):
		return x % 2 == 0
def par_ou_ímpar(x):
    impar = "Ímpar"
    par = "Par"
    if épar(x):
        return par
    else:
        return impar
print(par_ou_ímpar(7))
print(par_ou_ímpar(14))