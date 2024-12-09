#Definiranje Klase Kalkulator 
class Kalkulator:
    #Konstruktor
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    #Metode za izsavanje operacije na atributim
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b is 0:
            return "Error - ne možeš dijeliti s nulom"
        else:
            return self.a / self.b
        
    def potenciranje(self):
        return self.a ** self.b
    
    def korijne(self):
        return self.a + self.b