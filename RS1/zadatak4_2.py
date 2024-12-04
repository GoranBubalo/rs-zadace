#Guess what is wrong with this code
broj = 10 #Setting the number 
while broj > 0: #loop is running until the number is bugger then 0
  broj -= 1 #Lower the number by -1
  print(broj) #Output
  if broj < 5: #When number is smaller then 5 
    broj += 2 #Increment the number by 2 
    
    #Problem is that the number   gets to 5 than it is incremented by 2 
    #Then we have an infinitive loop