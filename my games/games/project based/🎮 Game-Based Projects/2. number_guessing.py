"""
Number Guessing Game 🔢
"""
from random import randint
print('-----------------INSANE NUMBER GUSSING GAME-----------------')

run = 0
tries = 0 
while True:
    if run == 0:
        user = input("Do you want to play (Y/N) ? : ").lower()
    else : 
        user = input("Do you want to play again (Y/N) ? : ").lower()
    if user == "n":
        if run == 0:
            print("AT LEAST TRY MY GAME!")
        else:
            print("Thanks for playing.")
        break
    elif user == "y":
        run += 1
        print("EASY = 1\nNORMAL = 2\nHARD = 3\nEXTREME = 4\nINSANE = 5\nNO LIFE = 6")
        d = {1 : "EASY",2 : "NORMAL",3 :"HARD",4 : "EXTREME",5 : "INSANE",6 : "NO LIFE"}
        while True:
            difficulty = int(input("Enter the difficulty : "))

            if  0 < difficulty < 7 :
                number = randint(1,10**(1+difficulty))
                break
            else:
                print("GOOD PRANK!!")
        print(f'-----------------------DIFFICULTY - {d[difficulty]}-----------------------')

        while True:
            try:
                tries += 1
                guess = int(input(f"Enter your guess in between {1} - {10**(1+difficulty)} 🔢 : "))
                if guess == number :
    
                    print(f"YOU WON !\nNUMBER = {number}\nNUMBER OF GUESSES = {tries}")
                    break
                elif guess > number:
                    print("Too high.")
    
                elif guess < number:
                    print("Too low")
    
            except ValueError:
                print("ONLY INTEGERS ARE ALLOWED")
                tries -= 1
            except KeyboardInterrupt :
                print("BE CAREFULL.")
                tries -= 1
    else :
        print("TRY USING Y OR N.")
