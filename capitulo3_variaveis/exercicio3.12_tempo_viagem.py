#Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

#Entrada dos dados
distancia = float(input("Digite a distância a percorrer em km: "))
velocidade_media = float(input("Digite a velocidade média esperada: "))

#Cálculo e condicional na exibição para o usuário
tempo_viagem = distancia / velocidade_media
if tempo_viagem < 1:
    tempo_minutos = tempo_viagem * 60
    print(f"O tempo de viagem será: {tempo_minutos:.0f} min")
else:
    print(f"O tempo de viagem será: {tempo_viagem:.2f} h")
