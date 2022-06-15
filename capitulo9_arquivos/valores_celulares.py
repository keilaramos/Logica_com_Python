# Criando e modificando arquivo
valores_celulares = [1100, 900, 800, 1200]

with open('valores_celulares.txt', 'w') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')