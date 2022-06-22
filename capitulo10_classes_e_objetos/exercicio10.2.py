# Atualmente, a classe Televisão inicializa o canal com 2. Modifique a classe Televisão de forma a receber o canal inicial em seu construtor.

class Televisão:
    def __init__(self, canal_inicial, min, max):
        self.ligada = False
        self.canal = canal_inicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal-1 >= self.cmin:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal+1 <= self.cmax:
            self.canal += 1


tv = Televisão(5, 1, 99)

print(tv.canal, tv.cmax)
