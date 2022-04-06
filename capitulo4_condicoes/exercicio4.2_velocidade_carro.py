#Escreva um programa que pergunte a velocidadedo carro de um usuário.
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso exiba o valor da multa, cobrando R$ 5,00 por km acima de 80 km/h.

velocidade = int(input("Informe a velocidade do seu carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"A sua velocidade ultrapassou 80 km/h e por isso você será multado em R$ {multa:.2f}")
if  velocidade <= 80:   
    print(f"A sua velocidade é {velocidade}")