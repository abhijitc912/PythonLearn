class Employee:
    company='Amazon'
    def getSalary(self):
        print(f'Salary earned is {self.salary} at {self.company}')
    
    @staticmethod
    def greet():
        print('Good morning!')
        
abhijit = Employee()
abhijit.salary = 100000
abhijit.getSalary() 
# Above line is same as:
Employee.getSalary(abhijit)

abhijit.greet()
# To make above line work similar to the previous one
# we have to type @staticmethod before the greet() function
# This will help to read the code like:
Employee.greet()
# @staticmethod is decorator

