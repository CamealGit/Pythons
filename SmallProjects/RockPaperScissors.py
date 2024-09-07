import random

print("Welcome to Rock Paper Scissors game!")

games = int(input("How many games u wanna play ? "))
NumberOfGames = 0
YourScore = 0
ComputerScore = 0
while NumberOfGames != games:
    compChoice = ["rock", "paper", "scissors"]
    number = random.randint(0, 2)
    computerChoice = compChoice[number - 1]
    yourChoice = input("Rock / Paper / Scissors? ").lower()
    if yourChoice == "rock" and computerChoice == "scissors":
        print("You Won")
        YourScore += 1
    elif yourChoice == "paper" and computerChoice == "rock":
        print("You Won")
        YourScore += 1
    elif yourChoice == "scissors" and computerChoice == "paper":
        print("You Won")
        YourScore += 1
    else:
        print("You Lost")
        ComputerScore += 1
    NumberOfGames += 1

    print(f"Your current score is {YourScore}")
    print(f"Computer current score is {ComputerScore}")
    print("--------------------------")

if YourScore > ComputerScore:
        print("You Won!")
elif YourScore == ComputerScore:
        print("Draw!")
elif YourScore < ComputerScore:
        print("You Lost!")
