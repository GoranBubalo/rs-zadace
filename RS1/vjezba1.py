broj_1 = float(input("Unesite broj"))
broj_2 = float(input("Unesite broj"))
print(broj_1,broj_2)

operator = input("Unesite operator: *")
dozvoljeni_operatori = ["+","-","*","/"]

if operator in dozvoljeni_operatori:
    print("Nepodržan operator")

if operator == "+":
    print(f"Rezultat operacije {broj_1} + {broj_2} je {broj_1 + broj_2}")
elif operator == "-":
    print(f"Rezultat operacije {broj_1} - {broj_2} je {broj_1 - broj_2}")
elif operator == "*":
    print(f"Rezultat operacije {broj_1} * {broj_2} je {broj_1 * broj_2}")
elif operator == "-":
    if broj_2 == 0:
        print("Dijeljenje s nulom nije dozvoljeno")
    print(f"Rezultat operacije {broj_1} / {broj_2} je {broj_1 / broj_2}")