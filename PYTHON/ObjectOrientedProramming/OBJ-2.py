class Employee:
    increment = 1.5
    no_of_employee = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.4
        Employee.no_of_employee += 1
    def increase(self):
        self.salary = int(self.salary * self.increment) 
harry = Employee('harry', 'Jackson', 80000)
print(Employee.no_of_employee)
maulik = Employee('Maulik', 'Mishra', 80000)
print(Employee.no_of_employee)
print(Employee.__dict__)
maulik.increase()
print(maulik.salary)
# print(maulik.fname, maulik.lname)

# class Student:
#     def __init__(self, name, marks, Class):
#         self.Name = name
#         self.marks = int(marks)
#         self.Class = Class
# Maulik_Mishra = Student('Maulik Mishra', 100, '5th-A')
# print(Maulik_Mishra.marks)