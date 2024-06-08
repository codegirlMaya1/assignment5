#Objective: The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.

# random integer
from random import randint

# list for weapon
WEAPON = ["Rock", "Paper", "Scissors"]
Options = {"Rock":{"Win":'Scissors', "Loss":"Paper", "Adj":"Smashes"},
        "Paper":{"Win":"Rock", "Loss":"Scissors", "Adj":"Covers"},
        "Scissors":{"Win":"Paper", "Loss":"Rock", "Adj":'Cuts'}}

def have_won(player, computer):
    #determines if the players choice has beaten the computers
    if Options[player]["Win"] == computer:
        adj = Options[player]['Adj']
        return True, ' '.join([player, adj, computer])
    else:
        adj = Options[computer]['Adj']
        return False, ' '.join([computer, adj, player])

# one player mode
def onePlayer():
    scoreP = 0
    scoreC = 0
    again = ""
    player = False

    print("---------------------------------------------")
    print("\n\tYou VS Boredom")

    while player == False:
        print("Play: Rock, Paper, Scissors: Choose your first option")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        player = input("\nEnter a given number: ")
        if player == "quit" or player == "q" or player == "4":
            player = True
        else:
            try:
                player = int(player)
                if player == 1:
                    player = WEAPON[0]
                elif player == 2:
                    player = WEAPON[1]
                elif player == 3:
                    player = WEAPON[2]
            except:
                print("please enter a number 1 through 4\n")

        computer = WEAPON[randint(0,2)]
        print (player, computer)
        outcome = have_won(player, computer)
        if player == computer:
            print(player," vs ",computer)
            print("It's a tie!\n")
            print("Player:",scoreP,"\nComputer:",scoreC)
            print("")

        elif outcome[0] == True:
            print(outcome[1]+"! You Win!!")
            scoreP += 1
        elif outcome[0] == False:
            print(outcome[1]+"! You Lose!!")
            scoreC += 1
        #else:
        #    print("Please select a valid play option\n")
        print("Player:",scoreP,"\nComputer:",scoreC)
        player = False
onePlayer()