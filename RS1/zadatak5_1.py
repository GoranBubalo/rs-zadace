
#User input of the number 
the_number = int(input("Input a number: "))
the_result = 1

while the_number > 1:
    the_result *= the_number
    the_number -= 1

print(f"Factorial is {the_result}")