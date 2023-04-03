class Employee:
    company = 'Google'
    empCode = 62819

class Freelancer:
    company = 'CloudGuru'
    level = 1
    
    def upgradeLevel(self):
        self.level = self.level + 1

#class Programmer(Employee,Freelancer):
class Programmer(Freelancer,Employee):
    name = 'Abhi'

p = Programmer()
print (p.name)
print (p.company) # Inherits from parent
print (p.empCode)
print (f'Initial level: {p.level}')
p.upgradeLevel()
print (f'Level after upgrade: {p.level}')
