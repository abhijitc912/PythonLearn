text = input("Enter your message:\n")
spam = False

if ("make money" in text):
    spam = True
elif ("subscribe" in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("click here" in text):
    spam = True
else:
    spam = False

if (spam):
    print ("This message is spam")
else:
    print ("This message is not a spam")
