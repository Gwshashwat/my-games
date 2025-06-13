"""
Simulate deposit, withdraw, and balance check.

Use a PIN for access.

Use loops and basic file I/O for persistent balance (optional).
"""
import os

# Constants
BASE_PATH = "C:\\Users\\DELL\\OneDrive\\Desktop\\my games\\games\\project based\\💻 Console Utility Projects\\6. ATM Simulator 🏧"

def create_account():
    account = input("Enter your account name: ")
    pin = input("Set a 4-digit PIN: ")
    balance = input("Enter initial deposit: $")

    account_path = os.path.join(BASE_PATH, account)
    os.makedirs(account_path, exist_ok=True)

    with open(os.path.join(account_path, "name"), "w") as f:
        f.write(account)
    with open(os.path.join(account_path, "pin"), "w") as f:
        f.write(pin)
    with open(os.path.join(account_path, "balance"), "w") as f:
        f.write(balance)

    print(f"Account '{account}' created successfully!\n")

def check_pin(account):
    try:
        with open(os.path.join(BASE_PATH, account, "pin"), "r") as f:
            correct_pin = f.read()
    except FileNotFoundError:
        print("Account does not exist.\n")
        return False
    entered_pin = input("Enter your PIN: ")
    if entered_pin != correct_pin:
        print("Incorrect PIN.\n")
        return False
    return True

def deposit(account):
    account_path = os.path.join(BASE_PATH, account)
    with open(os.path.join(account_path, "balance"), "r") as f:
        balance = int(f.read())

    deposit_amt = int(input("Enter deposit amount: $"))
    balance += deposit_amt

    with open(os.path.join(account_path, "balance"), "w") as f:
        f.write(str(balance))
    print("Deposit successful!\n")

def withdraw(account):
    account_path = os.path.join(BASE_PATH, account)
    with open(os.path.join(account_path, "balance"), "r") as f:
        balance = int(f.read())

    while True:
        withdraw_amt = int(input("Enter withdrawal amount: $"))
        if withdraw_amt <= 0:
            print("Enter a valid positive amount.")
        elif withdraw_amt > balance:
            print(f"Insufficient funds. Your balance is ${balance}")
        else:
            balance -= withdraw_amt
            with open(os.path.join(account_path, "balance"), "w") as f:
                f.write(str(balance))
            print("Withdrawal successful!\n")
            break

def check_balance(account):
    account_path = os.path.join(BASE_PATH, account)
    with open(os.path.join(account_path, "balance"), "r") as f:
        balance = int(f.read())
    print(f"Your current balance is: ${balance}\n")

def change_pin(account):
    account_path = os.path.join(BASE_PATH, account)
    if not check_pin(account):
        return
    new_pin = input("Enter your new PIN: ")
    with open(os.path.join(account_path, "pin"), "w") as f:
        f.write(new_pin)
    print("PIN changed successfully!\n")

# Main Loop
while True:
    print("---------------WELCOME TO SHASHWAT ATM---------------")
    print("1. Access Account")
    print("2. Create Account")
    print("3. Exit")

    user_command = input("Enter your choice: ")
    
    if user_command == "3":
        print("Thank you for using Shashwat ATM!")
        break

    elif user_command == "2":
        create_account()

    elif user_command == "1":
        account = input("Enter your account name: ")
        if not check_pin(account):
            continue

        while True:
            print("\n--- ACCOUNT MENU ---")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Change PIN")
            print("5. Exit to Main Menu")

            option = input("Choose an option: ")

            if option == "1":
                check_balance(account)
            elif option == "2":
                withdraw(account)
            elif option == "3":
                deposit(account)
            elif option == "4":
                change_pin(account)
            elif option == "5":
                print("Logging out...\n")
                break
            else:
                print("Invalid option.\n")
