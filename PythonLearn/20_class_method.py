class Employee:
    company = 'Mercedes'
    salary = 100                      # class attribute
    bonus = 10
    tax = 30
    location = 'Bangalore'
    
    def changeSalary(self,sal):
        self.salary = sal             # instance attribute
    
    def changeBonus(self,bon):        # This is one way to change the class attribute bonus
        self.__class__.bonus = bon    # but it is not recommended to do it this way
    
    @classmethod                      # Using class method to change class attribute
    def changeTax(cls, tax):          # This is the recommended way
        cls.tax = tax

e = Employee()
print (e.salary)
e.changeSalary(500)                   # Fails to change the class attribute
print (e.salary)
print (Employee.salary,'\n')
e.changeBonus(20)
e.changeTax(35)                       # Changes the class attribute using class method
print (Employee.bonus)
print (Employee.tax)

