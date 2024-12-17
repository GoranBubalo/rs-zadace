# import biblioteke
import asyncio, aiohttp


# Dohvaćanje ćinjenica o mačkama 
async def get_cat_fact(session):
    print("šaljemo zahtjev za mačji fact ")
    response = await session.get("https://catfact.ninja/fact") 
    rezultat = await response.json()
    return rezultat['fact']

# korutina za filtriranje
async def filter_cat_facts(stara_lista):
    return [fact for fact in stara_lista if 'cat' in fact.lower() or 'cats' in fact.lower()]    
    
# Glavna korutina 
async def main():
    async with aiohttp.ClientSession() as session:
        
        # Dohvaćanje 20 činjenica o mačkama 
        task = [get_cat_fact(session) for _ in range(20)]
        all_task = await asyncio.gather(*task)
        
        filtrirane_mace = await filter_cat_facts(all_task)
        
        print("Filtriranje činjenica o mačkama: ")
        for maca in filtrirane_mace:
            print(f"- {maca}")


# Funkcija za ispis gavne korutine 
asyncio.run(main())