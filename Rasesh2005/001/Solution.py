import random

'''GLOBAL VARIABLES'''
choices=["stone","paper","scissor"]

# Making A Dictionary where Key Kills Value
gameDict={'stone':'scissor','scissor':'paper','paper':'stone'}

def choose():
    return random.choice(choices)

def take_choice():
    choice=input("Enter your choice: ").lower()
    if choice in choices:
        return choice
    print("Invalid Choice, Choose one out of Stone,Paper or Scissor")
    return take_choice()
def tieGame():
    compChoice=userChoice='stone'
    while(compChoice==userChoice):
        compChoice=choose()
        userChoice=take_choice()
        if compChoice==userChoice:
            print("It is a TIE, Play Again")
        elif gameDict[compChoice]==userChoice:
            print("Sorry,You LOST!!")
        else:
            print("Bravo!! You WON !!")

def playGame():
    gamesLeft=15
    compScore=0
    playerScore=0
    while gamesLeft:
        compChoice=choose()
        userChoice=take_choice()
        print(f'\nYour Choice: {userChoice}\nComputer\'s Choice {compChoice}')
        if compChoice==userChoice:
            print("It is a TIE !")
        elif gameDict[compChoice]==userChoice:
            print("Computer Got 1 point !!")
            compScore+=1
        else:
            print("You Got 1 point !!")
            playerScore+=1
        gamesLeft-=1
        print(f'Your Score: {playerScore}\nComputer\'s Score: {compScore}')
    if compScore>playerScore:
        print('\n\n\nSorry, You LOST.\n\n\n')
    elif playerScore>compScore:
        print('\n\n\nBravo! You WON..\n\n\n')
    else:
        print('\n\n\nIts a TIE, Tie Breaker Starts,\n Play until one of the players Win: \n\n\n')
        tieGame()

if __name__ == "__main__":
    playGame()
