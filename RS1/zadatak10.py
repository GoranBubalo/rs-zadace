#Brojanje riječi u tekstu 
def brojac_rijeci(tekst):


    #uklanjanje interpunkcije 
    for znak in ['.',',','!','?',':',';','-','_','(',')']:
        tekst = tekst.replace(znak, '')
    print(f"Tet after punctuation removal: {tekst}") #Debugging output
    
    #Razdvajanje texta u riječi  
    rijeci = tekst.split()
    print(f"List of words: {rijeci}") #Debuging output 
    
    #brojanje rijeci
    broj_rijeci ={} #spremanje brebrojenih riječi
    for rijec in rijeci: #prolazimo kroz svaku riječ unutra liste 'rjeci'
        if rijec in broj_rijeci: #provjeravamo jeli 'rijec' vec u riječniku
            broj_rijeci[rijec] += 1 #ako je onda povećavamo za jedan
        else:
            broj_rijeci[rijec] = 1 #ako nije dodajemo je s pocetnom vrijednoscu 1
    
    return broj_rijeci #vracamo rijecnik s brojem ponavljanja rijeci 

# Tekst za testiranje 
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

#Pozivanje funkcije i ispis rezultata
rezultat = brojac_rijeci(tekst)
print(rezultat)