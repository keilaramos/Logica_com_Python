# Exercício 10.1- Adicione atributos à classe Televisao
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 14
        self.marca = "Pythonic"


tv = Televisao()
tv.tamanho = 40
tv.marca = "menorzinha"
tv_sala = Televisao()
tv_sala.tamanho = 60
tv_sala.marca = "Maiorzinha"

print(f"tv tamanho = {tv.tamanho} marca = {tv.marca}")
print(f"tv_sala tamanho = {tv_sala.tamanho} marca = {tv_sala.marca}")
