# importanje biblioteka 
import asyncio, aiohttp

# korutina za dohvačanje činjenica
async def get_dog_fact(session):
    print("Činjenice o psima....")
    response = await session.get("https://dogapi.dog/api/v2/facts")
    cinjenice = await response.json()
    return cinjenice

# Korutina za dohvacanj cinjenica o mackama
async def get_cat_fact(session):
    print("Dohvaćanje činjenica o macama.....")
    response = await session.get("https://catfact.ninja/fact")
    cinjenice = await response.json()
    return cinjenice



# Glavna korutina 
async def main():
    # Definirati klijent sesiju
    async with aiohttp.ClientSession() as session:
        
        # pet pasa
        lista_psi = [get_dog_fact(session) for _ in range(5)]
        
        # pet macaka
        lista_mace = [get_cat_fact(session) for _ in range(5)]
        
        # psi i mace u istu listu 
        dog_cat_facts = await asyncio.gather(*lista_psi,*lista_mace)
        
        # Ispis toga 
        for fact in dog_cat_facts:
            print(fact)
        
  


asyncio.run(main())