# Exercício 4.6 - Escreva um programa que pergunte a distância que um 
# passageiro deseja percorrer em km. Calcule o preço da passagem cobrando R$ 0,50 por km
# para viagens até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input("Digite a distância que deseja percorrer em quilometros: "))
if distancia <= 200:
    preco_passagem = float(distancia * 0.5)
else:
    preco_passagem = float(distancia * 0.45)
    
print(f"O preço da passagem é: R$ {preco_passagem:6.2f}")
    
    