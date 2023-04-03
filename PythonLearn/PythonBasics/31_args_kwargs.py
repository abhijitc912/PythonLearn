# Illustrate *args for a variable number of arguments
print("Illustrate *args for a variable number of arguments")

def argsOnly(*argv):
    print("Values in *argv: ", *argv, sep=";" )   # Here *argv is unpacked tuple
    print("Values in argv: ", argv, sep=";" )     # So that makes argv a packed tuple
                                                  # Now we can use our tuple to print values using a loop
                                                  # This way we are able to send multiple values to a function that we 
                                                  # can iterate through a loop   
    for arg in argv:                              
        print(arg)

argsOnly('Hello', 'Welcome', 'to', 'The Jungle')


# Illustrate *args with a first extra argument
print("\nIllustrate *args with a first extra argument")

def moreargs(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
 
moreargs('Hello', 'Welcome', 'to', 'The Jungle')


# Illustrate *kwargs for a variable number of keyword arguments
print("\nIllustrate *kwargs for a variable number of keyword arguments")

def kwargsOnly(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 

kwargsOnly(first='Welcome', mid='to', last='The Jungle')


# Illustrate  **kwargs for a variable number of keyword arguments with one extra argument
print ("\nIllustrate  **kwargs for a variable number of keyword arguments with one extra argument.")

def moreKwargs(arg1, **kwargs):
    print(arg1)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        
moreKwargs("Hi", first='Welcome', mid='to', last='The Jungle')


# Using both *args and **kwargs to call a function
print("\nUsing both *args and **kwargs to call a function")

def bothArgsKwargs(arg1, arg2, arg3):
    print("First argument:", arg1)
    print("Second argument:", arg2)
    print("Third argument:", arg3)

# Use *args or **kwargs to pass arguments to this function :
print ("*args")
args = ("Welcome", "to", "The Jungle")
bothArgsKwargs(*args)

print ("**kwargs")
kwargs = {"arg1": "Welcome", "arg2": "to", "arg3": "The Jungle"}
bothArgsKwargs(**kwargs)

print()
print("*"*80)
# Using *args and **kwargs to set values of object
print("\nUsing *args and **kwargs to set values of object")
# *args receives arguments as an array
# **kwargs receives arguments as a dictionary
class car(): #defining car class
    def __init__(self,*args): #args receives unlimited no. of arguments as an array
        self.speed = args[0] #access args index like array does
        self.color = args[1]
                 
#creating objects of car class
         
audi=car(100,'Red')
bmw=car(200,'Black')
    
print("Color of Audi: ",audi.color)
print("Speed of BMW: ",bmw.speed)


class student(): #defining car class
    def __init__(self,**kwargs): #args receives unlimited no. of arguments as an array
        self.name = kwargs['n'] #access args index like array does
        self.age = kwargs['a']
                 
#creating objects of car class
         
student1=student(a=30,n='Abhi')
student2=student(a=20,n='Subha')
    
print("Name of student1: ",student1.name)
print("Age of student 2: ",student2.age)

print()
print("*"*80)
def func(p1,p2,*args,k,**kwargs):
    print(f"Positional or keyword argument: {p1}, {p2}")
    print(f"Var-positional (*args):         {args}")
    print(f"Keyword:                        {k}")
    print(f"Var-keyword:                    {kwargs}")


func(1,2,3,4,5,k=6,key1=7,key2=8)                # Note that positional argument cannot appear after keyword arguments 
