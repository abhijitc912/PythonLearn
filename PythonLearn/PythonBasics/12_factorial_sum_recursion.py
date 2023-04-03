num = int(input('Enter number for factorial and sum of natural numbers: '))

def factorial_iter(x):
    n=1
    for i in range(x):
        n = n*(i+1)
    return n
                                                # Leave 2 blank lines after defining a function
   
fact_i=factorial_iter(num)
print (f'Factorial of {num} using interation is {fact_i}')

def factorial_recur(y):
    if y==0 or y==1:
        return 1
    return y*factorial_recur(y-1)
                                                # Leave 2 blank lines after defining a function
   
fact_r=factorial_recur(num)
print (f'Factorial of {num} using recursion is {fact_r}')

def sum_num(z):
    if z==0:
        return 0
    return z+sum_num(z-1)
                                                # Leave 2 blank lines after defining a function
   
sum=sum_num(num)
print (f'Sum of all natural numbers till {num} using recursion is {sum}')
