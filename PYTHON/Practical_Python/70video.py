
# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{fname}.{lname}@codewithharry.com"

#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"

#     @property
#     def email(self):
#         if self.fname==None or self.lname == None:
#             return "Email is not set. Please set it using setter"
#         return f"{self.fname}.{self.lname}@codewithharry.com"

#     @email.setter
#     def email(self, string):
#         print("Setting now...")
#         names = string.split("@")[0]
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]

#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None


# hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

# print(hindustani_supporter.email)

# hindustani_supporter.fname = "US"

# print(hindustani_supporter.email)
# hindustani_supporter.email = "this.that@codewithharry.com"
# print(hindustani_supporter.fname)

# del hindustani_supporter.email
# print(hindustani_supporter.email)
# hindustani_supporter.email = "Harry.Perry@codewithharry.com"
# print(hindustani_supporter.email)

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
              return "Email is not set, please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


Hindustani_Supporter = Employee("Hindustani", "Supporter")
Nikhil_Singh = Employee("Nikhil", "Singh")

print(Hindustani_Supporter.email)

Hindustani_Supporter.fname = "US"


print(Hindustani_Supporter.email)
Hindustani_Supporter.email = "This.That@gmail.com"
print(Hindustani_Supporter.fname)

del Hindustani_Supporter.email
print(Hindustani_Supporter.email)
Hindustani_Supporter.email = "Harry.Perry@codewithharry.com"
print(Hindustani_Supporter.email)

