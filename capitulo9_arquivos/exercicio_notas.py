# Criando e modificando arquivo
notas = [6, 7, 8, 3, 8, 9, 5 ]

with open('notas.txt', 'w') as prova:
    for valor in notas:
        prova.write(str(valor) + '\n')
        print(valor)

# with open('notas.txt', 'a') as prova:
#     for valor in notas:
#         prova.write(str(2) + '\n')
        
# with open('notas.txt', 'r') as prova:
#     for valor in prova:
#         print(valor) 
        
# with open('notas.txt', 'r+') as prova:
#     for valor in prova:
#         print(valor)
#     prova.write("10")