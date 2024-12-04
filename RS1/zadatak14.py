#Prosti brojevi 
def isPrime(number):
    #Checking if the number is smaller or equal to 1 
    if number <= 1:
        return False
    
    #Check if the number is devidable with 2 to number - 1
    for i in range(2, number):
        if number % i ==0:
            return False # If the number is devidable it is no a Prime number
    return True

print(isPrime(10))
print(isPrime(7))
    