# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado a média do aluno deve ser maior ou igual a 7.

aluno = input("Digite o nome do Aluno: ")
print(f"Vamos avaliar {aluno}")
portugues = int(input(f"Digite a nota em Português do(a) {aluno}: "))
print(portugues)
matematica = int(input(f"Digite a nota em Matemática do(a) {aluno}: "))
print(matematica)
ciencias = int(input(f"Digite a nota em Ciências do(a) {aluno}: "))
print(ciencias)
media = (portugues + matematica + ciencias)/3
if media >= 7:
    print(f"Parabéns {aluno} foi Aprovado(a)")
else:
    print(f"Infelizmente {aluno} foi Reprovado")
