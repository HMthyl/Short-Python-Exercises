#Looping 2-player Rock-Paper-Scissors
import os
ok = False
again = "y"
def checkup(choice):
    if choice != "rock" and choice != "paper" and choice != "scissors":
        print("Looks like you made a typo; please enter again")
    else:
        return True

print("Welcome to Rock-Paper-Scissors! \nRock beats Scissors \nScissors beats Paper \nPaper beats Rock")
while again == "y":
    #Let's ensure everything goes smoothly for Player 1: 
    while ok == False:
        p1 = input("Player 1, Choose your fighter: ").lower().strip()
        if checkup(p1):
            ok = True

    os.system('cls')  #Clear the screen to stop any cheating!
    print("Thank you player 1, choice saved. Hand to player 2")

    #Righto, let's make sure Player 2 gets a fair shake too:
    ok= False
    while ok == False:
        p2 = input("OK Player 2, Choose wisely: ").lower().strip()
        if checkup(p2):
            ok = True

    os.system('cls')
    print("Great. Both choices have been safely entered. \nDrumroll please;\n")
    ok = False

    if p1 == p2:
        print("It's a tie! Everyone wins?")
    elif p1 == "rock":
        if p2 == "scissors":
            print("Rock beats Scissors; Player 1 wins!")
        else:
            print("Paper beats Rock; Player 2 wins!")
    elif p1 == "paper":
        if p2 == "scissors":
            print("Scissors beats Paper; Player 2 wins!")
        else:
            print("Paper beats Rock; Player 1 wins!")
    elif p1 == "scissors":
        if p2 == "rock":
            print("Rock beats Scissors; Player 2 wins!")
        else:
            print("Scissors beats Paper; Player 1 wins!")
    
    again = input("Play again? y/n: ").lower().strip()
    if again == "yes":
        again = "y"
    else:
        again = "n"