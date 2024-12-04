#Viježba 2 prijsetupna godina 

#User input
year = int(input("Insert the year: ")) #Casting to integer data type

#Check if leap year 
if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Year {year}, is a leap year")
else:
    print(f"Year {year}, is not a leap year")


