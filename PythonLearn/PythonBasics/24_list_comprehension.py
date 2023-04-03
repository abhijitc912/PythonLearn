list = [1,2,3,4,5,6,7,8,9,100,150,201,203]

print('Printing even numbers in list:')
e=[]
for item in list:
    if item%2 == 0:
        e.append(item)
print(e)

print('\nPrinting odd numbers in list:')
o = [i for i in list if i%2!=0]
print(o)
