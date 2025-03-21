class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__ (self, fname, lname, salary):
        super().__init__(fname,lname)
        self.salary=salary
    
    def calculate_paycheck(self):
        return self.salary/12

class MonthlyEmployee(Employee):
    def __init__ (self, fname, lname, yearly_months, monthly_rate):
        super().__init__(fname,lname)
        self.yearly_months= yearly_months
        self.monthly_rate= monthly_rate
    
    def calculate_paycheck(self):
        return self.yearly_months*self.monthly_rate
