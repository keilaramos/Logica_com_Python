# Exercício 6.5 - Similação de uma fila de banco **** fila FIFO - Primeiro a entrar último a sair****
ultimo = 14
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("operação(F, A ou S):")
    x = 0
    sair = False
    while x < len(operacao):
        if operacao[x].upper() == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x].upper() == "F":
            ultimo += 1 #incrementa o ticket do novo cliente
            fila.append(ultimo)
        elif operacao.upper() == "S":
            sair = True
            print("Você saiu!")
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        x = x + 1
    if sair:
        break
    
