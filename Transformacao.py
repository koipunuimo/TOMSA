from Vetor import Vetor
from Orientacao import Orientacao

class Transformacao:
    def __init__(self):
        self.translacao = Vetor()
        self.orientacao = Orientacao()
        
    def __str__(self):
        return "Ponto: \n " + str(self.vetor) + "\nOrientação: \n " + str(self.orientacao)
    
    