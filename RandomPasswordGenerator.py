'''Question 7: Random Password Generator 
Write a Python function that generates a random password of a specified length, combining letters, numbers, and symbols.'''

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
specialchars = "!@#$%^&*()_-=+<>/?\."

def random_password(length=12):
    string = lower + upper + numbers + specialchars
    length = 12
    password = "".join(random.choice(string)for _ in range(length))

    print("Your password is: ",password)

random_password()
