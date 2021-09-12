#Let's play Bulls And Cows
#Computer generates a 4 digit number. All digits are different.
#You try and guess the number exactly.
#Get the number AND placement exactly right = Bull
#Get a number correct but the place wrong = Cow
#A Bull is not counted as a Cow. No overlap.
#Computer:  2475 
#Guess:     1572    =  1 Bull, 2 Cows

import random
from time import sleep
cows = 0
bulls = 0
user_as_list = [] #Store converted input as ints in a separate list
bull_index = [] #If a guess is a bull, I'm storing it in here!
win = False

#Generating the number:
print("Welcome to Bulls and Cows! \nThe computer is about to randomly choose a 4 digit number, see if you can guess it!")
print("Note: There will be no repeat numbers in the secret number.")
secret_number = random.sample(range(9), 4)
print("\nOK, a secret number has been chosen.")

while win == False:
    bulls = 0
    cows = 0
    bull_index = []
    user_as_list = []

    user_guess = input("Input a 4 digit number; no repeat numbers: ").strip()
    try:
        for digit in user_guess:    #Making your guess easier to work with
            if len(user_guess) == 4:
                user_as_list.append(int(digit))

        for index, number in enumerate(secret_number):
            if user_as_list[index] == number:
                bulls += 1
                bull_index.append(number)
            else:
                pass

        for digit in user_as_list:
            if digit in bull_index:
                pass
            else:
                if digit in secret_number:
                    cows += 1
        
        print(f"Bulls: {bulls} Cows: {cows} ")
        if bulls == 4:
            print(f"You got it! The number was {user_guess} \nThanks for playing :)")
            sleep(3)
            win = True

    except IndexError:
        print("\nInvalid input: Please ensure you're inputting only 4 numbers.\n")
    except ValueError:
        print("\nInvalid input: Please ensure you're not using letters or special characters.\n")
