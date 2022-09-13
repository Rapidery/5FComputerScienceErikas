# library to make random easier
from random import randint
# library for the pauses
from time import sleep
# colors!!!!!!!
import colorama
# where to put the colors
from colorama import Fore, Back, Style
# library for making the graphs
import pygal
# more libraries for random!
import random

# a small pause before start
sleep(4)

# set variables for the scores
PlayerWins = 0
ComputerWins = 0
Ties = 0

# sets the variables for how many times a move is done
rockcounter = 0
papercounter = 0
scissorcounter = 0

# sets the variables for logs
PlayerPastPlays = []
ComputerPastPlays = []

# sets the variables for the weight in order to make certain moves more common or less common
rockweight = 1
paperweight = 1
scissorweight = 1


# Make a list of choices, in this case "rock, paper and scissors"
t = ["Rock", "Paper", "Scissors"]

# set player to False cause its nice for making a loop so you dont have to restart code to play again
player = False

# the function in which the actual code is, its an infinite loop!
while player == False:

    # assign a random choice to the computer (robot player)
    # its paper, scissor and then rock so that if the player uses more rock,
    # paper is more likely to be chosen by the computer
    computer = random.choices(t, weights=(
        paperweight, scissorweight, rockweight,), k=1)
    print(computer)
    computer = computer[0]

    # set player to True
    # the "Fore.Cyan and Style Reset All" add some color to the text using colorama
    print(Fore.CYAN + "Rock, Paper or Scissors?" + Style.RESET_ALL)
    player = input()
    player = player.capitalize()

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
            print(Fore.RED + "You lose!", computer,
                  "covers", player + Style.RESET_ALL)
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
            print(Fore.RED + "You lose!", computer,
                  "cut", player + Style.RESET_ALL)
            ComputerWins = ComputerWins + 1
        else:
            # the "Fore.GREEN and Style Reset All" add some color to the text using colorama
            print(Fore.GREEN + "You win!", player,
                  "covers", computer + Style.RESET_ALL)
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
            print(Fore.GREEN + "You win!", player,
                  "cut", computer + Style.RESET_ALL)
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

    # counts how much of "rock, paper and scissors" are found within the variable
    for eachyoke in PlayerPastPlays:
        # if there is a rock add 1 to rock counter and the rock weight
        if eachyoke == "Rock":
            rockcounter = rockcounter + 1
            rockweight = rockweight + 1
        # if there is a paper add 1 to paper counter and the paper weight
        elif eachyoke == "Paper":
            papercounter = papercounter + 1
            paperweight = paperweight + 1
        # if there is a scissors add 1 to scissors counter and the scissors weight
        elif eachyoke == "Scissors":
            scissorcounter = scissorcounter + 1
            scissorweight = scissorweight + 1

    # Create a bar graph object
    bar_chart = pygal.Bar()
    # Adds the values
    bar_chart.add('Ties', [Ties])
    bar_chart.add('PlayerWins', [PlayerWins])
    bar_chart.add('Computerwins', [ComputerWins])
    # saves to an svg file
    bar_chart.render_to_file('score.svg')

    # Creates a bar graph object
    bar_chart = pygal.Bar()
    # adds the values
    bar_chart.title = 'Player Moves'
    bar_chart.add('Rock', [rockcounter])
    bar_chart.add('Paper',  [papercounter])
    bar_chart.add('Scissors', [scissorcounter])
    # saves to an svg file
    bar_chart.render_to_file('playermoves.svg')

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

    # resets the counter so that it doesnt "fibonacci"
    rockcounter = 0
    papercounter = 0
    scissorcounter = 0

    # resets the weight so that it doesnt "fibonacci"
    rockweight = 1
    paperweight = 1
    scissorweight = 1

    # the empty print is to add some space, but im to lazy to do it properly =)
    print("\n \n \n \n")

    # little pause before the next game
    sleep(3)

    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]
