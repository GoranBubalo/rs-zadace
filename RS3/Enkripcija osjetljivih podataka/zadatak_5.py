# importamo asyncio biblioteku za asinkrono programiranje
import asyncio

# Definirati listu zadaci s 3 riječnika
zadatci = [
    {'prezime' : 'Matešić', 'broj_kartice' : '009333835234', 'CVV': '4553'},
    {'prezime' : 'Jurešić', 'broj_kartice' : '007863835234', 'CVV': '2511'},
    {'prezime' : 'Milčić', 'broj_kartice' : '234333835987', 'CVV': '0953'}
]

# Definiramo korutinu za sigurnost podataka
async def secure_data(podatci):
    # Enkripcija traje 3 sekunde 
    await asyncio.sleep(3)
    
    osjetljivi_podatci = {
        'prezime' : podatci['prezime'],
        'broj_kartice' : hash(podatci['broj_kartice']),
        'CVV' : hash(podatci['CVV'])
    }
    return osjetljivi_podatci


# Glavna korutina
async def main():
    # Pokrećemo sve korutine paralelno i čega da se sve izvrše i onda to sprema u listu 
    rezultati = await asyncio.gather(*(secure_data(zadatak)for zadatak in zadatci))
    
    # Ispis liste rezultata
    for rezultat in rezultati:
        print(rezultat)



# Pokretanje glavne korutine 
asyncio.run(main())