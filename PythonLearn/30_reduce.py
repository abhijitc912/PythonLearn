from functools import reduce


def sum(a, b): return a+b

l = [1, 2, 3, 4]

val = reduce (sum,l)
print (val)

# Rolling computation to a sequential pair of elements
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10

