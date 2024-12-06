#Obrnute rječnik
def reverse_grammar_list(dictionary):
    #Declaring a empry Dincionary
    reverse_dictionary = []
    for key, value in dictionary.items():
        reverse_dictionary[value] = key #Swaping key and value 
    return reverse_dictionary
    
    
    

rijecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
rezultat = reverse_grammar_list(rijecnik)
print(rezultat)