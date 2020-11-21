import random
lst = ["Snake", "Water", "Gun"]
print("Instructions -")
print("Type Snake for Snake on your keyboard")
print("Type Water for Water on your keyboard")
print("Type Gun for Gun on your keyboard")

p =1
q= 1
for i in range(0,10):
    a = input("Enter your choice from snake, water and gun")
Choice = random.choice(lst)
print(Choice)
if a == Choice:
   p=p+1
else:
   q=q+1
  
print ("Match Score",p)
print  ("Non Match Score",q)