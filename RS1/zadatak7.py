#Validacija i provjera jakosti lozinke 
def check_password(password):
    #Check the length of the password 
    if len(password) < 8 or len(password) > 15:
        print("Password need's to contain between 8 and 15 characters")
        return
    
    #Check if the password contains one Upper case and one letter
    if not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
        print("Password need's to contain al least one upper case and one digit")
        return
    
    #check if password contains the word password or lozinka 
    if 'password' in password.lower() or 'lozinka' in password.lower():
        print("Password can't contain the world password or lozinka ")
        return
    
    #Password is good 
    print("Password is strong!")

#User input from user 
password = str(input("Input a password: "))

#Call the function to check the password 
check_password(password)