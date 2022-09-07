# Import the randint, sleep and colorama library
from random import randint
from time import sleep
import colorama
from colorama import Fore, Back, Style

# a small pause before start
sleep(4)

# set variables for the scores
PlayerWins = 0
ComputerWins = 0
Ties = 0

# sets the variables for logs
PlayerPastPlays = []
ComputerPastPlays = []


# Make a list of choices, in this case "rock, paper and scissors"
t = ["Rock", "Paper", "Scissors"]

# assign a random choice to the computer (robot player)
computer = t[randint(0, 2)]

# set player to False cause its nice for making a loop so you dont have to restart code to play again
player = False

# the function in which the actual code is, its an infinite loop!
while player == False:
    # set player to True
    # the "Fore.Cyan and Style Reset All" add some color to the text using colorama
    print(Fore.CYAN + "Rock, Paper or Scissors?" + Style.RESET_ALL)
    player = input()

    # just a break so its not instant
    sleep(2)

    # "if the player is equal to the PC print the word Tie"
    if player == computer:
        # the "Fore.RED and Style Reset All" add some color to the text using colorama
        print(Fore.RED + "Tie!" + Style.RESET_ALL)
        Ties = Ties + 1

    # if the player chose rock and the pc chose paper, print loss
    # if the player chose rock and the pc chose anything else, print win
    elif player == "Rock":
        if computer == "Paper":
            # the "Fore.RED and Style Reset All" add some color to the text using colorama
            print(Fore.RED + "You lose!", computer, "covers", player + Style.RESET_ALL)
            ComputerWins = ComputerWins + 1
        else:
            # the "Fore.GREEN and Style Reset All" add some color to the text using colorama
            print(
                Fore.GREEN + "You win!", player, "smashes", computer + Style.RESET_ALL
            )
            PlayerWins = PlayerWins + 1

    # if the player chose paper and the pc chose scissors, print loss
    # if the player chose paper and the pc chose anything else, print win
    elif player == "Paper":
        if computer == "Scissors":
            # the "Fore.RED and Style Reset All" add some color to the text using colorama
            print(Fore.RED + "You lose!", computer, "cut", player + Style.RESET_ALL)
            ComputerWins = ComputerWins + 1
        else:
            # the "Fore.GREEN and Style Reset All" add some color to the text using colorama
            print(Fore.GREEN + "You win!", player, "covers", computer + Style.RESET_ALL)
            PlayerWins = PlayerWins + 1

    # if the player chose scissors and the pc chose rock, print loss
    # if the player chose scissors and the pc chose anything else, print win
    elif player == "Scissors":
        if computer == "Rock":
            # the "Fore.RED and Style Reset All" add some color to the text using colorama
            print(
                Fore.RED + "You lose...", computer, "smashes", player + Style.RESET_ALL
            )
            ComputerWins = ComputerWins + 1
        else:
            # the "Fore.GREEN and Style Reset All" add some color to the text using colorama
            print(Fore.GREEN + "You win!", player, "cut", computer + Style.RESET_ALL)
            PlayerWins = PlayerWins + 1

    # if the input doesnt work at all it prints a fallback message
    # and restarts the game
    else:
        # the "Fore.RED and Style Reset All" add some color to the text using colorama
        print(
            Fore.RED
            + "That's not a valid play. Check your spelling... or are you...TRYING TO CHEAT?!?!?!?!?!"
            + Style.RESET_ALL
        )

    # Variables needed to print the log
    PlayerPastPlays.append(player)
    ComputerPastPlays.append(computer)

    # just a print that shows a move log and gives the text some color (player)
    print(Fore.MAGENTA + "Player Move Log:", PlayerPastPlays)
    # just a print that shows a move log and gives the text some color (player)
    print(Fore.YELLOW + "Computer Move Log:", ComputerPastPlays)

    # sets the color and adds a break
    print(Fore.CYAN + " ")
    # prints the amount of ties
    print(Ties, " ties")
    # prints the amount of wins
    print(PlayerWins, " wins")
    # prints the amount of losses
    print(ComputerWins, " losses")

    # the empty print is to add some space, but im to lazy to do it properly =)
    print("  ")
    print("  ")
    print("  ")
    print("  ")

    # little pause before the next game
    sleep(3)

    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]
