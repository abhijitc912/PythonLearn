m1 = int(input("Enter marks for student 1: "))
m2 = int(input("Enter marks for student 2: "))
m3 = int(input("Enter marks for student 3: "))
m4 = int(input("Enter marks for student 4: "))
m5 = int(input("Enter marks for student 5: "))

### HANDY TRICK TO TYPE SIMILAR LINES VERY FAST IN VS CODE ###
# To create above lines just type the first line.
# Copy paste it 5 times.
# Put curson next to m1 of second line and press "Alt" key. 
# Now put second curson after 1 in the second line
# Now we have two cursors with the cursor blinking after m1 in second line
# Just use backspace to now delete 1 from m1 and make it m2 
# You will notice it changes student 1 to student 2 in the same line
# Press "Esc" key and then "Down arrow" key to go to next line
# Repeat process to edit all the lines.

m_list = [m1,m2,m3,m4,m5]
m_list.sort()
print (m_list)
