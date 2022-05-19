# Exercício 6.6 - Similação de duas filas de banco 
ultimo1 = 14
ultimo2 = 12
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1")
    print(f"Fila atual: {fila1}")
    print(f"\nExistem {len(fila2)} clientes na fila 2")
    print(f"Fila atual: {fila2}\n")
    print("Digite F para adicionar um cliente ao fim da fila 1 ou G para a fila 2,")
    print("ou A para realizar o atendimento na fila 1 ou B na fila 2. S para sair.")
    operacao = input("operação(F, A ou S):")
    x = 0
    sair = False
    while x < len(operacao):
        if operacao[x].upper() == "A":
            if len(fila1) > 0:
                atendido1 = fila1.pop(0)
                print(f"Cliente {atendido1} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
                
        elif operacao[x].upper() == "B":
            if len(fila2) > 0:
                atendido2= fila2.pop(0)
                print(f"Cliente {atendido2} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
            
        elif operacao[x].upper() == "F":
            ultimo1 += 1 #incrementa o ticket do novo cliente
            fila1.append(ultimo1)
        
        elif operacao[x].upper() == "G":
            ultimo2 += 1 #incrementa o ticket do novo cliente
            fila2.append(ultimo2)
            
        elif operacao.upper() == "S":
            sair = True
            print("Você saiu!")
            break
        else:
            print("Operação inválida! Digite apenas F,G, A,B ou S!")
        x = x + 1
    if sair:
        break
