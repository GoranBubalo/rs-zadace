def count_vowels_consonants(text_value):
    #Samoglasnici -> (a, e, i, o, u)
    #Suglasnik -> ()
    
    #Variable for counting 
    vowels = 0
    consonants = 0
    
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    
    #Going through each char in text
    for char in text_value:
        #Logic for recognizing char and counting 
       if char.isalpha(): #Checking if the simbol is a letter
           if char.lower() in vowels_list:
               vowels += 1
           else:
               consonants += 1
           
        
    
    #Returning the value
    return {'samoglasnici': vowels, 'suglasnici': consonants}
    
    

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
result = count_vowels_consonants(tekst)
print(result)