#Exercício 09-02: Imprimia as linhas de um arquivo. O nome do arquivo, a primeira e última linha a imprimir serão passadas na linha de comando
import sys
if len(sys.argv) != 4:
    print("\nUso: e09-01.py nome do arquivo da Keila  agora com inicio e fim\n\n")
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open(nome, "r")
    for linha in arquivo.readlines()[inicio-1:fim]:
        #como a linha termina com Enter, retirei o ultimo caractere antes de imprimir.
        print(linha[:-1])
    arquivo.close()