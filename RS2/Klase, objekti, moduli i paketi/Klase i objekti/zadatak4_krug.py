import math
#Klasa / šablona  Krug 
class Krug:
    #Konstruktor s jednim atributom
    def __init__(self,r):
        self.r = r
        
    # opseg metoda 
    def opseg(self):
        opseg_kruga = 2 * math.pi * self.r
        print(f"Ospeg kruga je {opseg_kruga}")
    
    # Površina metoda 
    def povrsina(self):
        povrsina = math.pi * self.r * self.r
        print(f"Površina kruga je {povrsina}")

prvi_objek_krug = Krug(3)
prvi_objek_krug.opseg()
prvi_objek_krug.povrsina()
