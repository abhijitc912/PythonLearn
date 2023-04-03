def sum_eo(n, t):
    #Following lines within ''' is called docstring       **Always try to document functions**
    """Sum even or odd numbers in range.

    Return the sum of even or odd natural numbers, in the range 1..n-1.

    :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of the even or odd numbers in the range.
            Returns -1 if `t` is not 'e' or 'o'.
    """
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


help(sum_eo)
x = sum_eo(11, 'o')
print(f"Sum = {x}")

print()
print("*"*80)

def fibonacci(n):
    '''Return the n th Fibonacci number for positive n'''
    if 0<=n<=1:
        return n
    n_minus1, n_minus2 = 1,0
    result = None
        
    for i in range (n-1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    
    return result


for i in range (20):
    print (i+1,fibonacci(i))

print()
print("x"*80)

def factorial(n: int) -> int:
    """Return n! (0! is 1)."""
    if n <= 1:
        return 1
 
    result = 2
    for x in range(3, n + 1):
        result *= x
 
    return result
 
 
for i in range(15):
    print(i+1, factorial(i))
    
print()
print("x"*80)

def factorial_recur(n: int) -> int:
    """
    Return n! (0! is 1).
 
    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.
    """
    if n <= 1:
        return 1
 
    return n * factorial_recur(n - 1)


for i in range(15):
    print(i+1, factorial_recur(i))
    
print()
print("x"*80)
numbers= (1,2,3,4,5)
print(numbers,sep=";")
print(*numbers)
print(*numbers,sep=";")
