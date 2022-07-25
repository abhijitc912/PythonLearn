class Employee:
    company = 'Tesla'
    
    def showDetails(self):
        print ('Tesla employee')

class Programmer(Employee):
    language = 'Python'
    # company = 'Microsoft'
    
    def getLanguage(self):
        print (f'Employee is expert in {self.language}')
    
    # def showDetails(self):
        # print ('Python programmer at Tesla')

e = Employee()
p = Programmer()

e.showDetails()
print (p.company) # Inherits from parent class
p.getLanguage()
p.showDetails()   # Inherits from parent class

