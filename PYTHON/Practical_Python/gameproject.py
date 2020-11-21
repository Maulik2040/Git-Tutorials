import random
lst = ["Snake", "Water", "Gun"]
print("Instructions -")
print("Type Snake for Snake on your keyboard")
print("Type Water for Water on your keyboard")
print("Type Gun for Gun on your keyboard")
a = input("Enter your choice from snake, water and gun")
Choice = random.choice(lst)
print(Choice)

score = 0
if(a==lst[0] and Choice==lst[0]):
     print("Your choice has matched")
     score+=10
    
    

 # Water and Water
elif(a==lst[1] and Choice==lst[1]): 
     print("Your choice has matched")

# Gun and Gun
elif(a==lst[2] and Choice==lst[2]):
    print("Your choice has matched") 
   
 

# Snake and Water
elif(a==lst[0] and Choice==lst[1]):
    print("You won")
    print("Your score is:", score + 1)

# Water and Snake 
elif(a==lst[1] and Choice==lst[0]):
    print("You loose")
    print("Your score is:", score - 1)
       

# Snake and Gun
elif(a==lst[0] and Choice==lst[2]):
     print("You loose")
     print("Your score is:", score - 1)
     

# Gun and Snake 
elif(a==lst[2] and Choice==lst[0]):
    print("You won")
    print("Your score is:", score + 1)
 

# Water and Gun 
elif(a==lst[1] and Choice==lst[2]):
    print("You won")
    print("Your score is:", score + 1)

# Gun and Water 
elif(a==lst[2] and Choice==lst[1]):
    print("You loose")
    print("Your score is:", score - 1)
    
else:
    print("Your choice is invalid")

    print(i)

