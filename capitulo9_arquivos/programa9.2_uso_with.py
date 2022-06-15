#Uso do with para fechamento automático do arquivo aberto.
# with open("numeros.txt", "r") as arquivo:
#     for linha in arquivo.readline():
#         print(linha)
        
import sys
print(f"Número de parâmetros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")