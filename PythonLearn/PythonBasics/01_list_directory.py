# Author: Abhijit Chakraborty
# Location: Bangalore
# Company: Amadeus Labs

# Select all lines to comment out and then use Ctrl+"/". 
# Automatically all lines will be prefixed with "#" and consequently commented out
# You can repeat same to uncomment lines

import os
print (os.listdir())

ints = [1,2,4]
a,b,c = ints
print (a,b,c)

###################################################################################

mylist = []
if not mylist:
    print ("The list is empty")
else:
    print ("The list is not empty")

###################################################################################

# Using the get method
acronyms = {'LOL': 'Laugh out loud',
            'IDK': "I don't know",
            'TBH': 'to be honest'}

sentence = 'IDK'+' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)

####################################################################################

current_movies = {'The Grinch': '11:00 am',
                  'Rudolph': '01:00 pm',
                  'Frosty the Snowman': '3:00 pm',
                  'Christmas Vacation': '05:00 pm'}

print ("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)

######################################################################################

menus = {'Breakfast': ['Egg Sandwich','Bagel', 'Coffee'],
         'Lunch': ['Rice', 'Beans','Fish'],
         'Dinner': ['Bread', 'Chicken','Salad']}

for name, menu in menus.items():
    print(name,':',menu)

######################################################################################

# Nested Dictionary

contacts = {
    'number' : 4,
    'students' : 
        [
            {'name':'Abhijit Chakraborty', 'email':'abhijit@mycompany.com'},
            {'name':'Harry Potter', 'email':'harry@mycompany.com'},
            {'name':'Hermione Granger', 'email':'hermione@mycompany.com'},
            {'name':'Ron Weasley', 'email':'ron@mycompany.com'}
        ]
}    

print('Student details:')
for student in contacts['students']:
    print(student)

print('Student emails:')
for student in contacts['students']:
    print(student['email'])