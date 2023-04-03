email = input("Enter Your Email: ").strip()
'''The Strip() method in Python removes or truncates the given characters from the beginning and the end of the original string. 
The default behavior of the strip() method is to remove the whitespace from the beginning and at the end of the string.'''
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)
print(email)
