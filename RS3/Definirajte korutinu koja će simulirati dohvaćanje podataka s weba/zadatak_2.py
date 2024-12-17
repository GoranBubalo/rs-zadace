# Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba

# Prva korutina
# Lista proizvoljnih riječnika (npr. podatci o korisniku)
# neka vrati nakon 3 sekunde

# Drugak korutina 
# lista proizvojih riječnika (npr. podatci o proivodima)
# vrati nakon 5 sekundi 

# Korutine treba pozvati konkurentno korištenjem asyncio.gather() i ispišite rezultate

# Program se mora izvršiti u 5 sekundi 

import asyncio
import time

# Prva korutina user data 
async def user_data():
    
    # Dohvaćanje podatka sa web-a 
    user_data_dictionary = [{"ime" : "Ivan", "prezime" : "Matešić", "godina_rođenja" : 1999},
                            {"ime" : "Marko", "prezime" : "Ivčić", "godina_rođenja" : 2000},
                            {"ime" : "Stipe", "prezime" : "Ban", "godina_rođenja" : 2001},
                            {"ime" : "Gordan", "prezime" : "Markijević", "godina_rođenja" : 1995},
                            {"ime" : "Josip", "prezime" : "Josipović", "godina_rođenja" : 2003}]
    await asyncio.sleep(3) # Simulacija čekanja 3 sekunde 
    return user_data_dictionary

async def product_data():
    # Gohvačanje podataka s web-a 
    product_data_dictionary = [{"product_name" : "Mlijeko", "product_maker" : "Dorino ", "coutry_of_origin" : "Croatia"},
                               {"product_name" : "Čokolada", "product_maker" : "Milka", "coutry_of_origin" : "Švica"},
                               {"product_name" : "Sir", "product_maker" : "PagoSir ", "coutry_of_origin" : "hhh"},
                               {"product_name" : "Salama", "product_maker" : "SalamaFirma", "coutry_of_origin" : "svs"}]
    await asyncio.sleep(5) #
    return product_data_dictionary

async def main():
    pocetno_vrijeme = time.time() # Spremanje vrijednosti pocetka vremena u varijablu 
    user_podatci , proizvod_podatci = await asyncio.gather(user_data(),product_data())
    print(f"user podatci s web-a: {user_podatci} ")
    print(f"Podatci proizvoda s web-a: {proizvod_podatci}")
    zavrsno_vrijeme = time.time()
    proslo_vremena = zavrsno_vrijeme - pocetno_vrijeme # Spremanje zavrsetna vremena u varijablu 
    print(f"Proslo je vremena: {proslo_vremena}") # zavrsetak - pocetak = rezultat ukupnog vremena 



asyncio.run(main())