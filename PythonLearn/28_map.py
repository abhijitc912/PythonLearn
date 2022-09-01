def sqr(num):
    return num*num

# Method 1
l1 = [1,10,100]
l2 = []
for item in l1:
    l2.append(sqr(item))
print ("Square of list using method 1:\n", l2)

# Method 2
print ("Square of list using method 2:\n", list(map(sqr,l1)))
