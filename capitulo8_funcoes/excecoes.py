# exceções
# nomes = ["Nick", "Pri", "Deb"]
# for tentativa in range(3):
#     try:
#         i = int(input("Digite o índice que quer imprimir: "))
#         print(nomes[i])
#     except ValueError:
#         print("Digite um número!")
#     except IndexError:
#         print("valor inválido, digite entre -3 e 3")
    
    
nomes = ["Carluce", "Juliana", "Mônica"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except Exception as excecao_keila:
        print(f"Algo de errado aconteceu: {excecao_keila}")
        
nomes = ["Débora", "Priscila", "Nicola"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
    finally:
        print(f"Tentativa {tentativa + 1}")
    
# nomes = ["Débora", "Priscila", "Nicola"]
# for tentativa in range(3):
#     try:
#         i = int(input("Digite o índice que quer imprimir: "))
#         print(nomes[i])
#     except ValueError as execao:
#         print("Digite um número!")
#         raise
#     finally:
#         print(f"Sempre o finally é executado")  

# def epar(n):
#     try:
#         return n % 2
#     except Exception:
#         raise ValueError("Valor inválido!!!")