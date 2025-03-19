from Employee import Employee

class Company:
    def __init__(self):
        self.employees = []                                         # define a property called employees which equals to an empty list
    
    def add_employee(self, new_employee):                           # add_employee method takes in an employee object which will call new_employee
        self.employees.append(new_employee)                         # append the new_employee to the employees list property we defined above.

    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname,i.lname)
        print('----------------------------')
    
    def pay_employees(self):
        print('Paying employees')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: Rs.{ i.calculate_paycheck():,.2f}')
            print('----------------------------------')

def main():
    my_company = Company()                                          # Create a company object in the main program. It is called my_company and set it equal to the Company() constructor 

    employee1 = Employee('Abhijit','Chakraborty', 3600000)
    my_company.add_employee(employee1)
    employee2 = Employee('Subhajit','Chakraborty', 2400000)
    my_company.add_employee(employee2)
    employee3 = Employee('Srijeet','Chakraborty', 6000000)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()