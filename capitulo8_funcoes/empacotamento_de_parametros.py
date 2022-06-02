def soma(a,b):
    print(a+b)
L = [2, 3]
soma(*L) # esse asterisco indica que estou desempacotando a lista L utilizando os seus valores como parâmetros pra função soma. Para não ter q escrever soma(L[0], L[1]).

# def barra(n=10, c="*"):
#     print(c*n)
# L = [[5,"_K_ "], [10, "*"], [6, "."]]
# for e in L:
#     barra(*e)

