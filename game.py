

print("Rock, Paper, Scissors, Shoot!")

from random import randint 

choix=["Rock", "Paper", "Scissors"]

computer = choix[randint(0,2)]

print(computer)

player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print ("Tie")
    elif player == "Rock":
        if computer == "Paper":
           print ("LOSER", computer, "DOMINATED", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

player = False
computer = choix[randint(0,2)]