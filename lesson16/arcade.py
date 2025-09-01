from guess_number import gn
from rps import rps
import sys


def arcade(name='PlayerOne'):
    welcome_back = False


    while True: 
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playergamechoice = input(f"\n Please choose a game:\n 1 = Rock Paper Scissors\n 2 = Guess My Number\n\n or press " + "x" + " to exit the Arcade\n\n")

        if playergamechoice not in ["1", "2", "x"]:
            print(f"{name} please enter 1, 2 or x")
            return arcade()
        
        welcome_back = True
        

        if playergamechoice == "x":
            print("Goodbye")
            break

        def decide_game(game):
            nonlocal name

            if game == "1":
                rock_paper_scissors = rps(name)
                rock_paper_scissors()
            elif game == "2":
                guess_game = gn(name)
                guess_game()
            else:
                print("\nSee you next time!\n")
                sys.exit(f"Bye {name}! 👋")

        
        decide_game(playergamechoice)

        print(playergamechoice)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description= "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    args = parser.parse_args()

    arcade(args.name)

    