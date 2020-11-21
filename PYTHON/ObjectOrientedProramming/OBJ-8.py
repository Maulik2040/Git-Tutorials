class Employee:
    increment = 1.5
    no_of_employee = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
       # self.email = fname + lname + '@gmail.com'
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
    @property
    def email(self):
        if self.fname==None:
            return 'Email not set'
        else:
            return self.fname + '.' + self.lname + '@gmail.com'
    @email.setter 
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
    @staticmethod
    def is_open(day):
        if day=='Sunday':
            return False
        else:
            return True
        
if __name__ == '__main__':
    maulik = Employee("Maulik", "Mishra", 90997)
    rohan = Employee("Rohan", "Das", 909)
    print(maulik.email+'\n'+rohan.email)
    rohan.lname = "Khanna"
    print(rohan.email)
    rohan.email = 'Khanna.Rohan@gmail.com'
    del rohan.email
    print(rohan.email)

#    def __add__(self, other):
#         return self.salary + other.salary
#     def __repr__(self):
#         return 'Employee: ({}, {}, {})'.format(self.fname, self.lname, self.salary)

#     def __str__(self):
#         return 'The name of Employee if {}'.format(self.fname)
# harry = Employee('Maulik', 'Mishra', 99000)
# rohan = Employee('Maulik', 'Mishra', 9)

# print(harry)
# shubham = Employee('Shubham', 'Skillf', 900)
# harry = Employee('harry', 'Jackson', 80000)
# maulik = Employee('Maulik', 'Mishra', 300000)
# Employee.change_increment(5)
# maulik.increase()
# lovish = Employee.from_str('lovish-jackson-7600')
# print(f'{lovish.fname}\n{lovish.lname}\n{lovish.salary}')

# class Programmer(Employee):
#     def __init__(self, fname, lname, salary, proglang, exp):
#         super().__init__(fname, lname, salary)
#         self.proglang = proglang
#         self.exp = exp
    
#     def increase(self):
#             self.salary = int(self.salary * (self.increment+0.2))
# harry = Programmer('harry', 'Jackson', 10000000, 'Python', '14 Years')
# help(Programmer)
