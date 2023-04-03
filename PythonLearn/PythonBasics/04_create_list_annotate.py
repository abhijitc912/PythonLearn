m1 = int(input("Enter marks for student 1: "))
m2 = int(input("Enter marks for student 2: "))
m3 = int(input("Enter marks for student 3: "))
m4 = int(input("Enter marks for student 4: "))
m5 = int(input("Enter marks for student 5: "))

### HANDY TRICK TO TYPE SIMILAR LINES VERY FAST IN VS CODE ###
# To create above lines just type the first line.
# Copy paste it 5 times.
# Put cursor next to m1 of second line and press "Alt" key. 
# Now put second curson after 1 in the second line
# Now we have two cursors with the cursor blinking after m1 in second line
# Just use backspace to now delete 1 from m1 and make it m2 
# You will notice it changes student 1 to student 2 in the same line
# Press "Esc" key and then "Down arrow" key to go to next line
# Repeat process to edit all the lines.

m_list = [m1,m2,m3,m4,m5]
m_list.sort()
print (m_list)

a,b,c,d,e = m_list         #Unpack a list
print (a,b,c,d,e)

##########################################################################################################
print ("*"*80)
def is_palindrome(string):
    return string[::-1].casefold()==string.casefold()


def palindromeSentence(sentence):
    """
    Check if a sentence is a palindrome.
 
    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
 
    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string=""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return is_palindrome(string)  #Calling function within a function


word = input("Please enter the sentence to check if it is a palindrome: ") #Example: Radar, Level, Noon, Was it a car or a cat I saw?
if palindromeSentence(word):
    print(f"{word} is a palindrome sentence.")
else:
    print(f"{word} is not a palindrome sentence.")    

