#Napišite sljedeće funkcije 

#Funkcija koja vraća n-torku s prvim i zadnjim elementom liste u jednoj liniji koda.
def return_first_last(list):
    last_tuple = list[-1]
    first_tuple = list[0]
    return (first_tuple,last_tuple)
#Funkcija za minimalni i maksimalni element 
def max_min_elements(lista_one):
    #Check if the list is empty 
    if not lista_one:
        return None #If the list is empty then return None
    
    
    #Setting the first element as the beggining for max and min element
    max_element = lista_one[0] 
    min_element = lista_one[0]
    
    #Go through the list 
    for number in lista_one:
        #Check if the number is bigger than max
        if number > max_element:
            max_element = number #set new value 
        #Check if the number is smaller than min
        if number < min_element:
            min_element = number  #Set new value 
    return (max_element, min_element)

#Funkcija presjka koji prima dva skupa i vraća novi skup s elementima koji se nalaze u oba skupa 
def finding_common_elements_in_both_lists(list_two, list_three):
    return list_two & list_three


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prvi_i_zadnji = return_first_last(lista)
print(prvi_i_zadnji)


lista_one = [5, 10, 20, 50, 100, 11, 250, 50, 80]
result = max_min_elements(lista_one)
print(result)

#Example 
skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
new_result = finding_common_elements_in_both_lists(skup_1,skup_2)
print(new_result)

