#Escreva um programa que leia três números e que imprima o maior e o menor.
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("o primeiro número é o maior")
    
if numero2 > numero1 and numero2 > numero3:
    print("o segundo número é o maior")
    
if numero3 > numero1 and numero3 > numero2:
    print("o terceiro número é o maior")
    
if numero1 < numero2 and numero1 < numero3:
    print("E o primeiro número é o menor")
    
if numero2 < numero1 and numero2 < numero3:
    print("E o segundo número é o menor")
    
if numero3 < numero1 and numero3 < numero2:
    print("E o terceiro número é o menor")
