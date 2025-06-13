"""
User inputs desired length.

Generates a random strong password using letters, digits, symbols.

"""
import random

password = ""
while True :
    password_len = int(input("Enter the length of password : "))
    if 7 > password_len or password_len > 21:
        print("Password lenght must contain 8-20 characters.")

    else:
        for i in range(1,password_len+1):
            appeard = random.choice(
                [str(random.randint(0,9)),
                random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]),
                random.choice(["!","@","#","$","%","^","&","*"])])
            password += appeard
        print(f"Password = {password}")