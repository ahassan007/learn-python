import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:

    print(" ")

    playerchoice = input('Enter .. \n1 for Rock, \n2 for paper, or \n3 for scissors:\n\n')

    player = int(playerchoice)

    if player < 1 or player  > 3:
        sys.exit('You must enter 1,2, or 3.')

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print( "You chose " + str(RPS(player)).replace('RPS.', '') + '.')
    print( 'Python chose ' + str(RPS(computer)).replace('RPS.', '')  + '.')

    if player == 1 and computer == 3:
        print('🥳 You win!!')
    elif player == 2 and computer == 1:
        print('🥳 You win!!')
    elif player == 3 and computer == 2:
        print('🥳 You win!!')
    elif player == computer:
        print('😮 Tie')
    else:
        print('🐍 Python wins!!')
    
    playagain = input("\nPlay again? \nY for Yes or \nQ to Quite \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🥳🎊🥳🎊🥳")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye! ")





