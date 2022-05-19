# Programa 6.14 - Lendo e imprimindo lista de frutas.

S = ["maças", "laranjas", "peras"]
while True:
    fruta = input("Fruta: ")
    if fruta == "p":
        break
    S.append(fruta)
for k in S:
    print(k)