### Imports ###
import random
from hangManPicture import *
import time

file = open("WordList.txt", "r")
randomWord = random.choice(file.readlines())
lives = 6
shieldWord = ""

for i in range(len(randomWord)):
    shieldWord += "*"

print(randomWord), print(shieldWord)

print(hangManPictureStart)
print("Welcome to Hangman!")
print("The word has", len(randomWord) - 1, "letters")
print(randomWord)

while True:
    print("-----------------------------------------------------")
    print(shieldWord)
    print("Guess a letter:")
    guess = input()
    if guess in randomWord:
        print("Correct!")
        for i in range(len(randomWord)):
            if randomWord[i] == guess:
                shieldWord = shieldWord[:i] + guess + shieldWord[i + 1:]
        print(shieldWord)
    
    else:
        print("Wrong! That letter is not in the word!")
        print("You lose a life")
        lives -= 1

        if lives == 0:
            print(hangManPictureSeventh)
            print("You lose!")
            print("The word was", randomWord)
            break
        
        elif lives == 1:
            print(hangManPictureSixth)
            print("You have", lives, "life left")
            
        elif lives == 2:
            print(hangManPictureFifth)
            print("You have", lives, "life left")
        
        elif lives == 3:
            print(hangManPictureFourth)
            print("You have", lives, "life left")
        
        elif lives == 4:
            print(hangManPictureThird)
            print("You have", lives, "life left")
        
        elif lives == 5:
            print(hangManPictureSecond)
            print("You have", lives, "life left")