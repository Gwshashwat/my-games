"""
User guesses letters of a hidden word.

Limit number of wrong attempts.

Show correct guesses and blanks.
"""
import random

hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

#Word bank of animals
words = ('''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra ''').split(" ")

word = random.choice(words)

i = 0
l = []
print("_"*len(word))

while True :
    word2 = word
    
    letter = input("Enter your guess : ")
    if letter in word :
        for letterq in word :
            
            if letterq == letter :
                l.append(letter)
            else :
                if letterq in l :
                    pass
                
                else :
                    word2 = word2.replace(letterq,"_")
    else:
        for letterq in word :
    
            if letterq in l :
                pass
            else :
                word2 = word2.replace(letterq,"_")
        i += 1
    print(word2)
        
    if i == 6 :
        print(f"You lost !!\nWord was : {word}")
        break
    
    print(hangmanpics[i])