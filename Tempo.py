class Tempo:
    def __init__(self):
        self.sec = int(0)
        self.nsec = int(0)
    
    def __str__(self):
        return "Sec: " + str(self.sec) +"\n nSec: " + str(self.nsec )