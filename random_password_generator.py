#Random password generator in range 10
#Concept: using loop and import using forceful list comprehension

import random
import string 
user_input = int(input(f"Enter the size of charecters required in password (max 10): "))

if 0 < user_input <= 10:
    char = string.ascii_letters + string.digits + "!@#$%^&*_?"
    password = ["".join(random.sample(char,user_input)) for _ in range (1)]
    print(f"Generated password is:", password)
else:
    print("Invalid character lenght! Length must be within 0 to 10.")