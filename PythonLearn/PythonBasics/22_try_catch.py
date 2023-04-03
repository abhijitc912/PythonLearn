while (True):
    print ('Press q to exit')
    a = input('Enter a number: ')
    if a == 'q':
        break
    try:
        print ('Trying...')
        a = int(a)
        if a>10:
            print ('Number greater than 10')
        elif a==10:
            print ('Number equal to 10')
        else:
            print ('Number less than 10')
    except Exception as e:
        print(f'Input resulted in error {e}')
        
print ('Bye!')
#################################################################################################################

try:
    a = int(input('Enter a number for division: '))
    d = 500/a
    print (d)
    
except ValueError as e:
    print ('Please enter a number')
except ZeroDivisionError as e:
    print ('Please enter a number othen than 0')
    exit()                                        # Even after exit we reach finally

else:
    print('Good job!')
finally:
    print ('Thanks!')

print('Bravo! You did not enter 0')               # If 0 is entered program exits and this line is not reached.
###################################################################################################################

def readFile(filename):
    try:
        with (open(filename,'r') as f):
            print (f.read())
    except FileNotFoundError:
        print (f'File {filename} not found')
                                                        # Leave 2 blank lines after defining a function
   
readFile('one.txt')
readFile('two.txt')
readFile('three.txt')                         #This file is not there but program will not exit throwing an error.
