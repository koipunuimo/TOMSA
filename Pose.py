from Ponto import Ponto
from Orientacao import Orientacao
class Pose:
    def __init__(self):
        self.ponto      = Ponto()
        self.orientacao = Orientacao()
        
    def __str__(self):
        return "Ponto: \n" + str(self.ponto) + "\nOrientação: \n" + str(self.orientacao)

