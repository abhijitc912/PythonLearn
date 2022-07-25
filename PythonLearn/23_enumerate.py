list = ['Abhi', 500, True]


index=1                                   # We need to define a variable index which we will use to show the counter
for n in list:
    print (index,n)
    index += 1

print('\nList items using Enumerate:')

for counter, item in enumerate(list):     # No need to first define any variable to be used as the counter
    print(counter,item)
