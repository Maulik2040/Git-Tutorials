class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
harry = Employee('harry', 'Jackson', 80000)
maulik = Employee('Maulik', 'Mishra', 80000)
print(maulik.fname, maulik.lname)

# class Student:
#     def __init__(self, name, marks, Class):
#         self.Name = name
#         self.marks = int(marks)
#         self.Class = Class
# Maulik_Mishra = Student('Maulik Mishra', 100, '5th-A')
# print(Maulik_Mishra.marks)