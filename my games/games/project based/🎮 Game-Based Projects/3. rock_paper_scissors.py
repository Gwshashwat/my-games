"""
3. Rock Paper Scissors ✊✋✌️
User vs Computer.

Decide winner using simple if-else.

Track score across rounds.
"""
import random
print('----------Rock Paper Scissors ✊✋✌️----------')
d ={
    "r" : 1,
    "p" : 2, 
    "s" : 3
    }
d_reverse = {
    1 : "ROCK ✊",
    2 : "PAPER ✋", 
    3 : "SCISSORS ✌️"
    }

score = 0
score_computer = 0

while True :
    print('USE :\nR FOR ROCK ✊\nP FOR PAPER ✋\nS FOR SCISSORS ✌️')
    user = input("Enter your choice (Enter q to exit.) : ").lower()
    if user == "q":
        quit()
        break
    else:
        computer = random.randint(1,3)
        try:
            user_choice = d[user]
            diff = user_choice - computer
            if user_choice == computer :
                print(f"\n\nDRAW !!!\n\n")
            elif diff == 1 or diff == -2 :
                print("\n\nYOU WON !!!\n\n")
                score += 1
            elif diff == -1 or diff == 2 :
                print("\n\nYOU LOSE !!!\n\n")
                score_computer += 1
            
            print(f"COMPUTER CHOSE : {d_reverse[computer]}\nYOU CHOSE : {d_reverse[user_choice]}\nYOUR SCORE : {score}\nCOMPUTER SCORE : {score_computer} \n\n")

        except KeyError:
            print("CONSENTRATE ON YOUR TYPING .")