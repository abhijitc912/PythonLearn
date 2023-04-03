fruits = ['mango', 'banana', 'grape', 'apple', 'orange']
i = 0
print ('Print list with while loop')
while i<len(fruits):
    print (fruits[i])
    i+=1

sports = ['football', 'cricket', 'motogp', 'tennis', 'badminton']
print ('\nPrint list with for loop')
for i in sports:
    print (i)

# Use while loops when you are not sure how long to run the loop
exits=["north","south","east","west"]
my_choise=""
while my_choise not in exits:
    my_choise= input("Enter your choise to exit: ")         # One cannot tell how soon someone will enter one of the four exits
    if my_choise.casefold()=="quit":                        # Convert any string to all lower case. So "Quit" will work as well
        print("Quit")
        break
    
print("Great! Finally you are out.")
