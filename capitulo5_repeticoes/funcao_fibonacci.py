# Função para calcular o enésimo termo da sequência de fibonacci pode ser definida como:
from tkinter import N


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10 - 1) + fibonacci(10 - 2))
