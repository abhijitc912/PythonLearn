class SpecialString:
    def __init__(self,cont):
        self.cont=cont
    def __truediv__(self,other):
        line="="*len(other.cont)
        return "\n".join([self.cont,line,other.cont])


fname = SpecialString("Abhijit")
lname = SpecialString("Chakraborty")
print(fname/lname)                                              # Overloading the division operator

###############################################################################################################################
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def __add__(self,num):                                      # Overloading the add operator
        return BankAccount(self.balance+num.balance)


a = BankAccount(100)
b = BankAccount(200)

result = a+b
print("Sum of Account balance: ",result.balance)

###############################################################################################################################

class Juice:
    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity
    
    def __add__(self,other):                                    # Here other has both name and capacity attribute 
        finnam = self.name+" & "+other.name
        fincap = str(self.capacity+other.capacity)+" L"
        return (finnam,fincap)
    
    
a = Juice("Orange",1.0)
b = Juice("Apple",2.0)

finjuice = a+b
print ("Name: ",finjuice[0],"\nCapacity: ",finjuice[1])
