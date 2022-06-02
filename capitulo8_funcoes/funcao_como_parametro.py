def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def mostra(a, b, calculo):
    print(calculo(a,b))
mostra(5,9,soma)
mostra(10,1, subtracao)
