"""
Turn-based play on a 3x3 board.

Detect win/draw conditions.

Display board after every move.

MAIN GOAL - NO GPT!!!!
"""
import random

moves = 1
player_1_wins = 0
player_2_wins = 0
robot_wins = 0

sq_1 , sq_2 , sq_3 = 1,2,3
sq_4 , sq_5 , sq_6 = 4,5,6
sq_7 , sq_8 , sq_9 = 7,8,9

def print_board():
    print(f"{sq_1}|{sq_2}|{sq_3}\n_____\n{sq_4}|{sq_5}|{sq_6}\n_____\n{sq_7}|{sq_8}|{sq_9}\n")

def win() :
    global board, sq_1 ,sq_2 ,sq_3 ,sq_4 ,sq_5 ,sq_6 ,sq_7 ,sq_8 ,sq_9,moves,move,player_1_wins,player_2_wins,robot_wins
    if sq_1 == sq_2 == sq_3 == "X" or sq_1 == sq_4 == sq_7 == "X" or sq_4 == sq_5 == sq_6 == "X" or sq_1 == sq_5 == sq_9 == "X" or sq_2 == sq_5 == sq_8 == "X" or sq_7 == sq_5 == sq_3 == "X" or sq_9 == sq_6 == sq_3 == "X" or sq_7 == sq_8 == sq_9 == "X":
        player_1_wins += 1
        print(f"\n\nPLAYER 1 WON!\n\n")
        print_board()
        print(f"SCORE :\nPLAYER 1 = {player_1_wins}\nPLAYER 2 = {player_2_wins}")

        sq_1 , sq_2 , sq_3 = 1,2,3
        sq_4 , sq_5 , sq_6 = 4,5,6
        sq_7 , sq_8 , sq_9 = 7,8,9
        moves = 1
                
    elif sq_1 == sq_2 == sq_3 == "O" or sq_1 == sq_4 == sq_7 == "O" or sq_4 == sq_5 == sq_6 == "O" or sq_1 == sq_5 == sq_9 == "O" or sq_2 == sq_5 == sq_8 == "O" or sq_7 == sq_5 == sq_3 == "O" or sq_9 == sq_6 == sq_3 == "O" or sq_7 == sq_8 == sq_9 == "O":
        player_2_wins += 1
        print(f"\n\nPLAYER 2 WON!\n\n")
        print_board()
        print(f"SCORE :\nPLAYER 1 = {player_1_wins}\nPLAYER 2 = {player_2_wins}")

        sq_1 , sq_2 , sq_3 = 1,2,3
        sq_4 , sq_5 , sq_6 = 4,5,6
        sq_7 , sq_8 , sq_9 = 7,8,9
        moves = 1
                
    elif moves == 10 :
        print(f"\n\nDRAW !!\n\n")
        print_board()
        print(f"SCORE :\nPLAYER 1 = {player_1_wins}\nPLAYER 2 = {player_2_wins}")

        sq_1 , sq_2 , sq_3 = 1,2,3
        sq_4 , sq_5 , sq_6 = 4,5,6
        sq_7 , sq_8 , sq_9 = 7,8,9
        moves = 1
        
def reset_board():
    global sq_1, sq_2, sq_3, sq_4, sq_5, sq_6, sq_7, sq_8, sq_9, moves
    sq_1, sq_2, sq_3 = 1, 2, 3
    sq_4, sq_5, sq_6 = 4, 5, 6
    sq_7, sq_8, sq_9 = 7, 8, 9
    moves = 1

def make_move(pos, symbol):
    global sq_1 ,sq_2 ,sq_3 ,sq_4 ,sq_5 ,sq_6 ,sq_7 ,sq_8 ,sq_9,moves
    if pos == 1 and sq_1 == 1:
        sq_1 = symbol
        moves += 1
    elif pos == 2 and sq_2 == 2:
        sq_2 = symbol
        moves += 1
    elif pos == 3 and sq_3 == 3:
        sq_3 = symbol
        moves += 1
    elif pos == 4 and sq_4 == 4:
        sq_4 = symbol
        moves += 1
    elif pos == 5 and sq_5 == 5:
        sq_5 = symbol
        moves += 1
    elif pos == 6 and sq_6 == 6:
        sq_6 = symbol
        moves += 1
    elif pos == 7 and sq_7 == 7:
        sq_7 = symbol
        moves += 1
    elif pos == 8 and sq_8 == 8:
        sq_8 = symbol
        moves += 1
    elif pos == 9 and sq_9 == 9:
        sq_9 = symbol
        moves += 1


while True:

    print("-------------------- SHASHWAT TIC-TAC-TOE --------------------")

    com = int(input("ENTER :\n1. 1 PLAYER\n2. 2 PLAYER\n3. QUIT\nENTER YOUR CHOICE : "))

    if com == 2 :

        print_board()
        
        player_1_wins = 0
        player_2_wins = 0
        robot_wins = 0
        while True:
            
            player = moves % 2
            if player == 1 :
                move = input("Player 1 (q to quite) : ")
                if move == "q" :
                    break
                else :
                    try :
                        make_move(int(move),"X")
                    except ValueError :
                        print("Invalid move.")

            else:
                move = int(input("Player 2 : "))
                make_move(move,"O")
            
            win()
            
            print_board()

    elif com == 1 :

        print_board()
        
        player_1_wins = 0
        player_2_wins = 0
        robot_wins = 0
        while True:
            
            player = moves % 2
            if player == 1 :
                move = input("Player 1 (q to quite) : ")
                if move == "q" :
                    break
                else :
                    try :
                        make_move(int(move),"X")
                    except ValueError :
                        print("Invalid move.")
            else:
                avalaible_moves = []
                if sq_1 == 1 :
                    avalaible_moves.append(sq_1)
                if sq_2 == 2 :
                    avalaible_moves.append(sq_2)
                if sq_3 == 3 :
                    avalaible_moves.append(sq_3)
                if sq_4 == 4 :
                    avalaible_moves.append(sq_4)
                if sq_5 == 5 :
                    avalaible_moves.append(sq_5)
                if sq_6 == 6 :
                    avalaible_moves.append(sq_6)
                if sq_7 == 7 :
                    avalaible_moves.append(sq_7)
                if sq_8 == 8 :
                    avalaible_moves.append(sq_8)
                if sq_9 == 9 :
                    avalaible_moves.append(sq_9)                
                
                print("Robot is thinking ...")
                move = random.choice(avalaible_moves)
                make_move(move,"O")
                
            board =f"{sq_1}|{sq_2}|{sq_3}\n_____\n{sq_4}|{sq_5}|{sq_6}\n_____\n{sq_7}|{sq_8}|{sq_9}\n"

            win()               

            print_board() 
            
    elif com == 3 :
        break

    else :
        print("NICE TRY!!")
