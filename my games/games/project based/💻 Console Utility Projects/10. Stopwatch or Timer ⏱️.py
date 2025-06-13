"""
Start, stop, and reset time.

Use time module.

Optional: Countdown timer.

"""
import time

start_time = 0
run_time = 0

running = False 
while True:
    op = input("Enter s to start timer,e to end ,r to reset, q to quite : ")
    if op == "s" :
        if not running :
            start_time = time.time()
            print("Time started.")
            running = True
        else :
            print("Time is already running.")
    elif op == "e":
        if running :
            run_time = time.time() - start_time
            print(f"Time stopped. {round(run_time,2)}")

    elif op == "q" :
        quit()
        break
    elif op == "r" :
        if running :
            start_time = time.time()
            print("timer reseted.")
        else :
            print("Start the timer to reset.")

# 80% me 20 % gpt