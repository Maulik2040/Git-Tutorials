import cv2
import math

# This is My first comment
# print("Hello World !\n")
# print (5+8)
# print(math.gcd(8,12)) 
'''
This is a multiple line comment
My first comment in python proramming
'''
# This is also a comment
#if(age<18):
#print("HELLO")

# Quiz : Try these operators
# 1. **Exponentiation operator
# 2. //Floor division operator
# 3. % Modulo operator

# a = 34
# b = "Harry"
# c = 45.90
# d= 2

# print(a + d)
# print(a - d)
# print(a / d)
# print(a * d)

#  1.Wrong Syntax
#  2.Maulik project
#  3.Rules for creating variables
#  4.A variable should start with a variable or underscore
#  5. A variable cannot start with a number
# It can only contain alpha numeric characters
# variable names are case sensative Maulik and maulik are different variable
# typeb = type(b)
# print(typeb)

# s = 22
# t = 44
# a = s+t
# print(a)

# r = 11
# o = 22
# l = 33
# e = 44
# a = r/o/l/e
# print(a)
 
# e = "31"
# e =  str(31)
# typee = type(e)
# print(typee)
# print(e*4)

# name = "Maulik"
# print(name[0:5])
# print(name)
# print(name.strip())
# print(len(name))

# var = name.lower()
# var = name.upper()
# var = name.replace("k" ,"i")
# print(var)

# stri = "This is a "
#  name = "cat"
# stri2 = "This is not a "
# print(stri + name)
# name1 = "cat"
# name2 = "cute"
# # temp = "This is a {1}. It is very {0} ".format(name1, name2)
# temp = f"This is a {name1}. It is very {name2} ".format(name1, name2)
# print(temp)

'''
Python collection:

1. List
2. Tuple
3. Set
4. Dictionary
'''
# list
# lst = [61, 2, 3, 4, 6, 41]
# var = type(lst)
# lst[2] = 45
# var = lst[1]
# var = lst[0:5]
# var = lst
# lst.append(100)
# lst.append(200)
# lst.append(300)
# lst.insert(0, 700)
# lst.remove(61)
# var = len(lst)
# del lst[3]
# lst.clear()
# lst.clear()
# print(var)


#  Tuple
# a = ("Maulik", "Mummy", "Papa" )
# var = a
# a = list(a)
# a[0] = "Maulik Mishra"
# var = type(a)
# print(var)

# Set
# s1 = {1,2,3,4,5,6,7,8,8,8,8,8,9,10,777,}
# s1.add(444444)
# s1.update([555, 666, 777, 888, 999, 777 ])
# print(len(s1))
# s1.remove(777)
# s1.discard(1666)
#Like list: .pop, uninion, clear, del, intersection
# print(s1)

# Maulikdict = {
# "Name": "Maulik",
# "Class": "5th",
# "Marks": 40,
# "Hours in school": 6


# }
# Maulikdict["Marks"] = 39
# print(Maulikdict["Marks"])
# Maulikdict.pop('Marks')
# del, clear, pop, update
# print(Maulikdict)

# age = 34
# age = input("Enter your age")
# print(age) 

# The Programme is enough for today

# Next Day

# age = 18
# if(age<18):
#     print("you are smaller than 18 years old")

# elif(age==18):
#     print("You are 18 years old")

# else:
#  print("you are bigger than 18 yers old")

# Loop:
# scinario: print numbers from 1 to 1000
# for i in range(0, 1000):
    # print(i)

# li = [1,2,3,4,5,6,7,8]
# for item in li:
#     print(item)

# for i in range(0,100):
#    print(i)

# program to find the ASCII value of the given character

# c = 'p'
# print("The ASCII value of '" + c + "' is", ord(c))

# use for loop to iterate dictionary, sets and tuples
# i = 0

# Acscii Value 
# for i in range(97,123):
#    print(chr(i))
# i=0
# while(i<100):
#   print(i)
#   if  i ==78:
#       continue
#   i=i+1

# Functions
def greet():
    print("Good Morning")
    print("Good Afternoon")
    print("Good Evening")

greet()

# def sum(a,b):
#     c=a-b
#     return c

# d=sum(21,34)
# print(d)

# class Employee:
#    def __init__(self, gname, gsalary):
#         self.name = gname
#         self.salary = gsalary

# Maulik = Employee("Om", 40000)
# print(Maulik.name)
# print(Maulik.salary)
