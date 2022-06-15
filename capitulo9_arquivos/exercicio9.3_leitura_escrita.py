# Crie um programa que leia os arquivos pares.txt e ímpares.txt e que crie um só arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica.

with open("pareseimpares.txt", "w") as pareseimpares:
    with open("pares.txt") as pares:
        with open("impares.txt") as impares:
            for l in pares.readlines():
                pareseimpares.write(l)
            for l in impares.readline():
                if int(l):
                    pareseimpares.write(l)
                








# with open("multiplos de 4.txt", "w") as multiplos4:
#     with open("pares.txt") as pares:
#         for l in pares.readlines():
#             if int(l) % 4 == 0:
#                 multiplos4.write(l)