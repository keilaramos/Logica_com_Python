# exceções
nomes = ["Nick", "Pri", "Deb"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
    except IndexError:
        print("valor inválido, digite entre -3 e 3")
    