from Ponto import Ponto
from Transformacao import Transformacao


class Referencial:
    def __init__(self):
        self.origen = Ponto()
        self.transformacao = Transformacao()
        
    def __str__(self):
        return "Ponto: \n " + str(self.Pontos) + "\nOrientação: \n " + str(self.transformacao)
    
    def translacao(self):
        """------- Vetor translação -------"""
        
        self.transformacao.translacao.x
        self.transformacao.translacao.y
        self.transformacao.translacao.z

        """------- Origem do Ponto -------"""

        self.origen.x
        self.origen.y
        self.origen.z
        
        """------- Valor da translação -------"""

        self.calc_x = float(0)
        self.calc_y = float(0)
        self.calc_z = float(0)

        

        """-------------- Translação em X ---------------"""
        
        if self.origen.x == 0.00:  
            self.origen.x = self.transformacao.translacao.x
            self.calc_x = self.origen.x
        elif self.origen.x > 0 and self.transformacao.translacao.x > 0:
            if self.origen.x > self.transformacao.translacao.x:
                self.calc_x = self.transformacao.translacao.x - self.origen.x
                self.origen.x = self.origen.x + self.calc_x
            elif self.origen.x < self.transformacao.translacao.x:
                self.calc_x = self.transformacao.translacao.x - self.origen.x
                self.origen.x = self.origen.x + self.calc_x
        elif self.origen.x < 0 and self.transformacao.translacao.x < 0:  
            if self.origen.x > self.transformacao.translacao.x:
                self.calc_x = -(-self.transformacao.translacao.x + self.origen.x)
                self.origen.x = self.origen.x + self.calc_x
            elif self.origen.x < self.transformacao.translacao.x:
                self.calc_x = -(-self.transformacao.translacao.x + self.origen.x)
                self.origen.x = self.origen.x + self.calc_x
        elif self.origen.x > 0 and self.transformacao.translacao.x < 0:
            self.calc_x = -(self.origen.x - self.transformacao.translacao.x)
            self.origen.x = self.origen.x + self.calc_x
        elif self.origen.x < 0 and self.transformacao.translacao.x > 0:
            self.calc_x = self.transformacao.translacao.x - self.origen.x
            self.origen.x = self.origen.x + self.calc_x

        """----------------------------------------------"""
        """-------------- Translação em Y ---------------"""

        if self.origen.y == 0.00:     
            self.origen.y = self.transformacao.translacao.y
            self.calc_y = self.origen.y
        elif self.origen.y > 0 and self.transformacao.translacao.y > 0:
            if self.origen.y > self.transformacao.translacao.y:
                self.calc_y = self.transformacao.translacao.y - self.origen.y
                self.origen.y = self.origen.y + self.calc_y
            elif self.origen.y < self.transformacao.translacao.y:
                self.calc_y = self.transformacao.translacao.y - self.origen.y
                self.origen.y = self.origen.y + self.calc_y
        elif self.origen.y < 0 and self.transformacao.translacao.y < 0:  
            if self.origen.y > self.transformacao.translacao.y:
                self.calc_y = -(-self.transformacao.translacao.y + self.origen.y)
                self.origen.y = self.origen.y + self.calc_y
            elif self.origen.y < self.transformacao.translacao.y:
                self.calc_y = -(-self.transformacao.translacao.y + self.origen.y)
                self.origen.y = self.origen.y + self.calc_y
        elif self.origen.y > 0 and self.transformacao.translacao.y < 0:
            self.calc_y = -(self.origen.y - self.transformacao.translacao.y)
            self.origen.y = self.origen.y + self.calc_y
        elif self.origen.y < 0 and self.transformacao.translacao.y > 0:
            self.calc_y = self.transformacao.translacao.y - self.origen.y
            self.origen.y = self.origen.y + self.calc_y

        """----------------------------------------------"""
        """-------------- Translação em Z ---------------"""
        
        if self.origen.z == 0.00:     
            self.origen.z = self.transformacao.translacao.z
            self.calc_z = self.origen.z
        elif self.origen.z > 0 and self.transformacao.translacao.z> 0:
            if self.origen.z > self.transformacao.translacao.z:
                self.calc_z = self.transformacao.translacao.z - self.origen.z
                self.origen.z = self.origen.z + self.calc_z
            elif self.origen.z < self.transformacao.translacao.z:
                self.calc_z = self.transformacao.translacao.z - self.origen.z
                self.origen.z = self.origen.z + self.calc_z
        elif self.origen.z < 0 and self.transformacao.translacao.z < 0:  
            if self.origen.z > self.transformacao.translacao.z:
                self.calc_z = -(-self.transformacao.translacao.z + self.origen.z)
                self.origen.z = self.origen.z + self.calc_z
            elif self.origen.z < self.transformacao.translacao.z:
                self.calc_z = -(-self.transformacao.translacao.z + self.origen.z)
                self.origen.z = self.origen.z + self.calc_z
        elif self.origen.z > 0 and self.transformacao.translacao.z < 0:
            self.calc_z = -(self.origen.z - self.transformacao.translacao.z)
            self.origen.z = self.origen.z + self.calc_z
        elif self.origen.z < 0 and self.transformacao.translacao.z > 0:
            self.calc_z = self.transformacao.translacao.z - self.origen.z
            self.origen.z = self.origen.z + self.calc_z