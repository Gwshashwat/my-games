"""
Toss Simulator (Heads or Tails) 🪙
Simulate a coin toss.

Ask user to choose "heads" or "tails".

Track wins/losses.
"""
import random
print("------------------------Toss Simulator------------------------\n\n")
print("USE :\nT FOR TAILS\nH FOR HEADS\n")

wins = 0
losses = 0
d = {"T" : "TAILS","H" : "HEADS"}
runs = 0

while True :
    user = input("Enter you choice (Enter q to quit.) : ").upper()
    if user == "Q" :
        if runs == 0 :
            print("AT LEAST TRY MY GAME.")
        quit()
        break
    else:
        if user == "T" or user == "H":
            runs += 1
            l = ["T","H"]
            appear = random.choice(l)
            if user == appear:
                print("YOU WON !\n")
                wins += 1
            else:
                print("YOU LOSE !\n")
                losses += 1
        else:
            print("GOOD PRANK!!")
        print(f"{d[appear]} Appeared.\n\nWINS = {wins}\nLOSSES = {losses}\n")