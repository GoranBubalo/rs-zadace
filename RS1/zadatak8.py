#Function to print out only even numbers 
def filter_even_numbers(list):
    #
    even_number_list = [num for num in list if num % 2 == 0]
    print(even_number_list)
    
    
    
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_even_numbers(list_numbers)