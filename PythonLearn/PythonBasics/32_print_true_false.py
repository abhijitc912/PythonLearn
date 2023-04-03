print ("I","am","Abhijit","Chakraborty",sep="-",end="***\n",)
print (True>False)
print (False>True)
print ("Valse of True =",int(True),"and value of false =",int(False),sep=" ")
print ("Multiplying integers 2x3= ",2 * 3)
print ("Multiplying an integer 2 with a float 3.= ",2 * 3.)
print ("Division always returns a float. 6/2= ",6/2)
print ("This is an integer division 6/3= ",6//3)
print ("Integer division by default rounds off to the lesser digit. 6/4= ",6//4)
a = "A"
b = "B"
print ("Concatenate Strings stored in variables: ",a+b)
print ("Replicate strings: ",3*a)
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
tabbedString = "One\tTwo\tThree\tFour"
print(tabbedString)
splitString = """This string
is split over
several lines"""
print(splitString)

letters="abcdefghijklmnopqrstuvwxyz"
print(letters[25:0:-1])
print(letters[25::-1])
print("cde"in letters)
print("zab"in letters)
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31,"Jan","Mar","May","Jul","Aug","Oct","Dec"))
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}".format(28,30,31))
for i in range(1,11):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

item1 = "apple"
item2 = "orange"
print ("Item 1 is {} and item 2 is {}".format(item1,item2))
