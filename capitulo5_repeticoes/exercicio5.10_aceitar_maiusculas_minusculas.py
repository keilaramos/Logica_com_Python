# *******Operadores especiais********************************
# Operador / exemplo / equivalência
#  +=         x += 1    x = x + 1
#  -=         y -= 1    y = y - 1
#  *=         c *= 2    c = c * 2
#  /=         d /= 2    d = d / 2
#  **=        e **= 2   e = e ** 2
#  //=        f //= 4   f = f // 4

# Exercício5.10 - Aceitar respostas com letras maiúsculas ou minúsculas

pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questão == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questão == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1
    questão += 1
print(f"O aluno fez {pontos} ponto(s)")

