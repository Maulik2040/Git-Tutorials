class Employee:
    increment = 1.5
    no_of_employee = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.increment = 1.4
        Employee.no_of_employee += 1
    def increase(self):
        self.salary = int(self.salary * self.increment) 
    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount
harry = Employee('harry', 'Jackson', 80000)
maulik = Employee('Maulik', 'Mishra', 300000)
print(maulik.salary)
Employee.change_increment(5)
maulik.increase()
print(maulik.salary)
