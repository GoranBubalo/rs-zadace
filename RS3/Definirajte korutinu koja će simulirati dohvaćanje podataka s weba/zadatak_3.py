import asyncio,time

# Baza korisnika
baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

# Baza podataka lozinki
baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autentifikacija(korisnik):

  await asyncio.sleep(3)
 
  
  pronadi_korisnik = next((item for item in baza_korisnika 
                          if item['korisnicko_ime'] == korisnik['korisnicko_ime'] 
                          and item['email'] == korisnik['email']), None)
  if not pronadi_korisnik:
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen"
  return await autorizacija(pronadi_korisnik,korisnik['lozinka']) 

async def autorizacija(korisnik, lozinka):
  await asyncio.sleep(2)  
  
   
  provjera_lozinke = next((item for item in baza_lozinka 
                           if item['korisnicko_ime'] == korisnik['korisnicko_ime'] and item['lozinka'] == lozinka ), None)
   
  if not provjera_lozinke: 
    return f"Korisnik {korisnik['korisnicko_ime']} : Autorizacija je neuspješna "
  

  return f"Korisnik {korisnik['korisnicko_ime']} : Autorizacija je uspješna "   

 
async def main():
  
 
  korisnik = {
   'korisnicko_ime': 'mirko123',
   'email': 'mirko123@gmail.com',
   'lozinka': 'lozinka1423'}
  start_time = time.time()
  rezultat = await autentifikacija(korisnik)
  end_time = time.time()
  print(f"Vrijeme izvršavanje je {end_time - start_time}")
  print(rezultat)



# Pokretanje programa
asyncio.run(main())
