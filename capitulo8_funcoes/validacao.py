# Validando sem usar uma função
while True:
    v = int(input("Digite um valor entre 0 e 5: "))
    if v < 0 or v > 5:
        print("Valor inválido.")
    else:
        break
# Validação de inteiro usando função
# pergunta = int(input("Digite um valor entre 0 e 5: "))
# def faixa_int(pergunta, minimo, maximo):
#     while True:
#         v = int(input(pergunta))
#         if v < minimo or v > maximo:
#             print(f"Valor inválido. Digite um valor entre {minimo} e {maximo}")
#         else:
#             return v