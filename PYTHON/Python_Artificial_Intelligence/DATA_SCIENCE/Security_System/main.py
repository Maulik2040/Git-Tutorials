import pandas as pd
import random
First_Name = input("Enter the first name: ")
Last_Name = input("Enter the last name: ")
Phone_Number = input("Enter the Phone Number: ")
Code = random.randint(1000, 100000)
Data = pd.DataFrame([[First_Name, Last_Name, Phone_Number, Code]], columns=['First Name', 'Last Name', 'Phone', 'Code'])
print("Code:", Code)
print(Data)
Data.head(4)
Data.to_csv(f'{Code}.csv')
print("Data Collected Successfuly")