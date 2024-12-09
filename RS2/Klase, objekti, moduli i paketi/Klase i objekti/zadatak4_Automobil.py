import datetime
import math

#Definiranje Klase
class Automobil:
    #Konstruktor - definiranje atributa klase 
    def __init__(self, marka, model, godina_proivodnje, kilometraža):
        self.marka =marka
        self.model = model
        self.godina_proizodnje = godina_proivodnje
        self.kilometraža = kilometraža
    #Metoda za ipsis atributa klase
    def ispis(self):
        print(f"Marka je {self.marka}")
        print(f"Model je {self.model}")
        print(f"Godina proizvodnje je {self.godina_proizodnje}")
        print(f"Kilometraža je {self.kilometraža}")
        
    #Metoda za ispis starosti automobila 
    def starost(self):
        trenutacna_godina = datetime.datetime.now().year
        rezultat = trenutacna_godina - int(self.godina_proizodnje)
        print(f"Automobil je star {rezultat} gdine ")



    
#Storanje objekta klase Automobil
auto_jedan = Automobil("Mercedes", "MD01", "2020", 10000)

#Ispis atributa iz objekta auto_jedan nastao iz šablone Automobili
auto_jedan.ispis()

#Pozivanje metode za izračun starosti automobila
auto_jedan.starost()