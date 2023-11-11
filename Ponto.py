class Ponto:
    def __init__(self):
        self.x = float(0)
        self.y = float(0)
        self.z = float(0)
    
    def __str__(self):
        return " x: " + str(self.x) +"\n y=: " + str(self.y )+ "\n z: " + str(self.z)
