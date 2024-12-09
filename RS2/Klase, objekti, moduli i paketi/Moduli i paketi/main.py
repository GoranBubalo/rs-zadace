from shop import proizvodi
from shop.narudzbe import napravi_narudzbu, Narudba

# Lista proizvoda za dodavanje
proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]


# Pozivanje funkcije dodaj_proizvod za svaki proizvod u listi
for proizvod in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(
        proizvod["naziv"],
        proizvod["cijena"],
        proizvod["dostupna_kolicina"]
    ) 

# Ispis sadržaja liste
print("Sadržaj skladišta: ")
for proizvod in proizvodi.skladiste:
    proizvod.ispis()

# Lista proizvoda za narudžbu
naruceni_proizvodi_1 = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1},
]

naruceni_proizvodi_2 = [
    {"naziv": "Tipkovnica", "cijena": 200, "narucena_kolicina": 3},
    {"naziv": "Miš", "cijena": 100, "narucena_kolicina": 5},
]

# Kreiranje liste za narudžbe
narudzbe = []

# Kreiranje i dodavanje narudžbi
try:
    narudzba_1 = napravi_narudzbu(naruceni_proizvodi_1)
    narudzbe.append({"naruceni_proizvodi": narudzba_1.naruceni_proizvodi, "ukupna_cijena": narudzba_1.ukupna_cijena})

    narudzba_2 = napravi_narudzbu(naruceni_proizvodi_2)
    narudzbe.append({"naruceni_proizvodi": narudzba_2.naruceni_proizvodi, "ukupna_cijena": narudzba_2.ukupna_cijena})

    # Pozivanje metode za ispis narudžbi
    print("Ispis narudžbi:")
    narudzba_1.ispis_narudzbe()
    narudzba_2.ispis_narudzbe()

except ValueError as e:
    print(f"Greška: {e}")