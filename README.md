# game.py

print("Rock, Paper, Scissors, Shoot!")

from random import randint

# x = input("please choose rock, paper or scissors")
# print(x)

t = ["rock", "paper", "scissors"]

computer = t[randint(0,2)]

player = False

while player == False:

    player = input("rock, paper, scissors?")
    if player == computer:
        print ("Tie")
    elif player == "rock":
        if computer == "paper":
           print ("LOSER", computer, "DOMINATED", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
      


    player = False
    computer = t[randint(0,2)]

# from random import randint

# #create a list of play options
# t = ["Rock", "Paper", "Scissors"]

# #assign a random play to the computer
# computer = t[randint(0,2)]

# #set player to False
# player = False

# while player == False:
# #set player to True
#     player = input("Rock, Paper, Scissors?")
#     if player == computer:
#         print("Tie!")
#     elif player == "Rock":
#         if computer == "Paper":
#             print("You lose!", computer, "covers", player)
#         else:
#             print("You win!", player, "smashes", computer)
#     elif player == "Paper":
#         if computer == "Scissors":
#             print("You lose!", computer, "cut", player)
#         else:
#             print("You win!", player, "covers", computer)
#     elif player == "Scissors":
#         if computer == "Rock":
#             print("You lose...", computer, "smashes", player)
#         else:
#             print("You win!", player, "cut", computer)
#     else:
#         print("That's not a valid play. Check your spelling!")
#     #player was set to True, but we want it to be False so the loop continues
#     player = False
#     computer = t[randint(0,2)]
