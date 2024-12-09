class Radnik:
    
    # konstruktor 
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    
    #work metoda koja ispisuje neki tekst 
    def work(self):
        print(f"Radim na poziciji {self.pozicija}")
    
    #metoda za povećanje plaće radnika
    def give_raise(self, radnik , povecanje):
        radnik.placa += povecanje
        print(f"Plaća radnika {radnik.ime} je sada {radnik.placa} eura ")
        

#Klasa Manager koja nasljeđuje Radnik
class Manager(Radnik):
    #Konstruktor 
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
        
    #Metoda work koja ispisuje metodu work super klase i nadodaje toj metodi
    def work(self):
        super().work()
        print(f"u odjelu {self.department}" )
    
#Instance obe klase 

#Inicializacije objekta Klase Manger
prvi_manger_objekt = Manager("Marko","Middle Management",2100,"It-mangement")

#Pozivanje metode work da ispise tekst
prvi_manger_objekt.work()
#Povecanje place 
print(prvi_manger_objekt.placa)

#Povecanje place
prvi_manger_objekt.give_raise(prvi_manger_objekt,600)
#Ispis nakon povecanja
print(prvi_manger_objekt.placa)

#Definiranje isntance klase Radnik 
radnik_objekt_jedan = Radnik("Goran", "Developer",1200)
radnik_objekt_jedan.work()