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
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split('-')
        return cls(fname, lname, salary)
    @staticmethod
    def is_open(day):
        if day=='Sunday':
            return False
        else:
            return True
shubham = Employee('Shubham', 'Skillf', 900)
# harry = Employee('harry', 'Jackson', 80000)
# maulik = Employee('Maulik', 'Mishra', 300000)
# Employee.change_increment(5)
# maulik.increase()
# lovish = Employee.from_str('lovish-jackson-7600')
# print(f'{lovish.fname}\n{lovish.lname}\n{lovish.salary}')

class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp
    
    def increase(self):
            self.salary = int(self.salary * (self.increment+0.2))



harry = Programmer('harry', 'Jackson', 10000000, 'Python', '14 Years')
help(Programmer)