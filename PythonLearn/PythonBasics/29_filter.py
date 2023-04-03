def g5(num):
    if num > 5:
        return True
    else:
        return False
                                                # Leave 2 blank lines after defining a function
   
l6 = lambda num: num<6

myList = [0, 1, 2, 3, 4, 6, 7, 8, 9]

print (list(filter(g5, myList)))
print (list(filter(l6, myList)))
