"""
Dice Rolling Simulator 🎲
Simulate a 6-sided dice roll.
"""
from random import randint
print("-------------DICE ROLLING SIMULATOR-------------")

l = {}

run = 0 
while True:
    if run == 0 :
        user = input("Do you want to spin 🎲 ? : ").lower()
        run += 1
    else :
        user = input("Do you want to spin again 🎲 ? : ").lower()
    if user == "no":
        break
    elif user == "yes":
        dice = randint(1,6)
        print(dice)
        if dice in l:
            l[dice] += 1
        else:
            l[dice] = 1
        print(l)

    else :
        print("TRY USING YES OR NO.")