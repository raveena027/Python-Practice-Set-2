'''Question 8: Email Validator 
Develop a Python function that validates whether a given string is a valid email address or not.'''


import re

def validate(email):

    if(re.fullmatch(regex, email)):
        print("Valid Email address")

    else:
        print("Invalid Emailaddress")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email = input("Enter your email: ")

validate(email)
