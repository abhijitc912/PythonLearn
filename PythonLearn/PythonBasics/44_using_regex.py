import re

print("#"*80)
print()
print("Phone number check")
ptrn= "00"
phno= "0014860098"
if re.match(ptrn,phno):
    newpno=re.sub(ptrn,"+",phno,count=1)
    print(newpno)
else:
    print(phno)


print("#"*80)
print()
print("Four letter word check")
word =input("Enter four letter word: ")                   # Try with milk, mine, mile
if re.match("^m..e$",word):
    print("Match")
else:
    print("No match")
    

print("#"*80)
print()
print("Phone number validity check")    
def isvalid(phno):
    #strphno = str(phno)
    if len(phno)!=8:
        return "Invalid"
    else:
        return True

pn = r"81239870"
check = isvalid(pn)
print(check)


print("#"*80)
print()
print("Four character code check") 
# For a four character input, check if first two symbols of the input is uppercase characters 
# and last two symbols of the input are numbers
Id = input("Four character code: ")

pattern = r"^[A-Z][A-Z][0-9][0-9]$"

if re.search(pattern,Id):
    print ("Right format")
else:
    print("Wrong format")


print("#"*80)
print()
print("Password format check") 
# Check if the format of a password is valid. Password is valid if it has one uppercase and one numberic character

password = input("Enter password: ")

pattern1 = r"\w*[A-Z]\w*[0-9]\w*"
# To indicate a special sequence
# \d for any digits
# \w for any alphanumeric character
# \s for space

if re.search(pattern1,password):
    print (f"{password} is valid password")
else:
    print (f"{password} is invalid password")
    

print("#"*80)
print()
print("Vowel match")
# One or more repetations of a non-vowel followed by a vowel and followed by a non-vowel

vowelString = input("Enter your vowel string: ")

patternVowel = r"([^aeiou]+[aeiou]+[^aeiou])+"    # ^ means except, + means one or more repetations

if re.match(patternVowel,vowelString):
    print(f"{vowelString} is valid vowel string")
else:
    print(f"{vowelString} is invalid vowel string")


