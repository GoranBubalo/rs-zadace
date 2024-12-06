#Kvadriranje broja 
def kvadriraj(x):
    return x ** 2
print(kvadriraj(2))

#lambda izraz 
print((lambda x : x**2)(5))

#ili

kvadriraj = lambda x : x**2
print(kvadriraj(4))

#Zbroji pa kvadriraj
def zbroji_pa_kvadriraj(a, b):
    return (a + b) ** 2

#lambda izraz 
print((lambda x, y: (x + y) **2 )(2,2))
#ili
zbroji_kvadriraj = lambda x, y: (x + y) **2 
print(zbroji_pa_kvadriraj(2,2))

#Kvadriraj duljinu niza 
def kvadriraj_duljinu(niz):
    return len(niz) ** 2
niz = [1,2,3,4,5,6,7,8,9]

print(kvadriraj_duljinu(niz))

#lambda izraz 
duljina_niza = lambda niz : len(niz) ** 2
print(duljina_niza(niz))
#ili
print((lambda niz : len(niz) ** 2)(niz))

#pomnozivrijednost s 5 pa potenciraj na x:
def pomnozi_i_potenciraj(x, y):
    return (y * 5) ** x
print(pomnozi_i_potenciraj(2,2))

#Lamnda izraz
mnozi_potenciraj = lambda x, y: (y * 5) ** x
print(mnozi_potenciraj(2,2))
#ili
print((lambda x, y : (y * 5) ** x)(2,2))

#Vrati True ako je broj paran, inače vrati None:
#Klasičan pristup
def paran_broj(x):
    if x % 2 == 0:
        return True
    else:
        return None

#lambda izraz 
print((lambda x : True if x % 2 == 0 else False)(4))
#ili
paran_nepara = lambda x : True if x % 2 == 0 else False
print(paran_nepara(5))