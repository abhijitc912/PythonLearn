def greet(name):
    print (f'{name}, you are great!')
print (f'Value of __name__ is: {__name__}')
if __name__ == "__main__":
    n = input('Enter name: ')
    greet(n)
