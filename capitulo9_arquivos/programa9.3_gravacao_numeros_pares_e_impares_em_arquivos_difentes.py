# Programa 9.3 - Gravação de numeros pares e ímpares em arquivos diferentes.
def le_numero(arquivo):
    while True:
        numero = arquivo.readline()
        # Verifica se conseguiu ler algo
        if numero == "":
            return None
        # Ignora linhas em branco
        if numero.strip() != "":
            return int(numero)


def escreve_numero(arquivo, n):
    arquivo.write(f"{n}\n")


pares = open("pares.txt", "r")
ímpares = open("ímpares.txt", "r")
pares_ímpares = open("pareseimpares.txt", "w")
npar = le_numero(pares)
nimpar = le_numero(ímpares)
while True:
    if npar is None and nimpar is None:  # Termina se ambos forem None
        break
    if npar is not None and (nimpar is None or npar <= nimpar):
        escreve_numero(pares_ímpares, npar)
        npar = le_numero(pares)
    if nimpar is not None and (npar is None or nimpar <= npar):
        escreve_numero(pares_ímpares, nimpar)
        nimpar = le_numero(ímpares)

pares_ímpares.close()
pares.close()
ímpares.close()