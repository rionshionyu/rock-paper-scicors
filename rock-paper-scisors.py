# Rion Shionyu
# Level #05 Assignment

import random
print("Welcome to Rock Paper Scissors!")

iRounds = int(input("How many rounds would you like to play: "))
while iRounds % 2 == 0:
    iRounds = int(input("Sorry, the number must be an odd number. Please try again: "))
    
def get_player_choice():
    sChoice = input("Enter rock, paper, scissors: ").lower()
    while sChoice not in ["rock", "paper", "scissors"]:
        print("Sorry, that is not a valid choice. Please try again.")
        sChoice = input("Enter rock, paper, and scissors: ").lower()
    return sChoice

# 2nd function
def determine_winner(sPlayer, sComputer):
    if sPlayer == sComputer:
        return "tie"
    elif sPlayer == "rock" and sComputer == "scissors":
        return "win"
    elif sPlayer == "paper" and sComputer == "rock":
        return "win"
    elif sPlayer == "scissors" and sComputer == "paper":
        return "win"
    else:
        return "loss"

# Count the score

iPlayerWins = 0
iComputerWins = 0
iRoundsPlayed = 0

# Game Loop
while iRoundsPlayed < iRounds:
    sPlayer = get_player_choice()
    sComputer = random.choice(["rock", "paper", "scissors"])
    print("The computer chose " + sComputer + ".")

# sResult to iRoundsPlayed need to go under the Game Loop 
    sResult = determine_winner(sPlayer, sComputer)
    if sResult == "tie":
        print("Tie! Play again.")
        continue
    elif sResult =="win":
        print("You won!")
        iPlayerWins += 1
    else:
        print("You lost!")
        iComputerWins += 1

    iRoundsPlayed += 1

print("-------------------------------------------")
print(f"Score - You: {iPlayerWins} | Computer: {iComputerWins}")

if iPlayerWins > iComputerWins:
    print("You win!!!")
else:
    print("Computer wins!!!")
print("Thanks for playing!")