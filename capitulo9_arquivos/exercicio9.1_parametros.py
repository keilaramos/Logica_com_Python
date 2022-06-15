# Escreva um programa que receba o nome de um arquivo pela linha de comando e que imprima todas as linhas desse arquivo.
import sys
if len(sys.argv) != 2:
    print("\nUso: e09-01.py nome do arquivo da Keila\n\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    for linha in arquivo.readlines():
        #como a linha termina com Enter, retirei o ultimo caractere antes de imprimir.
        print(linha[:-1])
    arquivo.close()