#programa 9.1 - Abrindo, lendo e fechando um arquivo
arquivo = open("numeros.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()