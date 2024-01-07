'''Question 4: User Authentication 
Develop a Python program that simulates user authentication. Ask the user to enter a username and password, and validate them against predefined values.  '''


def login():  
    username = input("Enter your username: ")  
    password = input("Enter your password: ")  
  
    if username in users and users[username] == password:  
        print("Login successful!")  
    else:  
        print("Invalid username or password. Please try again.")  
  
users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}
login()
