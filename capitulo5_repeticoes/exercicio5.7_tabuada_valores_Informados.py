# Exercício_ 5.7 - Tabuada com valores iniciais e finais informados pelo usuário
n = int(input("Tabuada de: "))
x = int(input("De: "))
fim = int(input("Até: "))
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1