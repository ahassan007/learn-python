# Challenge i need enter py guess_number.py -n "Dave"
# Next it should display Dave, guess which number I'm thinking of... 1,2, or 3
# If you win it shows the results, add option to try again or quite and also inculde winning %

import sys
import random
def gn(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_gn():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        playerchoice = input(f"\n{name}, guess which number I'm thinking of... 1,2, or 3\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name} please enter 1,2, or 3")
            return play_gn()
        
        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print( f"\n{name}, you chose {str(player)}.")
        print( f"\nI was thinking about the number {str(computer)}.")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins

            if player == computer:
                player_wins += 1
                return f"\nWell done {name}, you win!!"
            else: 
                computer_wins += 1
                return f"\nSorry, {name}. Better luck next time."
        
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        game_percentage = "{:.2%}".format(player_wins/game_count)

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {game_percentage}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            return play_gn()
        else:
            print("\n🥳🎊🥳🎊🥳")
            print("Thank you for playing!\n")
            return
    return play_gn

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description= "Prvide a personalized game experince"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    args = parser.parse_args()

    guess_number = gn(args.name)
    guess_number()
   


