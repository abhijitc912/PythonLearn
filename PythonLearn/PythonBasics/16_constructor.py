class Employee:
    def __init__(self,name,salary,department):      # Constructor: This function will get executed even if not called
        self.name = name
        self.sal = salary         # Here self.sal will be used by other functions to fetch salary
        self.dept = department
        print ('Employee created')
                                                    # Leave 2 blank lines after defining a function
   
    def getDetails(self):
        print(f'Name of the employee is {self.name}')
        print(f'Salary of the employee is {self.sal}')
        print(f'Department of the employee is {self.dept}')
                                                    # Leave 2 blank lines after defining a function
   
abhijit = Employee('Abhijit Chakraborty',100,'NSS')
abhijit.getDetails()
