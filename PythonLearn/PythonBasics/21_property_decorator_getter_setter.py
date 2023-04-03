class Employee:
    company = 'TVS'
    salary = 5500
    bonus = 500
    
    @property                                      # Property decorator a.k.a getter method
    def totalSalary(self):
        return self.salary + self.bonus
    
    @totalSalary.setter                            # Setter method to dynamically change the class attribute
    def totalSalary (self, newtotsal):
        self.bonus = newtotsal - self.salary
        
    
e =Employee()
print ('Initial salary: ',e.salary)
print ('Initial bonus: ',e.bonus)
print (f'Initial total salary: {e.totalSalary}\n')  # Without property decorator we would have to use here
# print (e.totalsalary())                           # print (e.totalsalary())

e.totalSalary = 7000
print ('New Salary: ',e.salary)
print ('New bonus: ',e.bonus)
print ('New total Salary: ',e.totalSalary)
