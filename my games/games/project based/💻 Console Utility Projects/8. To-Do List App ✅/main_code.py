"""
Add, remove, mark complete tasks.

Display tasks in a list.

Optional: Save/load from a file.

"""
import os

while True:
    choice = int(input("1. CHECK TASKS\n2. ADD TASK\n3. MARK COMPLETE ON A TASK\n4. EXIT\n5. CLEAR\n\tEnter your choice : "))
    if choice == 1:
        with open("task.txt","r") as f :
            i = 1
            lines = f.read()
            l = lines.split("\n")
            l.pop()
            for task in l:
                print(f"{i}. {task.capitalize()}")
                i += 1
        i = 1

    elif choice == 2:
        while True:
            task = input("Enter your task (q to exit) : ")
            if task == "q" :
                break
            with open("task.txt", "a") as f :
                f.write(task + "\n")
    
    elif choice == 3:
        with open("task.txt","r") as f :
            i = 1
            lines = f.read()
            l = lines.split("\n")
            l.pop()
            for task in l:
                print(f"{i}. {task.capitalize()}")
                i += 1
        i = 1
        while True:
            do = int(input("Enter completed task (-1 to exit) : "))
            if do == -1 :
                break
            else :
                a = l[do-1]
                l[do-1] = a + " (Completed)"
                tasks = ""
                for task in l:
                    tasks += task + "\n"
                with open("task.txt" , "w") as f :
                    f.write(str(tasks))
    
    elif choice == 4 :
        break

    elif choice == 5 :
        with open("task.txt" , "w") as f :
            f.write("")