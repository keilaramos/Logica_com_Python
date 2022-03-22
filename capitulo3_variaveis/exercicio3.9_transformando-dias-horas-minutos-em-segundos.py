#Excercício 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos
# e segundos do usuário. Calcule o total em segundos.

#Entradas dos valores pelo usuário
dias = int(input("digite os dias: "))
horas = int(input("digite as horas: "))
minutos = int(input("digite os minutos: "))
segundos = int(input("digite os segundos: "))

#Cálculos
calculo_dias = dias * 86400
calculo_horas = horas * 3600
calculo_minutos = minutos * 60
resultado = calculo_dias + calculo_horas + calculo_minutos + segundos

print(f"Esse valor corresponde a: {resultado} segundos")


