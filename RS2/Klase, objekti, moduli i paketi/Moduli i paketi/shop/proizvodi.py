#Definiranje Klase
class Proizvod:
    #Konstruktor
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina
    
    #metoda za ispis svih atributa proizvoda
    def ispis(self):
        print(f"Naziv proizvoda je {self.naziv}, cijena proizvoda je "
              f"{self.cijena}, a dostupna kolicina je {self.dostupna_kolicina} ")

# Definiranje funkcije koja dodaje novi porizvod u listu skladiste
def dodaj_proizvod( naziv, cijena, dostupna_kolicina):
    #Kreiranje novog objekta 
    novi_proizvod = Proizvod(naziv, cijena, dostupna_kolicina)
    skladiste.append(novi_proizvod)

skladiste = []

#dodaj_proizvod("Coca-Cola", 3,40)
#dodaj_proizvod("Pepsi",4,30)
   
#Inicializacija dva objekta Klase Proizvod
proizvod_1 = Proizvod("Mlijeko", 1.5, 20)#Prvi proizvod
proizvod_2 = Proizvod("Kruh", 0.8,50)#Drugi hruh

#Pohranjivanje 2 proizvoda(objekta) u listu skladiste
#skladiste = [proizvod_1,proizvod_2]

#Ispis objekta (proizvod) iz liste skladište
#for proizvod in skladiste:
 #   proizvod.ispis()