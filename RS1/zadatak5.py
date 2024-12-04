#Faktorijel broja 

#User input of the number 
the_number = int(input("Input a number: "))
the_result = 1 

for i in range(1,the_number + 1):
    the_result *= i

print(f"Factorial of {the_number} is {the_result}")