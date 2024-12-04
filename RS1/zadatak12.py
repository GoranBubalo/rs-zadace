#Obrnute rječnik
def reverse_grammar_list(dictionary):
    return{value: key for key, value in dictionary.items()}
    
    
    

rijecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
rezultat = reverse_grammar_list(rijecnik)
print(rezultat)