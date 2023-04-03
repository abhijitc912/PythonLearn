def game():
    return 5000
                                                # Leave 2 blank lines after defining a function
   
score = game()

with open('13_hiscore.txt') as f:               # we use with to open a file as we will not need to close the file later
                                                # If we use open function with a for loop instead to print all the lines then
                                                # we will have to explicitly close the file as well
    hiscore= f.read()
    
if hiscore == '':
    with open('13_hiscore.txt','w') as f:
        f.write(str(score))  
         
elif score>int(hiscore):
    with open('13_hiscore.txt','w') as f:
        f.write(str(score))
