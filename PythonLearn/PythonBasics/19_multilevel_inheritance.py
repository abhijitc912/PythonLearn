class Citizen:
    print ('\nCitizen is born\n')
    country = 'India\n'
    
    def payTax(self):
        print ('Farmers are citizens but do not need to pay tax\n')

class Employee(Citizen):
    company = 'Google\n'
    print ('Employee is recruited\n')
    def payTax(self):
        print ('Do you pay tax?')
        print ('I am an employee. I have to pay tax.\n')

class Programmer(Employee):
    print ('Programmer is inducted\n')
    def payTax(self):
        super().payTax()
        print ('Also since I am a programmer. I pay very high tax.\n')
                                                # Leave 2 blank lines after defining a function
   
print ('#######################################\n')
c = Citizen()
e = Employee()
p = Programmer()

print ('***************************************\n')
print (f'Country of citizen is: {c.country}')
print (f'Country of employee is: {e.country}')
print (f'Country of programmer is: {p.country}')
print (f'Company of programmer is: {p.company}')

c.payTax()
e.payTax()
p.payTax()

