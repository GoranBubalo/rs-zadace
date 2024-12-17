# import važne biblioteke
import aiohttp, asyncio, time


# dohvaćanje korisnika
async def fetch_users(session):
    respones = await session.get("https://jsonplaceholder.typicode.com/users")
    fact_dict = await respones.json()
    return fact_dict

# glavna korutina 
async def main():
    async with aiohttp.ClientSession() as session:
        
        start_time = time.time()
        
        dohvat_korisnika = [fetch_users(session) for _ in range(5)]
        rezultat = await asyncio.gather(*dohvat_korisnika)
        
        # Korisnici je lista koja sadržava više lista korisnika biramo listu element 0 
        korisnici = rezultat[0]
        # Lista imena korisnika 
        imena_korisnika = [korisnik["name"] for korisnik in korisnici ]
        # Lista emaila
        emailovi = [email["email"] for email in korisnici]
        #Lista username
        usernamovi = [username["username"] for username in korisnici]
        
        print(imena_korisnika)
        print(emailovi)
        print(usernamovi)
        
        end_time = time.time()
        
        print(f"Vrijeme izvođenja je {end_time - start_time} sek")

# Glanvna funkcija za ozvianje glavne korutine
asyncio.run(main())