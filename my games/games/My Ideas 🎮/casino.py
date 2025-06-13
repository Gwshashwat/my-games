import random
print("---------WELCOME TO CASINO SPINN GAME---------")
def deposite():
    while True:
        try:
            deposite = int(input("Enter your deposite : $"))
            print(f"Deposite = ${deposite}")
            break
        except Exception:
            print("Something went wrong.")
    return deposite

def bet(deposite):
    while True:
        try :
            print(f"Avalable balance = ${deposite}")
            bet = int(input("Enter your betting ammount : $"))
            if bet > deposite:
                print(f"You only deposited ${deposite}.\ndeposite more dollar to bet ${bet}")
            else:
                deposite -= bet
                print(f"Balance = ${deposite}\nBet = ${bet}")
                break

        except ValueError:
            print("Please put a number.")
        except Exception :
            print("Something went wrong .")
    return deposite , bet


def colour():
    print("-----------------------PUT A COLOUR-----------------------")
    print("AVALABLE COLOURS\nRED\nBLACK")
    
    while True:
        colour = input("Enter your colour : ").lower()
        if colour == "black" or colour == "red":
            break
        elif colour == "white":
            print("white is reserved for house.\nTry again.")

    return colour

def game(deposite,bet,colour):
    decider = random.randint(0,13)

    if decider == 7 :
        present_colour = "white"
    elif decider > 7:
        present_colour = "red"
    elif decider < 7:
        present_colour = "black"
    print(f"Colour appeared = {present_colour}")

    if colour == present_colour:
        print(f"YOU WON ${bet*2}")
        deposite += bet*2
    elif present_colour == "white":
        print("HOUSE WON !\nYOU LOST!")
    
    else:
        print(f"YOU LOST !")

    print(f"Balance = ${deposite}")
    return deposite


def widraw(deposite):
    
    while True:
        if deposite > 0:
            print(f"Avalable balance = ${deposite}")
            withdraw = int(input("Enter the ammount you want to Withdraw :$ "))
            if withdraw > deposite or withdraw < 0 :
                print("Please be serious.")
            else:    
                deposite -= withdraw
                print(f"Withdraw = ${withdraw}\nDeposite = ${deposite}")
                break    
    return deposite

Deposite = None
while True:
    inputt = input("Do you want to play ? ").lower()
    if inputt == "yes" :
        if Deposite == None or Deposite == 0:
            print("Enter some money to play.")
            Deposite = deposite()
            d_allow = "no"
        d_allow = input("Do you want to Deposite more ? ").lower()
        if d_allow == "yes" :
            Deposite += deposite()
        Deposite, Bet = bet(Deposite)

        Colour = colour()
        Deposite = game(Deposite, Bet, Colour)

        if Deposite > 0:
            witdraw_permission = input("Do you want to Witdraw ? ").lower()
            if witdraw_permission == "yes":
                Deposite = widraw(Deposite)

    elif inputt == "no":
        break