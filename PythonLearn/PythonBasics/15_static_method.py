# When we need some functionality not w.r.t an Object but w.r.t the complete class, we make a method static. 
# This is pretty much advantageous when we need to create Utility methods as they aren’t tied to an object lifecycle usually. 
# Finally, note that in a static method, we don’t need the self to be passed as the first argument.

class Employee:
    company='Amazon'
    def getSalary(self):                                                  # Inside a class a function is called a method. Outside a class it is a function
        print(f'Salary earned is {self.salary} at {self.company}')
                                                    # Leave 2 blank lines after defining a function
   
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

########################################################################################

class Calculator:

    def addNumbers(x, y):
        return x + y

# create addNumbers static method
Calculator.addNumbers = staticmethod(Calculator.addNumbers)

print('Sum:', Calculator.addNumbers(15, 10))

########################################################################################

# The above code can be written using @staticmethod

class NewCalculator:

    @staticmethod
    def addNumbers(x, y):
        return x * y

print('Product:', NewCalculator.addNumbers(15, 10))

