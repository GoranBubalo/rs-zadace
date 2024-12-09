class Narudba: 
    # Definiraj konstruktor
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena
    # Metoda za ispis narudžbe
    def ispis_narudzbe(self):
        proizvodi_opis = ", ".join(
            f"{proizvod['naziv']} x {proizvod['narucena_kolicina']}"
            for proizvod in self.naruceni_proizvodi
        )
        print(f"Naručeni proizvodi: {proizvodi_opis}, Ukupna cijena: {self.ukupna_cijena} eura")

    

# Metoda koja prima listu proizvoda kao argument 
# vraća novu instancu klase Narudzba 
def napravi_narudzbu(lista_proizvoda):
    # Provjera 1: Argument mora biti lista
    if not isinstance(lista_proizvoda, list):
        raise ValueError("Argument 'lista_proizvoda' mra biti lista")
    
    # Provjera 2: Lista ne smije biti prazna
    if len(lista_proizvoda) == 0:
        raise ValueError("Lista ne smije biti prazna")
    
    # Provjera 3 i 4: Svi elementi moraju biti rječnici s traženim ključevima
    for proizvod in lista_proizvoda:
        if not isinstance(proizvod, dict):
            raise ValueError("Svaki element u listi mora biti rječnik.")
        if not all(key in proizvod for key in ["naziv", "cijena", "narucena_kolicina"]):
            raise ValueError("Svaki rječnik mora adržavati ključeve: 'naziv', 'cijena', i 'narucena_kolicina'.")
    
    
               

       
    # Izračun ukupne cijene
    ukupna_cijena = sum(proizvod["cijena"] * proizvod["narucena_kolicina"] for proizvod in lista_proizvoda )
    
    #kreiraj nove instance klase Narudzba
    nova_narudzba = Narudba(lista_proizvoda,ukupna_cijena)
    
    #vrati novu instancu
    return nova_narudzba

