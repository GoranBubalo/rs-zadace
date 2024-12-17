# Definirajte korutinu koja će simulirati dohvaćanje podataka s weba

# Lista brojeva od 1 do 10 - vratiti nakon 3 sekunde
# lista definirana coprehensionom
# nakon isteka vremena ispis poruke "Podaci dohvaćeni."
# bez korištenja asyncio.gather() i asyncio.create_task() funkcija.

import asyncio


async def povrat_liste_nakon_3_sekund3():
    print("Dohvaćanje podataka s weba....")
    # Definiraj listu pmoću comprehensiona
    lista_borojeva = [broj for broj in range(1,11)]
    await asyncio.sleep(3) # Vratiti nakon 3 sekunde - simulacija kašnjenja 
    print("Podatci dohvaćeni")
    return lista_borojeva


async def main():
    podatci_s_weba = await povrat_liste_nakon_3_sekund3()
    print(f"Podatci:  {podatci_s_weba}")
    print(f"Tip podatka je {type(podatci_s_weba)}")
    
# vrti program
asyncio.run(main())