#Remove duplicated numbers in list's
#Function that stores a list 
def remove_duplicated_number(number_list):
    #Use a special method that discard's duplicates
    #Store that in list and pass the data to remove_number variable 
    remove_number = list(set(number_list))
    #Output
    print(remove_number)
    
list_with_numbers = [1,2,2,3,4,5,6,6,7,8,8,9]
remove_duplicated_number(list_with_numbers)

#Other way to do that
#using the for loop 

#List with umbers - no filter
numbers = [1,2,3,4,5,5,6,7,7,8,9]
#List with filterd numbers
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)