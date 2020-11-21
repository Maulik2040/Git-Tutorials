import pandas
import time


Stock = pandas.read_excel('Stock.xlsx')








Need = input("Enter your need here: ")

if Need==Stock['Item'][0] or Need==Stock['Item'][1] or Need==Stock['Item'][2] or Need==Stock['Item'][3] or Need==Stock['Item'][4] or Need==Stock['Item'][5] or Need==Stock['Item'][6] or  Need==Stock['Item'][7]:
    print(Need, "is available")
    time.sleep(2)
    input_yes_no = input("Would you like to buy the item (Yes or No): ")

    if input_yes_no=="Yes":
        Ask_Code = input("Enter your Python Account Number: ")
        print("Successfuly credited amount from Account Number:", Ask_Code)
        
      



    

    else:
        print("Quiting....")
        time.sleep(1)
        print("Quited")

    

    
    

else:
    print("Your item is not available")