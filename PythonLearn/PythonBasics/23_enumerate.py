#Enumerate is useful when you need the index positions while iterating over a sequence
#Enumerate creates the index numbers for us. It iterates over an iterable and generates an index number for each number it
#finds starting at zero. It then returns tuples returning the index and values for each iterable
list = ['Abhi', 500, True]

print("\nList items in a list using for loop:")
index=1                                   # We need to define a variable index which we will use to show the counter
for n in list:
    print (index,n)
    index += 1

print('\nList items in a list using Enumerate:')

for counter, item in enumerate(list):     # No need to first define any variable to be used as the counter
    print(counter+1,item)
