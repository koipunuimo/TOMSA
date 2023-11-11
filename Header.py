from Tempo import Tempo
import numpy as np
class Header:
    def __init__(self):
        self.seq =  int()
        self.tempo = Tempo()
        self.frame = str()
        
    def __str__(self):
        return "Seq: " + str(self.seq) + "\nTempo: \n " + str(self.tempo) + "\nFrame: " + str(self.frame)