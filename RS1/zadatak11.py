#Grupiranje elemenata po paritetu
#Funkcija koja prima listu brojeva 
def numbers_list(numbers):
    even_numbers = [num for num in numbers if num % 2 ==0]
    odd_numbers = [num for num in numbers if num % 2 !=0]
    result = {'parni': even_numbers, 'neparni': odd_numbers}
    print(result)




#declaring a list of numbers 
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
numbers_list(list_of_numbers)