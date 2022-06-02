# Exercício 8.7 - Defina uma função recursiva que calcule o maior divisor comum (MDC) entre dois números a e b, em que a > b.

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b) # resto da divisão de a por b -> 40/25
        
print(f"MDC 40 e 25 -->  {mdc(40,25)}")