#Guess the number 

hidden_number = 47
guess_number = 0
number_is_guessed = False

while not number_is_guessed:
    #User input of the number 
    number = int(input("Guess the number: "))
    #Increment the number by one 
    guess_number +=1
    
    #If the number is smaller 
    if number < hidden_number:
        print("To low...")
    #If the number is higher
    elif number > hidden_number:
        print("To high number...")
    #Code that will will dislay that the number is guessed 
    else:
        print(f"You guessed the number in this many {number} tries ")
        #The number is Guessed convert the number_is_guessed to true 
        number_is_guessed=True
#Print that the game is over 
print("Game is over ")