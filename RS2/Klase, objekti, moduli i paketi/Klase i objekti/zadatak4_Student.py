#Definiranje šablone/Klase 
class Student:
    #Konstruktor
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
        
    #Metoda za ispis
    def ispis(self): 
        print(f"Ime: {self.ime}, Prezime: {self.prezime}, Godine: {self.godine}, Ocjene: {self.ocjene}")
    
    def prosjek(self):
        #Računanje prosjeka
        #Suma svih ocjena podijelimo s koliko ocjena smo dobili to dobivamo s len funkcijom 
        prosjecna_ocjena = sum(self.ocjene) / len(self.ocjene)
        print(f"{self.ime} {self.prezime} ima porsjecnu ocjenu {prosjecna_ocjena}")
    

#Lista studenata
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

#Stvaranje za svakog studenta objekt klase Student i dodavanje u novu listu studneti_objekti
student_objekti = [Student(student["ime"], student["prezime"], student["godine"],student["ocjene"]) for student in studenti]



#iteracije - prikaz 
for student_objekt in student_objekti:
    student_objekt.ispis()

#Iteracija za svakog studenta u listi studenti 
for student_objekt in student_objekti:
    student_objekt.prosjek()
    
# Pronalaženje najvećeg prosjeka
najveci_prosjek = max(sum(student.ocjene) / len(student.ocjene) for student in student_objekti)

# Filtriranje studenata koji imaju najveći prosjek
najbolji_studenti = [student for student in student_objekti if sum(student.ocjene) / len(student.ocjene) == najveci_prosjek]

# Ispis svih najboljih studenata
for student in najbolji_studenti:
    prosjecna_ocjena = sum(student.ocjene) / len(student.ocjene)
    print(f"Najbolji student: {student.ime} {student.prezime} s prosjekom {prosjecna_ocjena:.2f}")

        

