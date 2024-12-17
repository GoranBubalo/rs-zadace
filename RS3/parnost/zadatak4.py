import asyncio, random, time

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    
    if broj % 2 != 0:
        return f"Broj {broj} je neparan"
    return f"Broj {broj} je paran"


async def main():
     
    start_time = time.time()
    
    brojevi = [random.randint(1,100) for _ in  range(10)]
    
    zadatci = [asyncio.create_task(provjeri_parnost(broj)) for broj in brojevi]
    
    rezultati = await asyncio.gather(*zadatci)
    for rezultat in rezultati:
        print(rezultat)
    end_time = time.time()
    print(f"Vrijeme trajanja izvršenja je: {end_time - start_time:.2f}")
    
asyncio.run(main())