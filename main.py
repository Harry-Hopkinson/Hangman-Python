### Imports ###
import random
from hangManPicture import *
import time

### Variables ###
file = open("WordList.txt", "r")
randomWord = random.choice(file.readlines())
lives = 6
shieldWord = ""
tries = 0

for i in range(len(randomWord) - 1):
    shieldWord += "*"

print(randomWord), print(shieldWord)

for line in hangManPictureStart:
    print(line)

print("Welcome to Hangman!")
print("The word has", len(randomWord) - 1, "letters")
print(randomWord)

while True:
    print("-----------------------------------------------------")
    print(shieldWord)
    print("Guess a letter:")
    guess = input()
    tries += 1

    if "*" not in shieldWord:
        print("You win!")
        print("The word was", randomWord)
        print("It took you", tries, "tries")
        break

    elif guess in randomWord:
        print("Correct!")
        tries += 1
        for i in range(len(randomWord)):
            if randomWord[i] == guess:
                shieldWord = shieldWord[:i] + guess + shieldWord[i + 1:]
        print(shieldWord)
    
    elif guess in shieldWord:
        print("You already guessed that letter!")
        tries += 1
        print(shieldWord)

    
    ### If the letter is not in the word ###   
    else:
        print("Wrong! That letter is not in the word!")
        print("You lose a life")
        lives -= 1
        tries += 1

        if lives == 0:
            for line in hangManPictureSeventh:
                print(line)
            print("You lose!")
            print("The word was", randomWord)
            break
        
        elif lives == 1:
            for line in hangManPictureSixth:
                print(line)
            print("You have", lives, "life left")
            
        elif lives == 2:
            for line in hangManPictureFifth:
                print(line)
            print("You have", lives, "life left")
        
        elif lives == 3:
            for line in hangManPictureFourth:
                print(line)
            print("You have", lives, "life left")
        
        elif lives == 4:
            for line in hangManPictureThird:
                print(line)
            print("You have", lives, "life left")
        
        elif lives == 5:
            for line in hangManPictureSecond:
                print(line)
            print("You have", lives, "life left")

print("Thanks for playing!")
time.sleep(2)