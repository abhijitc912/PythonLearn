###### Format method is an old way of printing variables in a string . Now we use f string instead of format method ######

student1 = input('Enter name of Student 1: ')
student2 = input('Enter name of Student 2: ')
student3 = input('Enter name of Student 3: ')

text1 = 'This is {}. His friends are {} and {}'.format(student1, student2, student3)
text2 = 'This is {1}. His friends are {0} and {2}'.format(student1, student2, student3)

print (text1)
print (text2)
