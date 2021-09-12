#Number Guessing game (1 player)
print("We've just thought of a number between 1 and 9, guess it!!")
from random import randint
guesses = 5
flag = True
com = randint(1,9)

while flag == True:
    if guesses == 0:
        print("Game Over")
        break
    usern = int(input(f"Guesses left: {guesses} \nYour guess: "))
    if usern > 9:
        print("Please choose a number between 1 and 9!")
        continue
    elif usern == com:
        print(f"That's right, the number {com}! Well guessed!")
        flag = False
    else:
        guesses -= 1
        if guesses != 0:
            print(f"Nope, sorry; Try again")
        else:
            print(f"Sorry, the computer chose {com}, too bad!")