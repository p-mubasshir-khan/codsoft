import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.") 
        # password is not generated if user gives length less than 8 
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

username = input("Enter your username: ") # user is prompted to enter a username
length = int(input("Enter the length of the password: ")) # user is prompted to enter a desired length of password
password = generate_password(length)
if password:
    print(f"Username: {username}") # username is printed which is given by user in the program
    print(f"Generated Password: {password}") # password is Generated successfully
